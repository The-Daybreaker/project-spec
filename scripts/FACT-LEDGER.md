# 事实台账 — 单一真相源登记册（漂移免疫门禁）

> 模块：项目专用（母项目层，覆盖模板 + 技能 + 母项目文档）。
> 机器解析表格：列顺序与列名固定，勿改；一行一个事实。
> 状态：**已登记**（有唯一家，门禁强制）/ **待安家**（多处完整展开待归一，
> 门禁只报不拦，是 B2 的工作列表）。
> 指纹 = 事实正文归一化后的 SHA-256 前 12 位（由 `check_consistency.py` 校验，
> 正文变更后复核下游并用 `--accept` 重新登记）。

| 事实ID | 中文名 | 状态 | 家 | 指纹 | 备注 |
|---|---|---|---|---|---|
| redlines | 通用红线（19 条） | 已登记 | project-template/AGENTS.md | d6b25ebbe1d4 | 红线节全量正文；各处摘要/精简版为引用点（B2 打 REF） |
| version-rules | 版本规则 | 已登记 | project-template/AGENTS.md | 1fea077c495a | 版本管理节全量正文 |
| stage-card | 阶段卡机制 | 已登记 | project-template/private/dev/PHASES.md | 26393d6a2a04 | §5 全量正文；USER-GUIDE 旧三段式表述为活体漂移（B2/B4 修） |
| req-guide | 需求引导方法论 | 已登记 | project-template/private/dev/PHASES.md | 625b7175a016 | §6 全量正文；转译损耗还原（发现+逐层收敛）在 B4 |
| phases | 阶段体系（五阶段/16节点/档位） | 待安家 | — | — | 完整展开散落 12+ 处（两份 AGENTS/FLOW/USER-GUIDE/LOADING 等），B2 归一到 PHASES |
| release-flow | 发布流程 | 待安家 | — | — | 私有指引完整版 + 公开指引简化版两处展开，B2 定家 |
| doc-duty | 文档职责表 | 待安家 | — | — | 5 个表格变体（两份 AGENTS/DOCS/init-steps 等），B2 归一到文档总览 |
| three-zones | 三区表 | 待安家 | — | — | 两份 AGENTS 均完整展开，B2 定家 |
| doc-governance | 文档治理规则 | 待安家 | — | — | 三处完整（私有指引/红线 13/DOCS），B2 归一 |
| completion-checklist | 完成检查清单 | 待安家 | — | — | 私有指引完整版 + 精简版 9 项，B3 派生对齐 |
