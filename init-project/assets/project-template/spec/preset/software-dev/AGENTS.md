# AGENTS.md — 软件开发 spec（使用规则）

> **适用范围**：本项目启用「软件开发」spec 时，agent 承担开发任务先读本文件
> 判定入口、走路径。项目级总纲见仓库根 `AGENTS.md`。
>
> 本文件是**使用规则**（默认读）。「怎么造 / 改 spec 和模块」是构建规则，
> 默认不读，见 `spec/build/`。

## 一、这个 spec 是什么

「软件开发」场景的工作流，由 8 个模块按依赖链编排：

- vision（愿景与排期）→ design（方案与设计）→ prd（当期需求）→
  development（开发执行）→ test（测试与验收）→ audit（审计）→ release（收口）；
  adr（决策记录）横切全局。

模块目录以 `@` 前缀标识（如 `@vision/`）；`@` 只是目录命名，模块 id
不含 `@`（`module.json` 的 `id` 是 `vision`）。

## 二、这个 spec 包里有什么

```
software-dev/
  manifest.json      ← 组织清单（脚本读）：spec 身份 + 模块声明 + 入口
  AGENTS.md          ← 入口指引（本文件，默认读）
  CHANGELOG.md       ← 版本变更日志（跨版本迁移看它）
  lockfile.md        ← 锁文件规范：讲有哪些字段
  lockfile.json      ← 锁文件账本：空示例，初始化时 agent 照着填
  @vision/ @design/ @prd/ @adr/ @development/ @test/ @audit/ @release/
                     ← 8 个模块目录，每个内含 MODULE.md / module.json / README.md / CHANGELOG.md / assets
```

### manifest.json 字段

| 字段 | 类型 | 语义 |
| --- | --- | --- |
| `id` | string | spec 唯一标识（连字符小写命名） |
| `name` | string | spec 名 |
| `version` | string | 版本（semver） |
| `description` | string | 一句话说明这套 spec 管什么场景 |
| `modules` | string[] | 模块声明：这个 spec 需要哪些模块 |
| `entries` | object[] | 入口列表（缩放旋钮） |
| `entries[].id` | string | 入口标识（连字符小写命名） |
| `entries[].name` | string | 入口名 |
| `entries[].modules` | string[] | 这个入口启用哪些模块（集合，不表顺序） |

## 三、依赖全景与入口

### 依赖全景（谁依赖谁）

```mermaid
flowchart LR
    vision --> design
    vision --> prd
    adr --> design
    prd --> development
    design --> development
    design --> test
    prd --> test
    development --> test
    development --> audit
    test --> audit
    adr --> audit
    audit --> release
```

箭头 =「上游 → 下游」（`vision --> design` 表示 design 依赖 vision）。

prd 与 design 并行（都只依赖 vision），adr 横切（design、audit 都依赖它）。

依赖是必要而非充分条件，依赖文件是必需的，但是不代表只需要。

### 入口（启用哪些模块）

按「是否动需求 / 是否动设计 / 是否要发布」三个维度判定入口（入口可配置，改
`manifest.json` 的 entries）：

| 入口          | 判定                             | 启用的模块                                                        |
| ----------- | ------------------------------ | ------------------------------------------------------------ |
| 微调 tweak    | 不动需求、不动设计、不发布（错字 / 小 bug / 样式） | development                                                  |
| 小功能 feature | 动需求、不动架构、不发布（一个明确小功能）          | prd + development + test                                     |
| 一期 phase    | 动排期、可能动设计、要发布（完整一期）            | vision + design + prd + development + test + audit + release |

「启用的模块」是集合、不表顺序；执行顺序与依赖看上面的全景图。adr 横切、
不列入入口。路径外的模块不启用。入口判定拿不准时，先和用户对齐一句再动手。

## 四、模块字段表（module.json 10 字段）

填模块的 `module.json` 时查这张表：

| 字段 | 类型 | 语义 | 缺失时按什么处理 |
| --- | --- | --- | --- |
| `id` | string | 唯一标识（连字符小写命名） | 必须填，缺失报错 |
| `name` | string | 模块名 | 必须填 |
| `version` | string | 版本（semver） | 必须填 |
| `description` | string | 一句话职责（看板 / 清单展示） | 必须填 |
| `input` | string[] | 输入来源（组装画依赖线 / 看板展示） | 视为 `[]` |
| `output` | string[] | 产出物（下游认领的契约） | 视为 `[]` |
| `depends_on` | string[] | 依赖的模块 id | 视为 `[]`（无依赖） |
| `workspace` | object | 键 = 产物名，值 = 落点路径 | 视为 `{}` |
| `private` | bool | `true` = 项目私有外挂模块 | 视为 `false` |
| `self_implemented` | bool | `true` = 占空自实现，项目自填 | 视为 `false` |

补充约定：

- **json 放脚本会读的**：字段供脚本解析（构建 / 例化脚本读 id / name /
  version / depends_on / workspace；清单脚本读
  description / input / output）。脚本不消费、纯给人 / agent 读的语义（适用
  与边界、依赖哪个产出、运行过程、产物内容），写进 `MODULE.md` 或
  `README.md`，不进 json。
- **依赖只记模块 id**：`depends_on` 只列「依赖哪些模块」；「依赖它的哪个
  产出」是语义，写在 `MODULE.md`。
- **来源标注归锁文件**：模块是「云端例化副本」还是「项目私有」，源头与
  版本不进 `module.json`，归 `lockfile.md`。

## 五、状态灯：写在文档头部

模块的产出文档若有生命周期状态（如 PRD 的草稿 → 开发中 → 定格），不在
`module.json` 里声明，而是**写在每个产出文档的头部**两行：

```
> 状态：草稿
> 换档：交付给下游 → 开发中；开发完成 → 定格
```

- 换档即改「状态」那一行，随文档修改一起落盘（历史交给 git）。
- 头部没有状态声明的文档 = 活文档，随时可改。
- 换档事件的达标线（什么算交付达标）由 spec 定义，不写在文档头部。

## 六、空值处理惯例

- **空但有语义 → 留空**（`[]` / `{}`）：如 `depends_on: []` 表示「无依赖」，
  是有效信息。
- **不适用 → 删字段，不写 `null`**：字段对本模块无意义时直接删，不占位。
- **适用但值暂缺 → 留 `null`** 显式标注（如版本约束未定时）。

## 七、锁文件：引入与冷启动校验

锁文件（`lockfile.json`）是本 spec 包的溯源账本：记录 spec 和每个模块从云端
哪个版本例化来 + 内容指纹（hash），防止副本漂移。字段定义和完整生命周期见
`lockfile.md`（低频才读，只讲字段）；这里写 agent 日常要做的两件事。

### 引入本 spec（从云端拉取）

项目还没有本 spec 时，从云端仓库 `github.com/The-Daybreaker/project-spec` 拉取：

1. 读云端根目录 `registry.json`，确认有哪些 spec、哪些模块、各在什么路径；
2. `git clone` 云端仓库到临时目录，把需要的 spec 目录和模块目录复制进项目 `spec/`；
3. 跑 `lockfile.py`（生成模式）扫描 spec 包，生成 `lockfile.json`，记下来源与指纹。

拉取交给 agent 判断执行，**不写拉取脚本**：拉什么、哪个版本是决策，`git clone` +
复制只是几条命令，脚本帮不上忙；而且拉取脚本也没法放进云端仓库——否则拉取之前
就得先拉取脚本。

### 冷启动校验

每次冷启动（新会话恢复上下文）时，跑 `lockfile.py --verify` 比对本地内容指纹与
锁文件记录：

- 一致 → 无漂移，正常干活；
- 不一致 → 有未登记的 fork / 改动，停下来提示用户，不要擅自继续。
