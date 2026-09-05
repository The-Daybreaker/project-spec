#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""init_project.py - 把内嵌项目模板初始化到新项目目录

从本 skill 的 assets/project-template/ 复制模板骨架到目标目录，做确定性初始化：
  1) 复制模板（排除 _trash、.git 等临时内容）；目标目录非空时警告并
     继续——已有文件视为用户声明保留的内容，跳过不覆盖
  2) 可选替换 package.json 的项目名（仅作用于模板自己落盘的那份；目标
     目录已有 package.json 时视为保留内容，不改写、只提醒）
  3) git init + 首次提交（默认分支 main）；git 环节失败以非零退出码反映

安全边界：目标目录已含 .git（即已是 git 仓库）时直接报错退出，不做任何
git 操作——避免污染用户现有仓库；这种场景应由 agent 逐步接手初始化。

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
    """把项目名写入模板自己落盘的 package.json（调用方保证它是模板新复制的）。"""
    pkg = target / "package.json"
    if not pkg.is_file():
        return
    try:
        data = json.loads(pkg.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"警告：package.json 不是合法 JSON，跳过改名：{e}")
        return
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
        # `git init -b` 需要 git >= 2.28，旧版报参数不认识；init 是幂等的，
        # 直接回退 init + symbolic-ref 置默认分支，不解析报错文本
        r = _run(target, "git", "init")
        if r.returncode != 0:
            print(f"错误：git init 失败：\n{r.stderr.strip()}")
            return False
        r = _run(target, "git", "symbolic-ref", "HEAD", f"refs/heads/{branch}")
        if r.returncode != 0:
            print(f"错误：无法把默认分支设为 {branch}（本机 git 可能过旧）：\n{r.stderr.strip()}")
            return False
        print(f"提醒：git init -b 不可用（git < 2.28），已用 symbolic-ref 把默认分支设为 {branch}")
    r = _run(target, "git", "add", "-A")
    if r.returncode != 0:
        print(f"错误：git add 失败：\n{r.stderr.strip()}")
        return False
    # 无可提交改动用 status --porcelain 判定（机器可读，不依赖 git 输出语言）
    r = _run(target, "git", "status", "--porcelain")
    if r.returncode == 0 and not r.stdout.strip():
        print("提醒：没有需要提交的改动（目标目录内容已与模板一致），未产生提交")
        return False
    # 未配置身份提交必败，前置探测、给精准提示，不从报错文本猜原因
    if (not _git_config_set(target, "user.name")
            or not _git_config_set(target, "user.email")):
        print("警告：git 身份未配置（user.name / user.email），首次提交无法完成；文件已暂存。")
        print("请先配置后再手动提交，例如：")
        print('  git config --global user.name "你的名字"')
        print('  git config --global user.email "you@example.com"')
        return False
    r = _run(target, "git", "commit", "-m", "chore: init from project template")
    if r.returncode != 0:
        print("警告：首次提交未完成，文件已暂存，请手动提交：")
        print((r.stdout + r.stderr).strip())
        return False
    return True


def _git_config_set(target: Path, key: str) -> bool:
    """读 git 配置（含 global/system 合并结果），键存在且非空返回 True。"""
    r = _run(target, "git", "config", "--get", key)
    return r.returncode == 0 and r.stdout.strip() != ""


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
    if (target / ".git").exists():
        print(f"错误：目标目录已是 git 仓库（存在 .git）：{target}")
        print("本脚本只面向全新目录，不会对已有仓库执行任何 git 操作；")
        print("如需在已有仓库内套用模板，请由 agent 逐步接手初始化。")
        return 1
    if target.is_dir():
        existing = sorted(p.name for p in target.iterdir())
        if existing:
            print(f"警告：目标目录非空（{len(existing)} 项），继续初始化；"
                  "已有文件视为保留内容，不会被覆盖：")
            for name in existing:
                print(f"  - {name}")

    try:
        skipped = _copy_template(target)
    except OSError as e:
        print(f"错误：复制模板时发生 I/O 错误：{e}")
        return 1
    if skipped:
        print("以下文件已存在，跳过（模板不覆盖）：")
        for rel in skipped:
            print(f"  - {rel}")
    if args.name:
        # --name 只作用于模板自己落盘的 package.json；用户原有的（在 skipped 里）不改写
        if "package.json" in skipped:
            print("提醒：目标目录已有 package.json（视为保留内容），--name 未应用；"
                  "如需改名请手动处理")
        else:
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
