#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lockfile.py - spec 锁文件生成、校验与 fork 登记

锁文件是 spec 包的溯源账本（规范见 spec/lockfile.md）：
记录 spec 与每个模块的来源、版本、内容指纹，防止副本漂移。

三种模式：
  generate（默认）：扫描 spec 包，生成/更新 lockfile.json；
                     合并语义——保留既有 fork / private 条目的
                     source / origin / baseline，只重算 hash / version；
  verify（--verify）：冷启动校验，比对本地内容指纹与锁文件记录，
                     不一致（漂移 / 未登记改动）则退出码 1；
  fork（--fork <id>）：把一个云端模块显式登记为 fork——脚本内部保证
                     「baseline 取云端版本、再重算 hash」的正确顺序，
                     免去手改 lockfile.json 再跑 generate 的顺序坑。

用法：
  python lockfile.py <spec 包目录>                      # 生成/更新锁文件
  python lockfile.py <spec 包目录> --verify             # 校验（漂移则退出码 1）
  python lockfile.py <spec 包目录> --fork <模块id>       # 登记某云端模块为 fork
  python lockfile.py <spec 包目录> --spec-source private # 首次生成、声明自建 spec

溯源语义（与 lockfile.md 一致）：
  - spec：记 source + origin + version 作血缘备注，不算 hash、不校验
          （spec 是用户可自由编排的装配图，不做漂移锁）；source=private
          （自建）时 origin 记 null，不指向云端；
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
    data = json.loads(mf.read_text(encoding="utf-8"))
    if "id" not in data:
        print(f"错误：manifest.json 缺 id 字段（字段表：必须填）：{mf}")
        sys.exit(1)
    return data


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


def generate(spec_dir: Path, spec_source: str = "cloud") -> None:
    """合并语义：先读既有锁文件，保留手工登记的 fork / private 条目的
    source / origin / baseline（只重算 hash / version），不静默冲掉溯源账本。

    spec_source：首次生成时声明 spec 来源（cloud / private）；既有锁文件已有
    source 时以锁文件为准（合并保留），private 的 origin 恒记 null。"""
    manifest = _read_manifest(spec_dir)
    spec_id = manifest["id"]
    manifest_modules = manifest.get("modules", [])
    if "version" not in manifest:
        print("警告：manifest.json 缺 version 字段，spec 版本暂记 0.0.0（建议补全）")

    lf = spec_dir / "lockfile.json"
    old = {}
    if lf.is_file():
        old = json.loads(lf.read_text(encoding="utf-8"))
    old_spec = old.get("spec", {})
    old_modules = old.get("modules", {})

    # spec 来源：既有锁文件优先（合并保留）；旧锁文件无 source 时按 origin 是否
    # 为 null 推断（null→自建 private），再否则用本次声明
    spec_src = old_spec.get("source")
    if spec_src is None:
        spec_src = "private" if old_spec.get("origin", "x") is None else spec_source
    spec_origin = (None if spec_src == "private"
                   else (old_spec.get("origin") or f"{CLOUD_REPO}/specs/{spec_id}"))

    lock = {
        "lockfileVersion": 1,
        # spec 只留血缘（source + origin + version），不算 hash、不校验（见 lockfile.md）
        "spec": {
            "source": spec_src,
            "origin": spec_origin,
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
            problems.append(f"模块被改动（未登记）：@{mid}"
                            f"｜如属有意 fork，跑 `lockfile.py <spec> --fork {mid}` 登记")
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


def register_fork(spec_dir: Path, module_id: str) -> int:
    """把一个云端模块显式登记为 fork（风格一：verify 检测到改动只警告，
    本命令执行登记）。

    顺序由脚本内部保证——baseline 取锁文件里当前记录的云端版本（此时 source
    仍为 cloud），不受 module.json 是否已滚版本影响，避免 baseline 被污染。"""
    lf = spec_dir / "lockfile.json"
    if not lf.is_file():
        print(f"错误：无锁文件，请先运行 generate：{lf}")
        return 1
    lock = json.loads(lf.read_text(encoding="utf-8"))
    modules = lock.get("modules", {})
    if module_id not in modules:
        print(f"错误：模块未在锁文件登记：@{module_id}（请先跑 generate）")
        return 1
    entry = modules[module_id]
    if entry.get("source") != "cloud":
        print(f"提醒：@{module_id} 当前 source={entry.get('source')}，非 cloud，无需 fork 登记")
        return 0
    mdir = spec_dir / f"@{module_id}"
    if not mdir.is_dir():
        print(f"错误：模块目录缺失：{mdir}")
        return 1

    cur_hash = _hash_dir(mdir)
    rec_hash = entry.get("hash")
    if rec_hash is not None and cur_hash != rec_hash:
        print(f"警告：@{module_id} 内容已偏离云端登记版本（检测到本地改动）")

    baseline = entry.get("version")  # 锁文件当前记录的云端版本，作为 fork 基线
    meta = _read_module_meta(mdir)
    entry["source"] = "fork"
    entry["baseline"] = baseline
    entry["version"] = meta["version"]
    entry["hash"] = cur_hash
    lf.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n",
                  encoding="utf-8")
    print(f"已登记 fork：@{module_id}  baseline={baseline}（派生自云端版本）"
          f"  version={entry['version']}  hash 已重算")
    print("后续 fork 自己的迭代：滚 module.json 的 version、改动记模块 CHANGELOG.md")
    return 0


def main() -> int:
    _configure_utf8()
    parser = argparse.ArgumentParser(description="spec 锁文件生成与校验")
    parser.add_argument("spec", help="spec 包目录（含 manifest.json）")
    parser.add_argument("--verify", action="store_true", help="校验模式（默认生成）")
    parser.add_argument("--fork", metavar="MODULE_ID",
                        help="把指定云端模块登记为 fork（source=fork、记 baseline、重算 hash）")
    parser.add_argument("--spec-source", choices=["cloud", "private"], default="cloud",
                        help="首次生成时声明 spec 来源：cloud（云端拉来，默认）/ private（自建，origin 记 null）")
    args = parser.parse_args()

    spec_dir = Path(args.spec).resolve()
    if not (spec_dir / "manifest.json").is_file():
        print(f"错误：不是 spec 包目录（缺 manifest.json）：{spec_dir}")
        return 1

    if args.fork:
        return register_fork(spec_dir, args.fork)
    if args.verify:
        return verify(spec_dir)
    generate(spec_dir, args.spec_source)
    return 0


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


if __name__ == "__main__":
    sys.exit(main())
