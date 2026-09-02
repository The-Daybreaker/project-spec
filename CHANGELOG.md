# CHANGELOG

发布仓库的版本历史（三产物：project-template / init-project / agent-rules）。
模板本体的变更记录另见 `project-template/CHANGELOG.md`，其版本号与发布版本
解耦、各自演进。

条目粒度与 GitHub Release 对齐；更细的版本明细可按 git tag
（`v1.0.1` \~ `v1.6.1.patch1`）追溯对应提交。

## \[1.8.0] - 2026-09-03

云端模块库接入 + spec 模块字段精简。

### Added

- 云端模块库机制：`github.com/The-Daybreaker/project-spec` 作为 spec / 模块
  唯一事实源（SSOT），仓库结构 `registry.json`（目录索引）+ `build/`（构建
  规则）+ `specs/`（spec 真身）+ `modules/`（模块真身）。
- 锁文件落账：`spec/build/scripts/lockfile.py`（生成 + 校验两模式），
  `origin` 记真实仓库路径；预置 spec 锁文件已落真实账（来源 + 版本 + 指纹）。
- spec 的 `AGENTS.md` 新增「锁文件：引入与冷启动校验」一节——引入 spec 的
  拉取流程 + 冷启动 hash 校验（拉取交 agent，不写拉取脚本）。

### Removed

- module.json 的 `enable.instantiate` / `disable.keep` 字段（启停运行态由
  `manifest.json` 的 entries 表达，字段 12 → 10）。

## \[1.7.0] - 2026-09-02

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

- 发布仓库顶层 `CHANGELOG.md`（本文件，含 v1 各版本摘要）。

### Changed

- `init-project` skill 重构：内嵌 v3 模板镜像，初始化含 hooksPath 配置与
  回读校验清单（内联 SKILL.md）。

- `agent-rules` skill 重构：模板宪章的项目外精简形态（version 1.7.0）。

- 发布 README 重写（价值主张 / 快速开始 / 目录结构 / 版本说明）。

### Removed

- v1 结构整体移除：`private/` 子仓库、`docs/`、`dist/`、`archive/`、
  `.github/workflows/`、`version.json`、`install-targets.json` 及大部分
  维护脚本。

## \[1.6.1] - 2026-08-28

接口设计与设计环节补全 + 红线三要素收尾（patch0 + patch1 两次补丁）：
设计契约文件夹（架构 / 接口 / 数据 / 安全，适用必做、不适用须声明）；
接口契约场景化——用户审场景映射表、不审技术，确认后冻结，验收用例联动；
文档质量可持续机制（质量标准 + 反 AI 感清单 + 审计文档质量关）；红线 18
补齐显式三要素，19 条红线三要素终检齐全。

## \[1.6.0] - 2026-08-28

漂移免疫与文档架构改造（断代版本，不向前兼容）：单一真相源三层结构——
15 条规范事实各有唯一家（事实台账 + FACT/REF/INJECT 锚点机制）；漂移免疫
门禁（重复检测 / 摘要限长 / 正文指纹校验）；文档集归一；阶段契约（每阶段
必做清单 + 裁剪属性）；需求冲突检测入口闸；测试台账；安装目标扩至九处。

## \[1.5.0] - 2026-08-27

红线与要求可验证性改造：新增最顶层红线「要求三要素元规范」（所有红线
须同时具备意图 / 展示面 / 验收面，自指示范）；新增红线「敏感信息与私有区
边界」（密钥内容级扫描 + 推送前安全门禁三层）；「范围克制」与「提问共识」
两条红线重写（番茄炒蛋比喻入正文、共识卡机制）；测试正式子阶段与测试
报告双区；辩护性措辞扫描；历史泄露处置与全历史身份重写。

## \[1.4.2] - 2026-08-27

第九轮全面审计修复收口：新项目首跑即红等 5 项发现全修 + 表述面同类残留
清理；防再发机制——开箱即用冒烟自检（初始化 + 回读 + 骨架脚本自检，
发版前必绿）。

## \[1.0.0 – 1.4.1] - 2026-08-15 \~ 2026-08-27

v1 从首个版本到第四轮审计的演进期：从「通用项目模板 + init-project
skill」起步，逐步长出开发前规范（PRD / RFC / ADR / RESEARCH 四登记册）、
P1-P5 五阶段工作流、agent-rules skill、Python 维护脚本链、私有区与密钥
门禁、安装表与副本校验、agent 提问与共识确认机制等骨架，其间历经多轮
全面审计与修复（1.3.2 三域审计处置 16 项、1.4.0 架构重构、1.4.1 版本号
改四段式）。
