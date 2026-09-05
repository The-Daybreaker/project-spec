---
name: init-project
description: 通用项目模板的技能载体，兼两个用途，适用于所有非纯聊天的对话。①项目初始化：当用户要求新建项目、初始化项目仓库/文件夹并意图套用本通用项目模板时，复制模板框架、替换项目占位符、初始化 git 并首次提交。②项目外通用行为基线：当对话不在任何项目/工作区内（无项目 AGENTS.md、不属于已打开的工作区）且有任务/产出/需行动时（编码、写文档、分析、调研、规划、创建/修改/整理文件、事实性问答、执行命令等），读取并遵循 assets/project-template/AGENTS.md（协作总纲）与其「五、宪章」节指向的 spec/constitution.md「宪章」节的条款作为行为基线；规范的唯一事实源是 constitution.md，本 skill 只指向、不复制（避免漂移）。项目内对话以该项目自己的 AGENTS.md 为准；纯闲聊（无任务、无产出、无需行动）除外。
agent_created: true
version: 0.9.0
---

# init-project — 通用项目模板技能

## 适用范围与两种用途

本 skill 适用于**所有非纯聊天的对话**，按情境分两种用途：

1. **项目初始化**：对话要新建 / 初始化项目、套用本通用项目模板时，走下面
   「定位 → 前置确认 → 执行流程 → 执行红线」，把模板复制成一个新项目骨架。
2. **项目外通用行为基线**：对话**不在任何项目 / 工作区内**（无项目
   `AGENTS.md`、不属于已打开的工作区）、且有任务 / 产出 / 需行动（编码、写
   文档、分析、调研、规划、文件操作、事实性问答、执行命令等）时，读取并
   遵循 `assets/project-template/AGENTS.md`（协作总纲）与其「五、宪章」节指向的
   `spec/constitution.md`「宪章」节条款，作为本次对话的行为底线。

判定顺序：

- **纯闲聊**（无任务、无产出、无需行动）→ 本 skill 不介入。
- **项目内对话**（在某个有自己 `AGENTS.md` 的项目 / 工作区里）→ 以那个项目
  自己的 `AGENTS.md` 为准，本 skill 不越位（项目内已含同一套宪章）。
- **项目外 + 非纯聊天** → 走用途 2，照 `assets/project-template/AGENTS.md`
  与其 `spec/constitution.md`「宪章」节办。

## 定位

> 以下「定位 / 前置确认 / 执行流程 / 执行红线」四节是**用途 1（项目初始化）**的流程。

把内嵌的通用项目模板（`assets/project-template/`）应用到用户指定的项目文件夹，
生成一个**自洽自足**的项目骨架：任何 agent 从零接手都能按根 `AGENTS.md` 继续开发，
不依赖本次对话上下文。模板自带：

- **框架结构**：`AGENTS.md`（协作总纲）/ `README.md`（使用手册）/
  `context/`（项目上下文）/ `workspace/`（干活 + 发布层，结构由 spec / 项目定）/ `process/`
  （任务板 + agent 记忆 + 临时件）/ `archive/`（历史）/ `spec/`（声明式工作流 + `constitution.md` 规范宪章）。
- **spec 机制**：`spec/AGENTS.md`（机制说明书 + 拉取指引）常驻；spec 内容
  （`spec.md` + `assets/`）与构建规则按需从云端货架拉取
  （`github.com/The-Daybreaker/project-spec`）、拉下来自由改；空 spec 时项目
  以框架形态轻装运转。

## 前置确认（必须）

1. 与用户确认目标目录（必须为空，或仅含用户声明保留的文件；**不覆盖已有非模板
   文件**）。
2. 收集参数：项目名（英文/拼音，kebab-case）、目标目录、默认分支（默认 `main`）。
3. 向用户展示初始化方案（落盘哪些文件、创建 git 仓库、首次提交），**获用户确认
   后再执行**（初始化是高风险操作：创建 git 仓库、批量落盘）。

## 执行流程

1. **运行脚本**（确定性的复制与初始化）：
   `python <skill>/scripts/init_project.py <目标目录> --name <项目名> [--branch main] [--no-git]`
   - 脚本复制模板（排除 `_trash/`、`.git/`、`__pycache__/`）、替换 `package.json` 项目名、
     `git init` + 首次提交；
     `--no-git` 仅复制文件（不建 git）。
2. **回读校验**（初始化后逐项核对，缺失立即补正）：
   - **结构**：框架齐全（`AGENTS.md` / `README.md` / `context/` / `workspace/` /
     `process/` / `archive/` / `spec/`）；`process/memory.md`、`spec/AGENTS.md`、
     `spec/constitution.md` 存在（`spec/` 出厂有机制说明书 + 规范宪章两件，
     spec 工作流内容按需才拉）；`_trash/` 未随模板
     复制进来；
   - **参数**（若指定了 `--name`）：`package.json` 的 `name` 已替换为项目名，
     `version` 保持模板原值不变（不随初始化改动）。
   - **git**：主仓库 `.git` 存在；`git status` 干净；首次提交信息为
     `chore: init from project template`。
   - **常见问题**：首次提交失败多半是未配置 `git user.name` / `user.email`，让
     用户配置后手动提交；`--no-git` 模式不建 git。
3. **收尾汇报**：向用户汇报初始化位置、git 仓库，以及下一步建议
   （首次对话让 agent 冷启动对齐项目背景与目标；需要文档体系/工作流时引入 spec；
   配置远端后推送）。

## 执行红线

1. **先对齐后实施**：目标目录、参数、方案必须获用户确认后才落盘。
2. **不覆盖**：目标目录已有非模板文件时停下询问，绝不静默覆盖/删除。
3. **不越界**：只操作用户指定的目标目录；不向用户其他仓库执行任何 git 操作。
4. **不擅自推送**：初始化完成后不自动 `git push`（除非用户明确要求）。
5. **回读校验**：初始化后必须按清单回读核验，发现缺失立即补正。

## 加载规则

| 场景 | 读取 |
|---|---|
| **项目外对话的行为基线（用途 2）** | `assets/project-template/AGENTS.md`（协作总纲）+ 其「五、宪章」节指向的 `spec/constitution.md`「宪章」节条款（规范唯一事实源在 constitution.md，只指向不复制） |
| 模板结构与文件职责（向用户解释模板） | `assets/project-template/AGENTS.md` |
| 复制与初始化（用途 1，确定性执行） | 直接运行 `scripts/init_project.py` |
