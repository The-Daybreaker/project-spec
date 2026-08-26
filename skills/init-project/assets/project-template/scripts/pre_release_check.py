#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pre_release_check.py - pre-release checks (markdown-driven, script-assisted)

Usage:
  python scripts/pre_release_check.py [--version X.Y.Z] [--description "desc"]
      [--skip-subgit] [--allow-placeholder]

Behavior:
  1) private sub-git: if it has changes -> auto add + commit
     ("docs: private vX.Y.Z - desc") and confirm it is clean
     (required before every release; see root AGENTS.md release flow);
  2) main repo status: list uncommitted changes (the agent commits them, not this
     script); safety scan: no private/ path or gitlink may enter the main repo
     index/working tree, no secret-named files;
  3) version consistency: version.json 'version' vs top of CHANGELOG;
  4) ci_check.py must be implemented (no template placeholder), unless
     --allow-placeholder is given;
  5) print audit & release reminders.
Exit code: 0 all ready; 1 issues must be fixed first.

NOTE: stdlib-only, Python 3.9+; the repo root is resolved from this script's
      location (the parent of scripts/), so it can be run from any working dir.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SECRET_NAME_RE = re.compile(
    r"(?:^|[\\/])(?:\.env(?:[.\-]|$)|[^\\/]*\.(?:key|pem|pfx|p12)$|"
    r"(?:secret|credential|api[-_. ]?key|private[-_. ]?key)(?:[.\-_]|$))",
    re.IGNORECASE,
)


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


def _run(args: list, check: bool = False) -> subprocess.CompletedProcess:
    r = subprocess.run(
        args,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and r.returncode != 0:
        raise RuntimeError(
            f"command failed: {' '.join(args)}\n{r.stdout}{r.stderr}"
        )
    return r


def _is_private_path(p: str) -> bool:
    p = p.strip('"')
    return p == "private" or p.startswith("private/") or p.startswith("private\\")


def _read_text(path: Path) -> str:
    """Read a file as UTF-8; on decode/IO failure print and return ""."""
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
        print(f"[error] cannot read {path.relative_to(REPO_ROOT)}: {e}", file=sys.stderr)
        return ""


MARKER_ASSIGN_RE = re.compile(
    r'^\s*PLACEHOLDER_MARKER\s*=\s*"__CI_CHECK_PLACEHOLDER__"\s*$', re.MULTILINE
)


def _ci_check_state(text: str) -> str:
    """双向断言 ci_check.py 占位状态：占位常量（PLACEHOLDER_MARKER 赋值行）与
    占位实现（template placeholder 输出）必须成对出现，任一单边残留都视为
    改造不完整。Return "placeholder" | "inconsistent" | "stale_constant" | "implemented".
    """
    has_marker = MARKER_ASSIGN_RE.search(text) is not None
    has_body = "template placeholder" in text
    if has_marker and has_body:
        return "placeholder"
    if has_body:
        return "inconsistent"
    if has_marker:
        return "stale_constant"
    return "implemented"


def _status_paths() -> list:
    """Parse `git status --porcelain` into (status, path) pairs (handles renames)."""
    r = _run(["git", "-c", "core.quotepath=false", "status", "--porcelain"])
    pairs = []
    for line in r.stdout.splitlines():
        if len(line) < 4:
            continue
        status, path = line[:2], line[3:]
        if " -> " in path:
            old, new = path.split(" -> ", 1)
            pairs.append((status, old))
            pairs.append((status, new))
        else:
            pairs.append((status, path))
    return pairs


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(description="pre-release checks")
    parser.add_argument("--version", default="", help="expected version (optional)")
    parser.add_argument(
        "--description", default="", help="change description for the private sub-git commit"
    )
    parser.add_argument(
        "--skip-subgit", action="store_true", help="skip private sub-git sync"
    )
    parser.add_argument(
        "--allow-placeholder",
        action="store_true",
        help="allow ci_check.py to still be a template placeholder",
    )
    args = parser.parse_args()

    fail = False
    print("========== pre-release check ==========")

    if not (REPO_ROOT / ".git").exists():
        print(f"[error] not a git repo root (no .git): {REPO_ROOT}", file=sys.stderr)
        return 1

    # --- 1. version ---
    version_file = REPO_ROOT / "version.json"
    if not version_file.exists():
        print("[error] version.json missing.", file=sys.stderr)
        return 1
    try:
        version = json.loads(version_file.read_text(encoding="utf-8"))["version"]
    except (json.JSONDecodeError, KeyError, OSError) as e:
        print(f"[error] cannot read version.json: {e}", file=sys.stderr)
        return 1
    if args.version and args.version != version:
        print(
            f"[warning] --version ({args.version}) differs from version.json "
            f"({version}); using file value."
        )
    print(f"[1/7] current version: v{version}")

    # --- 2. private sub-git sync (required before release) ---
    if not args.skip_subgit:
        if (REPO_ROOT / "private" / ".git").exists():
            status = _run(["git", "-C", "private", "status", "--short"])
            if status.returncode != 0:
                print("[warning] could not read private sub-git status; skipping auto commit.")
            elif status.stdout.strip():
                print("==> private sub-git has changes; auto committing:")
                for line in status.stdout.splitlines():
                    print(f"    {line}")
                msg = (
                    f"docs: private v{version} - {args.description}"
                    if args.description
                    else f"docs: private v{version} - pre-release sync"
                )
                _run(["git", "-C", "private", "add", "-A", "--", "."], check=True)
                c = _run(["git", "-C", "private", "commit", "-m", msg])
                if c.returncode != 0:
                    print("[error] private sub-git commit failed; fix manually.", file=sys.stderr)
                    return 1
                print(f"==> committed: {msg}")
            else:
                print("[2/7] private sub-git clean.")
            after = _run(["git", "-C", "private", "status", "--short"])
            if after.stdout.strip():
                print("[error] private sub-git still dirty; fix manually.", file=sys.stderr)
                fail = True
        else:
            print("[warning] private/ is not a git repo (sub-git not initialized).")
    else:
        print("[2/7] private sub-git sync skipped (--skip-subgit).")

    # --- 3. main repo status + safety scan ---
    print("[3/7] main repo status:")
    pairs = _status_paths()
    if pairs:
        print("    uncommitted changes (commit before release):")
        for status, path in pairs:
            print(f"    {status} {path}")
        print(
            "[warning] main repo has uncommitted changes. Confirm no private/ or "
            "secret files, then commit."
        )
    else:
        print("    clean.")

    private_hits = [p for _, p in pairs if _is_private_path(p)]
    if not private_hits:
        cached = _run(["git", "diff", "--cached", "--name-only", "-z"])
        private_hits = [p for p in cached.stdout.split("\0") if p and _is_private_path(p)]
    if not private_hits:
        untracked = _run(["git", "ls-files", "--others", "--exclude-standard", "-z"])
        private_hits = [p for p in untracked.stdout.split("\0") if p and _is_private_path(p)]
    if private_hits:
        print("[error] private/ content in main repo status (must not be committed):")
        for p in private_hits:
            print(f"    {p}")
        fail = True

    secret_hits = [f"{s} {p}" for s, p in pairs if SECRET_NAME_RE.search(p)]
    if secret_hits:
        print("[error] suspicious secret-named files in main repo status:")
        for line in secret_hits:
            print(f"    {line}")
        fail = True

    # --- 4. version consistency (version.json vs CHANGELOG top) ---
    changelog = REPO_ROOT / "private" / "dev" / "CHANGELOG.md"
    if changelog.exists():
        top = next(
            (line for line in changelog.read_text(encoding="utf-8").splitlines()
             if line.startswith("## v")),
            "",
        )
        if top and f"v{version}" not in top:
            print(f"[error] CHANGELOG top ({top}) does not match version.json (v{version}).")
            fail = True
        elif top:
            print(f"[4/7] CHANGELOG top matches version.json: v{version}")
        else:
            print(
                f"[error] no '## v' entry found in "
                f"{changelog.relative_to(REPO_ROOT)} (must be updated before release)."
            )
            fail = True
    else:
        print(
            f"[error] missing {changelog.relative_to(REPO_ROOT)} "
            "(must be updated before release)."
        )
        fail = True

    # --- 5. ci_check must be implemented ---
    ci_check = REPO_ROOT / "scripts" / "ci_check.py"
    if not ci_check.exists():
        print("[error] scripts/ci_check.py missing (must exist for release).", file=sys.stderr)
        fail = True
    else:
        ci_text = _read_text(ci_check)
        if not ci_text.strip():
            print(
                "[error] cannot read scripts/ci_check.py (binary or non-UTF-8); "
                "fix file encoding.",
                file=sys.stderr,
            )
            fail = True
        else:
            ci_state = _ci_check_state(ci_text)
            if ci_state == "placeholder":
                if args.allow_placeholder:
                    print(
                        "[warning] ci_check.py is still a template placeholder "
                        "(allowed via --allow-placeholder)."
                    )
                else:
                    print(
                        "[error] ci_check.py is still a template placeholder; implement real "
                        "checks first (or use --allow-placeholder)."
                    )
                    fail = True
            elif ci_state == "inconsistent":
                print(
                    "[error] ci_check.py still has placeholder body but the "
                    "PLACEHOLDER_MARKER constant was removed; implement real checks "
                    "(or restore the marker line).",
                    file=sys.stderr,
                )
                fail = True
            elif ci_state == "stale_constant":
                print(
                    "[warning] ci_check.py placeholder body removed but a leftover "
                    "PLACEHOLDER_MARKER constant remains; remove the dead marker line."
                )
                print("[5/7] ci_check.py implemented (placeholder body gone).")
            else:
                print("[5/7] ci_check.py implemented (no placeholder marker).")

    # --- 6. doc consistency (lightweight) ---
    root_agents = REPO_ROOT / "AGENTS.md"
    priv_agents = REPO_ROOT / "private" / "AGENTS.md"
    doc_ok = True
    if not root_agents.exists():
        print("[error] root AGENTS.md missing (must exist for release).", file=sys.stderr)
        fail = True
        doc_ok = False
    elif "private/AGENTS.md" not in _read_text(root_agents):
        print("[error] root AGENTS.md must reference private/AGENTS.md.", file=sys.stderr)
        fail = True
        doc_ok = False
    if not priv_agents.exists():
        print("[error] private/AGENTS.md missing (must exist for release).", file=sys.stderr)
        fail = True
        doc_ok = False
    if doc_ok:
        print("[6/7] doc consistency ok (root/private AGENTS.md present, pointer intact).")

    # --- 7. pre-development doc registers (PRD/RFC/ADR/RESEARCH) ---
    check_dev_docs = REPO_ROOT / "scripts" / "check_dev_docs.py"
    if not check_dev_docs.exists():
        print(
            "[error] scripts/check_dev_docs.py missing (must exist for release).",
            file=sys.stderr,
        )
        fail = True
    else:
        r = _run([sys.executable, str(check_dev_docs)])
        if r.returncode != 0:
            print(
                "[error] check_dev_docs.py failed "
                "(pre-development doc registers drift):"
            )
            for line in (r.stdout + r.stderr).splitlines():
                print(f"    {line}")
            fail = True
        else:
            print(
                "[7/7] check_dev_docs.py ok "
                "(PRD/RFC/ADR/RESEARCH registers consistent)."
            )

    # --- reminders ---
    print("========== reminders ==========")
    print("1. auto-audit: check docs/audit-checklist.md; prefer an independent sub-agent to review git diff.")
    print("2. docs ready: CHANGELOG / DESIGN / TEST-REPORT / README / root AGENTS.md / private/AGENTS.md.")
    print("   dev docs: PRD/RFC/ADR/RESEARCH registers consistent (scripts/check_dev_docs.py).")
    print("3. checks & tests passed and recorded in private/dev/TEST-REPORT.md (no pass, no release).")
    print("4. commit format: normal commits feat:/fix:/docs:/chore:/refactor: - description;")
    print("   release commit carries version: feat: v<version> - description")
    print("5. release: git tag v<version> + git push origin v<version> + gh release create (or CI auto).")

    if fail:
        print("[error] issues must be fixed before release.", file=sys.stderr)
        return 1
    print("========== check passed, ready to release ==========")
    return 0


if __name__ == "__main__":
    sys.exit(main())
