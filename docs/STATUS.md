# STATUS — 通用项目模板工作区 当前状态快照

> 模块：项目专用。
> 只存**最新状态**；历史由 git 承担（`git log` 本文件）。阶段完成/收尾时**覆盖**更新，不追加。
> 新对话/压缩后按红线 15 重读：根 `AGENTS.md` → 模板 `AGENTS.md` → `private/AGENTS.md` → 本文件 → 「任务影响清单 → 要读文档清单」。

- 最后更新：2026-08-26 23:54

## 当前任务

- 需求：重新设计 agent 提问与共识确认机制（P1 进行中，需求已澄清并获用户确认）——
  ①范围=所有提问/确认节点；②严格禁止问题面板（选择面板类 UI），聊天内可给选项/
  推荐但不得仅依赖选项盲目推进；③回答≠终点=新信息输入，内部重检问题空间；
  ④反定型 6 项=关键/风险节点完整展示、每次提问后内部思考；⑤共识达成=完整展示
  反定型+用户明确确认，不得 push/诱导；⑥共识快照+显式确认=每次推进前展示、用户
  逐项表态；⑦确认不锁定=新信息可回到流程，PRD 定稿后走变更流程；⑧落点=模板
  【通用】+ skills，所有项目受益。
- 目标/验收：PRD-0001 定稿（用户确认）→ P2 方案 → 模板【通用】+ skills 全链改造
  （红线/PHASES/FLOW/agent-rules/init-project 资产镜像）→ 六处副本重装 + 全链验证绿。

## 当前阶段

- 模块：P1 需求（节点 01-05）｜ 子阶段：P1.3 PRD 草稿与评审｜ 状态：🔄 进行中（待用户评审）

## 📇 阶段卡（最新）

| 当前模块 | P1 需求（01-05）· agent 提问机制重设计 |
| 当前子阶段 | P1.3 PRD 草稿与评审 |
| 正在完成的任务 | 展示 PRD-0001 草稿供用户评审（P1.4 评审，决策型） |
| 已完成任务 | 1. 重读规范 2. STATUS 当前任务更新 3. P1.1 需求理解确认完成（9 项注释 → 共识快照 → 用户确认） 4. P1.2 红线 13 调研完成（RESEARCH-0001：18 条发现 + 结论：组合创新，无同款） 5. PRD-0001 草稿落盘 |
| 下一步（子阶段/模块） | 用户评审 → PRD 定稿（门禁 1：字段齐全 + 用户确认） |
| 阶段状态 | 🔄 进行中（P1 为决策型） |

## ✅ 生命周期合规清单

| 生命周期行为 | 状态 |
|---|---|
| 受影响文档已同步（红线 12） | ✓（STATUS 已更新；其余待需求定稿后同步） |
| STATUS 快照已落盘（覆盖更新） | ✓ |
| 本阶段 git 提交已完成（主仓库，D14；本工作区无 private 子 git） | ⏳（P1.2/1.3 完成后提交，带 P1 标识，待申请权限） |
| 产物质量校验通过（sync/verify/check_dev_docs/quick_validate/py_compile/冒烟） | ⏳（尚无实施产物；PRD/RESEARCH 已按登记册骨架格式落盘） |
| 阶段卡已展示 + 决策型已获确认 | ✓（P1.1 共识已获用户确认；后续子阶段继续展示） |
| 经验沉淀候选已写入（红线 9） | ⏳（任务收尾时写入 EXP-TO-KB） |

## 任务影响清单

- 影响文件：`version.json`×2（工作区 + 模板）、`AGENTS.md`×3（工作区 + 模板×2）、
  `README.md`×2、`project-template/{private/{AGENTS,PRIVATE}.md, private/dev/
  {DESIGN,CHANGELOG,TEST-REPORT}.md, scripts/{bump_version,pre_release_check}.py,
  .github/workflows/release.yml, docs/{audit-checklist,CONTRIBUTING,DOCS,UPGRADE}.md}`、
  `skills/init-project/{SKILL.md,scripts/init_project.py,references/init-steps.md}`、
  `skills/agent-rules/{SKILL.md,references/inheritance-map.md}`、
  工作区 `docs/{STATUS,CHANGELOG,EXPERIENCE-TO-KB}.md`、六处安装副本（重装）
- 依赖文档：P2 方案（版本号四段式规则 / 流程图 / 影响面清单 / 迁移说明）
- 要读文档清单（恢复时逐份读）：根 `AGENTS.md` → 模板 `project-template/AGENTS.md` → `project-template/private/AGENTS.md` → 本文件 → 模板 `project-template/private/dev/PHASES.md`

## 下一阶段输入预告

- 下一阶段：P5 交付发布（如需发版 `v1.4.0.patch0`）
- 输入：未发版变更区段（版本号体系重新设计条目）
- 预期产物：按发版流程（bump `--part` / CHANGELOG 顶部 / pre_release_check /
  tag `v1.4.0.patch0` + Release）
