#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bump_version.py - bump project version (VERSION file is the single source of truth)

Usage:
  python scripts/bump_version.py [--part patch|minor|major] [--version-file VERSION]
  python scripts/bump_version.py --help

Behavior:
  - read VERSION (X.Y.Z), bump by --part, write back (UTF-8, no BOM);
  - best-effort sync of version fields in package.json / Cargo.toml /
    pyproject.toml / src-tauri/*; targets come from version-sync.json (optional,
    entries merge over the built-in defaults; {"skip": true} disables a built-in
    target). Sync failure only warns, never aborts.
Exit code: 0 success; 1 failure.

NOTE: stdlib-only, Python 3.9+; the repo root is resolved from this script's
      location (the parent of scripts/), so it can be run from any working dir.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SYNC_TARGETS = {
    "package.json": {"type": "json", "key": "version"},
    "Cargo.toml": {
        "type": "regex",
        "pattern": r'(?m)^version\s*=\s*"[^"]+"',
        "replacement": 'version = "{version}"',
    },
    "src-tauri/Cargo.toml": {
        "type": "regex",
        "pattern": r'(?m)^version\s*=\s*"[^"]+"',
        "replacement": 'version = "{version}"',
    },
    "src-tauri/tauri.conf.json": {"type": "json", "key": "version"},
    "pyproject.toml": {
        "type": "regex",
        "pattern": r'(?m)^version\s*=\s*"[^"]+"',
        "replacement": 'version = "{version}"',
    },
}


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


def _write_utf8_no_bom(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def _bump(version: str, part: str) -> str:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version)
    if not m:
        raise ValueError(f"invalid VERSION format: '{version}' (expected X.Y.Z)")
    maj, minor, patch = (int(x) for x in m.groups())
    if part == "major":
        maj += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    else:
        patch += 1
    return f"{maj}.{minor}.{patch}"


def _load_config() -> dict:
    config_file = REPO_ROOT / "version-sync.json"
    if not config_file.exists():
        return {}
    try:
        data = json.loads(config_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"[warning] cannot read {config_file.name}: {e}", file=sys.stderr)
        return {}
    if not isinstance(data, dict):
        print(f"[warning] {config_file.name} must be a JSON object; ignored", file=sys.stderr)
        return {}
    return data


def _sync_targets(config: dict) -> dict:
    targets = dict(DEFAULT_SYNC_TARGETS)
    for path, spec in config.items():
        if isinstance(spec, dict) and spec.get("skip"):
            targets.pop(path, None)
        else:
            targets[path] = spec
    return targets


def _set_json_version(path: Path, key: str, version: str) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    node = data
    for part in key.split(".")[:-1]:
        node = node[part]
    node[key.split(".")[-1]] = version
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _sync_file(path: Path, spec: dict, version: str) -> bool:
    kind = spec.get("type", "regex")
    if kind == "json":
        key = spec.get("key", "version")
        try:
            _set_json_version(path, key, version)
            return True
        except (KeyError, TypeError, json.JSONDecodeError, OSError) as e:
            print(f"[warning] sync {path} failed (VERSION unchanged): {e}", file=sys.stderr)
            return False
    pattern = spec.get("pattern", "")
    replacement = spec.get("replacement", "").replace("{version}", version)
    try:
        content = path.read_text(encoding="utf-8")
        new_content, n = re.subn(pattern, replacement, content)
        if n == 0:
            return False
        path.write_text(new_content, encoding="utf-8", newline="\n")
        return True
    except (re.error, OSError) as e:
        print(f"[warning] sync {path} failed (VERSION unchanged): {e}", file=sys.stderr)
        return False


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(
        description="bump project version (VERSION is the single source of truth)"
    )
    parser.add_argument(
        "--part",
        choices=("patch", "minor", "major"),
        default="patch",
        help="version part to bump (default: patch)",
    )
    parser.add_argument(
        "--version-file",
        default="VERSION",
        help="version file path relative to repo root (default: VERSION)",
    )
    args = parser.parse_args()

    version_file = REPO_ROOT / args.version_file
    if not version_file.exists():
        print(f"[error] version file not found: {version_file}", file=sys.stderr)
        return 1

    old = version_file.read_text(encoding="utf-8").strip()
    try:
        new = _bump(old, args.part)
    except ValueError as e:
        print(f"[error] {e}", file=sys.stderr)
        return 1

    _write_utf8_no_bom(version_file, new + "\n")
    print(f"==> VERSION: {old} -> {new}")

    targets = _sync_targets(_load_config())
    for rel, spec in targets.items():
        path = REPO_ROOT / rel
        if path.exists() and isinstance(spec, dict):
            if _sync_file(path, spec, new):
                print(f"==> synced {rel} -> {new}")

    print("==> done. Update the top entry of private/dev/CHANGELOG.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
