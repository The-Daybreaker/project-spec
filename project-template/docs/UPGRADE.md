# 模板升级指南（UPGRADE.md）

> 模块：全通用。
> 用途：通用项目模板发布新版本后，指导存量项目应用新版本。

## v1.6.0 断代说明（重要）

v1.6.0 是**断代版本**：文档架构整体重建——每条规范事实只有一个家（事实台账 +
`FACT/REF/INJECT` 锚点 + 漂移免疫门禁）、流程图并入阶段定义、用户手册并入
README、新增阶段契约（阶段模块化）与测试台账。**v1.6 之前的项目没有平滑升级
路径**，请按新模板重建：

1. 用 init-project 技能在**新目录**初始化新骨架；
2. 迁移项目内容：`src/` 代码、`private/dev/` 登记册与状态文档、`private/test/`
   素材按需复制进新骨架；项目专属内容（README 项目部分、设计决策、本机环境）
   合并进新骨架对应位置；
3. 校验：占位符无残留（`git grep -n -E '\{\{[A-Z_]+\}\}'`）、
   `python scripts/ci_check.py` 与 `python scripts/check_dev_docs.py` 退出码 0、
   `python scripts/pre_release_check.py` 通过；
4. 根 `version.json` 的 `template_version` 更新为 `1.6.0.patch0`，并在
   `private/dev/CHANGELOG.md` 与 `private/dev/STATUS.md` 记录重建。

> v1.6 之前各版本的迁移要点已随断代作废（旧项目一律走重建）；历史细节见本文件
> 的 git 历史。

## 升级流程（v1.6.0 及以后的非断代版本适用）

1. **确认当前模板版本**：读项目根 `version.json` 的 `template_version`。
2. **获取模板变更历史**：读模板仓库根 `CHANGELOG.md`（本地路径或 GitHub URL）。
3. **比对变更**：列出 `template_version` → 目标版本之间所有变更条目；条目若标注
   「断代」，停止升级、按断代说明重建。
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
   退出码 0；`python scripts/check_consistency.py` 退出码 0（事实唯一家/锚点
   完整性）；`python scripts/pre_release_check.py` 通过。
7. **更新版本记录**：项目根 `version.json` 的 `template_version` 改为目标版本。
8. **记录升级**：`private/dev/CHANGELOG.md` 与 `private/dev/STATUS.md` 记录本次升级。

## B 区私有骨架迁移（模板随版本新增/变更的 private/ 骨架）

模板把以下 B 区骨架文件随模板分发（初始化即生成），模板发版也可能**新增**它们；
升级时按此规则处理：

- **新增的骨架文件**（本项目不存在该路径）→ 从新模板对应路径**直接复制**。
- **已存在的同名文件** → **只合并模板新增的字段/小节，绝不覆盖项目已有内容**：
  - `private/dev/STATUS.md`：合并模板新增字段；
  - `private/AGENTS.md`：只应用【通用】小节，【项目专用】内容保持不动；
  - `private/dev/EXPERIENCE-TO-*.md`、`private/dev/CHANGELOG.md`、
    `private/dev/TEST-REPORT.md`：只补模板新增的骨架字段，项目已写内容不动；
  - `private/.gitignore` / `private/PRIVATE.md`：按模板变更合并（如新增忽略规则）。
- **依赖补齐**：模板新增脚本可能依赖新骨架；缺依赖时 `ci_check.py` /
  `pre_release_check.py` 会失败，按上表补齐即可，不是模板缺陷。
- **私有子 git**：升级产生的 `private/` 改动同样走 private 子 git 提交（发布前
  `pre_release_check.py` 自动同步）。

## 升级迁移检查表

每次升级按以下清单核对（**迁移要点以模板 CHANGELOG 对应版本条目为权威**）：

- [ ] 已确认当前 `template_version` → 目标版本之间的全部变更条目（含断代标注检查）
- [ ] 【通用】文件已应用：根/私有 `AGENTS.md` 的【通用】小节、`docs/`、`scripts/`、
      `.github/`、模板资产（`.gitignore` / `.editorconfig` / `.gitattributes` 等）
- [ ] **B 区私有骨架已迁移**：新增的复制、已有的只合并新增字段（见上节）
- [ ] 占位符无残留（`git grep -n -E '\{\{[A-Z_]+\}\}'`）
- [ ] `python scripts/check_dev_docs.py` 退出码 0（登记册 / STATUS 阶段卡字段齐全）
- [ ] `python scripts/check_consistency.py` 退出码 0（事实锚点完整）
- [ ] `python scripts/ci_check.py` 退出码 0
- [ ] `python scripts/pre_release_check.py` 通过
- [ ] 根 `version.json` 的 `template_version` 已更新为目标版本
- [ ] 升级已记录到 `private/dev/CHANGELOG.md` 与 `private/dev/STATUS.md`

### 已知版本迁移要点

- **v1.6.0.patch0**：断代版本——无平滑升级，按文首「v1.6.0 断代说明」重建。
- **v1.6.1.patch0**：新增 `private/dev/design/` 设计契约文件夹（B 区骨架，
  `design/README.md` 直接复制）；DESIGN 补「设计总览与契约索引」节；审计清单
  新增 §11 设计完整性；纯新增不破坏已有内容（契约按需创建、不适用声明落设计总览）。
- （后续版本在此追加；模板 CHANGELOG 为权威）

> 注意：major 版本（如 2.0.0.patch0）升级前，先读新模板的 `AGENTS.md` 了解破坏性
> 变更与迁移方案；涉及红线/工作流变化时，同步核对本项目的私有规范是否需要调整。
