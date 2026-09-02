# project-spec — 云端模块库（SSOT）

spec 与模块的**唯一事实源**。本地（模板 preset、项目例化后的 `spec/`）里的
spec 和模块都是这里的**例化副本**；防漂移靠锁文件——副本记录「从哪个云端
模块、哪个版本例化来」+ 内容指纹。

## 结构

| 路径 | 是什么 |
| --- | --- |
| `registry.json` | 仓库目录索引（机器读）：有哪些 spec、哪些模块、各在什么路径 |
| `build/` | 构建规则（默认不读）：怎么造 spec 和模块（`build.md` + 两个模板） |
| `specs/` | spec 真身（每个 spec 一个目录） |
| `modules/` | 模块真身（每个模块一个目录，kebab-case 纯 id，不带 `@`） |

## 仓库目录

### specs

- **software-dev**（软件开发）—— `specs/software-dev/`

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
（语义化版本）；仓库整体暂不用 git tag 标记版本。
