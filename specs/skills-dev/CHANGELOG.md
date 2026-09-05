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

### Removed

- （2026-09-05）模块装置：`@模块/` 目录、`MODULE.md` / `module.json` /
  每模块 `README`·`CHANGELOG`，以及 spec 级 `AGENTS.md` / `manifest.json`——
  全部塌进 `spec.md`；防漂移锁文件随「拉进项目即自由编辑」退休。
