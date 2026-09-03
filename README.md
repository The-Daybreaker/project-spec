# Project-Template（通用项目模板）

一套**开箱即用、人和 AI 都能看懂的通用项目模板**。它把「AI 助手 + 人协作」
开发的骨架与规范固化下来：你说一句话，AI 助手就能按模板初始化一个新项目；
之后整个项目任何 agent 都能从零接手——冷启动读一遍 `AGENTS.md` 就恢复全貌，
不依赖某个特定的 AI 工具，也不依赖之前的对话记录。

核心理念是「结构是地基，工作流是 spec」：七件套骨架保证任何项目最低限度
可运转；文档种类、流程编排、仪式轻重全部由 spec 包声明——spec 是模子，
context 是模子出的件。

仓库附带两个 AI 助手技能（skill）：

- **init-project**：一键把任意空文件夹初始化成符合模板规范的新项目（复制
  骨架、替换占位符、建 git）；
- **agent-rules**：AI 助手的通用行为底线（仅在对话不属于任何项目、且不是
  纯聊天时生效）。

## 它能帮你做什么

- **开新项目不再从零开始**：模板自带协作总纲、任务板、人机交流三件套和
  历史归档，AI 助手一条指令就能搭好骨架并完成首次提交。
- **任何 AI 助手接手都能读懂项目**：项目根目录的 `AGENTS.md` 写清了冷启动
  链路；agent 的上下文是易失内存，任务板与三件套就是磁盘上的状态——会话
  中断、换新对话都不丢状态。
- **要文档有文档，不要也不背包袱**：需要文档体系 / 工作流时，从云端模块库
  拉取 spec 包（`github.com/The-Daybreaker/project-spec`，如 software-dev：
  愿景 / 设计 / 需求 / 决策 / 开发 / 测试 / 审计 / 发布 8 模块）；没有 spec，
  项目以地基形态轻装运转。
- **该确认的确认、该自动的自动**：不可逆操作（发布、永久删除、写交付物）
  agent 会先找你确认；`.gitignore` 预置常见密钥文件名模式，宁可误伤不
  可漏收。
- **一套规范装给所有助手**：两个技能可以复制到多个 AI 助手的用户级技能
  目录，让所有助手遵循同一套规则。

## 快速开始

### 方式一：安装技能使用（推荐）

把 `init-project/` 整个目录复制到 AI 助手的用户级技能目录（例如 Codex 是
`~/.codex/skills/`，其他助手见其文档），建议连同 `agent-rules/` 一起装，
之后对助手说：

> 「用 init-project 技能把 <目标目录> 初始化为一个新项目」

它会按清单执行：确认参数与方案 → 复制模板骨架 → 替换项目名占位符 →
初始化 git 并完成首次提交 → 回读校验。初始化会
创建 git 仓库、批量落盘，属于高风险操作，所以它会先和你确认再动手。

`agent-rules/` 是 AI 助手的通用行为规范（精简版），建议也装到每个助手：
它**只在对话不属于任何项目、且不是纯聊天时**加载；一旦进入某个项目，
就以那个项目自己的 `AGENTS.md` 为准。

### 方式二：手动应用模板

不想用技能也可以手动来：

```bash
# 一条命令：复制模板 + 替换占位符 + 建 git + 首次提交
python init-project/scripts/init_project.py <目标目录> --name my-app

# 只复制文件，不建 git
python init-project/scripts/init_project.py <目标目录> --name my-app --no-git
```

也可以直接把 `init-project/assets/project-template/` 下的七件套复制到新项目
目录（不含 `_trash/`、`.git/`），首次对话让 agent 冷启动。

### 初始化之后

1. 首次对话让 agent 冷启动（它会读 `AGENTS.md` 恢复上下文），对齐项目
   背景与目标；
2. 需要文档体系 / 工作流时，从云端模块库拉取 spec 包或自建
   （`github.com/The-Daybreaker/project-spec`，构建规则同在云端）；没有 spec，
   项目照常运转；
3. 确认后配置远端仓库并推送（agent 不擅自推送）。

## 目录结构（简要）

```text
Project-Template/
├── README.md                     # 本文件
├── CHANGELOG.md                  # 发布版本变更记录
├── init-project/                 # 项目初始化技能
│   ├── SKILL.md
│   ├── scripts/init_project.py
│   └── assets/project-template/  # 模板本体（唯一一份）
│       ├── AGENTS.md             #   AI 助手接手入口（协作总纲 + 宪章 6 条）
│       ├── README.md             #   使用手册（含给用户的 13 条协作规范）
│       ├── package.json          #   模板版本
│       ├── CHANGELOG.md          #   模板变更记录
│       ├── context/              #   项目上下文（种类由 spec 决定，零固有件）
│       ├── process/              #   任务板 + inbox / pending / reviews 三件套
│       ├── workspace/            #   source（源产物）+ delivery（交付物）
│       ├── logs/                 #   历史归档
│       └── spec/                 #   声明式规范（AGENTS.md 机制说明书 + lockfile 工具；spec 包按需拉取）
└── agent-rules/                  # AI 助手通用行为规范技能
    └── SKILL.md
```

## 版本与升级

- 本仓库发布版本 **v0.9.0**，与模板本体一致——版本号单一事实源是
  `init-project/assets/project-template/package.json`。
- 变更记录：本仓库见 `CHANGELOG.md`；模板本体见
  `init-project/assets/project-template/CHANGELOG.md`。
- 老项目注意：模板整体重设计，旧版项目无法原地升级；老项目继续按旧版运转
  即可，新项目用本版。

## 给维护者的几条约定

- **模板唯一落点**：模板本体只在 `init-project/assets/project-template/`
  存一份——改模板就是改这份，不另建镜像、不建同步机制。
- **发布前安全扫描**：推送前自行做密钥与个人信息检查（方法自选），
  高危凭据零命中、个人信息零残留再发版。
