#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_template.py - mirror project-template/ into init-project/assets/project-template/

Keep the two copies identical: project-template/ is the master (human-readable),
init-project/assets/project-template/ is what the init-project skill ships.
Run this after ANY change under project-template/ (or before packaging the skill).
Usage: python sync_template.py
Exit code: 0 synced and verified; 1 failure.
"""

import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "project-template"
DST = ROOT / "init-project" / "assets" / "project-template"
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
    if problems:
        print("[error] sync verification failed:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print(f"synced and verified {len(rel_src)} files: {SRC} -> {DST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
