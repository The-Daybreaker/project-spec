# 模板升级指南（UPGRADE.md）

> 模块：全通用。
> 用途：当通用项目模板发布新版本后，指导 agent 将本项目从旧模板版本升级到新版本。

## 升级流程

1. **确认当前模板版本**：读项目根 `TEMPLATE_VERSION`。
2. **获取模板变更历史**：读模板仓库根 `CHANGELOG.md`（本地路径或 GitHub URL）。
3. **比对变更**：列出 `TEMPLATE_VERSION` → 目标版本之间所有变更条目。
4. **只应用【通用】模块**：根/私有 AGENTS.md、`docs/`、`scripts/`、`.github/`、
  模板资产（`.gitignore` / `.editorconfig` / `.gitattributes` 等；
  `scripts/version-sync.json` 位于 `scripts/`）；
   **【项目专用】模块**（README、DESIGN 的项目内容、CHANGELOG/TEST-REPORT/WORKLOG、
   经验文档、本机环境、用户决策等）**绝不覆盖**。
5. **应用方式**：逐条人工/agent 合并；模板仓库可用
   `python scripts/sync_template.py` 验证副本，项目内按需手工复制对应文件后调整。
6. **回读校验**：占位符无残留（`git grep -n -E '\{\{[A-Z_]+\}\}'`）；脚本可运行
   （`python scripts/ci_check.py` 退出码 0）；`python scripts/pre_release_check.py`
   通过。
7. **更新版本记录**：项目根 `TEMPLATE_VERSION` 改为目标版本。
8. **记录升级**：`private/dev/CHANGELOG.md` 与 `private/dev/WORKLOG.md` 记录本次升级。

> 注意：major 版本（如 2.0.0）升级前，先读新模板的 `AGENTS.md` 了解破坏性变更与迁移
> 方案；涉及红线/工作流变化时，同步核对本项目的私有规范是否需要调整。
