from pathlib import Path
from urllib.parse import quote
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
import html
import re
import xml.etree.ElementTree as ET

ROOT = Path('/tmp/hermes-video-publish')
SLUG = 'basic-materials-2026h1-earnings-value-revaluation'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
TITLE = '基础材料板块价值重估：铜、黄金、铝、锂的半年报主线'
DESC = '从铜价与硫酸价格上行、黄金利率敏感性、铝板块被产能担忧错杀、锂价触底修复，到煤炭和钢铁的分化压力，梳理基础材料板块 2026 年上半年业绩前瞻与配置策略。'
DATE = '2026-07-12'
PUB_DT = datetime(2026, 7, 12, 17, 32, tzinfo=timezone(timedelta(hours=8)))
PUB_RSS = format_datetime(PUB_DT)
CATEGORY = '投资'
SERIES = '周期研究'
TAGS = ['基础材料', '铜', '黄金', '铝', '锂', '煤炭', '钢铁', '紫金矿业', '赣锋锂业', '周期股', '半年报']
READING_MIN = 8
COVER = f'/images/posts/{SLUG}/cover.svg'
OLDER_URL = '/2026/innovative-drugs-risk-clearing-license-out-2026-strategy/'
OLDER_TITLE = '创新药风险出清了吗：出海趋势、政策扰动与下半年配置策略'

ARTICLE_HTML = r'''
<p>基础材料板块正在进入一个很典型的再定价窗口。上半年，上海铜价同比上涨约 31%，硫酸价格同比飙升约 163%，但不少铜矿股年内反而跌了 20% 以上；铝价稳定在每吨 24000 元左右，一些龙头公司上半年利润仍有高增长预期，可股价却因为印尼新增产能担忧被提前压制。价格、利润和股价之间出现明显错位，说明市场并不是在单纯交易业绩，而是在被宏观噪音、产能担忧和风险偏好牵着走。</p>

<p>现在更关键的变化是，市场焦点正在从美联储加息、地缘冲突这类宏观叙事，逐步回到企业基本面。基础材料内部并不是全面机会，而是结构性分化：铜和黄金处在第一梯队，铝存在估值修复机会，锂开始触底反弹，煤炭偏稳但缺少爆发力，钢铁则仍然受制于高成本、低价格和库存压力。</p>

<h2 id="macro-shift">一、主线已经从宏观噪音切回盈利兑现</h2>

<p>周期股最容易被宏观变量压制。过去一段时间，市场对利率、美元、地缘冲突和全球需求的担忧很重，导致资源品价格上涨并没有完全反映到股票估值里。尤其是铜、黄金、铝这类品种，一边受益于商品价格走强，一边又被加息预期和外部风险压住估值。</p>

<p>这种状态正在变化。利率预期逐渐见顶缓和之后，黄金这类对利率敏感的资产吸引力会回升；同时，美国 Section 232 等关税与进口限制因素，也在强化铜供给偏紧的叙事。铜价有支撑，黄金有利率弹性，资源股又处在相对低估的位置，基本面和估值修复的逻辑开始重新合拢。</p>

<p>所以，这轮材料股不能简单理解成“商品涨了所以股票涨”。更准确地说，是前期宏观恐惧压低了优质资产的估值，现在半年报窗口临近，只要盈利兑现，市场就会重新承认这些公司的现金流、资源价值和分红能力。</p>

<h2 id="copper-gold">二、铜和黄金：价格强、盈利强，估值却还没有完全反映</h2>

<p>铜和黄金是当前基础材料板块最亮的方向。上海铜价上半年同比上涨约 31%，硫酸价格也大幅上行，直接改善了铜矿和综合矿业公司的盈利预期。相关龙头上半年利润预期相当强：MMG 预计利润增幅可达到约 120%，紫金矿业预计增长约 79%，江西铜业预计增长约 92%。这不是周期下行阶段的财务表现，而是商品价格、资源禀赋和副产品收益共同驱动的盈利释放。</p>

<p>紫金矿业的弹性尤其明确。A 股现价约 27 元，对应目标价约 46 元，潜在上行空间约 68%；H 股目标价约 50 港元，同样维持积极配置思路。对于高弹性资源股，MMG 的估值修复空间更大，现价约 7 港元，对应目标价约 13 港元，潜在涨幅约 85%。</p>

<p>这类机会的核心在于，市场此前把加息恐惧、全球需求担忧和资源股波动性放得太大，却低估了价格上涨对利润表的传导。半年报披露期一旦验证利润高增，资源股就有机会从“商品涨、股票不涨”的状态，切换到“盈利兑现、估值补涨”的状态。</p>

<h2 id="aluminum">三、铝板块：被印尼产能担忧错杀，分红和估值提供安全边际</h2>

<p>铝板块近期最大的压力来自印尼新增产能担忧。市场一听到供给可能扩张，往往先卖股票，再讨论真实影响。但当前铝价仍然稳定在每吨 24000 元左右，行业龙头的盈利并没有明显恶化。相反，中国铝业和中国宏桥上半年利润预计分别增长约 77% 和 51%，业绩韧性很强。</p>

<p>真正吸引人的地方在于估值和分红。中国宏桥 H 股股息率高达约 12%，中国铝业的股息率也有约 6% 至 7%；同时，这些公司的市盈率只有约 5 至 6 倍，明显低于海外同行。也就是说，市场把远期供给担忧提前打进了股价，却没有充分定价当前盈利和分红。</p>

<p>中国铝业 A 股目标价约 13 元，现价约 8.18 元；中国宏桥 H 股目标价约 30 港元，现价约 21 港元。两家公司都具备估值修复空间。铝板块的交易逻辑不是追高景气，而是在低估值、高分红和业绩兑现之间寻找错杀修复。</p>

<h2 id="lithium">四、锂：从价格崩盘担忧转向触底反弹</h2>

<p>锂板块此前最核心的压制因素，是碳酸锂价格持续下跌带来的盈利崩塌担忧。但 4 月之后，锂价已经开始反弹，二季度碳酸锂均价回升到约 16.9 万元/吨附近。叠加下半年电池厂传统补库周期，需求端具备一定支撑，板块逻辑开始从“继续杀盈利”转向“触底修复”。</p>

<p>赣锋锂业被上调至超配，关键原因在于一体化布局完整。从上游矿资源到电池材料，公司链条更完整，抗波动能力强，不完全依赖单一资源价格。上半年利润预计增长约 75%，而且连续几个季度环比改善，这意味着盈利拐点已经有迹象。</p>

<p>价格上，赣锋锂业 A 股目标价约 80 元，现价约 56 元；H 股目标价约 70 港元，现价约 43.8 港元，修复空间并不小。相比之下，天齐锂业维持中性，说明市场更偏好全产业链、一体化能力更强的公司，而不是单纯资源属性更强的公司。</p>

<h2 id="coal-steel">五、煤炭和钢铁：稳与弱的区别很明显</h2>

<p>煤炭板块没有太多惊喜，但也不是完全没有支撑。兖矿能源上半年利润预计增长约 78%，体现出一定韧性。不过，煤价 6 月已经回落，水电发力、煤矿复产顺利，都压制了煤价继续上行的空间。中国神华、兖矿能源这类公司更适合被看作高股息、稳现金流资产，而不是高爆发弹性品种。</p>

<p>钢铁的处境更困难。成本高、价格低、库存压力大，毛利率被压得很紧。如果没有新一轮去产能政策，钢铁行业很难靠自身供需自然修复完成估值反转。相关个股被给出低配评级，目标价甚至低于现价，本质上反映的是行业仍然缺少决定性的供给侧催化。</p>

<p>这也是基础材料板块当前最重要的差异：资源品里有强基本面方向，也有只能防守的方向，更有暂时看不到反转条件的方向。不能因为“材料”两个字就一篮子全买，结构选择越来越重要。</p>

<h2 id="valuation">六、中资材料股的估值折价，正在变成修复弹性</h2>

<p>中资材料股长期存在估值折价。过去折价的理由很多：周期波动大、宏观不确定、海外资金偏好不足、资源品价格难预测、政策扰动频繁。但当盈利高增、分红可观、商品价格有支撑同时出现时，这种折价就会变成潜在修复空间。</p>

<p>铜、黄金、铝、锂这些方向的共同点，是基本面并不弱，却在前期被情绪压制。铜矿股跌幅和铜价涨幅背离，铝股估值和分红被低估，锂股经历价格崩盘预期后的修复，都是同一个逻辑：市场先把风险放大，等财报和价格趋势逐步验证后，再重新承认资产价值。</p>

<p>真正值得关注的不是一句“便宜”，而是便宜背后有没有盈利兑现。只有利润增长、现金流和分红能支撑估值，低估才有意义。否则，低估值可能只是价值陷阱。</p>

<h2 id="ranking">七、行业排序：铜、黄金、铝、锂优先，煤炭中性，钢铁靠后</h2>

<p>当前行业排序可以概括为：铜优于黄金，黄金优于铝，铝优于锂，锂优于煤炭，煤炭优于钢铁。这个排序并不是简单按商品价格涨幅来排，而是综合了价格趋势、盈利弹性、估值位置、分红能力和政策催化。</p>

<p>铜和黄金排名靠前，是因为价格端、供给端和利率环境都相对有利；铝的吸引力来自错杀后的估值和分红修复；锂处于触底反弹阶段，弹性有，但仍要跟踪价格和需求；煤炭现金流稳定，却缺少持续涨价催化；钢铁如果没有去产能政策，反转难度最大。</p>

<p>这就是典型的优中选优。材料板块不是全面牛市，而是盈利强弱和资产质量重新分层。越到半年报密集披露期，市场越会用业绩兑现来筛选公司。</p>

<h2 id="strategy">八、配置策略：盯紧半年报，用业绩兑现确认修复</h2>

<p>接下来最重要的时间窗口，是 8 月中下旬开始的半年报密集披露期。紫金矿业、赣锋锂业、中国铝业、中国宏桥这类超配标的，如果业绩兑现，可能开启戴维斯双击：一边是盈利预期上修，一边是估值折价修复。</p>

<p>策略上，铜和黄金适合作为第一梯队关注，尤其是兼具资源禀赋和盈利弹性的龙头；铝适合关注高分红、低估值、被产能担忧错杀的公司；锂适合跟踪价格触底和电池厂补库节奏，优先选择一体化能力更强的企业；煤炭更偏稳健现金流；钢铁暂时需要等待更明确的政策信号。</p>

<p>对于普通投资者来说，不适合只看股价跌幅，也不适合只看商品涨幅。更合理的方法是把商品价格、公司利润、估值、分红和政策催化放在一起比较。价格强但股票弱，可能是机会；价格弱但估值低，也可能只是陷阱。半年报会给出更清晰的验证。</p>

<h2 id="conclusion">九、结论：材料股的机会来自结构性重估，而不是全面普涨</h2>

<p>基础材料板块的核心逻辑已经很清楚：宏观叙事正在退潮，盈利兑现重新成为主线。铜、黄金、铝、锂这些方向基本面并不弱，只是此前被加息担忧、产能担忧和市场情绪压制。随着半年报窗口临近，只要业绩兑现，估值修复就会变得更有基础。</p>

<p>但这不是所有材料股的普涨行情。煤炭偏稳，钢铁偏弱，真正值得投入精力的是盈利高增、估值有折价、分红有支撑、行业供需逻辑更清晰的方向。铜和黄金看盈利弹性，铝看错杀修复，锂看触底反弹，煤炭看现金流，钢铁看政策。</p>

<p>投资上需要保持两点克制：第一，不要因为商品价格上涨就无差别追周期股；第二，不要因为短期股价下跌就忽视基本面改善。周期投资的关键，不是情绪最热时冲进去，而是在市场误杀优质资产、财报又即将验证利润的时候，提前做好结构选择。</p>

<p>以上内容仅供研究参考，不构成任何投资建议。投资有风险，决策需谨慎。</p>
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
      <stop offset="0" stop-color="#0f172a"/>
      <stop offset="0.52" stop-color="#14532d"/>
      <stop offset="1" stop-color="#f59e0b"/>
    </linearGradient>
    <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fef3c7"/>
      <stop offset="0.4" stop-color="#fbbf24"/>
      <stop offset="1" stop-color="#b45309"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="14" flood-color="#000" flood-opacity="0.35"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#ffffff" fill="none">
    <path d="M120 690 C300 540 430 600 610 450 C760 325 930 410 1085 280 C1240 150 1375 210 1490 110" stroke-width="8"/>
    <path d="M100 760 C370 610 570 700 810 560 C1035 430 1220 470 1500 250" stroke-width="4"/>
  </g>
  <g filter="url(#shadow)">
    <rect x="170" y="500" width="190" height="160" rx="16" fill="#fdba74"/>
    <rect x="410" y="430" width="190" height="230" rx="16" fill="#facc15"/>
    <rect x="650" y="350" width="190" height="310" rx="16" fill="#d1d5db"/>
    <rect x="890" y="280" width="190" height="380" rx="16" fill="#a7f3d0"/>
    <rect x="1130" y="220" width="190" height="440" rx="16" fill="url(#metal)"/>
  </g>
  <path d="M210 610 C380 560 525 500 680 430 C850 355 1030 300 1220 215 C1325 168 1410 145 1490 110" fill="none" stroke="#fef08a" stroke-width="18" stroke-linecap="round" filter="url(#shadow)"/>
  <circle cx="1490" cy="110" r="44" fill="#fde047" filter="url(#shadow)"/>
  <text x="110" y="165" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="64" font-weight="800">基础材料板块价值重估</text>
  <text x="114" y="244" fill="#fef3c7" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">铜 · 黄金 · 铝 · 锂 · 半年报主线</text>
  <g fill="#111827" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="800">
    <text x="222" y="590">铜</text>
    <text x="460" y="550">金</text>
    <text x="700" y="495">铝</text>
    <text x="940" y="445">锂</text>
    <text x="1176" y="390">分红</text>
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
    forbidden = ['B站', 'bilibili', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主', '这期', '本期', '作者说', '他提到', '观看', '点赞', '下期', '欢迎收看', '感谢', '订阅', '老铁', '所长', '带你拆解', '欢迎在评论区']
    for w in forbidden:
        if w in txt:
            failures.append(f'forbidden word in article: {w}')
    for concept in ['上海铜价', '硫酸价格', '紫金矿业', '中国宏桥', '赣锋锂业', '兖矿能源', '钢铁', '半年报']:
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
