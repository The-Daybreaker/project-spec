# CHANGELOG

发布仓库的版本历史（三产物：project-template / init-project / agent-rules）。
模板本体的变更记录另见 `project-template/CHANGELOG.md`，其版本号与发布版本
解耦、各自演进。更早的 v1.x 历史保存在 git 提交记录中
（tag `v1.0.1` ~ `v1.6.1.patch1`）。

## [1.7.0] - 2026-09-02

断代版本：模板整体重设计为 v3，目录结构全新。v1 项目无法原地升级，
老项目继续按 v1 运转即可，新项目用本版。

### Added

- 七件套骨架：`AGENTS.md`（协作总纲 + 宪章 6 条）、`README.md`（使用手册）、
  `context/`（项目上下文，种类由 spec 决定）、`workspace/`（source +
  delivery）、`process/`（任务板 + inbox / pending / reviews 三件套）、
  `logs/`（历史归档）、`spec/`（声明式规范）。
- spec 机制：构建规则（`spec/build/`：build.md + spec / module 两模板）+
  预置 spec `software-dev`（vision / design / prd / adr / development /
  test / audit / release 共 8 模块）；空 spec 时项目以地基形态运转。
- 推送前密钥门禁（保留自 v1 并参数化）：`scripts/scan_secrets.py` +
  `.githooks/pre-push`，排除名单外置 `scan_secrets.ignore`（不入库）。
- 发布仓库顶层 `CHANGELOG.md`（本文件）。

### Changed

- `init-project` skill 重构：内嵌 v3 模板镜像，初始化含 hooksPath 配置与
  回读校验清单（内联 SKILL.md）。
- `agent-rules` skill 重构：模板宪章的项目外精简形态（version 1.7.0）。
- 发布 README 重写（价值主张 / 快速开始 / 目录结构 / 版本说明）。

### Removed

- v1 结构整体移除：`private/` 子仓库、`docs/`、`dist/`、`archive/`、
  `.github/workflows/`、`version.json`、`install-targets.json` 及大部分
  维护脚本。
