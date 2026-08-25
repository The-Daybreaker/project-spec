# WORKLOG — 通用项目模板工作区 工作进度日志

> 模块：项目专用。
> 使用规则：每完成一小阶段先更新本文件与受影响文档；新对话/新任务开始时，若旧内容
> 已完结或文档已膨胀，**先询问用户是否清理**（已完结条目归档到「历史记录」，或整段
> 移入 `_trash/`），得到确认后才清理；绝不自动删除。
- 最后更新：2026-08-26

## 当前任务

- 需求：init-project skill 初始化流程更新（审计后续）：`init_project.py` 下一步
  提示 + SKILL 执行流程/前置确认 + init-steps 校验清单/落地路线图补 v1.2.0
  特性（开发前登记册 / 流程提示 / 缩写翻译 / check_dev_docs）。
- 流程位置：14/16 · 展示与提交（S 档：01 需求提出 → 10 确认开工 直达）；
  已完成：01-13（含全面审计与修复）；下一步：16 沉淀汇报（15 发版 v1.2.1
  由用户决定）。
- 计划步骤：
  1. 自动化验证（✅ 已完成）：sync 36 文件 0 差异 / quick_validate×2 / py_compile /
     init 冒烟 / check_dev_docs / 版本与占位符 grep / 六处副本哈希 全绿
  2. 独立子代理审计（进行中）：只看 diff + audit-checklist，不共享上下文
  3. 人工文档核对（✅ 已完成）：发现并确认 4 处问题——P1：WORKLOG 当前任务陈旧、
     P1：CHANGELOG 版本非新在前；P2：维护约定 9 排在 8 前；P3：init-project
     SKILL 摘要缺「缩写中文翻译」
  4. 修复 + 复检
  5. 阶段落盘 + 提交 + 审计结论汇报

## 阶段记录

| 阶段 | 状态 | 完成内容 | 变更文件 | 验证 | 下一步 |
|---|---|---|---|---|---|
| 1 WORKLOG 修复 | ✅ | 阶段记录 29→28；当前任务切换为本次；旧任务归档历史 | docs/WORKLOG.md | 回读核对 | CHANGELOG |
| 2 CHANGELOG | ✅ | 新增「未发版变更（v1.1.2 候选）」区段（近 4 轮改动） | docs/CHANGELOG.md | 内容核对 | 规则补强 |
| 3 规则补强 | ✅ | 工作区 AGENTS 维护约定第 6 条；模板 WORKLOG 使用规则 / 完成清单 / audit-checklist | 4 文件 | 引用核对 | sync+校验 |
| 4 sync+校验+提交 | ✅ | sync 28 文件 0 差异；quick_validate；py_compile；git add + commit | 全部 | 通过 | 汇报 |
| 5 经验自动沉淀 | ✅ | 根因经验追加到 docs/EXPERIENCE-TO-KB.md；维护约定明确自动沉淀（不询问） | 3 文件 | 回读核对 | 汇报 |
| 6 审计·文档通读 | ✅ | 通读根 AGENTS / README / docs 全部 + 模板 AGENTS×2 + 模板 docs/scripts/private + skill | 无（只读） | 内容理解 | 自动化验证 |
| 7 审计·自动化验证 | ✅ | sync 28 文件 0 差异；quick_validate 通过；py_compile 通过；版本号 grep 无残留；占位符 9 类全覆盖；无 BOM、索引均 LF；git 跟踪齐全（private 骨架 20 文件） | 无 | 全部通过 | 冒烟测试 |
| 8 审计·端到端冒烟 | ✅ | init_project 初始化（28 文件/13 替换）+ 校验清单全过；ci_check / trash / pre_release（含占位拦截）/ bump_version / 非空目录拒绝 行为符合文档 | _ftest/（已清理） | 通过 | 汇总修复 |
| 9 修复+沉淀+提交 | ✅ | CHANGELOG 未发版区段移除 HEAD 固定引用+补条目；WORKLOG 当前任务切换；EXPERIENCE-TO-KB 追加本轮经验；清理 __pycache__ / _ftest；自动提交 | docs/CHANGELOG.md docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md | 回读核对+git status | 汇报 |
| 10 P3·UTF-8 输出 | ✅ | init_project.py 增加 `_configure_utf8`（main 入口调用）；冒烟输出无乱码 | init-project/scripts/init_project.py | 初始化冒烟通过 | UPGRADE |
| 11 P3·UPGRADE 澄清 | ✅ | 「应用方式」注明 sync_template.py 仅存在于模板母项目、目标项目不运行 | project-template/docs/UPGRADE.md（已 sync） | 引用核对 | CONTRIBUTING |
| 12 P3·CONTRIBUTING 措辞 | ✅ | 「新需求先对齐意图」改为 DESIGN + 用户决策 + WORKLOG 承载，移除 CHANGELOG 误述 | project-template/docs/CONTRIBUTING.md（已 sync） | 内容核对 | EXP-KB 索引 |
| 13 P3·EXP-KB 索引 | ✅ | 索引顺序与正文一致（新条目在前） | docs/EXPERIENCE-TO-KB.md | 回读核对 | 版本单一来源 |
| 14 P3·版本单一来源 | ✅ | SKILL/init-steps 正文移除硬编码 1.1.1 改引用 version.json；sync_template.py 新增 metadata.version==template_version 校验（实测通过）；维护约定同步 | 5 文件 | sync / quick_validate / py_compile 通过 | 收尾 |
| 15 收尾 | ✅ | 清理测试产物；经验自动沉淀；sync 失败路径实测（9.9.9 拦截）；自动提交 | docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md | 回读核对+git status | 汇报 |
| 16 审计+方案 | ✅ | 全面通读 + 自动化校验全部通过（sync 28 文件 0 差异、quick_validate
  valid、py_compile 5 脚本 OK、git 干净、private 骨架 10 文件强制跟踪、无远端）；
  交付精简版 agent 全局规范 skill（agent-rules）方案与实施清单 | docs/WORKLOG.md
  docs/EXPERIENCE-TO-KB.md | 回读核对 | 待用户确认方案后实施 |
| 17 实施·目录定位 | ✅ | 定位五个 agent skill 目录：codex（.codex/skills）、dsh
  （.dsh/skills）、workbuddy（.workbuddy/skills）、traework（TRAE Work CN →
  .trae-cn/skills）、qcoderwork（QoderWork CN → .qoderwork/skills，安装时创建） | 无
  （只读探查） | 回读核对 | agent-rules 创建 |
| 18 实施·skill 创建 | ✅ | 创建 agent-rules/ 四文件：SKILL.md（15 条红线通用化 +
  6 步工作流 + 审计/完成清单 + 触发规则）、inheritance-map.md（版本对照 + 红线覆盖
  矩阵 + 指纹）、audit-checklist-lite.md、agents/openai.yaml | agent-rules/ 4 新文件 |
  内容核对 | sync 扩展 |
| 19 实施·sync 扩展 | ✅ | sync_template.py 新增 agent-rules 校验：metadata.version、
  继承矩阵版本对照、矩阵覆盖完整性、红线正文指纹；破坏性测试 3/3 按预期拦截
  （指纹/版本/缺行） | scripts/sync_template.py | py_compile + 实测 | 文档同步 |
| 20 实施·文档同步 | ✅ | AGENTS.md 维护约定 1/4 + 目录 + 文档职责表；README 目录树 +
  使用方法 4（安装说明并入工作区 README）+ 维护约定；CHANGELOG 未发版区段登记 |
  AGENTS.md README.md docs/CHANGELOG.md | 回读核对 | 验证 |
| 21 实施·验证 | ✅ | sync 通过（28 文件 0 差异 + agent-rules verified）；quick_validate
  agent-rules valid；py_compile 通过 | 无 | 全过 | 安装到五个 agent |
| 22 实施·安装 | ✅ | 安装 agent-rules 到五个 agent skill 目录（沙箱无权限 → 升级
  权限获批）：codex / dsh / workbuddy / trae-cn（TRAE Work CN）/ qoderwork
  （QoderWork CN，新建 skills 目录）；每处 4 文件、SKILL.md 哈希一致 |
  5 处系统目录 | 复制后文件数+哈希核对 | 经验沉淀+提交 |
| 23 审计·双 skill | ✅ | 自动化校验全过：sync 28 文件 0 差异 + agent-rules verified；
  quick_validate×2 valid；py_compile 6 脚本；占位符 9/9 全覆盖；版本号无残留；
  路径引用无过时；init 冒烟（28 文件/13 替换/双 git 干净/check-ignore 命中）；
  五处 agent-rules 副本哈希一致。发现 init-project 过时项：SKILL 定位摘要缺
  v1.1.1 新特性（文档双模块/三级门禁/WORKLOG 生命周期/定案询问清单/发布前自测/
  红线 15 编号）+「自动版本递增发布」表述与默认手动确认策略有出入；init-steps
  「编码提示」未随 P3 UTF-8 修复更新；agent-rules 仅 1 条 P3 建议（正文硬编码
  「当前 1.1.1」） | docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md | 全过+回读核对 |
  待用户确认修复清单 |
| 24 修复+触发词同步 | ✅ | ① init-project SKILL 摘要补 v1.1.1 能力点+发布策略措辞
  修正；② init-steps 编码提示删除（用户指示旧说明不留档）；③ agent-rules 版本正文
  改引用；④ 发版同步约定加特性核对清单；⑤ 用户改动的触发词（仅非项目且非纯聊天
  加载）同步到 README / AGENTS / CHANGELOG；五处已安装副本重装并哈希一致 |
  init-project/SKILL.md init-project/references/init-steps.md agent-rules/SKILL.md
  README.md AGENTS.md docs/CHANGELOG.md + 5 处系统目录 | sync / quick_validate /
  py_compile / 副本哈希 全过 | 汇报 |
| 25 安装·init-project+目录纠正 | ✅ | init-project 首次安装到五个 agent（每处
  32 文件，不含 `__pycache__`/`.pyc`）；agent-rules 从误装 `~/.qoderwork/skills` 移到正确位置
  `~/.qoderworkcn/skills`（用户反馈实际目录为 qcoderworkcn）；误装目录已进回收站；
  两个 skill × 五处哈希全部一致 | README.md docs/CHANGELOG.md
  docs/EXPERIENCE-TO-KB.md + 5 处系统目录 | 文件数+哈希复核 | 提交 |
| 26 删除纪律命名统一 | ✅ | `_trash/<agent名>` 统一为 `_trash/<agent产品名>_<日期>_<时分>`
  （如 `codex_2026-08-25_2330`，只举例不设列表）；模板红线 4 / 私有 AGENTS ×2 /
  DOCS / audit-checklist / DESIGN / 工作区 AGENTS ×2 / README / init-project /
  agent-rules 共 9 处正文同步；红线 4 指纹 eb6d20857fe1 → ee28329cc7e5；sync
  通过、quick_validate ×2 通过 | 9 处正文 + inheritance-map + sync 镜像 |
  sync / quick_validate / py_compile | 重装五处副本 |
| 27 全面审计·第三轮 | ✅ | 全面通读 + 自动化验证全绿（sync 28 文件 0 差异、
  quick_validate ×2 valid、py_compile 6 脚本、init 冒烟 28 文件/13 替换/双 git
  干净/check-ignore 命中、tag 指向正确、五副本 × 两 skill 全量哈希一致、无秘密、
  无占位符残留）；人工核对发现并修复维护级问题：EXP-KB 索引/正文顺序不一致
  （P3 #4 复发）、WORKLOG/EXP-KB 最后更新日期陈旧、CHANGELOG 未发版区段缺 P3
  条目、WORKLOG 阶段 25 文件数 33→32 校准；当前任务切换 + 经验自动沉淀 |
  docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md docs/CHANGELOG.md | sync /
  quick_validate / git status | 汇报 |
| 28 P3 #6/#7 + dist 落地 | ✅ | 工作区根补 `.gitattributes`（LF 归一化，P3 #6）；
  模板【通用】补「项目归档/退役」流程（根/私有 AGENTS 小节 + README 说明 + DESIGN +
  audit-checklist 第 9 节）；补 `dist/` 发布产物约定（发布流程第 6 步 + DESIGN +
  README 结构 + release.yml 注释）；init-project SKILL 摘要 + inheritance-map
  不继承列表同步；工作区 AGENTS/README/CHANGELOG/EXP-KB 同步；sync /
  quick_validate ×2 / py_compile / 占位符 grep 全过；init 冒烟确认无残留 |
  .gitattributes project-template/（AGENTS×2、README、DESIGN、audit-checklist、
  release.yml）init-project/SKILL.md agent-rules/references/inheritance-map.md
  AGENTS.md README.md docs/CHANGELOG.md docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md |
  sync / quick_validate / py_compile / grep | 提交 + 评估汇报 |
| 29 实体目录+双置顶+测试指引+六处安装+发版 | ✅ | 模板实体化 `archive/`（A 区
  `ARCHIVE.md`）与 `dist/`（C 区 `.gitkeep`，`.gitignore` 改 `dist/*` +
  `!dist/.gitkeep`）；维护约定 #8「索引/未发版区段纪律（双置顶）」；新增
  `docs/TESTING.md` 测试落地指引；安装目标扩为六处（新增 `.qoder-cn`）；发版
  v1.1.2（未发版区段并入正式条目 + 版本递增 1.1.1→1.1.2 + sync/quick_validate/
  冒烟全过 + 六处副本哈希一致 + tag v1.1.2） |
  project-template/（archive、dist、TESTING.md、.gitignore、AGENTS×2、README、
  DESIGN、DOCS、audit-checklist、ci_check）init-project/SKILL.md AGENTS.md
  README.md docs/CHANGELOG.md docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md +
  六处 agent 目录 | sync / quick_validate / py_compile / grep / 冒烟 /
  副本哈希 | 汇报 + 下版讨论 |
| 30 init-project 覆盖度修复 | ✅ | 诊断确认：sync 镜像与 SKILL 摘要已覆盖
  v1.1.2，但 `references/init-steps.md` 校验清单缺 `archive/ARCHIVE.md`、
  `dist/.gitkeep`（ignore 规则）与 `docs/TESTING.md` 生成检查（自动化校验不覆盖
  清单级过时的实例）；已修复校验清单 + 初始化后建议引用；CHANGELOG 未发版
  v1.1.3 候选登记；六处副本重装哈希一致 | init-project/references/init-steps.md
  docs/CHANGELOG.md docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md + 六处 agent 目录 |
  quick_validate / sync / git status / 副本哈希 | 汇报 |
| 31 工作流缺陷修复（skill 覆盖自动校验 + 初始化路线图） | ✅ | 回答三问：
  「改模板不自动更新 skill」= 缺陷（sync 只校验资产镜像/版本/指纹，不校验 skill
  承载文档与已安装副本）；agent-rules 无需内容更新（v1.1.2 全是项目机制 + 红线
  指纹未变 + 版本已同步）；初始化流程需要更新（无 CI 落地时机/文档填写时机）。
  修复：sync_template.py 新增 `INIT_STEPS_COVERAGE` 校验（模板关键文件未进
  init-steps 即失败，破坏性测试拦截/还原通过）；init-steps 第 7 节升级为
  「落地路线图」（阶段 1 文档填空 / 2 实现 CI / 3 首个需求 / 4 首次发布 / 5
  立项调研 + 文档时机速查表）；维护约定 #4 补 skill 覆盖度复查；六处重装 |
  scripts/sync_template.py init-project/references/init-steps.md AGENTS.md
  README.md docs/CHANGELOG.md docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md +
  六处 agent 目录 | sync（含破坏性测试）/ quick_validate / py_compile /
  副本哈希 | 汇报 |
| 32 开发前规范·方案设计 | ✅ | 用户选定 C 档（PRD+RFC+ADR 三层体系）；确认
  「历史文档区例外」兼容性结论（普通正文仍禁留史，仅 prd/rfc/adr 允许正文留史）；
  完成全套方案设计：三目录实体化 + 状态机（PRD/RFC 定稿冻结、ADR 只增不改）、
  开发前门禁、S/M/L 档位、与 DESIGN/D-xxx/CHANGELOG 衔接、同步面清单、实施
  步骤；WORKLOG 当前任务切换；EXP-KB 沉淀 | docs/WORKLOG.md
  docs/EXPERIENCE-TO-KB.md | 回读核对 | 待用户确认方案细节与发版版本后实施 |
| 33 开发前规范·方案细化 | ✅ | 回答用户两问并细化方案：① 调研结果落点新增
  `private/dev/research/`（RESEARCH-000X + INDEX，进行中→已完成冻结→被新调研
  取代；PRD/RFC 内嵌摘要+链接，可跨需求复用且满足红线 6 防重复调研）；② 后续
  新增需求机制——编号跨版本持续增长不重置、PRD INDEX=需求登记册（草稿/已定稿/
  已实现/已废弃）、已定稿 PRD 变更开新 PRD 取代、开发前门禁贯穿每个 M/L 需求、
  一次发布=多个 PRD/RFC/ADR 实现集合（CHANGELOG 引用编号）、S 档持续可跳过；
  模板新增文件 3→4，同步面随之更新 | docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md |
  回读核对 | 待用户确认细化方案后实施 |
| 34 开发前规范·第二轮细化 | ✅ | 用户确认全部建议（S/M/L 跳过规则、PRD 默认
  私有、ADR 正文不可变/状态元数据可改、发版 v1.2.0 minor）并新增两点：①
  RESEARCH 允许追加更新——发现记录只追加（带日期/来源）、「结论与建议」为当前
  有效状态可覆盖、主题根本变化才开新号取代；② PRD 增加优先级字段（P0 紧急阻塞
  →P3 低/待定，属元数据可随时更新；INDEX 按状态+优先级分组排序，已实现/已废弃
  沉底）；给出四份 INDEX.md 骨架草案（PRD 含定稿门禁字段清单、RFC 候选对比表、
  ADR Nygard 不可变、RESEARCH 追加日志+结论覆盖）与 S/M/L 判定示例 |
  docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md | 回读核对 | 待用户审阅骨架与排序
  规则后实施 |
| 35 开发前规范·第三轮细化（状态机约束） | ✅ | 用户提出「状态机靠什么约束、
  避免文档落后」；设计三层约束：① 流程层——工作流第 1-3 步显式写「同步更新
  文档状态与索引」动作，并定义状态变更权限（定稿/采纳/废弃须用户确认，已实现
  由 agent 实施完成后自动更新）；② 检查层——完成检查清单 + audit-checklist
  新增「开发前文档一致性」检查项（编号连续 / INDEX 与正文状态一致 / 必填字段 /
  ADR 不可变靠 git log 核对）；③ 工具层——新增 `scripts/check_dev_docs.py`
  （stdlib 只读校验：文件名/编号连续/元数据枚举/状态机规则/INDEX 一致性/
  交叉引用，空目录通过），并入 pre_release_check.py 发布前必跑 + ci_check.py
  注释示例 + init-steps 校验清单；用户已确认剩余 3 小点（索引排序、P0-P3 定义、
  骨架无示例值） | docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md | 回读核对 |
  待用户确认约束方案后实施 |
| 36 开发前规范·第四轮细化（流程提示） | ✅ | 用户指出流程变长，要求每次对话
  agent 展示当前流程位置（当前节点/已完成/下一步）。设计：16 节点两阶段清单
  （开发前 01-09：需求提出/调研/PRD 草稿/PRD 评审/PRD 定稿/RFC 草稿/RFC 评审/
  ADR 记录/DESIGN 吸收；实施交付 10-16：确认开工/实施/审计/验证/展示提交/
  发布/沉淀汇报）；展示格式 `📍 流程位置：NN/16 · 节点名` + 已完成链 + 当前 +
  下一步；WORKLOG「当前任务」新增「流程位置」字段（单一真相，回复从 WORKLOG
  读取）；触发时机=每次实质回复/阶段落盘/上下文恢复/收尾/用户询问（纯闲聊
  除外）；S 档 N1→N10 直达；约束=工作流规则+完成清单+审计清单+check_dev_docs
  校验 WORKLOG 字段存在；母项目同步 dogfood | docs/WORKLOG.md
  docs/EXPERIENCE-TO-KB.md | 回读核对 | 待用户确认流程提示设计后实施 |
| 37 开发前规范·实施 | ✅ | 用户确认开始实施。模板新增 4 个登记册 INDEX.md
  （prd/rfc/adr/research）+ `scripts/check_dev_docs.py`；规范正文同步（根/私有
  AGENTS×2、WORKLOG 流程位置字段、DESIGN、DOCS、CONTRIBUTING、README、PRIVATE、
  audit-checklist 第 10 节）；pre_release_check/ci_check 接入 check_dev_docs；
  init-project SKILL/init-steps、agent-rules SKILL 内容同步；sync 覆盖列表 +
  工作区 AGENTS/README/CHANGELOG/WORKLOG dogfood | 见变更文件清单 |
  待验证 | 12 自动审计 → 13 验证 → 14 提交 → 15 发版 v1.2.0 |
| 38 开发前规范·验证+发版准备 | ✅ | 全链路验证全绿：sync 36 文件 0 差异
  （template_version=1.2.0）；quick_validate ×2 valid；py_compile OK；
  check_dev_docs 正/负向测试 4/4（缺定稿日期拦截、补齐通过、ADR 自取代拦截、
  编号缺口拦截；期间修复解析 bug×2：同行 `|` 分隔字段截断、`>` 块引用前缀
  剥离）；init 冒烟全过（36 文件/四登记册/流程位置字段/模板版本 1.2.0/
  check_dev_docs/ci_check/pre_release）；版本号全局 grep 无残留（仅历史）；
  占位符仅模板合法 | 无（只读验证） | 全过 | 提交 + tag v1.2.0 + 六处重装 |
| 39 开发前规范·发版+安装收尾 | ✅ | 发布提交 `60b10cf`（45 文件）+ 附注 tag
  `v1.2.0`；六处 agent skill 目录重装（init-project 40 文件 / agent-rules 4
  文件，全量 SHA-256 哈希一致）；`_trash/codex_2026-08-26_0245`（负向测试脚本）
  经 trash.py 进回收站；git 工作树干净 | 六处系统目录 | 哈希复核全过 |
  收尾汇报 |
| 40 流程展示要求+文档更新流程补实 | ✅ | 模板文档新增「缩写附中文翻译」强制
  规则 + 「缩写对照」表（private/AGENTS 流程提示、根 AGENTS、DESIGN、WORKLOG、
  agent-rules 工作流）；16 节点清单新增「文档更新流程（贯穿全程）」小节（文档
  就绪 / 发布前文档检查 / 状态文档收口 / 文档治理注释；审计 P1 补实——此前仅
  对话 mermaid 展示未落库）；工作区 AGENTS 维护约定 #9 / README / CHANGELOG
  未发版 v1.2.1 候选同步；修正工作区维护约定编号冲突（流程提示误编 8 → 9，
  索引纪律保持 8） | project-template/private/AGENTS.md、project-template/AGENTS.md、
  project-template/private/dev/DESIGN.md、WORKLOG.md、agent-rules/SKILL.md、
  AGENTS.md、README.md、docs/CHANGELOG.md、docs/EXPERIENCE-TO-KB.md
  （资产镜像经 sync） | sync 36 文件 0 差异 / quick_validate ×2 / py_compile /
  六处副本哈希一致 | 全面审计 → 发版 v1.2.1（用户决定） |
| 41 全面审计（第四轮） | ✅ | 自动化验证全绿（sync/quick_validate×2/py_compile/
  冒烟/check_dev_docs/版本+占位符 grep/六处哈希）；独立子代理审计（不共享上下文）
  结论：不通过（P1×1）→ 修复 4+1 项：① P1 补实「文档更新流程（贯穿全程）」
  持久小节；② P1 WORKLOG 当前任务陈旧（流程位置 11 与已完成 01-13 矛盾、计划
  步骤残留 v1.2.0 旧任务）→ 切换为审计任务；③ P1 CHANGELOG 版本非新在前
  （v1.1.1 排在 v1.2.0 上方）→ 重排为未发版→v1.2.0→v1.1.2→v1.1.1→…；④ P2
  维护约定 9 排在 8 前 → 顺序修正；⑤ P3 init-project SKILL 摘要缺「缩写中文
  翻译」→ 补充。复检：CHANGELOG 新在前 / 维护约定 1-9 / DOCS 地图 / 职责表 /
  audit §1-10 / 治理无残留 | 见修复清单 | sync / quick_validate / 六处哈希全过 |
  14 提交 → 16 汇报（15 待发版 v1.2.1） |
| 42 init-project 初始化流程更新 | ✅ | 用户指出 init-project 初始化流程也应
  更新；取证确认缺口：`init_project.py` 打印「下一步」仍为 v1.1 心智（无开发前
  登记册/流程提示）、SKILL 执行流程校验清单缺四登记册/check_dev_docs/流程位置、
  前置确认缺调研落点、init-steps 缺特性核对。修复：init_project.py 下一步扩为
  8 条（补登记册/流程提示/缩写翻译）；SKILL 执行流程第 3 步补 3 项校验、第 4
  步收尾建议补开发前门禁；前置确认 1 补调研落点 RESEARCH；init-steps 校验清单
  补「流程提示/缩写对照」、阶段 1 补流程提示说明；CHANGELOG 未发版登记 |
  init-project/scripts/init_project.py、init-project/SKILL.md、
  init-project/references/init-steps.md、docs/CHANGELOG.md | 待 py_compile/
  quick_validate/冒烟/重装 | 14 提交 → 16 汇报（15 待发版 v1.2.1） |

## 待办/遗留

- [x] 上一任务（模板 v1.1.0 第二轮改造）9/9 完结
- [x] 上一任务（文档治理经验吸收）6/6 完结
- [x] 上一任务（A–G 经验合入 v1.1.1，提交 1e02c3e + tag v1.1.1）完结
- [x] 上一任务（version.json 合并，提交 733065f）完结（阶段记录已归档）
- [x] 本任务（P2 修复 + WORKLOG 生命周期收口 + 经验自动沉淀）5/5 完结
- [x] 本任务（全面审计 + P2 修复 + 经验沉淀）9/9 完结
- [ ] 工作区无 git 远端，改动未推送（N/A 或用户决定）
- [ ] 模板根其余 7 个文件（AGENTS/README/LICENSE/version.json/
      .gitignore/.gitattributes/.editorconfig）为入口与工具必需；如仍想精简需单独评估
- [x] 下次发版 v1.1.2：把「未发版变更」区段并入正式条目，并 bump version.json / 打 tag
- [x] P3 #1/#2/#3/#4/#5 已实施（UTF-8 输出、UPGRADE 澄清、CONTRIBUTING 措辞、
      EXP-KB 索引、版本单一来源 + sync 自动化校验）
- [x] 本任务（P3 建议实施）15/15 完结
- [x] P3 #6 工作区根补 .gitattributes（行尾归一化）、#7 模板补「项目归档/退役」
      环节：已实施（随本任务提交）
- [x] 本任务（P3 #6/#7 + dist 产物约定补齐）完结
- [x] 新需求（精简版 agent 全局规范 skill，agent-rules）：方案已确认，已实施
      （skill 创建 + sync 校验 + 文档同步 + 安装到五个 agent）；随 v1.1.2 发版时
      同步版本
- [x] 本任务（全面审计·第三轮）完结：自动化验证全绿；维护级缺陷已修复并提交
- [x] 本任务（开发前规范实施 + v1.2.0 发版）完结：四登记册 + check_dev_docs +
      流程提示落地，六处重装哈希一致，tag v1.2.0

## 历史记录

- 2026-08-26 模板 v1.2.0 发版：开发前规范（PRD/RFC/ADR/RESEARCH 四登记册 +
  状态机三层约束 + 流程提示）；提交 60b10cf + tag v1.2.0；六处重装哈希一致。
- 2026-08-26 工作流缺陷修复（skill 覆盖自动校验 + 初始化路线图）：sync_template
  新增 INIT_STEPS_COVERAGE；init-steps 第 7 节升级落地路线图；维护约定 #4 补
  覆盖度复查；六处重装（阶段 31）。
- 2026-08-26 模板 v1.1.2 发版：实体化 `archive/` / `dist/`、维护约定 #8 双置顶、
  测试落地指引（TESTING.md）、六处 agent 安装（新增 `.qoder-cn`）；版本递增
  1.1.1→1.1.2，已提交并打 tag（v1.1.2）。
- 2026-08-26 模板生命周期补齐：工作区根 `.gitattributes`（P3 #6）+ 模板「项目
  归档/退役」流程（P3 #7）+ `dist/` 发布产物约定；全链路同步并提交。
- 2026-08-26 删除纪律命名统一：`_trash/<agent名>` → `<agent产品名>_<日期>_<时分>`
  （只举例不设列表），正文 9 处 + 继承矩阵红线 4 指纹更新 + 五副本重装，已提交
  （0fbec33）。
- 2026-08-26 全面审计（第三次）：通读全部规范/实现 + 自动化验证 + 端到端冒烟全过；
  发现并修复维护级缺陷（EXP-KB 索引/正文顺序、日期陈旧、CHANGELOG 未发版区段缺
  P3 条目、WORKLOG 33→32 校准）。
- 2026-08-25 P3 建议实施（按注释反馈）：init_project.py UTF-8 输出；UPGRADE.md
  澄清 sync_template 归属（目标项目无此脚本）；CONTRIBUTING 对齐意图措辞
  （DESIGN / 用户决策 / WORKLOG 承载）；EXPERIENCE-TO-KB 索引统一；SKILL/init-steps
  版本号单一来源（正文改引用 version.json + sync 自动化校验 metadata.version）。
- 2026-08-25 全面审计（第二次）：通读全部规范/实现 + 自动化验证 + 端到端冒烟全部
  通过（sync 28 文件 0 差异、quick_validate 通过、初始化校验清单全过）；发现
  P2×2（CHANGELOG 未发版区段 HEAD 引用过时 733065f→3006b97 且缺「经验自动沉淀」
  条目、WORKLOG 当前任务未随新任务切换）已修复；P3 建议清单待用户决策。
- 2026-08-25 模板 v1.1.1：A–G 实践项目经验合入，已提交并打 tag（1e02c3e / v1.1.1）
  完结（审计确认）。
- 2026-08-25 全面审计 + 修复整理：审计发现 3 处过时版本引用、WORKLOG 状态失真、
  重复表格行、发版同步约定盲区；修复并整理母项目目录（docs/ + scripts/），
  新建 docs/EXPERIENCE-TO-KB.md；模板根布局随后在二次整理中精简。
- 2026-08-25 目录结构二次整理：README 回根；project-template 精简
  （CONTRIBUTING → docs/、version-sync.json → scripts/，bump_version 同步更新）；
  修正「工作区 .git 只读」错误描述，改动由 agent 自动提交。
- 2026-08-25 子目录 README 改名：docs/README.md → docs/DOCS.md、
  private/README.md → private/PRIVATE.md、private/test/README.md →
  private/test/TEST.md（避免与项目根 README 混淆、便于索引），全部引用同步更新并提交。
- 2026-08-25 版本文件合并：`VERSION` / `TEMPLATE_VERSION` 合并为根 `version.json`
  （`version` + `template_version` 两字段），脚本/CI/skill/文档全部更新，提交。
- 2026-08-25 P2 修复 + 根因：WORKLOG 硬事实 29→28、当前任务切换、CHANGELOG 补
  未发版变更区段；根因=WORKLOG 生命周期缺两个收口（任务开始切换当前任务、收尾
  校准硬事实），规则补强（工作区维护约定 + 模板 WORKLOG/完成清单/audit-checklist）。
- 2026-08-25 模板 v1.1.0 第二轮改造：阶段落盘（WORKLOG）、双模块、【通用】/【项目专用】
  标注、经验文档×2（完整条目）、删除纪律（_trash + trash.py）、模板升级机制
  （TEMPLATE_VERSION + CHANGELOG + UPGRADE）、红线 13→15（阶段落盘、上下文恢复重读）。
  端到端测试全部通过（详情见阶段记录）。
- 2026-08-25 文档治理经验吸收：文档维护清单、红线 12/5 强化、文档治理约定（正文即当前
  状态；覆盖原文、禁止 AI 追加历史、留痕仅 CHANGELOG 一行、废案走 _trash、可恢复性由
  删除机制保证）、审计清单「文档无缝衔接」专项；未写入参考来源。
- 2026-08-25 v1.1.0 已提交并打 tag（c58a816）。
