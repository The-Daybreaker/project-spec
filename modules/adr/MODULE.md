# MODULE.md — 决策记录（模块规范）

> **适用范围**：当 agent 负责维护本模块的产出——`context/adr/` 下的
> decisions.md 与 history.md 时，加载并遵循本文件。项目级总纲见仓库根
> `AGENTS.md`。
>
> 本文件是「决策记录」模块自带的 agent 规范，随模块实例化。

## 一、产物目录与实例化

本模块的产物落在 `context/adr/`，两个文件：

```
context/adr/
  decisions.md   ← 当前仍有效的决策
  history.md     ← 被取代的决策（默认不读）
```

启用时按 `assets/decisions-template.md`（格式仅供参考）实例化 decisions.md，
内容由项目自行实现和改动。

## 二、运行过程

1. 决策及时记录：在对话中确定一个重要决策后，马上写进 decisions.md 顶部。
2. 过程归讨论记录：选路的对比过程（比了哪些路、当时怎么想）写进
   logs/discussion，不写进 decisions.md。
3. 取代：每次写入时，回读全文，发现决策重复或被推翻时，从 decisions.md 整段移出，记入 history.md 顶部，加一行「何时被何取代」；旧文不涂改。

## 三、规范

- decisions.md 只放当前仍有效的决策，新决策写在最上面。
- 被推翻的决策不删，写入 history.md；history.md 默认不读，追溯时才翻。

## 四、适用与边界

- **适用**：有选型 / 选路 / 架构决策等需要留痕的项目。
- **不管**：需求、方案整体组织。
