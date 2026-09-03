#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""init_project.py - 把内嵌项目模板初始化到新项目目录

从本 skill 的 assets/project-template/ 复制模板骨架到目标目录，做确定性初始化：
  1) 复制模板（排除 _trash、.git 等临时内容）
  2) 可选替换 package.json 的项目名
  3) git init + 首次提交（默认分支 main）

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


def _copy_template(target: Path) -> None:
    shutil.copytree(TEMPLATE_DIR, target, ignore=shutil.ignore_patterns(*EXCLUDE),
                    dirs_exist_ok=True)


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
    r = _run(target, "git", "init", "-b", branch)
    if r.returncode != 0:
        print("警告：git init 失败，跳过 git 初始化")
        return False
    _run(target, "git", "add", "-A")
    r = _run(target, "git", "commit", "-m", "chore: init from project template")
    if r.returncode != 0:
        print("警告：首次提交未完成（可能未配置 git user.name/email），已暂存，请手动提交：")
        print(r.stderr.strip())
        return False
    return True


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(description="把项目模板初始化到新项目目录")
    parser.add_argument("target", help="目标项目目录（必须为空或不存在）")
    parser.add_argument("--name", help="项目名（写入 package.json，kebab-case）")
    parser.add_argument("--branch", default="main", help="git 默认分支（默认 main）")
    parser.add_argument("--no-git", action="store_true", help="只复制文件，不建 git")
    args = parser.parse_args()

    if not TEMPLATE_DIR.is_dir():
        print(f"错误：模板镜像缺失：{TEMPLATE_DIR}")
        return 1

    target = Path(args.target).resolve()
    if target.exists() and any(target.iterdir()):
        print(f"错误：目标目录非空：{target}\n（只接受空目录或不存在的目录）")
        return 1

    _copy_template(target)
    if args.name:
        _set_project_name(target, args.name)

    committed = False
    if not args.no_git:
        committed = _git_init(target, args.branch)

    print(f"\n初始化完成：{target}")
    if committed:
        print("  首次提交：已完成")
    return 0


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


if __name__ == "__main__":
    sys.exit(main())
