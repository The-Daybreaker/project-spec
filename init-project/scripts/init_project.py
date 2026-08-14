#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""init_project.py — 根据通用项目模板初始化目标项目文件夹。

用法:
  python init_project.py <目标目录> [--name NAME] [--desc DESC] [--remote URL]
      [--branch main] [--author NAME] [--no-git] [--template PATH]

行为（按顺序）:
  1. 校验目标目录：不存在则创建；**非空时报错并列出已有文件**（不覆盖任何
     已有文件——与 skill 红线「不覆盖已有非模板文件」一致）。
  2. 复制模板（默认 <skill>/assets/project-template/）到目标目录，
     跳过 .git / __pycache__ / .DS_Store 等。
  3. 全文件替换占位符 {{PROJECT_NAME}} {{PROJECT_DESCRIPTION}} {{DEFAULT_BRANCH}}
     {{AUTHOR}} {{YEAR}} {{DATE}} {{VERSION}} {{LICENSE_NOTICE}}
     （UTF-8 文本；二进制文件跳过）。
  4. 默认初始化 git：主仓库（-b <branch>）与 private 子 git，各完成首次提交；
     配置远端（--remote，仅 add 不 push）。--no-git 跳过本步。
  5. 打印汇总与下一步（不自动 push；推送需另行征得用户同意）。

仅依赖 Python 标准库；退出码 0 成功，1 失败（git 不可用时警告并继续）。
"""

import argparse
import datetime
import shutil
import subprocess
import sys
from pathlib import Path

SKIP_NAMES = {'.git', '__pycache__', '.DS_Store', 'Thumbs.db'}

PLACEHOLDERS = [
    'PROJECT_NAME',
    'PROJECT_DESCRIPTION',
    'DEFAULT_BRANCH',
    'AUTHOR',
    'YEAR',
    'DATE',
    'VERSION',
    'LICENSE_NOTICE',
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description='根据通用项目模板初始化目标项目文件夹（仅标准库）。'
    )
    p.add_argument('target', help='目标项目目录（不存在则创建）')
    p.add_argument('--name', default='', help='项目名（默认取目录名）')
    p.add_argument('--desc', default='', help='一句话描述（默认同项目名）')
    p.add_argument('--remote', default='', help='git 远端 URL（仅 add remote，不推送）')
    p.add_argument('--branch', default='main', help='默认分支名（默认 main）')
    p.add_argument('--author', default='', help='作者（默认取 git 全局 user.name）')
    p.add_argument('--no-git', action='store_true', help='只复制+替换，不初始化 git')
    p.add_argument('--template', default='',
                   help='模板目录（默认 <skill>/assets/project-template/）')
    return p.parse_args()


def run_git(args: list, cwd: Path):
    """运行 git，返回 CompletedProcess；git 不存在时返回 None。"""
    try:
        return subprocess.run(
            ['git'] + args, cwd=str(cwd),
            capture_output=True, text=True, encoding='utf-8', errors='replace',
        )
    except FileNotFoundError:
        return None


def copy_tree(src: Path, dst: Path) -> int:
    """复制模板到目标目录，返回复制的文件数。目标非空时拒绝（不覆盖已有文件）。"""
    if dst.exists():
        if not dst.is_dir():
            print(f'[错误] 目标已存在且不是目录: {dst}')
            sys.exit(1)
        existing = [p for p in dst.rglob('*') if p.is_file()]
        if existing:
            print(f'[错误] 目标目录非空（{len(existing)} 个文件），为遵守'
                  f'「不覆盖已有文件」红线，脚本拒绝继续。')
            print('已存在的文件：')
            for f in sorted(existing)[:50]:
                print(f'  {f.relative_to(dst)}')
            print('处理方式：选择空目录；或先与用户确认保留清单，由 agent 将保留'
                  '文件移出/合并后重试。')
            sys.exit(1)
    else:
        dst.mkdir(parents=True)

    def ignore(dirpath, names):
        return [n for n in names if n in SKIP_NAMES]

    shutil.copytree(src, dst, dirs_exist_ok=True, ignore=ignore)
    return len([p for p in dst.rglob('*') if p.is_file()])


def replace_in_text(text: str, values: dict) -> str:
    for key in PLACEHOLDERS:
        text = text.replace('{{' + key + '}}', values.get(key, ''))
    return text


def replace_all(root: Path, values: dict) -> int:
    """全文件替换占位符，返回被修改的文件数。"""
    changed = 0
    for p in root.rglob('*'):
        if not p.is_file() or p.name in SKIP_NAMES or '.git' in p.parts:
            continue
        try:
            raw = p.read_bytes()
            text = raw.decode('utf-8-sig')
        except (UnicodeDecodeError, OSError):
            continue  # 二进制文件跳过
        new_text = replace_in_text(text, values)
        if new_text != text:
            p.write_text(new_text, encoding='utf-8', newline='\n')
            changed += 1
    return changed


def git_init_repo(repo: Path, branch: str, commit_msg: str, remote: str = '') -> bool:
    """初始化一个 git 仓库并完成首次提交；失败返回 False（文件已就绪，不删除）。"""
    if branch:
        r = run_git(['init', '-b', branch], repo)
    else:
        r = run_git(['init'], repo)
    if r is None:
        return False
    if r.returncode != 0:
        print(f'  [警告] git init 失败: {r.stderr.strip()}')
        return False
    if remote:
        rr = run_git(['remote', 'add', 'origin', remote], repo)
        if rr is not None and rr.returncode != 0:
            print(f'  [警告] remote add 失败: {rr.stderr.strip()}')
    run_git(['add', '-A', '--', '.'], repo)
    rc = run_git(['commit', '-m', commit_msg], repo)
    if rc is None:
        return False
    if rc.returncode != 0:
        print(f'  [警告] 首次提交失败（可能未配置 git 身份）: {rc.stderr.strip()}')
        print('  文件已暂存；请配置 git config user.name/user.email 后手动提交。')
        return False
    return True


def main() -> int:
    args = parse_args()
    target = Path(args.target).resolve()

    # 1. 模板目录
    if args.template:
        template = Path(args.template).resolve()
    else:
        template = Path(__file__).resolve().parent.parent / 'assets' / 'project-template'
    if not template.is_dir():
        print(f'[错误] 模板目录不存在: {template}')
        return 1

    # 2. 参数默认值
    name = args.name.strip() or target.name
    desc = args.desc.strip() or name
    author = args.author.strip()
    if not author:
        # 注意：此时目标目录可能尚未创建，cwd 必须用已存在的目录（模板目录）
        r = run_git(['config', '--global', 'user.name'], template)
        if r is not None and r.returncode == 0:
            author = r.stdout.strip()
    if not author:
        author = 'Your Name'  # 占位，用户可稍后修改 LICENSE

    # 3. 复制
    print(f'[1/4] 复制模板 -> {target}')
    copied = copy_tree(template, target)

    # 4. 替换占位符
    print('[2/4] 替换占位符')
    version = '0.1.0'
    vf = target / 'VERSION'
    if vf.is_file():
        version = vf.read_text(encoding='utf-8').strip() or version
    today = datetime.date.today()
    values = {
        'PROJECT_NAME': name,
        'PROJECT_DESCRIPTION': desc,
        'DEFAULT_BRANCH': args.branch,
        'AUTHOR': author,
        'YEAR': str(today.year),
        'DATE': f'{today.year}-{today.month:02d}-{today.day:02d}',
        'VERSION': version,
        'LICENSE_NOTICE': f'本项目使用 MIT 许可，详见 LICENSE。',
    }
    changed = replace_all(target, values)
    print(f'  复制 {copied} 个文件，替换 {changed} 个文件')

    # 5. git 初始化
    if args.no_git:
        print('[3/4] 跳过 git 初始化（--no-git）。')
    else:
        print('[3/4] 初始化 git 仓库')
        ok_main = git_init_repo(target, args.branch,
                                'chore: init from universal project template',
                                args.remote)
        if not ok_main:
            print('  [警告] 主仓库初始化未完成，请按 references/init-steps.md 第 4 节手动收尾。')
        priv = target / 'private'
        if priv.is_dir():
            ok_priv = git_init_repo(priv, args.branch, f'docs: private v{version} - init')
            if not ok_priv:
                print('  [警告] private 子 git 初始化未完成，请手动收尾。')

    # 6. 汇总
    print('[4/4] 完成')
    print(f'  项目: {name}（{desc}）  版本: {version}  分支: {args.branch}')
    print(f'  位置: {target}')
    if args.remote:
        print(f'  远端已配置: {args.remote}（未推送；推送前请征得用户同意）')
    print()
    print('下一步（agent 按 references/init-steps.md 校验清单执行）:')
    print('  1. 回读校验: git grep -n -E "\\{\\{[A-Z_]+\\}\\}" 应无残留；git status 与 git -C private status 应干净')
    print('  2. git check-ignore private/ 应命中（.gitignore 生效）')
    print('  3. 请用户补充 private/AGENTS.md 的「本机环境」「安装目标/部署目标」')
    print('  4. 按项目技术栈实现 scripts/ci-check.ps1 与 .github/workflows/ci.yml')
    print('  5. 用户确认后配置远端并推送首个提交（首次 push 不自动发 Release）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
