#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_template.py - mirror project-template/ into init-project/assets/project-template/

Keep the two copies identical: project-template/ is the master (human-readable),
init-project/assets/project-template/ is what the init-project skill ships.
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

ROOT = Path(__file__).resolve().parent.parent  # scripts/ 的上一级 = 工作区根
SRC = ROOT / "project-template"
DST = ROOT / "init-project" / "assets" / "project-template"
SKILL_MD = ROOT / "init-project" / "SKILL.md"
AGENT_RULES_DIR = ROOT / "agent-rules"
AGENT_RULES_SKILL_MD = AGENT_RULES_DIR / "SKILL.md"
INHERITANCE_MAP = AGENT_RULES_DIR / "references" / "inheritance-map.md"
SKIP_NAMES = {".git", "__pycache__", ".DS_Store", "Thumbs.db"}


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
        if p.is_file() and not any(part in SKIP_NAMES for part in p.parts)
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


def main() -> int:
    _configure_utf8()
    if not SRC.is_dir():
        print(f"[error] template source not found: {SRC}", file=sys.stderr)
        return 1
    if not (ROOT / "init-project" / "SKILL.md").exists():
        print(f"[error] skill folder not found under {ROOT}", file=sys.stderr)
        return 1

    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST, ignore=shutil.ignore_patterns(*SKIP_NAMES))

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
    for s, d in zip(src_files, dst_files):
        if _sha256(s) != _sha256(d):
            problems.append(f"content differs: {s.relative_to(SRC)}")

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

    _check_agent_rules(tpl_version, problems)

    if problems:
        print("[error] sync verification failed:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print(
        f"synced and verified {len(rel_src)} files: {SRC} -> {DST} "
        f"(template_version={tpl_version}, init-project metadata.version={skill_version}, "
        f"agent-rules verified)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
