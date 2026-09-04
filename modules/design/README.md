# 方案与设计（design）

选定路之后，把要建的东西画清楚——记在 `context/design/` 下：一份方案文档
`design.md`（把选路决策组织成整体）+ 按需图纸（架构图 / 接口契约 / 数据
模型 / 关键流程走查 / 交互原型 等，可按需扩展）。方案按需写、图按需画。

- **适用**：系统复杂到需要图纸的项目。
- **不管**：需求。

- **启用**：agent 按 `assets/design-template.md`（仅参考格式）在
  `context/design/` 下实例化 `design.md`，图纸按需生成，之后负责维护。

给 agent 的规范见 `MODULE.md`，结构化声明见 `module.json`。
