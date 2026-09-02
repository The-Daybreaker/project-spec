# Changelog

本文件记录模板本体的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/spec/v2.0.0.html)。

## [0.1.0] - 2026-09-02

### Added

- v3 本体首次成型：以 agent 为第一读者的项目模板。
- spec 机制：构建规则（spec/build/）+ 预置 spec（spec/preset/software-dev，含 8 模块）。
- 四步链设计（场景理顺 → 拆模块 → 组装 spec → 抽象 L0）完整落地。
- 宪章 6 条、协作总纲（AGENTS.md）、模板使用手册（README.md）。
- 密钥钩子机制：`scripts/scan_secrets.py`（高危凭据零容忍 + 个人信息复核，
  排除名单参数化、脚本零个人信息，首次运行自动生成排除名单模板）+
  `.githooks/pre-push` 推送门禁（初始化时 `git config core.hooksPath .githooks`
  启用）。
