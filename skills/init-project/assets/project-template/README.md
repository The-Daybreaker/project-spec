# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

> 模块：混合（【通用】= 模板约定；【项目专用】= 功能/使用说明，按项目填写）。
> 本项目由通用项目模板初始化。模板约定：根 `AGENTS.md` 为任何 agent 的接手入口；
> 开发规范与个人/机器信息在 `private/`（不进 GitHub，private 子 git 管理）。
> 使用模板规范前请先阅读 `AGENTS.md` 与 `docs/CONTRIBUTING.md`。

## 功能特性

（按项目实际填写）

## 快速开始

（按项目实际填写：安装、构建、运行、测试命令）

```bash
# 示例（Node）
npm install
npm run dev
npm test
```

## 项目结构

（按项目实际填写；模板默认骨架如下）

```text
.
├── AGENTS.md                # Agent 接手入口（公开）
├── src/                     # 代码区：全部业务源码/资源（子目录按技术栈自定，根目录不放业务代码）
├── docs/                    # 公开文档（DOCS.md / audit-checklist.md / UPGRADE.md / CONTRIBUTING.md / TESTING.md 等）
├── scripts/                 # 自动化脚本（bump_version / pre_release_check / ci_check / check_dev_docs / trash）
├── .github/workflows/       # CI 与自动发布
├── version.json             # 版本（version）与模板版本（template_version）单一事实来源
├── dist/                    # 发布产物（构建/打包输出，不进 git，Release 自动 attach）
├── archive/                 # 归档区（归档/退役时放归档说明与最终快照，进 git，只读）
└── private/                 # 私有区：个人/开发期文件（不进 GitHub）
    ├── PRIVATE.md           # 私有区说明与子 git 管理
    ├── AGENTS.md            # 开发入口与当前状态（唯一常青开发记忆）
    └── dev/
        ├── prd/             # 需求登记册（PRD-XXXX，开发前门禁）
        ├── rfc/             # 方案登记册（RFC-XXXX，评审后冻结）
        ├── adr/             # 决策登记册（ADR-XXXX，只增不改）
        ├── research/        # 调研登记册（RESEARCH-XXXX，红线 13 结果）
        ├── prototype/       # 页面原型/设计稿（界面/交互改动的可视化产物）
        └── DESIGN / CHANGELOG / TEST-REPORT / STATUS / 经验文档
```

## 开发与发布

- **Agent 协作**：见根 `AGENTS.md`（开发工作流、通用红线、发布流程）。
- **开发前规范**：M/L 需求先走开发前门禁——需求（PRD）、方案（RFC）、调研
  （RESEARCH）、架构决策（ADR）分别落 `private/dev/{prd,rfc,adr,research}/`
  （S 档可跳过；登记册状态机与模板见各 `INDEX.md`）；定稿方案吸收进
  `private/dev/DESIGN.md`。
- **可视化确认**：涉及界面/交互、架构/结构、流程/状态的改动，agent 会先出图
  （页面原型/架构图/流程图，Mermaid 或 SVG 单文件，路径见根 `AGENTS.md` 文档职责表）
  向用户展示、**获确认后才实施**。
- **阶段卡展示**：每次对话展示阶段卡（当前模块·子阶段/正在完成/已完成/下一步/
  状态 + 生命周期合规清单），以 `private/dev/STATUS.md`「📇 阶段卡」为准。
- **立项调研先行**：与 agent 讨论项目思路/需求/架构/功能/产品时，agent 会优先在
  GitHub 调研现成参考并提醒「先调研再立项」（见 `AGENTS.md` 红线 13）。
- **人类贡献**：见 `docs/CONTRIBUTING.md`。
- **版本管理**：`version.json` 的 `version` 字段 + git tag `vX.Y.Z`；版本递增由 agent 本地执行
  （`scripts/bump_version.py`），CI 对尚无 tag 的当前版本自动打 tag 并发布
  （`.github/workflows/release.yml`）。
- **阶段落盘**：任务中每完成一小阶段先更新 `private/dev/STATUS.md` 与受影响文档
  （红线 14），防止上下文压缩丢失进度。
- **模板升级**：项目根 `version.json` 的 `template_version` 记录模板版本；升级按 `docs/UPGRADE.md`
  只应用【通用】模块变更。
- **归档/退役**：项目停止主动开发时按根 `AGENTS.md`「项目归档/退役」执行
  （最终发布 + README 归档标记 + `archive/` 归档说明与快照 + 经验沉淀）。
- **私有区**：个人/开发期文件放 `private/`，主仓库 `.gitignore` 已忽略；
  private 子 git 内部管理，发布前自动同步（见 AGENTS.md「发布流程」）。

## 许可

{{LICENSE_NOTICE}}
