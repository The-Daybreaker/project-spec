# 事实台账 — 单一真相源登记册（漂移免疫门禁）

> 模块：项目专用（母项目层，覆盖模板 + 技能 + 母项目文档）。
> 机器解析表格：列顺序与列名固定，勿改；一行一个事实。
> 状态：**已登记**（有唯一家，门禁强制）/ **待安家**（多处完整展开待归一，
> 门禁只报不拦，是治理工作列表）。
> 指纹 = 事实正文归一化后的 SHA-256 前 12 位（由 `check_consistency.py` 校验，
> 正文变更后复核下游并用 `--accept` 重新登记）。

| 事实ID | 中文名 | 状态 | 家 | 指纹 | 备注 |
|---|---|---|---|---|---|
| redlines | 通用红线（19 条） | 已登记 | project-template/AGENTS.md | 5884797dac2c | 红线节全量正文（19 条均三要素齐全）；精简版由继承矩阵双侧台账联动 |
| principles | 设计原则（规范三层顶层） | 已登记 | project-template/AGENTS.md | bc15e96ca9e0 | 「设计原则」节；原则→规范→红线三层（F13） |
| three-zones | 三区表 | 已登记 | project-template/AGENTS.md | 6ebfef1d993c | 仓库布局节；私有指引已改摘要+指针 |
| version-rules | 版本规则 | 已登记 | project-template/AGENTS.md | d9048a043602 | 版本管理节全量正文 |
| archiving | 项目归档/退役流程 | 已登记 | project-template/AGENTS.md | 277412b41935 | 归档节全量正文；私有指引已改摘要+指针 |
| phases | 阶段体系（五阶段/16节点） | 已登记 | project-template/private/dev/PHASES.md | bd2a8cf4431a | §1 节点映射；两份入口完整展开已改摘要+指针，流程图已迁入 |
| stage-card | 阶段卡机制 | 已登记 | project-template/private/dev/PHASES.md | 26393d6a2a04 | §5 全量正文；USER-GUIDE 旧三段式已修复对齐 |
| req-guide | 需求引导方法论 | 已登记 | project-template/private/dev/PHASES.md | 036e2add95c2 | §6 全量正文（含状态机）；转译损耗已还原（引导发现+逐层收敛） |
| release-flow | 发布流程 | 已登记 | project-template/private/AGENTS.md | bc7dddd0452c | 发布流程节全量正文（含发版状态机）；公开指引已改摘要+指针 |
| doc-governance | 文档治理规则 | 已登记 | project-template/private/AGENTS.md | 5cb54a402d36 | 文档治理节 0-5 条；红线 13 保留红线级表述、DOCS 已改摘要+指针 |
| completion-checklist | 完成检查清单 | 已登记 | project-template/private/AGENTS.md | 494dec89734d | 清单全量正文；已含契约对应项（冲突检测/裁剪声明） |
| doc-duty | 文档职责表 | 已登记 | project-template/docs/DOCS.md | 2a484e770fe9 | 职责表+维护清单（含 design/ 契约文件夹）；各文档内摘要+指针指向本家 |
| doc-quality | 文档质量标准（四条标准+反AI感清单） | 已登记 | project-template/docs/DOCS.md | b8567b3b8898 | 改文档前读、改完对照审；审计清单 §12 联动（PRD-0005） |
| stage-contract | 阶段契约（必做项+裁剪属性） | 已登记 | project-template/private/dev/PHASES.md | 1054cbbf2c6f | §8：每阶段必做清单+裁剪规则+需求冲突检测+设计契约定稿/按契约实施（F14/F15/PRD-0004） |
| test-map | 测试台账 | 已登记 | project-template/docs/TEST-MAP.md | ee239c64063d | 每个脚本断言什么/能测出什么/盲区（F11） |
| loading | 加载规则 | 已登记 | project-template/docs/LOADING.md | e15b012dc94c | 全量加载规则表（含「改文档→读质量标准」行）；母项目副本已废除改指针 |
