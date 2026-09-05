# CHANGELOG

本文件记录模板本体的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/spec/v2.0.0.html)。

## [Unreleased]

### Changed

- 随项目分发的 `README.md` 重写为面向项目主人的使用手册：协作层/发布层
  心智模型、「读盘 → 干活 → 写盘」协作循环、高频场景速查、按需装 spec
  三步、三份核心文件分工；「写给用户」节原样保留。
- 同步 spec 新口径：`AGENTS.md` §六与 `spec/AGENTS.md` §一中阶段链由硬
  依赖改为「推荐推进顺序、不强制」，「缩放旋钮」→「流程调节」，「管什么
  场景」→「适用于什么场景」。
- spec 机制单文档化：一个 spec 塌成一份 `spec.md` + 同级 `assets/`（产出
  骨架）。`spec/AGENTS.md` 瘦身为机制说明书（spec 是什么 / 怎么拉 /
  怎么读 / 状态灯约定）；本体 `AGENTS.md`（§一 spec 行、§二 冷启动
  读盘、§六 读取约定）、`README.md`、`init-project/SKILL.md` 同步为新
  口径。配套云端库（project-spec）同步重构：模块装置 / manifest /
  registry 退休。
- 取消人机异步交流三件套，`process/` 重新定性为「协作活状态区」：常驻件
  （`task.md` / `memory.md`）+ 临时件（笔记 / `review-<简介>.md`，用完即清）；
  冷启动改为通读 `process/` 全部文件。review 降为 `process/` 根临时件（通过后
  删、不归档 logs），何时验收交对话或 spec；`memory.md` 改为 agent 自我维护区
  （只声明用途不声明内容）。本体 `AGENTS.md`（§一 / §二 / §三）、`README.md`、
  `init-project/SKILL.md`、`process/memory.md` 与云端 software-dev / skills-dev
  两份 spec 的 development / audit 阶段同步为新口径。
- 目录命名对齐业界惯例：`logs/` 更名 `archive/`（`logs` 是运行日志的事实标准
  名、易被工具写入污染归档语义，`archive` 无此撞名）；删除 `workspace/source/`、
  `workspace/delivery/` 两个预置子目录，`workspace/` 保留为「干活 + 发布层」
  通用声明、内部结构改由 spec / 项目定；配套云端 software-dev / skills-dev 两份
  spec 的产出落点改用业界惯例名 `workspace/src/`、`workspace/dist/`，其 `logs/*`
  归档路径改 `archive/*`。本体 `AGENTS.md`、两份 README、`SKILL.md`、
  `process/memory.md`、`spec/build/build.md` 同步。
- 规范正文从 `AGENTS.md` 拆出到 `spec/constitution.md`（宪章 / 项目级 / 项目
  自己的规范三节 + 「写给用户」头 + 准入 / 分类前言，条款原样搬运）；`AGENTS.md`
  §五 收敛为「宪章」强指针节（声明用户可自行修改 / 添加 / 维护 + 指向
  constitution.md、冷启动必读），§七 并入 constitution.md；冷启动链、§二读盘、
  §六、目录地图、维护权分区、`spec/AGENTS.md`、`init-project/SKILL.md`（用途②
  增加 constitution.md 指向）同步。

### Removed

- 三件套目录 `process/inbox/`、`process/pending/`、`process/reviews/`：异步
  交流在同步对话场景下是伪需求，inbox / pending 整个取消，review 降为 process
  临时件；logs 不再镜像这三个子目录。
- `workspace/source/`、`workspace/delivery/` 预置子目录：框架不再写死工作区
  结构，改由 spec / 项目按惯例（如 `src/`、`dist/`）自行声明。
- 锁文件三件：`spec/lockfile.py`、`spec/lockfile.md`（及实例化后的
  `lockfile.json`）——spec 拉进项目即自由编辑、无只读副本可锁，防漂移
  校验退休；冷启动不再跑 `lockfile.py --verify`。
- 根 `package.json`：`version`（0.9.0）与本 CHANGELOG 的版本标题重复、违反单一
  事实源，且随模块制退休已无脚本读取（原读它的 `build_delivery.py` 早已删除）；
  对非 Node 项目是杂物，对 Node 项目其 version 也是模板版本而非项目自身版本。
  删除后模板版本标记由本 CHANGELOG 独担；`init-project/scripts/init_project.py`
  去掉只服务于它的 `--name` 选项与 `_set_project_name`。

## [0.9.0] - 2026-09-03

版本号对齐发布仓序列（0.1.0 → 0.9.0）：模板本体是发布仓的核心资产，
版本号以本体 `package.json` 为单一事实源，发布仓跟随本体演进。

### Added

- `process/memory.md`：agent 记忆固有件（踩过的坑与被验证过的判断，
  冷启动必读；只存当前有效条目，失效归档 `logs/memory/`）。
- 云端模块库接入：锁文件 `origin` 记真实指向
  （`github.com/The-Daybreaker/project-spec`）；拉取 spec 包时落真实账：
  模块记 source / origin / version / hash（fork 另记 baseline），spec 只记
  source / origin / version 血缘备注，不算指纹、不参与漂移校验。
- 锁文件 source 三态：模块分 cloud / fork / private（self_implemented
  占位同 private、不校验）；source 表来源、hash 有无表是否校验。
  `--fork <id>` 显式登记改造，自建 spec 用 `--spec-source private` 声明
  （origin 留空）。

### Changed

- 术语全局更名：「地基」→「框架」（语义不变）；文档措辞不再用
  「七件套」之类清点式表述。
- README「给用户的规范」瘦身重写为「写给用户」（用户本人重写）。

### Removed

- module.json 的 `enable.instantiate` / `disable.keep` 字段（字段 12 → 10；
  启停运行态由 manifest 的 entries 表达，实例化语义归 MODULE.md）。
- 预置 spec `spec/preset/software-dev`（8 模块）与内置构建规则
  `spec/build/`：框架走查确认模板不依赖 spec 即可以框架形态运转；两者与
  云端模块库内容一致，改为唯一事实源在云端、按需拉取——出厂 `spec/` 只留
  机制三件（`AGENTS.md` 机制说明书 + `lockfile.py` 工具 + `lockfile.md`
  字段规范），spec 包落地为自己的子目录 `spec/<id>/`。
- 密钥门禁（`scripts/scan_secrets.py` + `.githooks/pre-push`）：模板不再
  携带，密钥防护的机械防线只留 .gitignore 的密钥文件名模式；要不要
  额外的门禁与钩子由使用者自行决定。

### Fixed

- `lockfile.py`：指纹计算归一化行尾（CRLF / LF 不再造成跨平台漂移误报）；
  `generate` 改合并语义——保留既有 fork / private 条目的 source / origin，
  private 模块按规范不参与指纹校验（hash 为 null）；module.json 缺
  version 时报错（与字段表「必须填」一致）；`verify` 增加「模块目录存在
  但 manifest 未声明」检查。
- `init_project.py`：目标目录非空时改为警告并继续（跳过已有文件、不覆
  盖），与 SKILL.md 对齐；目标为已存在文件时友好报错；git 缺失或失败
  时以非零退出码反映部分失败。
- 模板 `.gitignore` 补 `__pycache__/` / `*.pyc`；AGENTS.md 两处用户维护
  区指针同步为「写给用户」；README 修正 `AGENTS.md` 大小写。

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
