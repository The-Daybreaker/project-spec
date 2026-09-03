# Changelog

本文件记录模板本体的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/spec/v2.0.0.html)。

## [0.9.0] - 2026-09-03

版本号对齐 delivery 发布序列（0.1.0 → 0.9.0）：模板本体是 delivery 的核心
资产，此后版本号以本体 `package.json` 为单一事实源，delivery 跟随演进。

### Added

- 云端模块库接入：锁文件 `origin` 记真实指向
  （`github.com/The-Daybreaker/project-spec`）；preset 锁文件落真实账
  （spec + 8 模块的 origin / version / hash）。

### Removed

- module.json 的 `enable.instantiate` / `disable.keep` 字段（字段 12 → 10；
  启停运行态由 manifest 的 entries 表达，例化语义归 MODULE.md）。
- 预置 spec `spec/preset/software-dev`（8 模块）与内置构建规则
  `spec/build/`：地基走查确认模板不依赖 spec 即可以地基形态运转；两者与
  云端模块库内容一致，改为唯一事实源在云端、按需拉取——出厂 `spec/` 只留
  机制三件（`AGENTS.md` 机制说明书 + `lockfile.py` 工具 + `lockfile.md`
  字段规范），spec 包落地为自己的子目录 `spec/<id>/`。
- 密钥门禁（`scripts/scan_secrets.py` + `.githooks/pre-push`）：模板不再
  携带，密钥防护的机械防线只留 .gitignore 的密钥文件名模式；要不要
  额外的门禁与钩子由使用者自行决定。

## [0.8.0] - 2026-09-02

### Added

- 重构后的模板地基首次成型：以 agent 为第一读者的项目模板。
- spec 机制：构建规则（spec/build/）+ 预置 spec（spec/preset/software-dev，含 8 模块）。
- 四步链设计（场景理顺 → 拆模块 → 组装 spec → 抽象 L0）完整落地。
- 宪章 6 条、协作总纲（AGENTS.md）、模板使用手册（README.md）。
- 密钥钩子机制：`scripts/scan_secrets.py`（高危凭据零容忍 + 个人信息复核，
  排除名单参数化、脚本零个人信息，首次运行自动生成排除名单模板）+
  `.githooks/pre-push` 推送门禁（初始化时 `git config core.hooksPath .githooks`
  启用）。
