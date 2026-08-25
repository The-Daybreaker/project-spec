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
| 2026-08-26 | 删除纪律命名统一为产品名（只举例不设列表） | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | init-project 首次安装 + skill 目录位置复盘（qcoderworkcn） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | skill 触发语义变更的同步点清单（含用户直接改副本的处理） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | skill 派生自动化校验不覆盖摘要级过时（审计教训） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 多 agent 环境定位 skill 目录 + 派生规范安装的实操路径 | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | 从完整模板派生全局精简版 agent 规范 skill（继承矩阵+版本校验） | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | skill 版本号单一来源：正文引用 version.json + 工具自动化校验 | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | 未发版变更区段也是状态文档（HEAD 引用/条目需随提交同步） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 状态文档生命周期需要「开始/收尾双收口」 | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 版本硬事实过时与状态文档校准（审计教训） | 经验方法/教训 | 待沉淀 |

## 2026-08-25 · skill 触发语义变更的同步点清单（含用户直接改副本的处理）

- 来源项目/任务：通用项目模板工作区 agent-rules 触发词修改与同步
- 背景与上下文：用户把 agent-rules 触发语义从「任何非纯聊天对话都加载」收紧为
  「仅非项目（不在任何项目/工作区内）且非纯聊天才加载，项目内不加载」，直接改了
  仓库 `agent-rules/SKILL.md` 与 `agents/openai.yaml`（未提交）；Codex 已安装副本
  用户也同步了，其余四个 agent 副本仍是旧版。
- 需求/问题：规则/触发类语义变更后，哪些位置必须同步？用户直接改副本时如何避免
  覆盖其改动、并保证多副本一致？
- 做法与过程：
  1. 先 `git status` / `git diff` 确认用户改动的确切范围（仓库两个文件、Codex 副本
     已一致），再哈希比对五个已安装副本，找出仍旧的（dsh / workbuddy / trae-cn /
     qoderwork）；
  2. 盘点承载触发语义的全部位置：SKILL.md `description` 元数据 + 正文「触发与
     优先级」、`agents/openai.yaml` `short_description`、README 目录树注释 + 使用
     方法、根 AGENTS.md 目录概览 + 文档职责表、docs/CHANGELOG 未发版区段、五个
     已安装副本；
  3. 逐处同步为「仅非项目且非纯聊天加载；项目内不加载（以项目 AGENTS.md 为准）」，
     最终统一从仓库重装到五个副本并哈希复核。
- 经验/教训：
  - 触发/规则类语义的同步面 = 元数据 description + 正文规则 + 平台接口描述 +
    工作区文档（README/AGENTS/CHANGELOG）+ **所有已安装副本**，缺一处就会造成
    各 agent 行为不一致；
  - 用户直接改副本时：先 diff 再传播，不要把仓库旧版覆盖用户改动；以用户改动为
    准回灌仓库，再统一分发；
  - 「仅在某条件下加载」的触发词应同时写清「例外」（项目内不加载、纯聊天不加载），
    避免模型误判；
  - 旧说明/废案按用户规定**直接删除**，不写「已取代/旧行为」类替代表述
    （与模板文档治理一致，用户强调执行）。
- 验证/效果：五处副本与仓库哈希一致；sync / quick_validate 通过。
- 相关文件：`agent-rules/SKILL.md`、`agent-rules/agents/openai.yaml`、`README.md`、
  `AGENTS.md`、`docs/CHANGELOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=Agent 工程实践/文档治理`；
  `tags=[skill, 触发语义, 多副本同步, 变更同步清单]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 删除纪律命名统一为产品名（只举例不设列表）

- 来源项目/任务：通用项目模板工作区删除纪律命名修正
- 背景与上下文：`_trash/<agent名>_<日期>_<时分>/` 中「agent 名」有歧义——多 agent
  协作线程里主 agent 标识名是 `root`（非产品名 `codex`），导致临时删除区命名为
  `root_2026-08-25_*`，与用户预期不符。
- 需求/问题：命名约定既要消除歧义，又不能因为写死本机五个 agent 列表而失去
  通用性（模板会被其他机器/项目使用）。
- 做法与过程：
  1. 与用户确认：统一为**执行 agent 的产品名**，可举例（`codex_2026-08-25_2330`），
     但**不设固定 agent 列表**；
  2. 全局 grep `_trash/<agent` 找到 9 处正文（工作区 AGENTS×2、模板根 AGENTS 红线 4、
     模板私有 AGENTS×2、DOCS、audit-checklist、DESIGN、README、init-project SKILL、
     agent-rules SKILL），统一替换为 `<agent产品名>` 表述；
  3. 红线 4 正文变化 → 重新计算指纹更新继承矩阵 → sync 校验通过（机制实际生效）。
- 经验/教训：
  - 约定里的「标识」字段（agent 名）若与多 agent 环境内部名冲突，应明确为**面向
    用户可识别的产品名**，并允许举例、禁止写死列表，保证模板跨机器通用；
  - 「只举例不设列表」是通用规范的好写法：例子帮助理解，列表限制复用；
  - 指纹校验机制在本次变更中自动拦截旧指纹 → 强制同步继承矩阵，验证了防漂移设计。
- 验证/效果：9 处正文统一；sync 通过（红线 4 指纹 ee28329cc7e5）；quick_validate ×2；
  两 skill 五处副本重装哈希一致。
- 相关文件：`AGENTS.md`、`project-template/AGENTS.md`、
  `project-template/private/AGENTS.md`、`agent-rules/`、`README.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=文档治理/工程实践`；
  `tags=[删除纪律, 命名约定, 通用性, 产品名]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

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
     `<用户主目录>\.qoderworkcn\skills`（真实用户目录为 qcoderworkcn，
     早期误用 `.qoderwork`，经用户反馈后纠正并清理）；
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

## 2026-08-25 · init-project 首次安装 + skill 目录位置复盘（qcoderworkcn）

- 来源项目/任务：通用项目模板工作区 init-project 同步安装
- 背景与上下文：此前只把 agent-rules 装到了五个 agent，`init-project` 从未安装；
  且 QoderWork 的 skill 目录误装在 `~/.qoderwork/skills`，用户反馈实际目录是
  `~/.qoderworkcn/skills`（`<用户主目录>\.qoderworkcn` 存在且含空 `skills/`）。
- 需求/问题：多 agent 场景下，同一套 skill（init-project / agent-rules）如何
  一次性、可验证地分发到全部目标，且目录位置必须与各产品真实数据目录一致。
- 做法与过程：
  1. 先核对 `init-project` 在五个 skill 目录的存在性（全部 False），并确认
     `.qoderworkcn` 为 QoderWork CN 真实用户目录（含 `skills/`、`projects/`、
     `bin/` 等）；
  2. 一次升级权限命令完成：init-project × 5（每处 33 文件）+ agent-rules 移至
     `.qoderworkcn/skills` + 误装 `.qoderwork/skills` 移入 `_trash` 并进回收站；
  3. 用「文件列表 + 哈希」对两个 skill × 五处逐一复核，确认与仓库一致。
- 经验/教训：
  - 「安装 skill 到各 agent」是**两个 skill 都要装**，别只装新做的那个；发版/
    安装后应有一张「skill × agent × 位置」核对表（README 已更新为双 skill 表）；
  - 用户对目录位置的反馈优先于自行推断：`.qoderwork` 与 `.qoderworkcn` 极易混淆，
    安装前先向用户确认或直接列出候选让其指定；
  - 已安装位置表写入 README 后，用户能一眼发现路径错误，是纠错最快途径。
- 验证/效果：init-project / agent-rules 各五处哈希一致；误装目录已清理；
  README 安装表更新为双 skill + 正确路径。
- 相关文件：`README.md`（使用方法 4）、`docs/WORKLOG.md`、`docs/CHANGELOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=本机环境/Agent 工程实践`；
  `tags=[skill 安装, 多 agent, 目录纠错, qcoderworkcn]`；`project=通用项目模板`
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
