# LOADING — 文档加载规则表（渐进式披露协议）

> 模块：混合（【通用】= 规则表可随模板升级；【项目专用】= 本工作区实例）。
> 用途：**渐进式披露的单一真相**——「什么场景读什么文档、哪些必读、哪些按需、哪些
> 默认不读」。目标：提高指令遵循度 + 上下文卫生（历史默认不读、按需才读）。
> AGENTS.md 内放本表摘要版；本文件为全量版。

## 加载规则表

| 场景 | 优先级 | 文件路径 |
|---|---|---|
| **每次新对话 / 上下文压缩后恢复** | 必读 | 根 `AGENTS.md` → 模板 `project-template/AGENTS.md` → `project-template/private/AGENTS.md` → `docs/STATUS.md`（快照） |
| **红线规范** | 始终必读 | AGENTS 红线小节 / agent-rules 精简版 |
| 需要阶段定义 / 产物 / 切换规则 / 生命周期 | 按需读 | `project-template/private/dev/PHASES.md` |
| 需要流程图 / 状态机 / 动作链路 | 按需读 | `docs/FLOW.md` |
| 需要全量加载规则 | 按需读 | `docs/LOADING.md`（本文件） |
| 需求 / 方案 / 调研任务 | 按需读 | `project-template/private/dev/{prd,rfc,adr,research}/INDEX.md` → 目标文档 |
| 实施任务 | 必读 | `project-template/private/dev/DESIGN.md`、对应 PRD |
| 审计任务 | 必读 | `project-template/docs/audit-checklist.md` |
| 验证任务 | 必读 | `scripts/ci_check.py` 说明、`project-template/docs/TESTING.md` |
| 发布任务 | 必读 | 发布流程（`project-template/private/AGENTS.md`）→ `project-template/private/dev/CHANGELOG.md` → `pre_release_check.py` |
| 母项目改模板 / 同步 | 必读 | 根 `AGENTS.md` 维护约定 → `scripts/sync_template.py` |
| **历史决策 / 追溯** | **默认不读，按需** | `CHANGELOG` / `ADR`（用户明确要求或确需追溯时） |
| 经验沉淀 | 按需读 | `project-template/private/dev/EXPERIENCE-TO-TEMPLATE.md` / `EXPERIENCE-TO-KB.md` |

## 阶段 → 文档映射（披露隔离，D11）

每个阶段只读/只写自己的文档集，**阶段间只传产物**，不读上一阶段中间过程：

| 阶段 | 本阶段读写 | 只读（上游产物） | 默认不读 |
|---|---|---|---|
| P1 需求 | `prd/`、`research/` | — | 方案 / 实现 / 历史 |
| P2 方案 | `rfc/`、`adr/`、`prototype/`、`DESIGN.md` | 定稿 PRD | 调研过程 / 候选对比 / 历史 |
| P3 开发 | `src/` 实现 + 受影响文档 | DESIGN.md + PRD | 调研 / 候选方案 / 历史 |
| P4 审计验证 | TEST-REPORT.md、审计结论 | 实现产物 + DESIGN | 中间过程 |
| P5 交付发布 | CHANGELOG、发布产物、EXP 沉淀 | 验证产物 | 中间过程 |
| 贯穿 | STATUS.md（快照）、EXPERIENCE-TO-* | — | — |

## 恢复协议（中断 / 压缩后，红线 15 的落地）

1. 读根 `AGENTS.md`（红线 + 加载规则摘要）→ 定位场景行；
2. 读模板 `AGENTS.md` / `private/AGENTS.md`（私有加载规则 + 当前状态）；
3. 读 `docs/STATUS.md` 快照——由「📇 阶段卡（当前阶段节点 + 标题状态）」判断进度；
4. 按快照「任务影响清单 → 要读文档清单」逐份读；
5. 阶段卡缺失/空白时：`git log` 查本文件最近提交推断，仍不确定则**询问用户**；
6. 展示合并紧凑阶段卡（标题含状态 + 横置阶段线 + 合规两行）后继续。

> 渐进式披露在恢复场景不失效：恢复只读「必读 + 要读清单」，历史依旧默认不读。
