# 模板升级指南（UPGRADE.md）

> 模块：全通用。
> 用途：当通用项目模板发布新版本后，指导 agent 将本项目从旧模板版本升级到新版本。

## 升级流程

1. **确认当前模板版本**：读项目根 `version.json` 的 `template_version`。
2. **获取模板变更历史**：读模板仓库根 `CHANGELOG.md`（本地路径或 GitHub URL）。
3. **比对变更**：列出 `template_version` → 目标版本之间所有变更条目。
4. **只应用【通用】模块**：根/私有 AGENTS.md、`docs/`、`scripts/`、`.github/`、
   模板资产（`.gitignore` / `.editorconfig` / `.gitattributes` 等；
   `scripts/version-sync.json` 位于 `scripts/`）；
   **【项目专用】模块**（README、DESIGN 的项目内容、CHANGELOG/TEST-REPORT/STATUS、
   经验文档、本机环境、用户决策等）**绝不覆盖**。
   **例外——B 区私有骨架**：`private/` 内随模板分发的**骨架文件**也属于模板内容，
   升级时必须同步（新增的直接复制、已有的只合并模板新增字段，**不覆盖项目已有
   内容**），见下节「B 区私有骨架迁移」——否则会漏建登记册/漏加字段，导致
   `ci_check.py` / `pre_release_check.py` 升级后直接失败。
5. **应用方式**：逐条人工/agent 合并（把新模板对应文件复制进本项目后按需调整）。
   「模板仓库」指通用项目模板工作区（母项目）：它在修改模板后运行
   `python scripts/sync_template.py` 保证两份副本一致；**目标项目内没有该脚本**，
   升级时直接复制新模板文件即可，无需也不能运行它。
6. **回读校验**：占位符无残留（`git grep -n -E '\{\{[A-Z_]+\}\}'`）；脚本可运行
   （`python scripts/ci_check.py` 退出码 0）；`python scripts/check_dev_docs.py`
   退出码 0（登记册/STATUS 阶段卡字段，见「B 区私有骨架迁移」）；
   `python scripts/pre_release_check.py` 通过。
7. **更新版本记录**：项目根 `version.json` 的 `template_version` 改为目标版本。
8. **记录升级**：`private/dev/CHANGELOG.md` 与 `private/dev/STATUS.md` 记录本次升级。

## B 区私有骨架迁移（模板随版本新增/变更的 private/ 骨架）

模板把以下 B 区骨架文件随模板分发（初始化即生成），模板发版也可能**新增**它们；
升级时按此规则处理：

- **新增的骨架文件**（本项目不存在该路径）→ 从新模板对应路径**直接复制**（如
  v1.2.0 新增 `private/dev/{prd,rfc,adr,research}/INDEX.md` ×4、`private/test/TEST.md`
  等；v1.3.0 新增 `private/dev/prototype/README.md`）。
- **已存在的同名文件** → **只合并模板新增的字段/小节，绝不覆盖项目已有内容**：
  - `private/dev/STATUS.md`（v1.4.0 起由 WORKLOG.md 改名）：合并模板新增字段
    （如 v1.2.0「当前任务 → 流程位置」、v1.4.0「📇 阶段卡 + 生命周期合规清单 +
    任务影响清单 + 下一阶段输入预告」）；
  - `private/AGENTS.md`：只应用【通用】小节（工作流 / 流程提示 / 缩写对照 /
    文档更新流程 / 文档职责表等），【项目专用】内容（状态/环境/决策/定案清单）保持
    不动；
  - `private/dev/EXPERIENCE-TO-*.md`、`private/dev/CHANGELOG.md`、
    `private/dev/TEST-REPORT.md`：只补模板新增的骨架字段，项目已写内容不动；
  - `private/.gitignore` / `private/PRIVATE.md`：按模板变更合并（如新增忽略规则）。
- **依赖补齐**：模板新增脚本可能依赖新骨架（如 `scripts/check_dev_docs.py` 要求
  四登记册目录与 STATUS「📇 阶段卡」字段存在）；缺依赖时 `ci_check.py` /
  `pre_release_check.py` 会失败，按上表补齐即可，不是模板缺陷。
- **私有子 git**：升级产生的 `private/` 改动同样走 private 子 git 提交（发布前
  `pre_release_check.py` 自动同步）。

## 升级迁移检查表（按版本）

每次升级按以下清单核对（**迁移要点以模板 CHANGELOG 对应版本条目为权威**——模板
发版时会在条目中列出新增/变更文件，逐条对照）：

- [ ] 已确认当前 `template_version` → 目标版本之间的全部变更条目
- [ ] 【通用】文件已应用：根/私有 `AGENTS.md` 的【通用】小节、`docs/`、`scripts/`、
      `.github/`、模板资产（`.gitignore` / `.editorconfig` / `.gitattributes` 等）
- [ ] **B 区私有骨架已迁移**：新增的复制、已有的只合并新增字段（见上节）
- [ ] 占位符无残留（`git grep -n -E '\{\{[A-Z_]+\}\}'`）
- [ ] `python scripts/check_dev_docs.py` 退出码 0（登记册 / STATUS 阶段卡字段齐全）
- [ ] `python scripts/ci_check.py` 退出码 0
- [ ] `python scripts/pre_release_check.py` 通过
- [ ] 根 `version.json` 的 `template_version` 已更新为目标版本
- [ ] 升级已记录到 `private/dev/CHANGELOG.md` 与 `private/dev/STATUS.md`

### 已知版本迁移要点

- **v1.2.0**：新增开发前规范——`private/dev/{prd,rfc,adr,research}/INDEX.md` ×4
  （直接复制）、WORKLOG「当前任务 → 流程位置」字段（合并）、
  `scripts/check_dev_docs.py`（属 `scripts/`【通用】，自动应用）；未迁移时
  `ci_check` / `pre_release_check` 会因缺登记册/流程位置字段失败，按「B 区私有
  骨架迁移」补齐即可。
- **v1.2.1**（维护收口）：UPGRADE.md 补「B 区私有骨架迁移」规则与「升级迁移
  检查表」（应用本文件即可）；`.gitattributes` `*.ps1` / `*.bat` 行尾改 LF（与
  `.editorconfig` 一致）；`scripts/ci_check.py` / `pre_release_check.py` 子进程
  改 `sys.executable`（属 `scripts/`【通用】，自动应用）；`private/.gitignore`
  补 `test/**/staging-repo/`（B 区骨架合并）；根 `AGENTS.md` 版本管理补「自动
  发布视为发布/推送预授权」说明（【通用】应用）。
- **v1.2.2**（第七轮全面审计修复）：安装面机制化属模板母项目内部维护工具
  （`install-targets.json` / `verify_installed_copies.py` 仅母项目 `scripts/`，
  随同步脚本校验，不下发目标项目，**无迁移动作**）；模板内改动：B 区私有文档修订
  （`private/AGENTS.md` 三区表补 `archive/`、knowops 泛化，「已有文件只合并新增
  字段」即可）、`scripts/` 健壮性改动与【通用】流程文档（CHANGELOG 顶部手工更新、
  发布流程说明）自动应用。
- **v1.3.0**（新红线 + 图可视化规范）：新增红线 17「范围克制与纠错清零」（根/
  私有 AGENTS.md 红线区【通用】应用；`agent-rules` 精简版在母项目工作区同步）；
  新增 `private/dev/prototype/README.md`（B 区骨架，页面原型/设计稿目录说明，
  **直接复制**）；根/私有 `AGENTS.md` 开发工作流新增「可视化确认」小节（涉及
  界面/架构/流程改动先出图——流程图随 `prd/` `rfc/`、架构图随 `rfc/` `adr/`、
  页面原型落 `prototype/`，Mermaid/SVG 单文件；未确认不实施）；完成检查清单与
  `docs/audit-checklist.md` 新增图确认检查项（【通用】应用）；无脚本依赖变化
  （`check_dev_docs.py` 仍只管四登记册，`prototype/` 轻量目录不入校验）。
- **v1.3.1**（src/ 代码区实体化与分区约定）：新增 `src/.gitkeep`（A 区代码区
  实体占位，模板资产内**直接复制**）；根 `AGENTS.md` 项目概览与模板 `README.md`
  结构树补「代码区 = 全部业务源码/资源统一入 `src/`（子目录按技术栈自定）、根
  目录不放业务代码」（【通用】应用）；`private/dev/DESIGN.md` 项目形态补代码区
  约定（B 区骨架合并）；init-steps 校验清单补 `src/.gitkeep` 检查项（无脚本依赖
  变化）。
- **v1.3.2**（全生命周期审计修复）：无新增骨架文件；已初始化项目重点核对三处
  「照抄即失败」类修复是否需合并进本项目私有骨架：① `private/dev/rfc/INDEX.md`
  示例行的依据字段格式为「依据 PRD：PRD-XXXX」（带冒号；若项目已自行登记过 RFC
  则只对齐格式、不动已有内容）；② `private/dev/prototype/README.md` 相对路径
  应指向 `../../AGENTS.md` 与 `../../scripts/trash.py`；③ `private/AGENTS.md`
  三区表 A 区含 `archive/`（属【通用】小节，按合并规则应用）。脚本改动
  （`check_dev_docs.py` / `pre_release_check.py` / `trash.py`）与根 `AGENTS.md`
  「工程区」术语、归档 release.yml 说明均属【通用】自动应用；`init_project.py`
  仅母项目使用、不下发目标项目。
- **v1.4.2.patch0**（第九轮审计修复 + 开箱即用自检机制）：已初始化项目迁移要点：
  ① `scripts/check_dev_docs.py` STATUS 快照断言修复为合并阶段卡合规两行锚点
  （v1.4.1+ 项目 STATUS 已是合并格式，无需改 STATUS，同步脚本即可通过），属
  【通用】自动应用；② 模板 `README.md` / `private/dev/DESIGN.md` 骨架 /
  `docs/LOADING.md` 恢复协议的阶段卡描述统一为合并紧凑表述，已初始化项目可选
  对齐本仓库相应文档中的阶段卡描述文字（正文功能无变化）；③ 无新增骨架文件、
  无脚本依赖变化；母项目侧新增（`smoke_init.py` 开箱自检、维护约定 #10 断言面
  联动核对、工作区 FLOW/PRD 状态更新）不下发目标项目。
- **v1.4.1.patch0**（红线 18 提问与共识确认 + 阶段卡合并紧凑模块）：已初始化项目
  迁移要点：① 根 `AGENTS.md` 红线区新增红线 18（提问与共识确认：禁面板/回答≠确认/
  共识快照+逐项表态/反定型关键节点展示/确认不锁定），属【通用】应用；②
  `private/dev/STATUS.md`「📇 阶段卡」改为合并紧凑模块（标题含状态 + 横置阶段线
  当前节点加粗 + 合规两行；反定型为条件块仅关键/风险节点；全中文无缩写），
  `private/dev/PHASES.md` §5 为格式权威定义（已初始化项目合并 §5 变更即可）；③ 阶段卡
  展示全中文、不再展示「正在完成/已完成/下一步」字段；④ 无新增骨架文件、无脚本依赖
  变化；`agent-rules` 精简版规范 17 与进度卡同步属母项目工作区侧。
- **v1.4.0.patch0**（版本号体系重新设计）：版本号由 `X.Y.Z` 改为 `X.Y.Z.patchN`
  （第 4 段为字面 `patch` + 数字，从 0 开始）。已初始化项目迁移要点：① 根
  `version.json` 的 `version` / `template_version` 补 `.patch0`（如 `1.4.0` →
  `1.4.0.patch0`）；② `private/dev/CHANGELOG.md` 顶部条目与格式改
  `## vX.Y.Z.patchN`；③ 后续发版用 `scripts/bump_version.py --part
  patchn|patch|minor|major`（默认 `patchn`，最小单位）；④ 脚本（bump_version /
  pre_release_check / release.yml）与公开文档属 `scripts/`、`docs/`【通用】自动
  应用；⑤ 提交信息与 tag 改 `vX.Y.Z.patchN`。
- **v1.4.0**（整体架构重构：模块化）：**WORKLOG → STATUS 改名**——`private/dev/
  WORKLOG.md` 更名为 `private/dev/STATUS.md`（快照化：只存最新状态，历史由 git
  承担；含「📇 阶段卡 + ✅ 生命周期合规清单 + 任务影响清单 + 下一阶段输入预告」；
  旧 WORKLOG 内容迁移为快照格式，历史条目移 `_trash/` 或由 git 追溯）；新增
  `private/dev/PHASES.md`（阶段模块权威定义：P1-P5 五阶段 + 子阶段 + 16 节点映射 +
  切换规则 + 需求引导方法论 + 阶段↔文档映射，**直接复制**）；新增公开文档
  `docs/{FLOW,USER-GUIDE,LOADING}.md`（流程状态机总图 / 面向人指南 / 加载规则表，
  属 `docs/`【通用】自动应用）；三份 AGENTS.md 瘦身为「摘要 + 加载规则表 + 红线 +
  工作流摘要」（【通用】应用，私有版【项目专用】内容保持不动）；`check_dev_docs.py`
  校验点由 WORKLOG「流程位置」改为 STATUS「阶段卡」（属 `scripts/`【通用】自动
  应用）；每阶段/子阶段完成即 git 提交（阶段卡展示 = 落盘 = 提交）。迁移时旧项目
  把 `WORKLOG.md` 内容按 STATUS 快照模板整理后改名，历史删除走 `_trash/`。
- （后续版本在此追加；模板 CHANGELOG 为权威）

> 注意：major 版本（如 2.0.0.patch0）升级前，先读新模板的 `AGENTS.md` 了解破坏性变更与迁移
> 方案；涉及红线/工作流变化时，同步核对本项目的私有规范是否需要调整。
