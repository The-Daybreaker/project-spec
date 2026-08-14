# AGENTS.md — {{PROJECT_NAME}}

> 本文件随仓库发布到 GitHub（公开），是**任何 agent 从零接手本项目的入口**：自洽自足，
> 不依赖任何特定 agent、工具或对话上下文。
> 本文件只承载可公开的内容；项目开发与维护的完整规范、个人/机器专属信息位于
> `private/AGENTS.md`（由 private 子 git 管理，不进 GitHub，仅本机开发 agent 读取）。
> 两份文件冲突时：`private/AGENTS.md` 中的开发/机器/个人专属细节以它为准。

## 项目概览

- **定位**：{{PROJECT_DESCRIPTION}}
- **技术栈与目录**（按项目实际补充）：
  - `src/` — 主要代码
  - `docs/` — 公开文档
  - `scripts/` — 自动化脚本（版本、发布前检查、CI 检查）
  - `private/` — 私有区（个人/开发期文件，**不进 GitHub**，见「仓库布局」）
  - `.github/workflows/` — CI / 自动发布
- **版本**：以 `VERSION` 文件与 git tag `vX.Y.Z` 为准；完整历史见
  `private/dev/CHANGELOG.md`（私有，不发布）。
- **当前状态**：见 `private/AGENTS.md`「项目状态与版本」（开发期状态只记在私有指引）。

## 仓库布局与文件分类归属（三区，强制）

| 区 | 位置 | 内容 | 版本管理 |
|---|---|---|---|
| A. 公开 | 仓库根、`src/`、`docs/`、`scripts/`、`.github/` | 用户可见、可发布、无敏感信息 | 主仓库 git，发布到 GitHub |
| B. 私有 | `private/` | 个人/机器专属信息、开发期文档（DESIGN/CHANGELOG/TEST-REPORT）、测试素材 | private 子 git（本地、无远端） |
| C. 不管理 | 各处 | `node_modules/`、`dist/`、`build/`、日志、缓存、临时文件 | 无（.gitignore 忽略） |

**归属判定规则**（新增文件必须先判区再落盘）：

1. 含**个人/机器专属信息**或**发布前不公开**内容 → B（`private/`）；
2. **生成物/缓存/可重建**内容 → C（不版本管理）；
3. 用户可见、可发布、无敏感信息 → A（主仓库）；
4. **密钥/凭据绝不入库**：`.env`、`*.key`、`*_secret*` 等一律进 `.gitignore`；
   确需保留的密钥只放 `private/`（且不提交 private 子 git，或加密后提交）。

**发布前检查**：主仓库 `git status` 只应出现 A 区文件；`git -C private status`
负责 B 区；C 区内容两者都不得出现。发布前必须先同步 private 子 git（见「发布流程」）。

## Agent 快速上手（每次新对话、任何 agent 都按此 bootstrap）

1. 读本文件；再读 `private/AGENTS.md`（若存在）——它是**开发入口与当前状态**
   （唯一常青开发记忆），含版本、本机环境、用户决策。
2. 查看两个仓库状态：`git status`（主仓库）、`git -C private status`（私有子 git）。
3. 读 `VERSION` 与 `private/dev/CHANGELOG.md` 顶部，确认当前版本与最近变更。
4. 读 `private/dev/DESIGN.md`（设计）与 `private/dev/TEST-REPORT.md`（测试记录）。
5. 任何实施开始前，必须先走「开发工作流」第 1–3 步：**对齐需求与计划、获用户确认**。

## 开发工作流（强制，每次需求都走完）

> 本工作流是「Agent + 人协作」的核心：**先对齐、后实施、实施后自动审计、验证后发布**。

1. **需求提出**：用户提出需求（功能 / 文档 / 重构 / 修复 / 发布）。
2. **讨论对齐**：与用户讨论，理解意图与影响面；**复述需求**并列出方案要点
   （改哪些文件、是否破坏性、是否影响文档与用户视角）。
3. **确认开工**：用户明确确认后开始实施。**红线：未获确认不实施**（低风险微调例外，
   见「通用红线」第 2 条变更分级）。
4. **实施**：按 AGENTS.md、DESIGN.md 与项目规范修改；**同步更新受影响文档**
   （CHANGELOG / DESIGN / README / TEST-REPORT / 根 AGENTS.md / private/AGENTS.md /
   用户可见文档），做到「改动完成即文档就绪」，不等发布前补救。
5. **自动审计（实施后必做）**：见「自动审计」一节。修复全部发现后再继续。
6. **验证**：运行项目检查与测试（`scripts/ci-check.ps1` 或项目定义的命令），
   结果记录到 `private/dev/TEST-REPORT.md`；未通过不发布。
7. **展示与提交**：向用户展示成果 → **提交 private 子 git**（若 `private/` 有变动）
   → 主仓库 commit → push。
8. **发布**：按「发布流程」自动执行（版本递增、tag、Release、分发/部署）。
9. **经验沉淀（每次更新后必做提醒）**：每次**项目架构发生改变**（无论是否发布）
   以及**项目每次更新（发布）之后**，提醒用户沉淀经验：
   - 将经验/教训/决策沉淀进**个人知识库**（如 Obsidian 知识库 / KnowOps 等，
     按用户习惯）；
   - 将**可复用的经验**（新流程、新规范、工具用法、踩坑记录）**集成进通用项目
     模板**（如有适用，下次初始化新项目即可受益）；
   - 沉淀与否、沉淀到哪里由用户决定；agent 只负责提醒与协助。
10. **汇报**：汇总改动、版本、测试结果、Release 链接与回退方式，附「完成检查清单」。

## 自动审计（实施后必做）

实施完成后、提交前，**必须自动审计**：

1. **自审**：按 `docs/audit-checklist.md` 逐项核对（正确性、文档同步、红线合规、
   测试、密钥、private 同步）。
2. **独立审计（推荐）**：优先把审计委托给**独立子 agent / 独立会话**——给它
   `git diff` 与 `docs/audit-checklist.md`，用全新上下文审查本次改动（不共享本次
   对话记忆），只回传发现的问题清单。
3. **修复与复检**：修复全部发现；修复本身影响面大时再次审计。
4. 审计结论记入最终汇报（审计人、发现数、修复情况）。

## 通用红线（Agent 开发，强制）

1. **先对齐后实施**：实施之前必须对齐需求和计划，得到用户确认之后再实施；
   未确认不实施（低风险例外见第 2 条）。
2. **变更分级**：高风险操作（大规模影响文件、破坏性变更、永久删除、发布/推送、
   修改用户数据）先展示方案、征得用户同意后执行；低风险先执行、随后记录、告知用户
   并给出回退方案。
3. **实施后自动审计**：每次实施完成后按「自动审计」执行，优先独立子 agent 审计。
4. **删除纪律**：删除默认进系统回收站/版本控制可恢复；严禁绕过工具接口的永久删除
   （`rm -rf` 等）；确需永久删除必须用户确认。
5. **回读校验**：重要写入/修改/移动后回读核对内容与结构，缺失即补正。
6. **创建前相似检查**：创建新文件/内容前先搜索相似内容，高相似时由用户决策
   （合并 / 跳过 / 仍创建）。
7. **信息以用户/事实为准**：不自行臆造；信息不足时询问补齐，不猜测。
8. **不破坏用户未提交的改动**：不擅自回滚、reset、stash、覆盖用户未提交内容；
   不代为 `git init` 用户的其他仓库；不对共享分支 force push。
9. **private 目录纪律**：个人/开发期文件一律放 `private/`，主仓库绝不提交
   `private/` 内容；发布前必须先同步 private 子 git（见「发布流程」）。
10. **发布前验证**：检查与测试通过、TEST-REPORT 有记录、审计完成，才允许发布。
11. **密钥安全**：任何密钥/凭据不入主仓库（见「仓库布局」规则 4）。
12. **文档同步**：改动涉及用户视角或流程时，受影响文档在**同一次改动**内更新。

## 版本管理

- **版本号**：`VERSION` 文件为单一事实来源，格式 `X.Y.Z`；git tag `vX.Y.Z` 与
  Release 使用同一版本。
- **递增规则**：版本号**从 `0.0.1` 开始**；每次默认只升最后一位（patch）；
  **前两位（major/minor）增加必须向用户确认**；破坏性变更必须用户确认并升主版本、
  说明迁移方案。
- **提交信息格式**：`feat: / fix: / docs: / chore: / refactor: vX.Y.Z - 描述`；
  仅文档/内部改动用 `docs:` / `chore:`。
- **自动发布**：版本递增由 agent **本地**执行（`scripts/bump-version.ps1` 同步
  `VERSION` 与 `package.json` / `Cargo.toml`，同时更新 CHANGELOG——`private/` 不进
  GitHub，CI 无法代劳）；推送 main 后，若当前 `VERSION` 尚无对应 tag，CI
  （`.github/workflows/release.yml`）自动打 tag 并创建 GitHub Release。
- **手动/自动二选一**：手动发布（本地 bump + tag + `gh release create`）后不要再
  期望 CI 重复发布；CI 只发布「无 tag 的当前版本」，不会二次递增版本。

## 发布流程（每次改动完成后执行；md 驱动、agent 执行）

1. **版本递增**：默认 patch；更新 `VERSION`（`scripts/bump-version.ps1`，会同步
   `package.json` / `Cargo.toml` 若存在）与 `private/dev/CHANGELOG.md` 顶部条目。
2. **检查受影响文档**：改动完成即文档就绪（CHANGELOG / DESIGN / TEST-REPORT /
   README / 根 AGENTS.md / private/AGENTS.md / 用户可见文档）。
3. **同步 private 子 git（发布前必做）**：`git -C private status --short` 检查
   `private/` 是否有变动；有变动先 `git -C private add -A -- .` 并提交
   （`docs: private vX.Y.Z - 描述`），确认 `git -C private status --short` 干净后
   再进入主仓库发布。
4. **主仓库提交推送**：`git add -A -- .` + commit（格式见「版本管理」）+ `git push`。
5. **打标签与 Release**：`git tag vX.Y.Z` + `git push origin vX.Y.Z`；创建 GitHub
   Release（`gh release create vX.Y.Z --title "vX.Y.Z" --notes "<变更摘要>"
   --attach <发布产物>`；gh 未认证时请用户 `gh auth login` 或网页手动上传）。
   推送 main 后 CI 也会自动完成第 5 步（仅当当前 VERSION 尚无 tag 时；不会
   二次递增版本，见「版本管理」）。
6. **分发/安装/部署**：按项目实际（安装包、zip、文档站点等）。
7. **汇报**：汇总改动、版本、测试、Release 链接、安装位置与回退方式，附完成检查清单。

> 可用 `scripts/pre-release-check.ps1` 一键执行发布前检查（private 子 git 同步、
> 版本一致性、仓库状态、审计提醒）。

## 测试与质量

- **检查命令**：`scripts/ci-check.ps1`（本地与 CI 共用入口；按项目实际实现
  lint / build / test）。
- **发布前必测**：运行检查命令 + 项目测试，结果记录于 `private/dev/TEST-REPORT.md`；
  **未通过不发布**。
- **测试素材**：本地测试库/测试项目放 `private/test/`（B 区）。
- **明文例外（仅此一种）**：本次改动不涉及运行时文件、且用户明确确认时，测试结论
  可沿用上一版本，必须在 TEST-REPORT 注明「用户确认沿用」；禁止 agent 自行省略。

## 文档职责划分

| 文档 | 位置 | 职责 |
|---|---|---|
| 根 `AGENTS.md` | 公开 | 公开入口（任何 agent 接手本项目） |
| `private/AGENTS.md` | 私有 | 开发入口与当前状态（唯一常青开发记忆） |
| `private/dev/DESIGN.md` | 私有 | 当前设计 + 开发工作流 + 开发规范 + 文件分类归属 |
| `private/dev/CHANGELOG.md` | 私有 | 完整版本历史（每次发布必更新） |
| `private/dev/TEST-REPORT.md` | 私有 | 当前测试记录与运行方式（每次发布必更新） |
| `README.md` | 公开 | 面向使用者/贡献者 |
| `docs/` | 公开 | 公开文档（架构、审计清单等） |
| `CONTRIBUTING.md` | 公开 | 人类贡献者与 agent 的协作约定 |

## 许可

{{LICENSE_NOTICE}}
