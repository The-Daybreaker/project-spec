# 方案与设计（design）

选定路之后，把要建的东西画清楚——一份方案文档（design.md，把决策组织成整体）+ 按需图纸（架构图 / 接口契约 / 数据模型 / 关键流程走查 / 交互原型 等，可按需扩展）。记在 `context/design/` 下，方案按需写、图按需画。

- **适用**：系统复杂到需要图纸的项目。

- **不管**：选路、需求。

- **启用**：agent 在 `context/design/` 下按需生成图纸（画什么见
  `assets/design-template.md`），之后负责维护。

- **停用**：只停维护，不删 `context/design/`（文件留在原处）。

给 agent 的规范见 `MODULE.md`，结构化声明见 `module.json`。
