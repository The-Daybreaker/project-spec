# CHANGELOG

发布仓库的版本历史（两产物：project-template / init-project）。
模板本体只在 `init-project/assets/project-template/` 存一份。

版本号与模板本体一致（单一事实源：模板本体 `CHANGELOG.md` 的版本标题），当前 0.9.0。

## [Unreleased]

spec 机制单文档化重构（三仓联动）+ agent-rules skill 并入 init-project +
取消 inbox/pending/reviews 三个异步目录（process 重新定性为协作当前状态区）+ 目录命名对齐业界惯例
（logs→archive、workspace 去预置改 spec 驱动）+ 规范拆分出 `spec/constitution.md`
+ 移除模板 `package.json`（版本标记归 CHANGELOG 独担）。
版本号待用户确认后再定，不随本次自动 bump。

### Changed

- 三份 README 按「问题场景 → 设计理念 → 快速开始 → 日常使用 → 深入
  展开」的新用户叙事线重写：发布仓 README 新增痛点共鸣、协作层/发布层
  分离与流程/宪章分开的设计理念、冷启动读盘 mermaid；模板本体 README
  改为面向项目主人的使用手册（协作循环、高频场景、核心文件分工，
  「写给用户」节原样保留）；配套 project-spec 货架 README 补两层关系图
  与 software-dev 工作流实例讲解。
- 同步 spec 新口径（配套 project-spec 阶段链软化）：阶段链由硬依赖改为
  「推荐推进顺序、不强制」，「缩放旋钮」→「流程调节」，「管什么场景」→
  「使用场景 / 适用于什么场景」；涉及发布仓 README、模板本体 `AGENTS.md`
  §六与 `spec/AGENTS.md` §一。
- 一个 spec 合并为一份 `spec.md` + 同级 `assets/`（产出骨架）；云端库简化
  为只读货架、拉下来自由改。模板本体 `spec/AGENTS.md` 精简为机制说明书，
  `AGENTS.md`（§一/§二/§六）、`README.md`、`init-project/SKILL.md` 去掉
  模块 / 锁文件 / registry 口径；发布仓 README「核心理念」spec 段、
  mermaid、目录结构、「配套仓库」整节改写。
- `init-project` skill 适用范围扩为所有非纯聊天对话，新增「项目外通用
  行为基线」用途（指向模板本体 `AGENTS.md`「五、规范」宪章 6 条，只指向
  不复制）。
- 取消 inbox/pending/reviews 三个异步交流目录，`process/` 重新定性为「协作当前状态区」（常驻件
  task.md / memory.md + 临时件 笔记 / `review-<简介>.md`，用完即清）；冷启动
  改为通读 `process/` 全部文件；review 降为 process 根临时件（通过后删、不
  归档 logs），何时验收交对话或 spec；`memory.md` 改为 agent 自我维护区（只
  声明用途不声明内容）。模板本体 `AGENTS.md`（§一/§二/§三）、两份 README、
  `init-project/SKILL.md`、`process/memory.md`、目录树与配套 project-spec 的
  两份 spec 同步（详见模板本体 CHANGELOG 与开发仓决策 62）。
- 目录命名对齐业界惯例：`logs/` 更名 `archive/`（避开运行日志标准名的写入
  污染）；删除 `workspace/source/`、`workspace/delivery/` 预置，`workspace/`
  保留为「干活 + 发布层」通用声明、内部结构改由 spec / 项目定；配套云端两份
  spec 产出落点改用 `workspace/src/`、`workspace/dist/` 与 `archive/*` 归档路径
  （详见模板本体 CHANGELOG 与开发仓决策 63）。
- 规范正文从模板 `AGENTS.md` 拆出到新文件 `spec/constitution.md`（宪章 / 项目级 /
  项目自己的规范三节，条款原样搬运 + 「写给用户」头说明可自由删改增补）；
  `AGENTS.md` §五 收敛为「宪章」必读指引节、§七 并入 constitution.md、冷启动链与
  读盘加入 constitution.md；`spec/AGENTS.md`、`init-project/SKILL.md`（用途②增加
  constitution.md 指向）、两份 README 同步（详见开发仓决策 64）。
- 全仓措辞规范化：内部比喻与生造术语统一换成业界通用说法（状态标记、当前
  状态区、必读指引、框架自带文件、渐进式披露、独立审查等），历史 CHANGELOG
  条目同步改写、不改变任何历史事实；不涉及机制变更。

### Removed

- 异步交流目录 `process/inbox/`、`process/pending/`、`process/reviews/`：异步
  交流在同步对话场景下是伪需求，inbox / pending 整个取消，review 降为
  process 临时件；logs 不再镜像这三个子目录。
- `workspace/source/`、`workspace/delivery/` 预置子目录：框架不再写死工作区
  结构，改由 spec / 项目按惯例（如 `src/`、`dist/`）自行声明。
- 锁文件三类（`spec/lockfile.py` / `lockfile.md` 及实例化后的
  `lockfile.json`），冷启动不再跑漂移校验；模块机制（`@模块/`、
  `MODULE.md` / `module.json` / 每模块 `README`·`CHANGELOG`）、
  `manifest.json`、`registry.json`、`add.md`（详见配套仓 project-spec 的
  CHANGELOG）。
- `agent-rules` skill 整个删除：它与模板宪章是两处副本、必然漂移，其「项目
  外行为基线」职责并入 `init-project`（指向唯一事实源，杜绝漂移）。
- 模板本体根 `package.json`：`version` 与 CHANGELOG 版本标题重复（违反单一事实
  源）、随模块制废弃已无脚本读取、对非 Node 项目是杂物；删除后模板版本标记由
  CHANGELOG 独担，`init_project.py` 去掉 `--name` / `_set_project_name`（详见开发仓
  决策 65）。

### Fixed

- 宪章第 4–6 条序号恢复（与「分类声明」的显式序号约定一致）。
- `init_project.py` 去掉对 git 本地化输出措辞的依赖：无可提交改动改用
  `git status --porcelain` 判定，未配置身份改为前置探测并给精准提示；
  `git add` 检查返回码；`git init -b`（git ≥ 2.28）不可用时回退
  `git init` + `symbolic-ref` 设置默认分支。
- 默认 `.gitignore` 密钥文件名模式补 `*.crt` / `*.cer` / `*.p7b` /
  `.htpasswd` / `*.ovpn`。

## [0.9.0] - 2026-09-03

云端模块库接入 + spec 模块字段精简 + 仓库结构简化。

### Added

- 云端模块库：`github.com/The-Daybreaker/project-spec` 作为 spec / 模块唯一
  事实源（SSOT），仓库结构 `registry.json`（目录索引）+ `build/` + `specs/` +
  `modules/`；锁文件落地（`lockfile.py` 生成 + 校验，`origin` 记真实路径）。

- spec 的 `AGENTS.md` 锁文件节：引入 spec 的拉取流程 + 冷启动 hash 校验
  （拉取交 agent，不写拉取脚本）。

- 框架新增 `process/memory.md`：agent 记忆固定文件（踩过的坑与被验证过的
  判断，冷启动必读；只存当前有效条目，失效归档 `logs/memory/`）。

### Changed

- 术语全局更名：「地基」→「框架」（语义不变）；文档措辞不再用
  「七件套」之类清点式表述。

- 口径修订（用户定）：根 README 去「版本与升级 / 给维护者的几条约定」节、
  模板 README 用户规范瘦身重写为「写给用户」、init-project SKILL 前置确认
  精简（删「先调研再立项」步骤）。

- 仓库结构简化：模板本体从根目录 `project-template/` 移入
  `init-project/assets/project-template/`，全仓只存一份（单一事实源，
  不再是「根目录本体 + assets 镜像」两层复制）；根目录只剩两个 skill +
  README + CHANGELOG。

### Removed

- module.json 的 `enable.instantiate` / `disable.keep` 字段（启停运行态由
  `manifest.json` 的 entries 表达，字段 12 → 10）。

- 密钥门禁（`scripts/scan_secrets.py` + `.githooks/pre-push`）：模板与
  本仓不再携带；密钥防护的机械防线只留 .gitignore 的密钥文件名模式，
  要不要额外门禁由使用者自行决定。

### Fixed

- 审计修补：`lockfile.py` 指纹行尾归一化 + 生成模式保留 fork / private
  溯源；`init_project.py` 目标目录非空改为警告并继续（对齐 SKILL）+
  健壮性修正；模板 `.gitignore` 补 `__pycache__`；AGENTS.md「写给用户」
  节名引用同步；根 README 补 agent 记忆；仓根补 `.gitattributes`。

## [0.8.0] - 2026-09-02

断代版本：模板整体重设计，目录结构全新（旧版项目无法原地升级）。

### Added

- 初始骨架：`AGENTS.md`（协作总纲 + 宪章 6 条）、`README.md`（使用手册）、
  `context/`（项目上下文，种类由 spec 决定）、`workspace/`（source +
  delivery）、`process/`（任务板 + inbox / pending / reviews 三个异步目录）、
  `logs/`（历史归档）、`spec/`（声明式规范）。

- spec 机制：构建规则（`spec/build/`：build.md + spec / module 两模板）+
  预置 spec `software-dev`（vision / design / prd / adr / development /
  test / audit / release 共 8 模块）；空 spec 时项目以框架形态运转。

- 推送前密钥门禁（保留自旧版并参数化）：`scripts/scan_secrets.py` +
  `.githooks/pre-push`，排除名单外置 `scan_secrets.ignore`（不入库）。

### Changed

- `init-project` skill 重构：内嵌模板镜像，初始化含 hooksPath 配置与
  回读校验清单（内联 SKILL.md）。

- `agent-rules` skill 重构：模板宪章的项目外精简形式。

- 发布 README 重写（价值主张 / 快速开始 / 目录结构 / 版本说明）。

### Removed

- 旧版结构整体移除：`private/` 子仓库、`docs/`、`dist/`、`archive/`、
  `.github/workflows/`、`version.json`、`install-targets.json` 及大部分
  维护脚本。

## [0.7.1] - 2026-08-28

接口设计与设计环节补全 + 红线三要素收尾（patch0 + patch1 两次补丁）：
设计契约文件夹（架构 / 接口 / 数据 / 安全，适用必做、不适用须声明）；
接口契约场景化——用户审场景映射表、不审技术，确认后冻结，验收用例联动；
文档质量可持续机制（质量标准 + 反 AI 感清单 + 审计文档质量关）；红线 18
补齐显式三要素，19 条红线三要素终检齐全。

## [0.7.0] - 2026-08-28

防漂移与文档架构改造（断代版本，不向前兼容）：单一事实源三层结构——
15 条规范事实各有唯一家（事实台账 + FACT/REF/INJECT 锚点机制）；防漂移
检查（重复检测 / 摘要限长 / 正文指纹校验）；文档集归一；阶段契约（每阶段
必做清单 + 裁剪属性）；需求冲突检测检查点；测试台账；安装目标扩至九处。

## [0.6.0] - 2026-08-27

红线与要求可验证性改造：新增最顶层红线「要求三要素元规范」（所有红线
须同时具备意图 / 展示面 / 验收面，自指示范）；新增红线「敏感信息与私有区
边界」（密钥内容级扫描 + 推送前安全门禁三层）；「范围克制」与「提问共识」
两条红线重写（番茄炒蛋比喻入正文、共识确认机制）；测试正式子阶段与测试
报告双区；辩护性措辞扫描；历史泄露处置与全历史身份重写。

## [0.5.2] - 2026-08-27

第九轮全面审计修复收口：新项目首跑即红等 5 项发现全修 + 表述面同类残留
清理；防再发机制——开箱即用冒烟自检（初始化 + 回读 + 骨架脚本自检，
发版前必绿）。

## [0.1.0 – 0.5.1] - 2026-08-15 ~ 2026-08-27

从首个版本到第四轮审计的演进期：从「通用项目模板 + init-project
skill」起步，逐步建立开发前规范（PRD / RFC / ADR / RESEARCH 四类规范文档）、
P1-P5 五阶段工作流、agent-rules skill、Python 维护脚本链、私有区与密钥
门禁、安装表与副本校验、agent 提问与共识确认机制等骨架，其间历经多轮
全面审计与修复（0.4.2 三域审计处置 16 项、0.5.0 架构重构、0.5.1 版本号
改四段式）。
