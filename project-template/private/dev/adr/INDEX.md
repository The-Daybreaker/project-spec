# ADR — 架构决策记录（决策登记册）

> 模块：项目专用（B 区私有，不进 GitHub，由 private 子 git 管理）。
> 用途：承载架构级决策的完整理由（决定了什么、为什么、代价、备选为何不选）；
> **只增不改**——本目录是模板「文档治理」中允许正文留史的历史文档区之一
> （另见 `prd/`、`rfc/`、`research/`）。

## 使用规则（强制）

1. **触发**：架构级 / 触及 `private/AGENTS.md`「定案清单」的决策，用户确认后创建。
2. **不可变**：创建后正文（背景 Context / 决策 Decision / 后果 Consequences /
   备选方案 Alternatives）**只增不改**；仅状态元数据可改（已接受 → 已被
   ADR-XXXX 取代）。
3. **决策变更**：开新 ADR（新 ADR 头部 `Supersedes: ADR-XXXX`）；旧 ADR 状态改为
   「已被 ADR-XXXX 取代」，正文不动；取代关系写在新 ADR 的背景节。
4. **D-xxx 速查**：`private/AGENTS.md`「用户确认的设计决策」每行 = 一行摘要 +
   `详见 ADR-XXXX`；权威理由以 ADR 为准（单一真相，不重复维护）。
5. **与 CHANGELOG**：CHANGELOG 只记一行摘要（如 `决策 A→B（ADR-000X）`），不复制
   ADR 内容。
6. **不可变性核对**：发布前审计用 `git log` 核对 ADR 文件未被修改
   （`scripts/check_dev_docs.py` 校验状态/编号/引用）。

## 状态机

```
已接受 → 已被 ADR-XXXX 取代（正文不变）
```

- 创建（已接受）必须**用户确认**；被取代由新 ADR 触发。

## 编号

- `ADR-0001` 起，4 位前缀零；文件名 `ADR-0001-<slug>.md`；编号**永不重用**。

## 索引表（编号升序，历史追溯链）

| 编号 | 标题 | 状态 | 日期 | 取代/被取代 |
|---|---|---|---|---|

## 模板骨架

```markdown
# ADR-0001 — <决策标题>

> 状态：已接受 | 日期：YYYY-MM-DD | Supersedes：— | Superseded by：—

## 背景（Context）
## 决策（Decision）
## 后果（Consequences）
### 正面
### 负面
## 备选方案（Alternatives）与不选原因
## 关联（PRD / RFC / RESEARCH）
```
