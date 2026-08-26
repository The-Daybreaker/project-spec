#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_installed_copies.py - verify agent skill installs across targets

Machine-readable install table (install-targets.json) is the single source of
truth for where agent-rules / init-project are installed on this machine.
This script reads the table and, for every target x skill, compares the full
file tree (SHA-256) and the SKILL.md metadata.version sentinel against the
workspace sources. It is also invoked by sync_template.py, so the release
verification chain fails (exit 1) whenever any installed copy is missing or
stale - the install step becomes mandatory and cannot silently drift.
Usage: python scripts/verify_installed_copies.py
Exit code: 0 all installed copies verified; 1 missing/stale/inconsistent.
"""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # scripts/ 的上一级 = 工作区根
CONFIG = ROOT / "install-targets.json"
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
        if p.is_file()
        and not any(part in SKIP_NAMES for part in p.relative_to(root).parts)
    )


def _file_map(root: Path) -> dict:
    return {p.relative_to(root).as_posix(): p for p in _collect(root)}


def _skill_metadata_version(path: Path) -> str:
    """Read metadata.version from a SKILL.md frontmatter."""
    import re

    try:
        content = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return ""
    m = re.search(r"(?m)^metadata:\s*$", content)
    if not m:
        return ""
    m2 = re.search(r"(?m)^\s+version:\s*([0-9A-Za-z.\-]+)\s*$", content[m.end():])
    return m2.group(1) if m2 else ""


def _check_skill(skill_dir: Path, src_map: dict, src_version: str, label: str,
                 problems: list) -> None:
    missing = []
    if not skill_dir.is_dir():
        problems.append(f"[{label}] skill dir missing: {skill_dir}")
        return
    inst_map = _file_map(skill_dir)
    rels = sorted(set(src_map) | set(inst_map))
    for rel in rels:
        if rel not in src_map:
            missing.append(f"unexpected file: {rel}")
        elif rel not in inst_map:
            missing.append(f"missing file: {rel}")
        elif _sha256(src_map[rel]) != _sha256(inst_map[rel]):
            missing.append(f"content differs: {rel}")
    if missing:
        problems.append(f"[{label}] {len(missing)} file problem(s): {missing}")
    inst_version = _skill_metadata_version(skill_dir / "SKILL.md")
    if not inst_version:
        problems.append(f"[{label}] cannot read installed SKILL.md metadata.version")
    elif inst_version != src_version:
        problems.append(
            f"[{label}] version sentinel mismatch: installed={inst_version!r}, "
            f"source={src_version!r}"
        )


def check_installed_copies(problems: list, config_path: Path = CONFIG,
                           root: Path = ROOT) -> None:
    """Append installed-copy verification problems (used by sync_template.py)."""
    if not config_path.is_file():
        problems.append(f"install-targets.json missing: {config_path}")
        return
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        problems.append(f"cannot read install-targets.json: {e}")
        return

    skills = data.get("skills") or []
    targets = data.get("targets") or []
    if not skills or not targets:
        problems.append(f"install-targets.json empty skills/targets: {config_path}")

    for skill in skills:
        name = skill.get("name")
        source = skill.get("source")
        if not name or not source:
            problems.append(f"install-targets.json bad skill entry: {skill}")
            continue
        src_dir = root / source
        if not src_dir.is_dir():
            problems.append(f"skill source dir missing: {src_dir}")
            continue
        src_map = _file_map(src_dir)
        src_skill_md = src_dir / "SKILL.md"
        src_version = (_skill_metadata_version(src_skill_md)
                       if src_skill_md.is_file() else "")

        for target in targets:
            tid = target.get("id")
            tdir = target.get("dir")
            if not tid or not tdir:
                problems.append(f"install-targets.json bad target entry: {target}")
                continue
            label = f"{tid}/{name}"
            skill_dir = Path(tdir).expanduser() / name
            _check_skill(skill_dir, src_map, src_version, label, problems)


def main() -> int:
    _configure_utf8()
    problems = []
    check_installed_copies(problems)
    if problems:
        print("[error] installed copies verification failed:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())