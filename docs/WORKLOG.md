# WORKLOG — 通用项目模板工作区 工作进度日志

> 模块：项目专用。
> 使用规则：每完成一小阶段先更新本文件与受影响文档；新对话/新任务开始时，若旧内容
> 已完结或文档已膨胀，**先询问用户是否清理**（已完结条目归档到「历史记录」，或整段
> 移入 `_trash/`），得到确认后才清理；绝不自动删除。
- 最后更新：2026-08-25

## 当前任务

- 需求：全面了解并审计本工作区（通用项目模板母项目）——全流程是否规范、生命周期
  是否完整、通用性/规范性等方方面面。
- 目标/验收：通读全部规范与实现；自动化验证（同步哈希 / quick_validate /
  py_compile / 版本号 grep / 占位符 / 编码 / git 跟踪）；端到端冒烟（初始化 +
  校验清单 + 脚本行为 + 非空拒绝）；输出审计结论；按规则修复发现的状态文档过时
  （CHANGELOG 未发版区段 HEAD 引用/缺条目、WORKLOG 当前任务切换）；经验自动沉淀；
  清理测试产物；自动提交。
- 计划步骤：
  1. 通读规范与文档（根 AGENTS / 模板 AGENTS×2 / WORKLOG / CHANGELOG / README /
     docs / scripts / skill）
  2. 自动化验证（sync 哈希、quick_validate、py_compile、版本号 grep、占位符、
     行尾/BOM、git 跟踪）
  3. 端到端冒烟（init_project 初始化 + 校验清单 + ci_check / pre_release /
     bump_version / trash / 非空目录拒绝）
  4. 汇总审计结论 + 修复 P2（CHANGELOG 未发版区段 HEAD 过时/缺条目、
     WORKLOG 当前任务切换）
  5. 经验自动沉淀 + 清理测试产物（__pycache__ / _ftest）+ 自动提交 + 汇报

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
- [ ] P3 建议清单待用户决策：init_project.py UTF-8 输出；工作区根补
      .gitattributes（行尾归一化）；模板示例引用 KnowOps 是否改中性表述；
      SKILL.md/init-steps.md 内嵌版本号 1.1.1 的单一来源；UPGRADE.md「sync_template」
      表述；CONTRIBUTING「CHANGELOG 对齐意图」措辞；项目归档/退役环节缺失；
      EXPERIENCE-TO-KB 索引顺序

## 历史记录

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
