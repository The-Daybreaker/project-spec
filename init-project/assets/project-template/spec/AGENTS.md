# spec/ — 声明式规范（spec 机制说明书）

> 结构是框架，工作流是 spec。本目录出厂只有三个文件：本文件（机制说明 +
> 拉取指引）、`lockfile.py`（锁文件生成与校验工具）、`lockfile.md`（锁文件
> 字段规范，低频读）。spec 包与构建规则都从云端模块库按需拉取，不随模板
> 预置——云端是唯一事实源，防两处漂移。

## 一、拉取指引

云端模块库（唯一事实源）：`github.com/The-Daybreaker/project-spec`

1. 读云端根目录 `registry.json`，确认有哪些 spec、哪些模块、各在什么路径；
2. `git clone` 云端仓库到临时目录；
3. 复制进本目录：
   - **spec 包**（要工作流时）：`specs/<id>/` 整目录 → `spec/<id>/`，再把它
     声明的各 `modules/<id>/` 复制为 `spec/<id>/@<id>/`；
   - **构建规则**（要造 / 改 spec 或模块时）：`build/` 整目录 → `spec/build/`
     （build.md + spec-template/ + module-template/，纯文档与模板）；
4. 跑 `python spec/lockfile.py spec/<id>` 生成 `spec/<id>/lockfile.json`（记
   来源与指纹）；已拉过则跑 `--verify` 校验漂移。

拉取交 agent 判断执行，不写拉取脚本：拉什么、哪个版本是决策，`git clone` +
复制只是几条命令；而且拉取脚本也没法放进云端仓库——否则拉取之前就得先
拉取脚本。

## 二、spec 包结构（拉取后长什么样）

```
spec/<spec-id>/
  manifest.json      ← 组织清单（脚本读）：spec 身份 + 模块声明 + 入口
  AGENTS.md          ← 包入口（本包运转：这是什么 / 依赖全景 / 入口判定）
  CHANGELOG.md       ← 版本变更日志（跨版本迁移看它）
  lockfile.json      ← 锁文件账本（拉取时由 lockfile.py 生成）
  @<模块 id>/        ← 模块目录，每个内含 MODULE.md / module.json /
                       README.md / CHANGELOG.md / assets / add.md（按需）
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

### module.json 字段（10 字段）

读模块的 `module.json` 时查这张表：

| 字段 | 类型 | 语义 | 缺失时按什么处理 |
| --- | --- | --- | --- |
| `id` | string | 唯一标识（连字符小写命名） | 必须填，缺失报错 |
| `name` | string | 模块名 | 必须填 |
| `version` | string | 版本（semver） | 必须填 |
| `description` | string | 一句话职责（看板 / 清单展示） | 必须填 |
| `input` | string[] | 输入来源（组装画依赖线 / 看板展示） | 视为 `[]` |
| `output` | string[] | 产出物（下游认领的契约） | 视为 `[]` |
| `depends_on` | string[] | 强依赖的模块 id（仅必要才写，默认空） | 视为 `[]`（无强依赖） |
| `workspace` | object | 键 = 产物名，值 = 落点路径 | 视为 `{}` |
| `private` | bool | `true` = 项目私有外挂模块 | 视为 `false` |
| `self_implemented` | bool | `true` = 占空自实现，项目自填 | 视为 `false` |

补充约定：

- **json 放脚本会读的**：字段供脚本解析（构建 / 例化脚本读 id / name /
  version / depends_on / workspace；清单脚本读 description / input /
  output）。脚本不消费、纯给人 / agent 读的语义（适用与边界、依赖哪个产出、
  运行过程、产物内容），写进 `MODULE.md` 或 `README.md`，不进 json。
- **依赖只记强依赖**：`depends_on` 只写「不依赖对方模块就无法运转」的依赖
  （如 release → audit），默认为空；模块是独立能力，不感知其他模块，内部
  描述如非必要不提其他模块。谁依赖谁、执行顺序、检查点等编排语义，由各
  spec 的 `AGENTS.md` 依赖全景图表达。
- **来源标注归锁文件**：模块是「云端例化副本」还是「项目私有」，源头与
  版本不进 `module.json`，归锁文件（见第四节）。

### 命名

- **模块目录名 = `@` + id**：`@` 只是目录标识，让人一眼认出模块目录；模块
  id 不含 `@`（`module.json` 的 `id` 是 `vision`）。
- **id 用连字符小写命名**（kebab-case：全小写、单词间 `-` 连接，如
  `software-dev`、`@vision`）。
- **模块规范叫 `MODULE.md`**（不叫 `AGENTS.md`）：模块规范是按需读的，叫
  `AGENTS.md` 会被各 agent 软件按不同策略自动扫描，改 `MODULE.md` 靠指针
  主动加载，行为可控。

## 三、惯例（全局通用）

### 状态灯：写在文档头部

模块的产出文档若有生命周期状态（如 PRD 的草稿 → 开发中 → 定格），不在
`module.json` 里声明，而是**写在每个产出文档的头部**两行：

```
> 状态：草稿
> 换档：交付给下游 → 开发中；开发完成 → 定格
```

- 换档即改「状态」那一行，随文档修改一起落盘（历史交给 git）。
- 头部没有状态声明的文档 = 活文档，随时可改。
- 换档事件的达标线（什么算交付达标）由 spec 定义，不写在文档头部。

### 空值处理惯例

- **空但有语义 → 留空**（`[]` / `{}`）：如 `depends_on: []` 表示「无依赖」，
  是有效信息。
- **不适用 → 删字段，不写 `null`**：字段对本模块无意义时直接删，不占位。
- **适用但值暂缺 → 留 `null`** 显式标注（如版本约束未定时）。

### 模块本地补充：add.md

模块目录可按需带一个顶层 `add.md`：记这个项目里对模块的补充信息——项目
特有的约定、参数、踩坑备注等。它是例化后项目自己的增补：云端模块不带它，
不参与锁文件指纹（改它不算漂移）。

## 四、锁文件与冷启动校验

锁文件（`spec/<id>/lockfile.json`）是 spec 包的溯源账本：记录 spec 和每个
模块从云端哪个版本例化来 + 内容指纹（hash），防止副本漂移。字段定义和完整
生命周期见同目录 `lockfile.md`（低频才读，只讲字段）。

每次冷启动（新会话恢复上下文）时，跑
`python spec/lockfile.py spec/<id> --verify` 比对本地内容指纹与锁文件记录：

- 一致 → 无漂移，正常干活；
- 不一致 → 有未登记的 fork / 改动，停下来提示用户，不要擅自继续。
