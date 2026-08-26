# private — 私有区

> 模块：全项目专用（不随模板升级覆盖）。

本目录存放**个人/开发期文件**：本机专属信息、开发文档、测试素材等**不能发布到
GitHub** 的内容。

## 管理方式

- 主仓库 `.gitignore` 已整体忽略本目录（`private/`），**永远不会进入 GitHub**。
- 本目录由 **private 子 git** 独立管理（`private/.git`，本地、无远端）：
  - 新增子 git：`git -C private init`（模板初始化时已创建）。
  - 查看变动：`git -C private status --short`。
  - 提交：`git -C private add -A -- . && git -C private commit -m "docs: private vX.Y.Z - 描述"`。
- **发布前必须同步**：任何发布动作前，先检查并提交 private 子 git 的变动
  （见根 `AGENTS.md`「发布流程」第 3 步；`scripts/pre_release_check.py` 自动执行）。

## 内容

| 路径 | 内容 |
|---|---|
| `AGENTS.md` | 开发入口与当前状态（唯一常青开发记忆） |
| `dev/WORKLOG.md` | 工作进度日志（阶段落盘，每完成一小阶段更新） |
| `dev/EXPERIENCE-TO-TEMPLATE.md` | 可沉淀进通用项目模板的经验（完整条目） |
| `dev/EXPERIENCE-TO-KB.md` | 可沉淀进知识库的经验（完整条目） |
| `dev/prd/` | 需求登记册（PRD-XXXX：为什么做/做什么/验收/优先级） |
| `dev/rfc/` | 方案登记册（RFC-XXXX：怎么做/候选对比/推荐） |
| `dev/adr/` | 决策登记册（ADR-XXXX：决定了什么/为什么，只增不改） |
| `dev/research/` | 调研登记册（RESEARCH-XXXX：红线 13 调研结果，发现记录追加） |
| `dev/` | 开发期文档：DESIGN（设计）/ CHANGELOG（变更历史）/ TEST-REPORT（测试记录） |
| `test/` | 本地测试素材（测试库、测试项目等） |
| （按需） | 个人笔记、未公开素材、密钥（密钥不提交子 git 或加密后提交） |

## 规则

- 含个人/机器专属信息或发布前不公开的内容 → 放这里；
- 生成物/缓存/可重建内容 → 不放进这里（也不进任何版本管理）；
- 密钥确需保留 → 放这里且**不提交** private 子 git（或加密后提交）；
- `private/.gitignore` 用于排除本目录内的生成物。
