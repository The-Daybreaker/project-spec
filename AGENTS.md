# AGENTS.md — 通用项目模板工作区（本项目规范）

> 模块：混合（【通用】= 沿用模板规范；【项目专用】= 本工作区维护约定）。
> 本文件是**本项目（模板工作区）**的专属规范入口：任何 agent 在本工作区工作时先读
> 本文件，再读模板规范（`project-template/AGENTS.md` 与
> `project-template/private/AGENTS.md`）。上下文压缩后或新对话开始时，必须重读
> 本文件、模板规范与 `WORKLOG.md` 后再继续（红线 15）。

## 【项目专用】项目概览

- **定位**：通用项目模板 + init-project skill 的维护工作区（本项目本身就是模板的
  「母项目」）。
- **目录**：`project-template/`（权威模板，同步到 skill 资产）、`init-project/`
  （skill：SKILL.md / references / scripts / assets）、`sync_template.py`（同步脚本）。
- **版本**：根 `VERSION`（当前 1.1.0）+ git tag；模板自身变更历史见根 `CHANGELOG.md`。

## 【通用】红线与工作流

- 遵循模板规范：红线、工作流、版本/发布、审计，见 `project-template/AGENTS.md` 与
  `project-template/private/AGENTS.md`（冲突时私有版优先）。
- 阶段落盘：每完成一小阶段先更新根 `WORKLOG.md` 与受影响文档再继续。

## 【项目专用】维护约定（强制）

1. **改模板必同步**：修改 `project-template/` 后运行 `python sync_template.py`
   （同步 + 哈希校验），两份副本必须一致。
2. **private 骨架强制跟踪**：模板自身 `.gitignore` 忽略 `private/`，提交用
   `git add -f project-template/private init-project/assets/project-template/private`。
3. **skill 校验**：`PYTHONUTF8=1 python <skill-creator>/scripts/quick_validate.py
   init-project`（中文 Windows 默认 GBK 需 PYTHONUTF8=1）。
4. **发版同步**：版本递增时同步更新 `VERSION`、`project-template/TEMPLATE_VERSION`、
   根 `CHANGELOG.md`、`SKILL.md metadata.version`，再走模板发布流程。
5. **删除纪律**：对话内删除先移入 `_trash/<agent名>_<YYYY-MM-DD>_<HHMM>/`，
   任务结束时整体进回收站（`python scripts/trash.py`），避免小文件堆积。

## 【项目专用】本机环境

- 工作区：`<工作区路径>`
- 工具链：Python 3.14（模板脚本要求 3.9+）、git、pwsh（仅工作区自用）
- 已知坑：工作区 `.git` 在本环境只读（无法代提交）；git 全局 ignore 权限告警可忽略

## 【项目专用】用户确认的设计决策

- 模板脚本统一使用 Python（不再用 PowerShell）。
- 删除纪律：`_trash/` 临时删除区 + 整轮进回收站。
- 经验文档放 `private/dev/`，完整条目、不预设沉淀位置。
- 工作区不建 private 子 git（避免与模板 private 骨架混淆）。

## 文档职责

| 文件 | 模块 | 职责 |
|---|---|---|
| `AGENTS.md`（本文件） | 混合 | 工作区专属规范入口 |
| `WORKLOG.md` | 项目专用 | 阶段落盘（每完成一小阶段更新） |
| `CHANGELOG.md` | 项目专用 | 模板版本变更历史（升级比对依据） |
| `README.md` | 项目专用 | 面向使用者的说明 |
| `project-template/` | 通用 | 权威模板（同步到 `init-project/assets/`） |
| `init-project/` | 通用 | skill（SKILL.md / references / scripts / assets） |
