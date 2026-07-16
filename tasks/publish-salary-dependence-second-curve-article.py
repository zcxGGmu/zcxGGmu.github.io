from pathlib import Path
from urllib.parse import quote
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
import html
import re
import xml.etree.ElementTree as ET

ROOT = Path('/tmp/hermes-video-publish')
SLUG = 'salary-dependence-second-curve-income-structure-risk'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
TITLE = '死工资才是普通人最大的风险：第二曲线如何重写收入结构'
DESC = '如果明天被降薪 30%，存款能撑几个月？真正拉开普通人差距的，不只是能力，而是收入结构、第二曲线和长期现金流。'
DATE = '2026-07-16'
PUB_DT = datetime(2026, 7, 16, 16, 45, tzinfo=timezone(timedelta(hours=8)))
PUB_RSS = format_datetime(PUB_DT)
CATEGORY = '财富认知'
SERIES = '财富自由'
TAGS = ['死工资', '第二曲线', '副业', '收入结构', '个人IP', '现金流', '财富自由', '抗风险', '投资增值', '打工人']
READING_MIN = 10
COVER = f'/images/posts/{SLUG}/cover.svg'
OLDER_URL = '/2026/construction-machinery-cycle-domestic-export-tech-upgrade/'
OLDER_TITLE = '工程机械的周期拐点：内需、出海与技术升级的三重共振'

ARTICLE_HTML = r'''
<p>如果明天公司通知你降薪 30%，你手里的存款能撑几个月？这个问题不该被轻轻带过。先不要急着用“我应该还能扛一扛”来安慰自己，先把房贷、车贷、孩子的补习班、父母的医药费、日常开支、保险费用和未来几个月可能出现的意外支出全部摆在桌面上，再问自己一次：哪一样能立刻停掉？</p>

<p>这就是 2026 年普通打工人最需要直面的现实：经济下行周期里，没有哪份工作是真正意义上的铁饭碗。过去让人觉得稳定的岗位、行业和公司，现在都可能重新定价。昨天还拿着高薪的人，今天也可能开始投简历；昨天还觉得副业“不务正业”的人，今天可能忽然发现，那些悄悄构建第二份、第三份收入的人，才是最从容的一群人。</p>

<p>普通人最大的风险，往往不是工资低，而是收入结构太单一。一个人只靠一份工资，就等于把家庭现金流、生活安全感、未来选择权全部押在一个雇主、一家公司、一个岗位、一个行业周期上。只要外部环境稍有变化，安全感就会被迅速收回。</p>

<h2 id="salary-risk">一、只靠工资，不是稳定，而是集中风险</h2>

<p>很多人把工资理解成安全感，因为工资每个月按时到账，数字清楚，节奏稳定，路径熟悉。但这份安全感有一个容易被忽略的前提：它不是自己掌握的，而是别人发给你的。</p>

<p>只要收入完全来自主业，你的生活就高度依赖公司经营状况、行业景气度、部门预算、老板判断和组织调整。你可以努力，可以敬业，可以加班，可以把每一件事做得很好，但只要组织不再需要这个岗位，或公司决定压缩成本，收入就可能被降薪、停发或切断。</p>

<p>这不是悲观，而是现金流结构的事实。房贷不会因为公司裁员而暂停，孩子的教育费用不会因为行业下行而自动降低，父母的医药费更不会等你重新找到工作后再发生。支出是刚性的，工资却是可变的；家庭责任是连续的，雇佣关系却可能中断。这里面的错配，才是普通人真正的脆弱点。</p>

<p>所以，问题不是“要不要认真上班”。主业当然要认真做，它是大多数普通人的第一现金流，也是经验、资源和信用的来源。真正的问题是，能不能在主业之外，为自己长出第二条曲线。</p>

<h2 id="downturn-truth">二、经济下行时，收入结构决定抗风险能力</h2>

<p>在上行周期里，很多问题会被掩盖。行业扩张、公司扩张、岗位扩张，工资和奖金还能一起往上走。一个人只要跟着平台跑，也能感受到增长。但下行周期会把所有结构性问题暴露出来：谁只有单一收入，谁就最先感受到压力；谁提前准备了多元现金流，谁就多一层缓冲。</p>

<p>同样是面对降薪和裁员，有些人会陷入恐慌，因为工资一断，家庭现金流马上断；有些人却能相对从容，因为主业之外还有副业、投资、个人 IP 或其他变现方式。主业照常干，但手里还有第二份、第三份收入，抗风险能力就完全不同。</p>

<p>这就是收入结构的差距。人与人的差距，表面上看是能力差距、学历差距、资源差距，本质上常常是收入结构的差距。只用一个月工作换一个月工资，就是卖一次算一次；能把时间、经验、知识、内容、服务、产品和资本沉淀下来，就可能让同一份时间被卖出不止一次。</p>

<p>这并不意味着每个人都要立刻辞职创业，也不意味着副业一定比主业高贵。真正重要的是：不要让自己只有一种收入来源，不要让家庭生活只靠单点支撑。</p>

<h2 id="second-curve">三、第二曲线不是不务正业，而是安全边际</h2>

<p>很多人对副业的第一反应是“不务正业”。这种判断在过去或许有一定道理，因为稳定工作曾经是社会默认的最优路径。但在今天，只靠一份工资，反而可能是最大的冒险。</p>

<p>主业带来的安全感，是外部给予的，随时可能被收回；第二曲线是自己长出来的，别人很难直接拿走。它可以很小，刚开始甚至赚不到多少钱，但只要方向正确、持续积累，就会逐渐变成自己的现金流、能力栈、影响力和选择权。</p>

<p>第二曲线的意义，不只是多赚一点零花钱，而是改变自己与风险的关系。没有第二曲线时，裁员意味着现金流断裂；有第二曲线时，裁员可能只是主业暂停。没有第二曲线时，降薪 30% 会直接击穿生活预算；有第二曲线时，副业和投资收益至少能提供缓冲。没有第二曲线时，人只能被动接受组织安排；有第二曲线时，人还有主动选择的空间。</p>

<p>一个普通销售，业余时间做内容账号，起初可能会被同事嘲笑。但如果三年后公司裁员，他拿着补偿金离开，而副业收入已经超过主业，每天接广告、带学员、做服务，生活节奏反而更自由，那么当初被认为“不务正业”的事情，就变成了真正的安全垫。</p>

<h2 id="income-structure">四、真正拉开差距的，是收入结构</h2>

<p>工资收入的特点，是线性。一个月工作换一个月工资，停下来就没有。它高度依赖出勤、岗位和组织，是最清晰也最脆弱的现金流。</p>

<p>第二曲线则试图把收入从线性变成多层结构。副业带来第二现金流，投资带来资产性收入，个人 IP 带来信任和复购，公域内容带来陌生流量，私域产品带来长期关系，知识和经验产品化后可以重复交付。它们一开始都很小，但一旦积累起来，就能让时间不再只被卖一次。</p>

<p>“睡着也有钱进账”不是玄学，它背后需要结构：内容已经发布，产品已经沉淀，资产已经配置，客户关系已经建立，系统已经运转。真正的关键不是幻想被动收入，而是先构建能让主动收入持续沉淀的系统。</p>

<p>普通人要改变命运，不能只盯着工资涨幅。工资涨幅当然重要，但它受制于公司预算和行业周期。更重要的是：收入来源能不能从单一变成多元，时间能不能从一次性出售变成多次复用，能力能不能从岗位技能变成市场可交易的产品。</p>

<h2 id="five-problems">五、打通第二曲线，要先回答五个问题</h2>

<p>第二曲线不是随便做点什么，也不是看别人做什么赚钱就跟着冲。它需要系统地回答五个问题。</p>

<p>第一个问题：经济下行时，打工人如何逆势破局？破局不是逃离主业，而是在主业之外建立新杠杆。主业提供现金流和专业积累，第二曲线负责把这些积累外部化、产品化、资产化。</p>

<p>第二个问题：如何抓住市场分化行情，打造多元财富组合？市场不会一直普涨，收入也不会只有工资一种形态。现金储备、稳健投资、权益资产、技能变现、内容资产，都需要按风险承受能力组合起来。单一资产和单一收入一样，都会带来集中风险。</p>

<p>第三个问题：怎样找到投产比高的副业新思路？副业不是越多越好，而是要看投入产出比。普通人时间有限，不能把所有晚上和周末都耗在低单价、低复利、低成长的事情上。优先选择能沉淀能力、案例、客户、内容、产品和信任的方向。</p>

<p>第四个问题：怎样用公域和私域产品构建个人 IP，并形成长期现金流？公域解决被看见，私域解决被信任，产品解决可交付，复购解决长期现金流。个人 IP 的本质不是包装自己，而是持续输出可信价值，让别人知道你能解决什么问题。</p>

<p>第五个问题：如何精准定位核心优势，从 0 到 1 打通闭环？很多人做副业失败，不是因为不努力，而是没有定位。什么人群、什么痛点、什么交付、什么价格、什么转化路径、什么复购机制，如果这些问题没有闭环，努力就会变成自我感动。</p>

<h2 id="personal-ip">六、个人 IP 的价值，是把能力变成可交易资产</h2>

<p>普通人的能力如果只留在公司内部，价值就由公司定价。个人 IP 的意义，是把能力从组织内部拿到市场上重新定价。</p>

<p>一个人会销售，可以把销售经验整理成方法论；懂金融，可以做资产配置教育；会写作，可以做内容服务；懂职场，可以做咨询和陪跑；擅长某个细分行业，可以输出行业洞察。关键不是“我有什么名气”，而是“我能为谁解决什么具体问题”。</p>

<p>个人 IP 并不等于每天刷存在感，也不等于把生活变成表演。真正有价值的 IP，是稳定地提供判断、方法、案例和结果。它需要长期积累，需要可信表达，需要真实交付，也需要不断迭代产品。</p>

<p>一旦个人 IP 和产品体系形成闭环，收入就不再只来自上班时间。内容可以持续带来新客户，案例可以增强信任，产品可以重复销售，服务可以提高客单价，私域关系可以形成长期复购。这才是第二曲线真正有价值的地方。</p>

<h2 id="investment-growth">七、副业之外，还要有财富增值能力</h2>

<p>只做副业，不做财富增值，也容易掉进另一个陷阱：收入多了，但钱依然留不住。第二曲线不是只靠辛苦多赚一份钱，而是要把新增现金流转化为更稳固的资产结构。</p>

<p>投资增值的第一步不是追求暴富，而是建立基本的财务秩序：应急现金、保险保障、债务管理、长期资产配置、风险预算。没有现金垫，任何波动都会变成焦虑；没有风险预算，任何投资都可能变成赌博。</p>

<p>市场分化时代，财富组合也不能只押一个方向。普通人需要知道自己哪些钱是保命钱，哪些钱是机会钱，哪些钱可以长期波动，哪些钱绝不能亏损。副业负责增加现金流，投资负责提高资金效率，二者结合，才能真正改善财富结构。</p>

<h2 id="action-efficiency">八、选择质量和行动效率，拉开人生差距</h2>

<p>人和人之间没有绝对的本质差别，但选择的质量和行动的效率，会逐渐拉开巨大差距。</p>

<p>有些人把所有精力都放在抱怨工资、抱怨环境、抱怨公司，却没有建立任何新的收入入口；有些人知道环境无法立刻改变，于是开始做内容、做产品、学投资、建私域、积累案例。三个月看不出差距，一年开始不同，三年后就是完全不同的人生状态。</p>

<p>第二曲线什么时候开始都不算晚，但越早开始，试错成本越低。主业还稳定时开始，心态更稳；收入还没有断时开始，选择更多；家庭现金流还没有紧绷时开始，容错空间更大。等到裁员和降薪已经发生，再被迫启动第二曲线，难度会大很多。</p>

<p>行动不需要一步到位。先梳理自己的核心优势，确定一个细分人群，找到一个具体痛点，做一个最小产品，持续输出内容，积累第一批真实反馈，再逐步优化交付和变现路径。第二曲线不是突然爆发，而是持续复利。</p>

<h2 id="conclusion">九、结论：别把全部安全感押在一份工资上</h2>

<p>工资很重要，但只靠工资很危险。它能解决当下生活，却未必能抵御未来波动；它能提供稳定节奏，却不能保证长期安全；它能让人暂时安心，也可能让人忽视收入结构的脆弱。</p>

<p>真正稳固的安全感，不是来自某家公司永远需要你，而是来自你拥有多种创造现金流的能力：主业能力、副业能力、内容能力、产品能力、投资能力、长期经营关系的能力。主业是第一曲线，第二曲线是选择权，财富增值是加速器。</p>

<p>如果明天被降薪 30%，存款能撑几个月？这个问题的答案，不应该只停留在账户余额里，更应该落实到今天的行动里。现在开始建立第二曲线，重新设计收入结构，可能就是上半生和下半生的分界线。</p>
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
      <stop offset="0.52" stop-color="#7f1d1d"/>
      <stop offset="1" stop-color="#92400e"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="14" flood-color="#000" flood-opacity="0.35"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#fef3c7" stroke-width="4">
    <path d="M95 690 H1505"/>
    <path d="M95 570 H1505"/>
    <path d="M95 450 H1505"/>
    <path d="M95 330 H1505"/>
    <path d="M260 230 V745"/>
    <path d="M540 230 V745"/>
    <path d="M820 230 V745"/>
    <path d="M1100 230 V745"/>
    <path d="M1380 230 V745"/>
  </g>
  <g filter="url(#shadow)">
    <rect x="150" y="455" width="410" height="210" rx="26" fill="#fee2e2"/>
    <rect x="182" y="490" width="190" height="24" rx="12" fill="#991b1b" opacity="0.65"/>
    <rect x="182" y="535" width="300" height="18" rx="9" fill="#7f1d1d" opacity="0.28"/>
    <rect x="182" y="575" width="250" height="18" rx="9" fill="#7f1d1d" opacity="0.22"/>
    <path d="M505 455 L560 510 L505 510 Z" fill="#fecaca"/>
    <path d="M610 625 C735 555 805 580 935 490 C1045 414 1152 394 1324 292" stroke="#fef3c7" stroke-width="18" fill="none" stroke-linecap="round"/>
    <path d="M1306 291 L1342 282 L1331 318" stroke="#fef3c7" stroke-width="18" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="680" cy="605" r="50" fill="#f59e0b"/>
    <circle cx="935" cy="490" r="50" fill="#fbbf24"/>
    <circle cx="1195" cy="365" r="50" fill="#fde68a"/>
  </g>
  <text x="108" y="155" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="66" font-weight="800">死工资才是最大的风险</text>
  <text x="112" y="238" fill="#fed7aa" font-family="Noto Sans SC, PingFang SC, Arial" font-size="40" font-weight="700">第二曲线 · 收入结构 · 长期现金流</text>
  <text x="114" y="315" fill="#fee2e2" font-family="Noto Sans SC, PingFang SC, Arial" font-size="32" font-weight="600">不要把全部安全感押在一份工资上</text>
</svg>'''
    (d / 'cover.svg').write_text(svg, encoding='utf-8')


def build_article_page():
    template_path = ROOT / OLDER_URL.strip('/') / 'index.html'
    template = template_path.read_text(encoding='utf-8')
    start = template.find('<article class="post">')
    end = template.find('</article>', start) + len('</article>')
    if start == -1 or end == -1:
        raise RuntimeError('article template markers not found')
    head = template[:start]
    tail = template[end:]
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
    if URL_PATH not in txt:
        txt = re.sub(r'<a class="newer-posts">下一篇<br>没有更新的文章</a>', f'<a class="newer-posts" href="{URL_PATH}">下一篇<br>{esc(TITLE)}</a>', txt, count=1)
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
        marker = f'<a href="{OLDER_URL}">'
        pos = txt.find(marker)
        if pos == -1:
            raise RuntimeError('archive marker not found')
        start = txt.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
        if start == -1:
            raise RuntimeError('archive insertion point not found')
        txt = txt[:start] + item + txt[start:]
    p.write_text(txt, encoding='utf-8')


def list_page(kind, term, title_prefix=None, emoji=''):
    d = ROOT / kind / term
    d.mkdir(parents=True, exist_ok=True)
    p = d / 'index.html'
    if p.exists():
        txt = p.read_text(encoding='utf-8')
        if URL_PATH in txt:
            return False
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
        return True
    label = f'{title_prefix}: {term}' if title_prefix else term
    h1 = f'{emoji} {term}' if emoji else label
    txt = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="https://zcxggmu.github.io/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Noto+Sans+SC:wght@400;500;700&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons&amp;display=swap"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p><div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> </div></div></div><script src="/js/journal.js"></script></body></html>'''
    p.write_text(txt, encoding='utf-8')
    return True


def update_index_count(kind, term, should_increment):
    p = ROOT / kind / 'index.html'
    if not p.exists():
        return
    txt = p.read_text(encoding='utf-8')
    href = f'/{kind}/{quote(term)}/'
    if href in txt:
        if should_increment:
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
    added = list_page('categories', CATEGORY, '分类')
    update_index_count('categories', CATEGORY, added)
    added = list_page('series', SERIES, None, '📚')
    update_index_count('series', SERIES, added)
    for tag in TAGS:
        added = list_page('tags', tag, '标签', '🏷️')
        update_index_count('tags', tag, added)


def validate():
    failures = []
    article = ROOT / '2026' / SLUG / 'index.html'
    txt = article.read_text(encoding='utf-8')
    forbidden = ['B站', 'bilibili', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主', '这期', '本期', '作者说', '他提到', '观看', '点赞', '下期', '欢迎收看', '感谢', '订阅', '老铁', '评论区', '关注']
    for w in forbidden:
        if w in txt:
            failures.append(f'forbidden word in article: {w}')
    for concept in ['降薪 30%', '房贷', '车贷', '父母的医药费', '第二曲线', '收入结构', '个人 IP', '公域', '私域', '长期现金流']:
        if concept not in txt:
            failures.append(f'missing concept: {concept}')
    h2s = re.findall(r'<h2 id="([^"]+)">', txt)
    tocs = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', txt)
    if h2s != tocs:
        failures.append(f'toc mismatch: h2={h2s}, toc={tocs}')
    required = [
        article,
        ROOT / 'images/posts' / SLUG / 'cover.svg',
        ROOT / 'index.html',
        ROOT / 'index.xml',
        ROOT / 'archive/index.html',
        ROOT / 'categories' / CATEGORY / 'index.html',
        ROOT / 'series' / SERIES / 'index.html',
    ]
    for p in required:
        if not p.exists():
            failures.append(f'missing {p}')
    home = (ROOT / 'index.html').read_text(encoding='utf-8')
    links = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)
    expected = [
        '/2026/codeinsights-local-first-agent-workbench/',
        '/2026/what-you-need-to-learn-from-claw-code-repo/',
        '/2026/gaojingqi-investment-system/',
        '/2026/ai-revolution-permanent-underclass-career-selection/',
        '/2026/live-longer-than-earn-fast-investment-infinite-game/',
        URL_PATH,
        OLDER_URL,
    ]
    if links[:7] != expected:
        failures.append(f'homepage order mismatch: {links[:7]}')
    older = (ROOT / OLDER_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    if f'href="{URL_PATH}"' not in older:
        failures.append('older article does not link to new article')
    rss = (ROOT / 'index.xml').read_text(encoding='utf-8')
    if FULL_URL not in rss:
        failures.append('rss missing full url')
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
