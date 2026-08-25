# CHANGELOG — 通用项目模板 版本变更历史

> 模块：项目专用（工作区）。
> 记录模板自身每次发版变更，与根 `VERSION` 与 git tag 对齐；项目升级时据此比对
> （见 `project-template/docs/UPGRADE.md`）。

## v1.1.1（2026-08-25）

- WORKLOG 模板增强：「下次从这里继续」「人工介入点」；明确本文件不替代红线 15 重读。
- DESIGN 模板新增「关键不变量」「改动影响面定位表」占位小节。
- 私有 AGENTS 新增「定案清单」「必须询问人类清单」；决策记录格式
  （决策/原因/影响/不要，编号追加，字段可扩展，推翻按文档治理约定覆盖）。
- 发布流程补充「分发/打包前自测」（产物可运行、关键文件齐全、无运行时数据混入）。
- audit-checklist 新增「变更分级与质量门禁」（文档/常规/架构三级）。
- docs/README 新增「文档地图」。

## v1.1.0（2026-08-25）

- PowerShell 脚本迁移为 Python：`bump_version.py` / `ci_check.py` / `pre_release_check.py`
  / `sync_template.py` / `trash.py`（跨平台进回收站）。
- 新增 `TEMPLATE_VERSION`：项目记录初始化/升级时的模板版本。
- 新增 `docs/UPGRADE.md`：模板升级指南（比对 CHANGELOG → 只应用【通用】模块）。
- 新增 `private/dev/WORKLOG.md`（阶段落盘）、`EXPERIENCE-TO-TEMPLATE.md` /
  `EXPERIENCE-TO-KB.md`（完整经验条目，沉淀即用，不预设位置）。
- 文档双模块约定：【通用】/【项目专用】标注；升级只覆盖【通用】模块。
- 红线 13 → 15：阶段落盘、上下文恢复重读。
- 删除纪律：对话内删除先入 `_trash/<agent>_<日期>_<时分>/`，任务结束整体进回收站。
- 提交信息：普通提交不带版本号，发布提交带 `vX.Y.Z`。
- 发布策略：默认不自动发布（`--auto-release` 开启）。
- init 脚本：`--license` / `--license-file` / `--auto-release` / 参数校验 / GBK 作者名修复。
- `.gitignore` 密钥模式扩充；新增 `.gitattributes` / `.editorconfig` / `version-sync.json`。

## v1.0.2（2026-08-15）

- 立项调研先行：讨论项目思路/需求/架构/功能/产品时优先 GitHub 调研现成参考并提醒
  用户「先调研再立项」。

## v1.0.1（2026-08-15）

- 版本规范 0.0.1 起步（前两位须用户确认）+ 经验沉淀流程（知识库 + 模板）。

## v1.0.0（2026-08-15）

- 通用项目模板 v1.0.0：项目模板 + init-project skill。
