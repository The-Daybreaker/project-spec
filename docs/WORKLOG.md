# WORKLOG — 通用项目模板工作区 工作进度日志

> 模块：项目专用。
> 使用规则：每完成一小阶段先更新本文件与受影响文档；新对话/新任务开始时，若旧内容
> 已完结或文档已膨胀，**先询问用户是否清理**（已完结条目归档到「历史记录」，或整段
> 移入 `_trash/`），得到确认后才清理；绝不自动删除。
- 最后更新：2026-08-25

## 当前任务

- 需求：实施审计修复清单（用户已确认）——① init-project SKILL 定位摘要补齐
  v1.1.1 能力点 + 发布策略措辞修正；② init-steps「编码提示」直接删除（用户指示：
  旧说明/废案不留档）；③ agent-rules 版本正文改引用版本对照表；④ 发版同步约定加
  「特性核对清单」——并同步用户改动的 agent-rules 触发词（仅非项目且非纯聊天加载）
  到 README / AGENTS / CHANGELOG 与五个已安装副本。
- 目标/验收：修复+同步全部完成；sync / quick_validate / py_compile 全过；五处
  已安装副本与仓库哈希一致；CHANGELOG 未发版区段登记；自动提交。
- 计划步骤：
  1. init-project SKILL / init-steps 修复
  2. agent-rules 版本正文改引用
  3. 触发词同步（README / AGENTS / CHANGELOG / 维护约定）
  4. 验证 + 重装五个副本
  5. 落盘 + 提交

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
- [ ] 下次发版 v1.1.2：把「未发版变更」区段并入正式条目，并 bump version.json / 打 tag
- [x] P3 #1/#2/#3/#4/#5 已实施（UTF-8 输出、UPGRADE 澄清、CONTRIBUTING 措辞、
      EXP-KB 索引、版本单一来源 + sync 自动化校验）
- [x] 本任务（P3 建议实施）15/15 完结
- [ ] P3 #6 工作区根补 .gitattributes（行尾归一化）、#7 模板补「项目归档/退役」
      环节：未决策，待用户确认
- [x] 新需求（精简版 agent 全局规范 skill，agent-rules）：方案已确认，已实施
      （skill 创建 + sync 校验 + 文档同步 + 安装到五个 agent）；随 v1.1.2 发版时
      同步版本

## 历史记录

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
