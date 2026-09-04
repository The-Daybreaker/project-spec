# 决策记录（adr）

重要决策拍板后留一笔，被推翻的沉底不删——都记在 `context/adr/` 下：
decisions.md 放当前有效的决策，history.md 放被取代的（默认不读）。

- **适用**：有选型 / 选路 / 架构决策需要留痕的项目。
- **不管**：需求、方案整体组织。

- **启用**：agent 按 `assets/decisions-template.md`（仅参考格式）在
  `context/adr/` 下实例化 decisions.md，之后负责维护。

给 agent 的规范见 `MODULE.md`，结构化声明见 `module.json`。
