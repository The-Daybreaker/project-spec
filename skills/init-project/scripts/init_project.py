#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""init_project.py — 根据通用项目模板初始化目标项目文件夹。

用法:
  python init_project.py <目标目录> [--name NAME] [--desc DESC] [--remote URL]
      [--branch main] [--author NAME] [--license mit] [--license-file PATH]
      [--auto-release] [--no-git] [--template PATH]

行为（按顺序）:
  1. 校验目标目录：不存在则创建；**非空时报错并列出已有文件**（不覆盖任何
     已有文件——与 skill 红线「不覆盖已有非模板文件」一致）。
  2. 复制模板（默认 <skill>/assets/project-template/）到目标目录，
     跳过 .git / __pycache__ / .DS_Store 等。
  3. 全文件替换占位符 {{PROJECT_NAME}} {{PROJECT_DESCRIPTION}} {{DEFAULT_BRANCH}}
     {{AUTHOR}} {{YEAR}} {{DATE}} {{DATETIME}} {{VERSION}} {{LICENSE_NOTICE}} {{AUTO_RELEASE}}
     （UTF-8 文本；二进制文件跳过）。
  4. 许可：默认 MIT；--license-file 用自定义 LICENSE 替换模板文件。
  5. 默认初始化 git：主仓库（-b <branch>）与 private 子 git，各完成首次提交；
     配置远端（--remote，仅 add 不 push）。--no-git 跳过本步。
  6. 打印汇总与下一步（不自动 push；推送需另行征得用户同意）。

仅依赖 Python 标准库；退出码 0 成功，1 失败（git 不可用时警告并继续）。
"""

import argparse
import datetime
import json
import re
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
    'DATETIME',
    'VERSION',
    'LICENSE_NOTICE',
    'AUTO_RELEASE',
]


def _configure_utf8() -> None:
    """Windows 默认代码页（GBK）下把控制台输出切为 UTF-8，避免中文乱码。"""
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except AttributeError:
        pass


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
    p.add_argument('--license', default='mit',
                   help='许可（当前内置: mit；其他可用 --license-file 提供）')
    p.add_argument('--license-file', default='',
                   help='自定义 LICENSE 文件路径（替换模板 LICENSE，其中 {{YEAR}}/{{AUTHOR}} '
                        '占位符同样会被替换）')
    p.add_argument('--auto-release', action='store_true',
                   help='开启「每次改动完成后自动发布」（视为发布/推送预授权；'
                        '默认不自动发布，用户确认后发布）')
    p.add_argument('--no-git', action='store_true', help='只复制+替换，不初始化 git')
    p.add_argument('--template', default='',
                   help='模板目录（默认 <skill>/assets/project-template/）')
    return p.parse_args()


def _valid_name(name: str) -> bool:
    """kebab-case：小写字母/数字开头，后续段以单个连字符分隔。"""
    return bool(re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name))


def _kebab_slug(s: str) -> str:
    """把任意名称规范化为 kebab-case（小写、分隔符统一为连字符、去首尾连字符）。

    无法保留的有效字符（如中文、重音符号）会被去除；结果为空的场景回退原始名
    （保留目录名原样，避免 {{PROJECT_NAME}} 替换为空）并提示。
    """
    slug = re.sub(r'[^0-9A-Za-z\-_ .]+', '-', s).strip('-_ .')
    slug = re.sub(r'[\-_ .]+', '-', slug).strip('-').lower()
    if not slug:
        print(f'  [提示] 目录名含非 ASCII 字符，项目名回退为目录名原样: {s!r}'
              '（如需规范项目名请用 --name 指定）')
        return s.strip()
    return slug


def _valid_branch(branch: str) -> bool:
    """git 分支名基本合法性检查（不保证与所有 git 版本完全一致）。"""
    if not branch or branch.startswith(('-', '/')) or branch.endswith(('/', '.')):
        return False
    if '..' in branch or '@{' in branch or '//' in branch or ' ' in branch:
        return False
    return bool(re.fullmatch(r'[A-Za-z0-9._/-]+', branch))


def _read_git_user_name(cwd: Path) -> str:
    """读取 git 全局 user.name，按字节流尝试 UTF-8 / GBK 解码（中文 Windows 兼容）。"""
    try:
        r = subprocess.run(['git', 'config', '--global', 'user.name'],
                           cwd=str(cwd), capture_output=True)
    except FileNotFoundError:
        return ''
    if r.returncode != 0:
        return ''
    raw = r.stdout
    for enc in ('utf-8', 'gbk', 'latin-1'):
        try:
            return raw.decode(enc).strip()
        except UnicodeDecodeError:
            continue
    return raw.decode('utf-8', errors='replace').strip()


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
    _configure_utf8()
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

    # 2. 参数默认值与校验
    explicit_name = bool(args.name.strip())
    name = args.name.strip() or _kebab_slug(target.name)
    if explicit_name and not _valid_name(name):
        print(f'[错误] --name 必须是 kebab-case（小写字母/数字/连字符）: {name}')
        return 1
    if not _valid_name(name):
        print(f'[警告] 项目名不是 kebab-case（将按原样使用，建议后续改名为 kebab-case）: {name}')
    elif not explicit_name:
        print(f'[提示] 未指定 --name，已按目录名规范化为 kebab-case: {name}')
    if not _valid_branch(args.branch):
        print(f'[错误] --branch 不是合法 git 分支名: {args.branch}')
        return 1
    if args.remote and args.remote.startswith('-'):
        print(f'[错误] --remote 不能以 - 开头（以免被误解析为选项）: {args.remote}')
        return 1
    desc = args.desc.strip() or name
    author = args.author.strip()
    if not author:
        # 注意：此时目标目录可能尚未创建，cwd 必须用已存在的目录（模板目录）
        author = _read_git_user_name(template)
    if not author:
        author = 'Your Name'  # 占位，用户可稍后修改 LICENSE

    license_name = 'MIT'
    license_notice = '本项目使用 MIT 许可，详见 LICENSE。'
    if args.license_file:
        lf = Path(args.license_file).resolve()
        if not lf.is_file():
            print(f'[错误] LICENSE 文件不存在: {lf}')
            return 1
        license_name = '自定义'
        license_notice = '本项目使用自定义许可，详见 LICENSE。'
    elif args.license != 'mit':
        print(f'[错误] 未内置许可: {args.license}（当前支持: mit；其他可用 --license-file 提供）')
        return 1

    # 3. 复制
    print(f'[1/4] 复制模板 -> {target}')
    copied = copy_tree(template, target)

    if args.license_file:
        shutil.copyfile(Path(args.license_file).resolve(), target / 'LICENSE')

    # 4. 替换占位符
    print('[2/4] 替换占位符')
    version = '0.0.1'
    vf = target / 'version.json'
    if vf.is_file():
        try:
            data = json.loads(vf.read_text(encoding='utf-8'))
            version = str(data.get('version') or version)
        except (json.JSONDecodeError, OSError):
            pass
    today = datetime.date.today()
    now = datetime.datetime.now()
    values = {
        'PROJECT_NAME': name,
        'PROJECT_DESCRIPTION': desc,
        'DEFAULT_BRANCH': args.branch,
        'AUTHOR': author,
        'YEAR': str(today.year),
        'DATE': f'{today.year}-{today.month:02d}-{today.day:02d}',
        'DATETIME': f'{today.year}-{today.month:02d}-{today.day:02d} {now.hour:02d}:{now.minute:02d}',
        'VERSION': version,
        'LICENSE_NOTICE': license_notice,
        'AUTO_RELEASE': (
            '每次改动完成后自动执行发布（提交、推送、tag/Release、分发/部署），不再等待'
            '用户明确要求；自动发布视为用户对发布/推送的预授权（根 AGENTS.md 红线 2 '
            '对常规发布的同意要求视为已满足），破坏性变更、永久删除等高风险操作仍须'
            '单独确认（如需关闭，见「用户确认的设计决策」）。'
            if args.auto_release else
            '默认不自动发布：每次改动完成后先展示与确认，用户明确要求发布时才执行发布'
            '流程（提交、推送、tag/Release、分发/部署；如需改为自动发布，见「用户确认'
            '的设计决策」）。'
        ),
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
    print(f'  项目: {name}（{desc}）  版本: {version}  分支: {args.branch}  '
          f'许可: {license_name}  发布: {"自动" if args.auto_release else "手动确认"}')
    print(f'  位置: {target}')
    if args.remote:
        print(f'  远端已配置: {args.remote}（未推送；推送前请征得用户同意）')
    print()
    print('下一步（agent 按 references/init-steps.md 校验清单执行）:')
    print('  1. 回读校验: git grep -n -E "\\{\\{[A-Z_]+\\}\\}" 应无残留；git status 与 git -C private status 应干净')
    print('  2. git check-ignore private/ 应命中（.gitignore 生效）')
    print('  3. 请用户补充 private/AGENTS.md 的「本机环境」「安装目标/部署目标」')
    print('  4. 开发前登记册: 首个 M/L 需求按 private/dev/{prd,rfc,adr,research}/'
          'INDEX.md 走开发前门禁（S 档可跳过）')
    print('  5. 阶段卡展示: 每次对话展示阶段卡（模块·子阶段/正在完成/已完成/下一步/'
          '状态 + 生命周期合规清单，以 private/dev/STATUS.md「📇 阶段卡」为准；'
          '缩写附中文翻译；每阶段/子阶段完成落盘 + git 提交）')
    print('  6. 按项目技术栈实现 scripts/ci_check.py 与 .github/workflows/ci.yml')
    print('  7. 用户确认后配置远端并推送首个提交（首次 push 不自动发 Release）')
    print('  8. 立项初期先调研: 与 agent 讨论项目思路/需求/架构/功能/产品时，'
          '要求 agent 优先在 GitHub 调研现成参考并提醒「先调研再立项」（AGENTS.md 红线 13）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
