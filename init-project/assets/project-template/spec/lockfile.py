#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lockfile.py - spec 锁文件生成与校验

锁文件是 spec 包的溯源账本（规范见 spec/lockfile.md）：
记录 spec 与每个模块的来源、版本、内容指纹，防止副本漂移。

两种模式：
  generate（默认）：扫描 spec 包，生成/更新 lockfile.json；
                     合并语义——保留既有 fork / private 条目的
                     source / origin / baseline，只重算 hash / version；
  verify（--verify）：冷启动校验，比对本地内容指纹与锁文件记录，
                     不一致（漂移 / 未登记改动）则退出码 1。

用法：
  python lockfile.py <spec 包目录>             # 生成/更新锁文件
  python lockfile.py <spec 包目录> --verify    # 校验（漂移则退出码 1）

溯源语义（与 lockfile.md 一致）：
  - spec：只记 origin + version 作血缘备注，不算 hash、不校验
          （spec 是用户可自由编排的装配图，不做漂移锁）；
  - modules.<id>.hash：@模块 目录全部文件的指纹（顶层 add.md 除外——
                     项目内补充，改它不算漂移）；private 与 self_implemented
                     模块为 null（内容归项目，不参与指纹校验）；
  - modules.<id>.baseline：fork / self_implemented 记「派生自云端哪版」，
                     cloud / private 不带此字段；
  - lockfile.json / lockfile.md 自身不参与指纹（它们是账本，不是被溯源内容）。

Stdlib-only，Python 3.9+。
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

# 云端模块库：spec 本体在 specs/<id>，模块本体在 modules/<id>
CLOUD_REPO = "github.com/The-Daybreaker/project-spec"


def _hash_dir(d: Path) -> str:
    """对目录下全部文件计算 sha256 指纹（相对路径 + 内容，排序稳定）。

    模块顶层 add.md（项目内补充，见 spec/AGENTS.md）不参与指纹。
    内容先行尾归一化（CRLF → LF），指纹不随工作区行尾跨平台漂移。
    """
    h = hashlib.sha256()
    for f in sorted(d.rglob("*")):
        if f.is_file():
            rel = f.relative_to(d).as_posix()
            if rel == "add.md":
                continue
            h.update(rel.encode("utf-8"))
            h.update(b"\0")
            h.update(f.read_bytes().replace(b"\r\n", b"\n"))
            h.update(b"\0")
    return h.hexdigest()


def _read_manifest(spec_dir: Path) -> dict:
    mf = spec_dir / "manifest.json"
    if not mf.is_file():
        print(f"错误：找不到 manifest.json：{mf}")
        sys.exit(1)
    return json.loads(mf.read_text(encoding="utf-8"))


def _read_module_meta(mdir: Path) -> dict:
    mj = mdir / "module.json"
    if not mj.is_file():
        print(f"错误：找不到 module.json：{mj}")
        sys.exit(1)
    data = json.loads(mj.read_text(encoding="utf-8"))
    if "version" not in data:
        print(f"错误：module.json 缺 version 字段（字段表：必须填）：{mj}")
        sys.exit(1)
    return data


def generate(spec_dir: Path) -> None:
    """合并语义：先读既有锁文件，保留手工登记的 fork / private 条目的
    source / origin / baseline（只重算 hash / version），不静默冲掉溯源账本。"""
    manifest = _read_manifest(spec_dir)
    spec_id = manifest["id"]
    manifest_modules = manifest.get("modules", [])

    lf = spec_dir / "lockfile.json"
    old = {}
    if lf.is_file():
        old = json.loads(lf.read_text(encoding="utf-8"))
    old_spec = old.get("spec", {})
    old_modules = old.get("modules", {})

    lock = {
        "lockfileVersion": 1,
        # spec 只留血缘（origin + version），不算 hash、不校验（见 lockfile.md）
        "spec": {
            "origin": old_spec.get("origin", f"{CLOUD_REPO}/specs/{spec_id}"),
            "version": manifest.get("version", "0.0.0"),
        },
        "modules": {},
    }

    for mid in manifest_modules:
        mdir = spec_dir / f"@{mid}"
        if not mdir.is_dir():
            print(f"警告：模块目录缺失，跳过：{mdir}")
            continue
        meta = _read_module_meta(mdir)
        prev = old_modules.get(mid, {})
        # 私有（module.json 声明或锁文件已登记）与 self_implemented（云端给骨架、
        # 项目自填）都不参与指纹校验：hash 置 null
        is_private = meta.get("private", False) or prev.get("source") == "private"
        is_self_impl = meta.get("self_implemented", False)
        source = "private" if is_private else prev.get("source", "cloud")
        exempt = is_private or is_self_impl
        entry = {
            "source": source,
            "origin": None if is_private else prev.get("origin", f"{CLOUD_REPO}/modules/{mid}"),
            "version": meta["version"],
        }
        # baseline：fork / self_implemented 记「派生自云端哪版」；cloud / private 不带。
        # 首次登记取当时云端版本（prev.version 优先，其次 module.json 版本），之后保留。
        baseline = prev.get("baseline")
        if baseline is None and (source == "fork" or (is_self_impl and not is_private)):
            baseline = prev.get("version") or meta["version"]
        if baseline is not None:
            entry["baseline"] = baseline
        entry["hash"] = None if exempt else _hash_dir(mdir)
        lock["modules"][mid] = entry

    dropped = [mid for mid in old_modules if mid not in manifest_modules]
    if dropped:
        print("警告：丢弃锁文件中不在 manifest 的条目："
              + ", ".join(f"@{mid}" for mid in dropped)
              + "（仍需它们请先登记进 manifest）")

    lf.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n",
                  encoding="utf-8")
    print(f"已生成锁文件：{lf}")
    print(f"  spec: {spec_id} {lock['spec']['version']}")
    print(f"  modules: {len(lock['modules'])} 个")


def verify(spec_dir: Path) -> int:
    manifest = _read_manifest(spec_dir)
    spec_id = manifest["id"]
    lf = spec_dir / "lockfile.json"
    if not lf.is_file():
        print(f"错误：无锁文件，请先运行 generate：{lf}")
        return 1

    lock = json.loads(lf.read_text(encoding="utf-8"))
    problems = []

    # spec 层不做校验（只留 origin + version 血缘，见 lockfile.md）

    # 模块层
    lock_modules = lock.get("modules", {})
    manifest_modules = manifest.get("modules", [])
    for mid in manifest_modules:
        mdir = spec_dir / f"@{mid}"
        if not mdir.is_dir():
            problems.append(f"模块目录缺失：@{mid}")
            continue
        if mid not in lock_modules:
            problems.append(f"模块未登记：@{mid}")
            continue
        rec_hash = lock_modules[mid].get("hash")
        # hash 为 null = 私有 / self_implemented 模块，不参与指纹校验（见 lockfile.md）
        if rec_hash is not None and rec_hash != _hash_dir(mdir):
            problems.append(f"模块被改动（未登记）：@{mid}")
    for mid in lock_modules:
        if mid not in manifest_modules:
            problems.append(f"锁文件有残留条目（已不在 manifest）：@{mid}")

    # 磁盘存在但 manifest 未声明的模块目录（如删条目忘删目录）
    declared = {f"@{mid}" for mid in manifest_modules}
    for p in sorted(spec_dir.iterdir()):
        if p.is_dir() and p.name.startswith("@") and p.name not in declared:
            problems.append(f"模块目录存在但 manifest 未声明：{p.name}")

    if problems:
        print(f"校验失败（{spec_id}），发现 {len(problems)} 处漂移：")
        for p in problems:
            print(f"  - {p}")
        print("若属有意改动，请按 lockfile.md 更新锁文件（显式操作）。")
        return 1
    print(f"校验通过：{spec_id}，内容与锁文件一致")
    return 0


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(description="spec 锁文件生成与校验")
    parser.add_argument("spec", help="spec 包目录（含 manifest.json）")
    parser.add_argument("--verify", action="store_true", help="校验模式（默认生成）")
    args = parser.parse_args()

    spec_dir = Path(args.spec).resolve()
    if not (spec_dir / "manifest.json").is_file():
        print(f"错误：不是 spec 包目录（缺 manifest.json）：{spec_dir}")
        return 1

    if args.verify:
        return verify(spec_dir)
    generate(spec_dir)
    return 0


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


if __name__ == "__main__":
    sys.exit(main())
