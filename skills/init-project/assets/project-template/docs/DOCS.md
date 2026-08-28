# docs — 公开文档

> 模块：全通用（模板自带、可随模板升级）。

本目录存放随仓库发布（公开）的项目文档。约定：

- 面向使用者/贡献者的文档放这里；**开发期文档**（设计、变更记录、测试报告）放
  `private/dev/`（不进 GitHub）。
- 每份文档在文件开头写明读者对象与维护者（负责随改动同步更新的人/角色）。
- 文档语言按项目约定（建议中文，双语项目按 README 约定同步）。

## 文档职责表（唯一家）

<!-- FACT:doc-duty -->

- **动机**：职责表散在多处时，「这个信息该写哪、改这里要同步谁」必然各说各话；
  集中到一张表，写新内容先查表定归属，改完按维护清单核对同步。

**每份文档唯一职责**：

| 文档 | 位置 | 模块 | 职责 |
|---|---|---|---|
| 根 `AGENTS.md` | 公开 | 混合 | 公开入口（面向使用者/贡献者/接手 agent） |
| `private/AGENTS.md` | 私有 | 混合 | 开发入口与完整开发规范（唯一常青开发记忆） |
| `private/dev/PHASES.md` | 私有 | 通用 | 阶段模块权威定义（含流程图与状态机） |
| `private/dev/STATUS.md` | 私有 | 项目专用 | 当前状态快照（历史由 git 承担） |
| `private/dev/ROADMAP.md` | 私有 | 项目专用 | 长期需求与展望（唯一长期入口，覆盖式更新） |
| `private/dev/DESIGN.md` | 私有 | 混合 | 设计总览 + 开发规范（契约索引指向 `design/`） |
| `private/dev/design/` | 私有 | 混合 | 设计契约文件夹（架构/接口/数据/安全契约；适用必做/不适用须声明） |
| `private/dev/prd|rfc|adr|research/` | 私有 | 项目专用 | 四登记册（需求/方案/决策/调研，各含 INDEX 与状态机） |
| `private/dev/prototype/` | 私有 | 项目专用 | 页面原型/设计稿（一文件一原型） |
| `private/dev/CHANGELOG.md` | 私有 | 项目专用 | 完整版本历史（每次发布必更新） |
| `private/dev/TEST-REPORT.md` | 私有 | 项目专用 | 当前测试记录与运行方式（每次发布必更新） |
| `private/dev/EXPERIENCE-TO-TEMPLATE.md` | 私有 | 项目专用·沉淀暂存 | 可沉淀进模板的经验（完整条目） |
| `private/dev/EXPERIENCE-TO-KB.md` | 私有 | 项目专用·沉淀暂存 | 可沉淀进知识库的经验（完整条目） |
| `README.md` | 公开 | 项目专用 | 面向使用者/贡献者 |
| `docs/` | 公开 | 通用 | 公开文档（DOCS / LOADING / audit-checklist / TESTING / TEST-MAP / UPGRADE / CONTRIBUTING；流程图在 `private/dev/PHASES.md`；面向用户的内容在 `README.md`） |
| `docs/CONTRIBUTING.md` | 公开 | 混合 | 人类贡献者与 agent 的协作约定 |
| `version.json` | 公开 | 通用 | 版本（`version`）与模板版本（`template_version`）单一事实来源 |
| （按项目补充：架构、API、使用手册等） | | | |

**文档维护清单**（变更类型 → 必须同步的文档）：

| 变更类型 | 必须同步的文档 |
|---|---|
| 决策/选型/红线类 | `private/AGENTS.md`「用户确认的设计决策」（覆盖原文）+ CHANGELOG 一行摘要 |
| 需求/方案/调研 | `private/dev/prd|rfc|research/`（登记册状态+索引同步）+ DESIGN（定稿吸收） |
| 架构决策 | `private/dev/adr/`（只增不改）+ `private/AGENTS.md` D-xxx 一行摘要 + `详见 ADR-XXXX` + CHANGELOG 一行摘要 |
| 进度/状态/环境 | `private/dev/STATUS.md`（当前做到哪里）+ 受影响文档 |
| 设计/架构/数据流 | `private/dev/DESIGN.md` + `private/dev/design/` 对应契约（接口契约变更须重新确认） |
| 功能/接口实现 | DESIGN / README / docs（按项目实际） |
| 测试/验证 | `private/dev/TEST-REPORT.md` |
| 版本/发布 | `version.json` / CHANGELOG / README |
| 用户视角/流程 | README / docs（audit-checklist / UPGRADE / CONTRIBUTING 等）/ 根 AGENTS.md |
| 模板升级 | 按 `docs/UPGRADE.md` 流程 + `version.json` + CHANGELOG/STATUS |
<!-- /FACT -->

## 文档地图（每份文档回答什么问题）

| 文档 | 回答的问题 |
|---|---|
| 根 `AGENTS.md` | Agent 入口：红线摘要、必读顺序、文档职责、维护清单 |
| `private/AGENTS.md` | 开发规范全集、当前状态、环境、决策、定案/询问清单 |
| `private/dev/PHASES.md` | 阶段模块权威定义：每阶段输入/产物/生命周期/16节点映射/切换规则/需求引导/文档映射/流程图与状态机 |
| `private/dev/DESIGN.md` | 怎么做：设计总览 + 契约索引 + 关键不变量 + 影响面 |
| `private/dev/design/` | 接口/数据/权限长什么样：设计契约（审核面=场景映射表） |
| `private/dev/STATUS.md` | 做到哪了：当前状态快照（阶段卡 + 影响清单 + 生命周期合规清单 + 下阶段输入预告） |
| `private/dev/prd/` | 为什么做/做什么：需求登记册（状态+优先级，定稿门禁） |
| `private/dev/rfc/` | 怎么做：方案登记册（候选对比/评审结果，采纳后冻结） |
| `private/dev/adr/` | 决定了什么/为什么：决策登记册（只增不改，历史追溯） |
| `private/dev/research/` | 调研过什么：调研登记册（发现记录追加+当前结论） |
| `private/dev/prototype/` | 页面长什么样：页面原型/设计稿（界面/交互改动，「先出图再确认」产物） |
| `private/dev/CHANGELOG.md` | 变过什么：版本历史 |
| `private/dev/TEST-REPORT.md` | 验证过什么：测试记录 |
| `private/dev/EXPERIENCE-TO-TEMPLATE.md` | 可沉淀进模板的经验 |
| `private/dev/EXPERIENCE-TO-KB.md` | 可沉淀进知识库的经验 |
| `README.md` | 使用者视角：项目全貌/五阶段/阶段卡怎么读（唯一用户文档） |
| `docs/DOCS.md` | docs 目录说明与文档治理 |
| `docs/LOADING.md` | 什么场景读什么：加载规则表全量版（渐进式披露） |
| `docs/audit-checklist.md` | 改动对不对：实施后审计清单（自审/独立审计共用） |
| `docs/TESTING.md` | 怎么测：pytest 示例、覆盖率、CI 接入、TEST-REPORT 对应 |
| `docs/UPGRADE.md` | 模板如何升级 |
| `docs/CONTRIBUTING.md` | 人类贡献者与 agent 怎么协作 |
| `archive/ARCHIVE.md` | 归档：归档流程、归档说明与已归档内容快照 |

## 加载规则表摘要（渐进式披露；全量版见 `LOADING.md`）

| 场景 | 优先级 | 文件 |
|---|---|---|
| 新对话/压缩后恢复 | 必读 | 根 AGENTS → private/AGENTS → `STATUS.md` 快照 |
| 红线规范 | 始终必读 | AGENTS 红线小节 |
| 阶段定义/切换规则 | 按需 | `PHASES.md` |
| 流程图/状态机 | 按需 | `PHASES.md` §0/§4 |
| 需求/方案/调研 | 按需 | 登记册 INDEX → 目标文档 |
| 实施 | 必读 | DESIGN + 对应 PRD |
| 发布 | 必读 | 发布流程 → CHANGELOG → pre_release_check |
| 历史决策/追溯 | **默认不读** | CHANGELOG / ADR |

## 文档模块归属（通用 / 项目专用）

- 每份文档顶部标注 `> 模块：全通用 / 全项目专用 / 混合`；
- 混合文档内用 `## 【通用】` / `## 【项目专用】` 前缀区分小节；
- **更新纪律**：**通用模块**改动若可复用 → 沉淀回通用项目模板；**项目专用模块**
  不受模板更新覆盖（模板升级只应用【通用】模块，见 `UPGRADE.md`）。

## 文档治理（正文即当前状态）

<!-- REF:doc-governance -->
正文=当前有效状态：决策修改直接覆盖原文，禁历史标注，禁 AI 追加历史；留痕只记 CHANGELOG 一行；历史文档区（四登记册）例外。完整规则见 `private/AGENTS.md`「文档治理」节。
<!-- /REF -->
