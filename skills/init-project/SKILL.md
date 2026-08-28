---
name: init-project
metadata:
  version: 1.6.0.patch0
description: 根据通用项目模板初始化指定项目文件夹：复制完整模板骨架（AGENTS.md 公开/私有拆分、private 子 git、.gitignore、CI/CD 工作流、自动化脚本、Agent+人协作开发工作流与通用红线），替换项目占位符，初始化主 git 与 private 子 git 并完成首次提交。当用户要求新建项目、初始化项目仓库/文件夹、套用项目模板时使用。
---

# init-project 项目初始化

## 定位

把内嵌的通用项目模板（`assets/project-template/`）应用到用户指定的项目文件夹，
生成一个**自洽自足**的项目骨架：任何 agent 从零接手都能按根 `AGENTS.md` 继续开发，
不依赖本次对话上下文。模板自带：

- **AGENTS.md 拆分**：根目录公开版（发布到 GitHub）+ `private/AGENTS.md` 私有版
  （个人/机器信息，不进 GitHub）；冲突时私有版优先。
- **private 子 git**：`private/` 整体被主仓库 `.gitignore` 忽略，内部独立 git 管理；
发布前自动检查变动并提交（`scripts/pre_release_check.py`）。
- **开发工作流与红线（19 条）**：先对齐需求与计划、获确认后实施；实施后自动审计
  （推荐独立子 agent 审计）；阶段落盘、上下文恢复重读；验证后发布。红线 16
  「上下文恢复重读」：压缩/新对话后重读规范再继续。红线 17「范围克制与纠错
  清零」：不做需求外添加、被指出的多余内容直接删除且不为未做之事补写说明
  （意图=番茄炒蛋不加东坡肉、撤菜不留疤）。红线 18「提问与共识确认」：禁止
  问题面板/选择面板类 UI 提问，回答≠确认（每次回答输出重检行）、硬触发节点
  展示共识卡四项并逐项表态（详见模板 AGENTS.md 红线 18）。红线 1「要求三要素」：
  任何红线/要求须有意图/展示/验收三要素。红线 19「敏感信息与私有区边界」：
  跟踪目录禁个人信息/密钥，私有区禁远端/禁打包。
- **立项调研先行**：讨论立项类话题时先 GitHub 调研并提醒「先调研再立项」（红线 14）。
- **文档双模块与治理**：文档标注【通用】/【项目专用】，升级只应用【通用】；正文 =
  当前有效状态（覆盖旧决策、禁 AI 追加历史、留痕一行）。
- **版本管理与 CI/CD**：`version.json` 单一事实来源 + git tag；`.github/workflows/`
  自动 CI 检查；**版本递增由 agent 本地执行**（`scripts/bump_version.py`），
  **默认不自动发布**（用户确认后走发布流程，可用 `--auto-release` 开启）；CI 对
  尚无 tag 的当前版本自动打 tag 并建 Release。
- **自动化脚本**：`scripts/bump_version.py`、`pre_release_check.py`、`ci_check.py`
  、`trash.py`（仅依赖 Python 标准库，Python 3.9+ 跨平台运行，UTF-8）。
- **阶段落盘与经验沉淀**：`private/dev/STATUS.md`（当前状态快照：阶段卡 + 生命周期
  合规清单 + 影响清单；每完成阶段/子阶段覆盖更新 + git 提交）+ `EXPERIENCE-TO-TEMPLATE.md`
  / `EXPERIENCE-TO-KB.md`（每轮对话后写入完整候选经验）。
- **私有开发指引**：`private/AGENTS.md` 含本机环境、用户确认的设计决策、定案清单、
  必须询问人类清单；`private/dev/` 承载 PHASES（阶段模块定义）/ STATUS（状态快照）/
  DESIGN / CHANGELOG / TEST-REPORT / ROADMAP（长期需求与展望，唯一长期入口）/
  经验文档。
- **阶段体系模块化**：16 节点收敛为 P1-P5 五阶段（需求/方案/开发/审计验证/交付发布）
  + 子阶段两级；每阶段有输入/明确产物/完成标志/生命周期；阶段/子阶段完成展示
  **阶段卡**（进度 + 生命周期合规清单 + 下一阶段输入预告）；🔵 决策型阶段/子阶段须
  用户确认放行、🟢 执行型展示即走；双维度模型（主流程串行 + 贯穿动作不占阶段）；
  权威定义与流程图在 `private/dev/PHASES.md`。
- **渐进式披露**：`docs/LOADING.md` 加载规则表（场景→必读/按需/默认不读，历史默认
  不读、红线始终必读）；面向用户的阶段指南已并入 `README.md`（唯一用户文档）；
  新对话/压缩后读 AGENTS → private/AGENTS → STATUS 快照恢复。
- **需求引导方法论（P1 内嵌）**：先复述意图、提发散性问题引导用户发现真正需求
  （痛点溯源→阶段粒度→披露深度→恢复机制→切换节奏逐层收敛），未发现/未澄清前
  禁止直接抛方案选项。
- **质量门禁**：文档 / 常规代码 / 架构变更三级门禁；发布前自测（产物可运行、关键
  文件齐全、无密钥/运行时数据混入）。
- **发布产物与归档**：构建/打包产物统一输出 `dist/`（不进 git，Release 自动
  attach）；项目停止主动开发时按「项目归档/退役」流程执行（最终发布 + README
  归档标记 + 产物归档 + 经验沉淀，agent 不擅自删除）。
- **实体目录**：`src/`（代码区，业务源码/资源统一放这里，根目录不放业务代码）、
  `dist/`（发布产物，C 区占位）与 `archive/`（归档区，A 区进 git）
  随模板初始化即存在，目录树/三区表/归档流程已显式引用。
- **测试落地指引**：`docs/TESTING.md`（pytest 示例、覆盖率、CI 接入、TEST-REPORT
  对应；`ci_check.py` 内含接入示例注释）。
- **开发前规范（PRD/RFC/ADR/RESEARCH 四登记册）**：M/L 需求先走开发前门禁——
  需求（PRD）、方案（RFC）、调研（RESEARCH）、架构决策（ADR）分别落
  `private/dev/{prd,rfc,adr,research}/`（各含 `INDEX.md`：状态机/编号规则/
  模板骨架；S 档可跳过）；`scripts/check_dev_docs.py` 自动校验登记册一致性
  （编号连续/状态机/INDEX 同步），已并入 `ci_check.py` 与发布前检查。
- **图可视化规范（先出图再确认）**：涉及界面/交互、架构/结构、流程/状态的改动
  先出图——流程图随 PRD/RFC、架构图随 RFC/ADR（Mermaid/SVG 单文件同目录）、
  页面原型/设计稿落 `private/dev/prototype/`（目录随初始化存在，`README.md` 含
  使用规则，一文件一原型）——向用户展示获确认后才实施（开发工作流「可视化
  确认」）。
- **设计契约（有接口/数据/权限的项目）**：设计契约放 `private/dev/design/`
  （架构/接口/数据/安全，适用必做/不适用须声明，声明落设计总览）；接口契约含
  接口清单（大白话）+ 场景映射表（用户审核面，审场景不审技术）+ 错误情况 +
  示例，用户确认场景映射后冻结，改契约须重新确认；详见
  `private/dev/design/README.md`。
- **阶段卡展示**：每次对话展示合并紧凑阶段卡（标题含状态 + 横置阶段线当前节点
  加粗 + 合规两行 + 反定型条件块仅关键/风险节点；全中文不显示字母缩写），以
  `private/dev/STATUS.md`「📇 阶段卡」为单一真相。
- **删除纪律**：对话内删除先移入 `_trash/<agent产品名>_<日期>_<时分>/`（如
  `codex_2026-08-25_2330`），任务结束时用 `scripts/trash.py` 整体进回收站。
- **模板版本与升级**：项目根 `version.json` 的 `template_version` 记录初始化时的
  模板版本；升级按 `docs/UPGRADE.md` 只应用【通用】模块变更。

## 前置确认（必须）

1. 若目标项目尚在**立项/思路阶段**（用户要讨论项目思路、需求、架构、功能、产品
   等），先按模板红线 14 在 GitHub 调研现成参考（相似项目、方案、库），向用户
   展示调研结果并提醒**「先调研再立项」**，用户确认后再继续收集参数；正式调研
   结果落 `private/dev/research/RESEARCH-XXXX`（或内嵌 PRD/RFC 对应节）。
2. 与用户确认目标目录（必须为空目录，或仅含用户声明保留的文件；**不覆盖已有
   非模板文件**）。
3. 收集参数：项目名（英文/拼音，kebab-case）、一句话描述、GitHub 远端 URL
   （可选）、默认分支（默认 `main`）、作者名（可选）、许可（可选，默认 MIT，
   其他可用自定义 LICENSE 文件）、自动发布（可选，默认关闭）。
4. 向用户展示初始化方案（落盘哪些文件、创建两个 git 仓库、首次提交信息），
   **获用户确认后再执行**（初始化是高风险操作：创建 git 仓库、批量落盘）。

## 执行流程

1. **运行脚本**（确定性的复制与占位符替换）：
   `python <skill>/scripts/init_project.py <目标目录> --name <项目名> --desc "<描述>"
   [--remote <URL>] [--branch main] [--author "<作者>"] [--license mit]
   [--license-file <LICENSE 路径>] [--auto-release] [--no-git]`
   - 脚本默认同时初始化主 git 与 private 子 git 并完成首次提交；
     `--no-git` 仅复制文件（不建 git，需用户另行决定）。
2. **git 收尾**（脚本已做时跳过）：主仓库 `git init -b <branch>` + 首次提交
   `chore: init from universal project template`；`git -C private init` + 提交
  `docs: private v0.0.1.patch0 - init`。**未获用户确认前不 `git push`**（远端未配置
  时不推送；配置了远端也先征得同意）。
3. **回读校验**（按 `references/init-steps.md` 的校验清单）：
   - 占位符已全部替换（`git grep -n -E '\{\{[A-Z_]+\}\}'` 应无残留；GitHub
     Actions 的 `${{ }}` 表达式属正常）；
   - `private/.git` 存在、主仓库 `.git` 存在；
   - `git status`（主）与 `git -C private status`（子）均干净；
   - 根 `AGENTS.md` 与 `private/AGENTS.md` 可读且内容正确；
   - `version.json`：`version` 为 `0.0.1.patch0`、`template_version` 与 skill/模板版本一致
     （以 `assets/project-template/version.json` 的 `template_version` 字段为准）；
   - `private/dev/STATUS.md`、`PHASES.md`、`EXPERIENCE-TO-TEMPLATE.md`、
     `EXPERIENCE-TO-KB.md` 已生成；
   - `docs/LOADING.md` 已生成（加载规则表；流程图在 `private/dev/PHASES.md`；
     面向用户的指南在 `README.md`）；
   - `private/dev/{prd,rfc,adr,research}/INDEX.md` 已生成（开发前四登记册）；
   - `private/dev/prototype/README.md` 已生成（页面原型/设计稿目录说明）；
   - `private/dev/STATUS.md`「📇 阶段卡」为合并紧凑模块（标题含状态 + 横置阶段线
     当前节点加粗 + 合规两行（✓ 已完成 / ⏳ 待完成）+ 反定型条件块；全中文不显示
     字母缩写）+ 任务影响清单含要读文档清单；
   - `python scripts/check_dev_docs.py` 退出码 0（空登记册应通过）；
   - `python scripts/trash.py --help` 退出码 0。
4. **收尾与汇报**：确认 `.gitignore` 生效（`git check-ignore private/` 应命中）；
   向用户汇报：初始化位置、两个 git 仓库、下一步建议（填写 README 与
   `private/AGENTS.md` 的「本机环境」「用户决策」；首个 M/L 需求走开发前门禁
   ——需求/方案/决策/调研落 `private/dev/{prd,rfc,adr,research}/`；每次对话
   展示阶段卡（以 `private/dev/STATUS.md`「📇 阶段卡」为准）；配置远端后推送）。

## 执行红线

1. **先对齐后实施**：目标目录、参数、方案必须获用户确认后才落盘。
2. **不覆盖**：目标目录已有非模板文件时停下询问，绝不静默覆盖/删除。
3. **不越界**：只操作用户指定的目标目录；不向用户其他仓库执行任何 git 操作。
4. **不擅自推送**：初始化完成后不自动 `git push`（除非用户明确要求）。
5. **回读校验**：初始化后必须按清单回读核验，发现缺失立即补正。

## 加载规则

| 场景 | 读取 |
|---|---|
| 初始化执行细节（参数表、占位符清单、校验清单、常见问题） | `references/init-steps.md` |
| 模板结构与文件职责（向用户解释模板） | 根 `assets/project-template/AGENTS.md` |
| 阶段体系定义（P1-P5/子阶段/切换规则，向用户解释） | `assets/project-template/private/dev/PHASES.md` |
| 复制与替换（确定性执行） | 直接运行 `scripts/init_project.py` |
