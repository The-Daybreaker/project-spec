# AGENTS.md — 通用项目模板工作区（本项目规范）

> 模块：混合（【通用】= 沿用模板规范；【项目专用】= 本工作区维护约定）。
> 本文件是**本项目（模板工作区）**的专属规范入口：任何 agent 在本工作区工作时先读
> 本文件，再读模板规范（`project-template/AGENTS.md` 与
> `project-template/private/AGENTS.md`）与 `docs/STATUS.md` 快照。上下文压缩后或
> 新对话开始时，必须重读本文件、模板规范与 `docs/STATUS.md` 后再继续（红线 15）。

## 摘要与加载规则（渐进式披露）

- **阶段体系**：工作区任务按 P1-P5 五阶段串行（P1 需求/P2 方案/P3 开发/P4 审计验证/
  P5 交付发布），权威定义见 `project-template/private/dev/PHASES.md`；每次专注一个
  阶段，严禁跨阶段；阶段/子阶段完成展示**阶段卡**（进度 + 生命周期合规清单 + 下一
  阶段输入预告）；🔵 决策型须用户确认、🟢 执行型展示即走；流程状态机见
  `docs/FLOW.md`。
- **披露协议**：什么场景读什么按下方加载规则表；历史默认不读、红线始终必读；
  全量规则见 `docs/LOADING.md`。

| 场景 | 优先级 | 读什么 |
|---|---|---|
| 新对话 / 压缩后恢复 | 必读 | 本文件 → 模板 AGENTS×2 → `docs/STATUS.md` 快照 |
| 红线规范 | 始终必读 | 模板 AGENTS 红线小节 |
| 阶段定义 / 切换规则 | 按需 | 模板 `project-template/private/dev/PHASES.md` |
| 流程 / 状态机 | 按需 | `docs/FLOW.md` |
| 实施任务 | 必读 | 模板 `private/dev/DESIGN.md` + 对应 PRD |
| 审计任务 | 必读 | 模板 `docs/audit-checklist.md` |
| 发布任务 | 必读 | 模板 `private/AGENTS.md` 发布流程 → CHANGELOG → pre_release_check |
| 母项目改模板 / 同步 | 必读 | 本文件「维护约定」→ `scripts/sync_template.py` |
| 历史决策 / 追溯 | **默认不读** | `docs/CHANGELOG.md` / 模板 ADR |

## 【项目专用】项目概览

- **定位**：通用项目模板 + init-project skill 的维护工作区（本项目本身就是模板的
  「母项目」）。
- **目录**：`README.md`（面向使用者的说明）+ `docs/`（工作区自身文档：CHANGELOG /
  STATUS / EXPERIENCE-TO-KB / FLOW / USER-GUIDE / LOADING）、`scripts/sync_template.py`
  （同步脚本）、`project-template/`（权威模板，同步到 skill 资产）、`skills/`（skill
  目录）：`init-project/`（skill：SKILL.md / references / scripts / assets）、
  `agent-rules/`（skill：精简版 agent 全局行为规范，仅非项目且非纯聊天对话加载）。
- **版本**：根 `version.json`（当前 1.4.1.patch0）+ git tag `vX.Y.Z.patchN`；模板自身变更历史见
  `docs/CHANGELOG.md`。

## 【通用】红线与工作流

- 遵循模板规范：红线、工作流、版本/发布、审计，见 `project-template/AGENTS.md` 与
  `project-template/private/AGENTS.md`（冲突时私有版优先）。
- 阶段落盘：每完成一小阶段先更新 `docs/STATUS.md` 快照与受影响文档再继续。

## 【项目专用】维护约定（强制）

1. **改模板必同步**：修改 `project-template/` 后运行
   `python scripts/sync_template.py`（同步 + 哈希校验），两份副本必须一致；
   模板【通用】变更还需同步 `skills/agent-rules/`（精简版全局规范正文或继承矩阵
   指纹复核），sync 会一并校验（版本一致性 + 矩阵覆盖 + 红线正文指纹）。
2. **private 骨架强制跟踪**：模板自身 `.gitignore` 忽略 `private/`，提交用
   `git add -f project-template/private skills/init-project/assets/project-template/private`。
3. **skill 校验**：`PYTHONUTF8=1 python <skill-creator>/scripts/quick_validate.py
   skills/init-project`（以及 `skills/agent-rules`；脚本参数为 skill 目录路径，
   不是 skill 名；中文 Windows 默认 GBK 需 PYTHONUTF8=1）。
4. **发版同步**：版本递增时同步更新根 `version.json`、`project-template/version.json`
   （`version` 与 `template_version` 两字段）、`docs/CHANGELOG.md`、
   `skills/init-project/SKILL.md metadata.version`、
   `skills/agent-rules/SKILL.md metadata.version` 与
   `skills/agent-rules/references/inheritance-map.md` 版本对照，并**全局 grep 新旧
  版本号**（如 `1.4.1.patch0` / `1.4.2.patch0`）核对所有文档内嵌版本字样（`SKILL.md` 仅
   `metadata.version`；`references/init-steps.md` 已改为引用 `version.json`；
   模板内部文件一律用占位符、不写死版本），确认无残留后再走模板发布流程。
   `scripts/sync_template.py` 会自动校验各 `SKILL.md metadata.version`、
   `agent-rules` 继承矩阵版本/覆盖/指纹与 `project-template/version.json` 的
   `template_version` 一致（改模板/发版后运行 sync 即校验）；另按**特性核对清单**
   逐条对照模板 CHANGELOG 能力点与 `skills/init-project/`、`skills/agent-rules/`
   摘要（自动化校验不覆盖摘要级过时，需人工比对）。`sync_template.py` 还会自动
   校验 `skills/init-project/references/init-steps.md` 对模板关键文件的覆盖
   （`INIT_STEPS_COVERAGE`，缺失即拦截，防止「只同步资产镜像、不同步 skill 承载
   文档」）；改模板/发版后的 **skill 覆盖度复查**必须核对：①
   `skills/init-project/SKILL.md` 摘要、② `init-steps.md` 校验清单/落地路线图、
   ③ `skills/agent-rules/`（仅当模板【通用】红线/工作流原则变更）、④ 全部已安装
   副本重装并哈希复核。
5. **删除纪律**：对话内删除先移入 `_trash/<agent产品名>_<YYYY-MM-DD>_<HHMM>/`
   （如 `codex_2026-08-25_2330`；不设固定 agent 列表，以执行 agent 的产品名为准），
   任务结束时整体进回收站（`python project-template/scripts/trash.py`），
   避免小文件堆积。
6. **STATUS 快照纪律（dogfood）**：新任务开始先更新 `docs/STATUS.md`「当前任务」；
   每完成阶段/子阶段**覆盖更新**快照 + 展示阶段卡 + git 提交（主仓库，提交信息带
   阶段标识，D14）；任务收尾/汇报前回读校准硬事实（文件数、版本号、提交号）与实际
   仓库状态一致后再汇报。
7. **经验自动沉淀**：每轮对话结束后**自动**把完整候选经验写入
   `docs/EXPERIENCE-TO-KB.md`（必做、不需询问，与模板红线 9 对齐）；沉淀与否、
   沉淀到哪由用户决定。
8. **索引/未发版区段纪律（收尾核对）**：「新条目在前」的文档（如
   `docs/EXPERIENCE-TO-KB.md` 索引与正文、`docs/CHANGELOG.md` 未发版区段），新增
   条目必须**正文与索引同时置顶**；任务收尾/汇报前核对：索引顺序与正文一致、
   「最后更新」日期与最新提交一致、未发版区段与 `git log <tag>..HEAD` 逐条比对。
9. **流程提示（dogfood）**：工作区汇报/阶段落盘/收尾展示**合并紧凑阶段卡**（标题含
   状态 + 横置阶段线当前节点加粗 + 合规已完成/待完成两行 + 反定型紧凑内容（仅关键/
   风险节点）；**只用中文名称、不显示字母缩写**），以 `docs/STATUS.md`「📇 阶段卡」
   为单一真相。

## 【项目专用】本机环境

- 工作区：`<工作区路径>`
- 工具链：Python 3.14（模板脚本要求 3.9+）、git、pwsh（仅工作区自用）
- 提交：工作区改动由 agent 自动提交（普通提交不带版本号，发布提交带 vX.Y.Z.patchN）；
  当前沙箱下 `.git` 只读，`git add/commit` 需申请升级权限执行
- 已知坑：git 全局 ignore 权限告警（`unable to access .../git/ignore`）可忽略

## 【项目专用】用户确认的设计决策

- 模板脚本统一使用 Python（不再用 PowerShell）。
- 删除纪律：`_trash/` 临时删除区（命名 = `<agent产品名>_<YYYY-MM-DD>_<HHMM>`，
  如 `codex_2026-08-25_2330`；不设固定 agent 列表）+ 整轮进回收站。
- 经验文档放 `private/dev/`，完整条目、不预设沉淀位置。
- 工作区不建 private 子 git（避免与模板 private 骨架混淆）。
- 母项目不设 EXPERIENCE-TO-TEMPLATE 暂存：可复用进模板的经验直接改进
  `project-template/` 与 `skills/init-project/`；可进知识库的经验记于
  `docs/EXPERIENCE-TO-KB.md`，不混入模板内部。
- 工作区根补 `.gitattributes`（LF 归一化，与模板一致；P3 #6 落地）。
- 模板【通用】模块补「项目归档/退役」流程与 `dist/` 发布产物目录约定
  （P3 #7 + 产物治理落地）。
- 模板实体目录：`dist/`（C 区占位 `.gitkeep`）与 `archive/`（A 区归档说明
  `ARCHIVE.md`）**随模板初始化即存在**，不搞懒加载/约定式；目录树、三区表、
  归档流程显式引用。
- 测试落地指引：新增 `project-template/docs/TESTING.md`（pytest 示例、覆盖率、
  CI 接入、TEST-REPORT 对应），`ci_check.py` 内含接入示例注释。
- agent 安装目标：六处（codex / dsh / workbuddy / trae-cn / qwenworkcn / qoder-cn），
  由 `install-targets.json` 单一事实来源承载 + `verify_installed_copies.py` 全量
  哈希+版本哨兵校验（qwenworkcn 替换原 qoderworkcn，P1-1）。
- agent 提问与共识确认机制（红线 17，2026-08-27）：禁面板（禁止问题面板/选择面板类
  UI）/ 回答≠确认（回答=新信息输入并重检问题空间）/ 共识快照+逐项表态 / 反定型 6 项
  关键/风险节点展示（平时内部思考）/ 确认不锁定（需求阶段内新信息可回审，PRD 定稿
  后走变更流程=开新 PRD 取代）；本工作区按轻量流程实施（不建 DESIGN 文件，ADR-0001
  确认后直接进入实现）；详见 `docs/ADR-0001-agent-questioning.md`。

## 文档职责

| 文件 | 模块 | 职责 |
|---|---|---|
| `AGENTS.md`（本文件） | 混合 | 工作区专属规范入口 |
| `README.md` | 项目专用 | 面向使用者的说明 |
| `docs/STATUS.md` | 项目专用 | 当前状态快照（阶段卡 + 生命周期合规清单 + 影响清单；历史由 git 承担） |
| `docs/FLOW.md` | 混合 | 流程与状态机总图（主流程 + 每阶段子流程 + 动作状态机，mermaid） |
| `docs/USER-GUIDE.md` | 混合 | 面向人的阶段流程简明指南（防遗忘） |
| `docs/LOADING.md` | 混合 | 加载规则表全量版（渐进式披露协议） |
| `docs/CHANGELOG.md` | 项目专用 | 模板版本变更历史（升级比对依据） |
| `docs/EXPERIENCE-TO-KB.md` | 项目专用 | 可沉淀进知识库的经验（完整条目） |
| `install-targets.json` | 项目专用 | 机器可读安装表：两 skill 在各 agent 用户级 skill 目录的位置（单一事实来源） |
| `scripts/sync_template.py` | 项目专用 | 同步脚本（project-template/ → skills/init-project/assets/ + 全链校验） |
| `scripts/verify_installed_copies.py` | 项目专用 | 安装副本校验：读安装表 → 逐目录 × 逐 skill 全量 SHA-256 + 版本哨兵（随 sync 并入发版链） |
| `project-template/` | 通用 | 权威模板（同步到 `skills/init-project/assets/`） |
| `project-template/private/dev/PHASES.md` | 通用 | 阶段模块权威定义（I/O/产物/生命周期/16节点映射/切换规则/需求引导/文档映射） |
| `skills/` | 通用 | skill 目录（`init-project/`：初始化 skill；`agent-rules/`：精简版全局规范） |
| `skills/init-project/SKILL.md` | 通用 | 初始化 skill（SKILL.md / references / scripts / assets） |
| `skills/init-project/references/` `scripts/` `assets/` | 通用 | 初始化 skill 承载（init-steps.md / init_project.py / assets/project-template/ 模板镜像） |
| `skills/agent-rules/SKILL.md` | 项目专用 | 精简版 agent 全局行为规范（仅非项目且非纯聊天对话加载） |
| `skills/agent-rules/references/inheritance-map.md` | 项目专用 | 继承矩阵：模板红线 ↔ 精简条目 + 正文指纹（sync 校验依据） |
| `skills/agent-rules/references/audit-checklist-lite.md` `agents/` | 项目专用 | 精简审计清单 / 平台接口描述 |
