# CHANGELOG

发布仓库的版本历史（两产物：project-spec / init-project）。模板本体只在 `init-project/assets/project-template/` 存一份。

版本号与模板本体一致（单一事实源：模板本体 `CHANGELOG.md` 的版本标题），当前 1.0.0。1.0.0 之前的全部历史（0.1.0–0.9.0 及开发期 [Unreleased]）归档于开发仓 `dev/archive/changelog-public-pre-1.0.0.md`。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/spec/v2.0.0.html)。自 1.0.0 起进入稳定期，目录结构与 `AGENTS.md` 协作协议按 SemVer 约束兼容性。

## [1.0.0] - 2026-09-06

首个稳定版。经过三代设计（v1 大而全 → v2 构建解耦 → v3 框架 + spec）与开发期多轮自我重构后定型。

### Added

- `init-project` 成为唯一 skill，新增「项目外通用行为基线」用途：不属于任何项目的非闲聊对话，读取模板 `AGENTS.md` §四宪章 6 条作为行为底线，进入项目后自动让位于项目自己的 AGENTS.md。
- 同仓 `preset-spec/` 最佳实践集：两份工作流示例（software-dev 软件开发、skills-dev skill 开发，均为单份 `spec.md` + `assets/`）与 `build/` spec 构建规则；clone 一次拿全，不随模板分发。
- `process/` 临时件机制：随手笔记与 `review-<简介>.md` 验收件，用完即清、通过后删，历史交给 git。

### Changed

- spec 机制单文档化：一个 spec = 一份 `spec.md`（阶段链 + 概览 + 各阶段三段式）+ 同级 `assets/` 产出骨架，渐进式披露。
- `process/` 重新定性为「协作当前状态区」：常驻件（`task.md` / `memory.md`）原地更新到当前状态，冷启动通读 process/ 全部文件即恢复项目全貌。
- 目录命名对齐业界惯例：`logs/` → `archive/`（避开运行日志标准名）；删除 `workspace/source/`、`workspace/delivery/` 预置，产出落点改用业界通名 `workspace/src/`、`workspace/dist/`，工作区结构改由 spec / 项目声明。
- 规范仍在模板 `AGENTS.md` §四「规范（用户维护区）」：曾拆出 `spec/constitution.md`，验证后全量迁回（同一文件内分区足以划清维护权，分文件只增必读跳数）。
- 三份 README 按「问题场景 → 设计理念 → 快速开始 → 日常使用 → 深入展开」叙事线重写；全文去除手动折行（段落一行写完）；两轮措辞规范化，统一业界通用表达。
- 产品英文名 Project-Template 更名 **project-spec**（与公开仓名一致，中文名仍为「通用项目模板」）。

### Removed

- 模块机制整套：模块目录、`MODULE.md` / `module.json` / 每模块 README·CHANGELOG、spec 级 `manifest.json`、云端 `registry.json`——经第二个 spec 验证，跨 spec 模块复用不成立、小模块配整套机制代价大于收益。
- 锁文件三类（`lockfile.py` / `lockfile.md` / 实例化 `lockfile.json`）：spec 拉进项目即自由编辑，无只读副本可锁。
- 三个异步交流目录 `process/inbox/`、`process/pending/`、`process/reviews/`：同步对话场景下异步机制是伪需求，请示回归对话、验收降为临时件。
- `agent-rules` skill：与模板宪章是两处副本、必然漂移，职责并入 init-project（只指向唯一事实源）。
- 模板本体根 `package.json`：版本与 CHANGELOG 标题重复、对非 Node 项目是杂物，版本标记归 CHANGELOG 独担。
- `workspace/source/`、`workspace/delivery/` 预置子目录。

### 工程与仓库

- 两个公开仓（原发布仓 Project-Template 与原 spec 仓）合并为单一 `project-spec` 仓：迁移分支 `git mv` + `--allow-unrelated-histories` 合并，模板链与最佳实践集链两条历史完整保留；云端 fast-forward 合流，删旧仓前经六步包含性审计、删后复验。
- 模板本体收敛到 9 个出厂文件（空目录以 .gitkeep 占位）；空 spec 也能以框架形态运转（冷启动、任务板、归档、git 卫生均不读 spec）。
- 初始化脚本健壮性：改动判定改读 `git status --porcelain`、提交身份前置探测、旧版 git 无 `init -b` 时回退 symbolic-ref；初始化逐项回读校验，已有文件一律跳过不覆盖。
