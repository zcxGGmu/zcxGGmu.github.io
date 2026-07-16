from pathlib import Path
from urllib.parse import quote
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
import html
import re
import xml.etree.ElementTree as ET

ROOT = Path('/tmp/hermes-video-publish')
SLUG = 'wealth-freedom-time-business-model-security-trap'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
TITLE = '财富自由的第一性原理：时间、注意力与个人商业模式'
DESC = '财富自由不是拥有花不完的钱，而是不再为了生活必需出售时间。真正拉开人与人距离的，是对时间、注意力、复利、元认知和个人商业模式的理解。'
DATE = '2026-07-16'
PUB_DT = datetime(2026, 7, 16, 9, 58, tzinfo=timezone(timedelta(hours=8)))
PUB_RSS = format_datetime(PUB_DT)
CATEGORY = '财富认知'
SERIES = '财富自由'
TAGS = ['财富自由', '时间', '注意力', '复利', '元认知', '安全感', '个人商业模式', '李笑来', '财富自由之路', '投资自己']
READING_MIN = 14
COVER = f'/images/posts/{SLUG}/cover.svg'
OLDER_URL = '/2026/third-era-dividend-industrial-chain-engineer-globalization/'
OLDER_TITLE = '中国第三次时代红利：产业链、工程师与出海重估'

ARTICLE_HTML = r'''
<p>很多人拼尽全力工作，早出晚归，牺牲休息，牺牲陪伴，牺牲兴趣，可银行卡里的余额依然增长缓慢。于是问题就出现了：为什么已经这么努力，结果却没有明显改变？原因往往不是体力不够，也不是单纯智力不够，而是大脑里对“财富”这两个字的底层定义出了问题。</p>

<p>财富自由并不是拥有花不完的钱，也不是账户里必须有一千万或一个亿。更准确的定义是：从此不再为了满足生活必需而出售自己的时间。关键词不是钱，而是时间。财富自由的本质，是时间自由。</p>

<h2 id="freedom-definition">一、财富自由的核心不是钱，而是不再被迫出售时间</h2>

<p>一个人即使年薪百万，只要停止工作收入就立刻归零，只要每天仍然必须忍受并不喜欢的工作来换取生存资源，那么本质上仍然是时间的囚徒。表面上拥有高收入，底层结构却仍然没有摆脱“以时间换钱”。</p>

<p>真正自由的状态，是早晨睁开眼时，首先想到的不是“必须去完成那个讨厌的项目”，而是“今天要把注意力放到什么有价值的事情上”。这种选择权，才是财富自由真正要解决的问题。</p>

<p>因此，财富自由不是某个数字，而是一套个人操作系统。它要求重新理解时间、注意力、复利、选择、成长和风险。钱只是结果，真正决定结果的是系统。</p>

<h2 id="individual-business-model">二、每个人都是个体商人，出售时间的方式决定身价</h2>

<p>每个人本质上都是一个个体商人，都在出售自己的时间。差别在于，不同的人出售时间的方式完全不同，由此决定了收入天花板。</p>

<p>第一种商业模式，是一份时间卖一次。上班一天，获得一天工资；请假一天，这笔钱就没有了。大多数人都处在这个模式中。它最大的问题是天花板极低，因为一个人的精力和时间有限，一天只有二十四小时，再拼命也只是和生活打一场消耗战。</p>

<p>这种模式里也会有高收入者，例如顶尖医生、律师、专家，他们通过提高单位时间价格获得更高收入。但只要收入仍然强依赖本人持续工作，就无法摆脱“不干就没钱”的结构。</p>

<h2 id="sell-time-many-times">三、更高一级的模式：一份时间卖很多次</h2>

<p>第二种商业模式，是一份时间卖很多次。写书、做课程、做内容、开发软件、打造工具，都属于这种逻辑。前期投入一段时间完成作品，之后作品可以反复被销售、被传播、被使用。</p>

<p>这意味着一个人开始从时间零售，进入时间批发。互联网之所以给普通人带来巨大机会，就是因为它极大降低了复制个人时间的成本。一个人的思想、经验、审美、技能和作品，可以通过网络被多次交付，而不是只能在一个时间点服务一个对象。</p>

<p>这也是内容、软件、知识产品和数字工具的价值所在。它们让个人有机会脱离“每天卖一天”的模式，把一次投入变成长期资产。</p>

<h2 id="buy-others-time">四、最高级的模式：买入别人的时间再卖出去</h2>

<p>第三种商业模式，是买入别人的时间，再把这些时间组织成产品或服务卖给市场。这是创业者和投资者的游戏。当一个人雇佣他人为自己工作，本质上就是用金钱购买他人的时间，再通过组织、产品、品牌和市场，把这些时间创造的价值以更高价格出售。</p>

<p>这并不必然是剥削，也可以是协作。关键在于，组织者是否能创造出比单个劳动者更大的系统价值。如果组织能力足够强，所有参与者的时间都会被放进一个更有效率的结构里。</p>

<p>真正的富人看起来常常更从容，是因为他们已经完成了从劳动力逻辑到资本与组织逻辑的跨越。他们不再只出售自己的时间，而是在设计让时间持续创造价值的系统。</p>

<h2 id="security-trap">五、安全感陷阱：最稳定的东西，可能最限制成长</h2>

<p>道理并不复杂，但真正做到的人很少。最大的阻碍，是“追求安全感”的陷阱。人类大脑天然追求安全感，在远古环境中，这种本能可以帮助人活下来。但在现代社会，过度追求百分之百的安全，反而会成为进步的最大阻力。</p>

<p>很多人宁愿拿着几千块钱的固定工资，在重复和抱怨里消耗自己，也不愿尝试新的可能。原因不是不知道现状不好，而是那份工资提供了即时、确定、熟悉的安全感。离开熟悉轨道，探索未知，大脑会本能地产生恐惧。</p>

<p>可是财富增值往往发生在不确定的边缘。想获得非凡回报，首先必须学会和不安全感相处。安全感不是不能要，而是不能把安全感当成最高原则。过度安全，常常意味着主动放弃成长空间。</p>

<h2 id="compound-interest">六、复利的困难在于前期太平缓，平缓到让人怀疑人生</h2>

<p>复利是财富自由路径中最重要的概念之一。每天进步 1%，一年后会出现巨大差距；每天退步 1%，一年后几乎归零。这个模型并不难懂，难的是坚持到曲线真正抬头。</p>

<p>复利曲线在前期极其平缓，平缓到让人怀疑人生。很多人努力了一段时间，发现生活没有立刻变好，收入没有立刻上升，能力没有立刻显性化，于是就放弃了。他们没有意识到，真正的爆发点通常在很长一段“看不见回报”的积累之后。</p>

<p>财富自由不是一个动作，而是一个过程，更是一种长期修养。它要求一个人在正确方向上持续积累，让时间成为朋友，而不是每天用短期反馈否定长期逻辑。</p>

<h2 id="attention">七、注意力比时间更稀缺，时间又比金钱更重要</h2>

<p>很多人愿意花两个小时排队领一点赠品，愿意为了省一点车费在寒风中等半小时公交，却不愿认真计算自己失去了什么。在他们眼里，钱最重要，时间很廉价。但真相恰好相反：钱丢了可以再赚，时间流逝就不会回来。</p>

<p>比时间更高级的，是注意力。一个人每天真正可控、清醒、能用于创造价值的注意力非常有限。社交网络、情绪化内容、八卦新闻、无意义争吵，都在不断收割注意力。当注意力被免费交出去，未来也在被透支。</p>

<p>在信息过载时代，谁能守住注意力，谁就守住了最宝贵的财富。财富自由首先不是赚钱技巧，而是注意力管理能力。注意力投向哪里，人生就会长成什么样。</p>

<h2 id="metacognition">八、元认知：对自己的思考过程进行思考</h2>

<p>提升单位时间价值，需要成为元认知高手。元认知，就是对自己的思考过程进行思考。比如，当一个人准备发火时，脑子里能出现另一个声音提醒自己：现在的愤怒只是自尊被触碰，并不会帮助解决问题。这就是元认知在发挥作用。</p>

<p>拥有高阶元认知能力的人，会持续监控自己的行为和决策。他们不会轻易被情绪带走，也不会随波逐流。他们会不断追问：现在这个动作，对长期目标有帮助吗？我相信的观念是真的，还是只是为了让自己舒服而编造的解释？</p>

<p>平庸的根源，常常不是不努力，而是大脑里缺乏清晰、准确、必要的概念，以及这些概念之间的连接。没有概念，就无法识别问题；没有连接，就无法形成系统。元认知的作用，就是不断校正这套系统。</p>

<h2 id="real-diligence">九、真正的勤奋不是身体疲惫，而是持续处理高难度问题</h2>

<p>很多人把身体上的劳累误认为勤奋。每天忙到很晚，做大量重复性工作，于是觉得自己已经尽力。但如果这些动作难度很低，只是在回避真正困难的思考，那并不是真正的勤奋。</p>

<p>真正的勤奋，是脑力上的持续投入，是敢于面对那些让人头痛、复杂、模糊、短期没有答案的问题。重复低难度动作，有时候只是懒惰的另一种形式，因为它让人感觉自己很忙，却不必面对真正改变命运的问题。</p>

<p>所以，想要提升身价，不能只问自己有没有努力，还要问努力是否发生在高价值、高难度、可积累的方向上。错误方向上的勤奋，可能只是更快地消耗生命。</p>

<h2 id="slow-is-fast">十、快是慢的结果，捷径往往是最远的路</h2>

<p>很多人最关心的问题是：怎样才能快点赚钱？但真正有效的答案往往是：学会慢。快是慢的结果。当一个人在正确方向上积累足够久，加速会自然发生。</p>

<p>总想走捷径的人，常常走上最远的路。因为他们不断切换方向，不断追逐短期刺激，不断抛弃还没有进入复利阶段的积累。结果看起来一直在行动，实际上始终没有形成资产。</p>

<p>慢并不是拖延，而是愿意在正确路径上承受前期没有反馈的平淡。能穿越平淡期的人，才可能等到复利抬头。</p>

<h2 id="invest-yourself">十一、投资自己，比消费更能改变命运</h2>

<p>财富自由之路的第一步，是学会投资。这里的投资不只是买股票，更重要的是投资自己。很多人愿意花几千块买一件名牌衣服，却不愿花几百块买一本好书、一门课程或一次真正能提升自己的训练，这就是逻辑错位。</p>

<p>衣服会贬值，情绪消费会消失，但知识、技能、判断力和表达能力会随着时间产生复利。一个人真正的资本，也不只是钱。资本至少包括三件事：资金、资金可使用的期限，以及投资智慧。其中最容易被忽视的，是期限。</p>

<p>即使只有一万元，如果能给它二十年的成长时间，也可能比急于求成的百万资金更有力量。投资世界中最难的不是看见机会，而是拥有足够的耐心和智慧，把正确逻辑长期拿住。</p>

<h2 id="choice">十二、选择的权重大于努力，不选也是一种选择</h2>

<p>选择的权重远高于努力。如果一个人在没落行业里拼命挣扎，回报率往往注定偏低。真正重要的是能否基于社会底层逻辑，对未来方向形成判断。</p>

<p>这种判断不是算命，而是理解长期趋势：技术是否会持续进步？人类对更好生活的追求是否会持续？哪些行业代表未来，哪些行业只是在消耗存量？如果相信这些长期逻辑，就会自然关注那些能承载未来的技术、公司和能力。</p>

<p>很多人不敢选择，是因为害怕承担后果。但不选也是选择，而且往往是最坏的选择。停留在原地，看似没有风险，实则把人生交给环境和惯性。</p>

<h2 id="independent-thinking">十三、特立独行且正确：孤独是早期判断的代价</h2>

<p>通往财富自由的路上，最大的阻碍往往来自周围环境。亲戚朋友可能会劝你安稳一点，别做梦，别折腾。这些声音并不一定恶意，但它们通常代表旧系统的安全感。</p>

<p>真正需要的是“特立独行且正确”。重点不只是特立独行，而是正确。为了不同而不同，只是非主流；基于深度思考，发现大众尚未发现的真相，并且这个真相确实成立，才可能拥有超越众人的机会。</p>

<p>这种状态注定孤独。很多积累在早期都不被理解，就像竹子最初几年只长出几厘米，真正的工作却发生在地下：根系已经延伸很远。人生积累也一样，表面沉默的时期，可能正是根系生长的时期。</p>

<h2 id="seven-years">十四、七年一辈子：任何时候开始都不晚</h2>

<p>如果已经三十岁、四十岁，是否太晚？并不晚。一个人彻底掌握一项新技能，或真正进入一个新领域，大约需要一段完整周期。用“七年一辈子”的视角看，一个人如果能活到八十岁，其实拥有好几辈子可以重塑自己。</p>

<p>这意味着，每个人都可以开启第二人生、第三人生。关键不在年龄，而在是否愿意清理大脑中陈旧发霉的观念，换上一套新的固件。</p>

<p>真正可怕的不是开始太晚，而是一直用旧观念解释新世界。只要操作系统不升级，再多努力也只是在旧框架里打转。</p>

<h2 id="responsibility">十五、停止抱怨，拿回人生掌控权</h2>

<p>抱怨是最没有产出的心理活动。当一个人不断抱怨环境、老板、命运时，本质上是在把人生掌控权交给外界。追求财富自由的人，必须成为权责主义者。</p>

<p>权责主义并不是否认外部困难，而是无论发生什么，都先问自己能做什么、该承担什么、下一步如何调整。这听起来残酷，却是变强的唯一路径。因为只有把责任收回自己手中，行动才重新变得可能。</p>

<p>财富不是最终目的，而是工具。它让人能更有尊严地活着，有能力保护所爱的人，有自由选择真正热爱的生活方式。如果生命里只剩下钱，人仍然贫穷。真正的富有，是内心的从容和淡定。</p>

<h2 id="act-as-free">十六、假装已经财富自由：用更自由的心态做更理性的决策</h2>

<p>“假装已经实现财富自由”并不是让人挥霍，而是在心态上提前进入更自由的状态。当一个人假装自己不再为钱恐慌时，决策会更理性，不会为了眼前小利放弃长期发展，也不会因为外界一句评价就惶恐不安。</p>

<p>这种心态会形成良性循环。当一个人开始像自由的人那样思考，就会像自由的人那样行动；当行动越来越接近自由，真正的自由也更容易出现。</p>

<p>现实生活当然有房贷、车贷、孩子教育和家庭责任。财富自由不是逃避责任，而是在承担责任的同时，给未来留下一粒种子。每天哪怕只抽出一个小时学习、写作、研究行业、打磨作品，也是在为“卖很多次”的资产积累第一块砖。</p>

<h2 id="growth">十七、成长才是刚需，财富只是副产品</h2>

<p>如果只能用一句话概括财富自由之路，那就是：成长才是刚需。财富只是成长的副产品。一味盯着钱，钱会跑得很快；盯着自己的成长，让自己越来越值钱，钱反而会追上来。</p>

<p>需要被格式化的旧观念很多：赚钱是可耻的；这辈子就这样了；机会肯定轮不到我；我没资源所以没办法。这些话像脑子里的病毒，会不断削弱行动力。新的观念则是：赚钱是创造价值的体现；只要方法正确，人人都可以进步；机会属于有准备的大脑。</p>

<p>真正改变人生的，不是读过多少道理，而是能否把知识内化成行动。很多高学历者困在知识牢笼里，理论很多，成果很少；也有一些学历普通的人，因为在实践中悟出了正确逻辑，反而完成财富跃迁。差别就在于，知识是否被转化成行动。</p>

<h2 id="conclusion">十八、结论：财富自由给清醒、耐心、敢升级自己的人</h2>

<p>财富自由从来不是给最聪明的人准备的，而是给最清醒、最有耐心、最敢对自己下狠手的人准备的。清醒，是看清自己到底在出售什么；耐心，是愿意穿越复利曲线最平缓的阶段；下狠手，是敢于清理旧观念，守住注意力，持续升级元认知。</p>

<p>每一次艰难选择，都可以问自己：这是在追求安全感，还是在追求成长？每一次想要刷手机、逃避复杂问题、回到熟悉舒适区时，也可以问自己：这是在浪费注意力，还是在投资未来？</p>

<p>财富自由不是一夜暴富，也不是某个神奇技巧。它是一套长期系统：重新定义时间，守护注意力，升级个人商业模式，理解复利，投资自己，选择未来方向，并持续把认知转化成行动。真正的自由，就从这套系统开始。</p>
'''


def esc(s):
    return html.escape(s, quote=True)


def term_url(kind, term):
    return f'/{kind}/{quote(term)}/'


def meta_links():
    cat = f'<a href="{term_url("categories", CATEGORY)}">{esc(CATEGORY)}</a>'
    tag_links = '&nbsp;'.join(f'<a href="{term_url("tags", t)}">{esc(t)}</a>' for t in TAGS)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tag_links}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {READING_MIN} min'


def build_toc(body):
    links = []
    for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body):
        links.append(f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>')
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + ''.join(links) + '</nav></div></div>'


def make_cover():
    d = ROOT / 'images/posts' / SLUG
    d.mkdir(parents=True, exist_ok=True)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#111827"/>
      <stop offset="0.48" stop-color="#1e3a8a"/>
      <stop offset="1" stop-color="#f59e0b"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="14" flood-color="#000" flood-opacity="0.34"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.16" stroke="#fff" fill="none">
    <path d="M130 720 C360 560 520 630 720 455 C925 275 1110 335 1480 130" stroke-width="8"/>
    <path d="M120 610 C360 500 525 520 760 390 C980 268 1170 270 1490 80" stroke-width="4"/>
  </g>
  <g filter="url(#shadow)">
    <rect x="190" y="512" width="220" height="170" rx="18" fill="#bfdbfe"/>
    <rect x="460" y="442" width="220" height="240" rx="18" fill="#93c5fd"/>
    <rect x="730" y="352" width="220" height="330" rx="18" fill="#fde68a"/>
    <rect x="1000" y="252" width="220" height="430" rx="18" fill="#fbbf24"/>
    <path d="M260 590 C430 535 585 475 745 395 C920 310 1080 245 1295 160" fill="none" stroke="#fef3c7" stroke-width="18" stroke-linecap="round"/>
    <circle cx="1295" cy="160" r="46" fill="#facc15"/>
  </g>
  <text x="110" y="160" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="66" font-weight="800">财富自由的第一性原理</text>
  <text x="114" y="240" fill="#dbeafe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">时间 · 注意力 · 复利 · 个人商业模式</text>
  <g fill="#111827" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="800">
    <text x="238" y="610">时间</text>
    <text x="502" y="565">注意力</text>
    <text x="786" y="500">复利</text>
    <text x="1038" y="435">自由</text>
  </g>
</svg>'''
    (d / 'cover.svg').write_text(svg, encoding='utf-8')


def build_article_page():
    template = (ROOT / OLDER_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    head = template[:template.find('<article class="post">')]
    tail = template[template.find('</article>', template.find('<article class="post">')) + len('</article>'):]
    head = re.sub(r'<title>.*?</title>', f"<title>{esc(TITLE)} - zcxGGmu's Blog</title>", head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(DESC)}">', head)
    head = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{esc(FULL_URL)}">', head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(TITLE)}">', head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(DESC)}">', head)
    head = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{esc(FULL_URL)}">', head)
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{COVER}')"><div class="post-title">{esc(TITLE)}<div class="post-subtitle">{esc(DESC)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links()}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{ARTICLE_HTML}</div></div><nav class="post-pagination"><a class="newer-posts">下一篇<br>没有更新的文章</a><a class="older-posts" href="{OLDER_URL}">上一篇<br>{esc(OLDER_TITLE)}</a></nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(ARTICLE_HTML), tail, flags=re.S)
    out = ROOT / '2026' / SLUG / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head + article + tail, encoding='utf-8')
    older = ROOT / OLDER_URL.strip('/') / 'index.html'
    txt = older.read_text(encoding='utf-8')
    txt = re.sub(r'<a class="newer-posts">下一篇<br>没有更新的文章</a>', f'<a class="newer-posts" href="{URL_PATH}">下一篇<br>{esc(TITLE)}</a>', txt)
    older.write_text(txt, encoding='utf-8')


def home_card(url, title, desc, cover, minutes):
    return f'''<a href="{url}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(title)}</div>
            <div class="post-item-summary">{esc(desc)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {minutes} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{cover}')"></div></div>
        </div>
      </div>
    </a>'''


def update_home():
    p = ROOT / 'index.html'
    txt = p.read_text(encoding='utf-8')
    if URL_PATH not in txt:
        marker = f'<a href="{OLDER_URL}" class="a-block">'
        pos = txt.find(marker)
        if pos == -1:
            raise RuntimeError('older homepage marker not found')
        txt = txt[:pos] + home_card(URL_PATH, TITLE, DESC, COVER, READING_MIN) + '\n' + txt[pos:]
    p.write_text(txt, encoding='utf-8')


def update_rss():
    p = ROOT / 'index.xml'
    txt = p.read_text(encoding='utf-8')
    txt = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{PUB_RSS}</lastBuildDate>', txt)
    item = f'''<item>
<title>{esc(TITLE)}</title>
<link>{FULL_URL}</link>
<guid>{FULL_URL}</guid>
<pubDate>{PUB_RSS}</pubDate>
<description>{esc(DESC)}</description>
</item>
'''
    if FULL_URL not in txt:
        txt = txt.replace('<item>', item + '<item>', 1)
    p.write_text(txt, encoding='utf-8')


def update_archive():
    p = ROOT / 'archive/index.html'
    txt = p.read_text(encoding='utf-8')
    if URL_PATH not in txt:
        txt = re.sub(r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>', lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + 1} 篇</span>', txt, count=1)
        item = f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{URL_PATH}">{esc(TITLE)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(CATEGORY)}</span></span>
      </div> '''
        marker = f'<div style="padding:8px 0;font-size:15px">\n        <span style="color:#999">2026-07-12</span>&nbsp;\n        <a href="{OLDER_URL}">'
        pos = txt.find(marker)
        if pos == -1:
            raise RuntimeError('archive marker not found')
        txt = txt[:pos] + item + txt[pos:]
    p.write_text(txt, encoding='utf-8')


def list_page(kind, term, title_prefix=None, emoji=''):
    d = ROOT / kind / term
    d.mkdir(parents=True, exist_ok=True)
    p = d / 'index.html'
    if p.exists():
        txt = p.read_text(encoding='utf-8')
        if URL_PATH not in txt:
            txt = re.sub(r'共 (\d+) 篇文章', lambda m: f'共 {int(m.group(1)) + 1} 篇文章', txt, count=1)
            item = f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''
            insert = txt.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
            if insert == -1:
                insert = txt.find('</div></div></div>')
            txt = txt[:insert] + item + txt[insert:]
        p.write_text(txt, encoding='utf-8')
        return
    label = f'{title_prefix}: {term}' if title_prefix else term
    h1 = f'{emoji} {term}' if emoji else label
    txt = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="https://zcxggmu.github.io/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Noto+Sans+SC:wght@400;500;700&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons&amp;display=swap"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p><div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> </div></div></div><script src="/js/journal.js"></script></body></html>'''
    p.write_text(txt, encoding='utf-8')


def update_index_count(kind, term):
    p = ROOT / kind / 'index.html'
    if not p.exists():
        return
    txt = p.read_text(encoding='utf-8')
    href = f'/{kind}/{quote(term)}/'
    if href in txt:
        pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(term)}<span style="color:#999[^>]*>\()(\d+)(\)</span></a>)')
        txt = pattern.sub(lambda m: f'{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}', txt, count=1)
    else:
        if kind == 'tags':
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">(1)</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">(1)</span></a>\n'
        marker = '</div></div></div>'
        pos = txt.find(marker)
        if pos == -1:
            raise RuntimeError(f'{kind} index insertion marker not found')
        txt = txt[:pos] + item + txt[pos:]
    p.write_text(txt, encoding='utf-8')


def update_taxonomy():
    list_page('categories', CATEGORY, '分类')
    update_index_count('categories', CATEGORY)
    list_page('series', SERIES, None, '📚')
    update_index_count('series', SERIES)
    for tag in TAGS:
        list_page('tags', tag, '标签', '🏷️')
        update_index_count('tags', tag)


def validate():
    failures = []
    article = ROOT / '2026' / SLUG / 'index.html'
    txt = article.read_text(encoding='utf-8')
    forbidden = ['B站', 'bilibili', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主', '这期', '本期', '作者说', '他提到', '观看', '点赞', '下期', '欢迎收看', '感谢', '订阅', '老铁', '半亩野草', '投币', '一键三连']
    for w in forbidden:
        if w in txt:
            failures.append(f'forbidden word in article: {w}')
    for concept in ['财富自由', '时间自由', '个人商业模式', '一份时间卖一次', '一份时间卖很多次', '安全感陷阱', '复利', '注意力', '元认知', '成长才是刚需']:
        if concept not in txt:
            failures.append(f'missing concept: {concept}')
    for p in [article, ROOT / 'index.html', ROOT / 'index.xml', ROOT / 'archive/index.html', ROOT / 'categories' / CATEGORY / 'index.html', ROOT / 'series' / SERIES / 'index.html']:
        if not p.exists():
            failures.append(f'missing {p}')
    home = (ROOT / 'index.html').read_text(encoding='utf-8')
    links = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)
    expected = ['/2026/codeinsights-local-first-agent-workbench/', '/2026/what-you-need-to-learn-from-claw-code-repo/', '/2026/gaojingqi-investment-system/', '/2026/ai-revolution-permanent-underclass-career-selection/', '/2026/live-longer-than-earn-fast-investment-infinite-game/', URL_PATH, OLDER_URL]
    if links[:7] != expected:
        failures.append(f'homepage order mismatch: {links[:7]}')
    older = (ROOT / OLDER_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    if f'href="{URL_PATH}"' not in older:
        failures.append('older article does not link to new article')
    try:
        ET.parse(ROOT / 'index.xml')
    except Exception as e:
        failures.append(f'rss xml parse failed: {e}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print('validation passed')


def main():
    make_cover()
    build_article_page()
    update_home()
    update_rss()
    update_archive()
    update_taxonomy()
    validate()
    print('published local files for', FULL_URL)


if __name__ == '__main__':
    main()
