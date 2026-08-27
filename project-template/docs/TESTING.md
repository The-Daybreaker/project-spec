# 测试落地指引（TESTING.md）

> 模块：全通用。
> 用途：新项目初始化后按本指引落地测试。模板默认以 **pytest** 为示例
> （Python 技术栈），其他框架/语言同理替换；模板自带骨架，不强制任何技术栈。

## 1. 测试相关目录

| 路径 | 区 | 内容 |
|---|---|---|
| `tests/` | A（公开，进 git） | 测试代码（按项目实际创建，模板不预置） |
| `private/test/` | B（私有，不进 GitHub） | 本地测试素材（测试库、测试项目、测试数据） |
| `private/dev/TEST-REPORT.md` | B | 测试记录（每次发布必更新） |
| `.pytest_cache/` / `.coverage` / `htmlcov/` | C | 测试生成物（`.gitignore` 已忽略） |

## 2. pytest 落地步骤（Python 项目示例）

1. 创建 `tests/` 并编写测试，例如：

   ```python
   # tests/test_example.py
   def test_ok():
       assert 1 + 1 == 2
   ```

2. 安装测试依赖（示例）：

   ```bash
   pip install pytest
   pip install pytest-cov          # 覆盖率（可选）
   ```

3. 本地运行：

   ```bash
   python -m pytest
   python -m pytest --cov=src --cov-report=term-missing   # 覆盖率
   ```

4. 接入 `scripts/ci_check.py`：按文件内注释取消 pytest 调用并移除
   `PLACEHOLDER_MARKER` 行（`pre_release_check.py` 会拦截未实现的占位）。
5. 同步 `.github/workflows/ci.yml`（示例步骤已在文件注释中）。
6. 结果记录到 `private/dev/TEST-REPORT.md`（发布前必测，未通过不发布）。

## 3. 非 Python / 无测试框架

- 按技术栈等价实现：Node（`node:test` / jest / vitest）、Rust（`cargo test`）等；
- 至少保留统一检查入口 `scripts/ci_check.py`（lint / build / test），并把结果记入
  `private/dev/TEST-REPORT.md`；
- 无自动化测试的项目：`TEST-REPORT.md` 中写明「人工验证清单」与运行方式。

## 4. 用例登记与自测/用户验收分流

### 用例登记表（推荐字段）

| 编号 | 场景 | 步骤与数据 | 预期结果 | 负责人 | 实际结果 | 结果 |
|---|---|---|---|---|---|---|
| T1 | <场景> | <步骤/数据> | <预期> | agent | <实际> | ✅ / ❌ |
| U1 | <需人判断的场景> | <步骤/数据> | <预期> | 用户 | — | ✅ / ❌ |

### 分流标准

- **能自测**（agent 执行，进测试报告「自测区」）：有确定预期且 agent 可执行——
  命令/断言/扫描/文档一致性/冒烟；用例编号 T*；
- **不能自测**（交用户验收，进测试报告「用户验收区」）：需人的感官判断、真实
  账号/外部平台、发布后观测、业务价值判断；用例编号 U*，含**签署标准**
  （✅ 通过 / ❌ 未通过），对齐 UAT 与 IEEE 829 实践。

## 5. 门禁与例外

- **发布前必测**：检查命令 + 项目测试，结果记录于 `private/dev/TEST-REPORT.md`；
  未通过不发布；
- **明文例外（仅此一种）**：本次改动不涉及运行时文件、且用户明确确认时，测试结论
  可沿用上一版本，必须在 TEST-REPORT 注明「用户确认沿用」；禁止 agent 自行省略。
