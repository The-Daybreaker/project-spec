# WORKLOG — 通用项目模板工作区 工作进度日志

> 模块：项目专用。
> 使用规则：每完成一小阶段先更新本文件与受影响文档；新对话/新任务开始时，若旧内容
> 已完结或文档已膨胀，**先询问用户是否清理**（已完结条目归档到「历史记录」，或整段
> 移入 `_trash/`），得到确认后才清理；绝不自动删除。
- 最后更新：2026-08-25

## 当前任务

- 需求：修复全面审计发现（版本硬事实过时、WORKLOG 状态失真、重复表格行、
  发版同步约定盲区）+ 母项目文件夹整理（README 回根；工作区文档入 `docs/`、
  同步脚本入 `scripts/`；新建 `docs/EXPERIENCE-TO-KB.md`，不混入模板内部；
  母项目不设 EXPERIENCE-TO-TEMPLATE）+ 模板结构整理（CONTRIBUTING → `docs/`、
  version-sync.json → `scripts/`）+ 修正本机环境 `.git` 描述并由 agent 自动提交。
- 目标/验收：grep `1.1.0` 仅剩历史/CHANGELOG 合法引用；WORKLOG 与实际 git 状态
  一致；sync 0 差异；quick_validate 通过；根目录为 AGENTS/README/VERSION/.gitignore
  + docs/ + scripts/ + project-template/ + init-project/；模板根精简为 8 个必需文件。
- 计划步骤：
  1. 修复版本引用（AGENTS/SKILL/init-steps）+ 删重复行 + pre_release 编号
  2. 母项目目录整理（README 回根；docs/ + scripts/ + 新建 EXPERIENCE-TO-KB.md）
  3. 模板结构整理（CONTRIBUTING → docs/、version-sync.json → scripts/ + 引用更新）
  4. 更新引用文档（根 AGENTS / README / UPGRADE / WORKLOG）与发版约定
  5. sync + 校验 + 自动提交 + 汇报

## 阶段记录

| 阶段 | 状态 | 完成内容 | 变更文件 | 验证 | 下一步 |
|---|---|---|---|---|---|
| 1 修复 | ✅ | 三处 1.1.0→1.1.1；删 init-steps 重复许可行；pre_release_check [2/6] 编号补齐 | AGENTS.md / SKILL.md / init-steps.md / pre_release_check.py | grep 1.1.0 仅历史 | 目录整理 |
| 2 母项目目录整理 | ✅ | README 回根；docs/（CHANGELOG/WORKLOG/EXPERIENCE-TO-KB）；scripts/sync_template.py（修复路径解析） | 移动文件 + 新建 1 文件 | 结构检查 | 模板整理 |
| 3 模板结构整理 | ✅ | CONTRIBUTING → docs/；version-sync.json → scripts/；bump_version 路径更新；AGENTS/README/docs 引用更新 | project-template/ 多文件 | sync 0 差异 | 文档更新 |
| 4 文档更新 | ✅ | 根 AGENTS/README 路径与发版约定；本机环境修正（.git 可提交）；WORKLOG 校准 | 多文件 | 引用核对 | sync+校验 |
| 5 sync+校验+提交 | ✅ | sync 29 文件 0 差异；quick_validate；py_compile；git add + commit | 全部 | 通过 | 汇报 |

## 待办/遗留

- [x] 上一任务（模板 v1.1.0 第二轮改造）9/9 完结
- [x] 上一任务（文档治理经验吸收）6/6 完结
- [x] 上一任务（A–G 经验合入 v1.1.1，提交 1e02c3e + tag v1.1.1）完结
- [x] 本任务（审计修复 + 目录整理 + 模板结构整理）5/5 完结
- [ ] 工作区无 git 远端，改动未推送（N/A 或用户决定）
- [ ] 模板根其余 8 个文件（AGENTS/README/LICENSE/VERSION/TEMPLATE_VERSION/
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
- 2026-08-25 模板 v1.1.0 第二轮改造：阶段落盘（WORKLOG）、双模块、【通用】/【项目专用】
  标注、经验文档×2（完整条目）、删除纪律（_trash + trash.py）、模板升级机制
  （TEMPLATE_VERSION + CHANGELOG + UPGRADE）、红线 13→15（阶段落盘、上下文恢复重读）。
  端到端测试全部通过（详情见阶段记录）。
- 2026-08-25 文档治理经验吸收：文档维护清单、红线 12/5 强化、文档治理约定（正文即当前
  状态；覆盖原文、禁止 AI 追加历史、留痕仅 CHANGELOG 一行、废案走 _trash、可恢复性由
  删除机制保证）、审计清单「文档无缝衔接」专项；未写入参考来源。
- 2026-08-25 v1.1.0 已提交并打 tag（c58a816）。
