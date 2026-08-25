# init-project — 初始化执行细节（init-steps.md）

> 按 SKILL.md「执行流程」加载本文件。本文件提供参数表、占位符清单、校验清单与
> 常见问题；脚本与模板本身以 `assets/project-template/` 与 `scripts/init_project.py`
> 为准。

## 1. 参数收集表

| 参数 | 必填 | 默认 | 说明 |
|---|---|---|---|
| 目标目录 | 是 | — | 空目录（或仅含用户声明保留的文件）；路径先规范化再确认 |
| 项目名（`--name`） | 是 | 目录名 | kebab-case（小写字母、数字、连字符） |
| 描述（`--desc`） | 推荐 | 同项目名 | 一句话定位，写入 README 与 AGENTS.md |
| 远端 URL（`--remote`） | 否 | — | GitHub 等 git 远端；**设置了也不自动 push** |
| 默认分支（`--branch`） | 否 | `main` | 主仓库初始分支；同步替换工作流中的分支名 |
| 作者（`--author`） | 否 | git 全局配置 | 用于 LICENSE 与提交署名；全局配置也取不到时回退为
  `Your Name`（占位，初始化后请用户修改 LICENSE） |
| 许可（`--license`） | 否 | `mit` | 当前内置 MIT；其他许可用 `--license-file` 提供 |
| 自定义许可（`--license-file`） | 否 | — | 自定义 LICENSE 文件路径，替换模板 LICENSE
  （文件中的 `{{YEAR}}`/`{{AUTHOR}}` 占位符同样会被替换） |
| 自动发布（`--auto-release`） | 否 | 关闭 | 开启「每次改动完成后自动发布」；默认
  不自动发布（用户确认后执行发布流程） |
| 仅复制（`--no-git`） | 否 | — | 只复制+替换，不创建 git 仓库（需用户另行决定 git 方案） |
| 模板目录（`--template`） | 否 | skill 内嵌模板 | 用自定义模板目录替代（主要用于测试/定制） |

> **非空目录**：目标目录已存在且非空时脚本**拒绝**执行（列出已有文件）——这是
> 「不覆盖已有文件」红线的强制实现。处理方式：选择空目录，或先与用户确认保留
> 清单、由 agent 把保留文件移出/合并后再初始化。**没有 --force 开关**。

## 2. 占位符清单（脚本自动替换）

| 占位符 | 替换为 |
|---|---|
| `{{PROJECT_NAME}}` | 项目名 |
| `{{PROJECT_DESCRIPTION}}` | 一句话描述 |
| `{{DEFAULT_BRANCH}}` | 默认分支名 |
| `{{AUTHOR}}` | 作者 |
| `{{YEAR}}` / `{{DATE}}` | 当前年份 / 当前日期（YYYY-MM-DD，写入 CHANGELOG 与 TEST-REPORT） |
| `{{VERSION}}` | `version.json` 的 `version` 字段内容（初始 `0.0.1`，版本规则见模板 AGENTS.md「版本管理」） |
| `{{LICENSE_NOTICE}}` | 许可声明（默认「本项目使用 MIT 许可，详见 LICENSE。」） |
| `{{AUTO_RELEASE}}` | 发布策略（默认「不自动发布，用户确认后发布」；`--auto-release` 为「每次改动完成后自动发布」） |

> 校验方法：初始化后在目标目录运行
> `git grep -n -E '\{\{[A-Z_]+\}\}'`（只匹配模板占位符；GitHub Actions 的
> `${{ ... }}` 表达式属正常内容），结果应为空。

## 3. 脚本用法

```bash
python <skill>/scripts/init_project.py <目标目录> \
  --name my-app --desc "我的应用" \
  [--remote git@github.com:user/my-app.git] \
  [--branch main] [--author "Name"] \
  [--license mit] [--license-file PATH] [--auto-release] \
  [--no-git]            # 只复制+替换，不创建 git 仓库
  [--template PATH]     # 自定义模板目录（默认 skill 内嵌模板）
```

脚本行为（顺序）：

1. 校验目标目录：不存在则创建；非空时报错并列出已有文件（要求用户确认保留清单）。
2. 复制 `assets/project-template/` 全部内容（跳过 `.git`、`__pycache__`、
   `.DS_Store`）。
3. 全文件替换占位符（UTF-8；二进制文件跳过）。
4. 默认初始化 git：主仓库 `git init -b <branch>` + `git add -A` + 首次提交
   `chore: init from universal project template`；`git -C private init` + 提交
   `docs: private v0.0.1 - init`。失败（git 不可用）时警告并继续，由 agent 收尾。
5. 打印汇总与下一步。

## 4. git 收尾（脚本 `--no-git` 或 git 步骤失败时）

```bash
git init -b main                      # 主仓库（分支按参数）
git add -A -- .
git commit -m "chore: init from universal project template"
git -C private init                   # private 子 git
git -C private add -A -- .
git -C private commit -m "docs: private v0.0.1 - init"
```

- 主仓库与 private 子 git **分别独立**（`private/.git` 是独立仓库，主仓库的
  `.gitignore` 忽略整个 `private/`，互不嵌套跟踪）；两者初始分支均为
  `--branch` 指定的分支名（默认 `main`）。
- 配置远端（用户确认后）：`git remote add origin <URL>`；**推送必须另行征得同意**。

## 5. 校验清单（初始化后必做）

- [ ] `private/.git` 与主仓库 `.git` 均存在（除非 `--no-git`）
- [ ] 占位符无残留（`git grep -n -E '\{\{[A-Z_]+\}\}'` 为空；GitHub Actions 的
      `${{ }}` 表达式除外）
- [ ] `private/dev/CHANGELOG.md` 顶部与 `private/dev/TEST-REPORT.md` 日期已由脚本
      自动填写为初始化当天（`{{DATE}}` 占位被替换）
- [ ] 主仓库 `git status` 干净；`git -C private status` 干净
- [ ] `git check-ignore private/` 命中（`.gitignore` 生效）
- [ ] `archive/ARCHIVE.md` 已生成（A 区归档区说明；未归档时保持默认内容）
- [ ] `dist/.gitkeep` 已生成（C 区发布产物占位；`git check-ignore dist/<任意文件>`
      命中、`git check-ignore dist/.gitkeep` 不命中）
- [ ] `docs/TESTING.md` 已生成（测试落地指引：pytest 示例 / 覆盖率 / CI 接入 /
      TEST-REPORT 对应）
- [ ] 根 `AGENTS.md` 存在且 `{{PROJECT_NAME}}` 已替换
- [ ] `private/AGENTS.md` 存在（版本为 `0.0.1`，待用户补充「本机环境」「用户决策」）
- [ ] `version.json`：`version` = `0.0.1`；`private/dev/CHANGELOG.md` 顶部 = `v0.0.1`
- [ ] `version.json`：`template_version` 与 skill/模板版本一致（以
      `assets/project-template/version.json` 的 `template_version` 字段为准）
- [ ] `private/dev/WORKLOG.md`、`EXPERIENCE-TO-TEMPLATE.md`、`EXPERIENCE-TO-KB.md`
      已生成（阶段落盘与经验沉淀载体）
- [ ] `private/dev/prd/INDEX.md`、`private/dev/rfc/INDEX.md`、
      `private/dev/adr/INDEX.md`、`private/dev/research/INDEX.md` 已生成
      （开发前四登记册：状态机/编号规则/模板骨架）
- [ ] `private/dev/WORKLOG.md`「当前任务」含「流程位置」字段
- [ ] `private/AGENTS.md`「发布策略」已按所选模式生成（默认不自动发布；
      `--auto-release` 为自动发布）
- [ ] `scripts/ci_check.py` 可运行（`python scripts/ci_check.py` 退出码 0）
- [ ] `scripts/check_dev_docs.py` 可运行（`python scripts/check_dev_docs.py`
      退出码 0；空登记册应通过）
- [ ] `scripts/pre_release_check.py` 可运行（当前状态应提示「可以发布」或仅警告
       CHANGELOG 已就绪后通过；占位检查未实现时会失败，可用 `--allow-placeholder`
       临时放行）
- [ ] `scripts/trash.py` 可运行（`python scripts/trash.py --help` 退出码 0）

## 6. 常见问题

| 问题 | 处理 |
|---|---|
| 目标目录非空 | 脚本拒绝并列出已有文件；选择空目录，或与用户确认保留清单后由
  agent 移出/合并再初始化（无 --force） |
| Python 不可用 | 模板脚本需要 Python 3.9+（仅标准库）；提示用户安装 Python 或改用
  `--no-git` 后手动复制 |
| git 不可用 | `--no-git` 只复制文件；告知用户后续手动 `git init` 的步骤 |
| 用户已有同名远端仓库 | 不推送；提示用户选择（新仓库 / 先清空远端 / 改名） |
| Windows 路径/权限 | 用绝对路径；脚本失败时提示用管理员权限或换目录 |
| 用户要求其他许可 | 用 `--license-file <路径>` 提供自定义 LICENSE（文件中的
  `{{YEAR}}`/`{{AUTHOR}}` 会被替换），并在 `private/AGENTS.md`「用户确认的设计决策」
  记录 |
| 初始化后想改项目名 | 直接改 `README.md` 与 `AGENTS.md` 顶部标题；`version.json` 的 `version` 不受影响 |

## 7. 初始化完成后的落地路线图（分阶段）

> 初始化当场（脚本 + 第 5 节校验清单）只保证「骨架就绪」；项目真正可用还需要
> 按下列阶段落地。每个阶段完成后更新 `private/dev/WORKLOG.md`（阶段落盘）。

### 阶段 1 · 首个开发会话前（文档填空，一次做完）

- `README.md`：功能特性、快速开始、项目结构、许可（按项目实际填写）。
- `private/AGENTS.md`：「本机环境」「安装目标/部署目标」必填；「用户确认的设计
  决策」（D-001…）与「定案清单」「必须询问人类清单」按首个需求逐步补。
- `private/dev/DESIGN.md`：项目形态、核心设计、关键不变量、改动影响面定位表。
- `private/dev/CHANGELOG.md` / `private/dev/TEST-REPORT.md` / `private/dev/WORKLOG.md`：
  脚本已生成初始化条目，此后随开发/发布更新。
- `private/dev/EXPERIENCE-TO-KB.md` / `private/dev/EXPERIENCE-TO-TEMPLATE.md`：
  脚本已生成骨架；每轮对话结束写入完整候选经验。
- `docs/audit-checklist.md` / `docs/UPGRADE.md` / `docs/DOCS.md`：模板自带，
  按需阅读使用（实施后审计 / 模板升级 / 文档治理）。
- `private/dev/prd/INDEX.md` / `rfc/INDEX.md` / `adr/INDEX.md` /
  `research/INDEX.md`：模板自带登记册（状态机/编号/模板骨架）；首个 M/L 需求时
  按它创建文档（S 档可跳过）。

### 阶段 2 · 首个功能开发前（实现 CI，一次做完）

1. 按 `docs/TESTING.md` 落地测试：创建 `tests/`、写首批用例、本地跑通
   （`python -m pytest`，其他技术栈等价）；
2. 实现 `scripts/ci_check.py`：按项目技术栈填入真实 lint / build / test，并移除
   `__CI_CHECK_PLACEHOLDER__` 标记（`scripts/pre_release_check.py` 会拦截占位）；
3. 更新 `.github/workflows/ci.yml`：按技术栈补 setup / 依赖安装 / 检查步骤
   （文件内已有示例注释）；
4. 跑通 `python scripts/ci_check.py`，结果记入 `private/dev/TEST-REPORT.md`。

### 阶段 3 · 首个需求（走开发工作流）

档位判定（S/M/L，与用户确认）→ M/L 档走**开发前门禁**：调研（`RESEARCH-XXXX`
或内嵌）→ PRD 定稿（`private/dev/prd/PRD-0001-*.md`）→ RFC 评审（可选）→
ADR 记录（架构级）→ DESIGN 吸收 → `private/AGENTS.md` D-001 摘要 +
`详见 ADR-XXXX` → `private/dev/WORKLOG.md` 切换当前任务并记录「流程位置」→
实施（阶段落盘）→ 按 `docs/audit-checklist.md` 审计 → 提交。

### 阶段 4 · 首次发布

按根 `AGENTS.md`「发布流程」：`scripts/bump_version.py` 递增版本 → 更新
`private/dev/CHANGELOG.md` 顶部 → `scripts/pre_release_check.py` 发布前检查 →
主仓库提交/推送 → tag + Release（首次 push 不自动发 Release，见
`.github/workflows/release.yml` 说明；手动/自动二选一）。

### 阶段 5 · 立项类话题（持续）

与 agent 讨论项目思路/需求/架构/功能/产品时，要求 agent 优先在 GitHub 调研现成
参考并提醒「先调研再立项」（模板 `AGENTS.md` 红线 13），避免从零造轮子。
正式调研结果落 `private/dev/research/RESEARCH-XXXX`（或内嵌 PRD/RFC 对应节）。

### 文档时机速查

| 文档 | 初始化（脚本） | 首次开发前 | 开发中 | 每次发布 |
|---|---|---|---|---|
| `README.md` | 骨架 | 填写 | 随用户视角改动更新 | 核对 |
| `private/AGENTS.md` | 骨架 | 填环境/安装目标 | 决策/定案/询问清单随需求补 | 核对 |
| `private/dev/DESIGN.md` | 骨架 | 填项目形态/核心设计 | 设计变化时更新 | 核对 |
| `private/dev/WORKLOG.md` | 初始化条目 | — | **每小阶段更新** | 收口 |
| `private/dev/CHANGELOG.md` | v0.0.1 条目 | — | 变更要点 | **顶部新增条目** |
| `private/dev/TEST-REPORT.md` | 初始化条目 | 记 CI 落地结果 | 测试变化时更新 | **必更新** |
| `private/dev/EXPERIENCE-TO-*.md` | 骨架 | — | **每轮对话结束写入** | 提醒沉淀 |
| `private/dev/prd/INDEX.md` 等四登记册 | 模板自带 | 阅读登记册规则 | 每个 M/L 需求按状态机维护 | 核对（`check_dev_docs.py`） |
| `docs/TESTING.md` | 模板自带 | 按它落地测试 | 测试体系变化时更新 | 核对 |
| `version.json` | 0.0.1 / 模板版本 | — | — | **bump** |
