#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scan_defensive.py - 辩护性措辞扫描（红线 17「范围克制与纠错清零」验收面）

扫描「为未做/不做的事补写说明」类表达（撤菜不解释；意图=番茄炒蛋不加东坡肉、
撤菜不留疤）：
  1) git 提交信息（subject + body，全历史）——命中即硬拦（--check 退出码 1）；
  2) 跟踪文件中的注释/文档——命中输出「人工复核候选清单」（不硬拦，防误报；
     命中不代表违规，需人工判断）。

第一版规则（可扩展；含白名单降噪）：
  - 提交信息（硬拦，高精度）：不再需要 | 暂不实现 | 未引入 | 为什么不需要 |
    为什么没有 | 已移除多余的 | 不需要（…）了 | 「X（无 Y）」型结构 `（无…）`
  - 注释/文档（人工复核，宽口径）：已移除 | 已删除 | 已去掉 | 不再需要 |
    不需要 | 不适用 | 未引入 | 暂不实现 | 为什么不需要 | 为什么没有 | 多余 |
    「X（无 Y）」型结构 `（无…）`

用法:
  python scripts/scan_defensive.py            # 报告（提交信息命中 + 候选复核清单）
  python scripts/scan_defensive.py --check    # 门禁：提交信息命中退出码 1

说明：PR 描述无法在本地读取，由 agent 自检 + 审计清单人工核对（红线 17）。
stdlib-only，Python 3.9+。
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COMMIT_PATTERNS = [
    ("DEFENSIVE", re.compile(
        r"不再需要|暂不实现|未引入|为什么不需要|为什么没有|已移除多余的|"
        r"不需要[^，。;；]{0,10}(?:了|配置|支持|实现|保留)",
        re.I,
    )),
    ("NO_X", re.compile(r"（无[^）]{1,24}）")),
]
REVIEW_PATTERNS = [
    ("DEFENSIVE", re.compile(
        r"已移除|已删除|已去掉|不再需要|不需要|不适用|未引入|暂不实现|"
        r"为什么不需要|为什么没有|多余",
        re.I,
    )),
    ("NO_X", re.compile(r"（无[^）]{1,24}）")),
]
# 白名单/占位特征：命中行大概率是合法表述或示例，跳过
IGNORE_VALUE = re.compile(
    r"\{\{|<[^>]*>|xxx+|example|placeholder|\.\.\.|@example\.|"
    r"TODO|N/A|不适用于文档类|本检查项|正则|示例|白名单",
    re.I,
)


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


def _git(*args: str) -> str:
    r = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return r.stdout


def _scan_text(text: str, hits: list, reviews: list, label: str) -> None:
    patterns = COMMIT_PATTERNS if label.startswith("commit") else REVIEW_PATTERNS
    for lineno, line in enumerate(text.splitlines(), 1):
        if len(line.strip()) > 300:
            continue
        for name, pat in patterns:
            if pat.search(line):
                val = pat.search(line).group(0)
                if IGNORE_VALUE.search(line):
                    continue
                if label.startswith("commit"):
                    hits.append((name, label, lineno, val, line.strip()[:150]))
                else:
                    reviews.append((name, label, lineno, val, line.strip()[:150]))
                break


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(description="辩护性措辞扫描（红线 17 验收面）")
    parser.add_argument("--check", action="store_true",
                        help="门禁模式：提交信息命中退出码 1")
    args = parser.parse_args()

    hits: list = []
    reviews: list = []

    # 1) 提交信息（subject + body，全历史）
    commits = _git("log", "--format=commit %H%n%s%n%b").splitlines()
    _scan_text("\n".join(commits), hits, reviews, "commit history")

    # 2) 跟踪文件中的注释/文档（候选人工复核）
    for f in _git("ls-files").splitlines():
        p = ROOT / f
        if p.name == "scan_defensive.py":
            continue
        if not p.is_file():
            continue
        try:
            data = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "\x00" in data:
            continue
        _scan_text(data, hits, reviews, f)

    print(f"== 辩护性措辞扫描 ==\n\n[提交信息命中（硬拦）] {len(hits)} 处")
    for name, label, lineno, val, snip in hits[:30]:
        print(f"  [{name}] {label}:{lineno}  value={val!r}  | {snip}")
    if len(hits) > 30:
        print(f"  ... 其余 {len(hits) - 30} 处略")

    print(f"\n[注释/文档候选复核清单（不硬拦，需人工判断）] {len(reviews)} 处")
    for name, label, lineno, val, snip in reviews[:50]:
        print(f"  [{name}] {label}:{lineno}  value={val!r}  | {snip}")
    if len(reviews) > 50:
        print(f"  ... 其余 {len(reviews) - 50} 处略（详见输出文件）")

    if args.check:
        print(f"\n门禁结果：{'FAIL（提交信息含辩护性措辞，需改写）' if hits else 'PASS'}")
        return 1 if hits else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
