# WORKLOG — 通用项目模板工作区 工作进度日志

> 模块：项目专用。
> 使用规则：每完成一小阶段先更新本文件与受影响文档；新对话/新任务开始时，若旧内容
> 已完结或文档已膨胀，**先询问用户是否清理**（已完结条目归档到「历史记录」，或整段
> 移入 `_trash/`），得到确认后才清理；绝不自动删除。
- 最后更新：2026-08-25

## 当前任务

- 需求：两个 version 文件合并为一个 JSON——
  工作区根与模板骨架统一使用 `version.json`（`version` + `template_version` 两字段），
  删除 `VERSION` / `TEMPLATE_VERSION`，脚本、CI、skill 与全部文档引用同步更新。
- 目标/验收：全工作区无 `VERSION` / `TEMPLATE_VERSION` 文件与引用残留（历史除外）；
  bump_version / pre_release_check / release.yml / init_project 均读 `version.json`；
  sync 0 差异；quick_validate 通过；初始化冒烟通过；自动提交。
- 计划步骤：
  1. 创建 version.json（工作区 + 模板），删除 VERSION / TEMPLATE_VERSION
  2. 改造脚本与 CI（bump_version / pre_release_check / release.yml / init_project）
  3. 更新全部文档引用（模板 AGENTS / 私有 AGENTS / README / UPGRADE / audit-checklist /
     CONTRIBUTING / DESIGN / CHANGELOG / SKILL / init-steps / 工作区文档）
  4. sync + 校验 + 冒烟 + 自动提交 + 汇报

## 阶段记录

| 阶段 | 状态 | 完成内容 | 变更文件 | 验证 | 下一步 |
|---|---|---|---|---|---|
| 1 文件替换 | ✅ | 工作区 + 模板新建 version.json；删除 VERSION / TEMPLATE_VERSION | version.json ×2 + 删除 3 文件 | 结构检查 | 脚本改造 |
| 2 脚本/CI | ✅ | bump_version / pre_release_check / release.yml / init_project 读 version.json | 4 文件 | py_compile + 冒烟 | 文档更新 |
| 3 文档更新 | ✅ | 模板 AGENTS / 私有 AGENTS / README / UPGRADE / audit-checklist / CONTRIBUTING / DESIGN / CHANGELOG / SKILL / init-steps / 工作区文档 | 13 文件 | grep 残留核对 | sync+校验 |
| 4 sync+校验+提交 | ✅ | sync 29 文件 0 差异；quick_validate；py_compile；初始化冒烟；git add + commit | 全部 | 通过 | 汇报 |

## 待办/遗留

- [x] 上一任务（模板 v1.1.0 第二轮改造）9/9 完结
- [x] 上一任务（文档治理经验吸收）6/6 完结
- [x] 上一任务（A–G 经验合入 v1.1.1，提交 1e02c3e + tag v1.1.1）完结
- [x] 本任务（审计修复 + 目录整理 + 模板结构整理 + 子目录 README 改名 + version.json 合并）完结
- [ ] 工作区无 git 远端，改动未推送（N/A 或用户决定）
- [ ] 模板根其余 7 个文件（AGENTS/README/LICENSE/version.json/
      .gitignore/.gitattributes/.editorconfig）为入口与工具必需；如仍想精简需单独评估

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
- 2026-08-25 模板 v1.1.0 第二轮改造：阶段落盘（WORKLOG）、双模块、【通用】/【项目专用】
  标注、经验文档×2（完整条目）、删除纪律（_trash + trash.py）、模板升级机制
  （TEMPLATE_VERSION + CHANGELOG + UPGRADE）、红线 13→15（阶段落盘、上下文恢复重读）。
  端到端测试全部通过（详情见阶段记录）。
- 2026-08-25 文档治理经验吸收：文档维护清单、红线 12/5 强化、文档治理约定（正文即当前
  状态；覆盖原文、禁止 AI 追加历史、留痕仅 CHANGELOG 一行、废案走 _trash、可恢复性由
  删除机制保证）、审计清单「文档无缝衔接」专项；未写入参考来源。
- 2026-08-25 v1.1.0 已提交并打 tag（c58a816）。
