from __future__ import annotations

import base64
import importlib.util
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
BASE_SCRIPT = TASKS / "publish-three-life-business-articles-20260809.py"
ASSET_ROOT = TASKS / "video-batch-20260816-bv1ut-bv1ee-bv1fx"

spec = importlib.util.spec_from_file_location("publish_base", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = base
spec.loader.exec_module(base)

_base_run_gh = base.run_gh


def run_gh_with_retry(args: list[str], payload: dict | None = None):
    for attempt in range(5):
        try:
            return _base_run_gh(args, payload)
        except RuntimeError as exc:
            msg = str(exc).lower()
            if attempt < 4 and any(token in msg for token in ["stream error", "cancel", "connection", "reset", "timeout", "temporarily"]):
                time.sleep(2 + attempt * 3)
                continue
            raise


base.run_gh = run_gh_with_retry
base.__file__ = __file__
base.DATE = "2026-08-16"
base.BASE_DT = datetime(2026, 8, 16, 14, 45, 0, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/ai-bubble-hong-kong-japan-fed-china-path/"
base.PREV_EXISTING_TITLE = "AI 泡沫、港股与日本：从流动性到中国路径的市场框架"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-video-batch-bv1ut-bv1ee-bv1fx-20260816-changed-files.json"
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

PAGE1_SIZE = 24
PAGE_SIZE = 10
_active_ref = None


def fig(slug: str, name: str, caption: str) -> str:
    return f'<figure class="post-figure"><img src="/images/posts/{slug}/{name}" alt="{caption}" loading="lazy"><figcaption>{caption}</figcaption></figure>'


SLUG_SKILLS = "matt-pocock-skills-grill-spec-tickets-agent-workflow"
SLUG_CONSUMPTION = "china-consumption-rate-40-production-first-domestic-demand"
SLUG_RENT = "renting-better-than-buying-house-opportunity-cost-cashflow"

BODY_SKILLS = rf'''
<p><a href="https://github.com/mattpocock/skills" target="_blank" rel="noopener">Matt Pocock Skills</a> 的价值，不是又多了一套复杂的 Agent 编排框架，而是把开发过程中最容易失控的几个环节拆成一组可以组合的技能。它解决的是四类常见问题：Agent 做出来的东西和真实需求不一致，失败次数太多，代码异常不知道怎样收口，以及团队如何保证代码质量。</p>
<p>这套方法最重要的一句话是：使用工作流，但不要让工作流接管全部流程。Skills 提供的是单一职责的能力块，开发者仍然负责判断任务复杂度、选择入口、决定什么时候跳步、什么时候加重流程。也正因为它不强行接管，日常小改、复杂需求拆解、大项目维护、Bug 排查和代码审查都能用同一组能力重新组合。</p>
{fig(SLUG_SKILLS, '01-skills-title.jpg', 'Matt Pocock Skills 以一组工程化技能覆盖需求澄清、规格沉淀、任务拆分、实现和审查。')}

<h2 id="workflow-not-autopilot">一、工作流不是自动驾驶，而是工程护栏</h2>
<p>Agent 开发最常见的失败，不是模型完全不会写代码，而是它很快就开始“自以为理解了”。需求说得模糊时，它会补设定；上下文缺失时，它会猜结构；代码质量没人盯时，它会在局部通过的同时埋下全局问题。一个完整工作流的作用，就是把这些风险提前拆开处理。</p>
<p>但工作流如果过重，也会变成负担。某些从零到一的大版本，确实适合用更强的自动化框架，让 Agent 依据细颗粒度计划连续推进。可一旦项目进入日常维护阶段，大部分任务只是小功能、小修复、小改动；模型能力提升后，过细计划反而会浪费上下文和时间。</p>
<p>Matt Pocock Skills 更适合这种中间地带：需要规范，但不需要全流程被框架锁死；需要质量，但不想为一个按钮样式改动启动完整项目治理。它把决策权留给人，把重复的工程动作交给技能。</p>

<h2 id="when-to-use-which-flow">二、什么时候用轻流程，什么时候上重流程</h2>
<p>如果任务极其简单，例如修一个显而易见的样式问题，完全可以直接改，不必启动任何流程。流程本身没有神圣性，只有在它能降低错误率时才有价值。</p>
<p>如果需求一句话说不清楚，就应该先进入 grill。它的任务不是写代码，而是追问、澄清、压缩歧义。再复杂一点的需求，需要把讨论结果沉淀为 spec，让未来的自己和后续 Agent 都知道“为什么这么做、为什么不那么做”。当需求包含多个功能点、多个模块或多个交付面时，再用 tickets 拆成可以独立交付的垂直切片。</p>
<p>大型项目、多人协作、长期演进则更适合 OpenSpec 这类上层机制。OpenSpec 处理的是项目级变更记录、决策历史和跨角色协作；Matt Pocock Skills 更偏向每个具体任务的细节质量。两者不是互斥关系，而是层级不同。</p>

<h2 id="two-skill-modes">三、两类技能：用户触发与模型触发</h2>
<p>这套 Skills 可以分成两类。第一类是用户主动触发的入口技能，例如 grill-me、grill-with-docs、to-spec、to-tickets、implement、code-review。它们对应真实开发流程中的一个阶段。</p>
<p>第二类是模型在技能内部主动调用的子技能。这样设计是为了遵守单一职责原则：入口技能负责表达使用意图，底层技能负责执行具体流程。比如 grill-me 和 grill-with-docs 都会调用 grilling；差别在于 grill-with-docs 还会调用额外的文档沉淀能力，把讨论结果写成后续可用的材料。</p>
{fig(SLUG_SKILLS, '02-skill-modes.jpg', 'Skills 分为用户主动调用和模型内部调用两种形态，入口技能和底层技能各守单一职责。')}

<h2 id="grill-first">四、grill-me：先把问题问清楚</h2>
<p>grill-me 的本质是需求拷问。它适合那些“感觉要做点什么，但说不清到底要什么”的任务。很多开发失败并不是实现能力不足，而是问题本身没有被定义。越早让 Agent 追问，越能减少后面返工。</p>
<p>grill-with-docs 更进一步：它不只追问，还会把结论结构化保存。普通 grill 结束后，讨论可能停留在上下文里，一旦会话被压缩或换 Agent 接手，许多判断就会丢失。grill-with-docs 会把关键背景、约束、决定和理由落到文件中，让后续流程有据可依。</p>
<p>这一步看似慢，实际是在减少后面的盲改。对 AI 编程来说，真正昂贵的不是多问几个问题，而是在错误目标上快速写出一堆看似能跑的代码。</p>

<h2 id="to-spec-source-of-truth">五、to-spec：把对话变成单一事实源</h2>
<p>需求澄清以后，to-spec 会把讨论沉淀成可以发布、可以实现、可以审查的规格。这里的关键不是“写一份文档”，而是建立单一事实源：做什么，不做什么，为什么这样做，有哪些约束，验收标准是什么。</p>
<p>没有规格时，未来任何人回头看都很难判断当初为什么做了某个取舍。尤其在 AI 参与开发后，代码产出速度变快，决策记录反而更重要。否则几天之后连自己都可能忘记当时为什么这么选，更不用说让另一个 Agent 接手。</p>
<p>规格不是形式主义。它让需求从“临时聊天”变成“可追踪决策”，也是后续测试、拆票、实现和审查的共同依据。</p>
{fig(SLUG_SKILLS, '03-spec-flow.jpg', 'spec 的作用是把对话结论沉淀为单一事实源，避免后续实现偏离原始约束。')}

<h2 id="to-tickets-vertical-slices">六、to-tickets：按垂直切片拆任务</h2>
<p>to-tickets 的重要性在于拆分方式。很多人习惯按技术层拆任务：先写所有数据库层，再写所有服务层，再写所有前端页面。这样拆出来的任务之间依赖重、难独立验收，也不适合多个 Agent 并行。</p>
<p>更好的方式是垂直切片。假设有 A、B、C 三个增删改查能力，不应先做 A/B/C 的数据库，再做 A/B/C 的服务层，而应先完成 A 的数据库、服务、接口和界面，让它成为一个能独立交付、能独立验证的小功能；然后再做 B，再做 C。</p>
<p>这种拆法能显著降低长任务失控概率。每张 ticket 都有清楚的输入、输出、依赖和验收口径，既方便人审查，也方便为每个 ticket 开新的上下文，让 Agent 不被前一段执行噪声污染。</p>
{fig(SLUG_SKILLS, '04-tickets.jpg', 'tickets 不是按技术层横切，而是尽量拆成可独立交付的 vertical slices。')}

<h2 id="implement-tdd-review">七、implement：TDD、实现与代码审查</h2>
<p>implement 是主流程里的实现入口，但它并不是简单地让模型直接写代码。它会把实现放进更严格的工程顺序里：先测试，再开发，再审查。测试驱动开发在 AI 编程时代变得更自然，因为写测试、跑失败、补最小实现这些原本让人嫌麻烦的动作，已经可以由 Agent 高速完成。</p>
<p>标准 TDD 通常包含红、绿、重构三步：先写失败测试，再写最小代码让测试通过，最后在测试保护下优化结构。Matt Pocock 的拆分更细：TDD 技能只承担红绿循环，重构和质量检查交给 code-review 相关流程处理。这样做的好处是每个技能职责更清楚，不会把“功能是否满足”和“代码是否优雅”混在一起。</p>
<p>code-review 也分维度审查：一类检查代码是否符合项目编码标准，另一类检查实现是否符合已定义规格。分开报告能避免一个维度掩盖另一个维度。例如代码风格很漂亮，但需求没做对；或者需求完成了，但实现方式破坏了项目约定。两者都需要单独被看见。</p>
{fig(SLUG_SKILLS, '05-main-flow.jpg', '主流程可以概括为 grill → spec → tickets → implement，再根据复杂度灵活跳步。')}

<h2 id="sdd-is-standard-now">八、规格驱动开发正在成为事实标准</h2>
<p>过去软件工程也强调先设计、先测试、先审查，只是执行成本高，人又容易偷懒。团队里只要有一块短板，最终质量就会被那块短板拉低。进度压力一来，很多原本该做的地基工作就被省掉。</p>
<p>AI 改变了成本结构。模型写代码速度足够快，前置规格、测试和审查的相对成本下降，收益反而上升。现在还完全凭一句模糊需求直接开写，更像是快速但低质量的粗糙加工。想做出稳定作品，规格和测试已经不再是“高级流程”，而是基础设施。</p>
<p>差别只在于规格文件怎么设计、包含哪些内容、由谁维护、什么时候更新。写文档不是目的，让 Agent 在同一组事实和约束里工作才是目的。</p>

<h2 id="exploration-before-flow">九、主流程之前：探索、原型和分诊</h2>
<p>并不是所有任务一开始就能进入 spec。有些需求连目标都没想清楚，需要先探索。探索型流程的产物通常是一张任务地图和一组不同类型的 ticket：哪些需要研究，哪些需要追问，哪些需要原型，哪些可以直接实现。</p>
<p>research 适合那些模型不知道、但代码库或材料里能查出来的问题。grill 适合那些答案在人的脑子里、需要通过追问挖出来的问题。prototype 则对应原型驱动开发：有些产品体验只有先做出来，才知道下一步该怎么做。AI 让高保真原型成本下降，原型不再只是昂贵的大项目动作。</p>
<p>triage 更适合多人协作项目。项目有大量 issue 或外部反馈时，它可以先做分类：Bug、需求、需要补充信息、需要人处理、Agent 可自动处理、暂不处理。分诊不是写代码，但它决定了后续工作是否有秩序。</p>

<h2 id="setup-and-side-skills">十、setup、Debug、Teach 与上下文交接</h2>
<p>setup 通常安装后运行一次，用来配置 issue tracker、triage level 等基础选项。如果项目暂时不需要分诊，配置可以很轻；如果要接入协作系统，就应该把这些选项提前设好。</p>
<p>复杂 Bug 可以用专门的调试技能收束。重构入口也可以单独调用，只是它非常消耗上下文和 token，应该在有测试保护、目标明确时使用。Teach 属于元技能，适合把一个主题拆成学习材料；如果目的是让 Agent 通过提问帮助自己理解，类似 Sigma 的问答式学习也可以作为替代思路。</p>
<p>上下文压缩技能也很实用。长任务中途换 Agent、换会话或跨天继续时，仅靠对话历史很容易丢重点。把阶段性背景、已完成事项、未解决问题和验证证据写成 Markdown，下一位接手者才不需要重新探索。</p>

<h2 id="ask-matt-as-router">十一、ask-matt：不知道用哪个技能时的路由器</h2>
<p>ask-matt 可以理解为技能路由器。当任务摆在面前，却不确定应该先 grill、先 research、先 prototype、先 to-spec，还是直接 implement 时，先问它。它的价值不是替你完成工作，而是帮你判断下一步该用哪个技能。</p>
<p>这也是整套 Skills 的入门方式：不必一开始记住所有技能。先记住主链路，复杂度上来再逐步加技能；实在不确定，就用 ask-matt 选择入口。这样既不会被工具数量吓住，也不会把简单任务变复杂。</p>
{fig(SLUG_SKILLS, '06-ask-matt.jpg', '主流程之外还存在探索、分诊、教学、上下文交接和 ask-matt 等辅助技能。')}

<h2 id="practical-operating-model">十二、一套可落地的使用模型</h2>
<p>实际使用时，可以按复杂度建立四档策略。第一档，极小改动直接做，保持测试和验证即可。第二档，需求表述不清先 grill，把目标问清楚。第三档，有明确功能但影响范围较大，先 to-spec，再 implement。第四档，多功能、多模块或多人协作，先 to-spec，再 to-tickets，把每张 ticket 作为独立交付单元推进。</p>
<p>如果缺信息，用 research；如果缺人脑里的判断，用 grill；如果不知道产品到底长什么样，用 prototype；如果 issue 太多，用 triage；如果不确定入口，用 ask-matt。这样 Skills 才是工具箱，而不是新一层束缚。</p>

<h2 id="avoid-overusing-skills">十三、不要把技能当成万能按钮</h2>
<p>这套工作法真正容易用错的地方，是把每个任务都塞进完整链路。技能越多，越需要克制。一个一眼能修的错误，不必先写 spec；一个范围非常清楚的小改动，不必拆 tickets；一个没有风险的文本调整，也不需要复杂审查。工程纪律不是流程堆叠，而是在正确的时机增加正确的约束。</p>
<p>反过来，越是说不清需求、越是涉及多人协作、越是会改变数据结构或用户路径，就越应该把前置流程补齐。grill 用来减少歧义，spec 用来固化判断，tickets 用来控制切片，TDD 用来证明行为，code-review 用来防止局部通过但整体变差。每个技能都应当回答一个清楚问题：它正在降低哪一种风险。</p>
<p>因此，成熟用法不是背熟命令列表，而是形成一套判断习惯。先判断任务复杂度，再选择入口；先决定要降低什么风险，再决定调用哪个技能；先让输出可验证，再追求执行速度。这样才能既保留 AI 的速度，又不牺牲工程交付质量。</p>

<h2 id="conclusion">十四、结论：把 Agent 开发从“会写代码”推进到“能稳定交付”</h2>
<p>AI 编程的下一阶段，不是单纯追求模型更快写代码，而是让它更稳定地理解需求、沉淀规格、拆分任务、实现功能、接受审查并完成交接。Matt Pocock Skills 之所以值得认真拆解，是因为它没有把开发者赶出流程，而是把开发者最需要掌控的决策点保留下来。</p>
<p>grill 负责把问题问清楚，to-spec 负责把事实沉淀下来，to-tickets 负责把复杂需求拆成可交付切片，implement 负责在 TDD 和审查下推进实现，code-review 负责把项目标准和需求标准分开检查，ask-matt 负责在迷路时选择入口。它们合在一起，构成的不是自动驾驶，而是一套能让 Agent 少跑偏、少返工、少制造低质量代码的工程护栏。</p>
'''

BODY_CONSUMPTION = rf'''
<p>中国经济最尖锐的矛盾之一，是生产能力已经足够强，居民消费能力却没有同步变强。官方层面已经承认内需偏弱、居民消费率偏低，但短期政策重心仍然更偏向产业、生产、科技和制造业升级。这不是简单的刺激力度问题，而是发展模式是否愿意从生产端真正转向居民端的问题。</p>
<p>居民消费率只有约 40%，意味着经济成果中通过居民消费进入普通人生活的比例偏低。发达经济体的居民消费占比通常明显更高，很多在 60% 到 70% 区间。差距背后不是某个家庭“爱不爱花钱”，而是收入分配、资产负债、工作预期、公共保障和政策资源流向共同作用的结果。</p>
{fig(SLUG_CONSUMPTION, '01-consumption-rate.jpg', '居民消费支出占 GDP 比重偏低，反映的是经济成果进入居民生活端的比例不足。')}

<h2 id="production-first-remains-mainline">一、生产优先仍然是主线</h2>
<p>外部讨论常把焦点放在产能、补贴和贸易摩擦上，但更深的问题是：中国是否准备改变以生产投资和产业升级为优先的增长模式。从现实信号看，答案至少在短期内是否定的。政策会承认消费不足，也会通过以旧换新、国补、贷款贴息等方式托底消费，但更强的资源仍然会流向科技企业、新质生产力、制造业升级和供应链安全。</p>
<p>这条路线有自己的逻辑。过去几十年，中国确实靠工厂、基础设施、产业链和出口建立了完整制造体系。关键技术、产业安全、国际竞争力、半导体、机器人、新能源、高端制造，都被视为国家未来竞争的核心。突然压低投资和生产端支持，不只会影响企业，还会冲击地方财政、就业、银行资产和产业链稳定。</p>
<p>所以现在的政策选择并不是“完全不管消费”，而是“消费托底，生产优先”。这也是普通人感受到压力的原因：文件里会频繁出现扩大消费、鼓励消费、提振内需，但真正决定资源分配的主轴仍然偏向生产端和科技端。</p>

<h2 id="what-ordinary-households-lost">二、普通家庭失去的不只是消费欲望</h2>
<p>很多人把消费不足归因于“不愿意花钱”，这其实太浅。普通家庭不是突然变得保守，而是在过去几年同时失去了几项关键安全感。</p>
<p>第一是资产价值。对多数中国家庭来说，房子是最重要资产。很多家庭用多年积蓄支付首付，再用未来二三十年的收入偿还按揭。房价下跌不是账面数字变化，而是家庭资产负债表被重估。尤其 2017 年到 2021 年高位上车的人，很多不是投机，而是为了结婚、生育、改善居住、孩子入学和拥有一个稳定的家。</p>
<p>第二是收入预期。就业市场更难，降薪、裁员、岗位收缩、加班强化都在削弱家庭对未来收入的信心。一个人如果不知道明年还能不能维持今天的工资，自然不敢轻易消费。</p>
<p>第三是事业路径。工作岗位并不少，但真正有积累、有晋升、有收入成长、有专业复利的岗位变少。大量岗位时间长、替代性强、看不到成长空间，只能维持基本现金流，却很难让人相信未来会更好。</p>
<p>第四是未来风险。教育、医疗、养老、育儿、住房都需要大量资金。一次疾病、一次失业、一次老人重病，就可能击穿家庭现金储备。消费弱不是情绪问题，而是资产、工作和未来安全感同步下降后的理性反应。</p>

<h2 id="why-voice-is-weak">三、居民端为什么难以形成强博弈能力</h2>
<p>企业遇到困难，可以通过税收优惠、融资支持、订单安排、行业协会、地方政府和主管部门表达诉求。行业遇到困难，也更容易形成集中反馈。但普通人的困难往往是分散的：消费下降、房价下跌、婚育减少、就业恶化、信心不足。只有这些指标严重到影响宏观数据时，居民端压力才会被系统识别。</p>
<p>普通人并不是没有诉求，而是缺少把分散痛苦转化为政策议价能力的渠道。每个家庭都在承受房贷、教育、医疗、工作和养老压力，但这些压力很难像企业项目那样被打包成一个可统计、可考核、可融资、可落地的政策抓手。</p>
<p>这就是居民端弱势的根本原因。情绪可以表达，困难可以被看见，但能不能进入资源分配和政策设计，取决于它能否被组织成有效力量。</p>

<h2 id="production-coalition">四、生产端为什么更容易形成利益同盟</h2>
<p>生产端天然更容易组织。第一，国家战略需要科技自主、产业安全和国际竞争力。关键技术掌握在自己手里，才不会在产业链和核心技术上被卡住。这个逻辑很强，且能被明确写进长期战略。</p>
<p>第二，地方政府更容易考核生产端结果。建产业园、引项目、上固定资产投资、推动产值和税收，都可以被统计、汇报和考核。相比之下，直接给居民发钱，有的人可能储蓄，有的人可能跨区域消费，对地方政绩的确定性反而较弱。</p>
<p>第三，企业需要补贴、融资、订单和资本市场支持。科技企业、新能源企业、半导体企业、高端制造企业都可以围绕产业升级叙事获得资源。资本市场也会在政策明确支持的方向上形成更强的融资通道。</p>
<p>第四，金融机构也更容易服务生产端。贷款贴息、融资担保、基金、上市融资、保险资金入市，都能以产业项目为载体运行。居民端需要的劳动法执行、最低工资提高、公共医疗教育支出、养老育儿保障，见效周期更长，也更难在短期考核里体现。</p>
{fig(SLUG_CONSUMPTION, '02-production-side-map.jpg', '国家战略、地方政府、企业和金融机构更容易围绕生产端与科技端形成资源合力。')}

<h2 id="policy-red-line">五、所谓经济模式红线，画在生产端</h2>
<p>面对外部关于产能过剩和产业补贴的指责，中国释放的信号并不是准备放弃生产端路线，而是解释并捍卫这套发展模式。消费低被承认，但低消费率被解释为具有历史和阶段性原因；政策也不主张用直升机撒钱迅速改变结构，更不会为了提高消费率而压低投资和外贸。</p>
<p>这条红线的含义是：制造业仍然被视为支柱性产业，制造业升级仍然被视为中国最真实的竞争优势。政策会用国补、贴息和金融传导托底居民消费，但资金、市场、银行和保险资源仍会向科技企业与新质生产力倾斜。</p>
<p>真正的问题在于，科技增长能否在足够短的时间里创造足够广泛的就业、工资和地方收入，接住房地产和传统行业留下的缺口。如果接不住，生产端越强，居民端越弱，内需矛盾反而会更明显。</p>
<p>短期托底和长期分配是两件事。补贴可以让某些商品卖得更快，贷款贴息可以让部分消费提前发生，但这些工具不会自动改变收入结构，也不会自动减少家庭对教育、医疗、养老和住房的担忧。只要居民端没有稳定增量，消费政策就更像临时止痛，而不是体质修复。</p>

<h2 id="where-consumption-stimulus-fails">六、绕开居民端的刺激为什么会遇到瓶颈</h2>
<p>如果企业信心、资本市场、国补、贷款贴息和科技投资都被充分尝试，仍然无法改善整体循环，那么问题就不是某一种工具不够，而是所有工具都在绕开同一个堵点：居民没有足够收入、信心和安全感去承接生产能力。</p>
<p>生产越来越多的商品，最终要卖给谁？如果居民收入只够基本生活，自己生产出来的许多东西自己消费不起，商品只能依赖外需、降价、补贴或库存消化。外部市场有贸易壁垒，内部市场又缺购买力，生产优先模式就会面临越来越强的反噬。</p>
<p>过去中国缺生产能力，优先建设工厂、基础设施和产业链有充分合理性。今天真正缺的已经不是更多同质化商品，而是能稳定购买这些商品的人。</p>

<h2 id="external-demand-limit">七、外需不能永远替代内需</h2>
<p>当内部消费承接不足时，生产端会自然寻找外部市场。出口可以消化产能，也能带来企业利润和就业，但它无法永久替代本国居民购买力。原因很简单：外部市场也有自己的产业、就业、选民和政策压力。别的国家会用关税、反补贴、产业政策和本土保护来维护自己的企业与工人。</p>
<p>因此，把过多商品长期压向外部市场，会把国内的内需问题转化成国际贸易问题。对方指责产能过剩，中国强调产业优势和生产效率，双方都在维护自己的经济利益。贸易谈判表面上讨论补贴和产能，本质上是在争夺谁来承接过剩生产，谁来承担产业调整成本。</p>
<p>如果内部居民收入不强，外部需求又受到限制，企业再获得融资也会遇到销售天花板。生产端可以先繁荣一段时间，但如果最终没有足够终端购买力，投资回报、就业扩张和地方收入都会受到限制。内需不是锦上添花，而是生产体系长期闭环的基础。</p>

<h2 id="how-to-judge-real-shift">八、怎样判断政策是否真正转向居民端</h2>
<p>判断政策有没有真正转向普通人，不能只看文件里出现多少次“扩大消费”“鼓励消费”“支持消费”。更关键的是四个指标。</p>
<p>第一，居民收入能不能持续增长，尤其是工资性收入和经营性收入。第二，房产和债务压力能不能缓解，让家庭资产负债表不再继续恶化。第三，教育、医疗、养老、育儿成本能不能更多由公共财政承担，降低家庭预防性储蓄压力。第四，钱能不能直接进入居民资产负债表，而不是只通过企业、项目和金融链条间接传导。</p>
<p>如果这些指标没有变化，消费券、补贴和鼓励贷款消费只能短期托底，无法改变居民不敢花钱的根本原因。</p>

<h2 id="life-feels-expensive">九、为什么物价低，生活仍然贵</h2>
<p>生产优先、居民后置会产生一种很特殊的体验：商品越来越多，价格越来越低，普通人却觉得好生活越来越贵。基础消费品可能很便宜，但只要想追求更安全、更稳定、更高质量的教育、医疗、居住、养老和育儿服务，付出的代价就会急剧上升。</p>
<p>一分钱确实可以买到一分钱的货，但如果想买两分钱的品质，可能要付出远高于两分钱的成本。这种结构下，低物价并不自动等于高生活质量。真正影响居民消费意愿的，是高质量生活的边际成本和未来风险。</p>
<p>如果一个家庭每次提高生活质量都要付出巨大溢价，它就会自然压缩消费，把钱留给不确定未来。消费弱，不是道德问题，而是家庭风险管理的结果。</p>

<h2 id="ordinary-people-pressure">十、“再苦一苦老百姓”的真实含义</h2>
<p>“再苦一苦老百姓”不是一句政策文件里的话，而是普通人对资源分配感受的概括。它指的是：当生产端、产业端、科技端和企业端需要资源时，政策机制能更快响应；当居民端需要收入、保障、休息权、劳动权益和公共服务时，响应慢、周期长、见效难。</p>
<p>这并不意味着生产端不重要。问题在于，一个经济体不能只依靠生产端自我循环。没有居民收入增长和安全感恢复，生产能力最终会遇到需求约束。产业升级如果不能变成广泛就业、工资增长和家庭信心，就很难真正修复内需。</p>

<h2 id="repair-household-balance-sheet">十一、居民端修复要先修家庭资产负债表</h2>
<p>扩大内需不能只从“让大家花钱”开始，而要先从家庭资产负债表开始。房价下跌以后，很多家庭名义资产缩水，贷款本金却没有同步减少。收入预期不稳时，家庭会自然提高储蓄率，用来防失业、防疾病、防老人养老、防孩子教育。此时再用消费口号要求居民多花钱，效果一定有限。</p>
<p>真正有效的修复，至少要包含三条线。第一，降低债务压力，让高位买房家庭不再把未来二三十年现金流全部锁进月供。第二，稳定就业和工资，让劳动收入能覆盖基本生活之外的品质需求。第三，扩大公共服务，把教育、医疗、养老和育儿的一部分风险从家庭账本转移到公共财政账本。</p>
<p>只有当家庭觉得未来不会被一次风险击穿，才会减少预防性储蓄，重新释放消费。消费不是被宣传出来的，而是从安全感里长出来的。</p>

<h2 id="why-shift-is-hard">十二、为什么短期转向居民端很难</h2>
<p>居民端政策见效慢，是短期转向困难的重要原因。给企业融资、给项目贴息、建设产业园、推动上市融资，往往很快就能形成项目、投资、产值和统计结果；但提高居民收入、严格执行劳动法、改善公共医疗教育、降低育儿成本，可能需要五年、十年甚至更长时间才能完整显现。</p>
<p>这会造成一种政策偏好：越是下行压力大，越容易选择短期可统计、可交差、可形成项目的工具；越是需要长期投入、制度调整和利益再分配的居民端改革，越容易被放在后面。不是因为居民端不重要，而是因为它更难、更慢、更分散，也更难被单个部门拿来作为立刻可见的成绩。</p>
<p>但难并不等于可以绕开。如果产业升级最终不能创造足够岗位和工资，生产端资源再多，也只能形成局部繁荣。真正能支撑长期内循环的，不是企业融资规模，而是居民持续购买能力。</p>

<h2 id="conclusion">十三、结论：真正的扩大内需，要让居民有钱、有闲、有安全感</h2>
<p>中国过去最缺的是生产能力，所以工厂、基础设施、制造业体系和产业链建设曾经是正确重点。现在矛盾已经变化：商品不缺，缺的是稳定购买商品的人；产能不缺，缺的是能承接产能的居民收入；政策口号不缺，缺的是进入家庭资产负债表的实质改善。</p>
<p>真正扩大内需，不只是让居民多花钱，更是让居民敢花钱、能花钱、愿意为未来花钱。它需要收入增长、房债压力缓解、劳动权益改善、公共财政更多承担教育医疗养老育儿成本，也需要普通人的困难能在政策设计中拥有更强权重。</p>
<p>生产端和科技端仍然重要，但如果居民端长期后置，经济循环就会出现越来越明显的断点。未来真正的转向，不在于文件怎样表述，而在于普通家庭的账本是否变轻，收入预期是否变稳，对未来的安全感是否回来。</p>
'''

BODY_RENT = r'''
<p>在当下很多城市，租房比买房更划算，而且这个结论不是情绪判断，而是经济账。房子当然是用来住的，但实现居住目的有两种方式：买房和租房。房价高、租售比低、资产价格下行、收入预期不稳时，租房就是用较低成本占用高价值资产，把原本需要承担的资产风险留给房东。</p>
<p>很多人不愿意这样算，因为房子在文化里被赋予了太多额外含义：根、安稳、身份、婚姻、家庭、社会认可。但市场并不因为这些含义就停止重估价格。房子已经商品化，就必须接受现金流、机会成本和资产价格的检验。</p>

<h2 id="rent-price-ratio">一、低租售比决定了租房的财务优势</h2>
<p>先看一笔简单账。假设一套房总价 200 万，每月租金 4000 元，这在不少一二线城市已经不算低租金。年租金是 4.8 万，毛租金收益率只有 2.4%。如果再扣除物业费、维修、空置、折旧、重新装修和交易税费，净收益会进一步下降。</p>
<p>这就是低租售比的含义：租客用相对低的现金支出，获得了对高价资产的居住使用权；房东则用高额本金承担资产价格波动和维护责任。只要房价不涨，房东很难获得理想收益。只要房价下跌，房东不仅租金收益被成本吃掉，还要承受资产贬值。</p>
<p>买房看起来是把钱换成资产，租房看起来是把钱花掉，但在低租售比环境里，租金并不是纯损失，它购买的是居住权，同时让租客避开大额资产占用。</p>

<h2 id="opportunity-cost">二、买房真正昂贵的，是机会成本</h2>
<p>买房不只是支付房款，还要付出机会成本。所谓机会成本，是指这笔钱如果不买房，本来可以获得的收益。全款买房的人，可能放弃了债券、红利股、存款、货币基金或其他低风险资产的收益；贷款买房的人，虽然没有全款资金，但也把首付、月供能力和未来现金流锁进了房子。</p>
<p>如果一笔资金可以在较低风险下获得年化 3% 到 5% 的回报，而买房后房价不涨甚至下跌，那么买房的损失就不只包括账面跌价，还包括本来可以赚到却没有赚到的钱。很多家庭只计算月供和房价，却没有计算被房子占用掉的其他选择。</p>
<p>租房的优势不只是“少付一点居住成本”，更是保留了现金、流动性和重新选择的能力。现金在不确定时代尤其重要，它不是冷冰冰的数字，而是换城市、换工作、等待资产便宜、应对风险的筹码。</p>

<h2 id="falling-market">三、下跌市场里，不持有房产本身就是收益</h2>
<p>在房价上涨周期，不持有房产会同时承受两重压力：一边付租金，一边看资产价格越来越贵。但在下跌周期，逻辑反过来了。不持有房产，就不用承担资产下跌；付出有限租金，就可以继续满足居住需求。</p>
<p>如果一套 200 万的房子一年跌 5%，账面损失就是 10 万。租客一年付 4.8 万租金，表面上是支出，但与持有者相比，租客少承担了更大的资产损失。只要房价跌幅大于租金支出，房东就在用自己的资产损失补贴租客的居住。</p>
<p>这听起来刺耳，却是资产市场的基本账本。损失是相对的，可以被对冲。居住需求必须满足，但满足需求的方式不一定非要通过持有资产完成。</p>

<h2 id="housing-is-for-living">四、居住是目的，买和租只是手段</h2>
<p>房子是用来住的。买房和租房都只是实现居住目的的手段。买房支付的是大额购房款，贷款买房还要承担几十年的利息；租房支付的是月租或季度租金，房子不是自己的，但居住功能同样实现了。</p>
<p>把手段误认为目的，会让人做出很重的财务决策。真正应该问的不是“我有没有买房”，而是“我是否以合理成本获得了稳定居住”。如果租房能以更低成本满足当前居住需求，并保留资金和选择权，那么租房就是理性选择。</p>
<p>现在不买，不等于永远不买。今天坚持租房，是由当下房价、租售比、资产下跌趋势和收入不确定性决定的。如果未来房价跌到足够便宜，租金收益率明显提高，或者个人现金流足够稳定，租客完全可以转为买家。</p>

<h2 id="bad-asset-good-price">五、没有永远的垃圾资产，只有不合适的价格</h2>
<p>判断房子不能只看“它是不是房子”，还要看价格。一个资产在高价时可能很差，在低价时可能变好。高位买入、低租金、还要承受下跌风险的房子，是糟糕资产；如果未来价格足够低，租金回报足够高，现金流能覆盖成本，它也可能重新变成可买资产。</p>
<p>同样一家公司，价格高到离谱时可能是坏投资；价格跌到足够低、分红稳定时，可能又变成红利资产。房子也一样。居住需求真实存在，但资产价值要由未来现金流和增值潜力决定，而不是由“房子天然保值”这种观念决定。</p>
<p>因此，理性的态度不是永远不买，也不是永远要买，而是在每个时点算清楚账：价格、租金、利率、收入稳定性、家庭需求、机会成本、流动性和风险承受能力。</p>

<h2 id="security-feeling-and-debt">六、安全感不能建立在债务幻觉上</h2>
<p>很多人明知道租房更划算，仍然想买房，因为觉得买房有安全感，别人的房子住起来不踏实。这个感受真实存在，不能简单否定。但如果没有全款能力，房子并不完全属于自己，它同时也是一笔债务。</p>
<p>贷款买房带来的安全感，必须和月供压力、失业风险、利率变化、资产下跌和流动性损失一起看。断供时房子会被处置，债务压力会反过来吞噬生活稳定。把债务当成根，把抵押资产当成终极安全感，是一种危险幻觉。</p>
<p>反过来说，如果一个人有足够现金全款买房，他到哪里都有重新扎根的能力。此时更需要比较的是：把这笔现金买成房产，是否比持有更优质、更流动、更有现金流的资产划算。</p>

<h2 id="cultural-value">七、房子的文化价值不能替代财务价值</h2>
<p>房子在中国语境里承载了太多文化价值。它被等同于根、家族传承、稳定生活、婚姻资格和社会地位。过去二三十年的上升周期，又强化了“房子永远上涨”的神话，使很多人愿意为这种象征支付超额价格。</p>
<p>但过去土地之所以是根，是因为农业社会里土地是最重要的生产资料。现代城市住房多数时候并不生产现金流，真正更接近生产资料的，反而是厂房、机器、商铺、企业股权和能带来收益的资产。把住房继续当成封建时代土地的替代品，会让人在市场化环境里承受过高成本。</p>
<p>当社会联系高度市场化、资本化后，资产终究要接受账本检验。房子不是宗庙，不是祖坟，也不是任何神圣物。它是商品，商品就遵循商品规律。</p>

<h2 id="where-rent-arbitrage-comes-from">八、租房的套利空间来自观念滞后</h2>
<p>租房为什么能形成套利？很大一部分原因来自持有者的观念滞后。一些多套房持有者即使面对下跌，也不愿意按市场价格出售，因为在他们心里，房子不仅是资产，还是一辈子奋斗的象征、家族安全感的锚点和身份的证明。</p>
<p>这些观念让他们愿意继续承担资产损失、维护成本和低收益，把房子以相对低租金交给租客使用。租客支付租金，获得居住权，同时不承担价格下跌。套利空间正是从这种文化溢价和市场现实之间的落差里产生的。</p>
<p>如果租客也用同样的传统观念理解市场，把“必须买房”放在所有财务理性之前，就会在价格高、现金流差、风险大的阶段吃亏。市场不认情怀，只认价格和现金流。</p>

<h2 id="mobility">九、流动性时代，灵活性本身就是资产</h2>
<p>今天的社会流动性和信息化程度远远高于过去。一个人一生换三五个城市工作并不罕见，职业路径、家庭结构、城市机会都可能变化。买房会把人和某个城市、某个区域、某笔债务深度绑定；租房则保留迁移和调整的空间。</p>
<p>灵活性不是软价值，而是真实资产。它让人可以靠近更好的工作机会，躲开衰退区域，等待价格更合理的买点，也能在家庭变化时重新匹配居住需求。房子提供稳定，现金和租房提供弹性。在不确定时代，弹性本身值得付费。</p>

<h2 id="decision-framework">十、普通人该怎样做买租决策</h2>
<p>第一，看租售比。租金收益率越低，租房越占优；租金收益率越高，买房价值才可能上升。第二，看房价趋势。如果房价明显下行，持有成本要把跌价算进去。第三，看收入稳定性。工作越不稳定，越需要保留现金和流动性。</p>
<p>第四，看家庭刚性需求。孩子入学、老人照护、通勤、婚育、长期城市定居都会影响选择，但这些需求也要被量化，而不是直接压倒所有财务逻辑。第五，看机会成本。首付和月供占用的资金，本来能做什么，必须算进总账。</p>
<p>买房不是错误，错误的是在不合适的价格、不稳定的收入和高杠杆条件下，把它当成唯一安全感。租房也不是低人一等，它可能是在特定周期里更成熟的财务选择。</p>

<h2 id="rent-is-expensive-but-buying-can-be-more-expensive">十一、房租贵，不等于买房更值</h2>
<p>很多人会反驳：房租也很贵，每个月真金白银交出去，怎么能说租房划算？这个问题要回到比较对象。租金是显性的现金流支出，房价下跌、利息、维修、税费、装修折旧和机会成本则是持有房产的综合成本。前者每月都能看到，后者经常被藏在资产账面和未来现金流里。</p>
<p>如果只盯着每月租金，很容易觉得租房吃亏；但如果把买房后的首付占用、贷款利息、资产跌价和失去流动性全部算进去，租金反而可能是更便宜的居住成本。尤其在下跌周期里，租客没有买下资产，自然也不会承担资产下跌。</p>
<p>这不是鼓励永远漂着，而是提醒普通人不要只比较“房租”和“月供”。月供背后还有本金风险和流动性锁定，房租背后则保留了现金、迁移能力和等待更好价格的权利。</p>

<h2 id="when-buying-becomes-rational">十二、什么时候买房会重新变得合理</h2>
<p>买房重新变得合理，通常需要几个条件同时出现。房价要跌到租金现金流可以解释的水平，租金收益率要能覆盖持有成本，个人收入要足够稳定，家庭长期居住需求要清楚，贷款杠杆不能把生活推到脆弱边缘。</p>
<p>更重要的是，买房不能建立在“再不上车就永远上不了车”的恐惧上。恐惧会让人高估资产稀缺性，低估债务风险。真正好的买点，不需要用恐惧催促成交；它应该经得起计算，经得起压力测试，也经得起“如果未来一年收入下降怎么办”的追问。</p>
<p>压力测试至少要算三种情况：房价再跌一段时间，家庭收入下降一部分，房子短期无法卖出。只要其中一种情况会让家庭现金流断裂，买房就不是稳健选择。很多人以为自己买的是安全感，实际上买的是对未来收入永远稳定的假设。这个假设一旦错了，房子不会保护人，债务会先追上来。</p>
<p>合理买房还要保留余量。首付之后不能把现金清空，月供不能压到生活质量完全变形，家庭还要有应急资金、医疗准备和职业转换空间。一个资产如果要求生活其他部分全部让路，它就不是配置，而是绑架。</p>
<p>所以，租房和买房不是身份选择，而是资产价格选择。价格不合理时，租房是等待；价格合理时，买房才是配置。把这层关系想清楚，就不会被单一观念绑架。</p>

<h2 id="conclusion">十三、结论：冷静一点，先把账算清楚</h2>
<p>当代住房已经商品化，商品就要回到价格、现金流、风险和机会成本。低租售比、房价下行和收入不确定共同存在时，租房不是将就，而是用更低成本满足居住需求，同时把资产下跌风险留给持有者。</p>
<p>房子可以带来情感安全感，但不能因此免于财务检验。现在租房，不等于否定未来买房；现在不买，只是承认当下价格和风险不匹配。等价格足够低、租金回报足够高、收入和家庭需求足够稳定时，买房仍然可以重新成为合理选择。</p>
<p>真正重要的是把情绪和事实分开。不要用头撞墙的方式反抗现实，也不要用传统观念束缚自己的现金流。冷静一点，把自己的账算清楚，才能在市场化世界里为自己争取更实在的好处。</p>
'''


base.POSTS = [
    base.Post(
        slug=SLUG_SKILLS,
        title="Matt Pocock Skills 工作流拆解：从 grill-me 到 spec、tickets 与代码审查",
        desc="以 Matt Pocock Skills 为例，拆解如何用 grill、spec、tickets、implement、TDD 和 code-review 把 Agent 开发推进到可验证交付。",
        category="AI工具",
        series="AI Agent",
        tags=["AI Skills", "Agent", "Matt Pocock", "工作流", "TDD", "代码审查", "OpenSpec", "软件工程"],
        minutes=13,
        body=BODY_SKILLS,
        accent=("#111827", "#7c3aed", "#2563eb"),
        required=["Matt Pocock", "grill-me", "grill-with-docs", "to-spec", "to-tickets", "implement", "TDD", "code-review", "ask-matt", "单一职责", "OpenSpec", "vertical slices"],
        minimum=5200,
    ),
    base.Post(
        slug=SLUG_CONSUMPTION,
        title="居民消费率只有 40%：生产优先、扩大内需与普通人的压力",
        desc="从居民消费率、生产端利益同盟、房产与就业压力出发，理解为什么扩大内需不能只停留在鼓励消费。",
        category="宏观经济",
        series="中国经济",
        tags=["居民消费率", "扩大内需", "产业升级", "中国经济", "消费", "制造业", "房地产", "就业"],
        minutes=12,
        body=BODY_CONSUMPTION,
        accent=("#0f172a", "#0f766e", "#2563eb"),
        required=["居民消费率", "40%", "生产优先", "产业升级", "普通家庭", "资产价值", "收入预期", "生产端", "扩大内需"],
        minimum=4800,
    ),
    base.Post(
        slug=SLUG_RENT,
        title="租房为什么可能比买房更划算：租售比、机会成本与现金流",
        desc="在低租售比和房价下行环境里，租房是用较低成本满足居住需求，同时保留现金、流动性和未来选择权。",
        category="个人财务",
        series="房地产",
        tags=["租房", "买房", "租售比", "机会成本", "现金流", "房地产", "资产配置", "个人财务"],
        minutes=10,
        body=BODY_RENT,
        accent=("#1f2937", "#0e7490", "#f59e0b"),
        required=["租售比", "机会成本", "房价", "租房", "买房", "现金流", "安全感", "商品"],
        minimum=4200,
    ),
]

SCREENSHOT_SOURCES = {
    SLUG_SKILLS: [
        (ASSET_ROOT / "BV1UTby67EUR-article-images" / "01-skills-title.jpg", "01-skills-title.jpg"),
        (ASSET_ROOT / "BV1UTby67EUR-article-images" / "02-skill-modes.jpg", "02-skill-modes.jpg"),
        (ASSET_ROOT / "BV1UTby67EUR-article-images" / "03-spec-flow.jpg", "03-spec-flow.jpg"),
        (ASSET_ROOT / "BV1UTby67EUR-article-images" / "04-tickets.jpg", "04-tickets.jpg"),
        (ASSET_ROOT / "BV1UTby67EUR-article-images" / "05-main-flow.jpg", "05-main-flow.jpg"),
        (ASSET_ROOT / "BV1UTby67EUR-article-images" / "06-ask-matt.jpg", "06-ask-matt.jpg"),
    ],
    SLUG_CONSUMPTION: [
        (ASSET_ROOT / "BV1EeMD6hEaf-article-images" / "01-consumption-rate.jpg", "01-consumption-rate.jpg"),
        (ASSET_ROOT / "BV1EeMD6hEaf-article-images" / "02-production-side-map.jpg", "02-production-side-map.jpg"),
    ],
    SLUG_RENT: [],
}

_base_validate = base.validate


def get_file_at_active_ref(path: str) -> str | None:
    if _active_ref is None:
        raise RuntimeError("active remote ref is not set")
    try:
        data = base.run_gh([base.endpoint(f"contents/{quote(path, safe='/')}?ref={_active_ref.commit_sha}")])
    except RuntimeError as exc:
        if "Not Found" in str(exc):
            return None
        raise
    return base64.b64decode(data["content"]).decode("utf-8")


def cards_from(text: str) -> list[str]:
    return re.findall(r'<a href="[^"]+" class="a-block">.*?</a>', text, re.S)


def card_href(card: str) -> str:
    match = re.match(r'<a href="([^"]+)" class="a-block">', card)
    if match is None:
        raise RuntimeError("card href missing")
    return match.group(1)


def update_home_after_pinned(text: str) -> str:
    for post in base.POSTS:
        text = base.strip_home_card(text, post.url_path)
    matches = list(re.finditer(r'<a href="[^"]+" class="a-block">.*?</a>', text, re.S))
    pinned_last = base.PINNED_PREFIX[-1]
    target = next((match for match in matches if card_href(match.group(0)) == pinned_last), None)
    if target is None:
        raise RuntimeError("final pinned homepage card is missing")
    block = "\n".join(base.home_card(post) for post in base.POSTS) + "\n"
    return text[: target.end()] + "\n" + block + text[target.end():]


def pagination_nav(page: int, total: int) -> str:
    previous = "" if page == 1 else "/" if page == 2 else f"/page/{page - 1}/"
    nxt = f"/page/{page + 1}/" if page < total else ""
    left = f'<a class="pagination-action" href="{previous}"><span class="pagination-action-icon" aria-hidden="true">‹</span></a>' if previous else '<span class="pagination-action disabled"><span class="pagination-action-icon" aria-hidden="true">‹</span></span>'
    right = f'<a class="pagination-action" href="{nxt}"><span class="pagination-action-icon" aria-hidden="true">›</span></a>' if nxt else '<span class="pagination-action disabled"><span class="pagination-action-icon" aria-hidden="true">›</span></span>'
    return f'''<div class="pagination">
    <a id="globalBackToTop" class="pagination-action animated-visibility invisible" href="#top"><span class="pagination-action-icon" aria-hidden="true">↑</span></a>
    {left}
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">{page}<br><div style="display:inline-block;transform:rotate(-28deg);margin:2px 0">-</div><br>{total}</span></div>
    {right}
  </div></div>
    <div class="pagination">
    {left}
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">{page}/{total}</span></div>
    {right}
  </div>'''


def page_html(template: str, cards: list[str], page: int, total: int) -> str:
    first = template.find('<a href="', template.find("post-list-container"))
    matches = list(re.finditer(r'<a href="[^"]+" class="a-block">.*?</a>', template, re.S))
    if first == -1 or not matches:
        raise RuntimeError("pagination card markers missing")
    result = template[:first] + "\n".join(cards) + template[matches[-1].end():]
    result = re.sub(
        r'(<div id="extraContainer" class="extra-container"><div class="toc-wrapper"></div>).*?(<div id="single-column-footer">)',
        lambda m: m.group(1) + pagination_nav(page, total) + "\n    " + m.group(2),
        result,
        count=1,
        flags=re.S,
    )
    url = base.SITE + ("/" if page == 1 else f"/page/{page}/")
    result = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', result, count=1)
    return re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', result, count=1)


def rebuild_pagination(outputs: dict[str, str | None]) -> tuple[int, int]:
    template = outputs["index.html"] or ""
    cards = cards_from(template)
    previous_pages = 1
    for page in range(2, 200):
        source = get_file_at_active_ref(f"page/{page}/index.html")
        if source is None:
            break
        previous_pages = page
        cards.extend(cards_from(source))
    unique_cards: list[str] = []
    seen: set[str] = set()
    for card in cards:
        href = card_href(card)
        if href not in seen:
            seen.add(href)
            unique_cards.append(card)
    cards = unique_cards
    total = 1 + ((max(0, len(cards) - PAGE1_SIZE) + PAGE_SIZE - 1) // PAGE_SIZE)
    outputs["index.html"] = page_html(template, cards[:PAGE1_SIZE], 1, total)
    cursor = PAGE1_SIZE
    for page in range(2, total + 1):
        outputs[f"page/{page}/index.html"] = page_html(template, cards[cursor: cursor + PAGE_SIZE], page, total)
        cursor += PAGE_SIZE
    for page in range(total + 1, previous_pages + 1):
        outputs[f"page/{page}/index.html"] = None
    return len(cards), total


def collect_binary_outputs() -> dict[str, bytes]:
    outputs: dict[str, bytes] = {}
    for post in base.POSTS:
        for src, dest in SCREENSHOT_SOURCES[post.slug]:
            if not src.exists():
                raise RuntimeError(f"screenshot source missing: {src}")
            outputs[f"images/posts/{post.slug}/{dest}"] = src.read_bytes()
    return outputs


def refresh_manifest(outputs: dict[str, str | None], binary_outputs: dict[str, bytes]) -> None:
    manifest_path = f"tasks/{base.MANIFEST_NAME}"
    manifest_files = sorted({path for path, content in outputs.items() if content is not None} | set(binary_outputs.keys()) | {manifest_path})
    outputs[manifest_path] = json.dumps(manifest_files, ensure_ascii=False, indent=2)


FORBIDDEN = [
    "B站", "bilibili", "Bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主",
    "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅", "投币", "收藏", "下期", "关注", "欢迎收看", "感谢大家", "三连", "BV1",
]


def validate(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], card_count: int, total_pages: int) -> None:
    text_outputs = {path: content for path, content in outputs.items() if content is not None}
    _base_validate(text_outputs)
    failures: list[str] = []
    for post in base.POSTS:
        article = outputs[f"2026/{post.slug}/index.html"] or ""
        cover = outputs[f"images/posts/{post.slug}/cover.svg"] or ""
        for word in FORBIDDEN:
            if word in article or word in cover:
                failures.append(f"{post.slug}: forbidden wording {word}")
        if post.slug == SLUG_SKILLS and "https://github.com/mattpocock/skills" not in article:
            failures.append("Matt Pocock Skills GitHub link missing")
        for _, dest in SCREENSHOT_SOURCES[post.slug]:
            remote_path = f"images/posts/{post.slug}/{dest}"
            if remote_path not in binary_outputs:
                failures.append(f"{post.slug}: missing binary screenshot {dest}")
            if f"/{remote_path}" not in article:
                failures.append(f"{post.slug}: article does not reference {dest}")
        if article.count('<figure class="post-figure">') != len(SCREENSHOT_SOURCES[post.slug]):
            failures.append(f"{post.slug}: figure count mismatch")
        if post.slug == SLUG_RENT and '<figure class="post-figure">' in article:
            failures.append("rent article should not contain source screenshots")
    all_hrefs: list[str] = []
    for page in range(1, total_pages + 1):
        path = "index.html" if page == 1 else f"page/{page}/index.html"
        html = outputs.get(path) or ""
        hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', html)
        all_hrefs.extend(hrefs)
        if page == 1 and len(hrefs) != PAGE1_SIZE:
            failures.append(f"homepage card count {len(hrefs)} != {PAGE1_SIZE}")
        if 1 < page < total_pages and len(hrefs) != PAGE_SIZE:
            failures.append(f"{path} card count {len(hrefs)} != {PAGE_SIZE}")
    if len(all_hrefs) != card_count or len(all_hrefs) != len(set(all_hrefs)):
        failures.append("pagination coverage/duplicates failed")
    expected_prefix = base.PINNED_PREFIX + [post.url_path for post in base.POSTS] + [base.PREV_EXISTING_URL]
    home_hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', outputs["index.html"] or "")
    if home_hrefs[: len(expected_prefix)] != expected_prefix:
        failures.append(f"homepage prefix mismatch: {home_hrefs[:len(expected_prefix)]}")
    if "/page/0/" in (outputs["index.html"] or ""):
        failures.append("homepage contains /page/0/")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str | None], binary_outputs: dict[str, bytes]) -> None:
    out_dir = Path("/tmp/video-batch-bv1ut-bv1ee-bv1fx-20260816-output")
    if out_dir.exists():
        import shutil

        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        if content is None:
            continue
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for rel, content in binary_outputs.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(json.dumps({"local_output": str(out_dir), "text_files": len([v for v in outputs.values() if v is not None]), "binary_files": len(binary_outputs), "deleted": len([v for v in outputs.values() if v is None]), "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))


def render_asset_check() -> None:
    from PIL import Image

    out_dir = Path("/tmp/video-batch-bv1ut-bv1ee-bv1fx-20260816-output")
    for post in base.POSTS:
        svg = out_dir / f"images/posts/{post.slug}/cover.svg"
        png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(svg), "--out", str(png)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe or png.stat().st_size < 4096:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")
        for _, dest in SCREENSHOT_SOURCES[post.slug]:
            image_path = out_dir / f"images/posts/{post.slug}/{dest}"
            img = Image.open(image_path).convert("RGB")
            if img.width < 1000 or img.height < 600:
                raise RuntimeError(f"screenshot dimensions too small: {post.slug}/{dest}: {img.size}")
            if image_path.stat().st_size < 20_000:
                raise RuntimeError(f"screenshot file unexpectedly small: {post.slug}/{dest}")


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    for path, content in sorted(binary_outputs.items()):
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": base64.b64encode(content).decode("ascii"), "encoding": "base64"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = base.run_gh(["-X", "POST", base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = base.run_gh(
        ["-X", "POST", base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish video-derived articles 2026-08-16", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    base.run_gh(["-X", "PATCH", base.endpoint(f"git/refs/heads/{base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def remote_file(path: str, commit_sha: str) -> str:
    data = base.run_gh([base.endpoint(f"contents/{quote(path, safe='/')}?ref={commit_sha}")])
    return base64.b64decode(data["content"]).decode("utf-8")


def verify_remote_publish(commit_sha: str, card_count: int, total_pages: int, binary_outputs: dict[str, bytes]) -> None:
    tree = base.run_gh([base.endpoint(f"git/trees/{commit_sha}?recursive=1")])["tree"]
    paths = {entry["path"] for entry in tree}
    if any("__pycache__" in path for path in paths):
        raise RuntimeError("remote tree includes __pycache__")
    cards: list[str] = []
    for page in range(1, total_pages + 1):
        path = "index.html" if page == 1 else f"page/{page}/index.html"
        if path not in paths:
            raise RuntimeError(f"remote pagination page missing: {path}")
        cards.extend(re.findall(r'<a href="([^"]+)" class="a-block">', remote_file(path, commit_sha)))
    if len(cards) != card_count or len(cards) != len(set(cards)):
        raise RuntimeError("remote pagination coverage failed")
    for post in base.POSTS:
        article_path = f"2026/{post.slug}/index.html"
        if article_path not in paths:
            raise RuntimeError(f"remote article missing: {article_path}")
        article = remote_file(article_path, commit_sha)
        if post.title not in article:
            raise RuntimeError(f"remote article title missing: {post.slug}")
        for word in FORBIDDEN:
            if word in article:
                raise RuntimeError(f"remote forbidden wording in {post.slug}: {word}")
    for remote_path, local_bytes in binary_outputs.items():
        if remote_path not in paths:
            raise RuntimeError(f"remote image missing: {remote_path}")
        data = base.run_gh([base.endpoint(f"contents/{quote(remote_path, safe='/')}?ref={commit_sha}")])
        remote_bytes = base64.b64decode(data["content"])
        if remote_bytes != local_bytes:
            raise RuntimeError(f"remote image bytes mismatch: {remote_path}")


def main() -> None:
    global _active_ref
    for attempt in range(3):
        ref = base.get_ref()
        _active_ref = ref
        base.get_file = get_file_at_active_ref
        base.update_home = update_home_after_pinned
        outputs = base.collect_outputs()
        binary_outputs = collect_binary_outputs()
        card_count, total_pages = rebuild_pagination(outputs)
        refresh_manifest(outputs, binary_outputs)
        validate(outputs, binary_outputs, card_count, total_pages)
        write_outputs(outputs, binary_outputs)
        render_asset_check()
        if base.get_ref().commit_sha != ref.commit_sha:
            continue
        try:
            commit_sha = create_commit(outputs, binary_outputs, ref)
        except RuntimeError as exc:
            if attempt < 2 and "Reference update failed" in str(exc):
                time.sleep(2)
                continue
            raise
        verify_remote_publish(commit_sha, card_count, total_pages, binary_outputs)
        print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "cards": card_count, "pages": total_pages, "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))
        return
    raise RuntimeError("remote reference changed during all attempts")


if __name__ == "__main__":
    main()
