# CHANGELOG

本文件记录模板本体的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/spec/v2.0.0.html)。自 1.0.0 起进入稳定期，目录结构与 `AGENTS.md` 协作协议按 SemVer 约束兼容性。1.0.0 之前的历史（0.8.0 / 0.9.0 及开发期 [Unreleased]）归档于开发仓 `dev/archive/changelog-template-pre-1.0.0.md`。

## [1.0.0] - 2026-09-06

首个稳定版。模板出厂为 9 个实质文件（`AGENTS.md`、`README.md`、本文件、`.editorconfig`、`.gitattributes`、`.gitignore`、`process/task.md`、`process/memory.md`、`spec/AGENTS.md`，空目录以 .gitkeep 占位）。

### Added

- `process/` 临时件机制：随手笔记与 `review-<简介>.md` 验收件，用完即清、通过后删。
- 「项目自己的规范」预置两条文档形态示例：正文段落不手动句中折行、正文只写当前有效状态（任何会话都需遵守，可自行增改）。

### Changed

- spec 机制单文档化：一个 spec = 一份 `spec.md` + 同级 `assets/`；`spec/AGENTS.md` 精简为机制说明书（spec 是什么 / 怎么设计与获取 / 怎么读 / 状态标记约定），最佳实践集在公开仓同仓 `preset-spec/`，复制进项目即自由修改。
- `process/` 重新定性为「协作当前状态区」：常驻件（`task.md` / `memory.md`）+ 临时件；冷启动改为通读 process/ 全部文件；`memory.md` 为 agent 自我维护区（只声明用途、不声明内容）。
- 目录命名对齐业界惯例：`logs/` → `archive/`；删除 `workspace/source/`、`workspace/delivery/` 预置，工作区内部结构由 spec / 项目按惯例（如 `src/`、`dist/`）自行声明。
- 规范保留在 `AGENTS.md` §四「规范（用户维护区）」：曾拆出 `spec/constitution.md`，验证后全量迁回，§四内部小节去编号。
- `README.md` 重写为面向项目主人的使用手册（协作层 / 发布层心智模型、「读盘 → 干活 → 写盘」协作循环、高频场景速查、按需装 spec 三步、核心文件分工），「写给用户」节原样保留。
- 全文去除手动折行；两轮措辞规范化，统一业界通用表达。

### Removed

- 模块机制与锁文件（`@模块/`、`MODULE.md` / `module.json`、每模块 README·CHANGELOG、`spec/lockfile.py` / `lockfile.md` 及实例化 lockfile.json、spec 级 manifest）。
- 异步交流目录 `process/inbox/`、`process/pending/`、`process/reviews/`。
- `workspace/source/`、`workspace/delivery/` 预置子目录。
- `spec/constitution.md`（拆出后验证不成立，规范迁回 §四）。
- 根 `package.json`：模板版本标记由本 CHANGELOG 独担。

### Fixed

- 初始化健壮性：有无可提交改动改读 `git status --porcelain`（不依赖 git 本地化措辞）；未配置提交身份时前置探测并给精准提示；`git init -b` 不可用时回退 `git init` + symbolic-ref；目标目录非空时警告并继续、已有文件跳过不覆盖。
- 默认 `.gitignore` 补 `*.crt` / `*.cer` / `*.p7b` / `.htpasswd` / `*.ovpn` 与 `__pycache__/` / `*.pyc`。
