# RESEARCH-0002 — 红线可验证性与推送前安全门禁调研（调研记录）

> 状态：完成（草稿阶段调研）| 日期：2026-08-27 | 关联：PRD-0002
> 位置说明：本工作区（母项目）无 `private/dev` 登记册，RESEARCH 落于 `docs/`；
> 模板骨架（`project-template/private/dev/research/`）保持不动。

## 背景与问题

PRD-0002（红线与要求可验证性改造）涉及两个技术前提，先调研确认：

1. 推送前安全门禁的形态与必要性（本地钩子 vs 发布链 vs 持续集成）；
2. 版本化 git 钩子的分发方式（钩子不随 clone 分发）；
3. 现成扫描工具（gitleaks 等）与模板「零依赖自研扫描器」的关系；
4. 「要求可验证」是否与需求工程标准一致。

## 发现记录

### 发现 1：持续集成兜底对密钥泄漏「太晚」（2026-08-27，多来源）

- DevOps.com《Shift Left to the Developer's Machine》：没有本地门禁时，密钥在持续
  集成介入前就已到达远端；本地门禁在提交离开开发者机器前拦截；「本地钩子抓错、
  持续集成执行策略」。
- zwischen 设计文档（GitHub）：明确决策「pre-push 而非 pre-commit、而非仅持续
  集成」——持续集成扫描对密钥太晚，一旦 push 就在远端历史里；pre-push 是折中
  （pre-commit 太频繁，只扫待推送 diff）。
- 服务器端 pre-receive 钩子（Pricefx/GitLab 案例）能「入库前拒绝」，但依赖托管
  平台能力，GitHub 对普通仓库不提供自定义 pre-receive。
- **结论**：本地推送前门禁是必要防线；持续集成只能兜底。验证了 PRD-0002 三层
  门禁（本地推送钩子 + 发布链 + 持续集成兜底）的设计。

### 发现 2：版本化钩子的标准方式是 `core.hooksPath`（2026-08-27）

- git 文档（githooks(5)）：`core.hooksPath` 可将钩子目录指向仓库内版本化目录；
  pre-push 在推送前调用，可用于阻止推送。
- 社区模板实践（duclos-cavalcanti/templates 等）：钩子要随项目分发只能靠
  git template、符号链接或 `core.hooksPath`；本地 `git config core.hooksPath
  <path>` 是最简做法。
- **结论**：模板采用 `.githooks/pre-push` 目录 + 初始化脚本（`init_project.py`）
  配置 `core.hooksPath`；母项目同样启用。

### 发现 3：扫描工具生态（gitleaks / trufflehog / pre-commit 框架）

- gitleaks 可接 pre-commit/pre-push 钩子；AutoGPT 等仓库用 gitleaks + 白名单
  （`.secrets.baseline`、忽略测试夹具/文档示例）实践成熟。
- 这些工具多为独立二进制/第三方依赖；模板脚本约束为 stdlib-only、Python 3.9+。
- **结论**：保留自研 `scan_secrets.py`（零依赖、中文内容模式、与模板发布链同构），
  在 `docs/TESTING.md` / 模板文档中把 gitleaks 列为**可选增强**（不引入依赖）。

### 发现 4：「要求可验证」是需求工程标准属性

- 需求工程教材（Wiegers & Beatty，Oregon State 开放教材）：好需求应具备
  correct / unambiguous / complete / consistent / verifiable / modifiable /
  traceable 等属性；验收标准用于判定完成（Definition of Done）。
- 敏捷实践（DoR/DoD）：DoD 含「测试通过、验收标准达成、证据附带、文档更新」；
  验收标准以「给定…当…则…」格式可测。
- **结论**：PRD-0002 的「要求三要素（意图/展示/验收）」与行业标准一致——不是
  模板自创的怪规则，而是把需求工程「可验证 + 可追溯」显式化到 agent 协作语境。

## 结论与建议

1. 推送前门禁：本地 pre-push 钩子（`core.hooksPath`）为必要防线；发布链
   （pre_release_check 集成内容扫描）为模板强制门禁；持续集成仅兜底。
2. 扫描器：继续自研 stdlib 扫描器；gitleaks 等仅文档推荐（可选）。
3. 三要素元规范：与需求工程标准一致，可落地为模板红线 1。

