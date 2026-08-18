from __future__ import annotations

import importlib.util
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PUB_SCRIPT = TASKS / "publish-video-batch-bv1ut-bv1ee-bv1fx-20260816.py"
ASSET_ROOT = TASKS / "video-single-20260818-bv1jm"

spec = importlib.util.spec_from_file_location("video_publisher_base", PUB_SCRIPT)
pub = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = pub
spec.loader.exec_module(pub)

_run_gh = pub.base.run_gh


def run_gh_with_extra_retry(args: list[str], payload: dict | None = None):
    for attempt in range(6):
        try:
            return _run_gh(args, payload)
        except RuntimeError as exc:
            msg = str(exc).lower()
            retryable = [
                "504",
                "502",
                "503",
                "respond to your request in time",
                "bad gateway",
                "service unavailable",
                "timeout",
                "timed out",
                "connection",
                "reset",
                "temporarily",
                "can't assign requested address",
            ]
            if attempt < 5 and any(token in msg for token in retryable):
                time.sleep(2 + attempt * 3)
                continue
            raise


pub.base.run_gh = run_gh_with_extra_retry
pub.base.__file__ = __file__
pub.base.DATE = "2026-08-18"
pub.base.BASE_DT = datetime(2026, 8, 18, 16, 50, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/shengyi-technology-ai-ccl-citi-target-price-growth-risk/"
pub.base.PREV_EXISTING_TITLE = "生益科技的 AI CCL 重估：花旗 205 元目标价、毛利率新高与扩产风险"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-single-bv1jm-20260818-changed-files.json"
pub.base.PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
    "/2026/original-accumulation-time-autonomy-ordinary-people/",
    "/2026/next-decade-wealth-leap-deflation-rmb-ai-cashflow/",
]


def fig(slug: str, name: str, caption: str) -> str:
    return f'<figure class="post-figure"><img src="/images/posts/{slug}/{name}" alt="{caption}" loading="lazy"><figcaption>{caption}</figcaption></figure>'


SLUG_HERMES = "hermes-agent-memory-background-tasks-model-routing-local-os"


BODY_HERMES = rf'''
<p>Hermes Agent 的真正价值，不在于又多一个聊天窗口，而在于把记忆、工具、任务、模型、文件、邮件、会议、代码环境和本地电脑连接成一个长期运转的私人操作系统。只把它当成普通问答工具，就像买了一辆性能车却只用最低速度挪车，绝大部分能力都被浪费掉了。</p>
<p>更有效的使用方式，是把 Hermes Agent 训练成一个了解自己、能持续工作、能在后台跑任务、能按时间主动行动、能调度不同模型、能访问本地知识和外部工具的智能助理。它越了解个人目标、工作方式、业务上下文和系统连接，输出就越接近真正可执行的建议。</p>

<h2 id="not-chatbot">一、先把定位改掉：它不是聊天框，而是个人操作系统</h2>
<p>很多 AI 助手的使用方式都停留在“问一句、答一句”。这种方式当然有用，但很快会遇到上限：上下文断裂、历史丢失、工具不通、任务被打断、模型能力不匹配、文件和邮件都在系统外面。Hermes Agent 的强处，恰恰是把这些孤岛接起来。</p>
<p>一旦连接建立，它就不再只是回答问题，而是在一个持续存在的上下文里工作。今天讨论过的目标，明天还能继续；会议里出现过的承诺，可以被调出来；本地笔记里的洞察，可以进入当前决策；后台研究不用打断当前对话；早上该看的事项，可以按时送到面前。</p>
<p>这就是从聊天工具到操作系统的差别。聊天工具解决单点问题，操作系统负责协调资源。Hermes Agent 要发挥价值，必须让它拥有足够多的资源入口，也必须给它清晰的使用规则。</p>

<h2 id="memory-system">二、记忆系统是第一层地基</h2>
<p>Hermes Agent 最先要配置好的，是记忆。普通 AI 助手的上下文窗口再大，也不等于真正的长期记忆。真正有用的记忆系统，需要能记录历史对话、人物信息、时间偏好、当前缓存、模糊索引和个人画像，并且在需要时把相关信息调出来。</p>
<p>使用前先确认 Hermes Agent 已经更新到最新版本。记忆相关能力在近期更新后变得更强，如果还停留在旧版本，很多体验会打折。基础记忆通常由一个 <code>Memory.md</code> 之类的 Markdown 文件承载，用来记录已经讨论过的事项、关系和上下文。</p>
<p>更关键的是补齐个人灵魂档案。这个档案可以写成 <code>Soul.md</code> 或类似名称，内容包括：自己是谁、住在哪里、正在做什么业务、有哪些长期目标、喜欢怎样沟通、希望 AI 直接反驳还是温和辅助、哪些习惯不能被忽略、哪些偏好需要长期保留。它相当于一本“个人使用说明书”。</p>
<p>当 Hermes Agent 同时拥有长期记忆、个人档案、人物卡片、时间偏好、模糊索引和短时缓存时，使用成本不会无限膨胀，回答质量却会明显提高。真正的目标不是让它记住所有细枝末节，而是让它在正确时刻调出真正相关的东西。</p>
{fig(SLUG_HERMES, 'hermes-memory-clean.jpg', '记忆系统需要把会话历史、个人档案、模糊索引和短时缓存组合起来，既保留长期背景，又控制上下文成本。')}

<h2 id="local-knowledge">三、本地知识库会把记忆能力抬高一层</h2>
<p>只靠聊天记录还不够。一个人的真实知识往往分散在本地笔记、项目文档、会议纪要、灵感草稿、客户记录和过往研究里。把 Hermes Agent 接入本地 Obsidian 知识库或其他笔记系统，是提升长期价值的关键动作。</p>
<p>连接方式不必复杂。很多时候，只要让 Hermes Agent 知道本地知识库路径，并具备读取和检索权限，它就可以围绕具体问题动态搜索。例如需要做内容策略时，不必重新翻旧笔记，可以直接要求它从过往关于开头、标题、转化、留存的记录中提取最有用的洞察。</p>
<p>这种能力最适合处理“我明明知道以前想过，但现在想不起来”的问题。人脑擅长直觉和判断，但不擅长长期精确检索；本地知识库擅长保存材料，但不会主动在决策时出现。Hermes Agent 连接两者以后，就能在需要时把旧信息重新变成当前行动。</p>

<h2 id="meeting-memory">四、会议记录工具让过去的对话重新可用</h2>
<p>另一个很值得连接的系统，是会议记录。Granola、Fireflies、Fathom 等工具会保存大量真实讨论：客户的问题、合作伙伴的承诺、团队成员的顾虑、用户反馈、业务方向的微小变化。它们如果只躺在单独应用里，价值会很低；一旦可以被 Hermes Agent 查询，就会变成决策资料库。</p>
<p>实际使用时，可以询问上一场会议的标题、自己在会上说过的重点、某个客户曾经提出的疑问、每周社区电话里被反复问到的问题。Hermes Agent 不需要凭记忆猜，而是可以从会议文本里抽取相关内容。</p>
<p>这类连接的价值常常被低估，因为它解决的不是“有没有信息”，而是“信息在需要时能不能被找到”。很多业务机会、产品判断和内容选题，最初都藏在会议里的几句话中。</p>

<h2 id="email-tools">五、邮件和 MCP 连接要开放权限，也要限制权限</h2>
<p>邮件是私人助理最应该接入的工具之一。Gmail、日历、标签、归档、草稿、客户往来、账单提醒、合作邮件，都是现实工作流的一部分。通过 MCP 或类似 Zapier 的连接方式，可以把这些工具接进 Hermes Agent。</p>
<p>但连接工具不是一口气把所有权限都打开。更稳妥的做法，是按动作精确授权：可以读邮件，可以加标签，可以归档，可以写草稿，但不一定允许直接发送。这样既能让 Hermes Agent 参与工作流，又不会把最终责任完全交出去。</p>
<p>权限设计的原则很简单：高频、低风险、可回滚的动作可以自动化；高风险、代表个人意志、会影响外部关系的动作需要保留确认环节。一个成熟的智能助理，不是越能越权越好，而是越能在正确边界内做事越好。</p>

<h2 id="background-tasks">六、后台任务解决“被打断”的核心痛点</h2>
<p>普通对话很容易被新问题打断。让助手研究一个复杂主题时，临时又想问别的问题，原任务就可能被冲掉。后台任务的意义，就是允许多个长任务同时存在，当前对话继续进行，长期研究在背后运行。</p>
<p>使用后台任务时，可以把一个研究问题、资料整理、市场扫描、自动化机会分析、生活城市比较等任务放到后台，让它慢慢完成。当前窗口继续问其他问题，不需要担心上下文互相污染。</p>
<p>这对高强度使用者非常重要。真实工作不是线性的，而是并发的：一边写方案，一边查资料，一边等反馈，一边整理会议，一边思考新业务。Hermes Agent 如果只能处理一个对话，就跟不上现实节奏；后台任务让它更像真正的助理。</p>

<h2 id="scheduled-tasks">七、定时任务和“梦境序列”让助理主动工作</h2>
<p>一个真正有用的私人助理，不应该只在被叫到时才工作。Hermes Agent 可以通过定时任务主动执行固定流程，例如每天早上 8 点生成早间简报：天气、当天会议、重要提醒、来自企业家或思想家的短句、当天最关键的一件事。</p>
<p>更进一步，可以在简报之前安排一段“梦境序列”。例如每天早上 6 点，让 Hermes Agent 基于所有长期记忆、近期对话、会议记录、本地文件和任务状态，提前思考当天最值得采取的三条建议，以及必须雷打不动完成的一件事。等到 8 点简报出现时，它不只是罗列日程，而是给出经过上下文整合后的行动建议。</p>
<p>这类设计的关键，是让 Hermes Agent 越用越了解自己。每天的结果会反过来进入记忆，新的会议、新的目标、新的项目也会改变后续建议。它不是一次性模板，而是一套随个人成长而变化的日常操作流。</p>

<h2 id="code-bridge">八、把聊天助理和代码环境接起来，才有完整上下文</h2>
<p>很多人的工作已经分裂成两套系统：一边是通用 AI 助手，负责聊天、总结、规划和想法；另一边是 Claude Code、Codex、OpenCode、Antigravity CLI 等代码环境，负责实现、调试和项目推进。两边如果不互通，建议就会缺上下文。</p>
<p>更好的方式，是让 Hermes Agent 了解代码环境里发生的事情，也让代码工具知道 Hermes Agent 里的目标、决策和长期背景。这样，当一个项目正在推进时，通用助理不会只凭抽象描述提建议，代码环境也不会脱离业务目标盲目执行。</p>
<p>完整上下文意味着更少重复解释。当前项目做过哪些尝试、为什么改方向、哪些测试失败过、哪些需求来自会议、哪些任务还没交付，都应该能被同一套系统访问。桥接完成后，Hermes Agent 才真正接近个人 AI 操作系统。</p>

<h2 id="one-assistant">九、不要同时经营六七个助理，选一个深接入</h2>
<p>工具越多，越容易制造新的混乱。一个助手负责邮件，一个助手负责代码，一个助手负责日程，一个助手负责搜索，一个助手负责笔记，看似专业分工，实际会导致记忆分裂、权限分裂和上下文分裂。</p>
<p>更务实的做法，是选择一个主助理，把它深度接入自己的世界。其他模型和工具可以作为能力后端存在，但不应该变成多个彼此不知道对方在做什么的主入口。主入口越统一，个人记忆越完整，任务管理越清楚，日常使用成本越低。</p>
<p>Hermes Agent 的优势就在于适合作为这个主入口：它能接记忆，能跑后台任务，能安排定时任务，能做目标管理，能接模型，能接代码工具，也能接邮件和知识库。深接入比浅尝十个工具更有复利。</p>

<h2 id="goals">十、目标功能要具体，还要有人机握手</h2>
<p>目标功能可以把一次对话变成一个持续推进的任务。设置目标后，Hermes Agent 会围绕这个方向持续工作，通常会在约 20 条消息内保持问题不丢失，直到目标被解决。这相当于给当前会话放置一颗北极星。</p>
<p>目标必须具体。不要写“发展业务”这种模糊愿望，而要写清楚可交付物：需要什么缩略图、什么文档、什么页面、什么课程承诺、什么邮件序列、什么输出标准、什么完成条件。目标越具体，循环反馈越有效。</p>
<p>标准目标功能的不足，是容易缺少人机握手。很多复杂目标不是 AI 单独完成的，而是需要拆成由人完成和由 Hermes Agent 完成的部分。例如课程增长目标，可能包括定义课程承诺、搭建邮件获取机制、编写跟进序列、录制原始内容、制作页面、检查注册流程。某些部分适合 AI，某些部分必须由人完成。</p>
<p>因此，可以给目标功能叠加“超级目标”提示，把大目标分解成多个小任务，并明确每个任务由谁负责、交付标准是什么、完成后怎样进入下一步。这样目标不只是提醒，而是一个小型项目管理系统。</p>

<h2 id="model-routing">十一、模型路由决定成本和质量</h2>
<p>Hermes Agent 的另一个关键能力，是连接不同模型并按任务调度。可以接入自己的 ChatGPT 付费账户、OpenRouter、xAI Grok、OpenAI Codex、Claude 系列、Gemini 相关能力，以及其他模型提供商。命令层面可以通过类似 <code>hermes control model</code> 的方式查看当前模型和可用模型。</p>
<p>真正重要的不是“能接多少模型”，而是“什么任务交给什么模型”。多模态、长上下文、影像和图片分析，可以交给 Gemini 或 Antigravity CLI 这类更合适的能力；代码审查和产品设计，可以交给更擅长推理和工程判断的模型；社交平台实时趋势，可以用具备对应数据入口的 Grok；普通深度研究则不应该总是消耗最贵模型。</p>
<p>模型路由的原则，是把最强模型用在最需要它的地方，把便宜模型用在可拆分、可验证、可重跑的任务上。这样既能提升整体性能，又不会快速烧完 token 和预算。</p>
{fig(SLUG_HERMES, 'hermes-models-clean.jpg', '模型管理的重点不是堆叠更多模型，而是把不同模型放到最适合的任务上。')}

<h2 id="antigravity">十二、Antigravity CLI 与 Gemini 适合多模态和长上下文</h2>
<p>Antigravity CLI 可以理解为新的终端能力入口。安装 CLI、完成登录以后，Hermes Agent 就可以调用它来处理更适合 Gemini 的任务，例如多模态分析、图片理解、长文本材料、长上下文推理、页面生成和复杂资料梳理。</p>
<p>这类工具不应该被当成普通聊天模型使用。它的优势在于处理更复杂的输入形态和更长的材料。如果只是普通文本问答，未必需要动用它；如果任务涉及大量上下文、图片、页面、代码或影像材料，Antigravity CLI 的价值会更明显。</p>
<p>在一个成熟系统里，Hermes Agent 更像调度层，Antigravity CLI、Codex、Claude、Grok、OpenRouter 后端模型都是可调用能力。调度层知道目标和上下文，底层模型各做擅长的事情。</p>

<h2 id="control-center">十三、任务控制中心让使用情况可见</h2>
<p>只靠聊天记录，很难知道整个系统到底在怎样运行。一个真正好用的 Hermes Agent 环境，应该有任务控制中心：当前目标、长期目标、后台任务、模型连接、工具连接、使用频率、失败任务、平均用量、最近记忆、可用平台，都能集中展示。</p>
<p>即使某个任务没有跑成功，也应该被记录。失败任务同样有价值，因为它暴露了工具权限、模型选择、提示词结构、外部数据源或目标定义的问题。没有使用统计，就无法改进系统；没有任务面板，就很难长期管理多个并发事项。</p>
<p>任务控制中心的意义不是炫技，而是让个人 AI 系统具备可观察性。看得见连接，才知道哪里断了；看得见目标，才知道哪里卡住；看得见模型，才知道成本花在了哪里。</p>
{fig(SLUG_HERMES, 'hermes-cockpit-clean.jpg', '任务控制中心把目标、后台任务、模型、连接和使用状态集中呈现，让个人 AI 系统具备可观察性。')}

<h2 id="github-backup">十四、每天备份到私有 GitHub 仓库</h2>
<p>个人 AI 助理一旦积累了大量记忆、配置、工具连接和任务历史，就不能只存在一台机器上。更稳妥的做法，是每天给 Hermes Agent 做一次完整快照，并备份到私有 GitHub 仓库。</p>
<p>这样做的好处很现实：换电脑时可以迁移，系统损坏时可以恢复，配置改错时可以回滚，长期记忆也不会因为本地环境问题突然丢失。GitHub 在这里不是公开展示平台，而是一个可版本化、可追踪、可恢复的私有存储位置。</p>
<p>备份任务本身也可以交给 Hermes Agent 定时执行。它每天把关键文件整理好、提交到私有仓库，个人只需要确认仓库权限和敏感信息边界。一个真正长期使用的 AI 系统，必须先解决可迁移和可恢复问题。</p>

<h2 id="local-vs-vps">十五、本地运行通常比 VPS 更简单，也更安全</h2>
<p>Hermes Agent 应该部署在哪里？很多人第一反应是放到 VPS 或云服务器上，觉得这样更像真正的全天候系统。但在多数个人场景里，本地 Mac 或笔记本 24 小时运行反而更简单、更直接，也更容易控制安全边界。</p>
<p>原因很清楚：本地文件、Obsidian、会议记录、桌面应用、代码环境、MCP 服务和浏览器状态，本来就在自己的电脑上。把 Hermes Agent 放在同一台机器上，连接成本最低。如果搬到云端，就要额外处理隧道、权限、网络暴露、认证、安全策略和本地资源映射。</p>
<p>VPS 当然可以用，也可以搭得很安全，但前提是隧道、鉴权、端口、密钥、网络边界都正确。对大多数个人使用者来说，先在自己房间里的一台机器上稳定运行，往往比一开始追求云端部署更务实。</p>
<p>如果担心 Hermes Agent 访问太多本地文件，可以用 Docker 做隔离。Docker 像是在电脑里创建一个独立房间，除了明确允许的路径和服务，容器不能随意碰其他东西。这样既能保留本地运行的便利，又能限制访问边界。</p>

<h2 id="computer-control">十六、电脑控制是加分项，不是全部价值</h2>
<p>Hermes Agent 可以进一步控制本地电脑，例如打开应用、处理文件、执行终端命令、操作某些桌面流程。这种能力很酷，也确实能完成一些自动化动作，但它不是系统最核心的价值。</p>
<p>真正改变体验的，仍然是记忆、工具、目标、模型路由、后台任务和定时任务。电脑控制可以作为额外能力存在，用于执行明确、低风险、可验证的动作。不要因为它很直观，就忽略更底层的长期系统建设。</p>

<h2 id="commands">十七、常用命令背后是几类工作流</h2>
<p>常用命令可以按工作流理解。目标类命令负责让会话围绕一个明确结果持续推进；交接类命令负责切换角色、模型或平台；定时任务负责在指定时间自动执行；后台任务负责并发研究和长任务；方向控制负责在不打断任务的情况下调整输出方向；恢复类命令负责接回不同上下文；看板和多智能体面板负责管理多个任务；教学类命令负责把一个主题拆成可学习路径。</p>
<p>很多时候，不必死记命令。只要 Hermes Agent 正常运行，自然语言也能触发对应动作。但理解这些命令背后的分类，可以帮助设计更稳定的个人工作流。需要持续推进时用目标，需要并发时用后台，需要主动性时用定时，需要角色切换时用交接，需要不打断当前任务时用方向控制。</p>

<h2 id="web-research">十八、互联网检索能力让系统连接外部世界</h2>
<p>Hermes Agent 不能只连接个人世界，也要连接外部世界。网页本质上是 HTML，合适的抓取和检索工具可以把外部信息变成可处理材料。Firecrawl 这类工具的价值，在于更低成本地获取网页内容、解析结构、减少无效 token 消耗，并把互联网资料带入当前任务。</p>
<p>如果一个系统既能读取本地记忆，又能查会议、读邮件、看代码、调模型、跑后台任务，还能低成本检索外部网页，它就不再只是被动助手，而是一个能持续扩展边界的研究与执行层。</p>
{fig(SLUG_HERMES, 'hermes-internet-clean.jpg', '互联网检索能力让 Hermes Agent 既能使用个人长期记忆，也能把外部网页内容纳入当前任务。')}

<h2 id="conclusion">十九、结论：把 Hermes Agent 当成会成长的长期系统</h2>
<p>Hermes Agent 的使用重点，不是多问几个问题，而是把它建设成一个长期系统。第一步是更新到最新版本，补齐 <code>Memory.md</code> 和个人灵魂档案；第二步是连接本地知识库、会议记录、邮件和工具；第三步是使用后台任务、定时任务和目标功能，让它能并发、主动、持续地工作；第四步是接入代码环境和多模型路由，让不同模型各做擅长的事；第五步是建立任务控制中心、私有 GitHub 备份和本地部署边界。</p>
<p>最重要的原则，是选一个主助理深度接入，而不是同时经营一堆浅层助手。Hermes Agent 越了解个人背景，越能给出贴近现实的建议；连接越完整，越能把建议变成行动；目标越具体，越能持续推进到结果。</p>
<p>把它当聊天框，它只会回答问题；把它当个人操作系统，它会开始记住、调度、研究、提醒、执行、复盘，并随着时间越来越懂自己正在服务的人。真正的差距，就藏在这层系统化使用里。</p>
'''


pub.base.POSTS = [
    pub.base.Post(
        slug=SLUG_HERMES,
        title="Hermes Agent 实战框架：记忆、后台任务、模型路由与本地操作系统",
        desc="从记忆系统、本地知识库、会议邮件连接、后台任务、定时任务、目标管理、模型路由、GitHub 备份和本地部署，系统拆解 Hermes Agent 的高阶使用框架。",
        category="AI工具",
        series="AI Agent",
        tags=["Hermes Agent", "AI Agent", "记忆系统", "后台任务", "任务调度", "模型路由", "MCP", "自动化", "本地部署"],
        minutes=14,
        body=BODY_HERMES,
        accent=("#0f172a", "#7c3aed", "#0f766e"),
        required=[
            "Hermes Agent",
            "Memory.md",
            "Soul.md",
            "Obsidian",
            "MCP",
            "后台任务",
            "定时任务",
            "Claude Code",
            "目标功能",
            "OpenRouter",
            "Grok",
            "Antigravity CLI",
            "GitHub",
            "Docker",
            "Firecrawl",
        ],
        minimum=7000,
    ),
]


pub.SCREENSHOT_SOURCES = {
    SLUG_HERMES: [
        (ASSET_ROOT / "clean-shots" / "hermes-memory-clean.jpg", "hermes-memory-clean.jpg"),
        (ASSET_ROOT / "clean-shots" / "hermes-models-clean.jpg", "hermes-models-clean.jpg"),
        (ASSET_ROOT / "clean-shots" / "hermes-cockpit-clean.jpg", "hermes-cockpit-clean.jpg"),
        (ASSET_ROOT / "clean-shots" / "hermes-internet-clean.jpg", "hermes-internet-clean.jpg"),
    ],
}

if __name__ == "__main__":
    pub.main()
