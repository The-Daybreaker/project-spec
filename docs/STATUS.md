# STATUS — 通用项目模板工作区 当前状态快照

> 模块：项目专用。
> 只存**最新状态**；历史由 git 承担（`git log` 本文件）。阶段完成/收尾时**覆盖**更新，不追加。
> 新对话/压缩后按红线 15 重读：根 `AGENTS.md` → 模板 `AGENTS.md` → `private/AGENTS.md` → 本文件 → 「任务影响清单 → 要读文档清单」。

- 最后更新：2026-08-26

## 当前任务

- 需求：模板工作区**整体架构重构（模块化改造）**——①文档披露渐进式（加载规则表+AGENTS 瘦身）；②流程阶段模块化（P1-P5 五阶段+子阶段+阶段卡+生命周期合规清单）；③流程状态机（FLOW.md）；④WORKLOG→STATUS 快照化；⑤用户文档（USER-GUIDE）；⑥需求引导方法论回写模板。方案 v1 已定稿（计划文件：`<用户主目录>\.workbuddy\plans\<计划名>.md`，D1-D15 全部闭合）。
- 目标/验收：母项目试点跑通新体系 → 全链验证绿 → dogfood 一轮 → 回写模板+skill → 发布 v1.4.0（minor 须用户确认）。

## 当前阶段

- 模块：P3 开发（节点 10-11）｜ 子阶段：全部完成｜ 状态：✅ 已收尾（待 P4 审计）

## 📇 阶段卡（最新）

| 当前模块 | P3 开发（10-11） |
|---|---|
| 当前子阶段 | 已完成：骨架落地 → AGENTS 瘦身 → 脚本适配 → skill 同步 → 全链验证 |
| 正在完成的任务 | P3 全部子阶段完成，产物齐备 |
| 已完成任务 | 1. 新文档×8（工作区 STATUS/FLOW/USER-GUIDE/LOADING + 模板 PHASES/STATUS/FLOW/USER-GUIDE/LOADING + DOCS 扩展） 2. AGENTS×3 瘦身 3. sync/check_dev_docs 适配 + sync 增量镜像改造 4. SKILL/init-steps/init_project/agent-rules 同步 5. 全链验证全绿（sync 源侧/quick_validate×2/py_compile/check_dev_docs/冒烟） |
| 下一步（子阶段/模块） | P4 审计验证（12-13）→ P5 交付发布 |
| 阶段状态 | ✅ 已收尾 |

## ✅ 生命周期合规清单

| 生命周期行为 | 状态 |
|---|---|
| 受影响文档已同步（红线 12） | ✓（STATUS/CHANGELOG/AGENTS×3/模板全套） |
| STATUS 快照已落盘（覆盖更新） | ✓ |
| 本阶段 git 提交已完成（主仓库 + private 子 git，D14） | 🔄 本提交执行中 |
| 产物质量校验通过（sync/check_dev_docs/冒烟） | ✓（全绿） |
| 阶段卡已展示 + 决策型已获确认 | ✓（P1/P2 已确认；P3 执行型） |
| 经验沉淀候选已写入（红线 9） | ⏳ 收尾时执行 |

## 任务影响清单

- 影响文件：工作区 `docs/{STATUS,FLOW,USER-GUIDE,LOADING}.md`、`AGENTS.md`、`README.md`、`docs/CHANGELOG.md`；模板 `project-template/{AGENTS.md,docs/*,private/AGENTS.md,private/dev/*,scripts/check_dev_docs.py}`；`scripts/sync_template.py`；`skills/init-project/{SKILL.md,references/init-steps.md}`；`skills/agent-rules/*`（条件）
- 依赖文档：`project-template/private/AGENTS.md`（16 节点/红线/发布流程）、`project-template/docs/DOCS.md`（文档地图）、`skills/init-project/SKILL.md`（加载规则范式）
- 要读文档清单（恢复时逐份读）：根 `AGENTS.md` → `project-template/AGENTS.md` → `project-template/private/AGENTS.md` → 本文件 → `PHASES.md`（模板）→ 计划文件 `<用户主目录>\.workbuddy\plans\<计划名>.md`

## 下一阶段输入预告

- 下一阶段：P4 审计与验证（12-13）
- 输入：P3 产出的全部新文档 + 脚本改动
- 预期产物：审计结论 + 全链验证通过记录（sync 0 差异 / quick_validate / py_compile / 副本哈希 / init 冒烟）

## 流程位置

- 模块：P3 开发（10-11）· 子阶段「骨架落地」；已完成：P1 需求 → P2 方案 → P3.1 骨架落地；下一步：P3.2 AGENTS 瘦身 → P3.3 脚本适配 → P3.4 skill 同步 → P4 审计验证（缩写附中文翻译：PRD=产品需求文档、RFC=技术方案、ADR=架构决策记录）
