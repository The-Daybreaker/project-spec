---
name: init-project
description: 根据通用项目模板初始化指定项目文件夹：复制完整模板骨架（七件套 + spec 机制），替换项目占位符，初始化 git 并完成首次提交。当用户要求新建项目、初始化项目仓库/文件夹、套用项目模板时使用。
agent_created: true
version: 0.9.0
---

# init-project 项目初始化

## 定位

把内嵌的通用项目模板（`assets/project-template/`）应用到用户指定的项目文件夹，
生成一个**自洽自足**的项目骨架：任何 agent 从零接手都能按根 `AGENTS.md` 继续开发，
不依赖本次对话上下文。模板自带：

- **七件套骨架**：`AGENTS.md`（协作总纲 + 宪章 6 条）/ `README.md`（使用手册）/
  `context/`（项目上下文）/ `workspace/`（source + delivery）/ `process/`
  （任务板 + 三件套）/ `logs/`（历史）/ `spec/`（声明式规范）。
- **spec 机制**：`spec/AGENTS.md`（机制说明书 + 拉取指引）+ `lockfile.py` /
  `lockfile.md` 常驻；spec 包与构建规则按需从云端模块库拉取
  （`github.com/The-Daybreaker/project-spec`）；空 spec 时项目以地基形态轻装运转。

## 前置确认（必须）

1. 与用户确认目标目录（必须为空，或仅含用户声明保留的文件；**不覆盖已有非模板
   文件**）。
2. 收集参数：项目名（英文/拼音，kebab-case）、目标目录、默认分支（默认 `main`）。
3. 向用户展示初始化方案（落盘哪些文件、创建 git 仓库、首次提交），**获用户确认
   后再执行**（初始化是高风险操作：创建 git 仓库、批量落盘）。

## 执行流程

1. **运行脚本**（确定性的复制与初始化）：
   `python <skill>/scripts/init_project.py <目标目录> --name <项目名> [--branch main] [--no-git]`
   - 脚本复制模板（排除 `_trash/`、`.git/`）、替换 `package.json` 项目名、
     `git init` + 首次提交；
     `--no-git` 仅复制文件（不建 git）。
2. **回读校验**（初始化后逐项核对，缺失立即补正）：
   - **结构**：七件套齐全（`AGENTS.md` / `README.md` / `context/` / `workspace/` /
     `process/` / `logs/` / `spec/`）；`_trash/` 未随模板复制进来；
     `spec/AGENTS.md`、`spec/lockfile.py`、`spec/lockfile.md` 存在。
   - **参数**（若指定了 `--name`）：`package.json` 的 `name` 已替换为项目名，
     `version` 保持模板原值不变（不随初始化改动）。
   - **git**：主仓库 `.git` 存在；`git status` 干净；首次提交信息为
     `chore: init from project template`。
   - **常见问题**：首次提交失败多半是未配置 `git user.name` / `user.email`，让
     用户配置后手动提交；`--no-git` 模式不建 git。
3. **收尾汇报**：向用户汇报初始化位置、git 仓库，以及下一步建议
   （首次对话让 agent 冷启动对齐项目背景与目标；需要文档体系/工作流时引入 spec 包；
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
| 模板结构与文件职责（向用户解释模板） | `assets/project-template/AGENTS.md` |
| 复制与初始化（确定性执行） | 直接运行 `scripts/init_project.py` |
