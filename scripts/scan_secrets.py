#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scan_secrets.py - 公开仓库发版前安全扫描（高危凭据 + 个人信息）

背景（2026-08-27 安全审计）：本仓库为 PUBLIC，任何本机路径/用户名/凭据都会
全网可见。本脚本扫描 git 已跟踪文件（可选全部历史）中的：

  1) 高危凭据（零容忍，命中即门禁失败）：
     GitHub/OpenAI/AWS/Google/Slack/Stripe 令牌、私钥块、JWT、
     api key / secret / token / password 赋值等；
  2) 个人信息（需人工复核，--strict 下同样门禁失败）：
     Windows 本机绝对路径、系统用户名、邮箱、手机号、身份证号。

用法:
  python scripts/scan_secrets.py             # 扫当前跟踪文件
  python scripts/scan_secrets.py --history   # 追加扫全部 git 历史 blob
  python scripts/scan_secrets.py --check     # 门禁模式：高危命中退出码 1
  python scripts/scan_secrets.py --strict    # 门禁模式：高危或个人信息命中均退出码 1

降噪策略:
- 占位符/示例值（{{...}}、<...>、example、xxx、@example.com 等）自动忽略；
- 代码中正则字面量易被误判为 Windows 路径：命中值含正则元字符
  （([{*+$? 等）时忽略（真实路径极少含这些字符，且个人信息本就需人工复核）。

Stdlib-only，Python 3.9+。
"""

import argparse
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HIGH_PATTERNS = [
    ("GITHUB_TOKEN", r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    ("GITHUB_PAT", r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    ("OPENAI_SK", r"\bsk-[A-Za-z0-9]{20,}\b"),
    ("AWS_ACCESS_KEY", r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    ("GOOGLE_API_KEY", r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    ("SLACK_TOKEN", r"\b(xox[baprs]|xoxr)-[A-Za-z0-9\-]{10,}\b"),
    ("STRIPE_LIVE_KEY", r"\b(?:sk|pk|rk)_live_[A-Za-z0-9]{20,}\b"),
    ("PRIVATE_KEY", r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    ("JWT", r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{5,}\b"),
    ("SECRET_ASSIGN", r"(?i)\b(?:api[_-]?key|client[_-]?secret|access[_-]?token|"
                       r"auth[_-]?token|refresh[_-]?token|secret)\b\s*[:=]\s*"
                       r"[\"'][^\"']{8,}[\"']"),
    ("PASSWORD_ASSIGN", r"(?i)\b(?:password|passwd|pwd)\b\s*[:=]\s*"
                        r"[\"'][^\"']{4,}[\"']"),
    ("BEARER", r"(?i)authorization\s*:\s*bearer\s+[A-Za-z0-9._\-]{16,}"),
]

PERSONAL_PATTERNS = [
    # 排除仓库自身账号名 The-Daybreaker（公开仓库 URL 固有标识，非泄漏）
    ("USERNAME", r"(?<![\w-])Daybreaker(?![\w-])"),
    ("WIN_PATH", r"[A-Za-z]:\\[^\"'\s\\]*(?:\\[^\"'\s\\]*)+"),
    ("UNIX_HOME", r"(?<![A-Za-z0-9])/(?:home|Users)/[A-Za-z0-9._\-]+"),
    ("EMAIL", r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"),
    ("CN_MOBILE", r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    ("CN_ID", r"(?<!\d)\d{17}[\dXx](?!\d)"),
]

# 命中值里的占位符/示例特征 -> 忽略
IGNORE_VALUE = re.compile(
    r"\{\{|<[^>]*>|xxx+|example|placeholder|\.\.\.|your-|@example\.(com|org|net)|"
    r"localhost|REPLACE|git@github\.com",
    re.I,
)
# 命中值含正则元字符 -> 疑似代码中的正则字面量，忽略（防误报）
REGEX_META = re.compile(r"[({[\]*+$?|^}]")


def _git(*args: str) -> str:
    r = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return r.stdout


def _scan_text(text: str, patterns, hits: list, label: str, placeholder: list) -> None:
    for lineno, line in enumerate(text.splitlines(), 1):
        for name, pat in patterns:
            for m in re.finditer(pat, line):
                val = m.group(0)
                if IGNORE_VALUE.search(val):
                    placeholder.append((name, label, lineno, val, line.strip()[:150]))
                elif REGEX_META.search(val):
                    # 高度疑似正则字面量而非真实路径
                    continue
                else:
                    hits.append((name, label, lineno, val, line.strip()[:150]))


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(description="公开仓库发版前安全扫描")
    parser.add_argument("--history", action="store_true",
                        help="追加扫描全部 git 历史 blob（慢）")
    parser.add_argument("--check", action="store_true",
                        help="门禁模式：高危命中时退出码 1")
    parser.add_argument("--strict", action="store_true",
                        help="门禁模式：高危或个人信息命中均退出码 1")
    args = parser.parse_args()

    hits: list = []
    placeholders: list = []
    files = _git("ls-files").splitlines()

    for f in files:
        p = ROOT / f
        if p.name == "scan_secrets.py":
            continue  # 自身源码含模式字面量，不参与扫描
        if not p.is_file():
            continue
        data = p.read_text(encoding="utf-8", errors="replace")
        if "\x00" in data:
            continue
        _scan_text(data, HIGH_PATTERNS + PERSONAL_PATTERNS, hits, f, placeholders)

    hist_count = 0
    if args.history:
        blob_paths = defaultdict(set)
        for ol in _git("rev-list", "--objects", "--all").splitlines():
            parts = ol.split(" ", 1)
            if len(parts) == 2:
                blob_paths[parts[0]].add(parts[1])
        cur_blobs = {_git("rev-parse", f"HEAD:{f}").strip() for f in files}
        for sha, paths in blob_paths.items():
            if sha in cur_blobs:
                continue
            data = _git("cat-file", "blob", sha)
            if not data or "\x00" in data:
                continue
            if any(str(pa).endswith("scan_secrets.py") for pa in paths):
                continue  # 自身历史版本同理跳过
            hist_count += 1
            label = f"{sorted(paths)[0]} (历史 blob {sha[:10]})"
            _scan_text(data, HIGH_PATTERNS + PERSONAL_PATTERNS, hits, label, placeholders)

    high = [h for h in hits if h[0] in {n for n, _ in HIGH_PATTERNS}]
    personal = [h for h in hits if h[0] in {n for n, _ in PERSONAL_PATTERNS}]

    print(f"== 扫描范围：当前跟踪 {len(files)} 文件"
          + (f"，历史 blob {hist_count} 个" if args.history else "") + " ==")
    print(f"\n[高危凭据] {len(high)} 处")
    for name, label, lineno, val, snip in high:
        print(f"  [{name}] {label}:{lineno}  value={val!r}  | {snip}")
    print(f"\n[个人信息] {len(personal)} 处（需人工复核）")
    for name, label, lineno, val, snip in personal:
        print(f"  [{name}] {label}:{lineno}  value={val!r}  | {snip}")
    print(f"\n[忽略的占位符/示例] {len(placeholders)} 处")
    for name, label, lineno, val, snip in placeholders[:10]:
        print(f"  [{name}] {label}:{lineno}  value={val!r}  | {snip}")
    if len(placeholders) > 10:
        print(f"  ... 其余 {len(placeholders) - 10} 处略")

    fail = bool(high) or (args.strict and personal)
    if args.check or args.strict:
        print(f"\n门禁结果：{'FAIL（需处理后再发版）' if fail else 'PASS'}")
        return 1 if fail else 0
    return 0


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


if __name__ == "__main__":
    sys.exit(main())
