# CHANGELOG — skill 开发 spec

本文件记录 skill 开发 spec 的版本变更，方便跨版本迁移。版本号遵循 SemVer，
变更分类参考 Keep a Changelog（Added / Changed / Removed / Fixed）。
早期 0.1.0 滚动开发，不为早期措辞调整逐次递增版本号（开发仓决策 54）。

## [0.1.0] - 2026-09-03

### Added

- 初始版本：7 个阶段（vision / design / adr / development / test / audit /
  release）+ 两入口（小修 / 完整开发路径）+ 控制权检查点声明（实施放行 /
  收口放行）；相对 software-dev 不含 prd 阶段（skill 体量小，无排期与当期
  需求层）。

### Changed

- （2026-09-05）spec 机制单文档化重构：7 个模块塌进一份 `spec.md`（各阶段
  统一三段式——产出 / 运行过程 / 规范边界）；产出骨架移入同级 `assets/`；
  原 `manifest.json` 的入口（缩放旋钮）折进 spec.md 用 markdown 表表达。
- （2026-09-05）vision 阶段 tailor 为「想法池」：去掉软件版特有的近三期
  排期表 / 里程碑 / 演进原则，`assets/vision-template.md` 同步改为想法池骨架
  ——修正此前共享 vision 模块给本 spec 塞进用不上的排期内容的矛盾。
- （2026-09-05）development / audit 阶段的验收落点从 `process/reviews/` 改为
  `process/` 根 review 临时件（`review-<简介>.md`，通过后删、不归档 logs）——
  配合模板框架取消三件套（开发仓决策 62）。
- （2026-09-05）产出落点改用业界惯例名：development 的 `workspace/source/` →
  `workspace/src/`、release 的 `workspace/delivery/` → `workspace/dist/`；归档
  路径 `logs/*` → `archive/*`（配合模板框架 logs→archive、workspace 去预置，
  开发仓决策 63）。
- （2026-09-05）与 software-dev 同步口径：场景声明收窄为「个人长期维护
  项目」、「管什么场景」改「使用场景」；§二「依赖全景 · 入口 · 检查点」更名
  「概览」，阶段链从硬依赖软化为推荐顺序（不强制、可按实际调整），入口
  「缩放旋钮」更名「流程调节」，回溯线明确为「纳入任务进行核查和调整」；
  删除 release 阶段「强依赖 audit」表述；各阶段「运行过程」统一为有序列表。

### Removed

- （2026-09-05）模块装置：`@模块/` 目录、`MODULE.md` / `module.json` /
  每模块 `README`·`CHANGELOG`，以及 spec 级 `AGENTS.md` / `manifest.json`——
  全部塌进 `spec.md`；防漂移锁文件随「拉进项目即自由编辑」退休。
