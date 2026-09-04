# project-spec — 云端模块库（spec 与模块的唯一事实源）

本仓是[通用项目模板 Project-Template](https://github.com/The-Daybreaker/Project-Template)
的配套公开仓。模板提供每个项目都一样的协作框架，本仓提供按需装配的
工作流内容，两者分工如下：

- **spec 是「装配图」**：一套工作流启用哪些模块、设几档入口、模块之间
  按什么顺序配合，这套编排就是一个 spec；
- **模块是「标准件」**：一项自持的独立能力（有明确的输入、运行过程和
  产出，模块之间互不感知），供 spec 挑选组装；
- **build 是「构建规则」**：怎么设计、修改 spec 与模块的规则说明和母版。

项目里实际用到的 spec 和模块，都是从本仓拉取、复制进项目的**实例化
副本**。防漂移机制：模块带内容指纹，由项目里的锁文件记账，副本被改动
时冷启动校验会发现；spec 只登记它基于的云端来源与版本（血缘备注），
不做指纹锁定。**当前有哪些 spec、哪些模块、各自在什么路径，一律以根
目录的 `registry.json` 为准**，本 README 不复制清单，以免两处记账、
清单过时。

## 本仓有什么

| 路径 | 是什么 |
| --- | --- |
| `registry.json` | 仓库总目录索引（机器可读）：全部 spec、模块与构建规则的 id、名称和路径，选货先查它 |
| `specs/` | spec 货架：每个 spec 一个目录，只存「组织清单 + 包入口 + 变更日志」三件，模块不内嵌 |
| `modules/` | 模块货架：每个模块一个目录，目录名是纯 id（kebab-case，不带 `@`） |
| `build/` | 构建规则层：`build.md` 讲解 + `spec-template/`、`module-template/` 两个母版；默认不读，只有造 / 改 spec 或模块时才拉取 |

## spec 和模块的区别

两者是不同层级的东西，改动的自由度也不同：

| | 模块＝「标准件」 | spec＝「装配图」 |
| --- | --- | --- |
| 本仓存哪 | `modules/<id>/`，各模块独立存放 | `specs/<id>/` 只存三件，不内嵌模块 |
| 进项目后 | 复制为 `spec/<spec-id>/@<id>/`（`@` 前缀实例化时才加） | 整包复制为 `spec/<spec-id>/` |
| 改动自由度 | 从云端原样使用，默认不直接改 | 编排自由，随时可改 |
| 锁文件记什么 | 来源 + 版本 + **内容指纹**，私自改动会被校验发现 | 只记来源 + 版本血缘，**不做指纹校验** |

## 一个 spec / 模块在本仓长什么样

```text
specs/<spec-id>/            ← spec：云端只存三件，模块独立在 modules/
├── manifest.json           #   组织清单（脚本读）：id / version / modules / entries
├── AGENTS.md               #   包入口：这是什么 / 依赖全景 / 入口判定
└── CHANGELOG.md            #   版本变更日志

modules/<module-id>/        ← 模块：一个模块一个目录（纯 id，无 @）
├── MODULE.md               #   给 AI 助手的规范：适用范围、产物目录与运行过程
├── module.json             #   结构化声明（机器读）：身份、输入产出、依赖、产物落点
├── README.md               #   给人读：一句话定位 + 适用与边界
├── CHANGELOG.md            #   版本变更日志
└── assets/                 #   附件（模板 / 清单 / 脚本），按需携带，部分模块没有

build/                      ← 构建规则层
├── build.md                #   怎么造 / 改 spec 与模块的完整规则
├── build.json              #   构建规则层自己的版本身份
├── CHANGELOG.md
├── spec-template/          #   造新 spec 的母版
└── module-template/        #   造新模块的母版
```

## 怎么消费本仓

本仓是「货架」，日常干活不在本仓里进行，消费动作发生在**由
Project-Template 初始化的项目**中——模板出厂时，项目的 `spec/` 目录
已自带机制说明书 `AGENTS.md`、锁文件工具 `lockfile.py` 和字段规范
`lockfile.md`。分三种场景：

**1. 用现成工作流（拉取 spec 包）**，四步：

1. 读本仓 `registry.json` 选定 spec，它的 `manifest.json` 声明了需要
   哪些模块；
2. clone 本仓到临时目录；
3. 复制组合：`specs/<id>/` 整目录复制为项目的 `spec/<id>/`，再把它
   声明的各 `modules/<id>/` 复制为 `spec/<id>/@<id>/`；
4. 在项目里跑 `python spec/lockfile.py spec/<id>` 生成锁文件：spec
   登记来源与版本，每个模块登记来源、版本与内容指纹。

**2. 日常校验**：此后项目每次冷启动（新会话恢复上下文）跑一次
`python spec/lockfile.py spec/<id> --verify`。它只比对模块指纹：一致
就正常干活；模块被私自改动、目录缺失或未登记时报漂移、先停下，四条
出路选一——合法升级则重跑生成登记、项目特有补充挪进模块自带的
`add.md`（不参与指纹）、声明 `private` 转项目私有、`--fork <id>`
显式登记改造。spec 不参与指纹比对，改编排不会报漂移。

**3. 造 / 改 spec 或模块**：把本仓 `build/` 整目录拉到项目的
`spec/build/`，按 `build.md` 的规则和两个母版操作；造好的内容再回流
本仓，成为新的云端版本。

锁文件工具与字段规范随模板出厂、不放在本仓，因此本仓没有
`lockfile.py`；它只在由模板初始化的项目里运行。

## 版本

spec、模块、构建规则三套版本相互独立，各自写在 `manifest.json`、
`module.json`、`build.json` 的 `version` 字段里，遵循语义化版本
（SemVer）；每个目录都带自己的 `CHANGELOG.md`，跨版本迁移先读它。
`registry.json` 只做路径索引、不记版本，版本以各目录的 json 为准。
