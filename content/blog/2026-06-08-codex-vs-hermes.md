---
title: "Codex 那么全能，为什么还需要 Hermes？"
date: "2026-06-08T14:30:00+08:00"
updated: "2026-06-08T17:23:44+08:00"
slug: "codex-vs-hermes"
description: "Codex App 是 OpenAI 面向本地/云端编码线程的高强度工作台，Hermes Agent 是 Nous Research 的开源常驻 Agent 系统。两者的关键差异不在功能数量，而在运行边界、自动化入口、消息交付、模型治理和长期记忆。本文修正若干常见误解，并拆解生产开发流水线、印刷厂任务记忆、Autonovel、跨平台研究和团队 Telegram 助理等复杂 Hermes 案例。"
categories:
  - "AI"
tags:
  - "Codex"
  - "Hermes"
  - "AI Agent"
  - "架构分析"
  - "Claw Code"
  - "OpenAI"
series:
  - "AI Agent"
featured_image: "/images/posts/codex-vs-hermes/codex-vs-hermes-cover.png"
pinned: false
---

Codex App 发布后，一个很自然的问题是：OpenAI 已经把桌面编码、文件编辑、终端、Git、Worktree、Automations、MCP、Computer Use、Browser、Skills 都做到一个产品里了，为什么还需要 Hermes 这样的 Agent 框架？

更准确的回答不是“谁更强”，而是：

**Codex App 是一个面向代码仓库的高强度 Agent 工作台；Hermes Agent 是一个可以常驻、跨平台、跨模型、可沉淀记忆和技能的 Agent 系统。**

截至 2026-06-08，这个判断需要先修正几个常见误解：

- Codex App 不是整个 Codex 产品线。Codex 还包括 CLI、IDE Extension、Cloud、SDK 等形态；本文主要比较桌面端 Codex App 与 Hermes Agent。
- Codex 不是完全不能换模型。本地 Codex 可以指向支持 Chat Completions 或 Responses API 的模型/供应商；但 Codex Cloud 当前不能改默认模型，OpenAI 推荐模型仍是最完整的一等体验。
- Codex 不是“关闭就一切归零”。Codex 有 threads、thread automations，以及可用时的 Memories；只是它的长期记忆和消息网关不是 Hermes 那种显式的常驻系统。
- Hermes 也不是只有终端。Hermes 已经有 CLI、Messaging Gateway、Cron、Web/Dashboard 以及 native desktop app；但它的核心仍是 gateway/daemon 形态，而不是单一桌面应用。

## 一、系统边界先说清楚

### Codex App：项目内编码线程和本地自动化

![Codex 架构图](/images/posts/codex-vs-hermes/codex-architecture.png)

OpenAI 文档把 Codex App 定义为一个“focused desktop experience”，用来并行处理 Codex threads。它的核心能力是围绕本地项目和 Git 仓库组织起来的：

- **线程模式**：Local、Worktree、Cloud。Local/Worktree 在你的电脑上运行，Cloud 在配置好的远程环境中运行。
- **编码工具链**：文件读写、Shell/PowerShell、Git diff/commit/push/PR、集成终端、沙箱和审批。
- **扩展能力**：MCP、Skills、Web search、in-app browser、Computer Use、图片生成、非代码 artifacts 预览。
- **自动化**：Codex Automations 可以按计划运行，项目级任务可以进入 Inbox；thread automations 可以保留同一个 thread 的上下文做心跳式跟进。
- **模型**：OpenAI 当前推荐 Codex 使用 `gpt-5.5`、`gpt-5.4`、`gpt-5.4-mini` 等模型；本地 Codex 也可以配置兼容 Chat Completions 或 Responses API 的其他 provider/model。Codex Cloud 当前不能改默认模型。

这里最重要的限制不是“功能少”，而是**运行边界**：项目级 Automations 要求运行本地 Codex App 的机器开机、Codex 运行、项目仍在磁盘上。Codex App 也不是一个通用的公网 webhook gateway 或聊天平台机器人框架。

### Hermes Agent：常驻入口、模型路由和过程性记忆

![Hermes 架构图](/images/posts/codex-vs-hermes/hermes-architecture.png)

Hermes 的设计重心不同。它是 Nous Research 的开源 Agent 系统，强调“agent lives where you do”：

- **入口**：CLI、Desktop、Messaging Gateway、Cron、API/Web/Dashboard、Python/RPC 工具。
- **消息平台**：Telegram、Discord、Slack、WhatsApp、Signal、Email、Matrix、Mattermost、Lark/Feishu、DingTalk、WeCom/Weixin、Teams、LINE、ntfy、Browser 等多平台 adapter。
- **模型供应商**：README 当前重点列出 Nous Portal、OpenRouter、NovitaAI、NVIDIA NIM、Xiaomi MiMo、z.ai/GLM、Kimi/Moonshot、MiniMax、Hugging Face、OpenAI 和自定义 endpoint；本地/自托管路径可通过 Ollama、vLLM、llama.cpp 或 OpenAI-compatible endpoint 接入。
- **工具系统**：终端、文件、Web/search、browser、media、memory/session search、cron/delivery、Home Assistant、MCP 等 40+ 工具类别。
- **记忆**：持久记忆主要由 `MEMORY.md`、`USER.md` 这类有边界的文本记忆注入会话；README 另提到 FTS5 session search 用于跨会话检索。不要把它简化成一个万能“Memory DB”。
- **Cron**：Cron 运行在 Hermes gateway daemon 所在的位置。gateway 在 VPS 上，就不依赖你的笔记本；gateway 在本机上，本机仍然是运行前提。

Hermes 的关键词是**常驻服务**。它更像一个可被消息、cron、webhook、脚本、团队频道反复唤起的 Agent host。

## 二、核心差异对比

| 维度 | Codex App | Hermes Agent |
|------|-----------|--------------|
| 主要定位 | 桌面/云端编码线程工作台 | 常驻、多入口 Agent 系统 |
| 最强场景 | 修改代码、验证、Git 工作流、前端/桌面测试 | 消息触发、cron/webhook、跨平台交付、长期工作流 |
| 模型 | OpenAI 推荐模型是一等体验；本地可配置兼容 provider；Cloud 默认模型当前不可改 | 多 provider 和自定义 endpoint 是核心设计，支持本地/自托管路线 |
| 自动化 | App 内 Automations；项目级任务依赖本机 App、项目磁盘和沙箱配置 | Gateway/Cron 所在机器常驻；可在 VPS/服务器上 7x24 运行 |
| 交付 | App Inbox、线程、通知、Git/PR | Telegram/Discord/Slack/Email/Browser/本地文件/API 等 |
| 记忆 | threads、thread automations、Memories（可用时） | `MEMORY.md`/`USER.md`、session search、skills 过程沉淀 |
| 扩展 | MCP、Plugins、Skills、local environments | MCP、tools/toolsets、skills、gateway adapters、RPC 脚本 |
| 团队消息 | 不是通用消息平台机器人 | 多平台 Messaging Gateway 是核心能力 |
| 开源属性 | OpenAI 产品线 | MIT 开源项目 |

所以，Codex App 和 Hermes 的关系不是“替代”，而是“运行边界不同”。

## 三、为什么有了 Codex App 还需要 Hermes？

### 场景一：高强度编码任务，Codex App 更直接

如果目标是重构一个模块、修 bug、写 feature、跑测试、看 diff、提交 PR，Codex App 通常更顺手：

- 它的界面、Git diff、Worktree、审批和终端都围绕仓库修改组织。
- 它能把本地项目、IDE context、in-app browser、Computer Use 串在一个桌面工作流里。
- OpenAI 推荐模型在编码、工具调用和复杂推理上是一等入口。
- 对个人开发者来说，App 内 Inbox、thread automation、worktree 隔离已经能覆盖很多周期性代码任务。

Hermes 也能写代码，但它的优势不在“把一个本地仓库改得最快”，而在“把代码任务放进一个长期、跨平台、可被事件触发的系统”。

### 场景二：事件驱动和公网 webhook，Hermes 的形态更合适

Codex App 可以做定时轮询，也能通过插件和 GitHub 工具处理 PR 状态。但它不是一个对外暴露路由、校验 HMAC、接收 GitHub webhook、再把结果评论回 PR 的常驻服务。

Hermes 的 Messaging Gateway/Webhook/Cron 模式天然适合这类事情：

- GitHub、监控系统或业务系统发事件。
- Gateway 校验请求并把 payload 变成 Agent prompt。
- Agent 加载 skill，调用终端、GitHub CLI/API、项目脚本。
- 结果回写 GitHub、发到 Telegram/Discord/Slack，或保存到本地文件。

这不是“Codex 不能借助外部服务做到”，而是**Codex App 自身不是这个系统边界**。你需要 GitHub Actions、自建 server、Codex CLI/SDK 或其他 bot framework 做 glue code。Hermes 把这层 glue code 放进了产品架构。

### 场景三：跨平台异步协作，Hermes 是更自然的入口

现实里的工程讨论经常发生在群聊里：

- Telegram 里问“昨晚监控有没有异常？”
- Discord 里 @agent “看一下这个 PR diff”
- Slack 里让它把 CI 失败总结成 issue
- 手机上用语音或消息触发一个服务器任务

Codex App 有桌面 App、IDE 同步、ChatGPT mobile 远程连接等能力，但它不是一个覆盖 20+ 平台的 messaging gateway。Hermes 的假设是：Agent 应该活在你已经在用的通信流里。

### 场景四：长期记忆和 skill 沉淀，Hermes 的表达更显式

Codex 已经有 threads、thread automations 和 Memories，所以“Codex 每次都从零开始”是不严谨的。

真正的差异在于，Hermes 把长期记忆和过程性经验做成了更显式的用户资产：

- `MEMORY.md`、`USER.md` 用来存稳定偏好、个人背景、项目约定。
- Session search 用来找历史会话里的事实和决策。
- Skills 可以把成功完成复杂任务的流程固化为可复用说明和脚本。
- Gateway/Cron 可以在不同入口复用这些记忆和 skill。

这也不是魔法。长期记忆需要治理，skill 也需要审阅，否则错误经验会被固化。但对于“同一个 Agent 长期服务同一个人/团队”的场景，这个方向比单次编码会话更重要。

### 场景五：模型和工具治理，Hermes 更偏“可编排系统”

过去常见的说法是“Codex 绑死 OpenAI，Hermes 才能换模型”。这个说法现在需要收窄：本地 Codex 可以配置兼容 provider/model。

但二者的产品重心仍然不同：

- Codex 的最佳路径是 OpenAI/ChatGPT 账号、推荐 Codex 模型、Codex App/CLI/IDE/Cloud 的一体化体验。
- Hermes 把 provider 选择、`/model` 切换、自定义 endpoint、本地模型、工具后端、消息平台 delivery 都作为一等配置面。

如果你在做的是“用一个 agentic runtime 统一管理多个模型、多个工具后端、多个触发入口”，Hermes 的心智负担反而更低。

### 场景六：非编码任务和个人/团队 ops，Hermes 覆盖更宽

Codex 的工具生态正在扩展，已经不再只会写代码。但它的默认工作对象仍是项目、线程、文件、Git、浏览器预览和桌面应用。

Hermes 的工具面更像“知识工作者的操作台”：消息、邮件、日历、YouTube/媒体、Home Assistant、搜索、浏览器、服务器脚本、定时任务、通知交付。它适合把很多“不是写代码但围绕工程和生活运转”的任务串起来。

## 四、复杂案例拆解：Hermes 的价值不止 PR Bot

用户真正应该看的不是“安装 Hermes + 接一个模型”的教程，而是 **Hermes 能不能作为常驻系统接入真实工作流**。

我把公开材料按证据强度分成三层：

| 证据层级 | 能证明什么 | 不能证明什么 |
|----------|------------|--------------|
| 第一手生产报告 | 有真实用户把 Hermes 用在长期工作里，暴露了成本、记忆、稳定性问题 | 通常没有完整业务代码，不能一键复现 |
| 官方或社区可运行 repo | 架构和执行链路真实存在，可以拆解实现 | 不一定证明有外部生产部署 |
| usecase/runbook | 说明 Hermes 的 gateway、cron、skill、delivery 能如何组合 | 只是可落地方案，不等于已经生产运行 |

下面这些案例都排除了 React Native Hermes、OpenHermes 模型和 Hermès 奢侈品牌等同名噪音。

### 案例一：生产软件开发流水线，Hermes 作为长期工程搭档

来源是 [NousResearch/hermes-agent issue #5563](https://github.com/NousResearch/hermes-agent/issues/5563) 和社区整理的 [Production Software-Dev Workflow](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/production-software-dev-workflow.md)。这不是教程，而是一个重度用户的第一手 field report：连续 3 周、每天 8 小时以上，把 Hermes 用在生产软件开发中，项目涉及 DBOS、PostgreSQL、S3、Gmail API，并编排一个 3 actor email processing pipeline。

这个案例的工作流可以拆成四层：

```text
业务目标
  -> 多 actor 邮件处理 pipeline
  -> DBOS / PostgreSQL / S3 / Gmail API 代码与配置
  -> Hermes CLI 长会话、文件/终端/search 工具
  -> memory、session_search、delegate_task 子代理维持长期上下文
```

它说明的不是“只有 Hermes 能写代码”。恰恰相反，单仓库重构、测试、Git diff、PR 准备这类任务，Codex App 往往更顺手。这个案例真正有价值的地方在于，它把 Hermes 当成一个多日持续工作的工程 runtime，而不是一次性代码助手。

Hermes 的能力点有三个：

1. **长期上下文不是聊天记录本身，而是可检索状态**。用户依赖 persistent memory 和 `session_search` 跨天找回工程事实。
2. **复杂任务靠 delegation 降低主会话压力**。`delegate_task` 把局部问题拆给子代理，主线程维持架构判断和任务协调。
3. **真实生产会暴露 runtime 成本**。报告里提到一个约 12 小时 session 因上下文 replay 浪费约 2.6M tokens，还遇到 `state.db` 损坏、`MEMORY.md` 太小、环境幻觉等问题。

这个案例反而让文章更严谨：Hermes 的优势不是“永远自动、更省钱、更稳定”，而是它敢把长期记忆、session search、gateway、subagent 放在用户能改、能修、能扩展的位置。缺点也同样暴露在这个位置。对 Codex App 来说，它当然可以参与同一个代码库开发，但它的产品边界是一个桌面/云端 coding thread 工作台，不是让用户维护一个跨天、跨入口、跨脚本的 agent runtime。

证据 caveat：业务代码是私有的，所以它不能当作可复现 benchmark。它能证明的是“有人真实重度使用 Hermes 进行生产开发，并给出了具体失败模式和指标”，不是“你 clone 后能跑同一套 pipeline”。

### 案例二：印刷厂任务记忆，Hermes 作为业务运营记忆层

来源是 [NousResearch/hermes-agent issue #11653](https://github.com/NousResearch/hermes-agent/issues/11653)、社区整理的 [Printing-Factory Task Memory](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/printing-factory-task-memory.md)，以及作者开源的 [task-centric-memory-skill](https://github.com/Xwm1234/task-centric-memory-skill)。

这个案例很重要，因为它不是软件工程场景。用户经营印刷厂，日常任务包括印刷排期、库存、客户请求、任务完成状态。长会话变慢、记忆变差后，用户没有等 Hermes 官方改核心系统，而是写了一个 `Task-Centric Memory` skill：

```text
用户发来运营任务
  -> skill 自动判断领域：Printing / Stocks / 其他业务域
  -> 进行任务状态建模：In-Progress 保留完整细节
  -> Completed 任务压缩为 summary cards
  -> 写入本地 JSON index
  -> 后续遇到相似客户/任务时，亚秒级检索并注入相关历史
```

这里 Hermes 的关键不是“有 memory”这三个字，而是**记忆可以由用户按业务域改造**。印刷厂不需要一个昂贵的通用向量数据库，可能只需要本地 JSON 索引、任务分类、分层压缩和一个明确的 skill 触发规则。

这类场景对 Codex App 很难自然承载，原因不是 Codex 不能读写 JSON，也不是 Codex 没有 Memories。难点在运行形态：

1. 这是一个业务运营助理，不是代码仓库里的一个 feature thread。
2. 任务会从聊天、电话摘要、客户消息、人工补录等不同入口持续进入。
3. 记忆规则需要按业务域沉淀，而不是只在某个 repo 的开发线程里保留上下文。
4. 结果需要成为一个长期可维护的个人/团队资产，而不是一次对话里的提示词技巧。

这个案例最能说明 Hermes 和 Codex App 的差异：Codex App 的强项是把一个项目改好；Hermes 的强项是让用户把 Agent 变成某个业务流程里的长期角色。

证据 caveat：开源 skill 是社区贡献，不等于官方审计过的生产模块。实际使用时要检查本地脚本读写路径、隐私数据和备份策略。

### 案例三：Autonovel / House of Bells，Hermes 作为端到端创作工厂

来源是官方 repo [NousResearch/autonovel](https://github.com/NousResearch/autonovel) 和社区整理的 [Autonovel: House of Bells](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/autonovel-house-of-bells.md)。仓库描述明确写着它是 “An autonomous novel writing pipeline, by Hermes Agent”。这个项目产出了《House of Bells》：19 章、79,456 词，经过 6 轮自动修订和 6 轮 Opus review，并生成 LaTeX 排版、插图、封面和 4,179 段 audiobook。

它的链路不是“让模型写一章小说”，而是一个可拆分的生产管线：

```text
seed / program
  -> world、canon、characters、outline
  -> chapter draft
  -> review / evaluate / adversarial edit
  -> revision rounds
  -> LaTeX typeset
  -> art directions / cover / illustrations
  -> audiobook script / voice generation
  -> landing page and final artifacts
```

这个案例里的 Hermes 价值在于 orchestration。真正困难的是状态机：哪个章节已经冻结，哪一轮 review 通过，世界观和人物设定如何回灌到后续章节，哪些产物可以并行生成，最终如何把文本、图像、音频、排版组织成一个交付物。

Codex App 当然可以帮你写这样的 pipeline，也可以生成非代码 artifacts。但 Codex App 的默认交付形态仍然是 thread、文件改动、预览和 Git 工作流。Autonovel 体现的是另一个方向：Agent host 负责长时间驱动多个脚本、多个模型 API、多个产物目录和多轮质量门槛，直到最终作品冻结。

这个案例也提醒我们，不要把 Hermes 理解成“聊天机器人”。在复杂创作里，Hermes 更像 workflow runner：让 LLM 不是只产出文本，而是参与一个带检查点、评审、修订和发布工序的系统。

证据 caveat：这是官方项目，证据强，但它不是低成本日常 demo。跑完整链路需要模型、图像、语音 API 和足够的 wall-clock time。

### 案例四：跨平台研究简报，Hermes 作为研究编排入口

来源是 [Multi-Platform Social Media Research](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/multi-platform-research.md) 和 [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)。`last30days` 不是 Hermes 独占能力，它也支持 Codex、Cursor、Claude Code、Gemini CLI 等 agent skills host。它仍然适合放进这篇文章，因为它展示了 Hermes 作为 gateway/cron/delivery host 时能承载什么复杂研究任务。

典型链路是：

```text
一个研究主题
  -> Reddit / X / YouTube / Hacker News / Polymarket / GitHub 等多源并行搜索
  -> 账号、cookie、API key、yt-dlp、平台 fallback 各自处理
  -> 去重、聚类、评论/转录提取、engagement scoring
  -> agent judge 综合判断
  -> Markdown / HTML brief
  -> Telegram、Discord、Obsidian、本地文件或邮件交付
```

这个案例的复杂度不在单次搜索，而在“把多个封闭平台变成一个可重复研究过程”。如果你每周一早上都要看“AI coding agents 最近 30 天社区怎么讨论”，Hermes 可以用 cron 触发，调用 skill，最后把简报送进群聊或知识库。

Codex App 也有 web search、skills、browser 和非代码 artifact 能力，所以不能说它做不了研究。区别在于：Codex App 更像你打开一个研究线程；Hermes 更像你把研究流程部署成一个会定期醒来的服务。前者强在交互式深挖，后者强在跨平台入口、定时运行和消息交付。

证据 caveat：这个 skill 是跨 host 的，不能写成 Hermes 独占壁垒。Hermes 的优势来自它和 cron、messaging gateway、长期记忆组合后的运行形态。

### 案例五：零 token 通知/监控，Hermes 作为低成本事件过滤器

来源是 [Zero-Token Notifications](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/zero-token-notifications.md) 和社区 repo [agent-notifications](https://github.com/Kuberwastaken/agent-notifications)。它解决的是一个很实际的问题：cron 监控如果每 5 分钟都唤醒 LLM，即使 99% 时间没变化，也会持续烧 token。

更合理的链路是：

```text
cron 定时触发
  -> 纯 Python checker 先跑
  -> 没变化：无输出或返回 SILENT
  -> 有变化：输出结构化 diff
  -> Agent 只在变化时总结、判断优先级、决定 delivery
  -> Telegram / Email / Slack / Discord / local file
```

这个模式把确定性逻辑和 LLM 推理分开：抓取、diff、去重、状态保存交给脚本；解释、归因、下一步建议交给 Agent。它不是炫技，而是长期自动化能不能负担得起的核心设计。

Codex Automations 可以做定时任务，也可以跑项目脚本并汇报 findings。但 OpenAI 文档明确说明，项目级 automations 需要本机 Codex App 运行、机器开机、项目还在磁盘上。它的产品机制是“Codex 定时执行任务并把 findings 放进 Inbox”。Hermes 这个案例则更像一个后台 daemon：先用脚本决定是否值得唤醒 Agent，再把变化推到外部渠道。

证据 caveat：`agent-notifications` README 也说明它适配 Hermes、OpenClaw 和原始 cron。对于 Hermes，“真正零 token 的空跑”可能需要 scheduler patch 或严格的 silent-if-empty 编排。不要把 runbook 写成官方内置承诺。

### 案例六：Team Telegram Assistant，Hermes 作为团队常驻入口

来源是 [Team Telegram Assistant](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/team-telegram-assistant.md) 和 Hermes 官方团队 Telegram 教程。这个案例不是让 Agent 多会写代码，而是把 Agent 放进团队消息流里：

```text
Telegram 私聊或群聊 mention
  -> gateway 校验 bot token 和 allowlist
  -> 每个用户进入自己的 session / memory
  -> 需要 shell 时走 Docker terminal backend
  -> cron output、GitHub triage、backup report 进入 home channel
  -> 团队成员在同一个通信入口消费结果
```

这里最重要的是安全边界。团队 bot 不是个人桌面助手。任何被 allowlist 的成员理论上都能触发工具调用，所以 runbook 推荐 Docker terminal backend，把 shell 操作限制在容器里，避免授权用户直接影响 VPS host。

Codex App 也有协作相关能力，Codex Cloud、GitHub、SDK、IDE Extension 都能进入团队研发流程。但 Codex App 本身不是 Telegram bot framework，也不是多用户消息网关。要做同样的事情，需要另写 Telegram bot、鉴权、session 映射、delivery、sandbox 和任务路由。Hermes 的优势是把这些作为一等运行形态，而不是外部 glue code。

证据 caveat：这个案例是 first-party demo/runbook，能证明架构路径清晰、可运行，但它仍需要你正确配置 token、allowlist、Docker、日志和密钥管理。

### 顺手补充：PR 自动审查机器人仍然有参考价值

用户前面提到的 PR 自动审查机器人仍值得保留，但它不应该是唯一案例。[webhook 版本](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/github-pr-review-webhook.md) 和 [cron 版本](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/github-pr-review-cron.md) 的核心不是“AI 看 diff”，而是把 PR review 做成常驻服务：

```text
GitHub pull_request 或定时轮询
  -> Hermes gateway / cron
  -> 校验事件或过滤 open PR
  -> 加载 review skill
  -> 调用 gh pr diff / gh api / 项目测试脚本
  -> 写回 GitHub review
  -> 可选同步 Telegram / Discord / Slack
```

这个场景依然是 Codex App 很难独立完成的典型例子：Codex 可以很好地审查一个 PR，也可以通过 automation 轮询项目状态；但它本身不是公网 webhook server，也不是跨平台消息机器人。要做到团队级常驻 PR bot，Codex 需要 GitHub Actions、自建服务、Codex CLI/SDK 或其他 bot framework 作为外层编排。Hermes 则把 gateway、cron、delivery、skill 和工具调用放在同一个系统边界里。

### 从案例反推真正差异

这些案例合起来，比单纯功能列表更能说明问题：

| 真实需求 | 更像 Codex App 的部分 | 更像 Hermes 的部分 |
|----------|----------------------|--------------------|
| 修一个 repo 的 bug、跑测试、看 diff、提交 PR | 强 | 可做，但不是最顺手 |
| 长期业务记忆和可检索操作历史 | 有 threads/Memories，但不是业务 memory framework | 强，skill + memory + session search 可改造 |
| 多平台消息入口和交付 | 需要外部 glue | 强，gateway/delivery 是核心形态 |
| 定时研究、监控、日报 | 有 App automations，受本机 App 和项目边界约束 | 强，适合 daemon/VPS/cron |
| 多脚本、多模型、多产物的 pipeline | 可帮助编写和验证 | 更像 workflow host |
| 团队共享 bot | 需要额外系统 | 更自然 |

严谨地说，Codex CLI/SDK 加上外部服务，理论上也能搭出很多 Hermes 类系统。本文比较的是 **Codex App 本身** 和 **Hermes Agent 这类常驻 agent host**。所以结论不是“Codex 做不到”，而是“Codex App 的一等产品边界不在那里”。

## 五、怎么选？

你更像 Codex App 用户，如果：

- 主要工作是在本地/云端代码仓库里完成修改。
- 关心 diff、测试、Git、Worktree、前端预览、Computer Use。
- 能接受自动化运行在本机 App 或 Codex Cloud 的边界里。
- 希望尽量少配置，直接用 OpenAI 推荐模型和一体化体验。

你更像 Hermes 用户，如果：

- 需要一个 7x24 常驻的 Agent gateway。
- 需要 Telegram/Discord/Slack/Email 等消息入口和交付。
- 需要接收 webhook、跑 cron、调用脚本、把结果发回多个平台。
- 需要长期记忆、session search、skill 沉淀和多入口复用。
- 需要更强的模型/provider/tool 后端治理，包括本地或自托管模型。

很多实际工作流会同时使用二者：

- Codex App 负责本地高强度编码、修 bug、重构、验证和 PR 准备。
- Hermes 负责常驻自动化、消息机器人、跨平台通知、长期记忆和团队 ops。

## 六、结语

Codex App 和 Hermes 的分野不是“一个全能、一个落后”，而是：

- **Codex App 把编码工作台做深**：线程、Worktree、Git、终端、Browser、Computer Use、Automations 都围绕仓库修改组织。
- **Hermes 把 Agent host 做宽**：消息网关、Cron、provider routing、toolsets、memory、skills、delivery 都围绕常驻服务组织。

所以，Codex App 的存在不会消灭 Hermes 的价值。只要你的问题从“这次帮我改代码”变成“这个 Agent 能不能长期在我的工程和消息流里工作”，Hermes 就仍然有独立位置。

---

参考入口：

- [Codex App features](https://developers.openai.com/codex/app/features)
- [Codex Automations](https://developers.openai.com/codex/app/automations)
- [Codex Models](https://developers.openai.com/codex/models)
- [Hermes Agent README](https://github.com/NousResearch/hermes-agent)
- [Hermes Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)
- [Hermes Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
- [Hermes Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
- [Production Software-Dev Workflow](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/production-software-dev-workflow.md)
- [Hermes issue #5563: heavy production use field report](https://github.com/NousResearch/hermes-agent/issues/5563)
- [Printing-Factory Task Memory](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/printing-factory-task-memory.md)
- [Task-Centric Memory Skill](https://github.com/Xwm1234/task-centric-memory-skill)
- [Autonovel: House of Bells](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/autonovel-house-of-bells.md)
- [NousResearch/autonovel](https://github.com/NousResearch/autonovel)
- [last30days-skill](https://github.com/mvanhorn/last30days-skill)
- [Zero-token notifications](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/zero-token-notifications.md)
- [agent-notifications](https://github.com/Kuberwastaken/agent-notifications)
- [Team Telegram Assistant](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/team-telegram-assistant.md)
