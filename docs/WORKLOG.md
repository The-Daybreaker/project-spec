# WORKLOG — 通用项目模板工作区 工作进度日志

> 模块：项目专用。
> 使用规则：每完成一小阶段先更新本文件与受影响文档；新对话/新任务开始时，若旧内容
> 已完结或文档已膨胀，**先询问用户是否清理**（已完结条目归档到「历史记录」，或整段
> 移入 `_trash/`），得到确认后才清理；绝不自动删除。
- 最后更新：2026-08-25

## 当前任务

- 需求：修复全面审计发现的 P2 文档维护问题并排查根因——
  ① WORKLOG 硬事实校准（sync 为 28 文件）；② 当前任务切换（上一任务已完结）；
  ③ CHANGELOG 补充未发版变更区段；④ 根因：WORKLOG 生命周期缺两个收口
  （任务开始切换当前任务、收尾校准硬事实），对应规则补强；
  ⑤ 经验自动沉淀（必做）：根因经验追加到 `docs/EXPERIENCE-TO-KB.md`，
     维护约定明确「每轮对话结束自动沉淀、不询问」。
- 目标/验收：WORKLOG 阶段记录硬事实与实际一致（28 文件）；当前任务=本次；
  CHANGELOG 含「未发版变更（v1.1.2 候选）」区段；模板规则补强并 sync 0 差异；
  经验已自动追加；维护约定含「经验自动沉淀」；quick_validate 通过；自动提交。
- 计划步骤：
  1. 修复 WORKLOG 硬事实（29→28）+ 切换当前任务
  2. CHANGELOG 补未发版变更区段
  3. 规则补强（工作区 AGENTS 维护约定 + 模板 WORKLOG 使用规则/完成清单/audit-checklist）
  4. sync + 校验 + 自动提交 + 汇报

## 阶段记录

| 阶段 | 状态 | 完成内容 | 变更文件 | 验证 | 下一步 |
|---|---|---|---|---|---|
| 1 WORKLOG 修复 | ✅ | 阶段记录 29→28；当前任务切换为本次；旧任务归档历史 | docs/WORKLOG.md | 回读核对 | CHANGELOG |
| 2 CHANGELOG | ✅ | 新增「未发版变更（v1.1.2 候选）」区段（近 4 轮改动） | docs/CHANGELOG.md | 内容核对 | 规则补强 |
| 3 规则补强 | ✅ | 工作区 AGENTS 维护约定第 6 条；模板 WORKLOG 使用规则 / 完成清单 / audit-checklist | 4 文件 | 引用核对 | sync+校验 |
| 4 sync+校验+提交 | ✅ | sync 28 文件 0 差异；quick_validate；py_compile；git add + commit | 全部 | 通过 | 汇报 |
| 5 经验自动沉淀 | ✅ | 根因经验追加到 docs/EXPERIENCE-TO-KB.md；维护约定明确自动沉淀（不询问） | 3 文件 | 回读核对 | 汇报 |

## 待办/遗留

- [x] 上一任务（模板 v1.1.0 第二轮改造）9/9 完结
- [x] 上一任务（文档治理经验吸收）6/6 完结
- [x] 上一任务（A–G 经验合入 v1.1.1，提交 1e02c3e + tag v1.1.1）完结
- [x] 上一任务（version.json 合并，提交 733065f）完结（阶段记录已归档）
- [x] 本任务（P2 修复 + WORKLOG 生命周期收口 + 经验自动沉淀）5/5 完结
- [ ] 工作区无 git 远端，改动未推送（N/A 或用户决定）
- [ ] 模板根其余 7 个文件（AGENTS/README/LICENSE/version.json/
      .gitignore/.gitattributes/.editorconfig）为入口与工具必需；如仍想精简需单独评估
- [ ] 下次发版 v1.1.2：把「未发版变更」区段并入正式条目，并 bump version.json / 打 tag

## 历史记录

- 2026-08-25 模板 v1.1.1：A–G 实践项目经验合入，已提交并打 tag（1e02c3e / v1.1.1）
  完结（审计确认）。
- 2026-08-25 全面审计 + 修复整理：审计发现 3 处过时版本引用、WORKLOG 状态失真、
  重复表格行、发版同步约定盲区；修复并整理母项目目录（docs/ + scripts/），
  新建 docs/EXPERIENCE-TO-KB.md；模板根布局随后在二次整理中精简。
- 2026-08-25 目录结构二次整理：README 回根；project-template 精简
  （CONTRIBUTING → docs/、version-sync.json → scripts/，bump_version 同步更新）；
  修正「工作区 .git 只读」错误描述，改动由 agent 自动提交。
- 2026-08-25 子目录 README 改名：docs/README.md → docs/DOCS.md、
  private/README.md → private/PRIVATE.md、private/test/README.md →
  private/test/TEST.md（避免与项目根 README 混淆、便于索引），全部引用同步更新并提交。
- 2026-08-25 版本文件合并：`VERSION` / `TEMPLATE_VERSION` 合并为根 `version.json`
  （`version` + `template_version` 两字段），脚本/CI/skill/文档全部更新，提交。
- 2026-08-25 P2 修复 + 根因：WORKLOG 硬事实 29→28、当前任务切换、CHANGELOG 补
  未发版变更区段；根因=WORKLOG 生命周期缺两个收口（任务开始切换当前任务、收尾
  校准硬事实），规则补强（工作区维护约定 + 模板 WORKLOG/完成清单/audit-checklist）。
- 2026-08-25 模板 v1.1.0 第二轮改造：阶段落盘（WORKLOG）、双模块、【通用】/【项目专用】
  标注、经验文档×2（完整条目）、删除纪律（_trash + trash.py）、模板升级机制
  （TEMPLATE_VERSION + CHANGELOG + UPGRADE）、红线 13→15（阶段落盘、上下文恢复重读）。
  端到端测试全部通过（详情见阶段记录）。
- 2026-08-25 文档治理经验吸收：文档维护清单、红线 12/5 强化、文档治理约定（正文即当前
  状态；覆盖原文、禁止 AI 追加历史、留痕仅 CHANGELOG 一行、废案走 _trash、可恢复性由
  删除机制保证）、审计清单「文档无缝衔接」专项；未写入参考来源。
- 2026-08-25 v1.1.0 已提交并打 tag（c58a816）。
