# lockfile — 锁文件规范

> spec 包的溯源账本：记录每个模块的来源、版本、内容指纹，防止漂移；spec 本身
> 只留血缘备注（source + origin + version），不做漂移锁。生成 / 校验 / fork 登记
> 工具是同目录的 `lockfile.py`：拉取后跑生成模式落账，冷启动跑校验模式比对，
> fork 内置模块跑 `--fork`。

## 一、为什么需要锁文件

模块从云端模块库拉取而来（拉取指引见 `spec/AGENTS.md`），锁文件是模块溯源的
唯一事实源，回答三件事：

- 这个模块从哪来（云端 / fork / 项目私有）；
- 是什么版本、派生自云端哪个基线版本；
- 有没有被本地改过（未登记的 fork / 漂移）。

spec 不设漂移锁：spec 是用户可自由编排的装配图（改入口、改依赖全景都是正常
操作），锁它只会让每次编排都被误报成漂移。锁文件对 spec 只记 source + origin +
version 作血缘备注——「这套 spec 是云端拉来的还是自建的、最初基于云端哪个 spec
的哪一版」，不算指纹、不校验；自建 spec 的 source 记 private、origin 记 null。

## 二、结构

```json
{
  "lockfileVersion": 1,
  "spec": {
    "source": "cloud",
    "origin": "github.com/The-Daybreaker/project-spec/specs/software-dev",
    "version": "0.1.0"
  },
  "modules": {
    "vision": {
      "source": "cloud",
      "origin": "github.com/The-Daybreaker/project-spec/modules/vision",
      "version": "0.1.0",
      "hash": "def456"
    },
    "prd": {
      "source": "fork",
      "origin": "github.com/The-Daybreaker/project-spec/modules/prd",
      "version": "0.2.0",
      "baseline": "0.1.0",
      "hash": "aaa111"
    },
    "release": {
      "source": "cloud",
      "origin": "github.com/The-Daybreaker/project-spec/modules/release",
      "version": "0.1.0",
      "baseline": "0.1.0",
      "hash": null
    },
    "my-mod": {
      "source": "private",
      "origin": null,
      "version": "0.1.0",
      "hash": null
    }
  }
}
```

上例四种模块形态：`vision` 云端原样（算 hash、校验）；`prd` fork 自云端
（version 是 fork 自己的版本、baseline 记 fork 时的云端版本、hash 登记后校验）；
`release` 是 self_implemented 占位（骨架来自云端、项目自填，hash 为 null 不校验、
baseline 记云端骨架版本）；`my-mod` 项目私有（origin 与 hash 均为 null）。

## 三、字段语义

**顶层** `lockfileVersion`：锁文件格式版本（整数）。开发期保持 1——仓内没有
任何消费方据它分支，格式真演进时再议是否递增。

**`spec` 条目**（血缘备注，不算 hash、不校验）：

| 字段 | 含义 |
| ---- | ---- |
| `source` | `cloud`（云端拉来）/ `private`（项目自建，云端无此 spec） |
| `origin` | 这套 spec 最初基于的云端位置（仓库 + 路径）；`private`（自建）时恒为 `null` |
| `version` | spec 自身版本（取自 `manifest.json` 的 `version`） |

> 自建 spec 首次生成时用 `lockfile.py <spec> --spec-source private` 声明，工具即把
> `source` 记 `private`、`origin` 记 `null`，不再硬拼一个指向云端的假地址；之后
> 重跑 generate 按合并语义保留这一声明。

**`modules.<id>` 条目**（溯源 + 防漂移）：

| 字段 | 含义 |
| ---- | ---- |
| `source` | `cloud`（云端副本）/ `fork`（fork 自云端并本地改动）/ `private`（项目私有） |
| `origin` | 云端模块的真实位置（仓库 + 路径）；`private` 时为 `null` |
| `version` | 本地这份副本的版本（取自模块 `module.json`）：cloud 即云端版本，fork 是 fork 自己的版本 |
| `baseline` | 派生自云端的基线版本——仅 `fork` / `self_implemented` 模块带此字段，记「从云端哪一版派生」，供判断要不要与云端重新同步；`cloud` / `private` 不带（按空值惯例删字段） |
| `hash` | 内容指纹，校验「副本是否被改」；模块顶层 `add.md`（项目内补充，见 `spec/AGENTS.md`）不参与指纹；`private` 与 `self_implemented` 模块为 `null`（内容归项目，不校验） |

`source` 与 `hash` 是两件事：`source` 只表来源，`hash` 有无只表是否做漂移校验。
组合规则——`cloud`：算 hash 且校验；`fork`：登记时重算 hash、之后校验（专抓
登记后又偷改）；`private` 与 `self_implemented`：hash 为 null、不校验。

## 四、生命周期

1. **创建**：引入 spec 时——按拉取指引复制 spec 与模块 → 跑 `lockfile.py`
   生成锁文件。
2. **更新**（只有以下显式操作才动锁文件）：
   - 加私有模块 → 该模块 `source` 记 `private`（origin / hash 为 null）；
   - fork 内置模块 → 跑 `lockfile.py <spec> --fork <模块id>`：工具把该模块
     `source` 由 `cloud` 改 `fork`、`baseline` 记登记时锁文件里的云端版本、
     重算 `hash`（顺序由脚本保证，不必手改 lockfile.json）；fork 自己的迭代
     滚模块 `module.json` 的 `version`、改动记模块 `CHANGELOG.md`；
   - self_implemented 模块（如 release）→ 云端给骨架、项目自填，`hash` 记
     null 不校验、`baseline` 记云端骨架版本；
   - 升级云端模块 → 显式重新实例化，更新 `version` + `hash`；
   - 移除模块 → 删对应条目。
3. **校验**：冷启动时比对「本地模块内容 hash vs 锁文件 hash」（hash 为 null
   的 private / self_implemented 模块跳过），不一致说明有未登记的 fork / 漂移，
   提示用户。spec 不参与校验。
4. **不更新**：正常运行不漂移——云端发新版，本地锁文件锁定旧版，不悄悄变。
5. **删除**：移除 spec 时整个锁文件作废。

## 五、管理规范

- **进 git**：锁文件是溯源账本，随 spec 一起版本管理。
- **维护者**：agent 冷启动时校验（`lockfile.py --verify`）、变更时更新
  （`lockfile.py` 生成模式；fork 登记用 `lockfile.py <spec> --fork <模块id>`；
  生成是合并语义——保留既有 fork / private 条目的 source / origin / baseline，
  只重算 hash / version，手工登记的溯源不会被冲掉）。
- **纪律**：日常干活不碰锁文件；只有「引入 / 移除 / fork / 升级」才更新。
