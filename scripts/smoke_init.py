#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""smoke_init.py - 模板/初始化链「开箱即用」冒烟自检（模板发版前必跑）

背景（AUDIT-2026-08-27 F1 教训）：v1.4.1 发版时的冒烟只验证到「初始化退出码
0 + 占位符无残留」，未穿透到冒烟项目内部实跑骨架脚本，导致
`check_dev_docs.py` 字面断言与合并阶段卡骨架失同步、「新项目首跑即红」的
缺陷漏到发布后。本脚本把冒烟深度固化为代码：

  1) 实跑 `skills/init-project/scripts/init_project.py` 初始化冒烟项目；
  2) 回读校验：`{{占位符}}` 无残留；主仓库与 private 子 git 状态干净；
     `git check-ignore private/` 命中；
  3) 冒烟项目内骨架脚本自检四连（全部要求退出码 0）：
     `ci_check.py` / `check_dev_docs.py` / `trash.py --help` /
     `pre_release_check.py --allow-placeholder`；
  4) `version.json` 回读（version 与 template_version 字段齐全）。
  5) 新机制自检（PRD-0002，v1.5.0）：`.githooks/pre-push` + `core.hooksPath`；
     `scan_secrets --strict` 全绿且注入样例被拦截；`scan_defensive --check`
     全绿；`ROADMAP.md` 存在且小节齐全；测试报告含自测区/用户验收区；状态快照
     含 📌 共识卡与重检行。

冒烟项目默认直接建在删除纪律暂存区 `_trash/qwenwork_<日期>_<时分>/` 内，
成功后任务结束时随 `python project-template/scripts/trash.py` 整体进回收站
（可恢复；避免跨盘移动）；失败保留现场并打印路径。`--keep` 改建系统临时目录
并保留；`--target` 指定目录时不做任何清理。
Stdlib-only，Python 3.9+。
Usage: python scripts/smoke_init.py [--keep] [--target DIR]
Exit code: 0 全部通过; 1 任一步失败。
"""

import argparse
import datetime
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # scripts/ 的上一级 = 工作区根
INIT_SCRIPT = ROOT / "skills" / "init-project" / "scripts" / "init_project.py"
PLACEHOLDER_RE = r"\{\{[A-Z_]+\}\}"


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


def _env() -> dict:
    env = dict(os.environ)
    env["PYTHONUTF8"] = "1"
    return env


def _run(cmd: list, cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd, cwd=str(cwd), env=_env(), capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )


def _git(args: list, cwd: Path) -> subprocess.CompletedProcess:
    return _run(["git", *args], cwd)


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(description="模板开箱即用冒烟自检")
    parser.add_argument("--keep", action="store_true",
                        help="在系统临时目录初始化并保留冒烟项目")
    parser.add_argument("--target", default=None,
                        help="指定冒烟项目目录（不做任何清理）")
    args = parser.parse_args()

    if not INIT_SCRIPT.is_file():
        print(f"[error] init script missing: {INIT_SCRIPT}", file=sys.stderr)
        return 1

    now = datetime.datetime.now()
    stamp = now.strftime("%Y%m%d-%H%M%S")
    if args.target:
        target = Path(args.target)
    elif args.keep:
        target = Path(tempfile.gettempdir()) / f"smoke-init-{stamp}"
    else:
        # 直接建在删除纪律暂存区：成功即随 trash.py 整体进回收站，
        # 失败就地保留现场；全程不跨盘移动。
        target = (ROOT / "_trash" / f"qwenwork_{now:%Y-%m-%d_%H%M}"
                  / f"smoke-init-{stamp}")
    if target.exists():
        print(f"[error] target already exists: {target}", file=sys.stderr)
        return 1

    failures = []

    def step(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
              + (f" — {detail}" if detail and not ok else ""))
        if not ok:
            failures.append(name)

    print(f"[1/5] 初始化冒烟项目: {target}")
    r = _run([sys.executable, str(INIT_SCRIPT), str(target),
              "--name", f"smoke-{stamp}", "--desc", "smoke test",
              "--license", "mit", "--author", "smoke-user"], cwd=ROOT)
    step("init_project.py 退出码 0", r.returncode == 0,
         (r.stderr or r.stdout).strip()[-300:])
    if r.returncode != 0:
        print(f"[error] 初始化失败，现场保留: {target}", file=sys.stderr)
        return 1

    print("[2/5] 回读校验（占位符 / 双仓状态 / private 忽略）")
    r = _git(["grep", "-q", "-E", PLACEHOLDER_RE], cwd=target)
    step("无 {{占位符}} 残留", r.returncode == 1,
         f"git grep exit={r.returncode}")
    r = _git(["status", "--porcelain"], cwd=target)
    step("主仓库状态干净", r.returncode == 0 and not r.stdout.strip(),
         r.stdout.strip()[:200])
    r = _git(["status", "--porcelain"], cwd=target / "private")
    step("private 子 git 状态干净", r.returncode == 0 and not r.stdout.strip(),
         r.stdout.strip()[:200])
    r = _git(["check-ignore", "private/"], cwd=target)
    step("private/ 被主仓库忽略", r.returncode == 0)

    print("[3/5] 冒烟项目内骨架脚本自检四连")
    for label, cmd in [
        ("ci_check.py", [sys.executable, "scripts/ci_check.py"]),
        ("check_dev_docs.py", [sys.executable, "scripts/check_dev_docs.py"]),
        ("trash.py --help", [sys.executable, "scripts/trash.py", "--help"]),
        ("pre_release_check.py --allow-placeholder",
         [sys.executable, "scripts/pre_release_check.py", "--allow-placeholder"]),
    ]:
        r = _run(cmd, cwd=target)
        step(f"{label} 退出码 0", r.returncode == 0,
             (r.stderr or r.stdout).strip()[-300:])

    print("[4/5] version.json 回读")
    try:
        data = json.loads((target / "version.json").read_text(encoding="utf-8"))
        ok = bool(data.get("version")) and bool(data.get("template_version"))
        step("version/template_version 字段齐全", ok, json.dumps(data))
    except (OSError, json.JSONDecodeError) as e:
        step("version.json 可读", False, str(e))

    print("[5/5] 新机制自检（推送门禁 / 路线图 / 测试报告双区 / 共识卡锚点）")
    r = _run([sys.executable, "scripts/scan_secrets.py", "--strict"], cwd=target)
    step("scan_secrets.py --strict 退出码 0", r.returncode == 0,
         (r.stderr or r.stdout).strip()[-300:])
    r = _run([sys.executable, "scripts/scan_defensive.py", "--check"], cwd=target)
    step("scan_defensive.py --check 退出码 0", r.returncode == 0,
         (r.stderr or r.stdout).strip()[-300:])
    hook = target / ".githooks" / "pre-push"
    step(".githooks/pre-push 存在", hook.is_file())
    r = _git(["config", "--get", "core.hooksPath"], cwd=target)
    step("core.hooksPath=.githooks", r.returncode == 0 and r.stdout.strip() == ".githooks",
         f"hooksPath={r.stdout.strip()!r}")
    roadmap = target / "private" / "dev" / "ROADMAP.md"
    roadmap_ok = roadmap.is_file() and all(
        f"## {sec}" in roadmap.read_text(encoding="utf-8")
        for sec in ("愿景与长期目标", "需求地图", "版本排期", "文档治理")
    )
    step("ROADMAP.md 存在且小节齐全", roadmap_ok)
    trep = (target / "private" / "dev" / "TEST-REPORT.md").read_text(
        encoding="utf-8", errors="replace"
    )
    step("TEST-REPORT 含自测区/用户验收区",
         "自测区" in trep and "用户验收区" in trep)
    status_text = (target / "private" / "dev" / "STATUS.md").read_text(
        encoding="utf-8", errors="replace"
    )
    step("STATUS 含 📌 共识卡 + 重检行",
         "📌 共识卡" in status_text and "重检：" in status_text)

    # 注入样例：扫描器必须拦截（推送前门禁的验收面）
    fake = target / "leak_test.txt"
    # 运行时拼接，避免源码字面量被 scan_secrets 误判为真实凭据；
    # 注入文件内容仍为完整假 token，可被扫描器拦截（验收面）。
    fake.write_text("ghp_" + "FAKE123456789012345678901234\n", encoding="utf-8")
    _git(["add", "-A", "--", "."], cwd=target)
    r = _run([sys.executable, "scripts/scan_secrets.py", "--strict"], cwd=target)
    step("注入样例被 scan_secrets 拦截", r.returncode != 0)
    _git(["rm", "--cached", "--ignore-unmatch", "leak_test.txt"], cwd=target)
    fake.unlink(missing_ok=True)
    r = _git(["status", "--porcelain"], cwd=target)
    if r.stdout.strip():
        _git(["add", "-A", "--", "."], cwd=target)
        _git(["commit", "-m", "chore: smoke cleanup"], cwd=target)

    print()
    if failures:
        print(f"[error] 冒烟失败 {len(failures)} 项: {failures}", file=sys.stderr)
        print(f"现场保留（排查后自行处理）: {target}", file=sys.stderr)
        return 1

    print(f"==> smoke_init: 全部通过（{target}）")
    if args.target or args.keep:
        print("冒烟项目已保留（--target/--keep 模式，不清理）")
    else:
        print("冒烟项目位于删除纪律暂存区（_trash/），任务结束时随 "
              "project-template/scripts/trash.py 整体进回收站")
    return 0


if __name__ == "__main__":
    sys.exit(main())
