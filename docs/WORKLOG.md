# WORKLOG — 通用项目模板工作区 工作进度日志

> 模块：项目专用。
> 使用规则：每完成一小阶段先更新本文件与受影响文档；新对话/新任务开始时，若旧内容
> 已完结或文档已膨胀，**先询问用户是否清理**（已完结条目归档到「历史记录」，或整段
> 移入 `_trash/`），得到确认后才清理；绝不自动删除。
- 最后更新：2026-08-25

## 当前任务

- 需求：按用户注释反馈实施全面审计 P3 建议——① init_project.py UTF-8 输出；
  ② UPGRADE.md 澄清 sync_template 仅存在于模板母项目；③ CONTRIBUTING 对齐意图
  措辞修正（并确认承载文档）；④ EXPERIENCE-TO-KB 索引与正文顺序统一；
  ⑤ SKILL/init-steps 版本号单一来源（改引用 version.json + sync 自动化校验）。
- 目标/验收：5 项全部实施；模板改动已 sync 0 差异；quick_validate / py_compile /
  初始化冒烟通过；版本号仅 `SKILL.md metadata.version` 保留 1.1.1；经验自动沉淀；
  自动提交。
- 计划步骤：
  1. init_project.py 增加 `_configure_utf8`（对齐其他脚本）
  2. UPGRADE.md 澄清 + CONTRIBUTING 措辞修正
  3. EXPERIENCE-TO-KB 索引顺序统一
  4. SKILL/init-steps 版本号改引用 + sync_template.py 新增 metadata.version
     一致性校验
  5. 同步 + 校验 + 冒烟 + 经验沉淀 + 清理 + 自动提交 + 汇报

## 阶段记录

| 阶段 | 状态 | 完成内容 | 变更文件 | 验证 | 下一步 |
|---|---|---|---|---|---|
| 1 WORKLOG 修复 | ✅ | 阶段记录 29→28；当前任务切换为本次；旧任务归档历史 | docs/WORKLOG.md | 回读核对 | CHANGELOG |
| 2 CHANGELOG | ✅ | 新增「未发版变更（v1.1.2 候选）」区段（近 4 轮改动） | docs/CHANGELOG.md | 内容核对 | 规则补强 |
| 3 规则补强 | ✅ | 工作区 AGENTS 维护约定第 6 条；模板 WORKLOG 使用规则 / 完成清单 / audit-checklist | 4 文件 | 引用核对 | sync+校验 |
| 4 sync+校验+提交 | ✅ | sync 28 文件 0 差异；quick_validate；py_compile；git add + commit | 全部 | 通过 | 汇报 |
| 5 经验自动沉淀 | ✅ | 根因经验追加到 docs/EXPERIENCE-TO-KB.md；维护约定明确自动沉淀（不询问） | 3 文件 | 回读核对 | 汇报 |
| 6 审计·文档通读 | ✅ | 通读根 AGENTS / README / docs 全部 + 模板 AGENTS×2 + 模板 docs/scripts/private + skill | 无（只读） | 内容理解 | 自动化验证 |
| 7 审计·自动化验证 | ✅ | sync 28 文件 0 差异；quick_validate 通过；py_compile 通过；版本号 grep 无残留；占位符 9 类全覆盖；无 BOM、索引均 LF；git 跟踪齐全（private 骨架 20 文件） | 无 | 全部通过 | 冒烟测试 |
| 8 审计·端到端冒烟 | ✅ | init_project 初始化（28 文件/13 替换）+ 校验清单全过；ci_check / trash / pre_release（含占位拦截）/ bump_version / 非空目录拒绝 行为符合文档 | _ftest/（已清理） | 通过 | 汇总修复 |
| 9 修复+沉淀+提交 | ✅ | CHANGELOG 未发版区段移除 HEAD 固定引用+补条目；WORKLOG 当前任务切换；EXPERIENCE-TO-KB 追加本轮经验；清理 __pycache__ / _ftest；自动提交 | docs/CHANGELOG.md docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md | 回读核对+git status | 汇报 |
| 10 P3·UTF-8 输出 | ✅ | init_project.py 增加 `_configure_utf8`（main 入口调用）；冒烟输出无乱码 | init-project/scripts/init_project.py | 初始化冒烟通过 | UPGRADE |
| 11 P3·UPGRADE 澄清 | ✅ | 「应用方式」注明 sync_template.py 仅存在于模板母项目、目标项目不运行 | project-template/docs/UPGRADE.md（已 sync） | 引用核对 | CONTRIBUTING |
| 12 P3·CONTRIBUTING 措辞 | ✅ | 「新需求先对齐意图」改为 DESIGN + 用户决策 + WORKLOG 承载，移除 CHANGELOG 误述 | project-template/docs/CONTRIBUTING.md（已 sync） | 内容核对 | EXP-KB 索引 |
| 13 P3·EXP-KB 索引 | ✅ | 索引顺序与正文一致（新条目在前） | docs/EXPERIENCE-TO-KB.md | 回读核对 | 版本单一来源 |
| 14 P3·版本单一来源 | ✅ | SKILL/init-steps 正文移除硬编码 1.1.1 改引用 version.json；sync_template.py 新增 metadata.version==template_version 校验（实测通过）；维护约定同步 | 5 文件 | sync / quick_validate / py_compile 通过 | 收尾 |
| 15 收尾 | ✅ | 清理测试产物；经验自动沉淀；sync 失败路径实测（9.9.9 拦截）；自动提交 | docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md | 回读核对+git status | 汇报 |

## 待办/遗留

- [x] 上一任务（模板 v1.1.0 第二轮改造）9/9 完结
- [x] 上一任务（文档治理经验吸收）6/6 完结
- [x] 上一任务（A–G 经验合入 v1.1.1，提交 1e02c3e + tag v1.1.1）完结
- [x] 上一任务（version.json 合并，提交 733065f）完结（阶段记录已归档）
- [x] 本任务（P2 修复 + WORKLOG 生命周期收口 + 经验自动沉淀）5/5 完结
- [x] 本任务（全面审计 + P2 修复 + 经验沉淀）9/9 完结
- [ ] 工作区无 git 远端，改动未推送（N/A 或用户决定）
- [ ] 模板根其余 7 个文件（AGENTS/README/LICENSE/version.json/
      .gitignore/.gitattributes/.editorconfig）为入口与工具必需；如仍想精简需单独评估
- [ ] 下次发版 v1.1.2：把「未发版变更」区段并入正式条目，并 bump version.json / 打 tag
- [x] P3 #1/#2/#3/#4/#5 已实施（UTF-8 输出、UPGRADE 澄清、CONTRIBUTING 措辞、
      EXP-KB 索引、版本单一来源 + sync 自动化校验）
- [x] 本任务（P3 建议实施）15/15 完结
- [ ] P3 #6 工作区根补 .gitattributes（行尾归一化）、#7 模板补「项目归档/退役」
      环节：未决策，待用户确认

## 历史记录

- 2026-08-25 P3 建议实施（按注释反馈）：init_project.py UTF-8 输出；UPGRADE.md
  澄清 sync_template 归属（目标项目无此脚本）；CONTRIBUTING 对齐意图措辞
  （DESIGN / 用户决策 / WORKLOG 承载）；EXPERIENCE-TO-KB 索引统一；SKILL/init-steps
  版本号单一来源（正文改引用 version.json + sync 自动化校验 metadata.version）。
- 2026-08-25 全面审计（第二次）：通读全部规范/实现 + 自动化验证 + 端到端冒烟全部
  通过（sync 28 文件 0 差异、quick_validate 通过、初始化校验清单全过）；发现
  P2×2（CHANGELOG 未发版区段 HEAD 引用过时 733065f→3006b97 且缺「经验自动沉淀」
  条目、WORKLOG 当前任务未随新任务切换）已修复；P3 建议清单待用户决策。
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
