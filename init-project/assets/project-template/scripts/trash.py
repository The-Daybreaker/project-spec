#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""trash.py - send files/folders to the system Recycle Bin / trash (cross-platform)

Usage:
  python scripts/trash.py <path> [<path> ...]

Behavior:
  - Windows: native Recycle Bin via SHFileOperationW (ctypes, stdlib only)
  - macOS: try the `trash` CLI, then AppleScript Finder delete
  - Linux: try `gio trash`, then `trash-put`
Exit code: 0 all paths sent to trash; 1 failure (prints how to proceed).

NOTE: stdlib-only, Python 3.9+; used by the delete discipline in AGENTS.md
      (dialog-internal deletions first go to _trash/, then the whole folder is
      sent to the Recycle Bin with this script at the end of the task).
"""

import platform
import shutil
import subprocess
import sys
from pathlib import Path


def _win_trash(paths: list) -> None:
    import ctypes
    from ctypes import wintypes

    class SHFILEOPSTRUCTW(ctypes.Structure):
        _fields_ = [
            ("hwnd", wintypes.HWND),
            ("wFunc", wintypes.UINT),
            ("pFrom", wintypes.LPCWSTR),
            ("pTo", wintypes.LPCWSTR),
            ("fFlags", ctypes.c_uint16),
            ("fAnyOperationsAborted", wintypes.BOOL),
            ("hNameMappings", wintypes.LPVOID),
            ("lpszProgressTitle", wintypes.LPCWSTR),
        ]

    FO_DELETE = 3
    FOF_ALLOWUNDO = 0x40
    FOF_NOCONFIRMATION = 0x10
    FOF_SILENT = 0x4

    # pFrom must be double-NUL terminated
    source = "\0".join(str(Path(p).resolve()) for p in paths) + "\0\0"
    op = SHFILEOPSTRUCTW()
    op.wFunc = FO_DELETE
    op.pFrom = source
    op.fFlags = FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_SILENT
    res = ctypes.windll.shell32.SHFileOperationW(ctypes.byref(op))
    if res != 0:
        raise RuntimeError(f"SHFileOperationW failed with code {res}")


def _mac_trash(paths: list) -> None:
    if shutil.which("trash"):
        subprocess.run(["trash", *paths], check=True)
        return
    script = ["tell application \"Finder\"", *[f'delete POSIX file "{Path(p).resolve()}"' for p in paths], "end tell"]
    subprocess.run(["osascript", "-e", "\n".join(script)], check=True)


def _linux_trash(paths: list) -> None:
    for cmd in (["gio", "trash"], ["trash-put"]):
        if shutil.which(cmd[0]):
            subprocess.run([*cmd, *paths], check=True)
            return
    raise RuntimeError(
        "no trash tool found; install trash-cli (Linux) or use gio trash"
    )


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0

    paths = [p for p in sys.argv[1:] if not p.startswith("-")]
    missing = [p for p in paths if not Path(p).exists()]
    if missing:
        print(f"[error] path(s) not found: {missing}", file=sys.stderr)
        return 1
    if not paths:
        print("[error] no paths given", file=sys.stderr)
        return 1

    system = platform.system()
    try:
        if system == "Windows":
            _win_trash(paths)
        elif system == "Darwin":
            _mac_trash(paths)
        else:
            _linux_trash(paths)
    except Exception as e:  # noqa: BLE001 - report and let the user decide
        print(f"[error] failed to send to trash: {e}", file=sys.stderr)
        print("        fallback: move the folder out of the repo, or delete after user confirmation.", file=sys.stderr)
        return 1

    for p in paths:
        print(f"==> sent to trash: {Path(p).resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
