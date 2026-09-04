# project-spec — 云端模块库（SSOT）

本项目是 [The-Daybreaker/Project-Template](https://github.com/The-Daybreaker/Project-Template)
的配套项目，用于存放 spec 和 modules，是 spec 与模块的**唯一事实源**。本地（项目
实例化后的 `spec/`）里的
spec 和模块都是这里的**实例化副本**；防漂移靠锁文件——副本记录「从哪个云端
模块、哪个版本实例化来」+ 内容指纹。

## 结构

| 路径 | 是什么 |
| --- | --- |
| `registry.json` | 仓库目录索引（机器读）：有哪些 spec、哪些模块、各在什么路径 |
| `build/` | 构建规则（默认不读）：怎么造 spec 和模块（`build.md` + 两个模板），按需拉取到项目 `spec/build/` |
| `specs/` | spec（每个 spec 一个目录） |
| `modules/` | 模块（每个模块一个目录，kebab-case 纯 id，不带 `@`） |

## 一个 spec 包 / 模块长什么样

```
specs/<spec-id>/            ← spec
  manifest.json               组织清单（脚本读）：id / version / modules / entries
  AGENTS.md                   本包入口：这是什么 / 依赖全景 / 入口判定（本包运转）
  CHANGELOG.md                版本变更日志

modules/<module-id>/        ← 模块
  MODULE.md                   agent 规范（产物目录与实例化 / 运行过程）
  module.json                 结构化声明（机器读）
  README.md                   给人读（一句话定位 + 适用与边界）
  CHANGELOG.md                版本变更日志
  assets/                     附件（模板 / 清单 / 脚本）
```

## 机制通则与锁文件在哪

spec 包结构、manifest / module.json 字段表、命名、状态灯、空值惯例、拉取
指引、冷启动校验——这些**机制通则的单一来源在项目模板的
`spec/AGENTS.md`**；锁文件工具与字段规范在模板 `spec/lockfile.py` /
`spec/lockfile.md`（出厂自带，不在本仓重复）。spec 包的 `AGENTS.md` 只讲
本包运转。用本仓请从 [通用项目模板](https://github.com/The-Daybreaker/Project-Template)
初始化的项目里操作，或先读模板的 `spec/AGENTS.md`。

## 仓库目录

### specs

- **software-dev**（软件开发）—— `specs/software-dev/`
- **skills-dev**（skill 开发）—— `specs/skills-dev/`

### modules

| id | 名称 |
| --- | --- |
| `vision` | 愿景与排期 |
| `design` | 方案与设计 |
| `prd` | 当期需求 |
| `adr` | 决策记录 |
| `development` | 开发执行 |
| `test` | 测试与验收 |
| `audit` | 审计 |
| `release` | 收口 |

## 版本

模块与 spec 的版本 = 各自 `module.json` / `manifest.json` 里的 `version` 字段
（语义化版本）。
