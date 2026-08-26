#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ci_check.py - project check entry (shared by local and CI; see .github/workflows/ci.yml)

Purpose: idempotent, repeatable lint / build / test entry.
The template ships only a basic whitespace check; replace/extend with real checks
and remove the PLACEHOLDER_MARKER line (pre_release_check.py refuses to pass while
the marker is present, unless --allow-placeholder is used).
Usage: python scripts/ci_check.py
Exit code: 0 pass; non-zero fail (CI and pre-release both rely on this).

NOTE: stdlib-only, Python 3.9+; the repo root is resolved from this script's
      location (the parent of scripts/), so it can be run from any working dir.
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_MARKER = "__CI_CHECK_PLACEHOLDER__"


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


def _run(cmd: list) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def main() -> int:
    _configure_utf8()
    if not (REPO_ROOT / ".git").exists():
        print(f"[error] not a git repo root (no .git): {REPO_ROOT}", file=sys.stderr)
        return 1

    print("==> ci-check: basic check (git whitespace errors)")
    for staged in (False, True):
        cmd = ["git", "diff", "--check"]
        if staged:
            cmd.append("--cached")
        r = _run(cmd)
        if r.returncode != 0:
            label = "staged" if staged else "unstaged"
            print(
                f"[error] whitespace check failed ({label}):\n{r.stdout}{r.stderr}",
                file=sys.stderr,
            )
            return 1

    print("==> ci-check: pre-development doc registers (PRD/RFC/ADR/RESEARCH)")
    # 模板自带：校验开发前文档登记册（编号/状态机/索引一致性），建议保留。
    r = _run([sys.executable, "scripts/check_dev_docs.py"])
    if r.returncode != 0:
        print(r.stdout, end="", file=sys.stderr)
        print(r.stderr, end="", file=sys.stderr)
        print("[error] check_dev_docs.py failed", file=sys.stderr)
        return 1

    print("==> ci-check: TODO - implement lint / build / test for this project")
    print("    Node example: npm ci; npm run build; npm test")
    print("    Python example: python -m pytest")
    print("    Rust example: cargo check --all-targets; cargo test")
    print("    After implementing real checks, remove the PLACEHOLDER_MARKER line")
    print("    and update the check table in private/dev/TEST-REPORT.md.")
    print("    Guide: docs/TESTING.md (pytest setup, coverage, CI integration).")
    # Python 项目接入示例（创建 tests/ 后取消注释并移除 PLACEHOLDER_MARKER）：
    # r = _run([sys.executable, "-m", "pytest"])
    # if r.returncode != 0:
    #     print("[error] pytest failed", file=sys.stderr)
    #     return 1

    print("==> ci-check: passed (template placeholder)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
