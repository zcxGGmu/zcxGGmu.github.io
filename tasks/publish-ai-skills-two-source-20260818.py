from __future__ import annotations

import importlib.util
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE = TASKS / "publish-ai-skills-two-source-20260815.py"
spec = importlib.util.spec_from_file_location("daily_template", TEMPLATE)
template = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = template
spec.loader.exec_module(template)

base = template.base
base.__file__ = __file__
base.DATE = "2026-08-18"
base.BASE_DT = datetime(2026, 8, 18, 6, 45, tzinfo=timezone(timedelta(hours=8)))
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-ai-skills-two-source-20260818-changed-files.json"
base.PREV_EXISTING_URL = "/2026/generation-burden-east-asia-catch-up-population-dividend/"
base.PREV_EXISTING_TITLE = "这一代人在承受什么：人口红利、社会结构与代际差异"
base.PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
    "/2026/original-accumulation-time-autonomy-ordinary-people/",
    "/2026/next-decade-wealth-leap-deflation-rmb-ai-cashflow/",
]

BODY_A = r'''
<p>AI 开发生态正从单一的代码补全工具，变成由运行时、技能包、记忆层、执行环境、知识输入和质量门共同组成的工作系统。近期出现的一批项目覆盖八个方向、数十个不同能力：有的负责让 Agent 持续运行，有的负责把工程方法固化成 Skills，有的把网页、文档和内部系统接入上下文，还有的把权限、成本和审计放回交付流程。</p>
<p>这类项目不应被当成一次性安装清单。更有价值的观察方式，是按一个实际任务的生命周期来组织它们：先定义规格和权限，再补充信息和上下文，随后在受控环境中执行，最后记录结果、验证输出并保存可以复用的经验。只有这些环节形成闭环，工具数量才会转化为可持续的生产力。</p>

<h2 id="runtime">一、运行时决定 Agent 能否长期完成工作</h2>
<p><a href="https://github.com/deepseek-ai/deepseek-harness" target="_blank" rel="noopener">deepseek-ai/deepseek-harness</a> 将模型、工具、提示词、会话循环、存储、沙箱和界面拆成可替换模块。模块化的意义不只是方便换模型，而是让团队能单独规定工具调用、状态保存和错误处理的契约。复杂任务遇到超时、上下文切换或子任务失败时，系统需要知道该恢复哪一段，而不是重新开始一次不可解释的长对话。</p>
<p><a href="https://github.com/PrimeIntellect-ai/prime-agent" target="_blank" rel="noopener">PrimeIntellect-ai/prime-agent</a> 进一步把编程、研究和长期任务放进持续运行的 Agent 形态。它提示了一个核心工程问题：终端窗口关闭不应等于任务状态消失。真正的长任务需要目标、检查点、可恢复工作区、可追溯日志和明确的中止条件；没有这些基础设施，所谓自主执行只是在放大偶发成功。</p>

<h2 id="orchestration">二、并行协作先要解决边界，而非增加角色</h2>
<p>多个 Agent 同时工作时，最危险的不是速度慢，而是共享状态被无序修改。代码编辑、测试、资料检索、图表制作和评审可以拆分，但数据库、发布分支、依赖锁文件和对外动作必须具有唯一所有者。调度层应把任务输入、允许工具、输出格式、完成条件和回滚方式写清，而不是只把同一句需求分发给不同模型。</p>
<p><a href="https://github.com/paperclipai/paperclip" target="_blank" rel="noopener">paperclipai/paperclip</a> 代表了面向多 Agent 的工作管理界面：目标、任务、预算、审批与运行状态需要被放在同一处检查。这样的控制面不能替代工程责任，却能让负责人看到实际发生了什么，并在成本、权限或结果偏离时及时停止任务。</p>

<h2 id="skills">三、Skills 是可审查的工程依赖</h2>
<p><a href="https://github.com/obra/superpowers" target="_blank" rel="noopener">obra/superpowers</a> 把规划、实现、测试、审查和收尾整理为可调用方法。其价值不在于提示词更长，而在于把何时检查、怎样验证、失败后如何处理变成明确步骤。团队采用 Skills 时应像管理依赖一样管理它们：记录来源和版本，审阅网络、文件和凭据访问范围，升级后比较行为差异，并保留可以回退的稳定版本。</p>
<p><a href="https://github.com/anthropics/claude-plugins-official" target="_blank" rel="noopener">anthropics/claude-plugins-official</a>、<a href="https://github.com/addyosmani/agent-skills" target="_blank" rel="noopener">addyosmani/agent-skills</a> 与 <a href="https://github.com/affaan-m/ECC" target="_blank" rel="noopener">affaan-m/ECC</a> 展示了三种能力沉淀方式：官方维护的插件目录、生产工程实践集合和跨 Agent 的质量与记忆框架。它们都不应获得默认的生产写入权限。先在隔离工作区试运行，再以最小权限接入真实仓库，才能避免方法论成为越权操作的包装。</p>

<h2 id="knowledge">四、知识与记忆要保留来源和失效条件</h2>
<p><a href="https://github.com/virgiliojr94/book-to-skill" target="_blank" rel="noopener">virgiliojr94/book-to-skill</a> 的思路是把技术资料转成可检索、可调用的工作知识；<a href="https://github.com/firecrawl/firecrawl" target="_blank" rel="noopener">firecrawl/firecrawl</a> 则让网页内容能够以结构化方式进入上下文。两者解决的是输入效率，但不自动解决事实正确性。每个关键结论仍应能回到原始页面、版本、页码或抓取时间，并且要处理权限、许可和页面变化。</p>
<p><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory" target="_blank" rel="noopener">TencentCloud/TencentDB-Agent-Memory</a> 和 <a href="https://github.com/semantica-agi/semantica" target="_blank" rel="noopener">semantica-agi/semantica</a> 分别强调团队级记忆资产与可追溯关系图。长期记忆不能把事实、偏好、任务状态和推测混在一起：它们需要不同的写入门槛、保留期和读取范围。尤其在多人协作中，一条未经核验的记忆会比一次临时错误传播得更远。代码图谱、决策关系图也应附带来源和更新时间，方便后续复核。</p>

<h2 id="execution">五、本地执行、内部工具与界面都需要边界</h2>
<p><a href="https://github.com/unslothai/unsloth" target="_blank" rel="noopener">unslothai/unsloth</a> 面向本地模型运行和训练，<a href="https://github.com/ToolJet/ToolJet" target="_blank" rel="noopener">ToolJet/ToolJet</a> 面向内部业务应用、仪表盘和工作流。它们说明 AI 能力正在离真实数据和业务操作更近，但本地不等于无风险，低代码也不等于无须审计。模型版本、硬件资源、数据留存、账号权限和外部写入都需要在上线前被明确测试。</p>
<p>设计和沟通也属于执行链的一部分。<a href="https://github.com/cathrynlavery/diagram-design" target="_blank" rel="noopener">cathrynlavery/diagram-design</a> 将结构图、流程图、时序图和数据图整理为可生成的视觉类型。图能减少交接歧义，但其输入仍要有来源，数据仍要可复核。把可视化放在验证之后，才能避免漂亮图表为未经验证的结论背书。</p>

<h2 id="quality-gates">六、质量门应覆盖输入、执行和输出</h2>
<p>任何组合式 Agent 都至少需要三道质量门。输入门检查资料许可、数据敏感级别、仓库分支和任务范围；执行门限制网络、文件系统、账号和费用权限，并记录每一次工具调用；输出门则核对事实来源、测试结果、格式完整性和是否出现未授权写入。三者缺少任意一个，问题都会被推迟到更难恢复的阶段。</p>
<p>质量门还要能处理不确定性。检索不到证据时，应返回待确认项而不是生成确定结论；工具失败时，应保留错误与中间状态而不是静默重试；涉及外部系统时，应预览即将发生的改动并让责任人确认。这样设计会让流程在初期显得更慢，却能显著降低规模化以后由错误记忆、重复任务和不可逆写入带来的返工成本。</p>

<h2 id="adoption">七、采用顺序应从小闭环开始</h2>
<p>最稳妥的起点是一条低风险、输入输出清晰且可以回滚的流程，例如将公开文档整理成带引用的草稿，或让 Agent 在隔离分支中生成测试清单。先记录成功率、人工修订时间、单次成本、失败类型和恢复耗时；只有指标连续稳定，才扩大数据范围、并发量和写入权限。</p>
<p>运行时让任务可持续，Skills 让方法可复用，知识与记忆让上下文可追溯，内部工具把能力接进业务，质量门则决定系统是否值得信任。成熟的 AI 工作流不是“什么都能做”，而是能清楚说明它准备做什么、依据什么做、实际做了什么，以及失败后如何停止和恢复。</p>
'''

BODY_B = r'''
<p>截至 2026 年 8 月 17 日的一周，AI 与 Agent 开源项目的增量热度集中在三个方向：把信息表达为可用图表，让复杂任务能够持续执行，以及把分散材料整理为可追溯的上下文。榜单中的十个项目并不属于同一层级，但放在同一条工作链上，恰好展示了当前 Agent 系统从输入、推理到协作治理的完整轮廓。</p>
<p>周度增量数据只能说明一个时间窗口内的热度变化，不能替代项目质量、许可证审查、维护活跃度或生产可用性判断。更有意义的是借它识别问题类型，再把每个候选项目放进明确的试点场景、权限范围和验收指标中。</p>

<h2 id="ranking">一、这十个项目覆盖三层能力</h2>
<p>这一周的前十名依次包括 <a href="https://github.com/cathrynlavery/diagram-design" target="_blank" rel="noopener">cathrynlavery/diagram-design</a>、<a href="https://github.com/PrimeIntellect-ai/prime-agent" target="_blank" rel="noopener">PrimeIntellect-ai/prime-agent</a>、<a href="https://github.com/semantica-agi/semantica" target="_blank" rel="noopener">semantica-agi/semantica</a>、<a href="https://github.com/TencentCloud/TencentDB-Agent-Memory" target="_blank" rel="noopener">TencentCloud/TencentDB-Agent-Memory</a>、<a href="https://github.com/cactus-compute/needle" target="_blank" rel="noopener">cactus-compute/needle</a>、<a href="https://github.com/addyosmani/agent-skills" target="_blank" rel="noopener">addyosmani/agent-skills</a>、<a href="https://github.com/unslothai/unsloth" target="_blank" rel="noopener">unslothai/unsloth</a>、<a href="https://github.com/macro-inc/macro" target="_blank" rel="noopener">macro-inc/macro</a>、<a href="https://github.com/paperclipai/paperclip" target="_blank" rel="noopener">paperclipai/paperclip</a> 与 <a href="https://github.com/vitali87/code-graph-rag" target="_blank" rel="noopener">vitali87/code-graph-rag</a>。</p>
<p>它们可以分为三层：表现层负责把复杂结果讲清；运行层负责执行、检索、训练和代码理解；组织层负责记忆、工作区、审批和任务管理。选型时不能把层级混为一谈。一个优秀的图表 Skill 无法解决长期任务恢复，一个团队记忆库也不能替代对代码改动的测试。</p>

<h2 id="diagram">二、图表是 Agent 输出的可读性层</h2>
<p>diagram-design 提供多种结构化图形模板，并以独立 HTML 与 SVG 作为输出载体，适合把架构、流程、时序、时间线和数据关系做成可检查的交付物。它的优势是让表达从临时截图变成可以版本管理的文件；风险则是图表看起来清楚时，团队更容易忽略其事实基础。每张图都应说明数据来源、口径和更新时间，尤其是会影响决策的关系图和指标图。</p>
<p>在实践中，可将可视化置于变更说明、事故复盘和设计评审的最后一步：先有经过验证的事实和边界，再用图缩短沟通路径。对于自动生成的图，还应检查文本溢出、连线含义、单位、时间范围和是否遗漏异常分支。</p>

<h2 id="long-running">三、长期任务需要状态、记忆和恢复</h2>
<p>prime-agent 面向编码和研究等长任务，强调持续运行、子任务协作与经验积累。它适合把“找资料、改代码、跑验证、整理结果”这样的多步骤工作拆成可恢复的过程，但前提是每一步都有清晰的所有权和完成条件。并发研究可以提高信息覆盖，发布、数据库迁移和凭据操作却必须串行并设置人工闸门。</p>
<p>团队若试点这类运行时，应先测量三个指标：任务在中断后能否从正确检查点恢复，多个子任务的结论能否回溯到输入与日志，以及失败时是否能阻止后续外部写入。不能回答这三个问题的“长期运行”，只会把排错成本推迟到任务结束之后。</p>

<h2 id="context">四、可追溯上下文比更长的提示词重要</h2>
<p>semantica 将资料、决定、证据和来源组织为关系图，目标是让关键结论可以追溯到当时依据；TencentDB-Agent-Memory 则把对话、技能、文档和代码关系沉淀为团队可共享的记忆资产。二者都解决上下文碎片化，但都需要治理：谁可以写入，哪些材料可信，过期信息何时失效，敏感内容能否被另一个 Agent 读取，都必须在部署前定义。</p>
<p>code-graph-rag 将类似思路用于代码库，把函数、类和调用关系整理成可查询结构，形成可供 Agent 使用的代码图谱。它可以减少在大型仓库中反复搜索的成本，但不能绕过代码审查和测试。图谱是定位和解释的辅助层，最终改动仍应经过受影响测试、静态检查以及对业务边界的人工判断。</p>

<h2 id="edge">五、小模型与本地执行扩大了部署边界</h2>
<p>needle 面向低资源设备上的工具调用与结构化提取，提醒团队衡量模型尺寸、延迟、功耗和离线能力；unsloth 则服务于本地模型运行和训练。它们适合把一些明确、可验证的能力前移到本地环境，但本地部署并不会自动消除治理问题。模型、数据、提示词、工具权限和日志仍会形成新的攻击面和维护成本。</p>
<p>实际试点应先选择小范围数据集和只读任务，比较云端与本地在质量、延迟、成本和隐私边界上的差异。对模型输出设置结构化模式、范围限制和失败回退，比单纯追求更高吞吐更重要。</p>

<h2 id="work-management">六、工程方法和组织控制面应分开引入</h2>
<p>agent-skills 收集面向 AI 编码的工程实践，macro 将邮件、消息、文档、任务和客户关系放进协作工作区，paperclip 提供面向 Agent 的任务、预算和审批控制面。它们分别作用于“如何做”“在哪里协作”“如何管理”，可组合但不可混用。先引入规范化的只读或草稿能力，再接入协作数据，最后考虑带预算和审批的写入自动化，能大幅降低初期风险。</p>
<p>每个工作区还应具备最小权限、审计日志、成本上限和人工停止开关。任何能读取邮件、客户资料或内部文档的 Agent，都应明确数据用途与保留期限；任何能创建任务、发送消息或修改记录的 Agent，都应有可撤销的操作记录。</p>

<h2 id="evaluation">七、把榜单候选转成可比较的试验</h2>
<p>开始试用前，可先为每一类能力写一张验收表。图表生成检查事实是否可追溯、导出的 HTML 和 SVG 是否可打开；长期任务检查中断恢复、子任务隔离和日志完整性；记忆与图谱检查权限过滤、来源回链和过期清理；本地模型检查目标样本的准确率、延迟、资源占用与异常回退。没有可测标准，试用容易变成一次演示而非工程决策。</p>
<p>试验范围也要渐进：先用公开或脱敏资料执行只读流程，再接入受控草稿，最后才评估外部写入。每次运行应保留输入版本、模型与工具版本、耗时、成本、输出位置和人工修订量。这样即使某个项目不适合生产环境，团队也能留下可复用的选择依据，而不是只留下模糊印象。</p>

<h2 id="conclusion">八、从热度到价值，需要一条验证链</h2>
<p>这一周的项目变化反映出 AI 工具正从单点生成走向图形表达、持续执行、关系化上下文和受控协作。真正的采用顺序应该是：先从一个低风险任务验证输入输出，再加入可追溯上下文，然后接入执行和协作控制面，最后才扩大权限和自动化范围。</p>
<p>周度榜单可以提供候选清单，却不能替团队做决策。把项目放入真实样本，记录成功率、人工修订时间、资源成本、失败模式和回滚效果，才能判断它究竟是短期热度，还是值得进入长期工程体系的能力。</p>
'''

SLUG_A = "ai-agent-ecosystem-runtime-skills-memory-governance-20260817"
SLUG_B = "github-ai-agent-trending-diagram-design-prime-agent-semantica-20260816"
base.POSTS = [
    base.Post(
        slug=SLUG_A,
        title="AI Agent 生态全景：运行时、Skills、记忆与治理如何形成工作闭环",
        desc="从可插拔运行时、工程 Skills 到团队记忆与内部工具，梳理 AI Agent 系统走向稳定交付所需的关键边界。",
        category="AI工具", series="AI Agent",
        tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "工作流", "Agent框架", "AI治理"],
        minutes=13, body=BODY_A, accent=("#0f172a", "#0f766e", "#b45309"),
        required=["运行时", "Skills", "记忆", "治理", "验证", "回滚"], minimum=2400,
    ),
    base.Post(
        slug=SLUG_B,
        title="GitHub AI 趋势周榜：从 diagram-design 到可追溯 Agent 工作系统",
        desc="以一周开源项目变化为线索，拆解可视化、长期运行、团队记忆、本地执行与协作治理的真实边界。",
        category="AI工具", series="AI Agent",
        tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "Agent框架", "RAG", "工作流"],
        minutes=11, body=BODY_B, accent=("#111827", "#2563eb", "#047857"),
        required=["图表", "长期任务", "记忆", "代码图谱", "权限", "验证"], minimum=2500,
    ),
]

template.EXPECTED_LINKS = {
    SLUG_A: {
        "https://github.com/deepseek-ai/deepseek-harness", "https://github.com/PrimeIntellect-ai/prime-agent",
        "https://github.com/paperclipai/paperclip", "https://github.com/obra/superpowers",
        "https://github.com/anthropics/claude-plugins-official", "https://github.com/addyosmani/agent-skills",
        "https://github.com/affaan-m/ECC", "https://github.com/virgiliojr94/book-to-skill",
        "https://github.com/firecrawl/firecrawl", "https://github.com/TencentCloud/TencentDB-Agent-Memory",
        "https://github.com/semantica-agi/semantica", "https://github.com/unslothai/unsloth",
        "https://github.com/ToolJet/ToolJet", "https://github.com/cathrynlavery/diagram-design",
    },
    SLUG_B: {
        "https://github.com/cathrynlavery/diagram-design", "https://github.com/PrimeIntellect-ai/prime-agent",
        "https://github.com/semantica-agi/semantica", "https://github.com/TencentCloud/TencentDB-Agent-Memory",
        "https://github.com/cactus-compute/needle", "https://github.com/addyosmani/agent-skills",
        "https://github.com/unslothai/unsloth", "https://github.com/macro-inc/macro",
        "https://github.com/paperclipai/paperclip", "https://github.com/vitali87/code-graph-rag",
    },
}
template.FORBIDDEN = ["B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里", "本期", "这期", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "BV1"]


def validate_base(outputs: dict[str, str | None]) -> None:
    failures: list[str] = []
    for post in base.POSTS:
        article = outputs[f"2026/{post.slug}/index.html"] or ""
        cover = outputs[f"images/posts/{post.slug}/cover.svg"] or ""
        body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
        plain = base.plain_text(body_match.group(1) if body_match else "")
        if len(plain) < post.minimum:
            failures.append(f"{post.slug}: body too short: {len(plain)}")
        for word in base.FORBIDDEN:
            if word in article or word in cover:
                failures.append(f"{post.slug}: forbidden wording present: {word}")
        for term in post.required:
            if term not in article:
                failures.append(f"{post.slug}: missing required topic: {term}")
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        toc = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != toc or len(h2) < 4:
            failures.append(f"{post.slug}: toc mismatch")
        ET.fromstring(cover)

    ET.fromstring(outputs["index.xml"] or "")
    home_cards = re.findall(r'<a href="([^"]+)" class="a-block">', outputs["index.html"] or "")
    expected_prefix = base.PINNED_PREFIX + [post.url_path for post in base.POSTS]
    if home_cards[:len(expected_prefix)] != expected_prefix:
        failures.append(f"homepage prefix mismatch: {home_cards[:len(expected_prefix)]}")
    rss_links = re.findall(r"<link>(https://zcxggmu.github.io/2026/[^<]+/)</link>", outputs["index.xml"] or "")
    if rss_links[:len(base.POSTS)] != [post.full_url for post in base.POSTS]:
        failures.append(f"rss order mismatch: {rss_links[:len(base.POSTS)]}")
    for post in base.POSTS:
        if post.url_path not in (outputs["archive/index.html"] or "") or post.full_url not in (outputs["sitemap.xml"] or ""):
            failures.append(f"{post.slug}: archive or sitemap missing")
        for kind, term in [("categories", post.category), ("series", post.series), *[("tags", tag) for tag in post.tags]]:
            if post.url_path not in (outputs.get(f"{kind}/{term}/index.html") or ""):
                failures.append(f"{kind}/{term}: missing {post.slug}")
    previous = outputs[base.PREV_EXISTING_URL.strip("/") + "/index.html"] or ""
    if base.POSTS[-1].url_path not in previous:
        failures.append("previous article navigation missing new article")
    if failures:
        raise SystemExit("\n".join(failures))


base.validate = validate_base


def create_commit(outputs: dict[str, str | None], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            if base.get_file(path) is not None:
                entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = base.run_gh(["-X", "POST", base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = base.run_gh(["-X", "POST", base.endpoint("git/commits"), "--input", "-"], {"message": "Publish AI Skills articles 2026-08-18", "tree": tree["sha"], "parents": [ref.commit_sha]})
    base.run_gh(["-X", "PATCH", base.endpoint(f"git/refs/heads/{base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


template.create_commit = create_commit

if __name__ == "__main__":
    template.main()
