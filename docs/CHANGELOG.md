# CHANGELOG — 通用项目模板 版本变更历史

> 模块：项目专用（工作区）。
> 记录模板自身每次发版变更，与根 `version.json` 与 git tag 对齐；项目升级时据此比对
> （见 `project-template/docs/UPGRADE.md`）。

## v1.1.1（2026-08-25）

- WORKLOG 模板增强：「下次从这里继续」「人工介入点」；明确本文件不替代红线 15 重读。
- DESIGN 模板新增「关键不变量」「改动影响面定位表」占位小节。
- 私有 AGENTS 新增「定案清单」「必须询问人类清单」；决策记录格式
  （决策/原因/影响/不要，编号追加，字段可扩展，推翻按文档治理约定覆盖）。
- 发布流程补充「分发/打包前自测」（产物可运行、关键文件齐全、无运行时数据混入）。
- audit-checklist 新增「变更分级与质量门禁」（文档/常规/架构三级）。
- docs/README 新增「文档地图」。

## v1.1.2（2026-08-26）

以下为 v1.1.1 之后累积的全部变更（含工作区自身与模板【通用】模块），随本次发版
正式发布；`version.json` 的 `version` / `template_version` 与 tag `v1.1.2` 对齐。

- 目录结构：README 回根；工作区文档入 `docs/`、同步脚本入 `scripts/`。
- 模板结构：`CONTRIBUTING.md` → `docs/`；`version-sync.json` → `scripts/`；
  子目录 README 改名（`docs/DOCS.md`、`private/PRIVATE.md`、`private/test/TEST.md`）。
- 版本机制：`VERSION` / `TEMPLATE_VERSION` 合并为根 `version.json`
  （`version` + `template_version` 字段）；脚本/CI/skill 全部改读 `version.json`。
- P3 建议实施：`init_project.py` 增加 UTF-8 输出（中文 Windows 防乱码）；
  `UPGRADE.md` 澄清 `sync_template.py` 仅存在于模板母项目（目标项目不运行）；
  `CONTRIBUTING.md`「新需求先对齐意图」改为 DESIGN + 用户决策 + WORKLOG 承载
  （移除 CHANGELOG 误述）；`EXPERIENCE-TO-KB` 索引顺序规则（与正文一致、新条目
  在前）；版本单一来源（SKILL/init-steps 正文改引用 `version.json` +
  `sync_template.py` 自动校验 `metadata.version`）。
- 工作区根补 `.gitattributes`（LF 归一化，与模板一致；P3 #6 落地）。
- 模板补「项目归档/退役」流程（【通用】模块）：根/私有 `AGENTS.md` 新增小节 +
  README 归档说明 + DESIGN + `audit-checklist` 第 9 节归档前检查；触发=用户明确
  发起；流程=对齐确认→最终发布→README 归档标记→产物归档→经验沉淀→收尾；
  归档后只读维护（P3 #7 落地）。
- 模板补 `dist/` 发布产物约定：产物统一输出 `dist/`（C 区、不进 git、Release 自动
   attach `dist/**`）；发布流程第 6 步 / DESIGN「打包与发布」/ README 项目结构 /
   `release.yml` 注释同步；`init-project` SKILL 摘要加能力点；`agent-rules` 继承
   矩阵「不继承」列表登记（项目机制不进入全局精简版）。
- 模板实体目录：`dist/`（C 区占位 `.gitkeep`，`.gitignore` 改 `dist/*` +
  `!dist/.gitkeep`）与 `archive/`（A 区：`archive/ARCHIVE.md` 归档说明 + 最终
  快照）**随模板初始化即存在**；三区表 / 目录树 / 归档流程 / DESIGN /
  audit-checklist 同步引用（不搞懒加载）。
- 新增 `docs/TESTING.md` 测试落地指引（pytest 示例、覆盖率、CI 接入、TEST-REPORT
  对应）；DESIGN「测试」/ DOCS 文档清单 / README / `ci_check.py` 注释同步；
  init-project SKILL 摘要补能力点。
- 维护约定新增「索引/未发版区段纪律」：「新条目在前」的文档（EXP-KB 索引与正文、
  CHANGELOG 未发版区段）新增条目须**正文与索引同时置顶**，收尾核对索引顺序 /
  日期 / 未发版条目与 `git log` 一致。
- agent 安装目标新增 `.qoder-cn`：安装表扩为六处（codex / dsh / workbuddy /
  trae-cn / qoderworkcn / qoder-cn）。
- 发版同步：约定补充「全局 grep 新旧版本号」防版本字样残留。
- 工作流收口：WORKLOG 生命周期纪律（任务开始切换当前任务、收尾校准硬事实）。
- 经验自动沉淀：维护约定明确「每轮对话结束自动把完整候选经验写入
  `docs/EXPERIENCE-TO-KB.md`（必做、不需询问）」，并追加根因经验条目。
- 新增 `agent-rules/` skill：从模板【通用】派生精简版 agent 全局行为规范（15 条
  红线通用化 + 精简工作流/审计/完成清单，仅非项目且非纯聊天对话加载）；继承矩阵
  `references/inheritance-map.md` + `sync_template.py` 自动化校验（版本一致性 /
  矩阵覆盖 / 红线正文指纹）；安装说明并入工作区 README。
- init-project 审计修复：SKILL 定位摘要补齐 v1.1.1 能力点（文档双模块/三级门禁/
  WORKLOG 生命周期/定案询问清单/发布前自测/红线 15 条编号）+ 发布策略措辞修正
  （默认不自动发布）；init-steps 删除过时的「编码提示」（旧说明直接删除不留档）。
- agent-rules 触发语义收紧（用户确认）：仅当对话不在任何项目/工作区内且非纯聊天
  时加载，项目内不加载；同步 README / AGENTS 表述与五个已安装副本。
- init-project skill **首次安装**到五个 agent（codex / dsh / workbuddy /
  trae-cn / qoderworkcn）；QoderWork skill 目录纠正为 `~/.qoderworkcn/skills`
  （原误装 `~/.qoderwork/skills` 已清理进回收站）。
- 删除纪律命名统一：临时删除区文件夹 = `<agent产品名>_<YYYY-MM-DD>_<HHMM>`
  （如 `codex_2026-08-25_2330`），只举例、**不设固定 agent 列表**（保证通用性）；
  模板红线 4 / 私有 AGENTS / DOCS / audit-checklist / DESIGN / init-project /
  agent-rules 同步，继承矩阵红线 4 指纹更新。
- 发版同步约定增加「特性核对清单」：模板 CHANGELOG 能力点 ↔ 两 skill 摘要逐条
  对照（防摘要级过时复发）。

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
