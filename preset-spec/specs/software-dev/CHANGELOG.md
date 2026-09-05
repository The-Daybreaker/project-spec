# CHANGELOG — 软件开发 spec

本文件记录软件开发 spec 的版本变更，方便跨版本迁移。版本号遵循 SemVer，变更分类参考 Keep a Changelog（Added / Changed / Removed / Fixed）。早期 0.1.0 滚动开发，不为早期措辞调整逐次递增版本号（开发仓决策 54）。

## [0.1.0] - 2026-09-02

### Added

- 初始版本：8 个阶段（vision / design / prd / adr / development / test / audit / release）+ 三入口（微调 / 小功能 / 一期）。

### Changed

- （2026-09-05）spec 机制单文档化重构：8 个模块并入一份 `spec.md`（各阶段统一三段式——产出 / 运行过程 / 规范边界）；产出骨架移入同级 `assets/`；原 `manifest.json` 的入口（流程调节）并入 spec.md 用 markdown 表表达。
- （2026-09-05）development / audit 阶段的验收落点从 `process/reviews/` 改为 `process/` 根 review 临时件（`review-<简介>.md`，通过后删、不归档 logs）——配合模板框架取消三个异步目录（开发仓决策 62）。
- （2026-09-05）产出落点改用业界惯例名：development 的 `workspace/source/` → `workspace/src/`、release 的 `workspace/delivery/` → `workspace/dist/`；归档路径 `logs/*` → `archive/*`（配合模板框架 logs→archive、workspace 去预置，开发仓决策 63）。
- （2026-09-05）口径软化与格式统一：场景声明收窄为「个人长期维护项目」、「管什么场景」改「使用场景」；§二「依赖全景 · 入口 · 检查点」更名「概览」，阶段链从硬依赖软化为推荐顺序（不强制、可按实际调整），入口「缩放旋钮」更名「流程调节」，回溯明确为「纳入任务进行核查和调整」；删除 release 阶段「强依赖 audit」表述；各阶段「运行过程」统一为有序列表（修正 vision 段 tab 缩进），「专门调研」精简为「调研」。
- （2026-09-05）全文措辞规范化：内部比喻与生造术语统一换成业界通用表述（状态标记、当前状态区、流程调节、渐进式披露、独立审查、判断标准等），不涉及机制变更，版本不递增（开发仓决策 54）。

### Removed

- （2026-09-05）模块机制：`@模块/` 目录、`MODULE.md` / `module.json` / 每模块 `README`·`CHANGELOG`，以及 spec 级 `AGENTS.md` / `manifest.json`——全部并入 `spec.md`；防漂移锁文件随「拉进项目即自由编辑」废弃。
