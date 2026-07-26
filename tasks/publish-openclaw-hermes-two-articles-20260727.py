# -*- coding: utf-8 -*-
from __future__ import annotations

import importlib.util
import json
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path("/tmp/hermes-video-publish-20260721-triple")
BASE_PATH = ROOT / "tasks" / "publish-physical-ai-three-article-batch.py"
SCRIPT_NAME = "publish-openclaw-hermes-two-articles-20260727.py"
MANIFEST_NAME = "publish-openclaw-hermes-two-articles-20260727-changed-files.json"

spec = importlib.util.spec_from_file_location("base_publisher", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)

SLUG_GATEWAY = "openclaw-hermes-architecture-gateway-self-improving-agent"
TITLE_GATEWAY = "OpenClaw 与 Hermes 的架构分野：跨平台网关，还是自我进化 Agent"

SLUG_SELECTION = "hermes-openclaw-selection-skills-subagents-memory-production"
TITLE_SELECTION = "Hermes 与 OpenClaw 选型实战：Skill、Sub Agent、Memory 与长期落地"

BODY_GATEWAY = f"""
<p><img src="/images/posts/{SLUG_GATEWAY}/cover.svg" alt="{TITLE_GATEWAY}"></p>
<p>OpenClaw 和 Hermes 经常被放在一起比较，因为它们都属于开源 AI Agent 工具，许可证也都足够宽松，名字看起来像同类竞品。但真正拆开架构之后会发现，二者并不是同一个方向的产品。</p>
<p>OpenClaw 更像一个跨平台个人 AI 助手网关。它的重点不是让某一个 Agent 自己变聪明，而是把 Agent 接到日常使用的各种消息入口、运行时、工具和渠道里，让用户在 Telegram、Slack、微信、iMessage、Discord、网页面板、移动端伴侣应用等场景中都能调起同一套智能能力。</p>
<p>Hermes 更像一个自我改进的 AI Agent。它强调的是在使用过程中持续学习，自动创建和管理 Skill，逐渐加深对用户和任务习惯的理解，并把长期会话、记忆、外部 memory provider、IDE 集成和 OpenAI 兼容 API 组织成一个持续成长的系统。</p>
<p>所以，两者的根本差异不是技术栈，也不是谁的界面更好看，而是设计哲学完全不同：OpenClaw 向外铺，把 Agent 接到更多渠道；Hermes 向内生长，让 Agent 越用越贴近个人工作流。</p>

<h2 id="positioning">定位差异：网关系统与自我成长系统</h2>
<p>OpenClaw 的核心定位，是“自己的个人 AI 助手，接入任何平台”。这个定位决定了它首先关注入口、渠道、运行时调度和认证统一。它不是把所有能力都塞进一个单体 Agent，而是把 Agent 作为可以被调度、被接入、被替换的执行单元。</p>
<p>Hermes 的核心定位，是“自我改进的 AI Agent”。这个定位决定了它更重视长期使用过程中的成长性：自动学习、自动生成 Skill、自动整理记忆、自动加深用户理解。它不是优先解决“接入多少渠道”，而是优先解决“系统能不能越用越懂”。</p>
<p>这两个定位都会影响后续所有架构选择。OpenClaw 的问题意识是：如何让不同模型、不同运行时、不同消息入口、不同插件格式都能被统一调度。Hermes 的问题意识是：如何让一个 Agent 在长期任务、上下文、记忆和 Skill 中持续演化。</p>
<p>因此，评价 OpenClaw 时，要看它的网关能力、运行时编排、渠道覆盖、配置透明度和权限边界；评价 Hermes 时，要看它的学习机制、Skill 生命周期、长期记忆质量、IDE 工作流和自我维护能力。用同一套标准比较，反而会误判。</p>

<h2 id="runtime">运行时架构：多运行时调度与单原生循环</h2>
<p>OpenClaw 把运行时当成一等公民。它内置多个 runtime，可以接自己的 Pi，可以接 Codex，可以接 Claude CLI，也可以通过 ACP 协议接外部 Agent。每个模型都可以通过配置指定走哪个 runtime：OpenAI 模型可以交给 Codex CLI 的 AppServer，Anthropic 模型可以交给 Claude CLI，外部 Agent 也可以通过协议接入。</p>
<p>这种架构像一个窗口管理器或调度器。OpenClaw 自己不是必须亲自跑完所有 Agent Loop，而是负责把不同任务分发给不同运行时，让每个运行时在自己擅长的边界内工作。它的失败模式也更偏工程化：如果明确指定了某个 runtime，但系统找不到，就直接报错，而不是偷偷回退到另一个路径。</p>
<p>Hermes 则主要依赖自己的原生 SyncAgent Loop 来跑所有模型。Codex AppServer 是一个后加的可选 runtime，通过命令开关启用。打开之后，OpenAI 模型的相关回合可以委托给 Codex 运行；关闭之后，Hermes 仍然依靠自己的原生循环完成任务。</p>
<p>如果用一个比喻来理解，OpenClaw 像是一个多进程调度系统，核心能力是把不同 Agent runtime 纳入统一编排；Hermes 更像一个自带 Agent 能力的工作台，再通过扩展方式接入 Codex 这样的外部 runtime。一个是“调度多个独立执行器”，一个是“自己能跑，外部执行器是增强项”。</p>

<h2 id="memory">记忆系统：可见文件与多层检索</h2>
<p>OpenClaw 的记忆系统非常克制。长期记忆主要放在 `memory.md`，每日工作记忆按日期放在 markdown 文件里。它的原则很直接：模型只记得被保存到磁盘上的东西，没有隐藏状态。用户可以直接打开、阅读、修改和审计这些文件。</p>
<p>这种设计的优点是透明。记忆在哪里、内容是什么、什么时候写入、是否应该保留，都可以被人检查。缺点是自动化程度没有那么强，需要用户愿意理解并维护文件结构。</p>
<p>Hermes 的记忆系统更复杂。基础层有 `memory.md` 和 `user.md`，外层还套了 SQLite 与 FTS 全文检索的 Session 数据库，并且可以接入多个外部 memory provider，例如 Mem0、Langfuse、Supermemory、LangSmith 等。每个 provider 都会带来自己的工具与外部存储能力。</p>
<p>这种设计的优点是能力上限更高，可以做更复杂的检索、外部记忆和长期上下文管理。风险则在于系统复杂度明显提高：外部 provider 的同步、重复、冲突、失效和权限问题，都会进入整体记忆链路。</p>

<h2 id="promotion">记忆提升哲学：人工审核与自动策展</h2>
<p>两者真正有意思的差异，不在“有没有记忆”，而在“观察如何升级为长期记忆”。OpenClaw 使用类似候选清单的方式：后台 sweep 会把日常观察整理成草稿，写入类似 `dreams.md` 的候选区域，但不会自动升级到长期记忆。是否进入 `memory.md`，由用户审核决定。</p>
<p>这是一种 human in the loop 的哲学。OpenClaw 不替用户判断所有经验是否重要，只把候选信息摆出来，让用户决定哪些应该进入长期记忆。它牺牲了一部分自动化，换来更高的可控性和更少的污染风险。</p>
<p>Hermes 的 curator release 走的是相反方向。后台 curator 会给 Agent 自己的 Skill 打分、精简、归档，尽量做到零用户参与。它更相信系统可以自动判断哪些 Skill 值得保留，哪些应该被淘汰。</p>
<p>这正好对应二者的底层路线：OpenClaw 让用户把关，减少黑箱；Hermes 替用户整理，减少维护负担。前者更稳、更透明，后者更自动、更省心，但也更依赖自动判断的质量。</p>

<h2 id="auth">认证机制：集中 token sync 与委托登录态</h2>
<p>认证机制也体现了两种工程哲学。OpenClaw 把所有认证集中放在 auth profiles 的 JSON 文件里，官方把这种方式称为 token sync。一个配置文件里可以同时放 ChatGPT 账号的 auth token、OpenAI API key、Anthropic key，以及复用 Claude CLI 本地 auth 的信息，再分发给各个 runtime 使用。</p>
<p>集中管理的好处是方便统一审计、统一备份、统一配置，也更适合网关系统的定位。所有入口、模型和 runtime 都围绕同一套认证配置运行。问题是安全责任也更集中：一旦这个文件管理不当，影响面会比较大。</p>
<p>Hermes 走的是委托路线。Hermes 自己用 `hermes auth login` 管基础认证；如果启用 Codex runtime，Codex 相关认证就交给 Codex CLI 自己的 `auth.json`，绕过 Hermes。这样做减少了 Hermes 自己持有外部工具密钥的范围，也复用了外部 CLI 已有的认证机制。</p>
<p>委托认证的代价是维护更分散。用户需要分别理解 Hermes、Codex、其他 provider 的登录状态和过期机制。集中管理更像一个平台，委托管理更像多个工具协作，各自有边界。</p>

<h2 id="plugins">插件生态：Claw Hub 与 Python entrypoints</h2>
<p>OpenClaw 的插件生态围绕官方注册中心 Claw Hub 展开，artifact 类型包括 skills、code plugins、bundle plugins，以及角色包形式的 source。除了 Claw Hub，它还支持安装 npm 包、Git 仓库和本地 link。更关键的是，它兼容 Codex、Claude、Cursor 等客户端的 bundle 格式，一份插件可以被多套客户端复用。</p>
<p>这说明 OpenClaw 更关心“生态接入”和“跨客户端复用”。它要解决的不是一个工具内部的插件问题，而是不同 Agent 客户端、不同插件格式、不同工具生态如何被统一纳入。</p>
<p>Hermes 则使用 Python entrypoints 发现机制，插件大类包括 general、memory、context、model providers。Skill 层面，它对齐 agentskills.io 这样的开放标准，不强行绑定自家格式。它还提供 `skill_manage` 一类工具，让 Agent 自己创建、修改、删除 Skill。</p>
<p>这与 Hermes 的 self-improving 定位是配套的。OpenClaw 强在“外部生态整合”，Hermes 强在“内部 Skill 自我演化”。前者适合希望插件跨工具流动的用户，后者适合希望 Agent 在长期使用中主动维护能力的用户。</p>

<h2 id="channels">渠道覆盖：横向更广与纵向更深</h2>
<p>渠道分布上，OpenClaw 的优势非常明显。它覆盖大量 messaging 平台，从 Discord、Telegram、Slack 这样的主流渠道，到微信、飞书等国内协作渠道，再到 iMessage、电话接入、WebChat、Control UI、macOS、iOS、Android 三端伴侣应用。它的目标是让 Agent 成为一个真正跨平台的个人助手入口。</p>
<p>Hermes 的 messaging 覆盖相对少一些，但它在开发者工作流上更深。它有 ACP 协议接入，可以把 Agent 接入 VS Code、Zed、JetBrains 等 IDE，也提供 OpenAI 兼容 API server，方便把 Hermes 作为后端能力嵌入其他工具。</p>
<p>一句话概括：OpenClaw 横向铺得更广，Hermes 纵向接得更深。前者更像“到处都能叫得动的助手网关”，后者更像“深入开发工作流的自进化 Agent”。</p>
<p>这也解释了为什么两者并不互相替代。如果需求是消息入口、移动端、跨平台触达、统一 runtime 调度，OpenClaw 更顺手；如果需求是 IDE、长期学习、Skill 自我管理、OpenAI 兼容服务，Hermes 更有吸引力。</p>

<h2 id="selection">选型：主入口最好只选一个</h2>
<p>OpenClaw 更适合需要广泛接入各种 messaging 平台、希望使用 ChatGPT 或 Claude 账号认证、重视本地透明可控、愿意手动维护配置文件的用户。它的优势在清晰、可控、横向覆盖和运行时调度。</p>
<p>Hermes 更适合希望 Agent 长时间运行、能够自动学习、有 IDE 集成、自动管理 Skill 池、不断贴近个人习惯的用户。它的优势在自我改进、长期上下文、开发者工作流和自动整理。</p>
<p>两者可以同时安装，也可以对比使用，但主入口最好只挑一个。因为 Session 数据库、记忆系统、Skill 系统和用户习惯都会各自管理。如果两个系统混着承担同一类核心任务，很容易出现上下文割裂、记忆不一致、Skill 分散、排障困难的问题。</p>
<p>更合理的方式是明确边界：OpenClaw 做消息入口和 runtime 网关，Hermes 做专项开发工作流或长期自学习任务；或者反过来，让 Hermes 做个人主工作台，OpenClaw 只承担跨平台触达。关键不是谁更强，而是边界要清楚。</p>

<h2 id="conclusion">结论：一个向外连接，一个向内成长</h2>
<p>OpenClaw 与 Hermes 的本质差异，可以压缩成一句话：OpenClaw 向外连接，Hermes 向内成长。</p>
<p>OpenClaw 的价值在于把 Agent 接到更多渠道、更多运行时、更多插件生态和更多平台入口里，让智能能力像网关一样被统一调度。它强调可见、可控、可配置、可审计，适合需要清晰工程边界的用户。</p>
<p>Hermes 的价值在于让 Agent 在长期使用中沉淀 Skill、优化记忆、接入 IDE、理解用户习惯，逐步形成自我改进能力。它强调自动化、成长性、长期上下文和开发者工作流，适合愿意接受更高系统复杂度来换取更强自动化的人。</p>
<p>选择时不要只看名称、许可证或热度，而要回到真实需求：需要跨平台入口和透明控制，就优先 OpenClaw；需要自我学习和深度开发工作流，就优先 Hermes。二者都值得研究，但它们解决的是两类完全不同的问题。</p>
"""

BODY_SELECTION = f"""
<p><img src="/images/posts/{SLUG_SELECTION}/cover.svg" alt="{TITLE_SELECTION}"></p>
<p>Hermes 和 OpenClaw 的选型，不能停留在“谁更先进”“谁更智能”“谁宣传得更强”这种层面。真正落地以后，决定体验的往往不是演示效果，而是 Skill 生命周期、Sub Agent 协作机制、Memory 稳定性、权限编排、维护成本和长期可控性。</p>
<p>Hermes 的优势很明显：上手门槛低，对新手友好，前期能承接大量重复性工作，自动创建 Skill、持续学习、记忆增强等概念也很吸引人。但使用时间一长，底层设计的硬伤就会逐渐暴露：Skill 只增不减、profile 隔离不等于真正多 Agent 协同、记忆系统复杂且容易混乱。</p>
<p>OpenClaw 的特点恰好相反。它上手门槛更高，配置和工程概念更多，但底层更偏严谨、可控和长期落地。尤其在多 Agent 协作、任务委托、结果聚合、权限编排、记忆可追溯等方面，它更像一个面向生产场景的 Agent 架构底座。</p>

<h2 id="hermes-strength">Hermes 的优势：低门槛、快上手、适合轻量自动化</h2>
<p>Hermes 最大的吸引力，是用户不需要一开始就设计完整的多 Agent 架构。安装、登录、配置之后，它就能承担大量个人自动化任务。对于只想让 Agent 帮忙整理资料、执行简单流程、生成内容、维护少量 Skill 的用户来说，这种低门槛非常重要。</p>
<p>它的 self-improving 叙事也很符合直觉：用得越多，系统越了解用户；工具调用越多，系统越能总结经验；任务试错越多，系统越能生成和修正 Skill。这个方向本身没有问题，问题在于长期使用时，自动化能力必须配套治理机制。</p>
<p>如果只有创建，没有删除；只有积累，没有冲突检测；只有自动归档，没有使用追踪；只有记忆写入，没有严格去重和更新规则，那么“越用越聪明”很容易变成“越用越乱”。智能系统不是记得越多越好，而是要记得准确、适用、可追溯、可维护。</p>

<h2 id="skill-problem">Skill 系统：贵精不贵多</h2>
<p>Hermes 的 Skill 系统最容易让人兴奋，也最容易形成维护负担。自动创建机制可能由多次工具调用、试错模式、用户纠正有效性等信号触发。短期看，这能让 Agent 很快沉淀经验；长期看，如果没有负反馈、冲突检测和使用追踪，就会造成 Skill 泛滥。</p>
<p>两个 Skill 功能重复，只要名字不同，就可能同时存在。一个旧 Skill 已经过期，如果没有有效淘汰机制，仍然可能影响后续决策。多个 Skill 对同一任务给出不同规则，Agent 就可能在执行时冲突、犹豫或走错路径。最后，用户看到的是系统越来越“有记忆”，但实际体验是越来越难排障。</p>
<p>治理 Skill 的核心原则是：贵精不贵多。自动创建可以保留，但阈值要提高；无关或低频 Skill 要定期清理；功能模块要分类；高优先级 Skill 要明确适用边界；重复 Skill 要合并；冲突 Skill 要删除或重写。</p>
<p>更稳的方式，是把自动创建从默认行为改成受控行为。可以关闭自动创建，或者只在特定项目、特定任务类型里开启；也可以要求所有新 Skill 进入候选区，经过人工审核再进入长期池。没有维护机制的自动创建，最终会从资产变成负债。</p>

<h2 id="subagent-limitation">Profile 隔离不是多 Agent 协作</h2>
<p>Hermes 的 profile 隔离容易被误解为多 Agent 协作。实际上，profile 更接近独立进程隔离：不同 profile 可以有不同配置、不同上下文、不同执行环境，但它们并不天然具备原生子代理调度、消息互通、任务委托和结果聚合能力。</p>
<p>真正的多 Agent 协作，不只是“多个进程同时跑”。它需要主 Agent 拆分任务，需要子 Agent 动态创建，需要不同角色之间传递上下文，需要任务完成后聚合结果，需要失败时重试或回滚，还需要权限边界和资源隔离。</p>
<p>如果 Hermes 要承担复杂多 Agent 架构，就必须额外设计通信方式，例如共享文件、API 调用、消息队列或外部调度器。这样当然可以做，但落地成本会明显增加，很多能力不再是系统原生提供，而是用户自己搭出来的。</p>
<p>因此，Hermes 更适合单角色、轻协作、个人自动化和专项工作流。它可以承担很多任务，但不适合作为复杂多 Agent 团队架构的唯一调度底座。</p>

<h2 id="memory-disorder">Memory 风险：复杂记忆必须有治理</h2>
<p>Hermes 的记忆系统看起来层次丰富，但复杂度也高。长期使用时，记忆问题不只是“加载时机不合理”，还可能来自 `memory.md` 超载、旧信息被重新写入、上下文压缩误入记忆、nudge interval 长期累积，以及外部 memory provider 缺少去重和冲突校验。</p>
<p>当 `memory.md` 内容超过某个实际可承受阈值，模型读取就会变得不稳定。旧信息如果在压缩过程中被重新写入，就会出现新旧信息不同步。外部记忆系统如果没有严格去重，重复信息会被多次召回；如果没有冲突消解，过期规则和新规则会同时影响任务。</p>
<p>记忆混乱最麻烦的地方，是它不像报错那样清晰。用户看到的往往是 Agent 变得奇怪：忽略新要求，重复旧习惯，调用错误 Skill，对同一事实前后不一致，或者在任务中突然引入无关上下文。表面看像模型幻觉，底层可能是记忆污染。</p>
<p>治理记忆的原则与治理 Skill 类似：分层、去重、限长、冲突检测、定期清理。个人偏好、项目规则、临时任务、历史经验不能全部混在一起。越是长期运行的 Agent，越需要把记忆当成数据库来维护，而不是当成无限扩容的笔记本。</p>

<h2 id="openclaw-subagents">OpenClaw 的优势：原生多 Agent 协作</h2>
<p>OpenClaw 从底层就更偏多 Agent 协作。它提供 session spawn 与 ACP spawn 链，支持子代理动态创建、任务委托、结果聚合和权限编排。主 Agent 可以做总管，子 Agent 可以做执行，专门角色可以处理专项任务，职责划分更清楚。</p>
<p>这种设计与 Hermes 的 profile 隔离有本质不同。OpenClaw 的重点不是让多个隔离环境各自运行，而是让多角色在同一套任务结构里协作。任务拆分、执行、回收、聚合和权限控制，是架构的一部分，而不是用户事后自己补上去的外部流程。</p>
<p>对于复杂工作流，这一点非常关键。比如一个长期研究任务，可能需要资料搜集 Agent、代码分析 Agent、写作 Agent、审校 Agent、发布 Agent、验证 Agent。单 Agent 可以做，但上下文会膨胀，职责会混乱；多 Agent 原生协作，可以把任务切成更清晰的角色边界。</p>
<p>OpenClaw 更适合搭建私有 Agent 生态、做多角色分工、跑长期运营任务和支撑复杂团队结构。它不是最省事的选择，但更像可以长期扩展的底座。</p>

<h2 id="openclaw-memory">OpenClaw 的记忆：显式、可追溯、可查证</h2>
<p>OpenClaw 的记忆设计更强调工程化约束。每一条记忆写入都应当显式、可追溯、可查证。会话记忆和全局记忆分层隔离，检索和合并要经过明确规则，外部记忆也不能随意污染主记忆。</p>
<p>这类设计看起来没有自动记忆那么炫，但更适合长期落地。因为真正的长期使用，最怕的不是“系统没有记住”，而是“系统记错了还不知道哪里错了”。可追溯性比自动化更重要。</p>
<p>如果记忆写入有来源、时间、适用范围和冲突规则，排障时就可以定位问题；如果记忆只是自动堆积在多个层里，一旦出错，很难判断到底是哪个 provider、哪次压缩、哪个旧 Skill 或哪段全局记忆造成影响。</p>
<p>稳定不是保守，而是复杂系统的基本要求。Agent 越像生产工具，越不能只追求自动化；必须让关键状态可见、关键决策可查、关键记忆可改。</p>

<h2 id="selection-summary">选型结论：轻量任务用 Hermes，长期架构用 OpenClaw</h2>
<p>Hermes 适合新手、轻度使用、个人简单自动化场景。它上手快，不用一开始就设计复杂架构，能快速解决基础需求。如果主要任务是个人资料整理、简单自动化、少量 Skill 管理、IDE 辅助和轻量工作流，Hermes 足够好用。</p>
<p>但 Hermes 的深层短板也要看清楚：Skill 缺少完整负反馈机制，profile 隔离不等于多 Agent 协作，记忆系统复杂且存在污染风险。这些问题在轻量使用时不明显，进入复杂多 Agent 架构和长期迭代后会被放大。</p>
<p>OpenClaw 更适合想搭建私有 Agent 生态、做多角色分工、长期运行工作流、追求稳定可控的用户。它上手门槛更高，但底层架构更严谨，原生支持多 Agent 协作，记忆和 Skill 系统更偏工程化，更能支撑复杂场景的长期迭代。</p>
<p>简单总结：随便玩玩、轻度使用、快速自动化，选 Hermes；认真搭建多 Agent 架构、做智能体分工、长期落地，优先 OpenClaw。</p>

<h2 id="hybrid-architecture">混合架构：OpenClaw 总管，Hermes 专项执行</h2>
<p>更现实的方案不是非黑即白。复杂 Agent 架构里，单 Agent 统筹所有并不现实，多 Agent 才是核心。可以让 OpenClaw 做全局总管和调度层，负责角色分工、任务委托、权限编排、结果聚合；让 Hermes 承担某些专项任务，例如个人辅助、IDE 深度工作流、轻量自动化和特定 Skill 维护。</p>
<p>这种混合架构的关键，是边界清楚。OpenClaw 不必替代 Hermes 的全部能力，Hermes 也不必承担全局调度。一个做总管，一个做专项执行；一个强调工程化编排，一个强调自我改进和个人工作流。</p>
<p>同时，运维角色必须单独存在。多 Agent 架构不能只关注“能不能完成任务”，还要关注配置是否漂移、记忆是否污染、Skill 是否冲突、进程是否异常、日志是否可查、权限是否越界。没有运维角色，多 Agent 系统越复杂，越容易在无人维护时失控。</p>
<p>后续真正需要打磨的，是跨进程通信、任务分配、上下文传递、结果聚合和权限边界。混合架构不是把两个工具随便装在一起，而是把职责边界设计清楚，让每个系统只做自己最适合的部分。</p>

<h2 id="marketing-gap">警惕过度预期：自动变聪明不是免维护</h2>
<p>Agent 工具最容易被神话的功能，就是自动创建 Skill 和越用越聪明。这个方向本身没有错，但如果宣传把预期拉得太高，用户就会忽略维护成本。真正落地后会发现，看似全自动的系统，往往只是把问题延后了：Skill 多了要整理，记忆多了要清理，配置多了要审计，外部 provider 多了要排障。</p>
<p>Hermes 的问题不是功能错误，而是自动化需要治理。没有治理的自动化，最终会积累技术债。OpenClaw 的吸引力，也不只是功能清单，而是它更强调稳定性、工程化设计和长期可控，不用花哨概念掩盖维护成本。</p>
<p>选型时不要被“智能”“自动”“自我进化”这些词带着走。要问更实际的问题：Skill 怎么删除？冲突怎么检测？记忆怎么追溯？子代理怎么调度？任务失败怎么恢复？权限怎么限制？日志怎么审计？长期维护谁负责？</p>
<p>能回答这些问题的系统，才更适合作为长期生产底座。不能回答这些问题的系统，也许适合轻量使用，但不该直接承担复杂业务。</p>

<h2 id="implementation-checklist">落地检查清单：先问维护问题，再选框架</h2>
<p>真正开始部署之前，可以先列一张检查清单。第一，Skill 是否有创建、审核、合并、删除和优先级规则；第二，记忆是否分成全局、项目、会话和临时信息；第三，子代理是否有明确的创建、委托、回收和结果聚合流程；第四，认证信息是否集中管理或清晰委托；第五，外部插件和 memory provider 出错时是否有降级方案。</p>
<p>如果这些问题都没有答案，系统还不适合作为长期底座。轻量使用可以先跑起来，但一旦进入多角色分工、长期任务、核心业务或高频自动化，就必须把维护机制补齐。否则，早期省下的配置成本，会在后期以排障、冲突、记忆污染和不可复现的形式还回来。</p>
<p>Hermes 的合理使用方式，是限制自动膨胀：少量高质量 Skill、清晰的 memory 边界、定期清理、谨慎开启外部记忆，并把 profile 当成隔离环境，而不是天然协同层。OpenClaw 的合理使用方式，是把它当成调度骨架：先设计角色、权限、任务链和运行时，再逐步扩展渠道与插件。</p>
<p>框架选型不是一次性决定，而是一个持续治理过程。今天适合轻量自动化的工具，未必适合明天的多 Agent 团队；今天看起来复杂的工程化底座，可能会在长期运行中节省大量维护成本。判断标准不应是演示是否惊艳，而是半年后还能不能稳定、可查、可控地运行。</p>

<h2 id="conclusion">结论：真正的 Agent 选型，是维护成本的选择</h2>
<p>Hermes 和 OpenClaw 的差异，不只是功能差异，而是维护哲学差异。Hermes 把很多事情自动化，让用户前期更轻松；OpenClaw 把很多边界工程化，让用户后期更可控。</p>
<p>如果任务轻、周期短、协作少、容错高，Hermes 的低门槛和自动化体验很有价值。它可以快速帮助个人跑起来，承接重复性工作，建立简单自动化流程。</p>
<p>如果任务复杂、周期长、角色多、对稳定性和可追溯要求高，OpenClaw 更适合作为底座。它的价值不在于最省事，而在于更适合长期迭代、多人协作、多 Agent 分工和生产级运行。</p>
<p>最终，真正的 Agent 选型不是选择一个“更聪明”的工具，而是选择一套长期维护成本。短期省事和长期可控，经常不能同时最大化。看清这一点，才不会在框架热度、自动化想象和落地现实之间反复摇摆。</p>
"""


def configure() -> None:
    base.__file__ = __file__
    base.ROOT = ROOT
    base.DATE = "2026-07-27"
    base.BASE_DT = datetime(2026, 7, 27, 1, 50, tzinfo=timezone(timedelta(hours=8)))
    base.PREV_EXISTING_URL = "/2026/deepseek-dao-goodwill-restraint-open-source-agi/"
    base.PREV_EXISTING_TITLE = "DeepSeek 的道：善意、克制、开源与 AGI 主线"
    base.SCRIPT_NAME = SCRIPT_NAME
    base.MANIFEST_NAME = MANIFEST_NAME
    base.CHANGED = set()

    post_gateway = base.Post(
        source_id="BV1865B68EiY",
        slug=SLUG_GATEWAY,
        title=TITLE_GATEWAY,
        desc="OpenClaw 更像跨平台个人 AI 助手网关，Hermes 更像自我改进的 AI Agent。二者在运行时、记忆、认证、插件生态、渠道覆盖和选型边界上完全不同。",
        category="AI工具",
        series="Agent 系统",
        tags=["OpenClaw", "Hermes", "Agent", "AI工具", "运行时", "记忆系统", "插件生态", "跨平台", "ACP", "Skill"],
        minutes=13,
        body=BODY_GATEWAY,
        cover_kicker="架构分野",
        cover_line="跨平台网关 · 自我进化 Agent",
        cover_theme=("#0f172a", "#1d4ed8", "#22c55e"),
        duration=415.7653125,
        segments=189,
        chars=2930,
    )
    post_selection = base.Post(
        source_id="BV18GZFBtEqS",
        slug=SLUG_SELECTION,
        title=TITLE_SELECTION,
        desc="Hermes 上手快但长期维护依赖 Skill、Memory 和 profile 治理；OpenClaw 门槛更高但更适合多 Agent 协作、权限编排和生产级长期落地。",
        category="AI工具",
        series="Agent 系统",
        tags=["OpenClaw", "Hermes", "Agent", "多Agent", "Sub Agent", "Memory", "Skill", "源码分析", "工程化", "选型"],
        minutes=14,
        body=BODY_SELECTION,
        cover_kicker="选型实战",
        cover_line="Skill · Sub Agent · Memory · 长期落地",
        cover_theme=("#111827", "#7c2d12", "#38bdf8"),
        duration=455.296875,
        segments=256,
        chars=2801,
    )
    base.INPUT_ORDER = [post_gateway, post_selection]
    base.PUBLISH_ORDER = [post_gateway, post_selection]
    base.copy_script_and_manifest = copy_script_and_manifest


def copy_script_and_manifest() -> None:
    tasks_dir = ROOT / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve()
    dst = (tasks_dir / SCRIPT_NAME).resolve()
    if src != dst:
        shutil.copyfile(src, dst)
    base.rec(tasks_dir / SCRIPT_NAME)
    manifest_path = tasks_dir / MANIFEST_NAME
    all_changed = sorted(
        base.CHANGED
        | {
            "categories/index.html",
            "series/index.html",
            "tags/index.html",
            f"tasks/{SCRIPT_NAME}",
            f"tasks/{MANIFEST_NAME}",
        }
    )
    manifest_path.write_text(json.dumps(all_changed, ensure_ascii=False, indent=2), encoding="utf-8")
    base.rec(manifest_path)


def extra_validate() -> None:
    forbidden = [
        "B站", "bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主",
        "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅", "投币", "收藏", "下期", "评论区",
        "BV1865B68EiY", "BV18GZFBtEqS", "source_id",
    ]
    required = {
        SLUG_GATEWAY: ["OpenClaw", "Hermes", "运行时", "记忆系统", "认证", "插件生态", "渠道", "跨平台", "自我改进", "Skill"],
        SLUG_SELECTION: ["Hermes", "OpenClaw", "Skill", "Sub Agent", "Memory", "多 Agent", "profile", "记忆", "长期落地", "工程化"],
    }
    failures: list[str] = []
    for post in base.INPUT_ORDER:
        article_path = ROOT / post.url_path.strip("/") / "index.html"
        article = article_path.read_text(encoding="utf-8")
        body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
        body = body_match.group(1) if body_match else article
        plain = re.sub(r"<[^>]+>", "", body)
        if len(plain) < 5200:
            failures.append(f"{post.slug}: body too short {len(plain)}")
        for word in forbidden:
            if word in article:
                failures.append(f"{post.slug}: forbidden wording {word}")
        for word in required[post.slug]:
            if word not in article:
                failures.append(f"{post.slug}: missing required term {word}")
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        toc = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != toc:
            failures.append(f"{post.slug}: toc mismatch")
        ET.fromstring((ROOT / "images/posts" / post.slug / "cover.svg").read_text(encoding="utf-8"))
    manifest_path = ROOT / "tasks" / MANIFEST_NAME
    manifest = set(json.loads(manifest_path.read_text(encoding="utf-8")))
    missing = [p for p in base.CHANGED if p not in manifest]
    if missing:
        failures.append(f"manifest missing changed files: {missing[:10]}")
    if failures:
        raise SystemExit("\n".join(failures))


def main() -> None:
    configure()
    for pycache in ROOT.rglob("__pycache__"):
        shutil.rmtree(pycache)
    base.main()
    extra_validate()


if __name__ == "__main__":
    main()
