# project-spec — 云端 spec 货架

本仓是[通用项目模板 Project-Template](https://github.com/The-Daybreaker/Project-Template)
的配套公开仓。模板提供每个项目都一样的协作框架，本仓提供按需取用的
工作流 spec。

## spec 是什么

一个 spec = **一份 `spec.md` 主干 + 一个同级 `assets/`（产出文档骨架）**：

- **`spec.md`**：这套工作流的全部内容——管什么场景、有哪几个阶段、阶段之间
  怎么依赖、设几档入口（缩放旋钮）、哪里设检查点，以及每个阶段的产出落点、
  运行过程与规范边界。一份文档读完就懂整套工作流。
- **`assets/`**：各阶段产出文档的参考骨架（如愿景、方案、PRD、测试用例、
  决策记录的模板），`spec.md` 按需指向它们。这是「渐进披露」：主文档保持
  精炼当路标，骨架作为附件按需读，不把全部塞进一个文件。

**本仓只是货架、供浏览与取用**。spec 是高度定制化的东西，拉进项目后大概率
要按项目情况改，所以本仓**不做只读锁定、也没有防漂移校验**——拉一份下来
就是你的，自由改。

## 本仓有什么

| 路径 | 是什么 |
| --- | --- |
| `specs/` | spec 货架：每个 spec 一个目录，内含 `spec.md` + `assets/` + `CHANGELOG.md` |
| `build/` | 构建规则：`build.md`（怎么写一份 spec.md）+ `spec-template/`（spec.md 骨架母版）；默认不读，只有造 / 改 spec 时才拉 |

**现有哪些 spec、各自管什么场景、什么版本，直接看 `specs/` 目录**——每份
`spec.md` 开头就写明它管什么场景与版本。本 README 不复制清单，免得两处
记账、清单过时。

## 怎么消费本仓

日常干活不在本仓里进行，消费动作发生在**由 Project-Template 初始化的项目**
中。模板出厂时，项目的 `spec/` 目录已自带机制说明书 `AGENTS.md`（讲 spec
是什么、怎么拉、怎么读）。分两种场景：

**1. 用现成工作流（拉一份 spec）**：

1. 浏览 `specs/` 选定一个 spec，读它 `spec.md` 开头确认场景合适；
2. clone 本仓到临时目录（或直接下载）；
3. 把 `specs/<id>/` 里的 `spec.md` + `assets/` 复制进项目的 `spec/<id>/`
   （`CHANGELOG.md` 是货架的版本历史，可不带——项目本地以 git 为准）；
4. 之后这份 `spec.md` 归项目所有，按项目情况自由改。

**2. 造 / 改 spec**：把本仓 `build/` 拉到项目的 `spec/build/`，按 `build.md`
的规则和 `spec-template/` 母版操作；造好的内容可回流本仓，成为新的货架版本。

spec 机制的说明书随模板出厂、不在本仓（本仓只放 spec 内容本身）；在项目里
读 `spec/AGENTS.md`。

## 版本

每个 spec 的版本写在它 `spec.md` 顶部，变更历史记在同目录 `CHANGELOG.md`，
遵循语义化版本（SemVer）；`build/` 的版本写在 `build.md` 顶部。spec 拉进
项目后归项目自由改，本仓的版本只标「货架上这是哪一版」，供日后对照升级。
