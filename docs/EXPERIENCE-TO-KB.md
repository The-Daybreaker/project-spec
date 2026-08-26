# EXPERIENCE-TO-KB — 可沉淀进知识库的经验（工作区母项目）

> 模块：项目专用（工作区）。
> 用途：记录本工作区（通用项目模板母项目）产生的**经验方法/教训/方案**候选，
> 供后续按知识库规范（如适用）沉淀。每轮对话结束后由 agent 将**完整候选经验**
> 写入本文件；沉淀时以本文件为唯一依据，不需要重读整个项目。入库时由知识库流程
> 决定归属（本文件不预设位置）。
> 注意：本工作区即模板开发项目——可复用进模板的经验**直接改进**
> `project-template/` 与 `skills/init-project/`，不设 EXPERIENCE-TO-TEMPLATE 暂存；
> 本文件只记录可进知识库的经验，**不混入模板内部**（模板内部另有给目标项目用的
> 同名骨架文件，见 `project-template/private/dev/EXPERIENCE-TO-KB.md`）。
- 最后更新：2026-08-26

## 索引

| 日期 | 标题 | 类型 | 状态 |
|---|---|---|---|
| 2026-08-26 | v1.4.0 整体架构重构：引导式需求讨论 + 阶段模块化/渐进披露/STATUS 快照（可观察性模式）+ 三坑实录 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | v1.3.2 三域并行独立审计：照抄即失败缺陷最优先 + sync installed≠source 中间态预期 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | v1.3.1 发版后独立子代理审计全绿：自动化验证+文档硬事实核对方法 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | v1.3.1 src/ 代码区实体化：分区约定提通用性 + IDE 文件锁下 sync 兜底重试 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | v1.3.0 模板增强：红线16（规则为主+比喻为辅）+ 图可视化规范（挂靠阶段、先出图再确认）+ skills 目录合并 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | 第七轮审计修复 + v1.2.2 发版收口：sync 先于安装 / private 骨架强制跟踪核实 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | TRAE IDE 内存视图覆盖磁盘编辑：SearchReplace 成功后须整篇回读核对 | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | TRAE 沙箱写边界实测（新建可/覆盖删复制拒）+ 用户放行协作流程 | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | 第六轮审计：发版重装漏项（agent-rules 六副本漂移）+ 子代理通道失效自审兜底 | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | v1.2.1 发版 + 母项目发版不能用 bump_version.py 的教训 | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | P3 批量修复：文档/配置/脚本一致性收口（T2-T8，T5 跳过） | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | T1 升级路径修复 + 同步面约束机制根因（UPGRADE B 区骨架迁移） | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | 全流程审计（第五轮）：升级路径/初始化输出面/一致性硬事实核对 | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | init-project 初始化流程更新（审计后续补 v1.2.0 特性） | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | 全面审计（第四轮）：对话展示未落库导致的声称失真 | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | 流程展示要求：缩写附中文翻译 + 流程图体现文档更新流程 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | 开发前规范实施落地：四登记册 + check_dev_docs + 流程提示（v1.2.0） | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | 开发前规范（PRD/RFC/ADR）C 档方案设计 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | 工作流缺陷修复：sync 覆盖校验 + 初始化落地路线图 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | init-steps 校验清单未覆盖新实体（发版后遗漏检查实例） | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | 模板实体目录与「双置顶」维护约定 + 测试落地指引 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | 模板生命周期补齐：dist 产物约定 + 项目归档/退役流程 | 经验方法/方案 | 待沉淀 |
| 2026-08-26 | 全面审计第三轮：自动化全绿下仍复发的维护级缺陷（审计教训） | 经验方法/教训 | 待沉淀 |
| 2026-08-26 | 删除纪律命名统一为产品名（只举例不设列表） | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | skill 触发语义变更的同步点清单（含用户直接改副本的处理） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | skill 派生自动化校验不覆盖摘要级过时（审计教训） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 多 agent 环境定位 skill 目录 + 派生规范安装的实操路径 | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | init-project 首次安装 + skill 目录位置复盘（qcoderworkcn） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 从完整模板派生全局精简版 agent 规范 skill（继承矩阵+版本校验） | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | skill 版本号单一来源：正文引用 version.json + 工具自动化校验 | 经验方法/方案 | 待沉淀 |
| 2026-08-25 | 未发版变更区段也是状态文档（HEAD 引用/条目需随提交同步） | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 状态文档生命周期需要「开始/收尾双收口」 | 经验方法/教训 | 待沉淀 |
| 2026-08-25 | 版本硬事实过时与状态文档校准（审计教训） | 经验方法/教训 | 待沉淀 |

## 2026-08-26 · v1.4.0 整体架构重构：引导式需求讨论 + 阶段模块化/渐进披露/STATUS 快照（可观察性模式）+ 三坑实录

- 来源项目/任务：通用项目模板工作区（整体架构重构，D1-D15 定稿实施，v1.4.0 候选）
- 做法：
  1. **引导式需求讨论**（用户硬性偏好）：agent 不抛选项，先复述意图 + 提开放问题
     引导用户发现真正需求（痛点溯源→阶段粒度→披露深度→恢复机制→切换节奏逐层
     收敛）；用户原话「分阶段为了专注、分子阶段为了细化」成为设计原则。此方法论
     已回写模板 P1 需求阶段（禁抛选项）。
  2. **可观察性模式**：阶段卡 = 合规检查点（进度 + 生命周期合规清单 + 下一阶段
     输入预告）——用户一眼验证「任务完成 + 生命周期走完 + 按规范」；决策型阶段/
     子阶段须确认、执行型展示即走；双维度模型（主流程串行 + 贯穿动作各有状态机
     不占阶段）化解「严禁跨阶段 vs 文档同步贯穿」冲突。
  3. **STATUS 快照化**：WORKLOG 从「日志（追加历史）」改为「状态快照（只存最新）」，
     历史由 git 承担；中断恢复 = 读 STATUS 阶段卡 + 按影响清单/要读清单续上
     （渐进式披露不失效）。文档天然隔离：阶段边界=披露边界，阶段间只传产物。
- 关键发现模式：
  - **三坑实录**：① quick_validate 用 `description:\s*(.+)` 只取第一行——YAML 折叠
    块 `>-` 被误读为 description 含 `>` 而校验失败，description 必须单行；
    ② `re.search(r"(?m)...")` 中 `(.*?)` 默认不跨行，section 提取须 `(?ms)`（丢
    DOTALL 会静默匹配空串）；③ sync 全量镜像用 rmtree+copytree 会触发批量删除
    安全钩子，改**增量镜像**（删多余+复制变更+清空目录）更安全且不打断。
- 可复用点：项目流程重构（阶段模块化+可观察性）、文档治理（快照化+渐进披露）、
  引导式需求方法论均可进知识库；同步脚本避免 rmtree、description 单行化是通用教训。

## 2026-08-26 · v1.3.2 三域并行独立审计：照抄即失败缺陷最优先 + sync installed≠source 中间态预期

- 来源项目/任务：通用项目模板工作区（模板 v1.3.2 全生命周期专业审计发版）
- 做法：3 个**独立子代理**并行分域审计（不共享主对话上下文）：A=规范与文档语言、
  B=脚本与机制、C=流程闭环与生命周期；各输出 P0-P3 清单 + 总体结论；修复范围
  分级交用户决策（P1 必修 + P2 全修 + P3 精选），设计权衡类（如跨脚本公共函数
  抽取）只记录不改，避免为一致性牺牲单文件可分发特性。
- 关键发现模式：「**示例 vs 校验器**」配对核对——RFC 骨架示例写「依据 PRD-XXXX」
  而 `check_dev_docs.py` 校验要求「依据 PRD：」，新项目照抄骨架登记必被拦截，
  属「照抄模板即失败」类最高优先级缺陷（P1）。文档一致性审计不能只查文档互相
  引用，必须把骨架示例与其校验规则成对检查。
- 发版链中间态预期：版本递增后 sync 报 `installed='旧版' source='新版'` 属**预期
  中间态**（六处副本尚未重装），先重装再跑 sync 即全绿——报错信息本身可当重装
  清单用（逐目录 × 逐 skill 列出差异文件）；WinError 32 IDE 文件锁按已知坑兜底
  （等待约 25 秒重试成功，partial mirror 下次覆盖）。
- 结果：P1×3 + P2×7 + P3×6 共 16 项修复落地，v1.3.2 发布（发布提交 17a0927 +
  附注 tag）；sync 全绿（38 文件 / 版本哨兵 / 继承矩阵 / init-steps 覆盖度 /
  六处副本哈希）、py_compile 8 OK、冒烟验证修复行为生效。

## 2026-08-26 · v1.3.1 发版后独立子代理审计全绿：自动化验证+文档硬事实核对方法

- 来源项目/任务：通用项目模板工作区（v1.3.1 发版后全面审计）
- 背景与上下文：用户要求派子 agent 全面审计；独立子代理不共享主对话上下文，
  只给路径/清单/验证命令，全绿通过（P0/P1 零项），仅 P2 流程态 + P3 pyc 残留。
- 方案要点（审计方法论，可复用）：
  1. **独立审计必跑自动化链 + 文档硬事实对照**：sync（镜像+版本+指纹+装载校验）、
     verify（副本哈希）、quick_validate×2、py_compile、版本/指纹 grep、git
     log/tag/status——先验证「机器可说的」，再人工核对「机器不说但会过时的」：
     CHANGELOG 新在前、EXP-KB 双置顶、WORKLOG 阶段硬事实、UPGRADE 迁移要点。
  2. **文件数口径要按 verify 的 SKIP_NAMES 对齐**：Get-ChildItem -Recurse -File
     会把 `__pycache__/*.pyc` 计入，导致「42 文件」读到 43；核对硬事实前先扣除
     被排除项，避免误报。
  3. **流程态判定**：审计启动时 WORKLOG「当前任务切换」未提交属正常中间状态
     （不是缺陷），随审计收尾一并提交即可。
- 验证/效果：审计结论通过；处理后 git 干净、verify exit 0。
- 相关文件：docs/WORKLOG.md（阶段 55）、docs/EXPERIENCE-TO-KB.md、六处 agent 目录。

## 2026-08-26 · v1.3.1 src/ 代码区实体化：分区约定提通用性 + IDE 文件锁下 sync 兜底重试

- 来源项目/任务：通用项目模板工作区（模板 v1.3.1 发版）
- 背景与上下文：用户要求「模板文件夹分区，项目代码区和其他区分开」提高通用性，
  并建议直接在模板根加 src/ 目录、规定源码都放里面；原模板三区表虽 mention src/
  但无实体目录。
- 方案要点：
  1. **实体占位即约定载体**：`src/.gitkeep` 内含一行代码区说明（业务源码入
     src/、根目录不放业务代码），随初始化存在；「代码区/工程区」分区约定写在根
     AGENTS 项目概览 + README 结构树 + DESIGN 项目形态三处（正文=当前状态）。
  2. **通用性提升**：模板只规定「代码进 src/」，子目录按技术栈自定（backend/sdk/
     assets…），测试位置从宽——不绑定具体语言/布局。
  3. **IDE 文件锁 + P3-2 兜底**：sync 的 rmtree+copytree 在 IDE 占用
     `assets/.../.gitignore` 时报 WinError 32（partial mirror left）；等 20s 释放
     后重试即成功——发版链的兜底设计按预期工作，锁是暂时性的，不要改代码、
     直接重试。
- 验证/效果：sync 38 文件 0 差异（含六处副本校验）、quick_validate ×2 valid、
  py_compile 8 OK、冒烟（src/.gitkeep 生成、template_version=1.3.1、check_dev_docs
  0）；六处副本重装（init-project 42 文件 / agent-rules 4 文件）哈希一致；发布
  提交 + tag v1.3.1。
- 相关文件：project-template/src/.gitkeep（新建）、project-template/AGENTS.md
  （项目概览）、project-template/README.md（结构树）、project-template/private/dev/
  DESIGN.md（项目形态）、skills/init-project/references/init-steps.md、
  scripts/sync_template.py（INIT_STEPS_COVERAGE）。

## 2026-08-26 · v1.3.0 模板增强：红线16（规则为主+比喻为辅）+ 图可视化规范（挂靠阶段、先出图再确认）+ skills 目录合并

- 来源项目/任务：通用项目模板工作区（模板 v1.3.0 发版）
- 背景与上下文：用户提出三个密集需求——①红线规避「AI 过度添加 + 被纠正后写
  『（无 X）』辩护说明」现象；②补原型设计（页面原型/design 文件）；③两个 skill
  合并到 skills/。讨论中用户又提前了「架构图/流程图可视化规范化」（改架构/流程
  必须用图展示、确认后执行），与原型需求合并讨论，最终统一为「图可视化规范」。
- 方案要点（可直接复用）：
  1. **比喻性红线的写法：规则为主、比喻为辅**——红线标题可用短助记（如
     「按单办事、不加菜；撤菜不解释」）帮人类记忆，但正文必须是可执行规则
     （越界=先询问；被指出=直接删、禁止为未做之事写说明）；比喻的语义对 AI 执行
     帮助有限，AI 靠正文执行。
  2. **新环节不新增节点、挂靠既有阶段**——用户否定了「统一可视化环节」：页面
     原型（界面）、架构图（结构）、流程图（流程）分属不同阶段，各挂靠 PRD/RFC/
     ADR/DESIGN 吸收，16 节点数保持；门禁=开发工作流步骤 + 完成清单/审计清单
     双落点（不新增红线）。新增范围内容优先考虑「不破坏既有不变量（节点数）」
     的落法。
  3. **图文件单文件落库、随所属文档同目录**（Mermaid/SVG 文本化为主，可版本化、
     AI 可生成/复述）；页面原型单开 `prototype/` 轻量目录（无状态机、不入
     check_dev_docs 校验，避免第五登记册过度复杂化；新增实体骨架入
     INIT_STEPS_COVERAGE，防止初始化镜像缺文件）。
  4. **skills 目录等内部重构成本低**：移动源目录 + 更新脚本路径常量/安装表
     source/文档引用，已安装副本内容与目录名不变、无需停机；`install-targets.json`
     的 source 字段即单一真相。
- 验证/效果：sync 37 文件 0 差异 + 继承矩阵红线 16 行（指纹 1a89754aa5ba 按
  sync 规范化逻辑从文件实算）；quick_validate ×2 valid；py_compile 8 OK；冒烟
  （prototype README 生成、template_version=1.3.0、pre_release 占位拦截+放行）；
  六处副本重装（init-project 41 文件 / agent-rules 4 文件）哈希一致；发布提交
  0613dda + tag v1.3.0。
- 教训：shell 字符串传反引号会被吞（指纹计算必须从模板文件按 sync 同逻辑提取，
  不能手打正则里的反引号文本）。
- 相关文件：project-template/AGENTS.md（红线 16）、project-template/private/AGENTS.md
  （工作流「可视化确认」）、skills/init-project/references/init-steps.md、
  skills/agent-rules/references/inheritance-map.md、scripts/sync_template.py、
  install-targets.json、project-template/private/dev/prototype/README.md。

## 2026-08-26 · 第七轮审计修复 + v1.2.2 发版收口：sync 先于安装 / private 骨架强制跟踪核实

- 来源项目/任务：通用项目模板工作区（第七轮全面审计修复，P1+P2+P3 全部，发版 v1.2.2）
- 背景与上下文：t5 安装被沙箱拦截搁置、用户放行后补装；t7 发版链验证全过；
  t8 发布提交 01435a0 + 附注 tag v1.2.2。
- 需求/问题：安装与 sync 的先后顺序？private 骨架如何提交？审计报告文件是否入仓库？
- 做法与过程：
  1. sync 先于安装：t5 首次安装在 sync 前，导致六处 init-project 持旧资产镜像
     （18 文件差异）→ 重新 sync 后二次重装六处，再 sync 全绿闭环；
  2. 核实「工作区不建 private 子 git」设计：`git -C project-template/private`
     rev-parse --show-toplevel 落回主仓库属正常现象；private 骨架凭
     `git add -f` 强制跟踪进主仓库，t8 只需主仓库一次提交（含 private 与资产镜像）；
  3. `git ls-files | grep 审计` 取证：审计报告文件历史一律不入仓库 → 本次同样
     保持未跟踪（仅工作区交付物）；
  4. 发布提交 + 附注 tag，`git tag --points-at HEAD` 核对。
- 经验/教训：
  - 发版链「更新资产镜像 → 安装副本 → 再校验」顺序不可逆；安装后必须再过一次
    sync/verify 闭环，否则同旧内容也测不出差异（版本哨兵兜底）;
  - private 子 git 的有无以 `rev-parse --show-toplevel` 实测为准，不要凭文档名称
    假设；工作区既有既定设计（强制跟踪主仓库）就按其提交；
  - 审计/需求原始交付物（如审计报告 md）是否入库应由仓库惯例决定（git ls-files
    取证），不要默认 `git add -A` 全纳入。
- 验证/效果：提交 01435a0（49 files）+ tag v1.2.2 指向 HEAD；工作树仅剩未跟踪
  审计报告；六处副本 v1.2.2 哈希复核通过（t5/t7）。
- 相关文件：scripts/sync_template.py、install-targets.json、docs/CHANGELOG.md、docs/WORKLOG.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=版本管理/发布`；
  `tags=[发版链, 顺序依赖, sync, 强制跟踪, git add -f]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · TRAE IDE 内存视图覆盖磁盘编辑：SearchReplace 成功后须整篇回读核对

- 来源项目/任务：通用项目模板工作区（第七轮审计修复 t8 收尾；历史 t2 曾复发）
- 背景与上下文：对 `docs/WORKLOG.md` 与 `docs/CHANGELOG.md` 执行 SearchReplace，
  diff 输出显示成功；随后整篇 Read 发现部分 hunk 仍是旧内容（被 IDE 内存视图
  回写覆盖）；另一次改用过短 old_str 的替换还产生新旧内容拼接的脏行。
- 需求/问题：如何确认编辑真正落盘、避免脏拼接？
- 做法与过程：
  1. 每次 SearchReplace 后立即 Read 整篇/涉及区间核对，不只看 diff 输出；
  2. 覆盖复发时重做替换，且 old_str 取足够长的唯一块，避免部分匹配拼接；
  3. 同文件多 hunk 分批编辑、每批后回读，缩小被覆盖的定位面。
- 经验/教训：
  - 被 IDE 打开的文件，工具编辑结果可能与磁盘不一致；「diff 显示成功」≠「落盘」；
  - 短 old_str 的替换在旧版本文本上会拼出脏行，宁可取整段上下文；
  - 批量小 diff 分开做、立即核，比一次大替换更稳。
- 验证/效果：重做后逐行回读确认（WORKLOG 流程位置/计划步骤、CHANGELOG v1.2.2
  标题）均落盘；脏行已清理。
- 相关文件：docs/WORKLOG.md、docs/CHANGELOG.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=工具协作/IDE`；
  `tags=[IDE, SearchReplace, 内存视图, 回读核对, 脏拼接]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · TRAE 沙箱写边界实测（新建可/覆盖删复制拒）+ 用户放行协作流程

- 来源项目/任务：通用项目模板工作区（t5 安装，P1-1 落地）
- 背景与上下文：向六处用户级 agent skill 目录复制 skill 时被沙箱拦截
  （`hit restricted` / WinError 5）；多轮最小化测试探明边界，用户决策「先搁置
  安装推进后续」，放行后补装完成。
- 需求/问题：沙箱对工作区外写操作的真实边界？拦截后如何协作？
- 做法与过程：
  1. 小规模探测：新建文件/目录可成功；覆盖/删除已存在文件与整目录
     rmtree+copytree 被拒；
  2. 被拦后不硬闯，向用户如实说明并给出选项（搁置 / 放行 / 手动执行）；
  3. 用户放行后先删后复制完成六处 × 两 skill 重装 + `.qoderworkcn` 清理，
     verify 全绿闭环。
- 经验/教训：
  - 系统目录批量写操作前先探边界，避免大量文件半途而废；
  - 沙箱拦截是环境约束不是代码缺陷，搁置/放行流程比反复硬试高效；
  - 放行后仍走完整验证链（verify/哈希），安装完成度以校验结果为准。
- 验证/效果：六处副本 v1.2.2 全量 SHA-256 一致；verify EXIT=0。
- 相关文件：install-targets.json、scripts/verify_installed_copies.py（工作区外：六处 skill 目录）
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=工具协作/沙箱`；
  `tags=[沙箱, 写边界, 安装, 权限, 用户放行]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 第六轮审计：发版重装漏项（agent-rules 六副本漂移）+ 子代理通道失效自审兜底

- 来源项目/任务：通用项目模板工作区（v1.2.1 发版后用户要求再派子代理全面审计；
  子代理通信阻塞，按用户指示改主 Agent 自审）
- 背景与上下文：v1.2.1 发版时按约定「全部已安装副本重装并哈希复核」，实际只
  重装了 init-project（40 文件），漏掉 agent-rules（4 文件）；第六轮全量比对
  「六目录 × 两 skill」时发现六处 agent-rules 仍为 1.2.0（缺「缩写附中文翻译」
  正文与继承矩阵 1.2.1 版本）。
- 需求/问题：为什么「重装 + 哈希复核」仍漏一类 skill？如何让发版重装验证
  不漏项？独立子代理通道失效时如何兜底？
- 做法与过程：
  1. 尝试 spawn 独立子代理（fork_turns=none 与 followup_task 均未把任务内容
     送达，子代理反复回复「等待任务」并递归派生子代理阻塞）→ 用户指示主 Agent
     自审；
  2. 自动化全绿（sync / quick_validate×2 / py_compile / 冒烟 / 版本+占位符
     grep / git 与 tag / init-project 六副本哈希）；
  3. 全量比对「六目录 × 两 skill」时发现 agent-rules 六副本 SKILL.md 与
     inheritance-map.md 与工作区不同（1.2.0 vs 1.2.1、缺缩写翻译句）；
  4. 补装 agent-rules 六处 + 全量 4 文件哈希复核通过。
- 经验/教训：
  - **「全部已安装副本」= 六目录 × 两 skill（init-project + agent-rules）**，
    不是只重装主 skill；发版验证清单应显式写「逐目录 × 逐 skill 全量哈希」；
  - 哈希比对必须对每个 skill 都跑，并加「副本内版本号 = 新版本」哨兵检查
    （grep version: X.Y.Z）——只看文件数/哈希一致会漏「旧版本内容一致」；
  - 独立子代理通道不可用时，主 Agent 自审 + 全量硬事实比对可兜底，但自审要
    刻意「反向核对」（先假设有漏，再逐目录 × 逐 skill 找）；
  - 审计结论要区分「项目缺陷」与「工具/通道缺陷」：本次项目状态本身健康，
    缺陷在发版执行遗漏与协作通道。
- 验证/效果：补装后六处 agent-rules 4 文件逐文件哈希一致；全部自动化验证通过。
- 相关文件：agent-rules/SKILL.md、agent-rules/references/inheritance-map.md、
  docs/WORKLOG.md、docs/EXPERIENCE-TO-KB.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=版本管理/发布`；
  `tags=[发版重装, 副本漂移, 哈希复核, 全量比对, 子代理, 自审兜底]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · v1.2.1 发版 + 母项目发版不能用 bump_version.py 的教训

- 来源项目/任务：通用项目模板工作区（用户指示发版 v1.2.1）
- 背景与上下文：v1.2.1 为维护收口（UPGRADE B 区骨架迁移 + P3 批量修复 + 流程
  展示/初始化流程增强）；发版前未发版区段已积累 6 条候选。
- 需求/问题：母项目（模板仓库）发版时版本全量同步的正确姿势；bump_version.py
  能否用于母项目自身。
- 做法与过程：
  1. 先用 `python project-template/scripts/bump_version.py` 递增——脚本
     `REPO_ROOT = parents[1]` 指向 `project-template/`，误升模板骨架
     `version 0.0.1→0.0.2`（骨架 version 应恒为 0.0.1），立即回退；
  2. 按发版同步约定**手工**同步：根 version.json（version + template_version
     =1.2.1）、project-template/version.json（version=0.0.1 不变、
     template_version=1.2.1）、init-project/agent-rules SKILL metadata.version
     ×2、继承矩阵版本对照 ×3、CHANGELOG 未发版区段转正式条目、AGENTS/README
     当前版本字样、UPGRADE 追加 v1.2.1 已知迁移要点（新机制 dogfood）；
  3. 全链路验证：sync / quick_validate×2 / py_compile / 冒烟（template_version
     =1.2.1）/ 版本号全局 grep / 六处重装 40 文件逐文件哈希。
- 经验/教训：
  - **母项目发版不要用 bump_version.py**：它把所在目录当项目根；模板仓库自身
    的版本递增按「发版同步约定」手工改即可；
  - 版本全量同步面清单要包含「当前版本字样」类文档（AGENTS/README）与
    「迁移要点」类文档（UPGRADE）——后者是 v1.2.1 新增的同步面，发版时先给
    自己 dogfood；
  - 发版验证链固定为：sync → quick_validate ×2 → py_compile → 冒烟 → 版本
    grep → 六处重装哈希，任何一环不过都不打 tag。
- 验证/效果：全部验证通过；tag v1.2.1；六处重装哈希一致。
- 相关文件：version.json、project-template/version.json、init-project/SKILL.md、
  agent-rules/SKILL.md、agent-rules/references/inheritance-map.md、
  docs/CHANGELOG.md、project-template/docs/UPGRADE.md、AGENTS.md、README.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=版本管理/发布`；
  `tags=[发版, bump_version, 版本同步, 母项目, 迁移要点, dogfood]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · P3 批量修复：文档/配置/脚本一致性收口（T2-T8，T5 跳过）

- 来源项目/任务：通用项目模板工作区（全面审计第五轮 P3 建议实施）
- 背景与上下文：审计提出 T2-T8 六项 P3；用户指示「继续修 P3，约束增强不做」，
  因此跳过 T5（check_dev_docs 交叉引用增强，属工具层约束增强）。
- 需求/问题：把文档声称、配置规则、脚本行为三者对齐，并清理已安装副本生成物。
- 做法与过程：
  1. T2 文档↔配置对齐：`private/test/TEST.md` 声称 `staging-repo/` 被
     `../.gitignore` 忽略，实际无规则 → 补 `test/**/staging-repo/`；
  2. T3 语义预授权：`--auto-release` 与红线 2「发布/推送须同意」衔接——根
     AGENTS.md 版本管理、init_project.py 自动发布文案、init-steps 参数表三处
     同步「自动发布视为预授权；破坏性变更/永久删除仍须单独确认」；
  3. T4 FAQ 纠错：`--no-git` 不能绕过 Python（脚本本身需要解释器）→ 改为
     人工复制/换机器；
  4. T6 行尾统一：.gitattributes 的 ps1/bat CRLF 与 .editorconfig LF 冲突 →
     统一为 LF（工作区 + 模板同步）；
  5. T7 可移植性：ci_check / pre_release 子进程 `["python", ...]` →
     `[sys.executable, ...]`；
  6. T8 卫生：六处副本 + 工作区 `__pycache__` 经 trash.py 进回收站，重装后
     各 40 文件逐文件哈希一致。
- 经验/教训：
  - 「文档声称 ↔ 配置文件 ↔ 脚本行为」三面必须互相核对：TEST.md 引用
    .gitignore 规则、FAQ 描述脚本能力、help 文案与替换文本都要反向验证；
  - 语义预授权类文案要三处同步（规范正文 / 参数说明 / 生成文本），否则 init
    出来的项目与文档不一致；
  - 批量 P3 收口的最短验证链 = sync + quick_validate + py_compile + 冒烟 +
    副本全量哈希；明确「约束增强不做」时要在变更记录里显式登记跳过项，避免
    误以为遗漏。
- 验证/效果：sync 36 文件 0 差异；quick_validate ×2；py_compile；冒烟（自动发布
  文案/忽略规则/LF 行尾/sys.executable 调用）；六处重装 40 文件逐文件哈希一致。
- 相关文件：project-template/private/.gitignore、project-template/AGENTS.md、
  project-template/.gitattributes、project-template/scripts/ci_check.py、
  project-template/scripts/pre_release_check.py、init-project/scripts/init_project.py、
  init-project/references/init-steps.md、.gitattributes、docs/CHANGELOG.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=文档治理/工程实践`；
  `tags=[P3, 一致性, .gitignore, .gitattributes, sys.executable, 预授权, pycache]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · T1 升级路径修复 + 同步面约束机制根因（UPGRADE B 区骨架迁移）

- 来源项目/任务：通用项目模板工作区（全面审计第五轮 P2·T1 实施 + 用户追问约束
  机制）
- 背景与上下文：审计发现 UPGRADE.md「只应用【通用】/WORKLOG 绝不覆盖」规则未覆盖
  模板随版本新增的 B 区私有骨架（v1.2.0 四登记册 INDEX / WORKLOG 流程位置字段 /
  check_dev_docs 依赖），既有项目按文档升级会漏建并导致校验失败；用户同时追问
  「文档/skill/WORKLOG/private 子 git 各靠什么约束、为何 WORKLOG 问题反复出现」。
- 需求/问题：① 让升级路径显式覆盖 B 区骨架；② 说清各同步面的约束现状与根因。
- 做法与过程：
  1. 约束现状梳理：文档/WORKLOG=流程层（红线 12/14、使用规则）+ 检查层
     （audit-checklist §3/§7、完成清单）弱约束，自动化仅覆盖结构存在性
     （check_dev_docs 只查流程位置字段存在）；skill=sync_template 工具强约束
     （镜像哈希/版本/指纹/init-steps 覆盖）；private 子 git=发布前 pre_release
     强约束、日常流程约束；
  2. 根因：**内容新鲜度是语义判断，结构校验无法根治**；能抓「声称 vs diff
     失配」的是独立子代理审计（第四轮已实证）；WORKLOG 反复陈旧=流程入口
     （任务开始切换当前任务）再次未执行；
  3. 修复 T1：UPGRADE.md 新增「B 区私有骨架迁移」（新增复制/已有只合并字段/
     依赖补齐/私有子 git 同步）+「升级迁移检查表（按版本）」（v1.2.0 已知迁移
     要点），回读校验补 check_dev_docs；sync + 六处重装。
- 经验/教训：
  - 「改模板必同步」的同步面应包含**升级承载文档**（UPGRADE.md）：模板新增
    B 区骨架时，升级说明必须同步，否则既有项目升级即坏且无补救指引；
  - 模板分发的「私有骨架」与「项目私有内容」是两回事：升级规则要区分
    「骨架文件新增/字段合并」与「项目内容绝不覆盖」，不能一刀切按区忽略；
  - 约束分三层（流程/检查/工具），工具层只能约束「结构」，内容新鲜度要靠
    「入口显式动作 + 独立审计」兜底——把「任务开始切换 WORKLOG 当前任务」
    设为节点 01 的强制动作是成本最低的入口约束。
- 验证/效果：sync 36 文件 0 差异；回读核对；六处副本重装哈希一致。
- 相关文件：project-template/docs/UPGRADE.md、docs/CHANGELOG.md、docs/WORKLOG.md、
  project-template/private/AGENTS.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=文档治理/项目管理`；
  `tags=[升级路径, B区骨架, UPGRADE, 约束机制, WORKLOG, 独立审计]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 全流程审计（第五轮）：升级路径/初始化输出面/一致性硬事实核对

- 来源项目/任务：通用项目模板工作区（用户要求全面审计 + 判断能否支撑从零搭建）
- 背景与上下文：模板已迭代到 v1.2.0（四登记册/流程提示/缩写翻译），前四轮审计
  聚焦自动化全绿与维护级缺陷；本轮要求覆盖「全流程是否有缺口、流程描述是否清晰、
  能否从零搭建并开发」。
- 需求/问题：从零搭建到归档的每个环节是否都有文档/工具入口；流程描述是否自洽；
  硬事实（版本/文件数/副本哈希）是否与声称一致。
- 做法与过程：
  1. 通读工作区 AGENTS/README/docs + 模板根/私有 AGENTS + 模板 docs/scripts/
     workflows/private 骨架 + init-project 全套 + agent-rules 全套；
  2. 自动化验证：sync 36 文件 0 差异、quick_validate×2、py_compile、
     init 冒烟（36 文件/13 替换/双 git 干净/check-ignore 命中/check_dev_docs
     0 issue/pre_release 占位拦截符合预期）、版本 grep 无残留、六处副本全量哈希
     一致（排除 __pycache__）；
  3. 逐环节核对：立项调研→初始化→文档填空/CI 落地→首个需求（开发前门禁）→
     日常开发（实施/审计/验证/提交）→发布→升级→归档；
  4. 发现 P2×1：UPGRADE.md「只应用【通用】」规则未覆盖模板新增的 B 区骨架
     （四登记册 INDEX、WORKLOG 流程位置字段、check_dev_docs 依赖）——既有项目
     按 UPGRADE 升级会漏建登记册并导致 check_dev_docs/pre_release 失败而无补救
     说明；P3×5：TEST.md 称 staging-repo/ 被 ../.gitignore 忽略但 private/
     .gitignore 无此规则；--auto-release 与红线 2「发布/推送须征得同意」的衔接
     未明确；FAQ「Python 不可用→--no-git」表述误导（脚本本身需 Python）；
     check_dev_docs 交叉引用弱校验（RFC 依据 PRD / RESEARCH 取代目标不存在、
     ADR 双向 Supersedes 不一致不拦截）；.editorconfig（全 LF）与
     .gitattributes（ps1/bat CRLF）行尾规则不一致。
- 经验/教训：
  - 「改模板必同步」已覆盖资产镜像/摘要/校验清单，但**升级路径**（UPGRADE.md）
    是另一条同步面：模板新增私有骨架文件时，必须同步升级说明（否则既有项目
    升级即坏且无补救指引）；建议 UPGRADE 增加「模板新增文件清单 + 升级迁移
    检查表（含 B 区骨架）」；
  - 初始化流程（init_project.py 输出面）与文档（FAQ/校验清单）互为独立载体，
    审计时要同时核对「脚本打印信息 ↔ 文档描述 ↔ 实际行为」三者一致性；
  - 一致性硬事实核对应包含「已安装副本的完整文件集」而不只 SKILL.md 哈希——
    五处副本带 __pycache__、一处不带，全量对比需排除生成物才能得出「一致」；
  - 文档中的「详见 ../.gitignore」这类引用必须反向核对被引用文件确有对应规则。
- 验证/效果：全部自动化验证通过；冒烟端到端通过；结论=可支撑从零搭建全流程；
  修复建议待用户确认（P2 优先）。
- 相关文件：docs/WORKLOG.md、project-template/docs/UPGRADE.md、
  project-template/private/test/TEST.md、project-template/private/.gitignore、
  init-project/references/init-steps.md、project-template/private/AGENTS.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=文档治理/项目管理`；
  `tags=[审计, 升级路径, UPGRADE, 私有骨架, 初始化流程, 一致性核对]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · init-project 初始化流程更新（审计后续补 v1.2.0 特性）

- 来源项目/任务：通用项目模板工作区（全面审计后用户追问「初始化流程也该更新」）
- 背景与上下文：v1.2.0 新增开发前规范（四登记册/check_dev_docs/流程提示/缩写
  翻译）后，模板正文与 SKILL 摘要已同步，但**初始化流程本身**（`init_project.py`
  打印的「下一步」指引、SKILL 执行流程校验清单、前置确认、init-steps 特性核对）
  仍是 v1.1 心智，新项目初始化后 agent 看不到新规范入口。
- 需求/问题：初始化流程如何把 v1.2.0 新特性变成「初始化后可见的下一步」？
- 做法与过程：
  1. 取证：`init_project.py` 下一步 6 条（无登记册/流程提示）、SKILL 执行流程
     校验清单 6 项（无四登记册/check_dev_docs/流程位置）、前置确认 1 无调研
     落点、init-steps 校验清单缺特性核对；
  2. 修复：下一步扩为 8 条（补开发前登记册/流程提示/缩写翻译）；SKILL 第 3 步
     补 3 项校验、第 4 步收尾建议补开发前门禁；前置确认补「调研结果落
     RESEARCH-XXXX」；init-steps 校验清单补「流程提示/缩写对照」、阶段 1 补
     流程提示说明；CHANGELOG 未发版 v1.2.1 登记。
- 经验/教训：
  - 模板/技能类项目升级后，**初始化流程的「用户可见下一步」是最后一块拼图**：
    正文/摘要/校验清单都同步了，脚本打印的指引漏掉就会让新项目「找不到入口」；
  - 特性核对清单应包含「初始化输出面」：脚本打印信息、SKILL 执行流程内嵌清单
    （不只 references/init-steps.md）。
- 验证/效果：py_compile / quick_validate / 冒烟（下一步 8 条可见）/ 六处重装
  哈希一致。
- 相关文件：init-project/scripts/init_project.py、init-project/SKILL.md、
  init-project/references/init-steps.md、docs/CHANGELOG.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=Agent 工程实践/文档治理`；
  `tags=[init-project, 初始化流程, 下一步提示, skill, v1.2.1]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 全面审计（第四轮）：对话展示未落库导致的声称失真

- 来源项目/任务：通用项目模板工作区（v1.2.0 发版 + `386813b` 后全面审计）
- 背景与上下文：v1.2.0 发版 + 386813b（缩写翻译/流程图）后用户要求全面审计；
  自动化验证全绿，独立子代理审计（只看 diff + audit-checklist，不共享上下文）
  发现 P1：需求②「流程图补充文档更新流程」未落库——对话 mermaid 展示 ≠
  持久化，但 WORKLOG 阶段 40 / EXP-KB / 提交信息均声称已做。
- 需求/问题：为什么「机制全绿 + 提交已做」仍出现交付失真？——展示类产物没有
  持久化载体，状态文档却按「已实现」记账。
- 做法与过程：
  1. 自动化验证（sync / quick_validate×2 / py_compile / 冒烟 / check_dev_docs /
     版本+占位符 grep / 六处哈希）全绿；
  2. 独立子代理审计抓出 P1×1 / P2×2 / P3×1：流程图未落库、CHANGELOG 未发版缺
     「② + SKILL 摘要」条目、WORKLOG 阶段 40 变更文件缺 EXP-KB、提交信息失实；
  3. 修复：文档更新流程落成模板 16 节点清单**持久小节**（保持 16 节点不变式）；
     CHANGELOG 重排「新在前」（v1.1.1 原在 v1.2.0 上方）；WORKLOG 当前任务切换/
     硬事实校准；维护约定 8/9 顺序；SKILL 摘要补缩写翻译；状态文档校正。
- 经验/教训：
  - **展示类交付必须有持久化载体**：对话里画图/给方案 ≠ 已实现；若状态文档/
    提交信息要记账，先落库再记账；
  - 独立审计（只看 diff + 清单、不共享上下文）能抓到「声称 vs diff」失配——
    这是自审盲区（自审会顺着记忆确认）；
  - CHANGELOG 版本条目必须「新在前」（顶部最新），未发版区段在最新版本之上；
    历史顺序错乱是高频维护缺陷；
  - 状态文档「变更文件」列要覆盖全部实际改动（含工作区文档与 sync 镜像）。
- 验证/效果：修复后 sync / quick_validate / 六处哈希全过；审计结论由不通过 →
  复检通过。
- 相关文件：docs/WORKLOG.md、docs/CHANGELOG.md、project-template/private/AGENTS.md、
  init-project/SKILL.md、AGENTS.md、docs/EXPERIENCE-TO-KB.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=文档治理/项目管理`；
  `tags=[审计, 独立审计, 对话展示, 持久化, CHANGELOG, 状态失真]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 流程展示要求：缩写附中文翻译 + 流程图体现文档更新流程

- 来源项目/任务：通用项目模板工作区（v1.2.0 发版后流程展示反馈）
- 背景与上下文：用户查看 v1.2.0 流程图后提出两点：① 展示流程时缩写要附中文
  翻译（如 ADR=架构决策记录），该要求应写进项目文档（不只口头约定）；② 流程图
  未体现「文档更新流程」（改动完成即文档就绪 / 发布前文档检查 / 状态收口）。
- 需求/问题：把「展示可读性」与「文档同步可见性」变成模板显式要求。
- 做法与过程：
  1. 模板 `private/AGENTS.md`「流程提示」新增强制规则「缩写附中文翻译」+
     「缩写对照」表（单一真相）；根 AGENTS / DESIGN / WORKLOG 流程位置字段同步；
     agent-rules 工作流补通用原则（涉及缩写时附中文翻译）；
  2. 工作区 dogfood：AGENTS 维护约定 #9 补翻译要求（顺带修正编号冲突：流程提示
     误编为 8、索引纪律为原 8，改为 9）、README、CHANGELOG 未发版 v1.2.1 候选；
  3. 文档更新流程补实：持久化载体为模板 16 节点清单——新增「文档更新流程
     （贯穿全程）」小节（文档就绪 / 发布前文档检查 / 状态文档收口 / 文档治理）；
     对话内 mermaid 仅为展示，须与 16 节点清单一致（全面审计 P1 要求落库）。
- 经验/教训：
  - 面向用户的流程图必须把「文档同步」画成显式节点/泳道——它虽是贯穿动作，但
    用户视角看不到就等于没有；
  - 模板类项目新增条款要顺带核对既有编号（插入新条款复用编号会产出两条 #8）；
  - 缩写翻译要求要写进「展示规范」本身（自指），并给对照表做单一真相，避免
    每次展示重复定义；
  - **对话内展示≠已落地**：mermaid 流程图只在对话里展示、未写入任何持久化
    载体时，状态文档（WORKLOG/EXP-KB）与提交信息**不得声称「已补充」**——
    独立审计抓出 P1：386813b 提交信息/阶段 40 声称「流程图补充」但 diff 无此
    改动；修复=把文档更新流程落成 16 节点清单的持久小节。
- 验证/效果：sync / 校验 / 六处重装后副本一致（待执行）。
- 相关文件：project-template/private/AGENTS.md、project-template/AGENTS.md、
  project-template/private/dev/DESIGN.md、WORKLOG.md、agent-rules/SKILL.md、
  AGENTS.md、README.md、docs/CHANGELOG.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=文档治理/工程实践`；
  `tags=[流程图, 缩写翻译, 文档同步, 展示规范]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 开发前规范实施落地：四登记册 + check_dev_docs + 流程提示（v1.2.0）

- 来源项目/任务：通用项目模板工作区（开发前规范 C 档方案实施 + v1.2.0 发版）
- 背景与上下文：经过四轮方案细化（C 档、调研落点 research/、增量需求机制、
  优先级 P0-P3、状态机三层约束、流程提示），用户确认开始实施并随 v1.2.0 发版。
- 需求/问题：把方案落成模板实体——四登记册 INDEX.md + 校验脚本 + 规范正文同步
  + skill 同步 + 发版 + 六处重装。
- 做法与过程：
  1. 模板新增 `private/dev/{prd,rfc,adr,research}/INDEX.md`（实体化：用途/状态机/
     编号规则/模板骨架/索引；**索引表不预填示例行**）；
  2. 新增 `scripts/check_dev_docs.py`（stdlib 只读，空登记册通过）：文件名/
     编号连续、头部元数据（按 `|` 分段解析 `> key：value`）、状态机规则
     （PRD 定稿/实现字段、RFC 采纳日期、ADR 自取代拦截、RESEARCH 最近更新）、
     INDEX 行与文件/状态一致、D-xxx→ADR 交叉引用、WORKLOG 流程位置字段；
     并入 `ci_check.py` 与 `pre_release_check.py` 第 7 步；
  3. 规范正文 11 处同步（根/私有 AGENTS、WORKLOG、DESIGN、DOCS、CONTRIBUTING、
     README、PRIVATE、audit-checklist 第 10 节）；红线 12 加「历史文档区例外」
     → 指纹更新 + agent-rules 规范 11 同步；
  4. init-project SKILL/init-steps、agent-rules、`sync_template.py`
     `INIT_STEPS_COVERAGE` +5 条、工作区 dogfood（AGENTS 维护约定 #9 /
     WORKLOG 流程位置 / CHANGELOG / README）；
  5. 验证：sync 36 文件 0 差异、quick_validate×2、py_compile、check_dev_docs
     正/负向 4/4、init 冒烟、版本号全局 grep、占位符核对；
  6. 发版 v1.2.0 + 六处重装 + 哈希复核。
- 经验/教训：
  - **文档状态机必须三层约束**（流程显式步骤 + 完成/审计清单 + 工具校验），
    纯约定必然漂移；
  - 头部元数据解析的坑：`> 状态：草稿 | 优先级：P2 | …` 同行分隔时，第一段带
    `>` 块引用前缀、其余字段不在行首——解析须**先剥离 `>` 再按 `|` 分段**，
    否则状态解析不到 → 状态机规则全部被跳过 → **假通过**（负向用例抓出）；
  - 校验脚本的「空登记册通过」让新项目零负担，但 INDEX 里**不能放示例行**
    （会被当作「无文件的行」而失败）；
  - 正/负向用例是校验脚本可靠性的关键：4 组用例抓出 2 个解析 bug；
  - PowerShell 内联中文 + here-string 会把 UTF-8 弄成 GBK 乱码：含中文的测试
    脚本/内容要用 apply_patch 或文件方式生成，避免在 shell 命令里直接写中文。
- 验证/效果：全链路全绿；v1.2.0 发版完成（tag + 六处副本哈希一致）。
- 相关文件：project-template/private/dev/{prd,rfc,adr,research}/INDEX.md、
  project-template/scripts/check_dev_docs.py、project-template/AGENTS.md 等
  11 处、init-project/、agent-rules/、scripts/sync_template.py、docs/*
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=工程实践/文档治理/Agent 工程实践`；
  `tags=[PRD, RFC, ADR, RESEARCH, 状态机, 校验脚本, 流程提示, v1.2.0]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 开发前规范（PRD/RFC/ADR）C 档方案设计（方案设计）

- 来源项目/任务：通用项目模板工作区（v1.1.2 发版后讨论「项目开发前阶段规范」）
- 背景与上下文：模板此前只覆盖「立项调研（红线 13）→ 开发工作流 → 发布 → 归档」，
  缺少「开发前：需求讨论、定架构、定设计方案」的规范与载体；D-xxx 只有结论无
  上下文、DESIGN 是结果非过程、文档治理禁止正文留史，导致开发前过程不留痕。
- 需求/问题：如何补一套「开发前」体系，既能完整承载需求/方案/决策全过程，又
  不与「正文即当前状态、禁止正文留史」的治理冲突？
- 做法与过程（方案设计，待用户确认后实施）：
  1. **档位确认**：用户选择 C 档（PRD + RFC + ADR 三层体系）；兼容性结论——
     现有治理约束的是「当前状态文档」；把 PRD/RFC/ADR 定义为**历史文档区**
     （唯一允许正文留史），普通正文（AGENTS/DESIGN/README/docs）仍禁留史，
     即可零冲突；
  2. **文档结构**：`private/dev/prd/`、`rfc/`、`adr/`、`research/` 四目录
     （实体化，各含 INDEX.md：用途/状态机/编号规则/模板骨架/索引），编号
     `PRD-0001` / `RFC-0001` / `ADR-0001` / `RESEARCH-0001`（4 位前缀零，
     各序列独立、编号不重用）；
  3. **状态机**：PRD 草稿→已定稿（冻结）→已实现/已废弃（被新 PRD 取代）；RFC
     草稿→评审中→已采纳/已否决（冻结）；ADR 创建即不可变（正文 Context/
     Decision/Consequences/Alternatives 只增不改），仅状态元数据可改
     （Accepted → Superseded by ADR-000X）；
  4. **流程门禁**：开发工作流前扩展「开发前阶段」——需求提出 → 红线 13 调研 →
     PRD 草稿→评审→定稿（门禁 1）→ RFC 草稿（含候选方案对比+调研结论）→ 用户
     拍板 → ADR 记录（门禁 2）→ DESIGN 覆盖式吸收 → 确认开工（原第 3 步）；
  5. **S/M/L 档位**：S（小需求/修复）可跳过 PRD/RFC 直接实施+决策记录；M（新功能）
     PRD 必需、ADR 必需、RFC 可选；L（新项目/架构级）三件全必需；档位由 agent
     建议 + 用户确认；
  6. **与现有文档衔接**：DESIGN 仍为当前设计唯一正文（吸收定稿方案 + 链接
     RFC/ADR，不复制历史）；D-xxx 变速查（一行摘要 + 链接 ADR，权威理由在 ADR）；
     CHANGELOG 仍一行摘要（如 `决策 A→B（ADR-000X）`）；WORKLOG 引用编号；
  7. **同步面**：根/私有 AGENTS、DESIGN、DOCS、CONTRIBUTING、README、
     audit-checklist 新「开发前门禁」节、init-project SKILL/init-steps、
     agent-rules 继承矩阵（不继承列表 + 红线 12 指纹 + 规范 11「历史文档区
     例外」原则）、sync_template.py 的 INIT_STEPS_COVERAGE 新增四路径；
  8. **实施后**：全链路验证 + 六处重装 + 发版（版本号待用户确认，建议
     minor v1.2.0）；
  9. **调研落点（细化）**：新增 `private/dev/research/`（RESEARCH-0001-<topic>.md
     + INDEX.md；状态 进行中→已完成（仍可追加）→已过期（被新调研取代））；
     **允许追加更新**：发现记录只追加（每条带日期/来源，不改写不删除），
     「结论与建议」为当前有效状态（新发现导致结论变化时直接覆盖，留痕靠发现
     记录时间线，必要时 CHANGELOG 一行）；调研主题/方向根本变化才开新
     RESEARCH 号取代；PRD/RFC 只内嵌 2-3 行摘要 + `详见 RESEARCH-000X`（可跨
     需求/决策复用，也满足红线 6「创建前相似检查」防重复调研）；
  10. **后续新增需求（细化）**：编号序列跨版本持续增长、不重置；PRD INDEX =
      需求登记册（草稿=待办 / 已定稿=排期 / 已实现=完成 / 已废弃=放弃），索引
      按「状态（未完成在前）+ 优先级」分组排序，已实现/已废弃沉底；**优先级
      字段 P0-P3**（P0 紧急/阻塞→P3 低/待定），属元数据可随时更新；已定稿
      PRD 的需求变更开新 PRD 取代（旧 PRD 仅状态元数据改为已废弃，正文不动）；
      开发前门禁适用于**每个 M/L 需求**（不只在项目启动时）；一次发布 = 多个
      PRD/RFC/ADR 实现集合，CHANGELOG 按版本汇总并引用编号；S 档后续需求仍可
      跳过 PRD/RFC；
  11. **四份 INDEX.md 骨架与工作流细化**：PRD（含优先级与定稿门禁字段齐全
      清单）、RFC（候选对比表 + 评审冻结）、ADR（Nygard 不可变）、RESEARCH
      （追加日志 + 结论覆盖）；S/M/L 判定示例（S=bug/文案/单函数重构，
      M=新功能/模块/引入新库，L=新项目/技术栈选型/架构级重构）；索引排序规则
      （PRD 按状态+优先级分组、RFC/RESEARCH 新条目在前、ADR 编号升序）、P0-P3
      定义、骨架不预填示例值；发版版本号确认 v1.2.0（minor）；
  12. **状态机约束（第三轮细化）**：用户提出「文档状态机靠什么约束、避免落后」，
      设计三层约束——① **流程层**：工作流第 1-3 步显式写状态更新动作 + 状态
      变更权限（草稿→已定稿、评审→已采纳/否决、已接受 ADR、废弃均须用户确认；
      已定稿→已实现由 agent 实施完成后自动更新）；② **检查层**：完成检查清单
      与 audit-checklist 新增「开发前文档一致性」检查项（编号连续 / INDEX 与
      正文状态一致 / 必填字段齐全 / ADR 不可变靠 git log 核对 / RESEARCH 追加
      记录带日期）；③ **工具层**：新增 `scripts/check_dev_docs.py`（仅 stdlib、
      只读、退出码 0/1：校验文件名与编号连续、头部元数据枚举（状态/优先级等）、
      状态机规则（PRD 已定稿需定稿日期+字段齐全、已实现需实现版本、RFC 已采纳/
      否决需采纳日期、ADR 取代号存在、RESEARCH 已完成需最近更新）、INDEX 表格
      与文件/状态一致、D-xxx→ADR 交叉引用存在；空目录通过），并入
      pre_release_check.py 发布前必跑（扩展现有第 6 步文档一致性）、ci_check.py
      注释示例、init-steps 校验清单；
  13. **流程提示（第四轮细化）**：流程变长后用户要求每次对话展示流程位置——
      设计 16 节点两阶段清单（开发前 01-09：需求提出/调研/PRD 草稿/PRD 评审/
      PRD 定稿/RFC 草稿/RFC 评审/ADR 记录/DESIGN 吸收；实施交付 10-16：确认
      开工/实施/审计/验证/展示提交/发布/沉淀汇报）；展示格式
      `📍 流程位置：NN/16 · 节点名` + 已完成链 + 当前节点 + 下一步；WORKLOG
      「当前任务」新增「流程位置」字段（单一真相，回复从 WORKLOG 读取，避免
      对话记忆漂移）；触发时机=每次实质回复/阶段落盘/上下文恢复（红线 15）/
      收尾/用户询问进度（纯闲聊除外）；S 档 N1→N10 直达；约束=工作流规则+
      完成检查清单+audit-checklist+check_dev_docs.py 校验 WORKLOG 含流程位置
      字段；母项目（工作区）同步 dogfood，agent 回复自带流程位置。
- 经验/教训：
  - 「正文不留历史」与「历史文档区」可以并存：关键是**显式划分**哪类文档是
    历史文档（只增/冻结），其余一律当前状态；ADR 正是把「决策历史」从 CHANGELOG
    一行摘要升级为完整留痕的载体；
  - 完整流程文档体系要防文件膨胀：用 S/M/L 档位让模板保持「完整但不强迫」——
    C 档不是每个需求都全走，而是「能承载完整流程 + 可按档位裁剪」；
  - 不可变文档（ADR）的「状态元数据可改、正文不可改」是留史与可维护的平衡点；
    编号不重用保证追溯链完整。
- 验证/效果：方案细化完成（第三轮，尚未实施）；发版版本 v1.2.0 已确认；待用户
  确认状态机三层约束方案后实施。
- 相关文件：project-template/（AGENTS×2、DESIGN、DOCS、CONTRIBUTING、README、
  audit-checklist、private/dev/{prd,rfc,adr,research}/INDEX.md 待新增）、
  scripts/check_dev_docs.py 待新增）、init-project/、agent-rules/、docs/WORKLOG.md
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=项目管理/文档治理/工程实践`；
  `tags=[PRD, RFC, ADR, 开发前规范, 立项, 模板]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 工作流缺陷修复：sync 覆盖校验 + 初始化落地路线图（方案设计）

- 来源项目/任务：通用项目模板工作区（v1.1.2 发版后工作流复盘）
- 背景与上下文：用户连续三次提问暴露同一类缺陷——「改模板不会自动更新 skill」：
  资产镜像/版本/指纹有自动化，但 `SKILL.md` 摘要、`init-steps.md` 校验清单、
  已安装副本全靠人工（特性核对清单 + 手工重装），且刚踩过 `init-steps` 漏覆盖；
  另外 `init-steps.md` 只有 4 条粗略建议，没有「何时实现 CI / 何时写哪个文档」。
- 需求/问题：如何把「改模板 → 同步 skill 承载文档 → 副本一致」从人工约定升级为
  工具强制？初始化流程如何明确文档填写时机与 CI 落地时机？
- 做法与过程：
  1. 取证：agent-rules 版本/指纹/副本核对（结论：无需内容更新，红线指纹未变、
     v1.1.2 全为项目机制）；模板 31 文件 vs init-steps 覆盖对比（缺 audit-checklist/
     UPGRADE/bump_version/DESIGN/EXP-* 完整路径）；
  2. `sync_template.py` 新增 `INIT_STEPS_COVERAGE`：模板关键文件必须在 init-steps.md
     中出现，缺失即 sync 失败；破坏性测试（注入假 key → 失败；还原 → 通过）；
  3. `init-steps.md` 第 7 节升级为「落地路线图」：阶段 1 文档填空 / 阶段 2 实现 CI
     （tests + ci_check + ci.yml + TEST-REPORT）/ 阶段 3 首个需求 / 阶段 4 首次发布 /
     阶段 5 立项调研 + 「文档时机速查表」（何时写/何时更新）；
  4. 维护约定 #4 补「skill 覆盖度复查」四要素（SKILL 摘要 / init-steps / agent-rules
     如涉红线 / 已安装副本重装）。
- 经验/教训：
  - 「自动同步」必须覆盖**全部承载面**：镜像、元数据、操作文档（校验清单）、已安装
    副本，缺一都会形成「机制全绿但实际过时」的盲区；把人工核对项转成工具校验
    （哪怕只是「缺失即拦截」）是性价比最高的加固；
  - 模板类项目要给「初始化后」写**分阶段路线图**：光有骨架文件和文档职责表，
    新项目仍不知道「先做什么、CI 什么时候实现」；文档时机速查表（初始化/开发前/
    开发中/发布）让「何时写哪个文档」可执行；
  - 副本一致性若没有自动化校验，至少要有「重装 + 哈希复核」的强制步骤，且要写进
    维护约定（发版步骤 6 的落地动作）。
- 验证/效果：sync 正常通过 + 破坏性测试拦截/还原通过；quick_validate 通过；
  六处副本重装哈希一致。
- 相关文件：`scripts/sync_template.py`、`init-project/references/init-steps.md`、
  `AGENTS.md`、`README.md`、`docs/CHANGELOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=工程实践/文档治理`；
  `tags=[自动化同步, skill, 覆盖校验, 初始化路线图, 模板工程]`；
  `project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · init-steps 校验清单未覆盖新实体（发版后遗漏检查实例）

- 来源项目/任务：通用项目模板工作区（v1.1.2 发版后 init-project 覆盖度诊断）
- 背景与上下文：v1.1.2 发版时 SKILL 摘要、assets 镜像、metadata 版本、六处副本
  全部同步且校验全绿；但 `references/init-steps.md` 的校验清单没有覆盖新增的
  `archive/`、`dist/`、`docs/TESTING.md`。用户发版后询问「初始化仓库 skill 是否
  需要更新」才暴露该缺口。
- 需求/问题：为什么「全链路同步 + 发版校验全绿」仍漏了 init-steps？——sync 只
  校验 assets 哈希与 metadata 版本，不校验「操作文档/校验清单」是否覆盖新特性；
  SKILL.md 摘要更新了，但同族的 references/init-steps.md 没有同步（同文件族内
  部分裂）。
- 做法与过程：
  1. 只读诊断：sync 一致性 + grep SKILL.md / init-steps.md 对 archive/dist/TESTING
     的覆盖度，定位缺项在 init-steps 校验清单；
  2. 修复：校验清单补 `archive/ARCHIVE.md`、`dist/.gitkeep`（含 ignore 规则：
     `dist/<任意文件>` 命中、`.gitkeep` 不命中）与 `docs/TESTING.md` 生成检查；
     初始化后建议引用测试落地指引；
  3. CHANGELOG 未发版 v1.1.3 候选登记；六处副本重装并哈希复核。
- 经验/教训：
  - 发版核对清单要包含「references/init-steps.md 校验清单逐项与模板新文件对照」，
    不只核对 SKILL.md 摘要——校验清单是 agent 初始化后必做的动作，缺项会让新
    项目少验证关键内容；
  - SKILL 目录下多个文件（SKILL.md / references/*）是同一分发单元，改模板特性时
    **同族全文件**都要核对，不能只改摘要；
  - 用户「是否需要更新」的提问是有效的发版后审计触发点——发版后应主动做一次
    「新特性 → skill 全部承载文件」覆盖度复查（特性核对清单的补充动作）。
- 验证/效果：quick_validate 通过；sync 31 文件 0 差异；六处副本文件级哈希一致。
- 相关文件：`init-project/references/init-steps.md`、`docs/CHANGELOG.md`、
  `docs/WORKLOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=文档治理/Agent 工程实践`；
  `tags=[skill, 校验清单, 发版后审计, 覆盖度, 派生文档]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 模板实体目录与「双置顶」维护约定 + 测试落地指引（方案设计）

- 来源项目/任务：通用项目模板工作区（archive/dist 实体化、双置顶纪律、TESTING 指引、
  六处安装、v1.1.2 发版）
- 背景与上下文：上一轮补了 `dist/` 约定与归档/退役流程，但用户指出目录树里没有
  归档文件夹、模板里也没有 `archive/` 与 `dist/` 实体目录——「懒加载/约定式」在
  模板里不可接受；同时「新条目在前 = 索引与正文双置顶」此前只写在 P3 修复记录里，
  未进入维护约定，导致复发。
- 需求/问题：模板目录应**实体化**（初始化即存在、目录树/三区表/流程显式引用），
  而不是只在文档里约定；维护级纪律（双置顶）应进入强制约定与收尾核对，而不是
  依赖记忆。
- 做法与过程：
  1. **实体目录**：`project-template/archive/ARCHIVE.md`（A 区：归档说明 + 最终
     快照，进 git，只读）与 `project-template/dist/.gitkeep`（C 区占位，保证目录
     随模板/项目分发）；`.gitignore` 改 `dist/*` + `!dist/.gitkeep`（git 不能对
     整目录忽略后再排除内部文件）；三区表 A 区加 `archive/`、C 区保留 `dist/`；
     模板/工作区目录树、归档流程、DESIGN、audit-checklist 全部显式引用；
  2. **双置顶纪律**：维护约定新增第 8 条「索引/未发版区段纪律（收尾核对）」——
     新条目在前 = 正文与索引**同时置顶**；收尾核对索引顺序、日期、未发版区段与
     `git log <tag>..HEAD` 逐条比对；
  3. **测试落地指引**：新增 `project-template/docs/TESTING.md`（pytest 示例、
     覆盖率、CI 接入、TEST-REPORT 对应、无框架兜底），DESIGN/DOCS/README/
     ci_check 注释同步，init-project SKILL 摘要补能力点；
  4. **安装**：手工复制到六处 agent skill 目录（新增 `.qoder-cn`，其下 skills/
     目录不存在需创建），文件数 + 哈希逐一复核。
- 经验/教训：
  - 模板/骨架类内容**不要懒加载**：约定式（只在文档写「将来会有」）等于没有；
    实体目录 + 占位文件 + 显式引用才是可复现；
  - `.gitignore` 对「忽略目录但保留占位」必须用 `dir/*` + `!dir/.gitkeep`，
    直接忽略 `dir/` 后无法再排除内部文件；
  - 维护级纪律（双置顶、日期校准、未发版比对）必须写进**强制约定 + 收尾核对**，
    单独一次修复记录不足以防复发（P3 #4 → 复发 → 本轮才固化）；
  - 新增 agent 的 skill 目录可能不存在（`.qoder-cn` 无 `skills/`），安装时先创建；
    安装表应随发现同步更新，避免 README 与实际安装面不一致。
- 验证/效果：sync 通过（模板镜像一致）；quick_validate ×2；py_compile；占位符/
  版本 grep 无残留；init 冒烟确认 `archive/`、`dist/`、TESTING.md 生成；六处副本
  哈希一致；v1.1.2 发版完成。
- 相关文件：`project-template/archive/ARCHIVE.md`、`project-template/dist/.gitkeep`、
  `project-template/docs/TESTING.md`、`project-template/.gitignore`、
  `AGENTS.md`、`README.md`、`docs/CHANGELOG.md`、`docs/WORKLOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=项目管理/文档治理/工程实践`；
  `tags=[模板, 实体目录, 双置顶, 测试指引, 多 agent 安装]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 模板生命周期补齐：dist 产物约定 + 项目归档/退役流程（方案设计）

- 来源项目/任务：通用项目模板工作区（.gitattributes / dist / 归档补齐）
- 背景与上下文：全面审计后用户决策补两块——工作区根 `.gitattributes`（P3 #6
  悬置）；模板【通用】模块补「项目归档/退役」（P3 #7）与「`dist/` 发布产物」约定。
  模板此前只有 `.gitignore` 忽略 `dist/` 与 `release.yml` attach `dist/**`，但文档/
  流程未显式定义产物目录与项目生命周期收尾环节。
- 需求/问题：发布产物目录与项目生命周期终止如何成为模板的显式约定，而不是散落在
  `.gitignore` / workflow 里的隐式实现？
- 做法与过程：
  1. **dist 约定**：发布流程第 6 步（根/私有 AGENTS.md）明确「产物统一输出
     `dist/`、C 区不进 git、Release 自动 attach `dist/**`」；DESIGN「打包与发布」、
     README 项目结构、release.yml 注释同步；init-project SKILL 摘要加能力点；
     agent-rules 继承矩阵「不继承」列表登记（项目机制不进入全局精简版）；
  2. **归档流程**：根/私有 AGENTS.md 新增「项目归档/退役」小节（触发=用户明确
     发起；流程=对齐确认→最终发布→README 归档标记→产物归档→经验沉淀→收尾；
     归档后=只读维护）；README 加归档说明；audit-checklist 新增第 9 节归档前检查；
  3. **工作区 .gitattributes**：补根级行尾归一化（LF），与模板一致（P3 #6 落地）。
- 经验/教训：
  - 模板机制（dist/、release attach）一旦存在，就应在流程文档中显式化——隐式实现
    是文档缺口的主要来源（与「已修复但文档仍写旧行为」同类）；
  - 生命周期缺口（归档/退役）比功能缺口更隐蔽：模板覆盖「创建→开发→发布」，
    缺「终止」环节，补上后体系才闭环；
  - 项目机制类能力不进全局精简版（agent-rules），但在继承矩阵「不继承」列表登记，
    防止后续误继承或误删；
  - 工作区 .gitattributes 补齐后，git 按 LF 归一化，避免工作树 CRLF 与索引不一致
    的零散问题。
- 验证/效果：sync 通过（模板镜像一致）；quick_validate ×2；py_compile；初始化
  冒烟确认 README/AGENTS 无占位符残留；提交。
- 相关文件：`.gitattributes`、`project-template/AGENTS.md`、
  `project-template/private/AGENTS.md`、`project-template/README.md`、
  `project-template/private/dev/DESIGN.md`、`project-template/docs/audit-checklist.md`、
  `project-template/.github/workflows/release.yml`、`init-project/SKILL.md`、
  `agent-rules/references/inheritance-map.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/方案`；`domain=项目管理/文档治理`；
  `tags=[模板, 发布产物, 归档, 生命周期, dist]`；`project=通用项目模板`
- 状态：待沉淀
- 沉淀日期：

## 2026-08-26 · 全面审计第三轮：自动化全绿下仍复发的维护级缺陷（审计教训）

- 来源项目/任务：通用项目模板工作区全面审计（第三次）
- 背景与上下文：前两轮审计已修复 EXP-KB 索引顺序、CHANGELOG 未发版区段过时等问题；
  本轮再次全面审计时，自动化校验（sync 28 文件 0 差异、quick_validate x2、py_compile、
  init 端到端冒烟、tag 指向、五副本全量哈希）全部通过，但人工文档核对仍发现
  维护级缺陷复发。
- 需求/问题：为什么「机制全绿」时文档维护缺陷仍会复发？索引/日期/未发版清单这类
  自由文本状态如何防止再次漂移？
- 做法与过程：
  1. 先跑全部自动化验证（sync / quick_validate x2 / py_compile / init 冒烟 /
     tag 指向 / 五副本全量哈希），确认机制本身健康；
  2. 人工逐份文档核对：「最后更新」日期与最新提交日期比对、EXP-KB 索引与正文顺序
     比对、CHANGELOG 未发版区段与 `git log <tag>..HEAD` 逐提交比对、WORKLOG 硬事实
     （文件数/提交号）与仓库实际比对、换行/BOM/占位符/秘密扫描；
  3. 修复：EXP-KB 正文与索引统一「新条目在前」且顺序一致；WORKLOG / EXP-KB 日期补到
     2026-08-26；CHANGELOG 未发版区段补 P3 实施条目；WORKLOG 阶段 25 文件数 33→32
     校准（排除 __pycache__/.pyc）；当前任务切换 + 阶段落盘。
- 经验/教训：
  - 「新条目在前」的索引，新增条目必须**正文与索引同时置顶**，不能只改索引——
    这是 P3 #4 修复后立即复发的点，说明该约定应写成更明确的「双置顶」动作或纳入
    收尾核对；
  - 「最后更新」日期字段是高频过时源：当日有提交时，收尾/汇报前必须校准，可与
    WORKLOG 生命周期收口合并为同一动作；
  - 未发版 CHANGELOG 区段应随每次提交增量登记，防多轮提交后缺项；用
    `git log --oneline <tag>..HEAD` 与区段逐条比对是可靠核对法；
  - 硬事实（文件数）必须排除 `__pycache__`/`.pyc` 后再计数，否则安装/复制类记录
    会虚高。
- 验证/效果：修复后索引/顺序/日期/文件数与仓库实际一致；sync / quick_validate /
  git status 通过。
- 相关文件：`docs/WORKLOG.md`、`docs/EXPERIENCE-TO-KB.md`、`docs/CHANGELOG.md`
- 建议 KB 属性（沉淀时参考，可调整）：`type=knowledge`；
  `knowledge_type=经验方法/教训`；`domain=文档治理/项目管理`；
  `tags=[文档治理, 审计, 状态文档, 索引, 未发版清单]`；`project=通用项目模板`
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
