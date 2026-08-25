#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_template.py - mirror project-template/ into init-project/assets/project-template/

Keep the two copies identical: project-template/ is the master (human-readable),
init-project/assets/project-template/ is what the init-project skill ships.
Also verifies init-project/SKILL.md metadata.version matches project-template/version.json
template_version (single source of truth for the template version).
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


def _skill_metadata_version() -> str:
    """Read metadata.version from init-project/SKILL.md frontmatter."""
    content = SKILL_MD.read_text(encoding="utf-8")
    m = re.search(r"(?m)^metadata:\s*$", content)
    if not m:
        return ""
    m2 = re.search(r"(?m)^\s+version:\s*([0-9A-Za-z.\-]+)\s*$", content[m.end():])
    return m2.group(1) if m2 else ""


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
    skill_version = _skill_metadata_version()
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

    if problems:
        print("[error] sync verification failed:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print(
        f"synced and verified {len(rel_src)} files: {SRC} -> {DST} "
        f"(template_version={tpl_version}, SKILL.md metadata.version={skill_version})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
