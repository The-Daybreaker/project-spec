# CHANGELOG — 软件开发 spec

本文件记录软件开发 spec 的版本变更，方便跨版本迁移。版本号遵循 SemVer，
变更分类参考 Keep a Changelog（Added / Changed / Removed / Fixed）。

## [0.1.0] - 2026-09-02
### Added
- 初始版本：8 个模块（vision / design / prd / adr / development / test /
  audit / release）+ 三入口（微调 / 小功能 / 一期）
### Removed
- module.json 的 `enable.instantiate` / `disable.keep` 字段（启停归 entries，
  字段 12 → 10）
