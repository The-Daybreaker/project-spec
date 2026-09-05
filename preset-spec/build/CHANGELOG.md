# CHANGELOG — 构建规则（build）

本文件记录构建规则层的版本变更，方便跨版本迁移。版本号遵循 SemVer，变更分类参考 Keep a Changelog（Added / Changed / Removed / Fixed）。

## [0.1.0] - 2026-09-04

### Added

- 建立构建规则层版本身份：`build.json` + 本 CHANGELOG（`build.json` 于 2026-09-05 单文档化重构时移除，版本改记在 `build.md` 顶部）。
- 既有内容：`build.md` + `spec-template/` + `module-template/`。

### Changed

- （2026-09-05）配合 spec 单文档化：`build.md` 从「怎么造 spec 和模块」重写为「怎么写一份 spec.md」；`spec-template/` 母版从 AGENTS.md + manifest.json 改为单份 `spec.md` 骨架；版本行移进 `build.md` 顶部。
- （2026-09-05）配合 spec 口径软化：头部字段「管什么场景」→「使用场景」、§二「依赖全景 · 入口 · 检查点」→「概览」、入口「缩放旋钮」→「流程调节」、阶段箭头定性为推荐顺序（不强制）；新增「运行过程分步骤用有序列表、一步一行」规则，`spec-template/` 母版同步。
- （2026-09-05）全文措辞规范化：内部比喻与生造术语统一换成业界通用表述（状态标记、流程调节、渐进式披露、引用等），不涉及机制变更，版本不递增（开发仓决策 54）。

### Removed

- （2026-09-05）`build.json`（版本改记 build.md 顶部）、`module-template/` （无模块了）、`spec-template/manifest.json` 与 `spec-template/AGENTS.md` （并入 `spec-template/spec.md`）；构建规则不再讲锁文件与云端 `registry.json` （两者均已废弃）。
