# 通用项目模板（Universal Project Template）

一套**自洽自足的通用项目管理模板** + 基于它的 **init-project skill**（agent 可一键
初始化任意项目文件夹）。模板吸收了 PinNotes 与 KnowOps 两个项目的实战经验，面向
「Agent + 人协作」的长期迭代开发。

## 目录结构

```text
通用项目模板/
├── README.md                 # 本文件
├── sync-template.ps1         # 同步脚本：project-template/ → init-project/assets/
├── project-template/         # 通用项目模板（权威副本，人类可读）
│   ├── AGENTS.md             #   Agent 接手入口（公开版，随仓库发布）
│   ├── README.md / LICENSE / CONTRIBUTING.md / VERSION / .gitignore
│   ├── docs/                 #   公开文档（含 audit-checklist.md 审计清单）
│   ├── scripts/              #   自动化脚本（bump-version / pre-release-check / ci-check）
│   ├── .github/workflows/    #   CI 检查 + 自动版本递增发布
│   └── private/              #   私有区（不进 GitHub，内部子 git 管理）
│       ├── AGENTS.md         #     开发指引（唯一常青开发记忆）
│       └── dev/              #     DESIGN / CHANGELOG / TEST-REPORT
└── init-project/             # skill：根据模板初始化指定项目文件夹
    ├── SKILL.md
    ├── references/init-steps.md     # 初始化执行细节
    ├── scripts/init_project.py      # 复制 + 占位符替换 + git 初始化
    └── assets/project-template/     # 模板副本（skill 分发用，与 project-template/ 同步）
```

## 模板设计要点

1. **AGENTS.md 拆分**：根目录 `AGENTS.md`（公开，可发布到 GitHub，不写进
   .gitignore）承载任何 agent 从零接手的入口；`private/AGENTS.md`（私有）承载开发
   规范、本机环境、用户决策——**冲突时私有版优先**。
2. **private 子 git**：`private/` 整体写入主仓库 `.gitignore`，内部由独立 git 管理
   （本地、无远端）。**每次发布前**，agent 用 `git -C private status --short` 检查
   变动，有更新自动提交（`scripts/pre-release-check.ps1` 一键完成），再进入主仓库
   发布。
3. **三区文件归属**：A 公开（主仓库）/ B 私有（private 子 git）/ C 不管理
   （生成物、缓存）。新增文件必须先判区再落盘。
4. **Agent 开发红线**（写入模板，任何 agent 接手即生效）：
   - 实施之前必须对齐需求和计划，**得到确认之后再实施**；
   - 实施之后**自动审计**，推荐委托独立子 agent（只看 diff + 审计清单）复审；
   - 变更分级、删除纪律、回读校验、相似检查、密钥安全、文档同步等 13 条
     （含**立项调研先行**：讨论项目思路/需求/架构/功能/产品时优先在 GitHub
     调研现成参考，并提醒用户「先调研再立项」）。
5. **开发工作流**：需求提出 → 讨论对齐（复述需求；**立项类话题先 GitHub 调研并
   提醒「先调研再立项」**）→ 确认开工 → 实施（改动完成即
   文档就绪）→ 自动审计 → 验证（ci-check + TEST-REPORT）→ 展示与提交（先 private
   子 git）→ 发布（版本递增 + tag + Release）→ **经验沉淀提醒**（架构变化/每次更新
   后，提醒用户沉淀经验进知识库、可复用经验集成进项目模板）→ 汇报（附完成检查清单）。
6. **版本管理与 CI/CD**：版本号**从 `0.0.1` 开始**，每次默认末位 +1，**前两位
   （major/minor）增加必须向用户确认**；`VERSION` 单一事实来源 + git tag `vX.Y.Z`；
   版本递增由 agent 本地完成（`bump-version.ps1` 同步 `package.json` / `Cargo.toml`
   与 CHANGELOG），推送 main 后 `.github/workflows/release.yml` 对尚无 tag 的当前
   版本自动打 tag 并建 Release（不会二次递增，手动/自动发布二选一）；
   `.github/workflows/ci.yml` 提供 CI 检查入口。
7. **不依赖任何 agent 与上下文**：AGENTS.md 自带 bootstrap（任何新对话从零接手）；
   脚本自洽（ASCII-only，Windows PowerShell 5.1 / 7 均可运行）；`private/AGENTS.md`
   是唯一常青开发记忆。
8. **适配各种类型项目**：技术栈无关的骨架；CI 与检查命令留出明确适配点（见模板内
   注释与 README）。

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

```powershell
# 复制模板
Copy-Item -Recurse project-template <目标目录>
# 替换占位符（{{PROJECT_NAME}} {{PROJECT_DESCRIPTION}} {{DEFAULT_BRANCH}}
# {{AUTHOR}} {{YEAR}} {{DATE}} {{VERSION}} {{LICENSE_NOTICE}}）
# 初始化两个 git 仓库
git -C <目标目录> init -b main
git -C <目标目录> add -A -- . && git -C <目标目录> commit -m "chore: init"
git -C <目标目录>\private init
git -C <目标目录>\private add -A -- . && git -C <目标目录>\private commit -m "docs: private v0.0.1 - init"
```

### 3. 初始化后的下一步（模板内已写明）

读新项目的 `AGENTS.md` → 补 `private/AGENTS.md` 的「本机环境」与「用户决策」→
按技术栈实现 `scripts/ci-check.ps1` 与 `.github/workflows/ci.yml` → 用户确认后配置
远端并推送（首个 push 不自动发 Release）。

## 维护约定

- **改模板必同步**：修改 `project-template/` 后运行
  `powershell -File sync-template.ps1`，把改动镜像到
  `init-project/assets/project-template/`（skill 分发的是副本，两份必须一致）。
- **private/ 骨架的跟踪**：模板自身的 `.gitignore` 会忽略 `private/`（这正是设计
  目标——目标项目中的 private/ 永不进主仓库），因此本工作区仓库需要用
  `git add -f project-template/private init-project/assets/project-template/private`
  强制跟踪这些骨架文件；改动它们后提交时同样用 `-f`。
- **skill 校验**：改完 skill 用 skill-creator 的 quick_validate 校验：
  `python <skill-creator>/scripts/quick_validate.py init-project`。
- **版本**：本模板工作区自身用 git 管理并按同样规则打 tag（当前 v1.0.2；
  版本号见 `VERSION` 文件）。

## 经验来源

- [PinNotes](<项目路径>)：CI/CD 自动版本递增发布、
  CLAUDE.md 作为 agent 入口、提交信息与分支约定。
- [KnowOps](<项目路径>)：AGENTS.md 公开/私有拆分、
  private 子 git、三区文件归属、开发工作流（先对齐后实施、实施后审计、验证后发布）、
  完成检查清单、文档职责划分、唯一常青开发记忆。
