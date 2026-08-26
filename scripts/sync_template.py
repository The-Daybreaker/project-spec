#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_template.py - mirror project-template/ into skills/init-project/assets/project-template/

Keep the two copies identical: project-template/ is the master (human-readable),
skills/init-project/assets/project-template/ is what the init-project skill ships.
Also verifies init-project/SKILL.md metadata.version matches project-template/version.json
template_version (single source of truth for the template version), and verifies the
agent-rules skill (lite global agent rules derived from the template):
  - agent-rules/SKILL.md metadata.version == template_version;
  - references/inheritance-map.md version table == template_version;
  - inheritance-map red-line coverage: every template red line is mapped, no obsolete rows;
  - red-line body fingerprints: template red line text changed without updating the map
    (forces re-review of the lite skill before the template can be released).
Run this after ANY change under project-template/ or init-project/ (or before packaging the skill).
Usage: python scripts/sync_template.py
Exit code: 0 synced and verified; 1 failure.
"""

import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

from verify_installed_copies import check_installed_copies

ROOT = Path(__file__).resolve().parent.parent  # scripts/ 的上一级 = 工作区根
SRC = ROOT / "project-template"
DST = ROOT / "skills" / "init-project" / "assets" / "project-template"
SKILL_MD = ROOT / "skills" / "init-project" / "SKILL.md"
AGENT_RULES_DIR = ROOT / "skills" / "agent-rules"
AGENT_RULES_SKILL_MD = AGENT_RULES_DIR / "SKILL.md"
INHERITANCE_MAP = AGENT_RULES_DIR / "references" / "inheritance-map.md"
INIT_STEPS = ROOT / "skills" / "init-project" / "references" / "init-steps.md"
SKIP_NAMES = {".git", "__pycache__", ".DS_Store", "Thumbs.db"}

# 初始化流程必须覆盖的模板关键文件：模板新增/变更这类文件后，必须同步
# init-steps.md（校验清单 / 常见问题 / 落地路线图），否则 sync 失败——
# 防止「改模板只同步资产镜像、不同步 skill 承载文档」。
# 维护：按需增删；新增模板文件若属「初始化流程关键项」，加入本清单并同步 init-steps.md。
INIT_STEPS_COVERAGE = [
    "AGENTS.md",
    "private/AGENTS.md",
    "README.md",
    "version.json",
    "archive/ARCHIVE.md",
    "dist/.gitkeep",
    "docs/TESTING.md",
    "docs/audit-checklist.md",
    "docs/UPGRADE.md",
    "scripts/ci_check.py",
    "scripts/pre_release_check.py",
    "scripts/trash.py",
    "scripts/bump_version.py",
    "private/dev/WORKLOG.md",
    "private/dev/CHANGELOG.md",
    "private/dev/TEST-REPORT.md",
    "private/dev/EXPERIENCE-TO-KB.md",
    "private/dev/EXPERIENCE-TO-TEMPLATE.md",
    "private/dev/DESIGN.md",
    "private/dev/prd/INDEX.md",
    "private/dev/rfc/INDEX.md",
    "private/dev/adr/INDEX.md",
    "private/dev/research/INDEX.md",
    "scripts/check_dev_docs.py",
    "private/dev/prototype/README.md",
]


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _collect(root: Path) -> list:
    return sorted(
        p
        for p in root.rglob("*")
        if p.is_file()
        and not any(part in SKIP_NAMES for part in p.relative_to(root).parts)
    )


def _template_version() -> str:
    """Read template_version from project-template/version.json (authoritative)."""
    data = json.loads((SRC / "version.json").read_text(encoding="utf-8"))
    return str(data.get("template_version", ""))


def _skill_metadata_version(path: Path) -> str:
    """Read metadata.version from a SKILL.md frontmatter."""
    content = path.read_text(encoding="utf-8")
    m = re.search(r"(?m)^metadata:\s*$", content)
    if not m:
        return ""
    m2 = re.search(r"(?m)^\s+version:\s*([0-9A-Za-z.\-]+)\s*$", content[m.end():])
    return m2.group(1) if m2 else ""


def _extract_redlines(text: str) -> dict:
    """Extract the numbered red lines from project-template/AGENTS.md '通用红线' section.

    Returns {number: normalized_text}. A bullet may wrap across lines; whitespace is
    normalized so fingerprints are stable against formatting-only changes.
    """
    m = re.search(r"## 【通用】通用红线（Agent 开发，强制）(.*?)(?=\n## )", text, re.S)
    if not m:
        return {}
    items = re.findall(r"(?m)^(\d+)\.\s+(.*?)(?=^\d+\.\s+|\Z)", m.group(1), re.S)
    result = {}
    for num, body in items:
        result[int(num)] = re.sub(r"\s+", " ", body).strip()
    return result


def _parse_inheritance_map(text: str) -> tuple:
    """Parse agent-rules inheritance-map.md.

    Returns (version_table: dict, redline_rows: {number: {"entry", "mode", "fingerprint"}}).
    """
    version_table = {}
    vm = re.search(r"\|\s*模板\s+`template_version`（权威）\s*\|\s*([0-9A-Za-z.\-]+)\s*\|", text)
    if vm:
        version_table["template_version"] = vm.group(1)
    vm2 = re.search(r"\|\s*`\.\./SKILL\.md`\s+`metadata\.version`\s*\|\s*([0-9A-Za-z.\-]+)\s*\|", text)
    if vm2:
        version_table["skill_version"] = vm2.group(1)

    rows = {}
    for m in re.finditer(
        r"\|\s*红线 (\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(原样|通用化)\s*\|\s*([0-9a-f]+)\s*\|",
        text,
    ):
        rows[int(m.group(1))] = {
            "topic": m.group(2).strip(),
            "entry": m.group(3).strip(),
            "mode": m.group(4),
            "fingerprint": m.group(5),
        }
    return version_table, rows


def _check_agent_rules(tpl_version: str, problems: list) -> None:
    """Verify agent-rules lite skill stays in sync with the template."""
    if not AGENT_RULES_DIR.is_dir():
        problems.append(f"agent-rules skill not found: {AGENT_RULES_DIR}")
        return
    if not AGENT_RULES_SKILL_MD.is_file():
        problems.append(f"agent-rules/SKILL.md not found: {AGENT_RULES_SKILL_MD}")
        return
    if not INHERITANCE_MAP.is_file():
        problems.append(f"inheritance-map not found: {INHERITANCE_MAP}")
        return

    # 1. metadata.version consistency
    skill_version = _skill_metadata_version(AGENT_RULES_SKILL_MD)
    if not skill_version:
        problems.append("cannot read agent-rules/SKILL.md metadata.version")
    elif skill_version != tpl_version:
        problems.append(
            f"agent-rules version mismatch: SKILL.md metadata.version={skill_version}, "
            f"template_version={tpl_version}"
        )

    # 2. inheritance-map version table consistency
    version_table, rows = _parse_inheritance_map(
        INHERITANCE_MAP.read_text(encoding="utf-8")
    )
    if version_table.get("template_version") != tpl_version:
        problems.append(
            "inheritance-map template_version mismatch: "
            f"map={version_table.get('template_version')!r}, expected={tpl_version!r}"
        )
    if version_table.get("skill_version") != tpl_version:
        problems.append(
            "inheritance-map skill metadata.version mismatch: "
            f"map={version_table.get('skill_version')!r}, expected={tpl_version!r}"
        )

    # 3. red-line coverage + body fingerprints
    redlines = _extract_redlines((SRC / "AGENTS.md").read_text(encoding="utf-8"))
    if not redlines:
        problems.append("cannot find '通用红线' section in project-template/AGENTS.md")
        return
    for num in sorted(redlines):
        if num not in rows:
            problems.append(
                f"inheritance-map missing mapping for 红线 {num}: "
                f"review agent-rules/SKILL.md and add the row"
            )
            continue
        fp = hashlib.sha256(redlines[num].encode("utf-8")).hexdigest()[:12]
        if rows[num]["fingerprint"] != fp:
            problems.append(
                f"红线 {num} body changed (fingerprint {rows[num]['fingerprint']} -> {fp}): "
                f"re-review agent-rules/SKILL.md entry and update inheritance-map fingerprint"
            )
    for num in sorted(rows):
        if num not in redlines:
            problems.append(f"inheritance-map has obsolete mapping for 红线 {num}")


def _check_init_steps_coverage(problems: list) -> None:
    """Verify init-steps.md covers the key template files of the init flow."""
    if not INIT_STEPS.is_file():
        problems.append(f"init-steps not found: {INIT_STEPS}")
        return
    text = INIT_STEPS.read_text(encoding="utf-8")
    missing = [k for k in INIT_STEPS_COVERAGE if k not in text]
    if missing:
        problems.append(
            "init-steps.md missing coverage for template key file(s): "
            f"{missing} (add to init-steps.md 校验清单/常见问题/落地路线图; "
            "if not init-flow-critical, remove from INIT_STEPS_COVERAGE in sync_template.py)"
        )


def main() -> int:
    _configure_utf8()
    if not SRC.is_dir():
        print(f"[error] template source not found: {SRC}", file=sys.stderr)
        return 1
    if not (ROOT / "skills" / "init-project" / "SKILL.md").exists():
        print(f"[error] skill folder not found under {ROOT}", file=sys.stderr)
        return 1

    try:
        if DST.exists():
            shutil.rmtree(DST)
        shutil.copytree(SRC, DST, ignore=shutil.ignore_patterns(*SKIP_NAMES))
    except OSError as e:
        print(
            f"[error] failed to mirror {SRC} -> {DST}: {e} "
            "(partial mirror left for inspection; replaced on the next successful run)",
            file=sys.stderr,
        )
        return 1

    src_files = _collect(SRC)
    dst_files = _collect(DST)
    rel_src = [p.relative_to(SRC).as_posix() for p in src_files]
    rel_dst = [p.relative_to(DST).as_posix() for p in dst_files]

    problems = []
    if rel_src != rel_dst:
        problems.append(
            "file lists differ: "
            f"src-only={sorted(set(rel_src) - set(rel_dst))} "
            f"dst-only={sorted(set(rel_dst) - set(rel_src))}"
        )
    src_by_rel = {p.relative_to(SRC).as_posix(): p for p in src_files}
    dst_by_rel = {p.relative_to(DST).as_posix(): p for p in dst_files}
    for rel in sorted(set(rel_src) & set(rel_dst)):
        if _sha256(src_by_rel[rel]) != _sha256(dst_by_rel[rel]):
            problems.append(f"content differs: {rel}")

    tpl_version = _template_version()
    skill_version = _skill_metadata_version(SKILL_MD)
    if not tpl_version or not skill_version:
        problems.append(
            f"cannot read versions (template_version={tpl_version!r}, "
            f"SKILL.md metadata.version={skill_version!r})"
        )
    elif tpl_version != skill_version:
        problems.append(
            f"version mismatch: project-template/version.json template_version="
            f"{tpl_version}, init-project/SKILL.md metadata.version={skill_version}"
        )

    root_version_file = ROOT / "version.json"
    if not root_version_file.is_file():
        problems.append(f"workspace root version.json missing: {root_version_file}")
    else:
        try:
            root_data = json.loads(root_version_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            problems.append(f"cannot read workspace root version.json: {e}")
        else:
            root_version = str(root_data.get("version", ""))
            root_tpl = str(root_data.get("template_version", ""))
            if root_version != tpl_version:
                problems.append(
                    f"workspace root version.json version mismatch: "
                    f"root={root_version!r}, template_version={tpl_version!r}"
                )
            if root_tpl != tpl_version:
                problems.append(
                    f"workspace root version.json template_version mismatch: "
                    f"root={root_tpl!r}, template={tpl_version!r}"
                )

    _check_agent_rules(tpl_version, problems)
    _check_init_steps_coverage(problems)
    check_installed_copies(problems)

    if problems:
        print("[error] sync verification failed:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print(
        f"synced and verified {len(rel_src)} files: {SRC} -> {DST} "
        f"(template_version={tpl_version}, init-project metadata.version={skill_version}, "
        f"agent-rules verified, init-steps coverage verified, installed copies verified)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
