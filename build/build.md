# build — 构建规则（怎么造 spec 和模块）

> 本目录是「构建规则」层（决策 11 的 L0），回答「spec 和模块长什么样、怎么
> 造、怎么组合、怎么溯源」。它是**预置的、非包**的元规范，随模板本体分发，
> 不隶属任何一套 spec。
>
> **默认不读**：日常执行任务（判定入口、走模块）不读本文件；只有「设计或
> 修改 spec / 模块」时才读。日常要读的是「使用规则」——仓库根 `AGENTS.md`、
> 各 spec 的 `AGENTS.md`、各模块的 `MODULE.md`。

## 一、规则分两类：构建规则 vs 使用规则

一套项目里同时存在两类规则，性质相反，别混：

| | 构建规则 | 使用规则 |
| --- | --- | --- |
| 回答什么 | 怎么**造** spec 和模块 | 怎么**用** spec 和模块 |
| 读者 | 设计 / 修改 spec 模块的人或 agent | 日常执行任务的人或 agent |
| 默认读不读 | **默认不读**（只在造 / 改时读） | **默认要读**（每次任务都读） |
| 落点 | `spec/build/`（本目录） | 根 `AGENTS.md`、spec 的 `AGENTS.md`、模块的 `MODULE.md` |
| 命名 | 非 `AGENTS.md`（避免被各软件自动扫描误读） | `AGENTS.md`（本就该被自动读到） |

一句话：**构建规则是「说明书怎么造」，使用规则是「说明怎么用」**。造 spec /
模块时才翻开前者，日常干活只靠后者。

## 二、三层体系（这套东西怎么分层）

```
构建规则（本目录，预置非包）
   ↓ 照着造
spec 包（内置默认 + 外部导入 + 自建；单项目单 spec）
   ↓ 增补
项目补丁（纯增量：加私有模块、fork 内置，不改内置本体）
```

- **构建规则**：本目录，spec 无关——任何 spec 都照它造。
- **spec 包**：具体一套工作流（如 software-dev），从云端模块库拉取例化。
- **项目补丁**：项目对 spec 的增量修改，靠锁文件的 `source` 字段标记
  （`private` / `fork`），见各 spec 的 `lockfile.md`。

来源是两层的：spec 与模块都从云端模块库来（拉取流程见 §九；首次拉取的
入口指引在仓库根 `AGENTS.md` 与 `README.md`）。溯源统一归锁文件，不在
spec / 模块文件里重复记。

## 三、spec/ 的布局

模板出厂只有 `build/`（构建规则层）；spec 包按需从云端拉取，例化后与
`build/` 并存于 `spec/` 根：

```
spec/
  build/                     ← 构建规则（默认不读）
    build.md                 ← 本文件
    spec-template/           ← spec 模板（造新 spec 骨架）
    module-template/         ← module 模板（造新模块骨架）
    scripts/lockfile.py      ← 锁文件生成与校验
  （拉取例化后）AGENTS.md / manifest.json / CHANGELOG.md /
  lockfile.json / @<模块>/   ← spec 包（来源与拉取见 §九）
```

模板是「源头」，例化 = 从模板复制出实例，实例自带模板里的东西。

## 四、模块形态：一个模块一个目录

```
@<module-id>/                   ← 一个模块一个目录（目录名 = @ + id）
  MODULE.md                     ← agent 规范（开头声明适用范围）+ 产物目录与例化
  module.json                   ← 结构化声明（机器读）
  README.md                     ← 给人读：一句话定位 + 适用与边界 + 启用/停用
  CHANGELOG.md                  ← 版本变更日志（跨版本迁移看它）
  assets/                       ← 附件（模板 / 清单 / 脚本，随模块走）
```

新建模块：复制 `module-template/` 目录，改名为 `@模块 id`，替换 `<占位符>`，
按字段表填 `module.json`（字段表见各 spec 的 `AGENTS.md`）。三步：① 复制
改名 → ② 填 `module.json` → ③ 改写 `MODULE.md` 与 `README.md`。

## 五、模块命名规则

- **目录名 = `@` + id**：`@` 只作目录标识，让人一眼认出模块目录；模块 id 不含
  `@`（`module.json` 的 `id` 是 `vision`）。
- **id 用连字符小写命名**（kebab-case：全小写、单词间用 `-` 连接，如
  `software-dev`、`@vision`），与目录名（去 `@` 后）一致。
- **模块规范叫 `MODULE.md`**（不叫 `AGENTS.md`）：模块规范是按需读的，叫
  `AGENTS.md` 会被各 agent 软件按不同策略自动扫描，改 `MODULE.md` 靠指针主动
  加载，行为可控。

## 六、粒度判据（什么算一个模块）

三条同时满足才拆成独立模块：**跨场景复用**（不只一个场景用）、**独立启停**
（能单独启用停用）、**输入输出隔离**（有明确输入与产出）。不满足就并进现有
模块，或留给地基，不硬拆。

## 七、spec 包形态

一个 spec 包 = 组织清单（`manifest.json`）+ 入口指引（`AGENTS.md`）+ 模块
目录（`@模块`）。文件结构介绍与 manifest 字段表见各 spec 的 `AGENTS.md`——
spec 要自解释，0 上下文 agent 读 spec 内部就能懂，不必查本文件。

`manifest.json` 与 `AGENTS.md` 的分工，沿用「json 放脚本会读的、语义写
AGENTS.md」：

- **入口路径**（每个入口启用哪些模块）→ `manifest.json` 的 `entries`，脚本能读；
- **入口判定**（什么算微调 / 小功能 / 一期）→ `AGENTS.md`，是语义，agent 读。

## 八、入口缩放机制（设计规则）

一套 spec 不该只有一个「全流程」入口，而应定义**多个入口**，不同等级的任务
从不同入口进、启用不同模块子集——简单的事不背重流程，复杂的事不漏环节。

- **入口定义**（启用哪些模块）在 `manifest.json` 的 `entries`，是「集合、不表
  顺序」，执行顺序由依赖图决定；
- **入口判定语义**在 `AGENTS.md`（agent 读）；
- **模块间依赖与并行**用一张 mermaid 全景图表达（放在 `AGENTS.md` 里），让人
  一眼看懂、让 AI 能拓扑排序；`depends_on` 只是 agent 运行某模块时才读的字段，
  不做全局依赖唯一来源。

## 九、spec 的来源：云端模块库

spec 包的唯一事实源在云端模块库 `github.com/The-Daybreaker/project-spec`
（README + `registry.json` 目录索引 + `build/` + `specs/` + `modules/`）。
项目需要 spec 时从云端拉取：读 `registry.json` 选 spec 与模块 → `git clone`
云端仓库到临时目录 → 把 spec 目录与模块目录复制进项目 `spec/` → 跑
`lockfile.py`（生成模式）生成锁文件记来源与指纹。拉取交 agent 判断执行，
不写拉取脚本；拉取与冷启动校验的详细规范随 spec 自带（各 spec 的
`AGENTS.md`）。单项目单 spec，缩放靠入口解决，不需要一个项目挂多套 spec。

## 十、版本号规则与 CHANGELOG

**版本号（SemVer）**：模块与 spec 的 `version` 遵循语义化版本，格式
`主.次.修订`（如 `0.1.0`）：

- **主版本（首位）**：不兼容的变更才 +1（改了别人依赖的接口 / 行为），+1 时
  次、修订归零；
- **次版本（中位）**：向后兼容的新增才 +1（加新功能、加新模块）；
- **修订号（末尾）**：向后兼容的修复才 +1（改 bug、改措辞）；
- **主版本为 0**：开发期，接口不稳定，任何版本都可能变，不做兼容承诺；1.0.0
  起才承诺接口稳定。

**CHANGELOG**：每个模块和 spec 都带 `CHANGELOG.md`，按版本记录变更（分类参考
Keep a Changelog：Added / Changed / Removed / Fixed）。跨版本迁移时，agent 读
它就知道「从旧版迁到新版要注意什么」，不兼容的变更（主版本 +1）必须写清。
