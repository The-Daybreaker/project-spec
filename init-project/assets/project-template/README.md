# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

> 本项目由通用项目模板初始化。模板约定：根 `AGENTS.md` 为任何 agent 的接手入口；
> 开发规范与个人/机器信息在 `private/`（不进 GitHub，private 子 git 管理）。
> 使用模板规范前请先阅读 `AGENTS.md` 与 `CONTRIBUTING.md`。

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
├── CONTRIBUTING.md          # 协作约定（公开）
├── docs/                    # 公开文档（含 audit-checklist.md）
├── scripts/                 # 自动化脚本（bump-version / pre-release-check / ci-check）
├── .github/workflows/       # CI 与自动发布
├── VERSION                  # 版本号（单一事实来源）
└── private/                 # 私有区：个人/开发期文件（不进 GitHub）
    ├── AGENTS.md            # 开发入口与当前状态（唯一常青开发记忆）
    └── dev/                 # DESIGN / CHANGELOG / TEST-REPORT
```

## 开发与发布

- **Agent 协作**：见根 `AGENTS.md`（开发工作流、通用红线、发布流程）。
- **立项调研先行**：与 agent 讨论项目思路/需求/架构/功能/产品时，agent 会优先在
  GitHub 调研现成参考并提醒「先调研再立项」（见 `AGENTS.md` 红线 13）。
- **人类贡献**：见 `CONTRIBUTING.md`。
- **版本管理**：`VERSION` 文件 + git tag `vX.Y.Z`；CI 自动递增并发布
  （`.github/workflows/release.yml`）。
- **私有区**：个人/开发期文件放 `private/`，主仓库 `.gitignore` 已忽略；
  private 子 git 内部管理，发布前自动同步（见 AGENTS.md「发布流程」）。

## 许可

{{LICENSE_NOTICE}}
