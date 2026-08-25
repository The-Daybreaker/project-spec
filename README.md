# 通用项目模板（Universal Project Template）

一套**自洽自足的通用项目管理模板** + 基于它的 **init-project skill**（agent 可一键
初始化任意项目文件夹）。模板吸收了 PinNotes 与 KnowOps 两个项目的实战经验，面向
「Agent + 人协作」的长期迭代开发。

## 目录结构

```text
通用项目模板/
├── AGENTS.md                 # 本项目（工作区）专属规范入口
├── README.md                 # 本文件
├── version.json              # 版本（version）与模板版本（template_version）单一事实来源
├── .gitignore                # 工作区忽略规则
├── .gitattributes            # 工作区行尾归一化（LF，与模板一致）
├── docs/                     # 工作区自身文档
│   ├── CHANGELOG.md          # 模板版本变更历史（升级比对依据）
│   ├── WORKLOG.md            # 工作区阶段落盘日志
│   └── EXPERIENCE-TO-KB.md   # 可沉淀进知识库的经验（不混入模板内部）
├── scripts/
│   └── sync_template.py      # 同步脚本：project-template/ → init-project/assets/
├── project-template/         # 通用项目模板（权威副本，人类可读）
│   ├── AGENTS.md             #   Agent 接手入口（公开版，随仓库发布）
│   ├── README.md / LICENSE / version.json / .gitignore / .gitattributes / .editorconfig
│   ├── docs/                 #   公开文档（DOCS.md / audit-checklist.md / UPGRADE.md / CONTRIBUTING.md）
│   ├── scripts/              #   自动化脚本 + version-sync.json
│   ├── .github/workflows/    #   CI 检查 + 自动版本递增发布
│   └── private/              #   私有区（不进 GitHub，内部子 git 管理）
│       ├── PRIVATE.md        #     私有区说明与子 git 管理
│       ├── AGENTS.md         #     开发指引（唯一常青开发记忆）
│       └── dev/              #     DESIGN / CHANGELOG / TEST-REPORT / WORKLOG / 经验文档
└── init-project/             # skill：根据模板初始化指定项目文件夹
    ├── SKILL.md
    ├── references/init-steps.md     # 初始化执行细节
    ├── scripts/init_project.py      # 复制 + 占位符替换 + git 初始化
    └── assets/project-template/     # 模板副本（skill 分发用，与 project-template/ 同步）
```

另含 `agent-rules/`（见「使用方法 3」）：

```text
agent-rules/                     # skill：Agent 通用行为规范（精简版，全局基线）
├── SKILL.md                     # 规范正文（自包含）+ 触发规则（仅非项目且非纯聊天加载）
├── references/
│   ├── inheritance-map.md       # 继承矩阵：模板红线 ↔ 精简条目 + 正文指纹（防漂移）
│   └── audit-checklist-lite.md  # 精简审计清单（自审/独立审计共用）
└── agents/openai.yaml           # agent 平台接口描述
```

## 模板设计要点

1. **AGENTS.md 拆分**：根目录 `AGENTS.md`（公开，可发布到 GitHub，不写进
   .gitignore）承载任何 agent 从零接手的入口；`private/AGENTS.md`（私有）承载开发
   规范、本机环境、用户决策——**冲突时私有版优先**。
2. **private 子 git**：`private/` 整体写入主仓库 `.gitignore`，内部由独立 git 管理
   （本地、无远端）。**每次发布前**，agent 用 `git -C private status --short` 检查
   变动，有更新自动提交（`scripts/pre_release_check.py` 一键完成），再进入主仓库
   发布。
3. **三区文件归属**：A 公开（主仓库）/ B 私有（private 子 git）/ C 不管理
   （生成物、缓存）。新增文件必须先判区再落盘。
4. **Agent 开发红线**（写入模板，任何 agent 接手即生效）：
   - 实施之前必须对齐需求和计划，**得到确认之后再实施**；
   - 实施之后**自动审计**，推荐委托独立子 agent（只看 diff + 审计清单）复审；
   - 变更分级、删除纪律、回读校验、相似检查、密钥安全、文档同步、**阶段落盘**、
     **上下文恢复重读**等 15 条（含**立项调研先行**：讨论项目思路/需求/架构/
     功能/产品时优先在 GitHub 调研现成参考，并提醒用户「先调研再立项」）。
5. **开发工作流**：需求提出 → 讨论对齐（复述需求；**立项类话题先 GitHub 调研并
   提醒「先调研再立项」**）→ 确认开工 → 实施（改动完成即文档就绪；**每完成一小
   阶段先落盘更新 WORKLOG，红线 14**）→ 自动审计 → 验证（ci_check + TEST-REPORT）
   → 展示与提交（先 private 子 git）→ 发布（版本递增 + tag + Release）→
   **经验沉淀**（每轮对话后把完整候选经验写入 EXPERIENCE-TO-TEMPLATE /
   EXPERIENCE-TO-KB，并提醒用户真正沉淀）→ 汇报（附完成检查清单）。
6. **版本管理与 CI/CD**：版本号**从 `0.0.1` 开始**，每次默认末位 +1，**前两位
   （major/minor）增加必须向用户确认**；`version.json` 单一事实来源 + git tag `vX.Y.Z`；
   版本递增由 agent 本地完成（`bump_version.py` 按 `scripts/version-sync.json` 同步
   `package.json` / `Cargo.toml` / `pyproject.toml` 等与 CHANGELOG），推送 main 后
   `.github/workflows/release.yml` 对尚无 tag 的当前版本自动打 tag 并建 Release
   （不会二次递增，手动/自动发布二选一）；
   `.github/workflows/ci.yml` 提供 CI 检查入口。发布策略默认**不自动发布**
   （用户确认后执行发布流程；初始化时可用 `--auto-release` 开启自动发布）。
7. **不依赖任何 agent 与上下文**：AGENTS.md 自带 bootstrap（任何新对话从零接手）；
   脚本自洽（仅依赖 Python 标准库，Python 3.9+ 跨平台运行，UTF-8）；
   `private/AGENTS.md` 是唯一常青开发记忆。
8. **适配各种类型项目**：技术栈无关的骨架；CI 与检查命令留出明确适配点（见模板内
   注释与 README）。
9. **文档双模块 + 治理**：每份文档标注【通用】/【项目专用】；通用模块改动可沉淀回
   模板，项目专用模块不受模板更新覆盖；**正文 = 当前有效状态**（决策修改直接覆盖、
   禁止 AI 在正文追加历史、留痕只在 CHANGELOG 一行；详见模板
   `project-template/docs/DOCS.md`「文档治理」）。
10. **模板升级机制**：项目根 `version.json` 的 `template_version` 记录模板版本；
    模板 `CHANGELOG.md` 记录版本变更历史；升级按 `docs/UPGRADE.md` 只应用
    【通用】模块。
11. **删除纪律**：对话内删除先移入 `_trash/<agent产品名>_<日期>_<时分>/`（如
    `codex_2026-08-25_2330`；不设固定 agent 列表），任务结束时用 `scripts/trash.py`
    整体进回收站（避免小文件堆积）。
12. **发布产物与归档**：构建/打包产物统一输出 `dist/`（C 区、不进 git、Release
    自动 attach）；项目停止主动开发时有「项目归档/退役」流程（最终发布 + README
    归档标记 + 产物归档 + 经验沉淀，agent 不擅自删除）。

## 使用方法

### 1. 安装 skill（把 init-project 放入 agent 的 skill 目录）

将 `init-project/` 整个目录复制到 agent 的用户级 skill 目录（如 DeepSeek Harness：
`$DSH_HOME/skills` 或 `C:\Users\<你>\.dsh\skills\`；其他 agent 见其文档），
重启/刷新后即可用：

> 「用 init-project skill 把 <目标目录> 初始化为一个新项目」

skill 会：复制模板 → 替换占位符（项目名/描述/分支/作者）→ 初始化主 git 与
private 子 git 并完成首次提交 → 按清单回读校验。初始化是高风险操作，skill 强制
先与用户对齐参数与方案。

### 2. 手动应用模板（不用 skill）

```bash
# 复制模板并替换占位符（{{PROJECT_NAME}} {{PROJECT_DESCRIPTION}} {{DEFAULT_BRANCH}}
# {{AUTHOR}} {{YEAR}} {{DATE}} {{VERSION}} {{LICENSE_NOTICE}}）
# 推荐：用 init_project.py 只复制+替换、不建 git
python init-project/scripts/init_project.py <目标目录> --name my-app --desc "..." --no-git
# 初始化两个 git 仓库
git -C <目标目录> init -b main
git -C <目标目录> add -A -- . && git -C <目标目录> commit -m "chore: init"
git -C <目标目录>/private init
git -C <目标目录>/private add -A -- . && git -C <目标目录>/private commit -m "docs: private v0.0.1 - init"
```

### 3. 初始化后的下一步（模板内已写明）

读新项目的 `AGENTS.md` → 补 `private/AGENTS.md` 的「本机环境」与「用户决策」→
按技术栈实现 `scripts/ci_check.py` 与 `.github/workflows/ci.yml` → 用户确认后配置
远端并推送（首个 push 不自动发 Release）。

### 4. 安装 agent-rules 与 init-project 到各 agent

`agent-rules/` 是从通用模板【通用】部分派生的**精简版 agent 全局行为规范**：
**仅当对话不在任何项目/工作区内**（无项目 `AGENTS.md`、不属于已打开的工作区）
**且非纯聊天**（编码、文档、分析、调研、规划、文件操作、事实性问答等）时加载；
**项目内对话以项目自身 `AGENTS.md` 为准，不加载本 skill**。除项目专属的需求/规定
外，模板要求一律继承（继承矩阵 + sync 自动化校验保证随模板版本同步，不漂移）。
`init-project/` 是**项目初始化 skill**（用模板初始化新项目文件夹），同样建议装到
每个 agent。

安装：把 `agent-rules/` 整个目录复制到各 agent 的用户级 skill 目录（重启/刷新后
生效）。本机已安装位置（两个 skill 都装在下列目录下）：

| Agent | skill 目录 |
|---|---|
| Codex | `<用户主目录>\.codex\skills`（agent-rules / init-project） |
| DSH | `<用户主目录>\.dsh\skills`（agent-rules / init-project） |
| WorkBuddy | `<用户主目录>\.workbuddy\skills`（agent-rules / init-project） |
| TraeWork（TRAE Work CN） | `<用户主目录>\.trae-cn\skills`（agent-rules / init-project） |
| QoderWork（QoderWork CN） | `<用户主目录>\.qoderworkcn\skills`（agent-rules / init-project） |

其他机器/agent：找到对应用户级 skill 目录（如 `~/.codex/skills`、`~/.dsh/skills`、
`~/.workbuddy/skills`、`~/.trae-cn/skills`、`~/.qoderworkcn/skills`），把
`agent-rules/` 与 `init-project/` 复制进去即可。

## 维护约定

- **改模板必同步**：修改 `project-template/` 后运行
  `python scripts/sync_template.py`，把改动镜像到
  `init-project/assets/project-template/`（skill 分发的是副本，两份必须一致）；
  模板【通用】变更还需同步 `agent-rules/`（精简版全局规范正文或继承矩阵指纹复核），
  sync 会一并校验（版本一致性 + 矩阵覆盖 + 红线正文指纹）。
- **private/ 骨架的跟踪**：模板自身的 `.gitignore` 会忽略 `private/`（这正是设计
  目标——目标项目中的 private/ 永不进主仓库），因此本工作区仓库需要用
  `git add -f project-template/private init-project/assets/project-template/private`
  强制跟踪这些骨架文件；改动它们后提交时同样用 `-f`。
- **skill 校验**：改完 skill 用 skill-creator 的 quick_validate 校验：
  `python <skill-creator>/scripts/quick_validate.py init-project`
  （中文 Windows 默认 GBK 编码下若报 UnicodeDecodeError，先设置 `PYTHONUTF8=1`）。
- **发版同步**：版本递增时同步更新根 `version.json`、`project-template/version.json`
  （`version` 与 `template_version` 两字段）、`docs/CHANGELOG.md`、
  `SKILL.md metadata.version`、`agent-rules/SKILL.md metadata.version` 与
  `agent-rules/references/inheritance-map.md` 版本对照，并**全局 grep 新旧版本号**
  （如 `1.1.0` / `1.1.1`）核对所有文档内嵌版本字样（`SKILL.md` 仅
  `metadata.version`；`references/init-steps.md` 已改为引用 `version.json`；模板
  内部文件一律用占位符、不写死版本），确认无残留后再走模板发布流程。
  `scripts/sync_template.py` 会自动校验各 `SKILL.md metadata.version`、
  `agent-rules` 继承矩阵版本/覆盖/指纹与 `project-template/version.json` 的
  `template_version` 一致（改模板/发版后运行 sync 即校验）。
- **版本**：本模板工作区自身用 git 管理并按同样规则打 tag（当前 v1.1.1；
  版本号见 `version.json`）。

## 经验来源

- [PinNotes](<项目路径>)：CI/CD 自动版本递增发布、
  CLAUDE.md 作为 agent 入口、提交信息与分支约定。
- [KnowOps](<项目路径>)：AGENTS.md 公开/私有拆分、
  private 子 git、三区文件归属、开发工作流（先对齐后实施、实施后审计、验证后发布）、
  完成检查清单、文档职责划分、唯一常青开发记忆。
