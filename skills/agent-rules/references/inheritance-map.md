# agent-rules 继承矩阵（维护用）

> 本文件是「随模板每个版本及时更新」的核对依据。模板【通用】要求变更时，必须同步
> 更新本矩阵（指纹）与 `../SKILL.md` 正文；`scripts/sync_template.py` 会自动校验
> 版本一致性、矩阵覆盖完整性、红线正文指纹——校验失败即拦截，防止精简版与模板漂移。

## 1. 版本对照

| 项 | 版本 |
|---|---|
| 模板 `template_version`（权威） | 1.3.2 |
| `../SKILL.md` `metadata.version` | 1.3.2 |
| 上次核对模板版本 | 1.3.2 |

## 2. 模板红线覆盖（project-template/AGENTS.md「通用红线」）

> 指纹 = 该条红线正文（规范化空白）的 SHA-256 前 12 位。模板红线正文变更 → 指纹
> 不匹配 → sync 失败 → 必须复核 SKILL.md 对应条目并更新指纹。

| 模板红线 | 主题 | 精简版条目 | 处理 | 指纹 |
|---|---|---|---|---|
| 红线 1 | 先对齐后实施 | SKILL 规范 1 | 原样 | 55fb2ba46ee4 |
| 红线 2 | 变更分级 | SKILL 规范 2 | 原样 | 855b6bd7d44f |
| 红线 3 | 实施后自动审计 | SKILL 规范 3 | 原样 | b0aba1a12650 |
| 红线 4 | 删除纪律 | SKILL 规范 4 | 通用化 | ee28329cc7e5 |
| 红线 5 | 回读校验 | SKILL 规范 5 | 原样 | 8c1152fba4da |
| 红线 6 | 创建前相似检查 | SKILL 规范 6 | 原样 | 1cbeaaa75633 |
| 红线 7 | 信息以用户/事实为准 | SKILL 规范 7 | 原样 | 6484ccc76d68 |
| 红线 8 | 不破坏用户未提交的改动 | SKILL 规范 8 | 原样 | cbdd02ed2b0a |
| 红线 9 | private 目录纪律 | SKILL 规范 9 | 通用化 | 8666e79b114a |
| 红线 10 | 发布前验证 | SKILL 规范 10 | 通用化 | ed98f8b269a8 |
| 红线 11 | 密钥安全 | SKILL 规范 9 | 通用化 | f888e9170915 |
| 红线 12 | 文档同步与治理 | SKILL 规范 11 | 原样 | f691f0b47603 |
| 红线 13 | 立项调研先行 | SKILL 规范 12 | 原样 | ccc5f372d29d |
| 红线 14 | 阶段落盘 | SKILL 规范 13 | 通用化 | 5e5845856413 |
| 红线 15 | 上下文恢复重读 | SKILL 规范 14 | 原样 | 054844de3d36 |
| 红线 16 | 范围克制与纠错清零 | SKILL 规范 16 | 原样 | 1a89754aa5ba |

## 3. 其他继承来源

| 模板来源 | 内容 | 精简版位置 | 处理 |
|---|---|---|---|
| 根 AGENTS.md「开发工作流」 | 对齐→确认→实施→审计→验证→汇报+沉淀 | SKILL 第 3 节 | 精简为 6 步 |
| private/AGENTS.md「文档治理」 | 正文即状态/禁 AI 追加历史/一行留痕 | SKILL 规范 11 | 原样 |
| docs/audit-checklist.md | 审计清单 | references/audit-checklist-lite.md | 精简 |
| private/AGENTS.md「完成检查清单」 | 交付清单 | SKILL 第 5 节 | 精简 |
| 模板「版本管理」提交信息 | 提交/分支格式 | SKILL 第 4 节 | 原样 |
| 模板「经验沉淀」 | 每轮对话后写候选经验 | SKILL 规范 15 | 原样 |
| 模板「开发工作流·流程提示」 | 每次汇报展示当前节点/已完成/下一步 | SKILL 第 3 节 | 通用化 |

## 4. 不继承（项目机制；项目内由项目 AGENTS.md 覆盖）

- `version.json` / bump / CI-CD / Release / tag / 模板升级流程
- `dist/` 发布产物目录与 Release attach、项目归档/退役流程
- private 子 git、三区文件归属、STATUS/DESIGN/CHANGELOG/TEST-REPORT 文件体系
- PRD/RFC/ADR/RESEARCH 四登记册文件体系（`private/dev/{prd,rfc,adr,research}/`）
- `scripts/check_dev_docs.py` 登记册校验脚本（并入项目 ci_check/pre_release_check）
- STATUS「📇 阶段卡」字段（项目机制；「长流程任务每次汇报展示进度位置」的原则
  已继承进 SKILL 第 3 节）
- 具体脚本（`pre_release_check.py` / `trash.py` 等）
- 项目概览、技术栈、本机环境、用户决策、定案清单、必须询问清单

## 5. 更新流程（模板【通用】变更时）

1. 比对模板变更 → 更新 `../SKILL.md` 对应条目（或确认无需改）；
2. 更新本矩阵：版本对照 + 受影响行指纹（重新提取模板红线正文计算）；
3. 运行 `python scripts/sync_template.py`，通过后随模板发版。
