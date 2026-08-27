# 事实台账 — 单一真相源登记册（漂移免疫门禁）

> 模块：项目专用（母项目层，覆盖模板 + 技能 + 母项目文档）。
> 机器解析表格：列顺序与列名固定，勿改；一行一个事实。
> 状态：**已登记**（有唯一家，门禁强制）/ **待安家**（多处完整展开待归一，
> 门禁只报不拦，是治理工作列表）。
> 指纹 = 事实正文归一化后的 SHA-256 前 12 位（由 `check_consistency.py` 校验，
> 正文变更后复核下游并用 `--accept` 重新登记）。

| 事实ID | 中文名 | 状态 | 家 | 指纹 | 备注 |
|---|---|---|---|---|---|
| redlines | 通用红线（19 条） | 已登记 | project-template/AGENTS.md | d6b25ebbe1d4 | 红线节全量正文；各处摘要/精简版为引用点（B2 打 REF） |
| principles | 设计原则（规范三层顶层） | 已登记 | project-template/AGENTS.md | bc15e96ca9e0 | 「设计原则」节；原则→规范→红线三层（F13） |
| three-zones | 三区表 | 已登记 | project-template/AGENTS.md | 6ebfef1d993c | 仓库布局节；私有指引三区表 B2 第三步改指针 |
| version-rules | 版本规则 | 已登记 | project-template/AGENTS.md | d9048a043602 | 版本管理节全量正文 |
| archiving | 项目归档/退役流程 | 已登记 | project-template/AGENTS.md | 277412b41935 | 归档节全量正文；私有指引归档节 B2 第三步改指针 |
| phases | 阶段体系（五阶段/16节点） | 已登记 | project-template/private/dev/PHASES.md | bd2a8cf4431a | §1 节点映射；其余 12+ 处完整展开 B2 归一 |
| stage-card | 阶段卡机制 | 已登记 | project-template/private/dev/PHASES.md | 26393d6a2a04 | §5 全量正文；USER-GUIDE 旧三段式为活体漂移（B2 第七步修） |
| req-guide | 需求引导方法论 | 已登记 | project-template/private/dev/PHASES.md | 9f281beaf4d5 | §6 全量正文（含状态机）；转译损耗还原（发现+逐层收敛）在 B4 |
| release-flow | 发布流程 | 已登记 | project-template/private/AGENTS.md | bc7dddd0452c | 发布流程节全量正文（含发版状态机）；公开指引简化版 B2 第三步改指针 |
| doc-governance | 文档治理规则 | 已登记 | project-template/private/AGENTS.md | 5cb54a402d36 | 文档治理节 0-5 条；红线 13 保留红线级表述、DOCS 近逐字段 B2 改指针 |
| completion-checklist | 完成检查清单 | 已登记 | project-template/private/AGENTS.md | cb9dc29c0d7f | 清单全量正文；与阶段契约的派生对齐在 B3 |
| doc-duty | 文档职责表 | 已登记 | project-template/docs/DOCS.md | a3e946cf9ab8 | 职责表+维护清单；各文档内摘要+指针指向本家 |
| loading | 加载规则 | 已登记 | project-template/docs/LOADING.md | f45ed517cb40 | 全量加载规则表；母项目副本废除在 B2 第五步 |
