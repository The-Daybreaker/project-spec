# 通用项目模板（Universal Project Template）

一套**开箱即用、人和 AI 都能看懂的通用项目管理模板**。它把「AI 助手 + 人协作」
开发过程中的规范、流程、检查和版本管理都固化下来：你说一句话，AI 助手就能按
模板初始化一个新项目，之后整个项目从需求到发布都按清晰步骤推进。

项目里附带两个 AI 助手技能（skill）：

- **init-project**：一键把任意文件夹初始化成符合模板规范的新项目；
- **agent-rules**：AI 助手的通用行为底线（在对话不属于任何项目、且不是纯聊天时
  生效）。

## 它能帮你做什么

- **开新项目不再从零开始**：模板自带规范文档、目录结构、检查脚本和 git 初始化，
  AI 助手一条指令就能搭好骨架并完成首次提交。
- **任何 AI 助手接手都能读懂项目**：项目根目录的 `AGENTS.md` 写清楚了该怎么做，
  不依赖某个特定的 AI 工具或之前的对话记录。
- **该确认的确认、该自动的自动**：重要决策由你拍板，重复性检查交给脚本
  （文档一致性、版本一致性、发布前检查等）。
- **公开与私有分开**：适合发布到 GitHub 的内容放主仓库；个人偏好、机器专属信息、
  开发过程文档放 `private/`，单独管理、不进 GitHub。
- **一套规范装给所有助手**：两个技能可以复制到多个 AI 助手的用户级技能目录，
  让所有助手遵循同一套规则。

## 快速开始

### 方式一：安装技能使用（推荐）

把 `skills/init-project/` 整个目录复制到 AI 助手的用户级技能目录（例如 Codex 是
`~/.codex/skills/`，其他助手的目录见其文档），重启或刷新后，对助手说：

> 「用 init-project 技能把 <目标目录> 初始化为一个新项目」

它会按清单执行：复制模板 → 替换项目名、描述等占位符 → 初始化主 git 和
private 子 git 并完成首次提交 → 回读校验。初始化会创建文件，属于高风险操作，
所以它会先和你确认参数与方案再动手。

`skills/agent-rules/` 是 AI 助手的通用行为规范（精简版），建议也装到每个助手：
它**只在对话不属于任何项目、且不是纯聊天时**加载；一旦进入某个项目，就以那个
项目自己的 `AGENTS.md` 为准。

### 方式二：手动应用模板

不想用技能也可以手动复制模板：

```bash
# 复制模板并替换占位符（不建 git）
python skills/init-project/scripts/init_project.py <目标目录> --name my-app --desc "..." --no-git

# 初始化主 git
git -C <目标目录> init -b main
git -C <目标目录> add -A -- . && git -C <目标目录> commit -m "chore: init"

# 初始化 private 子 git（放私有内容）
git -C <目标目录>/private init
git -C <目标目录>/private add -A -- . && git -C <目标目录>/private commit -m "docs: private v0.0.1.patch0 - init"
```

### 初始化之后

1. 读新项目的 `AGENTS.md`（这是 AI 助手的接手入口）；
2. 按你的环境补充 `private/AGENTS.md`（本机环境、你的偏好）；
3. 按技术栈实现 `scripts/ci_check.py` 和 CI 配置；
4. 确认后配置远端仓库并推送（首次推送不会自动发版）。

## 目录结构（简要）

```text
通用项目模板/
├── AGENTS.md                 # 工作区规范入口（AI 助手先读这里）
├── README.md                 # 本文件
├── version.json              # 版本号单一事实来源
├── install-targets.json      # 两个技能的安装位置表
├── scripts/                  # 维护脚本（同步、副本校验、冒烟自检）
├── project-template/         # 通用项目模板本体（权威副本）
│   ├── AGENTS.md             #   AI 助手接手入口（公开版）
│   ├── docs/ scripts/ .github/ dist/ archive/
│   └── private/              #   私有区（不进 GitHub，单独管理）
└── skills/
    ├── init-project/         # 项目初始化技能（SKILL.md + 脚本 + 模板副本）
    └── agent-rules/          # AI 助手通用行为规范技能
```

## 版本与升级

- 版本号格式 `X.Y.Z.patchN`（例如 `1.4.2.patch0`），以 `version.json` 为准，
  并打 git tag `vX.Y.Z.patchN`。
- 本项目当前版本：**v1.6.0.patch0**。
- 模板每次发版的变更记录在 `private/dev/CHANGELOG.md`；初始化出的项目需要升级模板时，
  按项目内 `docs/UPGRADE.md` 的说明操作（只应用【通用】部分，不动你的项目内容）。

## 给维护者的几条约定

- **改模板必同步**：修改 `project-template/` 后运行
  `python scripts/sync_template.py`，把改动同步到
  `skills/init-project/assets/project-template/`（两份必须一致）；模板【通用】规则
  有变时还要同步 `skills/agent-rules/`。
- **private 骨架强制跟踪**：模板自己的 `.gitignore` 忽略 `private/`，提交骨架用
  `git add -f project-template/private skills/init-project/assets/project-template/private`。
- **技能校验**：改完技能用 skill-creator 的 quick_validate 校验
  （`PYTHONUTF8=1 python <skill-creator>/scripts/quick_validate.py skills/init-project`，
  agent-rules 同理）。
- **发版同步**：版本递增时同步更新 `version.json`、`private/dev/CHANGELOG.md`、两个
  SKILL.md 的 `metadata.version`、agent-rules 继承矩阵，并全局 grep 新旧版本号
  确认无残留。
- **发布前冒烟自检**：`python scripts/smoke_init.py` 必须全绿。
- **发版前安全扫描**：发布前运行 `python scripts/scan_secrets.py --check`
  （建议加 `--history` 复核全部 git 历史）——高危凭据零命中、个人信息零残留再发版。
- **删除纪律**：删除先移入 `_trash/<AI助手产品名>_<日期>_<时分>/`，任务结束时用
  `python project-template/scripts/trash.py` 整体进回收站。
