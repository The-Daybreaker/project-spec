#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_dev_docs.py - validate pre-development doc registers (PRD/RFC/ADR/RESEARCH)

Enforces the state machines defined in private/dev/{prd,rfc,adr,research}/INDEX.md
so the pre-development docs cannot silently drift:

  1) register dirs + INDEX.md exist (entity dirs, no lazy loading);
  2) doc file names <TYPE>-NNNN-<slug>.md; numbering contiguous from 0001 (no gaps,
     no reuse);
  3) header metadata: status within allowed enum, PRD priority, required fields;
  4) state-machine rules: PRD 已定稿/已实现 need 定稿 date (+ required sections),
     已实现 needs 实现版本; RFC 已采纳/已否决 need 采纳日期; ADR status is 已接受
     or 已被 ADR-XXXX 取代 (referenced ADR must exist); RESEARCH 已完成/已过期
     need 最近更新, 已过期 needs 取代 target;
  5) INDEX.md table rows: every doc file is registered, every row references an
     existing file, INDEX status matches the doc header status;
  6) private/AGENTS.md D-xxx entries: "详见 ADR-XXXX" references exist;
  7) STATUS.md snapshot: 阶段卡 + 任务影响清单（含要读文档清单）+ 生命周期合规清单
     present, 当前阶段 module in P1-P5 (phase carrier for recovery / observability).

Empty registers (INDEX.md only) pass, so freshly initialized projects are fine.
Stdlib-only, read-only, Python 3.9+; repo root resolved from script location.

Usage: python scripts/check_dev_docs.py
Exit code: 0 pass; 1 issues found (fix before release).
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEV = REPO_ROOT / "private" / "dev"

REGISTERS = {
    "PRD": ("prd", {"草稿", "已定稿", "已实现", "已废弃"}),
    "RFC": ("rfc", {"草稿", "评审中", "已采纳", "已否决", "已废弃"}),
    "ADR": ("adr", None),  # free-form: 已接受 or 已被 ADR-XXXX 取代
    "RESEARCH": ("research", {"进行中", "已完成", "已过期"}),
}

DOC_RE = re.compile(r"^(PRD|RFC|ADR|RESEARCH)-(\d{4})-(.+)\.md$")
ROW_ID_RE = re.compile(r"^(PRD|RFC|ADR|RESEARCH)-(\d{4})$")
ADR_STATUS_RE = re.compile(r"^已被 ADR-(\d{4}) 取代$")


def _configure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass


def _header_field(text: str, key: str) -> str:
    # 头部字段可能在同一行用 `|` 分隔（如 `> 状态：草稿 | 优先级：P2 | …`），
    # 也可能每个字段单独一行；按 `|` 分段后在段内匹配 `key：value`。
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith(">"):
            continue
        header = stripped.lstrip(">").strip()
        for seg in header.split("|"):
            m = re.match(rf"^\s*{re.escape(key)}[：:]\s*(.*?)\s*$", seg)
            if m:
                return m.group(1).strip()
    return ""


def _has_section(text: str, title: str) -> bool:
    return re.search(rf"(?m)^##\s+{re.escape(title)}\s*$", text) is not None


def _iter_docs(register_dir: Path) -> list:
    return sorted(
        p for p in register_dir.glob("*.md")
        if p.name.lower() != "index.md"
    )


def _read_text(path: Path, problems: list):
    """Read a file as UTF-8; on decode/IO failure report and return None."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        problems.append(
            f"{path.relative_to(REPO_ROOT)}: not valid UTF-8 (decode error); "
            f"fix the file encoding"
        )
    except OSError as e:
        problems.append(f"{path.relative_to(REPO_ROOT)}: read failed: {e}")
    return None


def _check_doc(typ: str, path: Path, statuses: set, problems: list) -> None:
    rel = path.relative_to(REPO_ROOT)
    text = _read_text(path, problems)
    if text is None:
        return
    status = _header_field(text, "状态")
    if statuses is not None and status and status not in statuses:
        problems.append(
            f"{rel}: invalid status {status!r} (allowed: {sorted(statuses)})"
        )

    if typ == "PRD":
        if not _header_field(text, "优先级"):
            problems.append(f"{rel}: missing 优先级 header field")
        if status in ("已定稿", "已实现"):
            if _header_field(text, "定稿") in ("", "—"):
                problems.append(f"{rel}: status={status} but 定稿 date missing")
            for sec in ("背景与目标", "用户与场景", "需求范围", "验收标准", "不在范围"):
                if not _has_section(text, sec):
                    problems.append(f"{rel}: status={status} but missing section ## {sec}")
        if status == "已实现" and _header_field(text, "实现版本") in ("", "—"):
            problems.append(f"{rel}: status=已实现 but 实现版本 missing")

    elif typ == "RFC":
        if not _header_field(text, "依据 PRD"):
            problems.append(f"{rel}: missing 依据 PRD header field")
        if status in ("已采纳", "已否决") and _header_field(text, "采纳日期") in ("", "—"):
            problems.append(f"{rel}: status={status} but 采纳日期 missing")

    elif typ == "ADR":
        if not status:
            problems.append(f"{rel}: missing 状态 header field")
        elif status != "已接受":
            m = ADR_STATUS_RE.match(status)
            if not m:
                problems.append(
                    f"{rel}: invalid ADR status {status!r} "
                    f"(expected 已接受 or 已被 ADR-XXXX 取代)"
                )
            else:
                n = int(m.group(1))
                self_n = int(DOC_RE.match(path.name).group(2))
                if n == self_n:
                    problems.append(f"{rel}: ADR cannot supersede itself")
                elif not list((DEV / "adr").glob(f"ADR-{n:04d}-*.md")):
                    problems.append(f"{rel}: superseded by missing ADR-{n:04d}")

    elif typ == "RESEARCH":
        if status in ("已完成", "已过期") and _header_field(text, "最近更新") in ("", "—"):
            problems.append(f"{rel}: status={status} but 最近更新 missing")
        if status == "已过期" and _header_field(text, "取代") in ("", "—"):
            problems.append(f"{rel}: status=已过期 but 取代 target missing")


def _check_register(typ: str, dirname: str, statuses: set, problems: list) -> None:
    d = DEV / dirname
    if not d.is_dir():
        problems.append(f"missing register dir: private/dev/{dirname}/ (see INDEX.md)")
        return
    index = d / "INDEX.md"
    if not index.is_file():
        problems.append(f"missing register index: private/dev/{dirname}/INDEX.md")
        return

    numbers = []
    for p in _iter_docs(d):
        m = DOC_RE.match(p.name)
        if not m:
            problems.append(
                f"bad file name (expect {typ}-NNNN-<slug>.md): {p.relative_to(REPO_ROOT)}"
            )
            continue
        if m.group(1) != typ:
            problems.append(f"type mismatch in file name: {p.name}")
            continue
        numbers.append(int(m.group(2)))
        _check_doc(typ, p, statuses, problems)

    if numbers:
        expected = list(range(1, max(numbers) + 1))
        if sorted(numbers) != expected:
            problems.append(
                f"{typ} numbering not contiguous from 0001: "
                f"found {sorted(numbers)}, expected {expected}"
            )

    index_text = _read_text(index, problems)
    if index_text is None:
        return
    rows = []
    for line in index_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) >= 3 and ROW_ID_RE.match(cells[0]):
            rows.append(cells)

    file_by_id = {}
    for p in _iter_docs(d):
        m = DOC_RE.match(p.name)
        if m:
            file_by_id[int(m.group(2))] = p

    row_ids = {int(ROW_ID_RE.match(c[0]).group(2)) for c in rows}
    missing_rows = sorted(set(file_by_id) - row_ids)
    if missing_rows:
        problems.append(
            f"{typ} INDEX.md missing row(s): "
            + ", ".join(f"{typ}-{n:04d}" for n in missing_rows)
        )
    extra_rows = sorted(row_ids - set(file_by_id))
    if extra_rows:
        problems.append(
            f"{typ} INDEX.md row(s) without file: "
            + ", ".join(f"{typ}-{n:04d}" for n in extra_rows)
        )

    for cells in rows:
        n = int(ROW_ID_RE.match(cells[0]).group(2))
        p = file_by_id.get(n)
        if not p:
            continue
        header_status = _header_field(p.read_text(encoding="utf-8"), "状态")
        row_status = cells[2]
        if header_status and row_status and header_status != row_status:
            problems.append(
                f"{p.relative_to(REPO_ROOT)} status mismatch: "
                f"header={header_status}, INDEX={row_status}"
            )


def _check_cross_refs(problems: list) -> None:
    agents = REPO_ROOT / "private" / "AGENTS.md"
    if not agents.is_file():
        problems.append("missing private/AGENTS.md (required for cross-ref check)")
        return
    agents_text = _read_text(agents, problems)
    if agents_text is None:
        return
    for line in agents_text.splitlines():
        if not line.lstrip().startswith("- D-"):
            continue
        for m in re.finditer(r"ADR-(\d{4})", line):
            n = int(m.group(1))
            if not list((DEV / "adr").glob(f"ADR-{n:04d}-*.md")):
                problems.append(
                    f"private/AGENTS.md references missing ADR-{n:04d} "
                    f"(line: {line.strip()[:80]})"
                )


def _check_status(problems: list) -> None:
    """Validate the STATUS.md snapshot (phase card + impact list + lifecycle checklist)."""
    status = DEV / "STATUS.md"
    if not status.is_file():
        problems.append(f"missing {status.relative_to(REPO_ROOT)} (STATUS snapshot)")
        return
    text = _read_text(status, problems)
    if text is None:
        return

    # 阶段卡：模块 P1-P5 枚举 + 阶段卡区块
    m = re.search(r"(?ms)^## 当前阶段(.*?)(?=\n## |\Z)", text)
    stage_section = m.group(1) if m else ""
    if not re.search(r"模块[：:]\s*P[1-5]", stage_section):
        problems.append(
            "STATUS.md 当前阶段 section missing 模块 P1-P5 (phase module; "
            "see template STATUS.md skeleton / private/dev/PHASES.md)"
        )
    for block in ("阶段卡", "任务影响清单", "要读文档清单", "生命周期合规清单"):
        if block not in text:
            problems.append(f"STATUS.md missing {block} section/field (snapshot skeleton)")


def main() -> int:
    _configure_utf8()
    problems = []

    if not DEV.is_dir():
        problems.append(f"missing private/dev dir: {DEV}")
    else:
        for typ, (dirname, statuses) in REGISTERS.items():
            _check_register(typ, dirname, statuses, problems)
        _check_cross_refs(problems)
        _check_status(problems)

    print(f"==> check_dev_docs: {len(problems)} issue(s)")
    for p in problems:
        print(f"  [error] {p}")
    if problems:
        print("[error] fix pre-development doc registers before release.", file=sys.stderr)
        return 1
    print("==> check_dev_docs: passed (PRD/RFC/ADR/RESEARCH registers consistent)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
