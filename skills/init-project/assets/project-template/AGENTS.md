# AGENTS.md — {{PROJECT_NAME}}

> 模块：混合（【通用】= 工作流/红线/版本/发布/测试/文档职责；【项目专用】= 项目概览/当前状态）。
> 本文件随仓库发布到 GitHub（公开），是**任何 agent 从零接手本项目的入口**：自洽自足，
> 不依赖任何特定 agent、工具或对话上下文。
> 本文件只承载可公开的内容；项目开发与维护的完整规范、个人/机器专属信息位于
> `private/AGENTS.md`（由 private 子 git 管理，不进 GitHub，仅本机开发 agent 读取）。
> 两份文件冲突时：`private/AGENTS.md` 中的开发/机器/个人专属细节以它为准。

## 【项目专用】项目概览

- **定位**：{{PROJECT_DESCRIPTION}}
- **技术栈与目录**（按项目实际补充）：
  - `src/` — 主要代码
  - `docs/` — 公开文档
  - `scripts/` — 自动化脚本（版本、发布前检查、CI 检查）
  - `private/` — 私有区（个人/开发期文件，**不进 GitHub**，见「仓库布局」）
  - `.github/workflows/` — CI / 自动发布
- **版本**：以 `version.json` 的 `version` 字段与 git tag `vX.Y.Z` 为准；完整历史见
  `private/dev/CHANGELOG.md`（私有，不发布）。
- **模板版本**：`version.json` 的 `template_version`（初始化/升级时的通用项目模板
  版本，见「模板升级」）。
- **当前状态**：见 `private/AGENTS.md`「项目状态与版本」（开发期状态只记在私有指引）。

## 【通用】仓库布局与文件分类归属（三区，强制）

| 区 | 位置 | 内容 | 版本管理 |
|---|---|---|---|
| A. 公开 | 仓库根、`src/`、`docs/`、`scripts/`、`.github/`、`archive/` | 用户可见、可发布、无敏感信息（含归档区） | 主仓库 git，发布到 GitHub |
| B. 私有 | `private/` | 个人/机器专属信息、开发期文档（PRD/RFC/ADR/RESEARCH 登记册、PROTOTYPE（页面原型/设计稿）、DESIGN/CHANGELOG/TEST-REPORT/WORKLOG/经验文档）、测试素材 | private 子 git（本地、无远端） |
| C. 不管理 | 各处 | `node_modules/`、`dist/`、`build/`、日志、缓存、临时文件、`_trash/` | 无（.gitignore 忽略） |

**归属判定规则**（新增文件必须先判区再落盘）：

1. 含**个人/机器专属信息**或**发布前不公开**内容 → B（`private/`）；
2. **生成物/缓存/可重建**内容 → C（不版本管理）；
3. 用户可见、可发布、无敏感信息 → A（主仓库）；
4. **密钥/凭据绝不入库**：`.env`、`*.key`、`*_secret*` 等一律进 `.gitignore`；
   确需保留的密钥只放 `private/`（且不提交 private 子 git，或加密后提交）。

**发布前检查**：主仓库 `git status` 只应出现 A 区文件；`git -C private status`
负责 B 区；C 区内容两者都不得出现。发布前必须先同步 private 子 git
（见「发布流程」与 `scripts/pre_release_check.py`）。

## 【通用】Agent 快速上手（每次新对话、任何 agent 都按此 bootstrap）

1. 读本文件；再读 `private/AGENTS.md`——它是**开发入口与完整开发规范**
   （唯一常青开发记忆），含完整工作流、发布流程、版本、本机环境、用户决策。
2. 查看两个仓库状态：`git status`（主仓库）、`git -C private status`（私有子 git）。
3. 读 `version.json` 与 `private/dev/CHANGELOG.md` 顶部，确认当前版本与最近变更。
4. 读 `private/dev/DESIGN.md`（设计）与 `private/dev/TEST-REPORT.md`（测试记录）；
   有进行中的需求/方案/决策时读 `private/dev/{prd,rfc,adr,research}/INDEX.md`
   （登记册状态，见「开发工作流」）。
5. 读 `private/dev/WORKLOG.md`（恢复进行中进度）；若旧任务已完结或内容膨胀，
   **先询问用户是否清理**（归档到「历史记录」或移入 `_trash/`），确认后才清理。
6. **上下文压缩后或任何新对话开始时，必须先完成以上重读（红线 15），不得凭记忆
   直接继续。**
7. 任何实施开始前，必须先走「开发工作流」前 3 步：**对齐需求与计划、获用户确认**。

## 【通用】开发工作流（摘要；完整版见 `private/AGENTS.md`「开发工作流」）

**开发前（M/L 需求必走；S 档直达「确认开工」）：需求提出 → 调研（红线 13，结果落
`RESEARCH-XXXX` 或内嵌）→ PRD 定稿（门禁 1）→ RFC 评审（可选）→ ADR 记录
（架构级，门禁 2）→ DESIGN 吸收 → 确认开工 → 实施（每完成一小阶段先落盘更新
WORKLOG 与受影响文档，红线 14）→ 自动审计 → 验证 → 展示与提交（先 private
子 git）→ 发布 → 经验沉淀（每轮对话结束把完整候选经验写入
`private/dev/EXPERIENCE-TO-TEMPLATE.md` / `private/dev/EXPERIENCE-TO-KB.md`）→
汇报。**涉及界面/交互、架构/结构、流程/状态的改动，需先出图（页面原型/架构图/
流程图）向用户展示、获确认后才进入下一步（见 `private/AGENTS.md`「开发工作流」
「可视化确认」）。**

**流程提示（每次对话强制）**：实质回复/阶段落盘/上下文恢复/收尾/用户询问进度时，
展示流程位置——当前节点（16 节点两阶段，见 `private/AGENTS.md`「流程提示」）、
已完成链、下一步；**展示时缩写须附中文翻译**（如 ADR=架构决策记录，对照表见
`private/AGENTS.md`「缩写对照」）；以 `private/dev/WORKLOG.md`
「当前任务 → 流程位置」为单一真相；**文档更新贯穿全程**（文档就绪 → 发布前
文档检查 → 状态文档收口，见 `private/AGENTS.md`「文档更新流程」）。

涉及**立项类话题**（项目思路/需求/架构/功能/产品）时，先按「通用红线」第 13 条在
GitHub 调研现成参考，并提醒用户**「先调研再立项」**。

## 【通用】自动审计（实施后必做；清单见 `docs/audit-checklist.md`）

实施完成后、提交前，必须自动审计：**自审**（按 `docs/audit-checklist.md` 逐项核对）
→ **独立审计（推荐）**（委托独立子 agent / 独立会话，只看 `git diff` 与审计清单）
→ **修复与复检**（修复影响面大时再次审计）→ 审计结论记入最终汇报。

## 【通用】通用红线（Agent 开发，强制）

1. **先对齐后实施**：实施之前必须对齐需求和计划，得到用户确认之后再实施；
   未确认不实施（低风险例外见第 2 条）。
2. **变更分级**：高风险操作（大规模影响文件、破坏性变更、永久删除、发布/推送、
   修改用户数据）先展示方案、征得用户同意后执行；低风险先执行、随后记录、告知用户
   并给出回退方案。
3. **实施后自动审计**：每次实施完成后按「自动审计」执行，优先独立子 agent 审计。
4. **删除纪律**：对话内删除先移动到项目本地 `_trash/<agent产品名>_<YYYY-MM-DD>_<HHMM>/`
   （临时删除区，如 `codex_2026-08-25_2330`；不设固定 agent 列表，以执行 agent 的
   产品名为准），对话任务结束时用 `python scripts/trash.py` 将整轮文件夹**整体**
   移入回收站（避免小文件堆积）；严禁绕过工具接口的永久删除（`rm -rf` 等）；
   确需永久删除必须用户确认。
5. **回读校验**：重要写入/修改/移动后回读核对内容与结构，缺失即补正；**同一文件
   多处并行编辑存在竞态（可能显示成功但未写盘），改完必须整篇回读抽查，不能只看
   diff**。
6. **创建前相似检查**：创建新文件/内容前先搜索相似内容，高相似时由用户决策
   （合并 / 跳过 / 仍创建）。
7. **信息以用户/事实为准**：不自行臆造；信息不足时询问补齐，不猜测。
8. **不破坏用户未提交的改动**：不擅自回滚、reset、stash、覆盖用户未提交内容；
   不代为 `git init` 用户的其他仓库；不对共享分支 force push。
9. **private 目录纪律**：个人/开发期文件一律放 `private/`，主仓库绝不提交
   `private/` 内容；发布前必须先同步 private 子 git（见「发布流程」）。
10. **发布前验证**：检查与测试通过、TEST-REPORT 有记录、审计完成，才允许发布。
11. **密钥安全**：任何密钥/凭据不入主仓库（见「仓库布局」规则 4）。
12. **文档同步与治理**：改动涉及用户视角或流程时，受影响文档在**同一次改动**内更新；
    **发现过时立即修（不论是否本轮引入），无变更时也须校准状态文档**（如 WORKLOG
    「当前做到哪里」）；**文档正文 = 当前有效状态**——决策修改时直接覆盖原文、禁止
    保留旧段落或「已取代」标注、禁止 AI 在正文追加大段历史说明，确需留痕只在
    `private/dev/CHANGELOG.md` 记一行摘要；**例外：`private/dev/prd|rfc|adr|research/`
    为历史文档区，允许正文留史**（PRD/RFC 定稿后冻结、ADR 只增不改、RESEARCH
    发现记录只追加，按各自 `INDEX.md` 状态机维护）；废案直接删除（走 `_trash/` →
    `trash.py`），可恢复性由删除机制保证。
13. **立项调研先行**：讨论项目思路/需求/架构/功能/产品等**立项类话题**时，
    **优先在 GitHub 调研现成参考**（相似项目、方案、库），并向用户展示调研结果、
    提醒用户**「先调研再立项」**；未经调研不引导用户立项，不把「从零造轮子」
    作为默认方案。
14. **阶段落盘**：任务过程中每完成一小阶段，先更新 `private/dev/WORKLOG.md` 与
    受影响文档再继续；进度不得只存在于对话记忆。
15. **上下文恢复重读**：上下文压缩后或任何新对话开始时，必须重读红线规范（根
    `AGENTS.md` 与 `private/AGENTS.md`）与相关文档（`WORKLOG.md`、`DESIGN.md`、
    `CHANGELOG.md`、`TEST-REPORT.md` 及受影响文档）后再继续；不得凭记忆直接继续。
16. **范围克制与纠错清零（按单办事、不加菜；撤菜不解释）**：严格按已确认的需求
    范围实施，不擅自添加需求外的功能、文件、依赖、配置或装饰；确需超出范围先
    征得用户同意。用户指出多余内容后：直接删除、恢复当前有效状态，**禁止在标题、
    提交信息、PR、注释或文档中为「未做/不做的事」补写说明**（如「已移除多余的 X」
    「为什么本项目不需要 X」），避免无用信息堆积污染上下文；确需留痕仅
    `private/dev/CHANGELOG.md` 记一行。

## 【通用】版本管理

- **版本号**：`version.json` 的 `version` 字段为单一事实来源，格式 `X.Y.Z`；git tag `vX.Y.Z` 与
  Release 使用同一版本。
- **递增规则**：版本号**从 `0.0.1` 开始**；每次默认只升最后一位（patch）；
  **前两位（major/minor）增加必须向用户确认**；破坏性变更必须用户确认并升主版本、
  说明迁移方案。
- **提交信息格式**：普通提交 `feat: / fix: / docs: / chore: / refactor: - 描述`
  （不带版本号）；**发布提交**（版本递增与发布前同步）带版本号
  `feat: vX.Y.Z - 描述`。
- **发布机制**：版本递增由 agent **本地**执行（`scripts/bump_version.py` 按
  `scripts/version-sync.json` 同步 `version.json` 与 `package.json` / `Cargo.toml` /
  `pyproject.toml` 等，同时更新 CHANGELOG——`private/` 不进 GitHub，CI 无法代劳）；
  推送 main 后，若当前 `version` 尚无对应 tag，CI（`.github/workflows/release.yml`）
  自动打 tag 并创建 GitHub Release。
- **手动/自动二选一**：手动发布（本地 bump + tag + `gh release create`）后不要再
  期望 CI 重复发布；CI 只发布「无 tag 的当前版本」，不会二次递增版本。
- **发布策略**：默认不自动发布（用户明确要求发布时才走发布流程）；如需自动发布，
  见 `private/AGENTS.md`「项目状态与版本」（初始化时可用 `--auto-release` 开启）；
  自动发布视为用户对发布/推送的**预授权**（红线 2 的同意要求对常规发布视为已
  满足），但破坏性变更、永久删除等高风险操作仍须单独确认。
- **模板版本**：项目根 `version.json` 的 `template_version` 记录初始化/升级时的
  通用项目模板版本；
  升级见「模板升级」与 `docs/UPGRADE.md`。

## 【通用】模板升级（详见 `docs/UPGRADE.md`）

当通用项目模板发布新版本时：读模板仓库 `CHANGELOG.md`（版本变更历史）→ 比对项目
`version.json` 的 `template_version` → **只应用【通用】模块变更**（【项目专用】
内容绝不覆盖）→ 回读校验 → 更新 `template_version` → 记录到 CHANGELOG/WORKLOG。

## 【通用】发布流程（每次发布时执行；完整版见 `private/AGENTS.md`「发布流程」）

1. **版本递增**：`scripts/bump_version.py`（默认 patch；前两位须用户确认），随后
   agent 手工更新 `private/dev/CHANGELOG.md` 顶部（脚本只校验同步目标，不写
   CHANGELOG，防止覆盖人工编辑的发布说明）。
2. **文档就绪**：CHANGELOG / DESIGN / TEST-REPORT / WORKLOG / README / 根 AGENTS.md /
   private/AGENTS.md / 用户可见文档同步。
3. **同步 private 子 git（发布前必做）**：`scripts/pre_release_check.py` 一键完成
   （检查并自动提交 private 变动、版本一致性、泄漏扫描、ci_check 已实现等）。
4. **主仓库提交推送**：提交信息见「版本管理」；`git push`。
5. **打标签与 Release**：`git tag vX.Y.Z` + `git push origin vX.Y.Z` +
   `gh release create`（或推送 main 后由 CI 自动完成，手动/自动二选一）。
6. **分发/安装/部署**：按项目实际（安装包、zip、文档站点等）；**构建/打包产物统一
   输出到 `dist/`**（C 区生成物，不进 git，`.gitignore` 已忽略；`release.yml` 自动
   attach `dist/**`，产物在别处时同步调整 workflow）；**分发/打包前自测**：产物
   可运行、关键文件齐全、无密钥/配置/素材等运行时数据混入。
7. **汇报**：汇总改动、版本、测试、Release 链接、安装位置与回退方式，附完成检查清单。

## 【通用】项目归档/退役（项目停止主动开发时执行）

- **触发**：项目停止主动开发（弃用 / 迁移 / 长期冻结）时，由**用户明确发起**归档；
  agent 不主动归档、不擅自删除。
- **归档流程**：
  1. **对齐与确认**：与用户确认归档原因与范围（只读冻结 / 迁移到新项目 / 删除），
     以及保留位置（本仓库 / 存档目录 / 归档仓库）；
  2. **最终发布**：按「发布流程」完成最后一次发版（版本递增、CHANGELOG /
     TEST-REPORT、审计、tag + Release），保证状态可复现；
  3. **归档标记**：README 顶部标注「⚠️ 已归档（只读）」+ 归档日期与原因；
     `private/AGENTS.md`「项目状态与版本」记录归档状态；
  4. **产物归档**：最终发布产物（`dist/**`）随 Release 保留；归档说明与最终快照
     放入 `archive/`（A 区，进 git，只读，见 `archive/ARCHIVE.md`）；如需本地存档
     再复制到项目外（不提交 git）；
  5. **经验沉淀**：把可复用经验写入 `EXPERIENCE-TO-TEMPLATE.md` /
     `EXPERIENCE-TO-KB.md`，并提醒用户真正沉淀；
  6. **收尾**：主仓库与 private 子 git 均提交干净；仓库/数据删除只由用户决定。
- **归档后约定**：只读维护（安全修复可走临时流程）；默认不再递增版本、不再自动
  发布；重新激活时先更新 `private/AGENTS.md` 状态，并按「快速上手」重新 bootstrap。

## 【通用】测试与质量

- **检查命令**：`scripts/ci_check.py`（本地与 CI 共用入口；按项目实际实现
  lint / build / test）。
- **发布前必测**：运行检查命令 + 项目测试，结果记录于 `private/dev/TEST-REPORT.md`；
  **未通过不发布**。
- **测试素材**：本地测试库/测试项目放 `private/test/`（B 区）。
- **明文例外（仅此一种）**：本次改动不涉及运行时文件、且用户明确确认时，测试结论
  可沿用上一版本，必须在 TEST-REPORT 注明「用户确认沿用」；禁止 agent 自行省略。

## 【通用】文档职责划分

| 文档 | 位置 | 模块 | 职责 |
|---|---|---|---|
| 根 `AGENTS.md` | 公开 | 混合 | 公开入口（本文件；面向使用者/贡献者/接手 agent） |
| `private/AGENTS.md` | 私有 | 混合 | 开发入口与完整开发规范（唯一常青开发记忆） |
| `private/dev/WORKLOG.md` | 私有 | 项目专用 | 阶段落盘（每完成一小阶段更新） |
| `private/dev/EXPERIENCE-TO-TEMPLATE.md` | 私有 | 项目专用·沉淀暂存 | 可沉淀进模板的经验（完整条目） |
| `private/dev/EXPERIENCE-TO-KB.md` | 私有 | 项目专用·沉淀暂存 | 可沉淀进知识库的经验（完整条目） |
| `private/dev/DESIGN.md` | 私有 | 混合 | 当前设计 + 开发规范（引用不重复） |
| `private/dev/prd/` | 私有 | 项目专用 | 需求登记册（PRD：为什么做/做什么/验收/优先级；定稿后冻结） |
| `private/dev/rfc/` | 私有 | 项目专用 | 方案登记册（RFC：怎么做/候选对比/推荐；评审后冻结） |
| `private/dev/adr/` | 私有 | 项目专用 | 决策登记册（ADR：决定了什么/为什么；只增不改） |
| `private/dev/research/` | 私有 | 项目专用 | 调研登记册（RESEARCH：红线 13 结果；发现记录追加、结论可覆盖） |
| `private/dev/prototype/` | 私有 | 项目专用 | 页面原型/设计稿（界面/交互改动的可视化产物；一文件一原型，轻量目录无状态机） |
| `private/dev/CHANGELOG.md` | 私有 | 项目专用 | 完整版本历史（每次发布必更新） |
| `private/dev/TEST-REPORT.md` | 私有 | 项目专用 | 当前测试记录与运行方式（每次发布必更新） |
| `README.md` | 公开 | 项目专用 | 面向使用者/贡献者 |
| `docs/` | 公开 | 通用（DOCS / audit-checklist / UPGRADE 等） | 公开文档 |
| `docs/CONTRIBUTING.md` | 公开 | 混合 | 人类贡献者与 agent 的协作约定 |
| `version.json` | 公开 | 通用 | 版本（`version`）与模板版本（`template_version`）单一事实来源 |

**文档维护清单**（变更类型 → 必须同步的文档）：

| 变更类型 | 必须同步的文档 |
|---|---|
| 决策/选型/红线类 | `private/AGENTS.md`「用户确认的设计决策」（覆盖原文）+ CHANGELOG 一行摘要 |
| 需求/方案/调研 | `private/dev/prd|rfc|research/`（登记册状态+索引同步）+ DESIGN（定稿吸收） |
| 架构决策 | `private/dev/adr/`（只增不改）+ `private/AGENTS.md` D-xxx 一行摘要 + `详见 ADR-XXXX` + CHANGELOG 一行摘要 |
| 进度/状态/环境 | `private/dev/WORKLOG.md`（当前做到哪里）+ 受影响文档 |
| 设计/架构/数据流 | `private/dev/DESIGN.md` |
| 功能/接口实现 | DESIGN / README / docs（按项目实际） |
| 测试/验证 | `private/dev/TEST-REPORT.md` |
| 版本/发布 | `version.json` / CHANGELOG / README |
| 用户视角/流程 | README / docs（audit-checklist / UPGRADE / CONTRIBUTING 等）/ 根 AGENTS.md |
| 模板升级 | 按 `docs/UPGRADE.md` 流程 + `version.json` + CHANGELOG/WORKLOG |

## 【通用】许可

{{LICENSE_NOTICE}}
