#!/usr/bin/env python3
"""check_consistency.py — 漂移免疫门禁（单一真相源守卫）。

依据 RFC-0003 / ADR-0003：每条规范事实只有一个「家」（FACT 锚点圈出的正文），
其余位置只许「一句摘要 + 指针」（REF 锚点），用户文档的易变事实由脚本注入
（INJECT 锚点）。事实台账（FACT-LEDGER.md）记录每条事实的家与指纹。

三道门禁：
1. 重复检测：每个事实全局只允许一个 FACT 块，且必须在台账登记的家里；
   未登记的锚点、REF 摘要超长一律拦截；
2. 摘要指纹：FACT 正文指纹与台账不一致时拦截，并列出该事实的全部下游
   （引用/注入位置）作为显式复核清单——改完下游后用 --accept 重新登记；
3. 注入一致性：INJECT 块内容必须与唯一家正文一致，不一致用 --inject 重填。

用法：
  python check_consistency.py                          # 检测（默认根=脚本所在项目根）
  python check_consistency.py --root <路径> --ledger <台账路径> [--exclude <相对路径> ...]
  python check_consistency.py --accept <事实ID>        # 复核完下游后重新登记指纹
  python check_consistency.py --inject                 # 从唯一家重填所有 INJECT 块
  python check_consistency.py --selftest               # 内置样例自检（验证门禁有效）

退出码：0=全绿；1=有拦截项。仅用 Python 标准库。
"""

import argparse
import hashlib
import re
import sys
import tempfile
from pathlib import Path

FACT_RE = re.compile(r"<!--\s*FACT:([a-z0-9-]+)\s*-->(.*?)<!--\s*/FACT\s*-->", re.S)
REF_RE = re.compile(r"<!--\s*REF:([a-z0-9-]+)\s*-->(.*?)<!--\s*/REF\s*-->", re.S)
INJECT_RE = re.compile(r"<!--\s*INJECT:([a-z0-9-]+)\s*-->(.*?)<!--\s*/INJECT\s*-->", re.S)

REF_SUMMARY_MAX = 160  # REF 摘要归一化后的最大字符数；中文信息密度高，160 足以容纳
                       # 「一句摘要+指针」，超过即视为「变相完整展开」

EXCLUDE_DIR_NAMES = {".git", "__pycache__", "_trash", "node_modules", "dist", "build"}
EXCLUDE_PATH_PARTS = ("skills/init-project/assets",)  # 自动镜像，字节级由同步脚本保证


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\r\n", "\n")).strip()


def fingerprint(text: str) -> str:
    return hashlib.sha256(normalize(text).encode("utf-8")).hexdigest()[:12]


def iter_markdown_files(root: Path, excludes):
    for path in sorted(root.rglob("*.md")):
        if any(part in EXCLUDE_DIR_NAMES for part in path.parts):
            continue
        rel = path.relative_to(root).as_posix()
        if any(rel.startswith(prefix) for prefix in EXCLUDE_PATH_PARTS):
            continue
        if any(rel == ex or rel.startswith(ex.rstrip("/") + "/") for ex in excludes):
            continue
        yield path, rel


def parse_ledger(ledger_path: Path):
    """解析事实台账，返回 (已登记 {事实ID: 行dict}, 待安家 [行dict])。"""
    registered, pending = {}, []
    if not ledger_path.is_file():
        return registered, pending
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 6 or cells[0] in ("事实ID", "") or set(cells[0]) <= {"-"}:
            continue
        fact_id, name, status, home, fp, note = cells[:6]
        if not re.fullmatch(r"[a-z0-9-]+", fact_id):
            continue
        row = {"id": fact_id, "name": name, "status": status, "home": home,
               "fingerprint": fp, "note": note}
        if status == "已登记":
            registered[fact_id] = row
        elif status == "待安家":
            pending.append(row)
    return registered, pending


def scan_anchors(root: Path, excludes):
    """扫描全部 md 文件中的三类锚点，返回 (facts, refs, injects, file_texts)。"""
    facts, refs, injects, file_texts = [], [], [], {}
    for path, rel in iter_markdown_files(root, excludes):
        text = path.read_text(encoding="utf-8")
        file_texts[rel] = text
        for m in FACT_RE.finditer(text):
            facts.append({"id": m.group(1), "file": rel, "body": m.group(2)})
        for m in REF_RE.finditer(text):
            refs.append({"id": m.group(1), "file": rel, "summary": m.group(2)})
        for m in INJECT_RE.finditer(text):
            injects.append({"id": m.group(1), "file": rel, "body": m.group(2)})
    return facts, refs, injects, file_texts


def run_checks(root: Path, ledger_path: Path, excludes):
    """执行三道门禁，返回 (错误列表, 提示列表)。"""
    errors, infos = [], []
    registered, pending = parse_ledger(ledger_path)
    if not ledger_path.is_file():
        infos.append(f"未找到事实台账（{ledger_path}），本项目暂未启用漂移免疫门禁。")
        return errors, infos
    facts, refs, injects, _ = scan_anchors(root, excludes)

    known_ids = set(registered) | {r["id"] for r in pending}

    # 门禁 U：未登记锚点
    for kind, items in (("FACT", facts), ("REF", refs), ("INJECT", injects)):
        for item in items:
            if item["id"] not in known_ids:
                errors.append(
                    f"未登记锚点：{kind}:{item['id']}（{item['file']}）——"
                    f"新事实必须先在台账登记唯一家（规范完成定义）。")

    # 门禁 H：每个已登记事实全局唯一 FACT 块，且在家里
    fact_blocks = {}
    for f in facts:
        if f["id"] in registered:
            fact_blocks.setdefault(f["id"], []).append(f)
    for fid, row in registered.items():
        blocks = fact_blocks.get(fid, [])
        if len(blocks) != 1:
            locs = "、".join(b["file"] for b in blocks) or "（未找到）"
            errors.append(
                f"事实 {fid}（{row['name']}）的 FACT 块应有且只有一个，"
                f"实际 {len(blocks)} 个：{locs}。")
            continue
        home_rel = Path(row["home"]).as_posix()
        if blocks[0]["file"] != home_rel:
            errors.append(
                f"事实 {fid}（{row['name']}）的 FACT 块在 {blocks[0]['file']}，"
                f"台账登记的家是 {home_rel}。")
            continue
        # 门禁 F：正文指纹
        fp = fingerprint(blocks[0]["body"])
        if fp != row["fingerprint"]:
            downstream = [r["file"] for r in refs if r["id"] == fid]
            downstream += [i["file"] for i in injects if i["id"] == fid]
            down_txt = "、".join(sorted(set(downstream))) or "（暂无）"
            errors.append(
                f"事实 {fid}（{row['name']}）正文已变更（指纹 {row['fingerprint']} → {fp}）。"
                f"显式复核清单——请逐一核对下游是否需要同步：{down_txt}；"
                f"全部复核后运行 --accept {fid} 重新登记。")

    # 门禁 R：REF 摘要限长
    for r in refs:
        if len(normalize(r["summary"])) > REF_SUMMARY_MAX:
            errors.append(
                f"REF:{r['id']}（{r['file']}）摘要超长——引用处只许一句话摘要+指针，"
                f"不得变相完整展开。")

    # 门禁 I：INJECT 内容必须与唯一家一致
    for inj in injects:
        blocks = fact_blocks.get(inj["id"], [])
        if inj["id"] not in registered:
            continue
        if len(blocks) != 1:
            continue  # 已由门禁 H 报错
        if normalize(inj["body"]) != normalize(blocks[0]["body"]):
            errors.append(
                f"INJECT:{inj['id']}（{inj['file']}）内容与唯一家不一致——"
                f"注入块禁止手改，运行 --inject 重填。")

    # 提示：待安家清单（B2 工作列表，只报不拦）
    for row in pending:
        infos.append(f"待安家：事实 {row['id']}（{row['name']}）——{row['note']}")
    return errors, infos


def accept(root: Path, ledger_path: Path, excludes, fact_id: str) -> int:
    registered, _ = parse_ledger(ledger_path)
    if fact_id not in registered:
        print(f"台账中没有已登记的事实 {fact_id}。")
        return 1
    facts, _, _, _ = scan_anchors(root, excludes)
    blocks = [f for f in facts if f["id"] == fact_id]
    if len(blocks) != 1:
        print(f"事实 {fact_id} 的 FACT 块不唯一，先修复再登记。")
        return 1
    new_fp = fingerprint(blocks[0]["body"])
    text = ledger_path.read_text(encoding="utf-8")
    row = registered[fact_id]
    old_line = f"| {row['id']} | {row['name']} | {row['status']} | {row['home']} | {row['fingerprint']} | {row['note']} |"
    new_line = f"| {row['id']} | {row['name']} | {row['status']} | {row['home']} | {new_fp} | {row['note']} |"
    if old_line not in text:
        print("台账行格式与预期不符，请手工更新指纹列。")
        return 1
    ledger_path.write_text(text.replace(old_line, new_line), encoding="utf-8")
    print(f"已重新登记 {fact_id} 指纹（{row['fingerprint']} → {new_fp}）。"
          f"请确认该事实的全部下游已复核同步。")
    return 0


def inject(root: Path, excludes) -> int:
    facts, _, injects, file_texts = scan_anchors(root, excludes)
    home_body = {}
    for f in facts:
        home_body.setdefault(f["id"], f["body"])
    changed = {}
    for inj in injects:
        if inj["id"] not in home_body:
            print(f"INJECT:{inj['id']}（{inj['file']}）找不到对应 FACT 块，跳过。")
            continue
        text = file_texts[inj["file"]]
        pattern = re.compile(
            r"(<!--\s*INJECT:" + re.escape(inj["id"]) + r"\s*-->).*?(<!--\s*/INJECT\s*-->)", re.S)
        new_text, n = pattern.subn(lambda m: m.group(1) + "\n" + home_body[inj["id"]].strip() + "\n" + m.group(2), text, count=1)
        if n and new_text != text:
            changed[inj["file"]] = new_text
    for rel, new_text in changed.items():
        (root / rel).write_text(new_text, encoding="utf-8")
        print(f"已重填 {rel} 中的注入块。")
    if not changed:
        print("没有需要重填的注入块。")
    return 0


def selftest() -> int:
    """内置样例自检：验证每道门禁都能拦住该拦的情况。"""
    results = []

    def build_case(name, ledger_rows, files, expect_error_kw):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "scripts").mkdir()
            ledger = root / "scripts" / "FACT-LEDGER.md"
            header = ("# 事实台账（自检样例）\n\n"
                      "| 事实ID | 中文名 | 状态 | 家 | 指纹 | 备注 |\n"
                      "|---|---|---|---|---|---|\n")
            ledger.write_text(header + "\n".join(ledger_rows) + "\n", encoding="utf-8")
            for rel, content in files.items():
                p = root / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content, encoding="utf-8")
            errors, _ = run_checks(root, ledger, [])
            if expect_error_kw is None:
                ok = not errors
                detail = "；".join(errors) if errors else "全绿"
            else:
                ok = any(expect_error_kw in e for e in errors)
                detail = "；".join(errors) if errors else "（无拦截）"
            results.append((name, ok, detail))

    clean_fact = "<!-- FACT:demo -->\n示例正文。\n<!-- /FACT -->"
    fp = fingerprint("\n示例正文。\n")
    row = f"| demo | 示例 | 已登记 | home.md | {fp} | 样例 |"
    pend = "| messy | 多处事例 | 待安家 | — | — | 待整理 |"

    build_case("全绿基线", [row, pend],
               {"home.md": clean_fact,
                "other.md": "<!-- REF:demo -->一句话摘要，详见 home.md。<!-- /REF -->"}, None)
    build_case("重复 FACT 块被拦", [row],
               {"home.md": clean_fact, "copy.md": clean_fact}, "应有且只有一个")
    build_case("正文变更被拦并列出下游",
               [f"| demo | 示例 | 已登记 | home.md | {'0' * 12} | 样例 |"],
               {"home.md": clean_fact,
                "other.md": "<!-- REF:demo -->摘要。<!-- /REF -->"}, "正文已变更")
    build_case("REF 摘要超长被拦", [row],
               {"home.md": clean_fact,
                "other.md": "<!-- REF:demo -->" + "长" * 200 + "<!-- /REF -->"}, "摘要超长")
    build_case("未登记锚点被拦", [row],
               {"home.md": clean_fact + "\n<!-- FACT:ghost -->幽灵。<!-- /FACT -->"}, "未登记锚点")
    build_case("INJECT 不一致被拦", [row],
               {"home.md": clean_fact,
                "user.md": "<!-- INJECT:demo -->过时的内容。<!-- /INJECT -->"}, "不一致")
    build_case("待安家事实只报不拦", [pend], {"a.md": "正文"}, None)

    print("漂移免疫自检结果：")
    all_ok = True
    for name, ok, detail in results:
        mark = "通过" if ok else "失败"
        all_ok = all_ok and ok
        print(f"  [{mark}] {name}：{detail}")
    return 0 if all_ok else 1


def main():
    parser = argparse.ArgumentParser(description="漂移免疫门禁（单一真相源守卫）")
    default_root = Path(__file__).resolve().parent.parent
    parser.add_argument("--root", default=str(default_root), help="项目根目录")
    parser.add_argument("--ledger", default=None, help="事实台账路径（默认 <root>/scripts/FACT-LEDGER.md）")
    parser.add_argument("--exclude", action="append", default=[], help="排除的相对路径，可多次")
    parser.add_argument("--accept", metavar="事实ID", help="复核下游后重新登记该事实指纹")
    parser.add_argument("--inject", action="store_true", help="从唯一家重填所有 INJECT 块")
    parser.add_argument("--selftest", action="store_true", help="内置样例自检")
    args = parser.parse_args()

    if args.selftest:
        return selftest()

    root = Path(args.root).resolve()
    ledger_path = Path(args.ledger) if args.ledger else root / "scripts" / "FACT-LEDGER.md"
    excludes = [ex.replace("\\", "/").strip("/") for ex in args.exclude]

    if args.accept:
        return accept(root, ledger_path, excludes, args.accept)
    if args.inject:
        return inject(root, excludes)

    errors, infos = run_checks(root, ledger_path, excludes)
    for info in infos:
        print(f"[提示] {info}")
    if errors:
        for e in errors:
            print(f"[拦截] {e}")
        print(f"共 {len(errors)} 项拦截。修复后重跑；正文变更类须先复核下游再 --accept。")
        return 1
    print("漂移免疫门禁：全绿。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
