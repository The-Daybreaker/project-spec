# WORKLOG — 通用项目模板工作区 工作进度日志

> 模块：项目专用。
> 使用规则：每完成一小阶段先更新本文件与受影响文档；新对话/新任务开始时，若旧内容
> 已完结或文档已膨胀，**先询问用户是否清理**（已完结条目归档到「历史记录」，或整段
> 移入 `_trash/`），得到确认后才清理；绝不自动删除。
- 最后更新：2026-08-26

## 当前任务

- 需求：模板工作区**全面审计（全生命周期/专业级）**——不只版本，覆盖方方面面：
  ①规范与文档（模板根/私有 AGENTS、DESIGN/DOCS/UPGRADE/README/CONTRIBUTING/
  TESTING/audit-checklist/登记册：语言一致性、准确性、精炼度、交叉引用、术语统一、
  模块标注、红线编号与继承矩阵）；②脚本与机制（8 个脚本 + CI×2 + version-sync：
  冗余、健壮性、闭环、门禁正确性、文档↔实现一致性）；③流程闭环与生命周期可用性
  （初始化→首个需求开发前门禁→实施→验证→发布→模板升级→归档全链路演练、断链、
  16 节点 vs 实际流程、可用性/防呆/回退）；④安装面（六处副本、agent-rules 与模板
  一致）；⑤全量自动化验证。分 3 个独立子代理并行审计，输出 P0-P3 清单，汇总修复
  后复检汇报。
- 流程位置：01 需求提出 → 12 自动审计（全面审计）；当前 12 自动审计（独立子代理
  ×3 并行执行中）；后续 13 验证 → 14 修复 → 16 汇报。
- 计划步骤：
  1. WORKLOG 当前任务切换（本步）
  2. 派 3 个独立子代理并行审计：A=规范与文档语言、B=脚本与机制、C=流程闭环与
     生命周期（各带验证命令与审计清单，不共享主对话上下文）
  3. 汇总三份审计报告，P0/P1 必清、P2/P3 与用户对齐
  4. 修复 + 全量复检（sync/verify/quick_validate/py_compile/冒烟）
  5. WORKLOG 校准 + EXP-KB 沉淀 + 汇报

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
  init-project/references/init-steps.md、docs/CHANGELOG.md | ✅ 本轮审计补验：
  py_compile / quick_validate×2 / sync / init 冒烟 / 六处副本哈希 全过 | 14 提交
  → 16 汇报（15 待发版 v1.2.1） |
| 43 全面审计（第五轮） | ✅ | 全流程覆盖与清晰度审计：通读工作区/模板/skill/
  agent-rules 全部规范与脚本；自动化验证全绿（sync 36 文件 0 差异、quick_validate
  ×2、py_compile、init 冒烟 36 文件/13 替换/双 git 干净/check-ignore 命中、
  check_dev_docs 0 issue、pre_release 占位拦截符合预期、六处副本全量哈希一致）；
  补验阶段 42 待验证项；人工核对发现 P2×1（UPGRADE.md 未覆盖模板新增 B 区骨架：
  四登记册/流程位置字段/check_dev_docs 依赖）与 P3×5（TEST.md 与 private/.gitignore
  的 staging-repo 不一致、--auto-release 与红线 2 衔接未明确、FAQ「Python 不可用
  →--no-git」表述误导、check_dev_docs 交叉引用弱校验、.editorconfig/.gitattributes
  行尾不一致）；结论：可支撑从零搭建全流程，修复建议待用户确认；切换当前任务 +
  经验自动沉淀 | docs/WORKLOG.md docs/EXPERIENCE-TO-KB.md | sync / quick_validate
  / py_compile / 冒烟 / 副本哈希 | 汇报（修复建议待用户确认；15 发版 v1.2.1
  由用户决定） |
| 44 T1·升级路径修复 | ✅ | UPGRADE.md 补「B 区私有骨架迁移」规则（新增骨架直接
  复制、已有同名文件只合并模板新增字段、依赖补齐、私有子 git 同步）+「升级迁移
  检查表（按版本）」（v1.2.0 已知迁移要点：四登记册 INDEX 复制 / WORKLOG 流程
  位置字段合并 / check_dev_docs 依赖补救）；回读校验补 check_dev_docs 步骤；
  sync 36 文件 0 差异；CHANGELOG 未发版登记；WORKLOG 当前任务切换；EXP-KB
  沉淀 | project-template/docs/UPGRADE.md（assets 镜像同步）、docs/CHANGELOG.md、
  docs/WORKLOG.md、docs/EXPERIENCE-TO-KB.md | sync 36 文件 0 差异 / quick_validate
  ×2 valid / 六处副本全量哈希一致（40 文件逐文件）+ UPGRADE 新节就位 | 提交 →
  汇报 |
| 45 P3 批量修复（T2-T8，T5 跳过） | ✅ | ① T2 private/.gitignore 补
  `test/**/staging-repo/`（与 TEST.md 一致）；② T3 自动发布预授权语义：根
  AGENTS.md 版本管理 + init_project.py 自动发布文案 + init-steps 参数表；
  ③ T4 init-steps FAQ「Python 不可用」纠正；④ T6 .gitattributes ps1/bat 行尾
  LF（工作区 + 模板同步）；⑤ T7 ci_check/pre_release 子进程改 sys.executable；
  ⑥ T8 清理工作区与六处副本 __pycache__（回收站）；sync + quick_validate×2 +
  py_compile + 冒烟（--auto-release 预授权文案/规则/LF 生效）+ 六处重装 40 文件
  逐文件哈希一致 全过 | project-template/（private/.gitignore、AGENTS.md、
  .gitattributes、scripts/ci_check.py、scripts/pre_release_check.py）、
  .gitattributes、init-project/（scripts/init_project.py、references/init-steps.md）、
  docs/CHANGELOG.md、docs/WORKLOG.md、docs/EXPERIENCE-TO-KB.md + 六处 agent 目录 |
  sync / quick_validate / py_compile / 冒烟 / 副本哈希 全过 | 提交 → 汇报（15
  发版 v1.2.1 由用户决定） |
| 46 发版 v1.2.1 | ✅ | 版本递增 1.2.0→1.2.1（按发版同步约定手工同步：根
  version.json / project-template/version.json（version=0.0.1 不变、
  template_version=1.2.1）/ SKILL metadata.version ×2 / 继承矩阵版本对照 /
  CHANGELOG 未发版区段转正式 v1.2.1 条目 / AGENTS+README 当前版本字样 /
  UPGRADE 追加 v1.2.1 已知迁移要点）；sync 36 文件 0 差异
  （template_version=1.2.1）；quick_validate ×2 valid；py_compile OK；冒烟
  （初始化 template_version=1.2.1、version=0.0.1、check_dev_docs 0 issue）；
  版本号全局 grep 无残留；六处重装 40 文件逐文件哈希一致、无 pycache；
  注意：母项目发版不能用 bump_version.py（REPO_ROOT=project-template，误升
  模板骨架 version 0.0.1→0.0.2，已回退并记入经验） | 多文件（version.json ×2、
  SKILL.md ×2、inheritance-map.md、CHANGELOG、AGENTS、README、UPGRADE（assets
  经 sync）、WORKLOG、EXP-KB）+ 六处 agent 目录 | 全过 | 发布提交 + tag v1.2.1
  + 汇报 |
| 47 第六轮全面审计（自审） | ✅ | 子代理通道阻塞（fork_turns=none / followup
  消息未送达、子代理递归派生），按用户指示主 Agent 亲自执行；自动化全绿（sync
  36 文件 0 差异、quick_validate×2、py_compile、冒烟 template_version=1.2.1、
  版本+占位符 grep 无残留、git 干净、tag v1.2.1→946b8ac、无 pycache、private
  骨架 14+14 强制跟踪）；文档生命周期核对通过（CHANGELOG 新在前、EXP-KB
  索引/正文双置顶、日期一致）；**发现并修复发版重装漏项**：六处 agent-rules
  仍为 1.2.0（缺「缩写附中文翻译」正文与继承矩阵 1.2.1 版本）→ 补装六处 +
  全量 4 文件哈希一致；init-project 六副本 40 文件哈希一致 | docs/WORKLOG.md
  docs/EXPERIENCE-TO-KB.md + 六处 agent-rules 目录 | sync / quick_validate /
  py_compile / 冒烟 / 哈希 全过 | 汇报 |
| 48 第七轮审计·t2 模板内改动 | ✅ | 脚本健壮性：check_dev_docs 两处裸 read_text
  改走 _read_text（P2-4a）；pre_release_check 修复 `_ci_check_state` NameError
  bug + CI 占位门禁双向断言（P2-4b）+ SECRET_NAME_RE 收紧（P3-3c）+
  CHANGELOG/root_agents 读取兜底；sync_template rmtree+copytree 失败兜底（P3-2）；
  init_project 绝对路径 parts→relative_to + _valid_branch 拦 `/-/` 开头（P3-2/P3-3）；
  trash.py 核实 P3-3 已修复无需改。文档一致性：P2-1 CHANGELOG 手工更新表述
  （根/私有 AGENTS + release.yml + bump_version 文案）；P2-3 三区表补 archive/；
  P3-1 knowops 泛化×5；P3-5 模块标注×5；P3-6 细节一致性×5（DOCS 文档清单/地图、
  audit-checklist §10 字段名、rfc INDEX PRD-XXXX、README 结构树、DESIGN 相对路径
  风格统一 9 处） | project-template/（scripts×4、AGENTS×2、README、DOCS、
  audit-checklist、PRIVATE、TEST-REPORT、TEST、rfc/INDEX、private/AGENTS、
  release.yml、DESIGN、EXPERIENCE-TO-KB） | 回读核对（发现并发编辑丢失 6 处
  已重应用并逐处验证） | 待验证 → t3 工作区文档（P3-7） |
| 49 第七轮审计·t3/t4 工作区与机制化 | ✅ | t3 P3-7：工作区 AGENTS.md / README.md
  grep 版本示例 `1.1.0 / 1.1.1` → `1.1.2 / 1.2.0`。t4 P1-1 机制化：新增
  install-targets.json（机器可读安装表 ×6：codex/dsh/workbuddy/trae-cn/
  qwenworkcn/qoder-cn，qwenworkcn 替换原 qoderworkcn）；新增
  scripts/verify_installed_copies.py（逐目录 × 逐 skill 全量 SHA-256 + SKILL.md
  metadata.version 版本哨兵比对）；sync_template.py 并入 `check_installed_copies`
  钩子（发版链强制安装校验，缺失/过时即拦截）；README §4 / AGENTS 目录 + 维护约定
  #4 + 设计决策 + 文档职责表更新为引用机器可读表；CHANGELOG 未发版区段登记
  P2/P3/机制化条目（删占位符） | install-targets.json、
  scripts/verify_installed_copies.py、scripts/sync_template.py、README.md、
  AGENTS.md、docs/CHANGELOG.md | verify 首跑实测：精确命中 qwenworkcn 缺失 ×2 +
  现役 5 处仅 `scripts/init_project.py` 哈希漂移（t2 改动被系统性定位）；
  回读核对 | t5 P1-1 落地安装 |
| 50 第七轮审计·t5 搁置 + t6 版本递增 | ✅ | t5 安装被 TRAE 沙箱拦截：工作区外写
  操作敏感（多轮最小化测试探明边界：新建文件/目录可成功、覆盖/删除已存在文件与整
  目录复制被拒，`hit restricted` / WinError 5），用户决策「先搁置安装推进后续」
  （待沙箱外执行）。t6 版本递增 1.2.1→1.2.2：根 version.json（version +
  template_version）、project-template/version.json（template_version=1.2.2、
  version=0.0.1 按历史约定不变）、SKILL metadata.version ×2 与继承矩阵版本对照 ×3；
  grep 1.2.1 全量 51 处分类确认——仅 AGENTS.md:18 / README.md:197「当前版本」字样，
  均已更新，其余为历史合法引用；UPGRADE 追加 v1.2.2 迁移要点（安装表机制化仅母
  项目脚本、不下发、无迁移动作）；CHANGELOG 未发版区段占位符替换为版本递增登记
  （发版条目 t8 补） | version.json ×2、SKILL.md ×2、inheritance-map.md、
  AGENTS.md、README.md、project-template/docs/UPGRADE.md（assets 经 t7 sync）、
  docs/CHANGELOG.md、docs/WORKLOG.md | grep 分类核对 + 逐文件回读 | t7 发版链验证 |
| 51 第七轮审计·t5 补装 + t7 发版链验证 | ✅ | 用户放行沙箱后补装：t5 六处 × 两
  skill 全量重装（init-project 在 sync 后二次重装以纳入资产镜像变更）、.qoderworkcn
  旧副本清理、verify EXIT=0 全绿。t7 验证链：sync 36 文件 0 差异 + 版本/继承矩阵 /
  INIT_STEPS_COVERAGE / 已装副本全过（首两次 .gitignore 被 IDE 文件锁 WinError 32，
  10s 后释放重试成功，P3-2 兜底按设计工作）；quick_validate ×2 valid；
  py_compile ×8 OK；冒烟 _ftest/smoke_v122（init template_version=1.2.2 /
  version=0.0.1、36 文件 13 替换、占位符 CLEAN、check_dev_docs 0、ci_check pass、
  pre_release 占位拦截预期 + allow-placeholder 全绿）；资产镜像 grep 版本正确；
  清理 __pycache__、冒烟产物移入 _trash/trae_2026-08-26_1351 | 六处 agent 目录 +
  多文件 | sync / validate / py_compile / 冒烟 / pre_release / grep 全过 |
  t8 提交发版 |
| 52 第七轮审计·t8 提交发版 + t9 收尾 | ✅ | t8：核实 private 子 git 不存在属既定
  设计（工作区不建 private 子 git，`git -C project-template/private` 落回主仓库
  正常；private 骨架凭 `git add -f` 强制跟踪在提交内）；CHANGELOG 未发版区段
  收口为正式 v1.2.2 条目（IDE 内存视图覆盖两处编辑，重做 + 整篇回读确认落盘，
  期间一次短块替换产生脏行已清理）；发布提交 01435a0（49 files，+748/−134；
  审计报告文件不入仓库，保持未跟踪）+ 附注 tag v1.2.2 指向 HEAD。t9：WORKLOG
  校准（本阶段 + 待办/遗留完结）、EXP-KB 沉淀 3 条（sync 先于安装 / IDE 覆盖
  落盘核对 / 沙箱边界实测 + 放行协作）双置顶、索引核对（CHANGELOG 无未发版
  残留、EXP-KB 索引与正文一致、工作树干净） | docs/CHANGELOG.md docs/WORKLOG.md
  docs/EXPERIENCE-TO-KB.md | git log/tag/status + 回读核对 | 汇报 |
| 53 模板 v1.3.0·实施+发版 | ✅ | ① 红线 16「范围克制与纠错清零（按单办事、
  不加菜；撤菜不解释）」落模板根/私有 AGENTS + DESIGN 规范 17 + audit-checklist
  合规项 + agent-rules 规范 16 + 继承矩阵行（指纹 1a89754aa5ba，按 sync 规范化
  逻辑从文件实算）+ 精简审计清单项；② 图可视化规范「先出图再确认」：流程+清单
  双落点（私有 AGENTS 工作流 3.「可视化确认」+ 完成清单/audit-checklist 检查项）、
  三类图分挂各阶段（流程图随 prd/rfc、架构图随 rfc/adr、页面原型落
  prototype/）、`private/dev/prototype/README.md` 实体化 + INIT_STEPS_COVERAGE/
  init-steps 校验清单/路线图/速查表 + UPGRADE v1.3.0 迁移要点、根 AGENTS/私有
  AGENTS 文档职责表、DOCS 地图、template README 结构树 + 工作区 README 设计要点
  13/14；③ skills 合并：init-project/agent-rules → `skills/`（sync/verify 路径
  常量 + install-targets source + 工作区 AGENTS/README 全链），六处副本重装
  （init-project 41 文件、agent-rules 4 文件）哈希一致；④ 版本递增
  1.2.2→1.3.0（version.json ×2、SKILL metadata ×2、继承矩阵版本表、AGENTS/README
  当前版本，grep 无残留，资产镜像经 sync）；⑤ 验证链全过：sync 37 文件 0 差异
  （含六处副本校验）、quick_validate ×2 valid、py_compile 8 OK、冒烟
  （smoke_v130：37 文件/13 替换/prototype README 生成/template_version=1.3.0/
  占位符 0/check_dev_docs 0/ci_check pass/pre_release 占位拦截+放行全绿）；
  ⑥ 发布提交 0613dda（62 files）+ 收尾 9c1a663 + 附注 tag v1.3.0 指向 0613dda；
  冒烟产物/__pycache__ 已清理 | 多文件（模板 AGENTS×2、DESIGN、audit-checklist、
  DOCS、UPGRADE、README、prototype/README 新建、skills/×2、sync_template.py、
  install-targets.json、AGENTS.md、README.md、docs/CHANGELOG.md、docs/WORKLOG.md、
  version.json ×2）+ 六处 agent 目录 | sync / quick_validate / py_compile / 冒烟 /
  副本哈希 全过 | 收尾汇报 |
| 54 src/ 代码区实体化·v1.3.1 | ✅ | ① 模板内：`src/.gitkeep` 实体化（A 区，进 git，
  含代码区说明注释）+ 分区约定「代码区 = 全部业务源码/资源入 `src/`（子目录按
  技术栈自定）、根目录为工程区不直接放业务代码」落根 AGENTS 项目概览、模板 README
  结构树、DESIGN 项目形态；② init-project：INIT_STEPS_COVERAGE 补 src/.gitkeep +
  init-steps 校验清单/落地路线图补 src/ 检查项 + SKILL 摘要「实体目录」补 src；③
  版本递增 1.3.0→1.3.1（version.json ×2、SKILL metadata ×2、继承矩阵版本表、
  AGENTS/README 当前版本，grep 无残留，资产镜像经 sync）；④ UPGRADE 补 v1.3.1
  迁移要点；⑤ 验证链全过：sync 38 文件 0 差异（含六处副本校验；IDE 文件锁
  WinError 32 按 P3-2 兜底重试通过）、quick_validate ×2 valid、py_compile 8 OK、
  冒烟（smoke_v131：38 文件/13 替换/src/.gitkeep 生成/template_version=1.3.1/
  占位符 0/check_dev_docs 0）；⑥ 六处副本重装（init-project 42 文件、agent-rules
  4 文件）哈希一致；发布提交 + 附注 tag v1.3.1 | project-template/（AGENTS、README、
  DESIGN、src/.gitkeep 新建、UPGRADE 经 sync）、skills/init-project/（SKILL.md、
  init-steps）、skills/agent-rules/（SKILL.md、inheritance-map）、scripts/
  sync_template.py、AGENTS.md、README.md、docs/CHANGELOG.md、docs/WORKLOG.md、
  version.json ×2 + 六处 agent 目录 | sync / quick_validate / py_compile / 冒烟 /
  副本哈希 全过 | 收尾汇报 |
| 55 v1.3.1 发版后全面审计（独立子代理） | ✅ | 独立子代理（不共享本对话上下文）
  按模板 audit-checklist 与工作区维护约定全面审计：自动化验证全绿（sync 38 文件
  0 差异 + installed verified、verify exit 0、quick_validate ×2 valid、py_compile
  8 OK、版本 1.3.1 无残留、tag v1.3.1 指向 d9b1e1f、红线 16 指纹 1a89754aa5ba
  一致且模板/精简版各 16 条）；文档一致性全达标（CHANGELOG 新在前、EXP-KB 双置顶、
  WORKLOG 阶段 54 硬事实与实际一致、UPGRADE v1.3.1、src 分区五处一致、16 节点
  不变式、图可视化规范双落点）；结论**通过**（P0/P1 零项）。处理子代理建议：
  P2-1 WORKLOG 当前任务切换随本审计收尾提交；P3-1 清理 skills/init-project/
  scripts/__pycache__（审计方复核：源 42 文件口径正确） | docs/WORKLOG.md
  docs/EXPERIENCE-TO-KB.md + 清理 __pycache__ | verify exit 0 + git 干净 |
  汇报 |

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
- [x] 本任务（init-project 初始化流程更新）完结：提交 4347220；阶段 42 验证项
      已由第五轮审计补验全绿
- [x] 本任务（全面审计第五轮）完结：审计结论汇报已交付，P2/P3 修复建议待用户
      确认（P2·T1 已由新任务实施）
- [x] 本任务（T1 升级路径修复）完结：提交 344b423；sync + 六处重装哈希复核
- [x] 本任务（P3 批量修复 T2-T8，T5 跳过）完结：提交 3b8d3d4；sync + 冒烟 +
      六处重装哈希复核
- [x] 本任务（发版 v1.2.1）完结：提交 946b8ac + 附注 tag v1.2.1；六处重装哈希
      一致（收尾提交 b1607fc）
- [x] 本任务（第七轮全面审计修复 v1.2.2）完结：提交 01435a0 + 附注 tag v1.2.2；
      六处副本 v1.2.2 哈希复核一致
- [x] 本任务（模板 v1.3.0：红线 16 + 图可视化规范 + skills 目录合并）完结：发布
      提交 0613dda + 收尾 9c1a663 + 附注 tag v1.3.0；六处副本 v1.3.0 哈希复核一致
- [x] 本任务（模板 v1.3.1：src/ 代码区实体化与分区约定）完结：发布提交 + 附注
      tag v1.3.1；六处副本 v1.3.1 哈希复核一致
- [x] 本任务（全面审计修复 v1.3.2：三域并行独立审计 P1×3+P2×7+P3×6）完结：
      发布提交 17a0927 + 收尾提交 + 附注 tag v1.3.2；六处副本 v1.3.2 哈希复核一致

## 历史记录

- 2026-08-26 第六轮全面审计（自审）：自动化全绿；发现并补装 v1.2.1 发版漏项的
  六处 agent-rules 副本（1.2.0→1.2.1），全量哈希一致。
- 2026-08-26 模板 v1.2.1 发版：维护收口（UPGRADE B 区骨架迁移 + P3 批量修复 +
  流程展示/初始化流程增强）；版本递增 1.2.0→1.2.1，提交 946b8ac + 附注 tag
  v1.2.1；六处重装哈希一致。
- 2026-08-26 P3 批量修复（T2-T8，T5 跳过）：文档/配置/脚本一致性收口 +
  pycache 清理；sync / quick_validate / 冒烟 / 六处重装哈希复核全过。
- 2026-08-26 T1 升级路径修复：UPGRADE.md 补「B 区私有骨架迁移」+「升级迁移
  检查表（按版本）」（v1.2.0 迁移要点），sync 通过，六处重装哈希复核。
- 2026-08-26 全面审计（第五轮）：全流程覆盖与清晰度审计，自动化验证 + 端到端
  冒烟 + 六处副本哈希全绿；结论可支撑从零搭建全流程；发现 P2×1 / P3×5 建议
  （详见阶段 43），修复待用户确认。
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
