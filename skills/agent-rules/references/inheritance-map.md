# agent-rules 继承矩阵（维护用）

> 本文件是「随模板每个版本及时更新」的核对依据。模板【通用】要求变更时，必须同步
> 更新本矩阵（指纹）与 `../SKILL.md` 正文；`scripts/sync_template.py` 会自动校验
> 版本一致性、矩阵覆盖完整性、红线正文指纹——校验失败即拦截，防止精简版与模板漂移。

## 1. 版本对照

| 项 | 版本 |
|---|---|
| 模板 `template_version`（权威） | 1.5.0.patch0 |
| `../SKILL.md` `metadata.version` | 1.5.0.patch0 |
| 上次核对模板版本 | 1.5.0.patch0 |

## 2. 模板红线覆盖（project-template/AGENTS.md「通用红线」）

> 双侧台账：模板侧指纹 = 模板红线正文（规范化空白）的 SHA-256 前 12 位；精简版
> 条目侧指纹 = SKILL.md 对应条目正文的同口径指纹。任一侧变更 → sync 失败 →
> 必须复核另一侧对应条目的语义是否需同步，然后运行
> `python scripts/sync_template.py --update-map` 重新登记双侧指纹（堵「只改指纹
> 即放行」漏洞）。

| 模板红线 | 主题 | 精简版条目 | 处理 | 模板侧指纹 | 精简版条目侧指纹 |
|---|---|---|---|---|---|
| 红线 1 | 要求三要素（意图/展示/验收） | SKILL 规范 1 | 原样 | bbd3023e05df | 9e03458429b7 |
| 红线 2 | 先对齐后实施 | SKILL 规范 2 | 原样 | d752f43ec3aa | abf60e2c76b1 |
| 红线 3 | 变更分级 | SKILL 规范 3 | 原样 | fa18fa77f392 | 6daf741e9f79 |
| 红线 4 | 实施后自动审计 | SKILL 规范 4 | 原样 | c15806ca6359 | d71e85ae6eb6 |
| 红线 5 | 删除纪律 | SKILL 规范 5 | 通用化 | 7084c4fa82de | f3ba072d0a12 |
| 红线 6 | 回读校验 | SKILL 规范 6 | 原样 | c9527c6bd7c5 | 8c1152fba4da |
| 红线 7 | 创建前相似检查 | SKILL 规范 7 | 原样 | 09ad37570edf | 1cbeaaa75633 |
| 红线 8 | 信息以用户/事实为准 | SKILL 规范 8 | 原样 | cb33fd3f224f | 6484ccc76d68 |
| 红线 9 | 不破坏用户未提交的改动 | SKILL 规范 9 | 原样 | 397a2954248d | cbdd02ed2b0a |
| 红线 10 | private 目录纪律 | SKILL 规范 10 | 通用化 | 4e5c808660a1 | 135012ae4197 |
| 红线 11 | 发布前验证 | SKILL 规范 11 | 通用化 | aefa67f1c75c | 4204227d3340 |
| 红线 12 | 密钥安全 | SKILL 规范 10 | 通用化 | e163d11860f4 | 135012ae4197 |
| 红线 13 | 文档同步与治理 | SKILL 规范 12 | 原样 | 6453d18278ec | 427f2cc3566d |
| 红线 14 | 立项调研先行 | SKILL 规范 13 | 原样 | ad970383b66f | 9168e9eccf1b |
| 红线 15 | 阶段落盘 | SKILL 规范 14 | 通用化 | 07d360b36a0a | 7e3939608a1e |
| 红线 16 | 上下文恢复重读 | SKILL 规范 15 | 原样 | 1138ff380449 | b471a7d80fea |
| 红线 17 | 范围克制与纠错清零 | SKILL 规范 17 | 原样 | fc1a9cdebe5e | 289c44d16ef4 |
| 红线 18 | 提问与共识确认（共识卡/重检行） | SKILL 规范 18 | 原样 | cd4ffccd0713 | 40e71616d1bf |
| 红线 19 | 敏感信息与私有区边界 | SKILL 规范 10 | 通用化 | 5e50671be3c6 | 135012ae4197 |

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
