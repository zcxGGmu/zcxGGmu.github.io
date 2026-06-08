---
title: "Codex 那么全能，为什么还需要 Hermes？"
date: "2026-06-08T14:30:00+08:00"
updated: "2026-06-08T14:30:00+08:00"
slug: "codex-vs-hermes"
description: "Codex 是 OpenAI 的全能编码 Agent，Hermes 是 Nous Research 的自进化 AI 框架。它们的竞争不在功能数量上，而在架构哲学的根本分野：Cloud-first vs Local-first，Single-provider vs Multi-provider，Session-bound vs Cross-session。这篇文章从架构图出发，深入分析两种 Agent 的设计选择及其适用边界。"
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

Codex App 发布后，一个很自然的质疑是：当 OpenAI 已经做出了一个可以在桌面端自主编码、读文件、跑命令、设置定时任务、甚至调用子 Agent 的工具，为什么还需要另一个 Agent 框架？

简单回答：**Codex 解决的是"怎么让 AI 帮你写代码"，Hermes 解决的是"怎么让 AI 成为一个持续的工程伙伴"。**

这句话隐藏着两类 Agent 在架构哲学上的根本分歧。下面我们从架构图出发，逐步展开。

## 一、系统架构对比

本文的对比对象是 **Codex App**（OpenAI 的桌面编码 Agent，包含 CLI、IDE 扩展和 Web 端）与 **Hermes Agent**（Nous Research 的开源自进化 Agent 框架）。Codex App 是目前 Codex 产品线中最完整的产品形态，支持 Automations（定时任务）、Worktrees、Review、Computer Use 等功能。

### Codex App：深度编码体验 + 项目级自动化

![Codex 架构图](/images/posts/codex-vs-hermes/codex-architecture.png)

Codex App 的架构可以用一句话概括：**本地 Agent Runtime + 远程 OpenAI 模型 + 项目级自动化**。它运行在你的机器上，负责读取配置、加载 AGENTS.md、管理工具调度（Shell、文件系统、Git、MCP、Computer Use），每一次推理通过 HTTPS 调用 OpenAI API。

这个设计的核心特征：

1. **单一模型供应商** — 必须使用 OpenAI 的模型（GPT-4o、o4-mini 等），通过 ChatGPT 订阅或 API Key 接入。没有切换模型的自由。
2. **会话级状态** — Codex 的一次对话是自包含的。关闭 App，会话结束。没有跨会话的持久记忆。
3. **工具围绕代码展开** — Shell、文件编辑、Git、沙箱执行、MCP、Computer Use。所有工具都为编码场景优化。
4. **Automations（定时任务）** — Codex App 支持通过 cron 表达式设置定时任务，结果发送到 Inbox。但要求 Codex App 保持运行、机器开机、项目在磁盘上可用。支持 Worktree 隔离。
5. **Subagent 横向扩展** — 支持子 Agent 并行执行任务，共享同一模型和工具集。

### Hermes Agent：多模型、多平台、自进化的 Agent 系统

![Hermes 架构图](/images/posts/codex-vs-hermes/hermes-architecture.png)

Hermes 的架构在多个维度上做出了截然不同的选择：

1. **多入口点** — CLI (`hermes`)、消息网关（Discord / Telegram / Slack / Signal / WhatsApp / Matrix / Email / WeChat）、ACP 适配器、Cron 调度器、API Server、Python 库。

2. **多模型供应商** — OpenAI、Anthropic、DeepSeek、Google、xAI、Groq、Mistral、OpenRouter、Nous Portal，以及本地 llama.cpp / vLLM / Ollama。热切换：`/model deepseek:deepseek-v4-pro`。

3. **跨会话持久化** — Memory DB（SQLite + FTS5 全文搜索）让 Hermes 记住用户偏好、项目结构。Session Search 检索历史对话。

4. **自进化的技能系统** — 执行复杂任务后自动抽象为"技能"（Skill），包含完整执行逻辑和陷阱说明。

5. **工具生态远超编码** — 40+ 工具：Terminal、File System、Browser、ComfyUI（图片生成）、TTS、Spotify、GitHub、Notion、Linear、Airtable、Email、Calendar、YouTube、Maps、Home Assistant、Kanban、Obsidian、OCR……

6. **Cron 调度器** — 服务端常驻执行，不需要本地机器开机。支持多平台推送（Telegram、Discord 等）、script-only 零 token 模式、job 间链式依赖。

### 核心差异对比

| 维度 | Codex App | Hermes Agent |
|------|-----------|-------------|
| **模型自由度** | 仅 OpenAI | 20+ 供应商，可本地部署 |
| **入口点** | 桌面 App / CLI / IDE / Web | 终端 + 消息平台 + Cron + API |
| **持久化** | 会话内 | 跨会话 Memory + FTS5 检索 |
| **技能系统** | 静态 Skills | 自进化的过程性技能 |
| **工具范围** | 编码工具 + Computer Use | 生活+工作全栈工具 |
| **定时任务** | Automations（需本机开机+App运行） | Cron 调度器（服务端常驻） |
| **定时任务交付** | Inbox（App 内查看） | 多平台推送 / 本地文件 / 链式依赖 |
| **生态系统** | OpenAI 封闭生态 | 开源 MIT + 社区 Skill Hub + Skills Hub |
| **多平台消息** | 无 | Discord / Telegram / Slack / Signal 等 20+ |

## 二、Codex 那么全能，为什么还需要 Hermes？

这不是一个"谁更好"的问题，而是**"你在解决什么问题"**的问题。Codex 和 Hermes 分别适合不同的使用场景。

### 场景一：纯编码任务 → Codex 是更好的选择

如果你打开终端的目的是：重构一个模块、修复一个 bug、写一段新的 feature、审查代码，那么 Codex 是更直接的选择。

**原因：**
- Codex 的工具链围绕代码优化到了极致：Shell、文件编辑、Git、沙箱、MCP。每一个工具都是为编码场景调优的。
- Codex 的 prompt 工程经过 OpenAI 的大量优化，在代码理解和生成上的表现是顶级的。
- 不需要跨会话记忆——一次编码会话通常是一次性的、自包含的。
- ChatGPT 订阅用户的开箱体验极好：`curl ... | sh` 一条命令装完，登录 ChatGPT 账号就能用。

**Hermes 也能做编码，但不是它的主战场。** Hermes 的工具更泛化，模型选择更多样，但在纯编码任务的"平均体验"上，不如 Codex 聚焦。

### 场景二：跨会话工程协作 → Hermes 是唯一的选择

当你的工作跨越多个会话、多天甚至多周——例如一个持续演进的开源项目贡献——Hermes 的持久化能力就变成了刚需。

**具体来说：**

1. **Memory 系统**：Hermes 会在你第一次告诉它"这个项目用的是 pytest + xdist"后，把这个事实存入持久化记忆。下次新开一个会话，这个知识会自动注入 system prompt。你不需要重复解释。

2. **Session Search**：你可以问 Hermes "我们上周讨论的那个 PR #42 是怎么处理的？"，它会从 SQLite 数据库中检索历史对话并给出准确答案。Codex 做不到这一点——关闭终端，一切归零。

3. **Skills 的积累效应**：每一次成功完成一个复杂任务，Hermes 都会把执行模式沉淀为技能。使用 Hermes 的时间越长，它就越懂你的工作流。Codex 的每次对话都是"从零开始"。

**这是最深层的差异：Codex 是工具，Hermes 是伙伴。** 工具每次使用前都要重新"设置"，伙伴记得你们共同的历史。

### 场景三：多平台异步协作 → 这是 Hermes 的独特定位

Codex App 是桌面应用，交互发生在 App 内部。但现实中，很多工程讨论发生在群聊里。

Hermes 的 Messaging Gateway 让它可以在 Discord、Telegram、Slack 等平台上被团队成员 @ 唤起。你可以：

- 在 Discord 群里 @Hermes "review 一下这个 PR"
- 在 Telegram 里让它查一下今天的 CI 状态
- 在 Slack 里让它创建 Linear issue

同时，因为 Memory 是跨平台的，你在 Telegram 上交代过的偏好，在 Discord 会话中也会被记住。

**Codex App 没有消息平台集成。** 它是一款桌面应用，交互局限在 App 窗口内。Hermes 假设你是一个团队中的一员，需要异步、多平台的信息流动。

### 场景四：定时任务 → 两者都有，但交付模型完全不同

Codex App 和 Hermes 都支持定时任务，但设计哲学截然不同：

**Codex Automations**（[文档](https://developers.openai.com/codex/app/automations)）：
- 在本地机器上运行，要求 Codex App 保持开启、机器不关机
- 结果发送到 App 内的 **Inbox**，无变更时自动归档
- 项目级：每个 automation 绑定到特定项目，Git 项目支持 Worktree 隔离
- 可与 Skills 结合完成复杂任务
- 适合：个人开发者在自己机器上的周期性编码任务

**Hermes Cron**（[文档](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron)）：
- 在 gateway 服务器上运行（可以是一台 $5/月的 VPS），7×24 常驻
- 结果推送到 **任意消息平台**（Telegram、Discord、Slack）或本地文件
- 支持 **script-only 模式**（`no_agent=True`）：Python 脚本做机械检测，只在有变更时唤醒 Agent → 零 token 静默运行
- 支持 **job 间链式依赖**（`context_from`）：job A 采集数据 → job B 分析处理
- 不绑定项目，可执行任意系统级任务（服务器监控、价格追踪、竞品动态）
- 适合：团队共享的常驻自动化，或需要跨平台通知的场景

关键差异不是"有没有"，而是**"能不能在你不开机的时候跑"**和**"结果发到哪里"**。

### 场景五：模型自由和隐私需求 → Hermes 是唯一选择

如果你的组织对数据隐私有严格要求，不能把代码发送到 OpenAI 的 API；或者你希望使用特定的开源模型来降低成本——Codex 完全无法满足。

Hermes 支持本地模型（llama.cpp、vLLM、Ollama），所有推理都在本地完成，代码永不离开你的机器。同时，你可以为不同类型的任务使用不同的模型：
- 编码用 DeepSeek（成本低、代码能力强）
- 创意写作用 Claude（语言质量高）
- 敏感项目用本地 Llama（数据不出境）

**Codex 绑死了 OpenAI。** 无论你的需求如何变化，你只能使用 OpenAI 的模型。

### 场景六：非编码的日常任务 → Hermes 的工具生态更丰富

Codex 的工具集是为编码设计的。Hermes 的工具集覆盖了更广泛的生活和工作场景：

- **想听音乐？** → `在 Spotify 上播放 Lo-fi 歌单`
- **需要生成封面图？** → `用 ComfyUI 生成一张赛博朋克风格的封面`
- **要管理日历？** → `帮我在下周三下午 3 点安排一个会议`
- **想控制智能家居？** → `把客厅的灯调成暖色`
- **要做笔记？** → `把这个 idea 存到 Obsidian`
- **要 OCR 文档？** → `提取这个 PDF 里的所有表格`

这些场景和"写代码"没有关系，但它们构成了一个现代知识工作者的真实日常。Hermes 让你不需要在 10 个不同的工具之间切换——一个 Agent 解决所有。

## 三、Hermes 复杂使用案例

以下案例均来自 Hermes Agent 官方文档中的实战教程（见 [`hermes-agent/website/docs/guides/`](https://github.com/NousResearch/hermes-agent/tree/main/website/docs/guides)），每个案例都有完整的配置步骤和可运行代码。

### 案例一：每日简报机器人（Daily Briefing Bot）

来自官方教程 [Tutorial: Daily Briefing Bot](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)。这是一个完全自动化的新闻摘要系统：

```
流程：
1. 每天 8:00 AM — Cron 调度器触发任务
2. Hermes 启动全新 Agent 会话，加载预设 prompt
3. Web Search（Firecrawl）拉取 AI / 开源 LLM 相关最新新闻
4. Agent 提炼并格式化为简报（含来源链接）
5. 自动推送到 Telegram 或 Discord
```

**这个案例展示的能力链条：**
- **Cron** → 定时自主触发，无需人工干预
- **Web Search** → 接入实时信息
- **NL Summarization** → 将原始信息提炼为结构化简报
- **Messaging Delivery** → 推送到你日常使用的通讯平台
- **零代码配置** → 全程通过对话式 prompt 完成，不写一行代码

官方教程还提供了不使用消息平台的方案（`deliver: "local"`，简报保存到 `~/.hermes/cron/output/`），以及如何先手动测试工作流再自动化。

### 案例二：GitHub PR 自动审查 Agent

来自官方教程 [Tutorial: GitHub PR Review Agent](https://hermes-agent.nousresearch.com/docs/guides/github-pr-review-agent) 和 [Webhook 版本](https://hermes-agent.nousresearch.com/docs/guides/webhook-github-pr-review)。

两种模式都支持：

**Cron 轮询模式**（适合无公网 IP 的环境）：
```
每 2 小时 → gh pr list → 检出新增 PR → 获取 diff → Agent 审查 → 推送审查结果到 Discord/Telegram
```

**Webhook 实时模式**（需要公网端点）：
```
GitHub PR 事件 → Webhook POST → Hermes 接收 → Agent 获取 diff → 审查 → 直接评论到 PR 线程
```

**这个案例的关键价值：**
- **Cron 模式**可以在 NAT/防火墙后的机器上工作，不需要公网 IP
- **Webhook 模式**是实时的，PR 一开就能收到审查
- 审查结果可以直接评论到 PR 页面（Webhook 模式）或推送到聊天频道（两种模式都支持）
- 官方文档明确警告了 webhook 的 prompt injection 风险并给出了沙箱化建议——这是一个真正可上生产的设计

### 案例三：团队 Telegram 助手

来自官方教程 [Tutorial: Team Telegram Assistant](https://hermes-agent.nousresearch.com/docs/guides/team-telegram-assistant)。

这不是一个人的工具，而是整个团队共享的 AI 助手：

- **多用户会话隔离** — 每个团队成员有自己的对话上下文，互不干扰
- **权限控制** — 只允许白名单用户交互，防止未授权访问
- **全工具访问** — Terminal、文件编辑、Web Search、代码执行，跑在服务器上
- **定时团队任务** — 每日站会提醒、健康检查、共享日报推送到团队频道

官方教程从零开始：创建 BotFather 机器人 → 配置 Hermes gateway → 设置用户授权 → 测试运行。全部步骤清晰可操作。

### 案例四：网站变更监控

来自官方教程 [Automate Anything with Cron](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron) 的 Pattern 1。

利用 Hermes Cron 的 `script` 参数实现零 token 浪费的变更监控：

```
Python 脚本（change-detection）→ 仅在有变更时输出 diff → Agent 收到 diff 后判断是否值得通知 → 推送
```

**设计精妙之处：**
- Python 脚本负责机械工作（fetch + hash + diff），**不消耗 token**
- Agent 只在脚本检测到变更时才介入，做语义判断（"这个改动用通知用户吗？"）
- 脚本无变更时输出为空 → Agent 不运行 → 零成本静默

这个模式可以适配到任何"检测-判断-通知"场景：价格监控、竞品动态、安全公告、API 文档变更。

### 案例五：Nous Portal 统一工具订阅

[Nous Portal](https://portal.nousresearch.com) 是 Hermes 生态的关键组件。它解决了一个现实痛点：**工具 API Key 碎片化**。

如果要让 Agent 同时使用搜索、图片生成、TTS 和云端浏览器，传统上需要：
- Firecrawl（搜索）— 单独注册付费
- FAL / ComfyUI Cloud（图片生成）— 单独注册付费
- OpenAI / ElevenLabs（TTS）— 单独注册付费
- Browser Use（云端浏览器）— 单独注册付费

Nous Portal 用一个订阅统一覆盖所有这些后端。一条命令完成全部配置：

```bash
hermes setup --portal
```

Codex 没有这个维度的对应物——它的工具边界由 OpenAI 定义，工具网关的控制权不在你手里。

## 四、你是 Codex 用户还是 Hermes 用户？

这个问题的答案取决于你的需求图景：

```
你是 Codex App 用户，如果：
  ✓ 你的主要场景是在桌面端写代码
  ✓ 你需要最好的一手编码体验 + Computer Use
  ✓ 你已经深度使用 OpenAI/ChatGPT 生态
  ✓ 你的定时任务可以接受"本机开机+App运行"的前提
  ✓ 你不需要跨会话记忆或多平台消息

你是 Hermes 用户，如果：
  ✓ 你需要跨会话的持久记忆和技能积累
  ✓ 你需要多平台（Discord/Telegram/Slack 等）交互
  ✓ 你的定时任务需要 7×24 常驻（VPS 上跑，不依赖本机）
  ✓ 你需要定时任务结果推送到消息平台而非 App 内 Inbox
  ✓ 你需要模型自由（不同任务用不同模型）
  ✓ 你需要非编码工具（Spotify、日历、智能家居等）
  ✓ 你对数据隐私有要求（需要本地模型）
  ✓ 你希望一个随时间越来越懂你的 Agent
```

**最佳实践：两者并不是互斥的。**

很多开发者同时使用两者：
- **Codex App** 用于桌面端的高强度编码会话
- **Hermes** 作为"常驻 Agent"，管理知识、自动化任务、跨平台协作

这不是一个零和博弈。Codex App 和 Hermes 在各自的架构哲学下做到极致，聪明的用户会在合适的场景使用合适的工具。

## 五、结语

Codex App 和 Hermes 的差异不是功能数量之争，而是架构哲学之争。

- Codex App 选择了 **深度**：在编码这个垂直场景里，把体验打磨到极致（Automations、Worktrees、Computer Use、Review）。代价是生态封闭、限于桌面端。
- Hermes 选择了 **广度**：在多场景、多平台、多模型的图景里，构建一个自进化的 Agent 系统。代价是单点编码深度不如 Codex。

两个项目都还在快速演进。Codex App 在 OpenAI 的资源支持下，功能迭代速度惊人。Hermes 作为开源社区驱动的项目，凭借插件生态和社区 Skill Hub，走的是另一条"群体智慧"的路线。

最终，**Codex App 让你写更好的代码，Hermes 让你成为一个更高效的工程师。**

---

*本文架构图使用 dark-themed SVG 风格绘制，源码可在 [GitHub](https://github.com/zcxGGmu/zcxggmu.github.io) 查看。*
