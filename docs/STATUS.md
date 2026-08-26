# STATUS — 通用项目模板工作区 当前状态快照

> 模块：项目专用。
> 只存**最新状态**；历史由 git 承担（`git log` 本文件）。阶段完成/收尾时**覆盖**更新，不追加。
> 新对话/压缩后按红线 15 重读：根 `AGENTS.md` → 模板 `AGENTS.md` → `private/AGENTS.md` → 本文件 → 「任务影响清单 → 要读文档清单」。

- 最后更新：2026-08-27 00:18

## 当前任务

- 需求：重新设计 agent 提问与共识确认机制（P3 已完成，P1/P2 已完成并获用户确认）——
  ①范围=所有提问/确认节点；②严格禁止问题面板（选择面板类 UI），聊天内可给选项/
  推荐但不得仅依赖选项盲目推进；③回答≠终点=新信息输入，内部重检问题空间；
  ④反定型 6 项=关键/风险节点完整展示、每次提问后内部思考；⑤共识达成=完整展示
  反定型+用户明确确认，不得 push/诱导；⑥共识快照+显式确认=每次推进前展示、用户
  逐项表态；⑦确认不锁定=新信息可回到流程，PRD 定稿后走变更流程；⑧落点=模板
  【通用】+ skills，所有项目受益。
- 目标/验收：PRD-0001 定稿 + ADR-0001 已接受（用户确认；轻量流程无 DESIGN 文件）→
  模板【通用】+ skills 全链改造（红线 17/PHASES/FLOW/audit-checklist/agent-rules/
  init-project 资产镜像）→ 六处副本重装 + 全链验证绿。

## 当前阶段

- 模块：P3 开发（节点 10-11）｜ 子阶段：P3.1 模板【通用】+ skills 实施｜ 状态：✅ 已完成（下一步 P4 审计验证）

## 📇 阶段卡（最新）

| 当前模块 | P3 开发（10-11）· agent 提问与共识确认机制 |
| 当前子阶段 | P3.1 模板【通用】+ skills 实施（已完成） |
| 正在完成的任务 | P3 收口：sync_template.py 全链绿（42 文件镜像+版本/指纹/覆盖/副本校验）→ quick_validate×2 绿 → 六处副本全量哈希+版本哨兵校验绿 → git 提交 |
| 已完成任务 | P1 收尾（PRD-0001 定稿）→ P2 收口（ADR-0001 已接受，用户指示轻量流程：无 DESIGN 文件直接进实现）→ 实施编辑完成（AGENTS×3 / PHASES / FLOW / audit-checklist / agent-rules×3 / 工作区 AGENTS+CHANGELOG）→ 资产镜像同步 + 全链校验绿 |
| 下一步（子阶段/模块） | P4 审计验证：自审（audit-checklist 逐项）→ 独立审计 → 修复复检 → 审计结论收口落盘 |
| 阶段状态 | ✅ 已完成（P3 为执行型，展示即走；收口提交后进入 P4） |

## ✅ 生命周期合规清单

| 生命周期行为 | 状态 |
|---|---|
| 受影响文档已同步（红线 12） | ✓（模板+skills+工作区文档已在实施中同步） |
| STATUS 快照已落盘（覆盖更新） | ✓ |
| 本阶段 git 提交已完成（主仓库，D14；本工作区无 private 子 git） | ✓（P2+P3 收口提交随本快照落盘后执行） |
| 产物质量校验通过（sync/verify/check_dev_docs/quick_validate/py_compile/冒烟） | ✓（sync 全链绿：42 文件镜像 + 版本一致性 + agent-rules 指纹 + init-steps 覆盖 + 六处副本全量哈希/哨兵；quick_validate×2 绿） |
| 阶段卡已展示 + 决策型已获确认 | ✓（PRD-0001 定稿 + ADR-0001 已接受，均获用户确认；P3 执行型展示即走） |
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
