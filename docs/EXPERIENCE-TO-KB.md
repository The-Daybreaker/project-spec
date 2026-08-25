# EXPERIENCE-TO-KB — 可沉淀进知识库的经验（工作区母项目）

> 模块：项目专用（工作区）。
> 用途：记录本工作区（通用项目模板母项目）产生的**经验方法/教训/方案**候选，
> 供后续按知识库规范（如 knowops）沉淀。每轮对话结束后由 agent 将**完整候选经验**
> 写入本文件；沉淀时以本文件为唯一依据，不需要重读整个项目。入库时由知识库流程
> 决定归属（本文件不预设位置）。
> 注意：本工作区即模板开发项目——可复用进模板的经验**直接改进**
> `project-template/` 与 `init-project/`，不设 EXPERIENCE-TO-TEMPLATE 暂存；
> 本文件只记录可进知识库的经验，**不混入模板内部**（模板内部另有给目标项目用的
> 同名骨架文件，见 `project-template/private/dev/EXPERIENCE-TO-KB.md`）。
- 最后更新：2026-08-25

## 索引

| 日期 | 标题 | 类型 | 状态 |
|---|---|---|---|
| 2026-08-25 | skill 派生自动化校验不覆盖摘要级过时（审计教训） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 多 agent 环境定位 skill 目录 + 派生规范安装的实操路径 | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | 从完整模板派生全局精简版 agent 规范 skill（继承矩阵+版本校验） | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | skill 版本号单一来源：正文引用 version.json + 工具自动化校验 | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | 未发版变更区段也是状态文档（HEAD 引用/条目需随提交同步） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 状态文档生命周期需要「开始/收尾双收口」 | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 版本硬事实过时与状态文档校准（审计教训） | 经验方法/教训 | 待沉淀 |

## 2026-08-25 · skill 派生自动化校验不覆盖摘要级过时（审计教训）

- 来源项目/任务：通用项目模板工作区双 skill 审计（init-project / agent-rules）
- 背景与上下文：用户反馈 init-project skill「似乎很久没有更新」。自动化校验
  （sync 哈希、metadata.version、继承矩阵覆盖/指纹、quick_validate、占位符全覆盖、
  版本 grep、路径引用）全部通过，但人工内容比对仍发现过时项。
- 需求/问题：为什么「机制完全同步」下 skill 仍会显得过时？自动化校验覆盖了
  **结构/硬事实**（版本、文件、指纹），却覆盖不了**自由文本摘要**（SKILL.md 定位
  能力清单是否列全模板新特性、措辞是否与最新策略一致）。
- 做法与过程：
  1. 逐条对照模板 CHANGELOG（v1.1.0 / v1.1.1 / 未发版区段）与 SKILL.md 定位摘要，
     找「模板已加、摘要没提」的特性：文档双模块与治理、三级质量门禁、WORKLOG
     生命周期、定案/询问清单、发布前自测、红线 15 条编号；
  2. 对照最新策略找措辞偏差：SKILL.md「自动版本递增发布」vs 模板「默认不自动发布、
     版本递增由 agent 本地执行、CI 仅对无 tag 版本发布」；
  3. 对照最新实现找「已修复但文档仍写旧行为」：P3 已给 init_project.py 加
     `_configure_utf8`，但 init-steps.md「编码提示」仍写「可能乱码、必要时设
     PYTHONUTF8=1」。
- 经验/教训：
  - 派生态（skill/精简版/镜像文档）的自动化校验解决「漂移」，不解决「摘要级
    过时」——后者需要**特性核对清单**（模板新版本的能力点列表 ↔ 派生态摘要）或
    发版时的人工比对步骤；
  - 「已修复但文档仍写旧行为」是最隐蔽的过时源：修复实现的同时必须同步搜索文档
    中对旧行为的描述（P3 修了 init_project.py，漏改了 init-steps.md 的提示）；
  - 审计「是否过时」不能只看版本号一致与校验通过，要把模板 CHANGELOG 当核对清单
    逐条对照派生文档。
- 验证/效果：审计定位 init-project 过时项 3 类（摘要缺新特性 / 策略措辞偏差 /
  编码提示未随修复更新）；agent-rules 因刚创建且含继承矩阵，仅 1 条正文硬编码建议。
- 相关文件：`init-project/SKILL.md`、`init-project/references/init-steps.md`、
  `project-template/docs/CHANGELOG.md`、`agent-rules/`、`docs/WORKLOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=文档治理/Agent 工程实践`；
  `tags=[skill, 过时审计, 派生文档, 特性核对清单, 自动化校验]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-25 · 多 agent 环境定位 skill 目录 + 派生规范安装的实操路径

- 来源项目/任务：通用项目模板工作区 agent-rules skill 实施与安装
- 背景与上下文：用户要求把新 skill 安装到五个 agent：traework、workbuddy、codex、
  dsh、qcoderwork。`<用户主目录>` 根目录枚举被拒，直接按 App 名猜路径均失败。
- 需求/问题：如何可靠定位各 agent 的用户级 skill 目录，以及沙箱写权限受限时如何
  完成安装。
- 做法与过程：
  1. 从已授权可读的子目录入手（`.codex`、`.dsh`、`.workbuddy`、`AppData\Roaming`）；
  2. **Start Menu 快捷方式是关键线索**：`*.lnk` 文件名揭示真实产品名——
     `TRAE Work CN.lnk`（traework）、`QoderWork CN.lnk`（qcoderwork）、
     `WorkBuddy.lnk`；`WScript.Shell` 可解析快捷方式目标/工作目录；
  3. 产品数据目录：TraeWork → `<用户主目录>\.trae-cn\skills`（与 Trae CN
     共用用户目录，`<工作区路径>` 只是工作区）；QoderWork →
     `<用户主目录>\.qoderwork\skills`（原目录不存在，安装时新建）；
     WorkBuddy → `.workbuddy/skills`；Codex → `.codex/skills`；DSH → `.dsh/skills`；
  4. 安装：沙箱无写权限 → 升级权限获批后 `Copy-Item -Recurse`，装完核对文件数与
     SKILL.md 哈希，确认不是「报错但显示 OK」的假成功（PowerShell 非终止错误 +
     try/catch 会误报 OK，必须用文件数/哈希验证）。
- 经验/教训：
  - 定位未知应用的数据目录：优先看 Start Menu 快捷方式（真实产品名）→ 解析目标 →
    再按 `~/.<product>` 与 `AppData\Roaming\<Product>` 排查，比盲目猜路径高效；
  - 同系列产品可能共用用户目录（TRAE Work 与 Trae CN 共用 `.trae-cn`），不要按
    字面名猜目录；
  - PowerShell `Copy-Item` 的访问拒绝是非终止错误，try/catch 不会捕获——安装类
    操作成功与否必须以「文件数 + 哈希」复核，不能只看 OK 输出；
  - 全局规范类 skill 安装到多 agent 时，把「安装位置表」写进工作区 README，
    便于复现与后续更新。
- 验证/效果：五处均安装 4 文件、SKILL.md 哈希一致；quick_validate 通过。
- 相关文件：`agent-rules/`、`README.md`（使用方法 4）、`docs/WORKLOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=本机环境/Agent 工程实践`；
  `tags=[skill 安装, 多 agent, Windows, 目录定位, 沙箱权限]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-25 · 从完整模板派生全局精简版 agent 规范 skill（继承矩阵+版本校验）

- 来源项目/任务：通用项目模板工作区新需求方案设计（agent-rules 精简版要求 skill）
- 背景与上下文：通用项目模板的规范体系完整但体量庞大（两份 AGENTS + docs/ +
  scripts/ + private/dev 文档体系），面向「项目」场景。用户希望给**每个 agent 的
  所有非纯聊天对话**提供一份精简版要求 skill：不依赖项目结构、随模板每版本更新、
  除项目专属规定外一律继承。
- 需求/问题：如何从「项目级完整规范」派生「全局精简规范」，并保证两者不漂移——
  精简版既不能只是机械摘抄（大量【通用】内容是项目机制：private 子 git、
  version.json、CI/CD、WORKLOG 等文件体系，非项目场景不适用），也不能手工维护
  导致漏更。
- 做法与过程（方案设计）：
  1. 边界划分：**继承原则、裁剪机制**——15 条红线/工作流/文档治理/审计/完成清单
     以「原则」形式继承并通用化（如阶段落盘从「更新 private/dev/WORKLOG.md」改为
     「更新项目进度文档或向用户落盘」）；private 子 git、版本发布、CI/CD、模板
     升级等**项目机制**不进入精简版（在项目内由项目 AGENTS.md 覆盖）；
  2. 独立 skill 目录（`agent-rules/`，与 init-project 平级），SKILL.md 自包含
     规范正文 + 触发规则（非纯聊天即加载）+ 冲突优先级（项目规范优先）；
  3. **继承矩阵**（references/inheritance-map.md）作为唯一维护依据：模板红线/
     章节 ↔ 精简条目 ↔ 是否通用化改写 ↔ 核对版本；
  4. **版本一致性校验挂到 sync_template.py**：metadata.version == template_version
     + 继承矩阵覆盖完整性（模板红线条数/编号变更 → sync 失败），把「随版本更新」
     从人工约定升级为工具强制。
- 经验/教训：
  - 派生/精简类规范的核心风险是**漂移**：解决靠「显式继承矩阵 + 自动化校验」，
    而不是复制粘贴时的手工小心；
  - 「继承」要区分**原则**与**机制**：项目机制裁剪掉，但机制背后的原则
    （进度落盘、可恢复删除、先对齐后实施）保留并通用化，才是真正的继承；
  - 全局 skill 的触发规则要写进 description 且覆盖面广（「非纯聊天」），
    并让项目级规范声明优先级，避免双规范冲突。
- 验证/效果：方案阶段（待用户确认后实施验证）；审计确认当前 sync/校验机制可扩展。
- 相关文件：`project-template/AGENTS.md`、`project-template/private/AGENTS.md`、
  `docs/audit-checklist.md`、`scripts/sync_template.py`、`docs/WORKLOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=项目管理/Agent 工程实践`；
  `tags=[skill, 规范派生, 继承矩阵, 版本同步, 自动化校验]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-25 · skill 版本号单一来源：正文引用 version.json + 工具自动化校验

- 来源项目/任务：通用项目模板工作区 P3 建议实施（全面审计注释反馈）
- 背景与上下文：`init-project/SKILL.md` 的 `metadata.version` 与
  `references/init-steps.md` 正文都硬编码模板版本 1.1.1；skill 清单要求 frontmatter
  静态版本（`quick_validate.py` 只校验 frontmatter 键，不校验版本一致性），发版时
  需手动维护多处，靠「全局 grep」兜底。
- 需求/问题：内嵌版本号如何在「skill 元数据必须静态」与「避免多处手工维护漂移」
  之间取得平衡。
- 做法与过程：
  1. 保留 `SKILL.md metadata.version`（skill 清单必需、静态）；
  2. 文档正文（SKILL.md 校验清单、init-steps.md 校验清单）不再写死版本号，改为
     引用 `assets/project-template/version.json` 的 `template_version` 字段
     （单一事实来源）；
  3. 在 `scripts/sync_template.py` 中新增校验：`SKILL.md metadata.version` 必须等于
     `project-template/version.json` 的 `template_version`，不一致则 sync 失败——
     把「人工 grep 核对」升级为「工具强制校验」。
- 经验/教训：
  - 「单一来源」不必追求字面上只有一处：对**必须静态**的元数据（如 skill
    frontmatter），保留静态值 + 用**自动化校验**保证其与权威来源一致，比在正文里
    到处引用更可靠；
  - 版本/元数据一致性检查应挂在现有工具链入口（sync/CI）上，而不是只靠文档约定；
  - 文档正文优先写「到哪里查」而不是「当前值」，可显著减少硬事实过时。
- 验证/效果：改后 `grep 1.1.1` 在 SKILL/init-steps 仅剩 metadata.version；sync 实测
  通过（1.1.1==1.1.1）；人为改错版本时 sync 会失败（校验生效）。
- 相关文件：`scripts/sync_template.py`、`init-project/SKILL.md`、
  `init-project/references/init-steps.md`、根 `AGENTS.md`、`README.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=项目管理/工程实践`；
  `tags=[版本管理, 单一来源, 自动化校验, skill]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-25 · 未发版变更区段也是状态文档（HEAD 引用/条目需随提交同步）

- 来源项目/任务：通用项目模板工作区全面审计（第二次）
- 背景与上下文：`docs/CHANGELOG.md`「未发版变更（v1.1.2 候选）」区段标注
  「HEAD 733065f」，实际 HEAD 已前进到 3006b97（其后两次提交：WORKLOG 生命周期
  收口规则补强、经验自动沉淀），且区段条目缺最近一次提交（经验自动沉淀）的变更内容。
- 需求/问题：未发版区段本质上也是**状态文档**——它引用「当前 HEAD」并列举
  「已完成但未发版的变更」；若只在创建时写一次、后续提交不更新，就会与仓库实际
  状态脱节，形成新的硬事实过时源。
- 做法与过程：
  1. 审计时用 `git log --oneline --decorate -8` 核对 HEAD 与 tag 指向；
  2. 把未发版区段内容与 HEAD 之后各次提交主题逐一比对，找出缺失条目；
  3. 修复：补充「经验自动沉淀」条目；并**移除区段的 HEAD 固定引用**（改为不依赖
     提交号的表述，以提交记录为准），从根上避免每次提交后再次过时；WORKLOG 当前
     任务同步切换为本次审计任务（生命周期收口规则）。
- 经验/教训：
  - 未发版/待发布类状态区段应**避免固定提交号**（推荐不写 HEAD、以提交记录为准）；
    确需写时，每次提交后顺手校准，至少任务收尾/汇报前回读核对一次——与 WORKLOG
    生命周期收口同理；
  - 审计硬事实 grep 范围应同时包含**提交号/版本号**（`git log` 对照），而不只是
    版本号字符串；
  - 未发版清单建议只列面向用户的变更要点，避免把工作区内部文档修复（如 WORKLOG
    自身校准）全部计入，防止区段膨胀与混淆。
- 验证/效果：修复后区段不再依赖提交号，不会随后续提交过时；条目与提交记录一致。
- 相关文件：`docs/CHANGELOG.md`、`docs/WORKLOG.md`、`docs/EXPERIENCE-TO-KB.md`（本文件）
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=项目管理/文档治理`；
  `tags=[文档治理, CHANGELOG, 版本管理, 审计]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-25 · 状态文档生命周期需要「开始/收尾双收口」

- 来源项目/任务：通用项目模板工作区全面审计 + P2 修复（WORKLOG 维护问题根因排查）
- 背景与上下文：审计发现 WORKLOG 两处维护问题——阶段记录硬事实错误
  （sync 29 vs 实际 28 文件）与「当前任务」未随新任务切换。排查现有规范发现
  红线 14（阶段落盘）、红线 12（过时即修）**已存在**，问题仍发生。
- 需求/问题：状态文档（WORKLOG）在**任务边界**失守——只规定了「过程中更新」，
  没有覆盖「任务开始（切换当前任务）」与「任务收尾（校准硬事实）」两个边界。
- 做法与过程：
  1. 排查根因：现有规则只有「每完成一小阶段先更新」和「清理需询问」，缺两个
     显式收口——新任务开始先切换当前任务、任务收尾回读校准硬事实；
  2. 修复：WORKLOG 硬事实 29→28、当前任务切换、CHANGELOG 补「未发版变更」区段；
  3. 规则补强（模板级，新项目继承）：WORKLOG 使用规则扩展为四条（阶段即时更新 /
     开始切换当前任务 / 写入后回读校准 / 收尾核对）；完成检查清单与 audit-checklist
     增加「当前任务已切换、阶段记录硬事实与实际一致」检查项。
- 经验/教训：
  - 状态文档治理要有**生命周期视角**：除「过程中更新」外，必须显式覆盖
    「开始（切换当前任务）」与「收尾（校准硬事实）」两个边界；只规定过程更新
    会在边界失守。
  - 阶段记录不要**预填 ✅**：写入后必须回读校准，硬事实（文件数、版本号、提交号）
    以实际仓库状态为准，环境变化后立即修正。
  - 完成检查清单/审计清单要包含状态文档的「生命周期合规」检查项，让收口可被复核。
  - 经验沉淀是**每轮对话结束后的必做动作**（不是可选项、不需要询问）：agent 自动
    把完整候选经验写入本文件，沉淀与否、沉淀到哪由用户决定。
- 验证/效果：修复后 WORKLOG 硬事实与实际一致；规则补强已同步进模板
  （`project-template/private/dev/WORKLOG.md` 等），初始化出的新项目直接继承。
- 相关文件：`docs/WORKLOG.md`、`docs/EXPERIENCE-TO-KB.md`（本文件）、根 `AGENTS.md`、
  `project-template/private/dev/WORKLOG.md`、`project-template/private/AGENTS.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=项目管理/文档治理`；
  `tags=[文档治理, WORKLOG, 工作流, 审计]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-25 · 版本硬事实过时与状态文档校准（审计教训）

- 来源项目/任务：通用项目模板工作区全面审计 + 修复整理（v1.1.1 之后）
- 背景与上下文：v1.1.1 发版完成后审计，发现 3 处文档内嵌版本号仍为 1.1.0
  （根 AGENTS.md、`init-project/SKILL.md`、`init-project/references/init-steps.md`），
  且 WORKLOG 阶段状态（「提交+tag 待执行」）与实际 git 状态
  （commit `1e02c3e` + tag `v1.1.1` 已存在）矛盾。
- 需求/问题：文档中的硬事实（版本号、完成状态）容易在发版/任务收尾时漏更，
  造成校验误判（按过时版本号核对 `version.json` 的 `template_version` 会误报
  不一致）与状态失真。
- 做法与过程：
  1. 发版后做「版本号全局 grep」：搜索旧版号与新版的全部出现位置，逐一核对
     （元数据、正文、校验清单、文档示例），确认只应出现在历史记录/CHANGELOG 中。
  2. 状态文档与实际仓库状态交叉核对：WORKLOG「阶段记录」对照 `git log`/`git tag`，
     任务实际完成后立即将阶段标为 ✅，防止「待办已完结」与「阶段 🔄」自相矛盾。
  3. 修复后把「版本号全局 grep」写入发版同步约定，作为强制步骤防复发。
- 经验/教训：
  - 发版清单必须包含「全局 grep 新旧版本号」；版本号尽量用占位符或单一维护点，
    避免同一事实在多处手工维护。
  - 状态文档（WORKLOG）以仓库实际状态为准：任务收尾时先核对 git 再更新文档，
    不留「文字说待办、实际已完成」的中间态。
  - 全面审计时，自动化验证（同步哈希比对、skill 校验、语法编译、初始化冒烟、
    非空目录拒绝、版本递增、发布前检查）比人工读文档更能发现硬事实问题；
    建议审计先跑自动化，再人工核对文档引用。
- 验证/效果：修复后 grep `1.1.0` 仅剩历史记录/CHANGELOG 中的合法引用；
  quick_validate 通过；同步 29 文件 0 差异；初始化冒烟通过。
- 相关文件：`docs/WORKLOG.md`、`docs/EXPERIENCE-TO-KB.md`（本文件）、根 `AGENTS.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=项目管理/文档治理`；
  `tags=[文档治理, 版本管理, 审计]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：
