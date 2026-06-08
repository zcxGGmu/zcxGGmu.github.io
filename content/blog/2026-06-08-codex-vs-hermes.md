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

Codex CLI 发布后，一个很自然的质疑是：当 OpenAI 已经做出了一个可以在终端里自主编码、读文件、跑命令、甚至调用子 Agent 的工具，为什么还需要另一个 Agent 框架？

简单回答：**Codex 解决的是"怎么让 AI 帮你写代码"，Hermes 解决的是"怎么让 AI 成为一个持续的工程伙伴"。**

这句话隐藏着两类 Agent 在架构哲学上的根本分歧。下面我们从架构图出发，逐步展开。

## 一、系统架构对比

### Codex CLI：Cloud-model, Local-execution

![Codex 架构图](/images/posts/codex-vs-hermes/codex-architecture.png)

Codex 的架构可以用一句话概括：**本地 Agent Loop + 远程 OpenAI 模型**。它的运行时运行在你的机器上，负责读取配置、加载 AGENTS.md、管理工具调度（Shell、文件系统、Git、MCP），但每一次推理都通过 HTTPS 打到 OpenAI 的 API 上。

这个设计的核心特征：

1. **单一模型供应商** — 你必须使用 OpenAI 的模型（GPT-4o、o4-mini 等），通过 ChatGPT 订阅或 API Key 接入。没有切换模型的自由。
2. **会话级状态** — Codex 的一次对话是自包含的。关闭终端，状态就消失了。没有跨会话的持久记忆，没有"上次我们聊到哪了"的机制。
3. **工具围绕代码展开** — Shell、文件编辑、Git、沙箱执行、MCP 集成。所有工具都是为了更好地写代码。
4. **Subagent 是横向扩展** — Codex 支持子 Agent 并行执行任务，但子 Agent 共享同一个模型和同一套工具集。

这不是缺点，而是**刻意的设计选择**：Codex 的定位非常清晰——它就是 OpenAI 生态里的编码 Agent。它不试图成为一个通用 Agent 框架，也不试图跨出 OpenAI 的边界。

### Hermes Agent：Multi-provider, Multi-platform, Self-improving

![Hermes 架构图](/images/posts/codex-vs-hermes/hermes-architecture.png)

Hermes 的架构在多个维度上做出了截然不同的选择：

1. **多入口点** — CLI (`hermes`)、消息网关（Discord / Telegram / Slack / Signal / WhatsApp / Matrix / Email / WeChat）、ACP 适配器、Cron 调度器、API Server、Python 库。你用同一个 Agent 内核，可以在终端里交互，也可以在群聊里被 @ 唤起，也可以被定时任务自动触发。

2. **多模型供应商** — OpenAI、Anthropic、DeepSeek、Google、xAI、Groq、Mistral、OpenRouter、Nous Portal，以及本地的 llama.cpp / vLLM / Ollama。你可以热切换模型：`/model deepseek:deepseek-v4-pro`。

3. **跨会话持久化** — Memory DB（SQLite + FTS5 全文搜索）让 Hermes 记住你是谁、你的偏好、你的项目结构。Session Search 可以检索历史对话。"上次我们聊到哪了"是一个真实的系统能力，而不是一句 prompt。

4. **自进化的技能系统** — Hermes 会在执行复杂任务后，自动把成功的模式抽象为"技能"（Skill）。这些技能不是静态的 prompt 模板，而是存有完整执行逻辑和陷阱说明的过程性知识。下次遇到类似任务，技能就会被自动加载。

5. **工具生态远超编码** — 40+ 内置工具覆盖 Terminal、File System、Browser、Code Execution、Image Generation (ComfyUI)、TTS、Spotify、GitHub、Notion、Linear、Airtable、Email、Calendar、YouTube、Maps、Home Assistant、Kanban、Obsidian、OCR……它不只是一个编码助手，而是一个生活+工作操作系统里的 Agent。

6. **Cron 调度器** — 这是 Codex 完全不具有的能力。你可以让 Hermes 每天早晨 9 点抓取新闻简报，或者在代码仓库有新 PR 时自动审查。

### 核心哲学差异

| 维度 | Codex CLI | Hermes Agent |
|------|-----------|-------------|
| **模型自由度** | 仅 OpenAI | 20+ 供应商，可本地部署 |
| **入口点** | 终端 / IDE / Web | 终端 + 消息平台 + Cron + API |
| **持久化** | 会话内 | 跨会话 Memory + FTS5 检索 |
| **技能系统** | 静态 Skills | 自进化的过程性技能 |
| **工具范围** | 编码工具 | 生活+工作全栈工具 |
| **自动化** | 无定时任务 | 内置 Cron 调度器 |
| **生态系统** | OpenAI 封闭生态 | 开源 MIT + 社区 Skill Hub |

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

Codex 只能在终端里交互（或者它的 Web/IDE 版本）。但现实中，很多工程讨论发生在群聊里。

Hermes 的 Messaging Gateway 让它可以在 Discord、Telegram、Slack 等平台上被团队成员 @ 唤起。你可以：

- 在 Discord 群里 @Hermes "review 一下这个 PR"
- 在 Telegram 里让它查一下今天的 CI 状态
- 在 Slack 里让它创建 Linear issue

同时，因为 Memory 是跨平台的，你在 Telegram 上交代过的偏好，在 Discord 会话中也会被记住。

**Codex 没有这个维度。** 它假设你是一个人坐在电脑前对着终端。Hermes 假设你是一个团队中的一员，需要异步、多平台的信息流动。

### 场景四：定时自主任务 → 只有 Hermes 能做

这是最直观的"为什么需要 Hermes"的场景。

Codex 是**被动响应**的：你发指令，它执行。Hermes 的 Cron 调度器让它可以是**主动触发**的：

```yaml
# 每天早上 9:00，抓取 AI 领域新闻并推送到 Discord 频道
cron 0 9 * * * → 搜索 arXiv 最新 AI 论文 + 抓取 Hacker News 头条 + 推送到 #ai-news

# 每 2 小时检查一次 GitHub PR，有新 PR 时自动做初筛 review
cron every 2h → 检查 repo PRs → 对新的 PR 做 diff 分析 → 推送到 #code-review

# 监控服务器状态
cron every 30m → SSH 到服务器 → 检查 CPU/内存/磁盘 → 异常时告警
```

这些定时任务不需要人守着终端。你定义好规则，Hermes 按时执行并推送到指定平台。这是一个**Agent 从"听从指令"升级到"自主管理"**的关键跃迁。

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

以下案例来自 Hermes 官方文档、GitHub 仓库和社区实践，展示了 Hermes 在"非简单问答"场景中的真实能力。

### 案例一：自动化科研流水线（Claw AI Lab）

来自 [Claw AI Lab](https://github.com/NousResearch/hermes-agent) 社区的实践：利用 Hermes 的 Cron + Skills + Subagents 构建了一个自动化科研流水线。

```
流程：
1. Cron 每天触发 → 搜索 arXiv 最新论文
2. Skills (arxiv-search) → 提取论文摘要和关键结论
3. Subagent → 对每篇论文做深度分析（方法、创新点、局限性）
4. Skills (obsidian) → 将分析结果结构化存入 Obsidian 知识库
5. Discord → 推送每日简报到研究频道
```

这不是一个 prompt 能做到的。它需要：
- **Cron** 提供定时触发
- **Skills** 提供可复用的搜索和分析流程
- **Subagents** 提供并行处理能力
- **Memory** 提供跨天的知识积累（避免重复分析同一篇论文）
- **Messaging** 提供推送交付

### 案例二：多 Agent 协作的代码审查系统

利用 Hermes 的 Subagent Delegation 实现了一个分层代码审查系统：

```
主 Agent（Orchestrator）
├── Subagent 1: Security Reviewer → 检查安全漏洞
├── Subagent 2: Performance Reviewer → 检查性能问题
└── Subagent 3: Style Reviewer → 检查代码风格
     ↓
  各 Subagent 返回审查结果
     ↓
  主 Agent 汇总 → 生成统一 Review Report → 推送到 Discord
```

这是 [Subagent-driven Development](https://hermes-agent.nousresearch.com/docs) 技能的实战应用。每个 Subagent 可以使用不同的模型（Security Reviewer 用最强的模型，Style Reviewer 用便宜的模型），在成本和质量之间取得平衡。

### 案例三：跨平台个人助理

一个用户的真实配置：

- **Discord**：日常交互的主界面，随时 @ 唤起
- **Telegram**：接收 Cron 推送（每日新闻、CI 告警）
- **Cron**：
  - 每早 8:00 推送天气预报
  - 每早 9:00 推送 AI/技术简报
  - 每 30 分钟检查 GitHub CI 状态
  - 每晚 22:00 推送明日日历摘要
- **Skills**：积累了 30+ 个技能（代码审查、论文分析、翻译、会议总结）
- **Memory**：记录了用户的编程偏好、项目结构、常用工具链

这本质上是一个**个人 AI 操作系统**，而不是一个编码工具。

### 案例四：Nous Portal 统一工具订阅

[Nous Portal](https://portal.nousresearch.com) 是 Hermes 生态中的另一个关键组件。它解决了 Agent 使用中一个实际问题：**工具 API Key 碎片化**。

通常，如果你想让 Agent 同时使用搜索、图片生成、TTS 和云端浏览器，你需要分别注册和付费：
- Firecrawl（搜索）
- FAL / ComfyUI Cloud（图片生成）
- OpenAI / ElevenLabs（TTS）
- Browser Use（云端浏览器）

Nous Portal 用一个订阅覆盖了所有这些后端。对 Hermes 用户来说，一条命令完成配置：

```bash
hermes setup --portal
```

这背后反映的是 Hermes 的生态哲学：不仅 Agent 本身是开放的，工具网关也是统一的。Codex 在这个维度上没有对应物——它的"工具"就是 Shell、文件系统和 MCP 插件。

## 四、你是 Codex 用户还是 Hermes 用户？

这个问题的答案取决于你的需求图景：

```
你是 Codex 用户，如果：
  ✓ 你的主要场景是在终端里写代码
  ✓ 你需要最好的一手编码体验
  ✓ 你已经深度使用 OpenAI/ChatGPT 生态
  ✓ 你不需要跨会话记忆或定时任务

你是 Hermes 用户，如果：
  ✓ 你需要跨会话的持久记忆和技能积累
  ✓ 你需要多平台（Discord/Telegram/Slack 等）交互
  ✓ 你需要定时自主任务（Cron）
  ✓ 你需要模型自由（不同任务用不同模型）
  ✓ 你需要非编码工具（Spotify、日历、智能家居等）
  ✓ 你对数据隐私有要求（需要本地模型）
  ✓ 你希望一个随时间越来越懂你的 Agent
```

**最佳实践：两者并不是互斥的。**

很多开发者同时使用两者：
- **Codex** 用于终端里的高强度编码会话
- **Hermes** 作为"操作系统级 Agent"，管理知识、自动化任务、跨平台协作

这不是一个零和博弈。Codex 和 Hermes 在各自的架构哲学下做到极致，而聪明的用户会选择在合适的场景使用合适的工具。

## 五、结语

Codex 和 Hermes 的差异不是功能数量之争，而是架构哲学之争。

- Codex 选择了 **深度**：在编码这个垂直场景里，把体验打磨到极致。代价是生态封闭、场景单一。
- Hermes 选择了 **广度**：在多场景、多平台、多模型的图景里，构建一个自进化的 Agent 系统。代价是单点深度不如 Codex。

两个项目都还在快速演进。Codex 在 OpenAI 的资源支持下，功能迭代速度惊人。Hermes 作为开源社区驱动的项目，凭借插件生态和社区 Skill Hub，走的是另一条"群体智慧"的路线。

最终，**Codex 让你写更好的代码，Hermes 让你成为更好的工程师。**

---

*本文架构图使用 dark-themed SVG 风格绘制，源码可在 [GitHub](https://github.com/zcxGGmu/zcxggmu.github.io) 查看。*
