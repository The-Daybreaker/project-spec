# {{PROJECT_NAME}} — 协作约定

本文件面向所有协作者（人类与 agent）。Agent 的完整工作流与红线见根 `AGENTS.md`
与 `private/AGENTS.md`（私有）；本文件只约定协作层面的通用规则。

## 分支与提交

- 默认分支：`{{DEFAULT_BRANCH}}`；直接在该分支上开发（小型个人项目约定；
  多人在线协作时改为 feature 分支 + PR）。
- 提交信息格式：`feat: / fix: / docs: / chore: / refactor: vX.Y.Z - 描述`
  （版本号见 `VERSION`；纯文档改动用 `docs:`）。
- 不 force push 共享分支；不修改他人未提交的改动。

## 改动流程（简要）

1. 新需求先在 `private/dev/CHANGELOG.md` 与 `private/dev/DESIGN.md` 对齐意图；
2. 实施 + 同步更新受影响文档（「改动完成即文档就绪」）；
3. 运行 `scripts/ci-check.ps1`（lint / build / test）并记录到
   `private/dev/TEST-REPORT.md`；
4. 按 `docs/audit-checklist.md` 自审，建议由独立 agent 复审；
5. 提交并推送；发布按根 `AGENTS.md`「发布流程」。

## 代码与文档规范

（按项目实际补充：命名、格式、测试要求、文档语言等）

## 安全问题

- 密钥/凭据绝不入库（`.env`、`*.key` 等已在 `.gitignore`）。
- 发现泄露立即在 `private/AGENTS.md` 记录并轮换。

## 联系我们

（按项目实际填写）
