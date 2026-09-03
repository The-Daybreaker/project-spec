#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""init_project.py - 把内嵌项目模板初始化到新项目目录

从本 skill 的 assets/project-template/ 复制模板骨架到目标目录，做确定性初始化：
  1) 复制模板（排除 _trash、.git 等临时内容）；目标目录非空时警告并
     继续——已有文件视为用户声明保留的内容，跳过不覆盖
  2) 可选替换 package.json 的项目名
  3) git init + 首次提交（默认分支 main）；git 环节失败以非零退出码反映

Stdlib-only，Python 3.9+。
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = SKILL_DIR / "assets" / "project-template"

# 复制时排除的内容（临时删除区 / git 元数据 / 缓存）
EXCLUDE = {"_trash", ".git", "__pycache__"}


def _run(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=str(cwd), capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def _copy_template(target: Path) -> list:
    """复制模板到目标目录；已存在的文件跳过不覆盖（保留用户内容）。

    返回被跳过的相对路径清单。"""
    skipped = []
    for src in sorted(TEMPLATE_DIR.rglob("*")):
        rel = src.relative_to(TEMPLATE_DIR)
        if any(part in EXCLUDE for part in rel.parts):
            continue
        dst = target / rel
        if src.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
        elif dst.exists():
            skipped.append(rel.as_posix())
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    return skipped


def _set_project_name(target: Path, name: str) -> None:
    pkg = target / "package.json"
    if not pkg.is_file():
        return
    data = json.loads(pkg.read_text(encoding="utf-8"))
    data["name"] = name
    pkg.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")


def _git_init(target: Path, branch: str) -> bool:
    """git init + 暂存 + 首次提交。返回是否完成提交。"""
    try:
        r = _run(target, "git", "init", "-b", branch)
    except FileNotFoundError:
        print("错误：未找到 git 命令，无法完成 git 初始化")
        return False
    if r.returncode != 0:
        print(f"错误：git init 失败：\n{r.stderr.strip()}")
        return False
    _run(target, "git", "add", "-A")
    r = _run(target, "git", "commit", "-m", "chore: init from project template")
    if r.returncode != 0:
        print("警告：首次提交未完成（可能未配置 git user.name/email），文件已暂存，请手动提交：")
        print(r.stderr.strip())
        return False
    return True


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(description="把项目模板初始化到新项目目录")
    parser.add_argument("target", help="目标项目目录（空目录，或仅含要保留的文件）")
    parser.add_argument("--name", help="项目名（写入 package.json，kebab-case）")
    parser.add_argument("--branch", default="main", help="git 默认分支（默认 main）")
    parser.add_argument("--no-git", action="store_true", help="只复制文件，不建 git")
    args = parser.parse_args()

    if not TEMPLATE_DIR.is_dir():
        print(f"错误：模板目录缺失：{TEMPLATE_DIR}")
        return 1

    target = Path(args.target).resolve()
    if target.exists() and not target.is_dir():
        print(f"错误：目标路径已存在且不是目录：{target}")
        return 1
    if target.is_dir():
        existing = sorted(p.name for p in target.iterdir())
        if existing:
            print(f"警告：目标目录非空（{len(existing)} 项），继续初始化；"
                  "已有文件视为保留内容，不会被覆盖：")
            for name in existing:
                print(f"  - {name}")

    skipped = _copy_template(target)
    if skipped:
        print("以下文件已存在，跳过（模板不覆盖）：")
        for rel in skipped:
            print(f"  - {rel}")
    if args.name:
        _set_project_name(target, args.name)

    if args.no_git:
        print(f"\n初始化完成：{target}")
        return 0

    committed = _git_init(target, args.branch)
    print(f"\n初始化完成：{target}")
    if committed:
        print("  首次提交：已完成")
        return 0
    print("  首次提交：未完成（见上方提示）")
    return 1


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


if __name__ == "__main__":
    sys.exit(main())
