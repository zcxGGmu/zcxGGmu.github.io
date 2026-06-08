---
title: "Codex 那么全能，为什么还需要 Hermes？"
date: "2026-06-08T14:30:00+08:00"
updated: "2026-06-08T15:34:00+08:00"
slug: "codex-vs-hermes"
description: "Codex App 是 OpenAI 面向本地/云端编码线程的高强度工作台，Hermes Agent 是 Nous Research 的开源常驻 Agent 系统。两者的关键差异不在功能数量，而在运行边界、自动化入口、消息交付、模型治理和长期记忆。本文修正若干常见误解，并用 GitHub PR 自动审查机器人说明 Hermes 能完成而 Codex App 很难独立完成的复杂场景。"
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

## 四、GitHub 上的复杂案例：PR 自动审查机器人

用户真正应该看的不是“安装 Hermes + 接一个模型”的教程，而是 **Hermes 能不能作为常驻系统接入真实工作流**。

我在 GitHub 上更推荐研究这个案例：

- [GitHub PR Review Agent: webhook 版本](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/github-pr-review-webhook.md)
- [GitHub PR Review Agent: cron 版本](https://github.com/aliaihub/awesome-hermes-usecases/blob/main/usecases/github-pr-review-cron.md)
- [Hermes 官方 webhook 文档源码](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/messaging/webhooks.md)
- [Hermes 官方 cron 文档源码](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/cron.md)

它的核心不是“让 AI 看 diff”，而是把 PR review 做成一个常驻机器人。

### Webhook 模式

```text
GitHub pull_request 事件
  -> Hermes gateway 接收 webhook
  -> 校验 HMAC secret
  -> 把 payload 转成 agent prompt
  -> 加载 pr-review skill
  -> 调用 gh pr diff / gh api 读取上下文
  -> Agent 审查代码
  -> gh pr review 或 GitHub API 评论回 PR
  -> 可选：把摘要发到 Telegram/Discord
```

这个模式适合公网服务器。优点是实时：PR 一创建或更新，机器人就能响应。

### Cron 模式

```text
每 N 分钟触发
  -> 在指定 repo workdir 运行
  -> gh pr list 找 open PR
  -> 过滤已审查/无需审查的 PR
  -> 获取 diff 和项目上下文
  -> Agent 输出 review 或 digest
  -> 发到聊天频道或写回 GitHub
```

这个模式不需要公网 webhook，适合不能暴露端口的环境。缺点是实时性取决于轮询间隔。

### 为什么这个案例 Codex App 很难独立完成？

这里要讲严谨：Codex App 不是完全不能帮你做 PR review。你可以让 Codex 在本地仓库里读 diff、跑测试、写 review；也可以用 Codex Automations 轮询某个项目并输出结果。

难点在“独立、常驻、事件驱动、跨平台交付”：

1. **公网事件入口**：Codex App 本身不是 HTTP webhook server，不能直接承担 GitHub webhook 接收、HMAC 校验、路由分发。
2. **服务生命周期**：PR bot 需要长期在线。Codex 项目级 Automations 依赖本机 App、机器电源和本地项目；Hermes gateway 可以跑在 VPS 上。
3. **事件到 Agent 的路由**：Hermes 把 webhook payload 转 prompt、加载 skill、选择 workdir、调用 CLI/API 作为一套 gateway 流程；Codex App 需要外部 server 或 GitHub Actions 做编排。
4. **多平台 delivery**：Hermes 可以把结果写回 GitHub，同时发到 Telegram/Discord/Slack；Codex App 的一等交付面是 App 内线程/Inbox/通知。
5. **团队共享**：PR bot 是团队服务，不是某个开发者桌面上的一次性 thread。Hermes 的网关、白名单、平台 adapter 更贴近这个形态。

这个案例也有 caveat：`awesome-hermes-usecases` 里的 PR bot 是 runbook，不是一个完整可 `docker compose up` 的成品 repo。另一个 [NousResearch/hermes-agent issue #5563](https://github.com/NousResearch/hermes-agent/issues/5563) 提供了更接近生产的 field report，但它描述的是私有生产流水线，不能当成可复现实验。严谨的结论应该是：**公开材料已经足以证明 Hermes 的架构适合这类工作流，但落地仍需要工程化配置、凭据管理、sandbox 和 prompt-injection 防护。**

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
