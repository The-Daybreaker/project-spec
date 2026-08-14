# private/test — 本地测试素材

本目录存放**不能发布到 GitHub** 的本地测试素材（测试库、测试项目、测试数据、
模拟仓库等），由 private 子 git 管理。

约定：

- 测试库/测试项目的**生成物**（缓存、导出、日志等）用 `../.gitignore` 排除，
  不提交 private 子 git。
- 可重建的临时测试仓库放子目录并忽略（如 `staging-repo/`，见 `../.gitignore`）。
- 真实场景测试的场景清单与记录见 `../dev/TEST-REPORT.md` 与 `../dev/DESIGN.md`。
