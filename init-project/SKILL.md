---
name: init-project
metadata:
  version: 1.2.1
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
- **开发工作流与红线（15 条）**：先对齐需求与计划、获确认后实施；实施后自动审计
  （推荐独立子 agent 审计）；阶段落盘、上下文恢复重读；验证后发布。
- **立项调研先行**：讨论立项类话题时先 GitHub 调研并提醒「先调研再立项」（红线 13）。
- **文档双模块与治理**：文档标注【通用】/【项目专用】，升级只应用【通用】；正文 =
  当前有效状态（覆盖旧决策、禁 AI 追加历史、留痕一行）。
- **版本管理与 CI/CD**：`version.json` 单一事实来源 + git tag；`.github/workflows/`
  自动 CI 检查；**版本递增由 agent 本地执行**（`scripts/bump_version.py`），
  **默认不自动发布**（用户确认后走发布流程，可用 `--auto-release` 开启）；CI 对
  尚无 tag 的当前版本自动打 tag 并建 Release。
- **自动化脚本**：`scripts/bump_version.py`、`pre_release_check.py`、`ci_check.py`
  、`trash.py`（仅依赖 Python 标准库，Python 3.9+ 跨平台运行，UTF-8）。
- **阶段落盘与经验沉淀**：`private/dev/WORKLOG.md`（每完成一小阶段更新）+ 
  `EXPERIENCE-TO-TEMPLATE.md` / `EXPERIENCE-TO-KB.md`（每轮对话后写入完整候选经验）。
- **私有开发指引**：`private/AGENTS.md` 含本机环境、用户确认的设计决策、定案清单、
  必须询问人类清单；`private/dev/` 承载 DESIGN / CHANGELOG / TEST-REPORT / WORKLOG /
  经验文档。
- **质量门禁**：文档 / 常规代码 / 架构变更三级门禁；发布前自测（产物可运行、关键
  文件齐全、无密钥/运行时数据混入）。
- **发布产物与归档**：构建/打包产物统一输出 `dist/`（不进 git，Release 自动
  attach）；项目停止主动开发时按「项目归档/退役」流程执行（最终发布 + README
  归档标记 + 产物归档 + 经验沉淀，agent 不擅自删除）。
- **实体目录**：`dist/`（发布产物，C 区占位）与 `archive/`（归档区，A 区进 git）
  随模板初始化即存在，目录树/三区表/归档流程已显式引用。
- **测试落地指引**：`docs/TESTING.md`（pytest 示例、覆盖率、CI 接入、TEST-REPORT
  对应；`ci_check.py` 内含接入示例注释）。
- **开发前规范（PRD/RFC/ADR/RESEARCH 四登记册）**：M/L 需求先走开发前门禁——
  需求（PRD）、方案（RFC）、调研（RESEARCH）、架构决策（ADR）分别落
  `private/dev/{prd,rfc,adr,research}/`（各含 `INDEX.md`：状态机/编号规则/
  模板骨架；S 档可跳过）；`scripts/check_dev_docs.py` 自动校验登记册一致性
  （编号连续/状态机/INDEX 同步），已并入 `ci_check.py` 与发布前检查。
- **流程提示**：每次对话展示流程位置（当前节点/已完成/下一步，16 节点两阶段
  清单），以 `private/dev/WORKLOG.md`「流程位置」为单一真相；展示时缩写附中文
  翻译（对照表见模板 `private/AGENTS.md`「缩写对照」）。
- **删除纪律**：对话内删除先移入 `_trash/<agent产品名>_<日期>_<时分>/`（如
  `codex_2026-08-25_2330`），任务结束时用 `scripts/trash.py` 整体进回收站。
- **模板版本与升级**：项目根 `version.json` 的 `template_version` 记录初始化时的
  模板版本；升级按 `docs/UPGRADE.md` 只应用【通用】模块变更。

## 前置确认（必须）

1. 若目标项目尚在**立项/思路阶段**（用户要讨论项目思路、需求、架构、功能、产品
   等），先按模板红线 13 在 GitHub 调研现成参考（相似项目、方案、库），向用户
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
   `docs: private v0.0.1 - init`。**未获用户确认前不 `git push`**（远端未配置
   时不推送；配置了远端也先征得同意）。
3. **回读校验**（按 `references/init-steps.md` 的校验清单）：
   - 占位符已全部替换（`git grep -n -E '\{\{[A-Z_]+\}\}'` 应无残留；GitHub
     Actions 的 `${{ }}` 表达式属正常）；
   - `private/.git` 存在、主仓库 `.git` 存在；
   - `git status`（主）与 `git -C private status`（子）均干净；
   - 根 `AGENTS.md` 与 `private/AGENTS.md` 可读且内容正确；
   - `version.json`：`version` 为 `0.0.1`、`template_version` 与 skill/模板版本一致
     （以 `assets/project-template/version.json` 的 `template_version` 字段为准）；
   - `private/dev/WORKLOG.md`、`EXPERIENCE-TO-TEMPLATE.md`、`EXPERIENCE-TO-KB.md`
     已生成；
   - `private/dev/{prd,rfc,adr,research}/INDEX.md` 已生成（开发前四登记册）；
   - `private/dev/WORKLOG.md`「当前任务」含「流程位置」字段；
   - `python scripts/check_dev_docs.py` 退出码 0（空登记册应通过）；
   - `python scripts/trash.py --help` 退出码 0。
4. **收尾与汇报**：确认 `.gitignore` 生效（`git check-ignore private/` 应命中）；
   向用户汇报：初始化位置、两个 git 仓库、下一步建议（填写 README 与
   `private/AGENTS.md` 的「本机环境」「用户决策」；首个 M/L 需求走开发前门禁
   ——需求/方案/决策/调研落 `private/dev/{prd,rfc,adr,research}/`；每次对话
   展示流程位置；配置远端后推送）。

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
| 复制与替换（确定性执行） | 直接运行 `scripts/init_project.py` |
