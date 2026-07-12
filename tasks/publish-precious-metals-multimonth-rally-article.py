from pathlib import Path
from urllib.parse import quote
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
import html
import re
import textwrap
import xml.etree.ElementTree as ET
import subprocess

ROOT = Path('/tmp/hermes-video-publish')
SLUG = 'gold-silver-multimonth-rally-secular-bull-market'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
TITLE = '黄金与白银的下一阶段：多月反弹、关键阻力与长期牛市路径'
DESC = '从黄金突破后的历史修正、4000 美元支撑、4400 美元与白银 70 美元阻力，到股金比、情绪指标、矿业股修正类比和未来数年贵金属牛市路径，梳理黄金、白银与矿业股的核心交易框架。'
DATE = '2026-07-12'
PUB_DT = datetime(2026, 7, 12, 15, 18, tzinfo=timezone(timedelta(hours=8)))
PUB_RSS = format_datetime(PUB_DT)
CATEGORY = '投资'
SERIES = '贵金属前沿'
TAGS = ['黄金', '白银', '贵金属', '矿业股', 'GDX', 'GDXJ', '美股', '技术分析', '情绪指标', '投资策略']
READING_MIN = 12
COVER = f'/images/posts/{SLUG}/cover.svg'
OLDER_URL = '/2026/index-investing-middle-age-anxiety-life-investment/'
OLDER_TITLE = '50 岁后开始指数投资：从 3,000 万亏损到走出中年焦虑'

ARTICLE_HTML = r'''
<p>贵金属已经进入一个非常值得重视的位置。黄金和白银经历突破后的第一轮显著修正后，正在酝酿一轮多月级别的反弹。真正的分歧不在于贵金属能不能反弹，而在于反弹是不是已经开始：低点可能已经出现，也可能还需要一次假跌破、一次更低的低点，才会完成最终洗盘。</p>

<p>从黄金自身的历史修正、日线与周线形态、情绪指标、黄金相对标普 500 的走势，再到 GDX、GDXJ 这类矿业股的回撤类比，结论可以归纳为一句话：未来数月，黄金和白银更大概率处在反弹窗口；未来两三年，真正驱动贵金属进入更大级别牛市的力量，可能来自资金从股票市场向黄金和白银的再配置。</p>

<h2 id="setup">一、贵金属已经具备多月反弹的条件</h2>

<p>当前贵金属的核心判断是：市场已经为一轮多月级别反弹做好准备。问题只剩两个场景。</p>

<p>第一个场景，是黄金已经完成阶段低点，接下来以相对温和、稳定的方式向上修复。这个路径更像 2006 年突破后的修正结束，而不是 1973 年那种垂直式上冲。也就是说，反弹可以很强，但不一定会马上进入极端陡峭的直线拉升。</p>

<p>第二个场景，是眼下这轮刚刚出现的反弹无法持续，随后价格再向下打一轮，形成一个“假新低”。如果这个路径发生，最终低点可能落在 3700 至 3800 美元附近，更具体地说，3700 多美元、接近 50% 回撤的位置会非常关键。那样反而会为后面更有力度的反弹创造条件。</p>

<p>所以，短线低点是否已经出现并不是最重要的问题。更重要的是，无论是现在开始反弹，还是先跌出一个更低的低点，黄金和白银都已经接近一个中期反弹的起点区域。</p>

<h2 id="daily-chart">二、黄金 4000 美元上方的支撑与 4400 美元阻力</h2>

<p>从日线结构看，黄金已经出现反弹，并且至少在最近一周仍然守在 4000 美元上方。这里的意义在于，4000 美元附近成为短期市场能否继续上修的重要观察位。</p>

<p>如果反弹能够持续，黄金下一阶段最重要的阻力大约在 4400 美元。这个位置很可能成为第一道明显压力。无论反弹以哪种方式展开，4400 美元都不是一个可以轻易忽略的价格带。</p>

<p>但如果当前反弹只是短暂修复，随后价格重新走弱，那么黄金可能会向 3720 美元附近靠拢。这个区域对应大约 50% 回撤。一旦市场先向下完成这次假跌破，再从 3700 多美元反身向上，那么从 3700 到 4400 美元的反弹空间反而更可观。</p>

<p>白银的路径也类似。短期可能先出现一些买盘和反弹，但如果无法站稳，就可能再向下完成一次清洗。中期看，白银的重要阻力大约在 70 美元附近。黄金 4400 美元、白银 70 美元，是未来反弹中最需要重视的两个价格关口。</p>

<h2 id="weekly-hammers">三、周线连续锤子线说明买盘已经出现</h2>

<p>周线结构给出的信号偏积极。黄金最近三周连续出现偏多的锤子线，这说明每次价格被压低后，都有资金在下方承接。连续三根周线级别的锤子线，至少表明市场不再是单边抛售状态。</p>

<p>这并不等于价格一定不会再创新低。技术形态从来不是绝对答案。但它说明下方买盘正在增强，市场已经不再像修正初期那样脆弱。结合 4000 美元上方的短期支撑，黄金已经具备向 4400 美元一带反弹的结构基础。</p>

<p>对于白银而言，逻辑也相同。白银通常波动更大，弹性更高，因此在黄金企稳后，白银可能表现出更强的上冲能力。但白银的关键验证位仍然是 70 美元，突破前要把它当作重要压力，而不是默认已经进入毫无阻力的上升通道。</p>

<h2 id="sentiment">四、情绪指标正在给出中期看多信号</h2>

<p>贵金属市场最值得关注的部分之一，是情绪。情绪指标并不告诉我们精确的日内买点，但它能告诉我们市场是否已经进入过度悲观、容易反身向上的区域。</p>

<p>GLD 相关的情绪指标经过 50 日均线平滑后，已经落到历史上非常重要的位置。回看过去多次类似读数，它们往往出现在黄金重要低点附近，或者出现在最终低点前一两个月。比如 2008 年大跌后的阶段、2016 年低点附近、2018 年重要低点、2022 年低点前后，都出现过类似信号。</p>

<p>这个指标的重要含义是：黄金很可能会迎来一轮质量不错的反弹。需要注意的是，情绪信号可能提前出现。也就是说，它可以告诉我们未来两三个月、三四个月甚至五个月内反弹概率很高，但不一定保证最低点已经在今天出现。</p>

<p>因此，情绪数据支持的是“中期反弹窗口”，而不是“马上满仓追高”。如果黄金还需要一个月左右完成最后一跌，这并不破坏情绪指标的看多含义；相反，那可能是反弹前最后一次把浮筹洗掉的过程。</p>

<h2 id="not-1975">五、这不是 1975 至 1976 年那种深度熊市结构</h2>

<p>判断黄金会不会进入更深级别下跌，不能只看金价本身，还要看黄金相对于股票市场的表现。历史上，贵金属出现特别剧烈的大跌之前，往往先发生过一轮非常巨大的资金迁移：资金从股票市场流向黄金，黄金相对标普 500 出现极端上涨。</p>

<p>1971 至 1974 年、1976 至 1980 年，以及之后若干长期周期中，都出现过资金持续从股票转向黄金的过程。以 1971 至 1974 年为例，黄金相对标普 500 在大约四年内出现过数倍级别的上涨，这种极端迁移为后来的大波动埋下了基础。</p>

<p>而过去几年虽然也出现了资金从股票向黄金的轮动，但时间和幅度都远不如历史上那些大型顶部前的极端阶段。最近这轮黄金相对股票的走强，大致只有两年左右，也没有达到 1970 年代那种夸张幅度。</p>

<p>更重要的是，历史上真正的大级别下跌，通常会先经历明显的顶部构筑过程。比如金价先大幅下跌，再横盘稳定一段时间，随后跌破关键支撑；或者先下跌 40%，再反弹，之后长期缓慢下行。1975 至 1976 年的情况也是先有初步回撤，再横盘数月，最后出现向下破位。</p>

<p>现在的黄金结构并不符合那些大型顶部后的深熊模板。当前更像一次突破后的正常显著修正：时间约五到七个月，幅度约 22% 至 30%。从历史类比看，这种修正更接近牛市中的阶段性回撤，而不是长期顶部后的崩塌。</p>

<h2 id="stock-bear-market">六、真正的大牛市需要股票熊市配合</h2>

<p>要理解未来两三年的贵金属行情，必须把黄金和标普 500 放在一起看。历史上真正强劲的黄金牛市，往往伴随着股票市场进入严重熊市，资金从股票资产中撤出，转向黄金和白银。</p>

<p>从逻辑上讲，如果没有股票市场的明显压力，就很难形成贵金属长期牛市中最强的一段。因为推动黄金和白银加速上涨的，不只是商品自身供需，也包括资产配置层面的资金迁移。当股票市场下跌、风险偏好收缩、长期牛市结束时，资金需要寻找新的避险和保值方向，贵金属就会成为重要承接资产。</p>

<p>这也说明，当前并不是 2008 年那种“所有资产一起崩，再一起反弹，只是黄金后来涨得更多”的情形。更可能出现的路径，是类似 2001 至 2003 年，或者 1972 至 1973 年：股票市场进入熊市，但黄金和贵金属反而走强，因为资金正在从股票流向贵金属。</p>

<p>标普 500 的长期牛市终究会结束。具体是在 18 个月后，还是 6 个月、12 个月后，没有人能精确知道。但一旦股票市场进入严重熊市，而黄金同时保持上行，贵金属的长期牛市就会获得真正的燃料。</p>

<h2 id="long-term-targets">七、黄金 7000 至 10000 美元，白银重回 100 美元上方</h2>

<p>如果未来两三年出现股票市场走弱、资金持续流入贵金属的环境，那么黄金上行目标就不应只看短线反弹。中长期路径上，黄金有机会向 7000、8000、9000 美元推进，甚至在三到四年维度上触及 10000 美元附近。</p>

<p>白银的弹性通常更大。如果黄金进入这类长期牛市，白银不仅有机会重新站上 100 美元，还可能向 200 美元附近靠拢。白银的特点是上涨时往往更剧烈，下跌时也更凶，因此它更适合被视为高弹性资产，而不是低波动避险工具。</p>

<p>这些目标并不是短线预测，也不是说价格会一路直线抵达。更合理的理解是：贵金属的长期上行空间取决于股票市场是否进入新一轮长期风险重估，以及资金是否真正从股票体系迁移到黄金和白银。如果这个过程展开，贵金属行情就不会只是一次普通反弹，而会演变为一轮更完整的长期牛市。</p>

<h2 id="miners">八、矿业股也处在修正后的反弹窗口</h2>

<p>矿业股的结构同样值得关注。以 GDX、GDXJ 为代表的金矿股和初级矿业股，已经经历了相当明显的修正。历史上，在类似 40% 至 50% 的回撤后，矿业股往往会出现非常可观的反弹。</p>

<p>例如，2022 年 GDXJ 曾经出现约 50% 的下跌，随后迎来强劲修复；2016 年底的 GDX 也曾经历慢性下跌，跌幅较深，但之后出现了约 45% 左右的反弹。当前矿业股的修正幅度与这些历史阶段具备可比性。</p>

<p>这意味着，即便当前这轮小反弹后续失败，矿业股再低迷几周或一个月，也更像是在构筑更好的反弹起点，而不是无止境下跌的开始。只要黄金和白银的中期反弹逻辑成立，矿业股大概率会跟随出现弹性修复。</p>

<h2 id="stock-selection">九、比买指数更重要的是公司筛选</h2>

<p>矿业股投资不能只停留在买 GDX 或 GDXJ。指数基金提供了便利的行业暴露，但它也会把好公司、普通公司和差公司一起装进去。对于愿意做公司分析的人，真正的机会在于筛选出一篮子更优质的矿业公司。</p>

<p>优质矿业公司的标准，应该包括更好的资产质量、更稳健的成本结构、更强的资产负债表、更合理的项目推进节奏，以及在金银价格上涨时更大的利润弹性。这样的组合有机会在下跌时比指数承受更小回撤，在上涨时比指数获得更高弹性。</p>

<p>换句话说，可以自己构建一个“更好的 GDX”或“更好的 GDXJ”：不是追求持仓数量最多，而是追求公司质量更高、下行风险更低、上行空间更大。</p>

<h2 id="strategy">十、交易策略：等待确认，不在情绪里追涨杀跌</h2>

<p>当前最理性的策略，不是简单判断“已经见底”或“一定还要跌”，而是接受两种路径都存在：如果黄金已经完成低点，后续应关注能否继续守住 4000 美元并向 4400 美元推进；如果反弹失败，应重点观察 3700 至 3800 美元、尤其是 50% 回撤附近是否出现最终低点。</p>

<p>白银则重点看 70 美元附近的阻力。站上之前，要尊重压力；如果回撤后再次启动，白银的弹性会更值得重视。矿业股方面，可以在行业回撤后逐步筛选优质公司，而不是无差别追入整个板块。</p>

<p>美联储政策也可能成为短期催化因素。如果市场开始重新定价加息，甚至出现九月加息预期，贵金属短线可能承压。但这类压力反而可能制造真正重要的低点。对中期投资者来说，关键不是被单次政策信号吓出局，而是判断这种政策冲击是否把价格打到了更有吸引力的位置。</p>

<h2 id="conclusion">十一、结论：贵金属的关键不是短线猜底，而是抓住中期与长期结构</h2>

<p>黄金和白银已经进入一个重要阶段。短期看，低点可能已经出现，也可能还需要一次假跌破；中期看，情绪指标、周线形态和历史修正类比都支持多月级别反弹；长期看，真正的大行情需要股票市场走弱与资金再配置配合。</p>

<p>黄金 4400 美元、白银 70 美元，是中期反弹首先要面对的阻力；黄金 3700 至 3800 美元，则是如果反弹失败后最值得关注的潜在最终低点区域。未来两三年，如果股票市场进入严重熊市，而资金加速流入贵金属，黄金向 7000 至 10000 美元推进、白银重回 100 美元上方甚至走向 200 美元，就不再只是激进想象，而是一条具备历史逻辑支撑的路径。</p>

<p>贵金属投资最重要的不是每天猜涨跌，而是理解周期位置、情绪极值、资产间资金流向和矿业股质量差异。真正的机会往往出现在市场犹豫、情绪低迷、价格完成大幅修正之后。现在的黄金、白银和矿业股，正处在这样一个需要认真准备的位置。</p>
'''


def esc(s):
    return html.escape(s, quote=True)

def qpath(s):
    return quote(s, safe='/')

def term_url(kind, term):
    return f'/{kind}/{quote(term)}/'

def meta_links():
    cat = f'<a href="{term_url("categories", CATEGORY)}">{esc(CATEGORY)}</a>'
    tag_links = '&nbsp;'.join(f'<a href="{term_url("tags", t)}">{esc(t)}</a>' for t in TAGS)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tag_links}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {READING_MIN} min'

def build_toc(body):
    links=[]
    for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body):
        links.append(f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>')
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + ''.join(links) + '</nav></div></div>'

def make_cover():
    cover_dir=ROOT/'images/posts'/SLUG
    cover_dir.mkdir(parents=True, exist_ok=True)
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#111827"/>
      <stop offset="0.52" stop-color="#4a3213"/>
      <stop offset="1" stop-color="#d6a53b"/>
    </linearGradient>
    <linearGradient id="silver" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#cbd5e1"/>
      <stop offset="1" stop-color="#f8fafc"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.35"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <path d="M0 670 C250 580 430 720 650 610 C880 495 1020 585 1240 430 C1390 324 1505 286 1600 250 L1600 900 L0 900 Z" fill="#0f172a" opacity="0.45"/>
  <path d="M170 640 C310 585 430 600 560 535 C710 460 820 420 960 440 C1110 462 1235 370 1415 250" fill="none" stroke="#facc15" stroke-width="18" stroke-linecap="round" filter="url(#shadow)"/>
  <path d="M180 705 C360 655 515 710 690 650 C835 600 940 610 1085 535 C1220 465 1325 470 1450 405" fill="none" stroke="url(#silver)" stroke-width="10" stroke-linecap="round" opacity="0.92"/>
  <circle cx="1415" cy="250" r="58" fill="#facc15" filter="url(#shadow)"/>
  <circle cx="1450" cy="405" r="40" fill="#e5e7eb" filter="url(#shadow)"/>
  <text x="120" y="190" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="70" font-weight="800">黄金与白银的下一阶段</text>
  <text x="124" y="270" fill="#fde68a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="40" font-weight="700">多月反弹 · 关键阻力 · 长期牛市路径</text>
  <g fill="#f8fafc" font-family="JetBrains Mono, Arial" font-size="30" opacity="0.9">
    <text x="126" y="760">Gold 4400</text>
    <text x="126" y="810">Silver 70</text>
    <text x="126" y="860">Miners rebound window</text>
  </g>
</svg>'''
    (cover_dir/'cover.svg').write_text(svg, encoding='utf-8')

def build_article_page():
    template=(ROOT/'2026/index-investing-middle-age-anxiety-life-investment/index.html').read_text(encoding='utf-8')
    head=template[:template.find('<article class="post">')]
    tail=template[template.find('</article>', template.find('<article class="post">'))+len('</article>'):]
    # update head metadata
    head=re.sub(r'<title>.*?</title>', f'<title>{esc(TITLE)} - zcxGGmu\'s Blog</title>', head, flags=re.S)
    head=re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(DESC)}">', head)
    head=re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{esc(FULL_URL)}">', head)
    head=re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(TITLE)}">', head)
    head=re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(DESC)}">', head)
    head=re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{esc(FULL_URL)}">', head)
    toc=build_toc(ARTICLE_HTML)
    article=f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{COVER}')"><div class="post-title">{esc(TITLE)}<div class="post-subtitle">{esc(DESC)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links()}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{ARTICLE_HTML}</div></div><nav class="post-pagination"><a class="newer-posts">下一篇<br>没有更新的文章</a><a class="older-posts" href="{OLDER_URL}">上一篇<br>{esc(OLDER_TITLE)}</a></nav>
    </article>'''
    tail=re.sub(r'<div class="toc-wrapper">.*?</div></div>', toc, tail, flags=re.S)
    out=ROOT/'2026'/SLUG/'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head+article+tail, encoding='utf-8')
    # update previously latest article to point newer to new page
    older=ROOT/OLDER_URL.strip('/')/'index.html'
    txt=older.read_text(encoding='utf-8')
    txt=re.sub(r'<a class="newer-posts">下一篇<br>没有更新的文章</a>', f'<a class="newer-posts" href="{URL_PATH}">下一篇<br>{esc(TITLE)}</a>', txt)
    older.write_text(txt, encoding='utf-8')

def home_card(url, title, desc, cover, minutes, pinned=False):
    pin_class='post-item-pinned' if pinned else ''
    pin_badge='<span class="pin-badge">📌 置顶</span> ' if pinned else ''
    image=f'<div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url(\'{cover}\')"></div></div>'
    return f'''<a href="{url}" class="a-block">
      <div class="post-item-wrapper {pin_class}">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(title)}</div>
            <div class="post-item-summary">{esc(desc)}</div>
            <div class="post-item-meta">{pin_badge}{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {minutes} min&nbsp;&nbsp;</div>
          </div>
          {image}
        </div>
      </div>
    </a>'''

def update_home():
    path=ROOT/'index.html'
    txt=path.read_text(encoding='utf-8')
    card=home_card(URL_PATH, TITLE, DESC, COVER, READING_MIN)
    if URL_PATH not in txt:
        marker=f'<a href="{OLDER_URL}" class="a-block">'
        pos=txt.find(marker)
        if pos == -1:
            raise RuntimeError('older homepage card not found')
        txt=txt[:pos]+card+'\n'+txt[pos:]
    path.write_text(txt, encoding='utf-8')

def update_rss():
    path=ROOT/'index.xml'
    txt=path.read_text(encoding='utf-8')
    txt=re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{PUB_RSS}</lastBuildDate>', txt)
    item=f'''<item>
<title>{esc(TITLE)}</title>
<link>{FULL_URL}</link>
<guid>{FULL_URL}</guid>
<pubDate>{PUB_RSS}</pubDate>
<description>{esc(DESC)}</description>
</item>
'''
    if FULL_URL not in txt:
        txt=txt.replace('<item>', item+'<item>', 1)
    path.write_text(txt, encoding='utf-8')

def update_archive():
    path=ROOT/'archive/index.html'
    txt=path.read_text(encoding='utf-8')
    if URL_PATH not in txt:
        txt=txt.replace('2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">153 篇</span>', '2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">154 篇</span>')
        item=f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{URL_PATH}">{esc(TITLE)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(CATEGORY)}</span></span>
      </div> '''
        marker=f'<div style="padding:8px 0;font-size:15px">\n        <span style="color:#999">2026-07-12</span>&nbsp;\n        <a href="{OLDER_URL}">'
        pos=txt.find(marker)
        if pos == -1:
            raise RuntimeError('archive insertion marker not found')
        txt=txt[:pos]+item+txt[pos:]
    path.write_text(txt, encoding='utf-8')

def list_page(kind, term, title_prefix=None, emoji=''):
    safe=quote(term)
    d=ROOT/kind/term
    d.mkdir(parents=True, exist_ok=True)
    path=d/'index.html'
    if path.exists():
        txt=path.read_text(encoding='utf-8')
        if URL_PATH not in txt:
            txt=re.sub(r'共 (\d+) 篇文章', lambda m: f'共 {int(m.group(1))+1} 篇文章', txt, count=1)
            item=f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''
            insert=txt.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
            if insert == -1:
                insert=txt.find('</div></div></div>')
            txt=txt[:insert]+item+txt[insert:]
        path.write_text(txt, encoding='utf-8')
        return
    label = f'{title_prefix}: {term}' if title_prefix else term
    h1 = f'{emoji} {term}' if emoji else label
    txt=f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="https://zcxggmu.github.io/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Noto+Sans+SC:wght@400;500;700&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons&amp;display=swap"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p><div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> </div></div></div><script src="/js/journal.js"></script></body></html>'''
    path.write_text(txt, encoding='utf-8')

def update_index_count(path, term, kind, delta=1):
    p=ROOT/path/'index.html'
    txt=p.read_text(encoding='utf-8')
    url=f'/{path}/{quote(term)}/'
    pattern=rf'(<a href="{re.escape(url)}"[^>]*>{re.escape(term)}<span[^>]*>\()(\d+)(\)</span></a>)'
    m=re.search(pattern, txt)
    if m:
        txt=txt[:m.start(2)] + str(int(m.group(2))+delta) + txt[m.end(2):]
    else:
        if path == 'tags':
            item=f' <a href="/{path}/{quote(term)}/" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">(1)</span></a>'
        else:
            item=f' <a href="/{path}/{quote(term)}/" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">(1)</span></a>'
        pos=txt.rfind('</div></div></div></div>')
        if pos == -1:
            pos=txt.rfind('</div></div></div>')
        txt=txt[:pos]+item+txt[pos:]
    p.write_text(txt, encoding='utf-8')

def update_taxonomy():
    list_page('categories', CATEGORY, '分类')
    update_index_count('categories', CATEGORY, 'category')
    list_page('series', SERIES, None, '📚')
    update_index_count('series', SERIES, 'series')
    for tag in TAGS:
        list_page('tags', tag, '标签', '🏷️')
        update_index_count('tags', tag, 'tag')

def validate():
    failures=[]
    article=ROOT/'2026'/SLUG/'index.html'
    txt=article.read_text(encoding='utf-8')
    forbidden=['B站','bilibili','视频里','视频中','原视频','音频里','音频中','UP主','up主','这期','本期','作者说','他提到','观看','点赞','下期','欢迎收看','感谢','订阅','老铁','所长','Jordan Roy','TheDailyGold']
    for w in forbidden:
        if w in txt:
            failures.append(f'forbidden word in article: {w}')
    for p in [article, ROOT/'index.html', ROOT/'index.xml', ROOT/'archive/index.html', ROOT/'categories'/CATEGORY/'index.html', ROOT/'series'/SERIES/'index.html']:
        if not p.exists():
            failures.append(f'missing {p}')
    home=(ROOT/'index.html').read_text(encoding='utf-8')
    links=re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)
    expected=['/2026/codeinsights-local-first-agent-workbench/','/2026/what-you-need-to-learn-from-claw-code-repo/','/2026/gaojingqi-investment-system/','/2026/ai-revolution-permanent-underclass-career-selection/','/2026/live-longer-than-earn-fast-investment-infinite-game/',URL_PATH,OLDER_URL]
    if links[:7] != expected:
        failures.append(f'homepage order mismatch: {links[:7]}')
    try:
        ET.parse(ROOT/'index.xml')
    except Exception as e:
        failures.append(f'rss xml parse failed: {e}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print('validation passed')

make_cover()
build_article_page()
update_home()
update_rss()
update_archive()
update_taxonomy()
validate()
print('published local files for', FULL_URL)
