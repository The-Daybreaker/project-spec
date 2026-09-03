# lockfile — 锁文件规范

> spec 包的来源标注账本：记录 spec 与每个模块的来源、版本、内容指纹，防止
> 漂移。生成 / 校验工具是同目录的 `lockfile.py`：拉取后跑生成模式落账，
> 冷启动跑校验模式比对。

## 一、为什么需要锁文件

来源是两层的：spec 与模块都从云端模块库来（拉取指引见 `spec/AGENTS.md`）。
锁文件是溯源唯一事实源，回答三件事：

- 这个 spec / 模块从哪来（云端还是项目私有）；
- 是什么版本；
- 有没有被本地改过（fork / 漂移）。

## 二、结构（两层）

```json
{
  "lockfileVersion": 1,
  "spec": {
    "source": "cloud",
    "origin": "github.com/The-Daybreaker/project-spec/specs/software-dev",
    "version": "1.0.0",
    "hash": "abc123"
  },
  "modules": {
    "vision": {
      "source": "cloud",
      "origin": "github.com/The-Daybreaker/project-spec/modules/vision",
      "version": "1.0.0",
      "hash": "def456"
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

## 三、字段语义

| 字段 | 含义 |
| ---- | ---- |
| `lockfileVersion` | 锁文件格式版本（整数，格式变更时递增） |
| `source` | `cloud`（云端副本）/ `fork`（fork 自云端）/ `private`（项目私有） |
| `origin` | 云端 spec / 模块的真实位置（仓库 + 路径，如 `github.com/The-Daybreaker/project-spec/modules/vision`）；`private` 时为 `null` |
| `version` | 来源版本（云端版本）；`private` 时是自身版本 |
| `hash` | 内容指纹，用于校验「副本是否被改」（识别 fork / 漂移）；模块顶层 `add.md`（项目内补充，见 `spec/AGENTS.md`）不参与指纹，改它不算漂移；`private` 时为 `null`（项目私有模块不参与指纹校验） |

## 四、生命周期

1. **创建**：引入 spec 时——按拉取指引复制 spec 与模块 → 跑 `lockfile.py`
   生成锁文件。
2. **更新**（只有以下显式操作才动锁文件）：
   - 加私有模块 → `modules` 加一条 `source: "private"`；
   - fork 内置模块 → 该模块 `source` 由 `cloud` 改 `fork`，重算 `hash`；
   - 升级云端模块 → 显式重新例化，更新 `version` + `hash`；
   - 移除模块 → 删对应条目。
3. **校验**：冷启动时比对「本地内容 hash vs 锁文件 hash」，不一致说明有未登记
   的 fork / 漂移，提示用户。
4. **不更新**：正常运行不漂移——云端发新版，本地锁文件锁定旧版，不悄悄变。
5. **删除**：移除 spec 时整个锁文件作废。

## 五、管理规范

- **进 git**：锁文件是溯源账本，随 spec 一起版本管理。
- **维护者**：agent 冷启动时校验（`lockfile.py --verify`）、变更时更新
  （`lockfile.py` 生成模式；生成是合并语义——保留既有 fork / private 条目
  的 source / origin，只重算 hash / version，手工登记的溯源不会被冲掉）。
- **纪律**：日常干活不碰锁文件；只有「引入 / 移除 / fork / 升级」才更新。
