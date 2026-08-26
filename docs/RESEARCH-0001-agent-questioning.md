# RESEARCH-0001 — agent 提问与共识确认机制（调研）

> 状态：已完成 | 创建：2026-08-26 | 最近更新：2026-08-26 | 取代：—
> 位置说明：本工作区（母项目）无 `private/dev` 登记册，调研记录落于 `docs/`；
> 模板骨架（`project-template/private/dev/research/`）保持不动。

## 调研问题

1. 主流 agent 的澄清提问机制是什么形态？选择题面板是否普遍、有何已知副作用？
2. 业界如何区分「用户回答了问题」与「用户确认了需求/方案」？
3. 有无现成的「共识快照 / 显式确认 / 假设显式化 / 回答后重检」机制可参考？
4. 是否存在与「禁面板 + 开放提问 + 共识确认」完全同款的现成方案？

## 方法与范围

- GitHub 搜索：agent 提问/澄清机制、需求获取（requirements elicitation）、确认工作流；
- 框架与产品文档：Spring AI、Claude Code AskUserQuestionTool、Tessl、Pi Coding Agent；
- 学术/社区：ROPE（arXiv 2409.08775）、OntoChat、SpecBench agent-intent、UX 讨论。

## 发现记录（追加式，新条目在前）

| 日期 | 来源/链接 | 发现/对比结果 |
|---|---|---|
| 2026-08-26 | [When Claude Asks Too Often](https://plutonicrainbows.com/posts/2026-01-07-when-claude-asks-too-often.html) | Claude Code 的 AskUserQuestionTool（结构化多选题面板）被评价「既有用又有点烦」：减少盲目猜测的同时，频繁弹题造成打扰；佐证「面板诱导快速作答/疲劳」问题真实存在。 |
| 2026-08-26 | [Spring AI AskUserQuestionTool](https://spring.io/blog/2026/01/16/spring-ai-ask-user-question-tool) | 主流框架默认把「澄清问题」实现为执行中弹多选题；选择题面板是当前 agent 交互的主流默认形态。 |
| 2026-08-26 | [DmiyDing/clarify-first](https://github.com/DmiyDing/clarify-first) | 风险分级对齐：模糊请求先停下、只问阻塞性问题、破坏性操作前显式确认——「回答」与「确认」分离的雏形；但仍建议「with choices when possible」。 |
| 2026-08-26 | [Agentlas-OS clarify-question-loop](https://github.com/agentlas-ai/Agentlas-OS/blob/main/docs/clarify-question-loop.md) | 澄清时机=缺失细节且影响产物形态；问题预算 1-5 个（偏好 3）；问题应可一句话/一个选择回答——预算控制反疲劳。 |
| 2026-08-26 | [kumaran-is/claude-code-onboarding](https://github.com/kumaran-is/claude-code-onboarding/commit/fd1faff53ba68c63cac17aedf20ded195ad4224b) | 「问太多也比错误假设好」；极端设计：问题全部放专用文件、禁止聊天直接问——与用户诉求相反（用户要聊天内提问并中止），但佐证提问价值与结构化承载的多样性。 |
| 2026-08-26 | [SpecBench agent-intent proposal](https://huggingface.co/datasets/haowang94/specbench/raw/main/projects/agent-intent/proposal.md) | 意图获取框架：开放开场→收窄追问→实时可见可纠正的理解；「收尾：呈现总结并请求最终确认，而不是继续 push」——支持共识快照+显式确认；承认疲劳权衡。 |
| 2026-08-26 | [SpecBench sam_oconnor requirement](https://huggingface.co/datasets/haowang94/specbench/blob/main/projects/agent-intent/requirements/sam_oconnor.md) | 「Wrap up, present the summary, and ask for final confirmation rather than pushing for more」——总结+最终确认优先于继续追问，与共识快照思路一致。 |
| 2026-08-26 | [SpecBench gabriel_ferreira requirement](https://huggingface.co/datasets/haowang94/specbench/blob/main/projects/agent-intent/requirements/gabriel_ferreira.md) | 每次获取会话设预算（轮次/时间）；预算将尽时无条件转入确认模式——疲劳管理与「确认模式」切换。 |
| 2026-08-26 | [discover skill（meta-skills）](https://raw.githubusercontent.com/NeverSight/skills_feed/refs/heads/main/data/skills-md/hungv47/meta-skills/discover/SKILL.md) | 浅深度范围确认时偏好 assumption-surfacing 格式——「防止静默假设失败」；Clarity Check 步骤：总结关键决策、记录未决问题及影响——与反定型/共识快照高度吻合。 |
| 2026-08-26 | [Tessl Spec-Driven Development](https://docs.tessl.io/use/spec-driven-development-with-tessl) | Spec-first 工作流：agent 先逐问澄清→写规格→暂停等评审批准——「先澄清、写产物、显式审批」的完整闭环。 |
| 2026-08-26 | [think-before-coding skill](https://github.com/DevelopersGlobal/ai-agent-skills/blob/main/skills/think-before-coding/SKILL.md) | 歧义时只问「一个阻塞问题」而非 10 个；多方案时给 2-3 选项+权衡再问——问题预算与选项边界的实践。 |
| 2026-08-26 | [ROPE（arXiv 2409.08775）](https://ar5iv.labs.arxiv.org/html/2409.08775) | 需求导向提示工程：用户侧需求表达质量影响结果——需求获取是双向能力，不单是 agent 行为。 |
| 2026-08-26 | [Consensus Server Pattern](https://dev.to/mrclaw207/the-consensus-server-pattern-how-to-catch-ai-confabulation-before-it-reaches-your-users-1kg2) | 多 agent 投票防幻觉/编造——是「内部共识」，非「用户共识」；可作为 agent 内部自查补充，不替代用户确认。 |
| 2026-08-26 | [deepagents ask_user authorization](https://github.com/langchain-ai/deepagents/commit/9975874d897ada8979c084145eb730e15c9cf979) | 授权回执与用户轮次绑定、防复用（trusted user-turn binding）——技术层面把「一次回答」与「一次授权」解耦，佐证回答≠确认。 |
| 2026-08-26 | [HCI 审批完整性](https://www.hci.today/ko/news/7388) | LLM agent 的审批对话框可被虚假解释欺骗——审批/确认 UI 的完整性设计值得警惕，用户对面板的不信任有依据。 |
| 2026-08-26 | [grill-me-html 反疲劳问卷](https://yudesk.dev/blog/grill-me-html) | 一次一问太慢、批量文字问答容易点到麻木；自适应 HTML 问卷提供推荐答案——业界在探索替代面板的反疲劳方案。 |
| 2026-08-26 | [UX：选择不是越多越好](https://note.com/suna81040/n/n34bd4089c901) | 选择多≠亲切，反而增加噪音与疲劳；2 选 1 最强、屏显选项上限 4——选择架构的 UX 结论，支持减少选择题依赖。 |
| 2026-08-26 | [OntoChat](https://link-hkg.springer.com/chapter/10.1007/978-3-031-78952-6_10) | 对话式需求获取（本体工程场景）：LLM 驱动的结构化访谈与聚类——需求获取中「对话式 + 结构化」可并存。 |

## 结论与建议（当前有效结论，可覆盖）

1. **面板是主流默认，但有实证副作用**：主流框架（Spring AI / Claude Code）默认用多选
   题面板收集需求，社区与 UX 讨论普遍指出其「打扰、疲劳、诱导快速作答」问题——用户
   诉求有现实依据，禁面板是合理方向。
2. **业界已有散点实践，但无同款组合**：「总结+最终确认」（SpecBench）、「假设显式化」
   （discover）、「显式确认后推进」（clarify-first / Tessl）、「问题预算」（Agentlas /
   think-before-coding）、「回答与授权解耦」（deepagents）各有一面，但**未见**把
   「禁面板 + 开放提问 + 回答重检 + 共识快照 + 反定型 6 项 + 变更流程回退」组合成
   模板级红线的现成方案——本需求属组合创新。
3. **可借鉴的反疲劳手段**：一次 1-3 个开放问题、问题预算、预算将尽转确认模式——
   与本需求「展示克制」方向一致，可在机制中吸收。
4. **明确不采用**：问题专用文件（kumaran 方案，与用户「聊天内提问并中止」诉求相反）；
   多 agent 投票替代用户确认（内部共识≠用户共识）；生理信号自适应（过度工程）。

## 关联（PRD / RFC / ADR）

- PRD：`docs/PRD-0001-agent-questioning.md`
- ADR：待 P2（机制级红线，必走）
