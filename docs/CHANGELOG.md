# CHANGELOG — 通用项目模板 版本变更历史

> 模块：项目专用（工作区）。
> 记录模板自身每次发版变更，与根 `version.json`、git tag 对齐；项目升级时据此比对
> （见 `project-template/docs/UPGRADE.md`）。

## v1.4.2.patch0（2026-08-27）

> 本次发版：第九轮全面审计修复收口——F1（新项目首跑即红）等 5 项发现全修 +
> 修复轮表述面 sweep 新增 6 处同类残留一并清理；新增防再发机制（开箱即用冒烟
> 自检 + 断言面联动核对 + sync 排除项清理）；版本号 `1.4.2.patch0`（普通功能
> 升级/补齐，第 3 段 +1、patchN 归零）。审计报告与根因分析见
> `docs/AUDIT-2026-08-27.md`（§六）。

- **审计修复全链（F1-F5 + 表述面 sweep）**：`check_dev_docs.py` STATUS 断言改合并
  阶段卡合规两行锚点（修复新项目首跑即红）；旧阶段卡表述 9 处全量清理
  （init_project 输出 / init-steps×2 / 两侧 README / 模板 DESIGN×2 / 两侧
  LOADING×2 / init-project SKILL×2）；工作区 FLOW 同步红线 17 状态机；
  PRD-0001 回填实现版本；六处副本重装。
- **防再发机制**：新增 `scripts/smoke_init.py`（开箱即用冒烟自检：初始化 + 回读 +
  冒烟项目内骨架脚本自检四连，发版前必绿）；`AGENTS.md` 维护约定 #10 +
  `README.md` 维护约定（改格式/字段类红线须全量 grep 枚举断言面并零残留）。
- **sync 排除项清理（F5 根因修复）**：`sync_template.py` 镜像前清理 DST 中命中
  排除名（`__pycache__` 等）的残留，杜绝「排除项进镜像即永存」。

## 未发版变更（v1.4.2 之后）

> 以下为 v1.4.2 发布后、尚未发版的累积变更；发版时并入对应版本条目。条目以
> `git log v1.4.2.patch0..HEAD` 记录为准，不固定提交号。

## v1.4.1.patch0（2026-08-27）

> 本次发版：红线 17 提问与共识确认机制 + 阶段卡/合规/反定型合并紧凑模块 + 审计修复
> 收口；版本号 `1.4.1.patch0`（普通功能升级，第 3 段 +1、patchN 归零）。

- **阶段卡/生命周期合规清单/反定型合并模块重设计**：阶段卡改为合并紧凑模块——标题
  含状态（括号内不保留其他内容）、横置阶段线（标签=阶段中文名、当前节点加粗、只显示
  当前阶段节点）、合规两行（✓ 已完成 / ⏳ 待完成，分号分隔）、反定型为**条件块**
  （仅关键/风险节点展示，6 项附内容非仅勾选；非关键节点省略）；去掉「正在完成/已完成/
  下一步」字段；**阶段卡展示只用中文名称、不显示字母缩写**（保留数字编号）；PHASES
  §5 定义 / STATUS 骨架 / AGENTS 展示规则 / audit-checklist / agent-rules 精简版同步。
- **agent 提问与共识确认机制（红线 17）**：模板【通用】新增红线 17——禁止问题面板/
  选择面板类 UI、回答≠确认（回答=新信息输入并重检问题空间）、聊天内选项仅信息辅助
  不得仅依赖选项推进、共识快照+逐项表态、反定型 6 项关键/风险节点展示（平时内部
  思考）、确认不锁定（PRD 定稿后变更走开新 PRD 取代）；PHASES.md 需求引导方法论/
  阶段卡共识快照块、FLOW.md P1 子流程与需求引导状态机、audit-checklist 检查项同步；
  agent-rules 精简版规范 17 + 继承矩阵指纹；工作区按轻量流程实施（无 DESIGN 文件，
  ADR-0001 直接进入实现）；PRD-0001/RESEARCH-0001/ADR-0001 落于 `docs/`。
- **全面审计修复（第一轮，v1.4.0 发布后）**：
  - check_dev_docs 支持 PRD/RFC「已废弃（由 XX-XXXX 取代）」复合状态 + 读取容错；
  - init_project.py 中文目录名回退 + `{{DATETIME}}` 占位符（时间标签精确到分钟）；
  - 模板骨架 STATUS/EXP/TEST-REPORT 时间标签 `{{DATE}}` → `{{DATETIME}}`；模板
    STATUS 移除冗余「流程位置」小节；
  - 工作区文档路径实例化、AGENTS 加载表补实施/审计/发布场景、`.gitignore` 补
    `.workbuddy/`；六处副本重装。
- **全面审计修复（第二轮，本次）**：
  - 文档可执行性（P1）：`AGENTS.md` / `README.md` 的 quick_validate 校验命令改为
    完整目录路径（`skills/init-project` / `skills/agent-rules`），修复「照文档执行
    必失败」缺陷；
  - 状态文档收口（P2）：`docs/STATUS.md` 硬事实校准（最后更新/阶段卡与仓库实际
    一致）；`docs/CHANGELOG.md` 新增本「未发版变更」区段（与 `git log` 逐条对应）；
    `docs/EXPERIENCE-TO-KB.md` 最后更新时间戳校准 + 本轮审计经验置顶；
  - 细节修复（P3）：`README.md` 目录结构树补 `install-targets.json` 与
    `scripts/verify_installed_copies.py`；`init-steps.md` 校验清单补 `{{DATETIME}}`
    占位符说明；`skills/init-project/agents/openai.yaml` 行尾归一为 LF（与
    `.gitattributes` 一致）；v1.3.2「sync/verify 公共函数不抽取」权衡注记更新；
  - 删除纪律（P2）：清理 `_trash/` 遗留 3 轮 trae 临时删除区（整体进回收站，
    可恢复）；
  - 六处安装副本重装 + 全链验证绿（sync / verify / check_dev_docs /
    quick_validate×2 / py_compile / 冒烟）。
- **版本号体系重新设计（四段式）**：版本号由 `X.Y.Z` 改为 `X.Y.Z.patchN`（第 4 段
  为字面 `patch` + 数字，N 从 0 开始）；递增规则：补丁/小修复升 `patchN`、普通
  功能升级/补齐升第 3 段（patchN 归零）、大功能升级升第 2 段（后两段归零）；
  **前两位（major/minor）增加必须用户确认的现有管理不变**（不新增红线）；
  `bump_version.py` 新增 `--part patchn|patch|minor|major`（默认 `patchn`）；
  模板【通用】机制（bump / pre_release / release.yml / 文档 / skill）全链同步；
  工作区当前版本迁移为 `1.4.0.patch0`、新项目初始 `0.0.1.patch0`；六处副本重装
  + 全链验证。

## v1.4.0（2026-08-26）

> 整体架构重构（模块化改造）试点：需求清单 v1 七条（阶段模块化/可观察性/渐进式披露/
> 中断恢复/用户文档/需求引导方法论/流程图状态机）+ 决策 D1-D15（2026-08-26 引导式
> 讨论定稿，计划见 `<用户主目录>\.workbuddy\plans\<计划名>.md`）。

- **阶段体系模块化（D6/D7/D9/D10）**：16 节点收敛为 5 模块（P1 需求/P2 方案/P3 开发/
  P4 审计验证/P5 交付发布）+ 子阶段两级；决策型须用户确认、执行型展示即走；双维度
  模型（主流程串行 + 贯穿动作不占阶段）。
- **STATUS 快照化（D8/D12）**：WORKLOG → STATUS 改名（日志→状态快照，只存最新、
  历史由 git 承担）；`docs/STATUS.md`（工作区）与模板 `private/dev/STATUS.md` 新建；
  旧 WORKLOG×2 移 `_trash/`。
- **阶段卡 = 合规检查点（D15）**：阶段卡含 📇 进度 + ✅ 生命周期合规清单（文档同步/
  落盘/提交/校验/确认/沉淀逐条勾选）+ 📥 下一阶段输入预告。
- **文档披露渐进式（D3/D5/D11）**：新增 `docs/{FLOW,USER-GUIDE,LOADING}.md` +
  模板版三件 + `private/dev/PHASES.md`；DOCS.md 文档地图扩展 + 加载规则表摘要；
  阶段↔文档映射（披露隔离）；需求引导方法论（禁抛选项）。
- **git 提交节奏（D14）**：每阶段/子阶段完成落盘后即提交（主仓库 + private 子 git），
  提交信息带阶段标识。
- **工程改进**：sync_template.py 增量镜像改造（避免 rmtree 批量删除钩子 + 空目录
  清理）；check_dev_docs.py 新增 STATUS 快照校验；agent-rules description 单行化。
- **验证**：全链绿（sync 源侧 / quick_validate×2 / py_compile / check_dev_docs /
  init 冒烟）+ 发布前独立审计（P0=0/P1=0/P2=2）+ dogfood 一轮（P1→P3→P4 走通，
  阶段卡/STATUS 快照/决策型确认/阶段提交/合规清单均按预期）。

## v1.3.2（2026-08-26）

> 全生命周期专业审计修复版本（patch）：三域并行独立子代理审计（A 规范与文档语言 /
> B 脚本与机制 / C 流程闭环与生命周期），结论「能支撑完整生命周期」，处置
> P1×3 + P2×7 + P3×6 共 16 项；`version.json` 的 `version` / `template_version`
> 与 tag `v1.3.2` 对齐。

### P1 一致性缺陷（照抄模板即失败类）

- **RFC 骨架依据字段补冒号**：`private/dev/rfc/INDEX.md` 示例「依据 PRD-XXXX」→
  「依据 PRD：PRD-XXXX」，与 `check_dev_docs.py` 校验规则对齐；此前新项目照抄
  骨架登记 RFC 必被校验拦截。
- **私有 AGENTS 三区表 A 区补 `archive/`**：v1.2.2 曾声称补齐但实际丢失，本次
  复核补上，与实体目录约定一致。
- **prototype/README 相对路径修正**：`../AGENTS.md` → `../../AGENTS.md`、trash
  脚本路径补 `../../` 前缀（页面原型目录位于 `private/dev/` 下两级）。

### P2 描述准确性 / 流程体验

- **agent-rules 规范 9 溯源标注**：标注「模板红线 9『private 目录纪律』+
  红线 11『密钥安全』合并」，消除精简版条目与模板红线位置一一对应的误解。
- **「工程区」术语入模板根 AGENTS 项目概览**：定义从 `src/.gitkeep` 注释提升至
  规范正文（根目录为工程区，业务代码统一入代码区）。
- **归档约定补 release.yml 自动发布说明**：注明项目归档后 CI 仍会对尚无 tag 的
  当前版本自动发 Release 的现象与机器级防呆思路。
- **工作区 AGENTS 文档职责表补 skill 子文件行**：`init-project/references|
  scripts|assets` 与 `agent-rules/references/*` 不再缺位。
- **pre_release_check 步骤标签补齐**：auto-commit 分支补 `[2/7]`、ci_check 占位符
  提醒行改 `[5/7]` 标签、docstring 步骤清单 5→7 步对齐实际实现、reminder 补
  ci_check 接线提示。
- **init_project --name 默认值规范化**：未指定时目录名经 `_kebab_slug()` 规范化
  并给出提示，消除默认路径下的 kebab-case 告警噪音。

### P3 脚本健壮性

- **check_dev_docs WORKLOG 尾段正则修正**：「当前任务」段位于文末（无后续 `## `
  标题）不再误报缺字段（`(?=\n## )` → `(?=\n## |\Z)`）。
- **pre_release private/ 纵深检查**：status 无输出时追加 `git ls-files -- private`
  兜底，堵住「已提交进主仓库索引且工作树干净」的泄漏盲区。
- **git 子进程输出解码修正**：新增 `_decode()`（Windows 按 mbcs/GBK 解码），中文
  文件名不再乱码导致校验误判。
- **trash.py 支持 `--` 分隔符**：`-` 开头路径不再被当作选项丢弃。
- **pre_release CHANGELOG 读取走 `_read_text`**：编码异常兜底与其余读取点统一。
- **sync/verify 公共函数不抽取**（设计权衡记录）：`_sha256` / `_collect` 等重复
  函数保留各自内联（不抽取公共模块，维持单文件可分发）；同步校验通过
  `sync_template.py` 调用 `verify_installed_copies.check_installed_copies` 并入
  发版链（两脚本均属母项目、不分发目标项目，跨脚本调用可接受）。

## v1.3.1（2026-08-26）

> 维护增强版本（patch）：src/ 代码区实体化与分区约定；`version.json` 的 `version` /
> `template_version` 与 tag `v1.3.1` 对齐。

- **src/ 代码区实体化与分区约定**：`src/` 从文档提及提升为实体代码区
  （`src/.gitkeep` 随初始化存在，A 区进 git）；约定「代码区 = 全部业务源码/资源入
  `src/`（子目录按技术栈自定）、根目录为工程区（AGENTS/docs/scripts/.github/
  private 等），不直接放业务代码」，模板根/私有 AGENTS 项目概览、README 结构树、
  DESIGN 项目形态同步；init-steps 校验清单与 INIT_STEPS_COVERAGE 补 `src/.gitkeep`。

## v1.3.0（2026-08-26）

> 功能增强版本（minor）：新增红线 16「范围克制与纠错清零」+ 图可视化规范
> （先出图再确认：流程图/架构图/页面原型分挂各阶段）+ 工作区 skills 目录合并；
> `version.json` 的 `version` / `template_version` 与 tag `v1.3.0` 对齐。

- **新增红线 16「范围克制与纠错清零（按单办事、不加菜；撤菜不解释）」**：不过度
  添加需求外内容（超出范围先询问用户）；被用户指出的多余内容直接删除，**禁止为
  「未做之事」补写说明**（标题/提交信息/PR/注释/文档中的「已移除多余 X」「为什么
  不需要 X」类表述），避免无用信息堆积污染上下文；确需留痕仅 CHANGELOG 一行
  （模板 `AGENTS.md` 红线区 + `agent-rules/SKILL.md` 规范 16 + 继承矩阵指纹同步）。
- **图可视化规范（流程图 / 架构图 / 页面原型）**：涉及界面/交互、架构/结构、
  流程/状态改动先出图（Mermaid 或 SVG 单文件）→ 向用户展示确认后才执行；分挂各
  阶段（流程图随 PRD/RFC、架构图随 RFC/ADR、页面原型挂设计阶段新增
  `private/dev/prototype/` 目录，README 实体化随初始化存在）；门禁=开发工作流节点
  + 完成检查清单/audit-checklist 双落点；16 节点数不变。
- **skills 目录合并**：`init-project/` 与 `agent-rules/` 并入工作区 `skills/`
  （`skills/init-project`、`skills/agent-rules`）；sync/verify 脚本路径常量、
  install-targets.json source、工作区 AGENTS/README 引用全部更新；已安装副本内容
  与目录名不变、无需重装。

## v1.2.2（2026-08-26）

> 第七轮全面审计修复版本（patch）：P1-1 安装面机制化（安装表机器可读化 + 部署到
> `~/.qwenworkcn` + 六处副本哈希复核）+ P2×4 + P3×7；`version.json` 的 `version` /
> `template_version` 与 tag `v1.2.2` 对齐。

### P2 流程/工具收口

- **P2-1 CHANGELOG 顶部改由 agent 手工更新**：发布流程第 1 步明确为「agent 手工
  更新 CHANGELOG 顶部 + 解释」——脚本不写 CHANGELOG，防止覆盖人工编辑的发布说明
  （`project-template/AGENTS.md` 发布机制与发布流程两处、`release.yml` 头注释、
  `private/AGENTS.md` 发布流程第 1 步）。
- **P2-2 bump_version.py 兜底**：静默漂移告警（版本文件差异即拦截）+ 版本号正则补全 +
  装配解析容错（`version.json` 缺失字段不崩溃）。
- **P2-3 三区表补 `archive/`**：`private/AGENTS.md` 三区表 A 区补归档目录，与实体目录
  约定一致。
- **P2-4 文档/占位状态脚本加固**：`check_dev_docs.py` 两处裸 `read_text` 改走
  `_read_text`（UnicodeDecodeError/OSError 兜底）；`pre_release_check.py` 修复
  **`_ci_check_state` NameError**（被调用未定义）并实现**双向断言**（`PLACEHOLDER_MARKER`
  赋值与 "template placeholder" 输出必须成对存在，任一单边残留即拦截），ci_check /
  CHANGELOG / root_agents 读取失败兜底。

### P3 批量修复（组 B + 组 C）

- **P3-1 knowops 泛化**：模板与工作区 5 处「如 knowops」改为「如适用」
  （`private/AGENTS.md` ×2、`private/dev/DESIGN.md`、`private/dev/EXPERIENCE-TO-KB.md`、
  工作区 `docs/EXPERIENCE-TO-KB.md`）。
- **P3-2 路径/同步健壮性**：`init_project.py` replace_all 绝对路径 `.git` 判定改
  `relative_to().parts`；`sync_template.py` rmtree+copytree 失败兜底（残留镜像待下次
  覆盖）。
- **P3-3 安全/校验收紧**：`pre_release_check.py` SECRET_NAME_RE 收紧（`.env`、私钥/
  证书扩展名、secret/credential/api key 文件名等，避免子串误报）；`init_project.py`
  `_valid_branch` 拦截 `/` 开头分支；`trash.py` 已核实（osascript argv +
  Windows `\\?\` 长路径）。
- **P3-5 模块标注补齐**：`docs/audit-checklist.md`、`private/PRIVATE.md`、
  `private/dev/TEST-REPORT.md`、`private/test/TEST.md`、`README.md` 顶部补模块标注。
- **P3-6 一致性微修**：`audit-checklist.md` §10 字段名对齐「背景与目标/用户与场景」；
  `private/dev/DESIGN.md` 路径风格统一 9 处（去 `dev/` 前缀、`../AGENTS.md`、
  `../../scripts/`）；`rfc/INDEX.md` PRD-0001→PRD-XXXX；`README.md` 结构树补
  `check_dev_docs`；`docs/DOCS.md` 文档清单/地图补齐（ARCHIVE / audit-checklist /
  TESTING / CONTRIBUTING）。
- **P3-7 工作区版本示例更新**：AGENTS.md / README.md grep 示例 `1.1.0 / 1.1.1` →
  `1.1.2 / 1.2.0`（不与 v1.2.2 发版 grep 冲突）。

### P1-1 安装面机制化

- **安装表机器可读化**：新增 `install-targets.json`（两 skill × 六处 agent 目录的
  单一事实来源；`qwenworkcn` 替换原 `qoderworkcn`）+ `scripts/verify_installed_copies.py`
  （逐目录 × 逐 skill 全量 SHA-256 + SKILL.md `metadata.version` 版本哨兵比对）；
  校验随 `sync_template.py` 并入发版验证链——安装状态脱离文档自由文本，副本缺失或
  过时直接拦截发版。
- **安装表更新**：README.md §4 / AGENTS.md 维护约定 #4 改为引用机器可读表；
  安装到 `~/.qwenworkcn/skills` 并清理 `~/.qoderworkcn` 旧副本（替换方案，已确认）。

- **版本递增 v1.2.1→v1.2.2**：根 `version.json`（`version` / `template_version`）、
  `project-template/version.json`（`template_version`）、`init-project/SKILL.md`、
  `agent-rules/SKILL.md` 与 `agent-rules/references/inheritance-map.md` 版本对照
  全部递增到 1.2.2；`AGENTS.md` / `README.md` 当前版本字样同步；UPGRADE.md 补
  v1.2.2 迁移要点（安装表机制化仅母项目脚本、不下发、无迁移动作）。

## v1.2.1（2026-08-26）

> 维护收口版本（patch）：升级路径补齐（B 区私有骨架迁移）+ P3 批量修复 + 流程
> 展示/初始化流程增强；`version.json` 的 `version` / `template_version` 与 tag
> `v1.2.1` 对齐。

- P3 批量修复（全面审计第五轮后续；T5 属约束增强，按用户要求跳过）：
  ① T2 `project-template/private/.gitignore` 补 `test/**/staging-repo/`（与
  `private/test/TEST.md` 描述一致）；② T3 `--auto-release` 与红线 2 衔接明确——
  「自动发布视为用户对发布/推送的预授权，红线 2 对常规发布视为已满足；破坏性
  变更、永久删除等仍须单独确认」（根 AGENTS.md 版本管理、`init_project.py`
  自动发布文案、init-steps 参数表同步）；③ T4 init-steps FAQ「Python 不可用」
  表述纠正（`--no-git` 不能绕过脚本，只能人工复制/换机器）；④ T6 `.gitattributes`
  `*.ps1` / `*.bat` 行尾改为 LF（与 `.editorconfig` 一致；工作区与模板同步）；
  ⑤ T7 `ci_check.py` / `pre_release_check.py` 子进程调用改 `sys.executable`
  （提升仅有 `python3` 环境的可移植性）；⑥ T8 清理六处副本与工作区
  `__pycache__`（重装后各 40 文件逐文件哈希一致）。
- UPGRADE 升级路径补齐（全面审计第五轮 P2·T1）：`project-template/docs/UPGRADE.md`
  新增「B 区私有骨架迁移」规则（新增骨架直接复制、已有同名文件只合并模板新增
  字段、依赖补齐、私有子 git 同步）与「升级迁移检查表（按版本）」（含 v1.2.0
  已知迁移要点：四登记册 INDEX ×4 复制 / WORKLOG「流程位置」字段合并 /
  `check_dev_docs.py` 依赖补救）；回读校验补 `check_dev_docs.py` 步骤——解决
  「既有项目按【通用】规则升级会漏建 B 区骨架，导致 `ci_check` /
  `pre_release_check` 升级后失败且无补救说明」的缺口。
- 流程提示补充「缩写附中文翻译」要求：模板 `private/AGENTS.md`「流程提示」新增
  强制规则 + 「缩写对照」表（PRD=产品需求文档 / RFC=技术方案文档 /
  ADR=架构决策记录 / RESEARCH=调研记录 / DESIGN=设计文档 / WORKLOG=工作进度日志 /
  CHANGELOG=变更日志 / TEST-REPORT=测试报告 / CI=持续集成 / CD=持续交付）；
  根/私有 AGENTS、DESIGN、WORKLOG 流程位置字段、agent-rules 工作流同步；
  init-project SKILL 摘要同步。
- 16 节点流程清单补充「文档更新流程（贯穿全程）」小节（文档就绪 / 发布前文档
  检查 / 状态文档收口 / 文档治理注释）；根 AGENTS 摘要、DESIGN 同步
  （全面审计 P1 落地）。
- init-project **初始化流程更新**：`init_project.py` 打印「下一步」补开发前
  登记册 / 流程提示 / 缩写中文翻译提示；SKILL 执行流程校验清单补四登记册 /
  `check_dev_docs.py` / WORKLOG 流程位置，前置确认补调研落点 RESEARCH；
  `init-steps.md` 校验清单补「流程提示/缩写对照」特性核对、落地路线图阶段 1
  补流程提示说明（全面审计后续）。
- 工作区 AGENTS 维护约定 #9 / README dogfood；六处副本重装（同版本内容更新）。

## v1.2.0（2026-08-26）

> 本版为「项目开发前阶段」规范大版本：新增 PRD/RFC/ADR/RESEARCH 四登记册体系、
> 状态机三层约束、流程提示；`version.json` 的 `version` / `template_version` 与
> tag `v1.2.0` 对齐（minor 升版，用户已确认）。

- **开发前规范（PRD/RFC/ADR/RESEARCH 四登记册）**：模板新增
  `private/dev/{prd,rfc,adr,research}/`（各含 INDEX.md：状态机/编号规则/模板骨架/
  索引），覆盖「开发前」阶段——需求（PRD：背景/范围/验收/优先级 P0-P3，定稿
  门禁）、方案（RFC：候选对比，评审后冻结）、决策（ADR：Nygard 模板，只增不改）、
  调研（RESEARCH：红线 13 结果，发现记录追加+结论可覆盖）；编号跨版本连续不重用；
  PRD INDEX=需求登记册（草稿=待办/已定稿=排期/已实现=完成/已废弃=放弃，按状态+
  优先级排序）；已定稿 PRD 变更开新 PRD 取代；开发前门禁贯穿每个 M/L 需求
  （S 档可跳过）。
- **文档治理扩展**：`private/dev/prd|rfc|adr|research/` 为**历史文档区**（唯一
  允许正文留史；PRD/RFC 定稿冻结、ADR 只增不改、RESEARCH 发现记录只追加）；
  其余正文仍「即当前状态」；根/私有 AGENTS、DOCS、DESIGN、CONTRIBUTING、
  audit-checklist（新增第 10 节）、PRIVATE、README 同步。
- **状态机三层约束**：流程层（工作流显式状态更新动作 + 状态变更权限：定稿/采纳/
  废弃须用户确认，已实现由 agent 自动更新）；检查层（完成清单 + audit-checklist
  开发前文档一致性）；工具层（新增 `scripts/check_dev_docs.py`：编号连续/元数据
  枚举/状态机规则/INDEX 与正文一致/D-xxx→ADR 交叉引用/WORKLOG 流程位置字段；
  并入 `ci_check.py` 与 `pre_release_check.py` 发布前必跑）。
- **流程提示**：16 节点两阶段清单（开发前 01-09 / 实施交付 10-16）；每次实质
  回复/阶段落盘/上下文恢复/收尾展示流程位置（当前节点/已完成/下一步），以
  `private/dev/WORKLOG.md`「流程位置」为单一真相；模板 WORKLOG 新增该字段；
  agent-rules 工作流补「长流程任务每次汇报展示进度位置」通用原则。
- init-project 同步：SKILL 摘要补开发前规范/流程提示；`init-steps.md` 校验清单
  补四登记册 INDEX 与 `check_dev_docs.py` 生成检查、落地路线图阶段 3 升级为
  「开发前门禁」、文档时机速查表补登记册行。
- agent-rules 同步：规范 11 补「历史文档区例外」原则；继承矩阵红线 12 指纹更新、
  「不继承」列表登记四登记册/`check_dev_docs.py`/WORKLOG 流程位置字段。
- sync 校验扩展：`INIT_STEPS_COVERAGE` 新增四登记册 INDEX 与 `check_dev_docs.py`
  五条路径。
- 工作区同步：根 `AGENTS.md` / README 版本号校准为 1.2.0（发版同步）；工作区
  WORKLOG 新增「流程位置」字段（dogfood）。

- init-project 覆盖度修复（v1.1.2 发版后审计发现）：`references/init-steps.md`
  校验清单补
  `archive/ARCHIVE.md`、`dist/.gitkeep`（含 ignore 规则校验：`dist/<任意文件>`
  命中、`.gitkeep` 不命中）与 `docs/TESTING.md` 生成检查；初始化后建议引用测试
  落地指引。
- 工作流缺陷修复：`scripts/sync_template.py` 新增 `INIT_STEPS_COVERAGE` 校验——
  模板关键文件未同步到 `init-steps.md`（校验清单/常见问题/落地路线图）时 sync
  直接失败，把「改模板 → 同步 skill 承载文档」从人工特性核对升级为工具强制；
   `init-steps.md` 第 7 节升级为「初始化后落地路线图」（阶段 1 文档填空 / 阶段 2
  实现 CI / 阶段 3 首个需求 / 阶段 4 首次发布 / 阶段 5 立项调研 + 文档时机速查表），
  明确「何时写/何时更新各模板文档」与「实现 CI 的时机与步骤」。

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
