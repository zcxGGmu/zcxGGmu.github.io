from pathlib import Path
from urllib.parse import quote
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
import html
import re
import xml.etree.ElementTree as ET

ROOT = Path('/tmp/hermes-video-publish')
SLUG = 'third-era-dividend-industrial-chain-engineer-globalization'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
TITLE = '中国第三次时代红利：产业链、工程师与出海重估'
DESC = '从人口红利、城市化红利，到完整产业链和工程师群体的重新定价，理解第三次时代红利为什么不是简单的内需扩张，而是中国生产要素主动接入全球市场。'
DATE = '2026-07-12'
PUB_DT = datetime(2026, 7, 12, 23, 18, tzinfo=timezone(timedelta(hours=8)))
PUB_RSS = format_datetime(PUB_DT)
CATEGORY = '宏观经济'
SERIES = '宏观研究'
TAGS = ['时代红利', '人口红利', '城市化红利', '出海', '产业链', '工程师红利', '制造业', '全球化', '生产要素', '中国经济']
READING_MIN = 12
COVER = f'/images/posts/{SLUG}/cover.svg'
OLDER_URL = '/2026/labor-alienation-human-nature-abstract-work/'
OLDER_TITLE = '劳动为什么从人的天性变成了强制'

ARTICLE_HTML = r'''
<p>过去四十多年，中国出现过两次全民性的时代红利。第一次是人口红利，第二次是城市化红利。今天许多人觉得这类机会已经彻底消失，但如果从生产要素重新定价的角度看，中国的第三次红利并没有结束，反而刚刚开启。</p>

<p>所谓时代红利，并不是一句宏观口号，也不是某个行业突然景气。它的本质是一种关键生产要素，从被严重低估的旧体系，迁移到能够正确定价它的新体系。在这个迁移过程中，卷入要素流动的人、企业和城市，其价值都会被大幅抬升。</p>

<h2 id="what-is-dividend">一、什么样的机会，才配叫时代红利</h2>

<p>经济学意义上的生产要素，可以概括为土地、劳动、资本、知识与组织。要素本身的价值，并不只取决于它是否稀缺，更取决于它所在的体系能不能把它的价值最大化。</p>

<p>同一块土地，在一个体系里可能一文不值，在另一个体系里却寸土寸金；同一个劳动者，在低效农业体系里可能收入极低，进入全球制造业体系后收入却可能增长数倍甚至十倍。差异不在要素本身突然变化，而在定价体系发生了变化。</p>

<p>因此，每当一种要素在旧体系里被严重低估，而新体系正在孕育并能够给它更高定价时，要素就会自发地从估值洼地流向估值高地。这个流动过程就是红利。过去四十年改变命运的机会，看起来形式各异，底层逻辑却几乎一致：参与到关键要素重新定价之中。</p>

<h2 id="labor-dividend">二、第一次红利：人口红利不是人多，而是劳动力被重新定价</h2>

<p>第一次红利通常被称为人口红利，但这五个字很容易误导人。人口多并不天然产生红利。如果人多就是红利，印度和孟加拉应该拥有更强的增长曲线。真正重要的不是数量，而是劳动力价值能否从低估中被纠正。</p>

<p>1978 年前后，中国农村劳动力价值处在极低位置。大量农民生活在公社体制下，土地集体所有，壮劳力与老人获得的报酬差异并不充分，劳动动力被压低。学界常用边际生产率接近零来描述当时农村的隐性剩余劳动力：抽走一个劳动力，生产队总产出甚至未必下降。</p>

<p>1952 年至 1972 年，中国农村人口增加了约 55%，但人均耕地面积减少近一半，大量新增劳动力不仅没有被充分定价，反而不断稀释有限资源。以土地贫瘠地区为例，农民年收入极低，与同时期一些亚洲新兴经济体存在巨大差距。劳动力要素被旧体系严重低估，是第一次红利出现的前提。</p>

<h2 id="township-enterprises">三、乡镇企业和南下就业，把劳动力接入更高定价体系</h2>

<p>改革开放真正改变的，并不是让人口数量突然变多，而是让数以亿计的农村劳动力第一次获得流动机会。包产到户让农民脱离低效的工分体系，释放出大量剩余劳动力；随后，农村加工合作社和乡镇企业崛起，成为 80 年代经济增长的重要力量。</p>

<p>到 90 年代初，全国乡镇企业数量突破 2000 万家，生产总量约占全社会产值三分之一。这些家门口的企业，让约 1.3 亿农民离开土地，进入价值更高的工业体系。它们给农民提供了除种地之外的第二条出路，也成为改革开放前二十年的重要支柱。</p>

<p>更高层级的定价体系来自南方经济特区和珠三角制造业。1992 年之后，劳动力从乡镇进一步流向南方就业市场。乡镇企业把劳动力放入国内工业体系重新定价，而南下务工则把劳动力放入全球市场重新定价。外资工厂密集铺开，产品销往欧美，劳动者收入对应的不再只是本地支付能力，而是全球消费者的购买力。</p>

<p>这解释了为什么同一个人，从村口乡镇企业走到珠三角工厂，收入就能再上台阶。一个劳动者的收入，并不只对应他的辛苦程度，更对应他所服务的市场愿意支付多少溢价。</p>

<h2 id="first-dividend-end">四、第一次红利结束：劳动力低估被逐步磨平</h2>

<p>1980 年至 1995 年，中国农村人均月收入从约 16 元增长到约 114 元，已经是明显改善；但同时期外出务工月收入可达约 448 元，相当于三个月工资就接近一位农民一年收入。如果进入珠三角地区，农民工月收入甚至接近 800 元，相当于老家多个人种地收入的总和。</p>

<p>同一个人没有突然变得更聪明，只是从旧体系迁移到新体系，收入就能显著提升。这就是第一次时代红利的本质：劳动力作为关键生产要素，从农业体系流向工业体系，从国内低效定价流向全球市场定价。</p>

<p>但任何红利都会被充分定价。2008 年后，中国农村剩余劳动力开始出现枯竭，刘易斯拐点被反复讨论。到 2012 年前后，劳动力价格上升，大量外资工厂开始向东南亚迁移。曾经被大幅低估的劳动力要素逐步完成重新定价，普通人的第一次红利随之结束。</p>

<h2 id="urban-dividend">五、第二次红利：城市化红利不是城镇化率，而是城市土地被重新定价</h2>

<p>第二次红利通常被称为城市化红利。它同样不是城镇化率上升这么简单。80 年代到 90 年代，城市规模确实在扩大，但最先受益的并不是城市核心区居民，反而是郊区和县域工业带。</p>

<p>1984 年至 1999 年，是中国初级加工业的黄金期。浙江民营经济、广东电子加工、纺织出口等产业快速崛起，但这些故事的主角往往是郊区、县城和乡镇，而不是传统城区。加工制造业需要大量成片工业用地，城市核心地段早已用于住宅和行政办公，反而是郊区土地便宜、约束少，培育出大规模产业集群。</p>

<p>90 年代出现过“郊区经济超过城区”的典型现象。杭州下属乡镇企业产值占比很高，萧山、顺德、长安等地都曾在产业活力上超过传统城区。与此同时，许多城市居民的生活质量并不高。以上海为例，90 年代末仍有大量困难家庭和下岗职工，城市并未真正释放土地和聚集效应的价值。</p>

<h2 id="city-repricing">六、WTO 之后，城市从行政容器变成全球产业链节点</h2>

<p>90 年代的城市，更多只是行政容器，而不是高效生产要素。城市真正的价值，不在于人口数量，而在于是否能产生强大的聚集效应，是否能提供足够多的第三产业、高端制造、研发、金融、营销和服务岗位。</p>

<p>2001 年中国加入 WTO 后，全球资本和订单进入中国，沿海城市开始承担全球产业链分工节点的角色。城市产业生态随之变化。首先是第三产业爆发，2000 年至 2015 年，中国服务业占 GDP 比重从约 37% 提升到约 52%，为城市提供了海量就业岗位。</p>

<p>其次是产业升级。中国研发支出从 2000 年约 900 亿元，一路增长到 2022 年约 3 万亿元。中国不再只是依赖大量土地的初级加工，而是开始向更高端的制造、互联网、金融、研发和技术企业升级。华为、腾讯等企业的出现，意味着高薪企业和高薪岗位开始向城市聚集。</p>

<p>随着就业质量提升，城市土地开始承载更强的聚集效应。2000 年至 2020 年，主要一二线城市人均可支配收入普遍增长 7 至 9 倍；2002 年至 2014 年，一线城市核心区房价普遍上涨 10 至 12 倍，二线城市普遍上涨 8 至 10 倍。事后看，这一阶段的上涨本质上是城市聚集效应在土地上的价值投射。</p>

<h2 id="second-dividend-end">七、第二次红利结束：土地价值回归后，房价进入横盘回落</h2>

<p>第二次红利的本质，是城市土地作为重要生产要素，重新回归真实价值。在 2000 年至 2015 年之间进入一线城市，并买入住房的人，成为这轮要素重新定价的最大受益者。他们参与的并不只是房地产上涨，而是城市聚集效应对土地价值的重估。</p>

<p>但土地红利同样不可能无限持续。2017 年之后，城市房价重新定价速度明显放缓，许多城市开始横盘甚至回落。城市土地从极度低估到充分定价，第二次红利也基本结束。</p>

<p>这给第三次红利提供了判断框架：如果红利来自要素重新定价，那么问题就变成，当下中国还有什么要素被系统性低估？</p>

<h2 id="undervalued-factors">八、今天被低估的两类要素：完整产业链与工程师群体</h2>

<p>现阶段，中国至少还有两类关键要素被严重低估：一是全球独一份的完整产业链，二是庞大的工程师群体与高学历人才供给。前者代表组织要素，后者代表人力资本要素。</p>

<p>2024 年，中国制造业产值占全球比重首次达到约 30%，成为全球唯一覆盖联合国工业分类 41 个大类、207 个中类、666 个小类的国家。这种完整性意味着，同一款产品在中国可以从设计、生产到交付，在很短半径内完成，周期和成本往往只有其他国家的一半左右。</p>

<p>2022 年，中国制造业增加值约 5 万亿美元，超过欧美 28 个国家合计约 4.9 万亿美元，从产业链能力上达到“一国等于欧美总和”的量级。可是从这一阶段开始，国内企业利润却持续承压，“增收不增利”成为制造业普遍感受。问题已经不只是技术差距，而是产业链要素没有被合理定价。</p>

<h2 id="pricing-gap">九、同样的产品，代工和品牌之间差出二十倍利润</h2>

<p>电动手工具是一个直观例子。中国厂家为海外品牌做贴牌代工，一个成本 100 元的产品，打上海外品牌后可以卖到 500 元，但国内代工企业利润率通常只有约 5%，也就是只赚 5 元。产业链真实价值、研发投入和制造能力，都被压缩在这 5 元以内。</p>

<p>如果中国厂家自己做品牌，同样产品可以卖到欧洲中端市场，售价约 300 元，却可能获得 100 至 150 元利润。同样的产品、同样的产业链能力，收益相差可能达到 20 倍。这就是当下中国产业链定价不合理的核心。</p>

<p>中国制造并不缺能力，缺的是直接面向全球消费者、全球渠道和全球品牌心智的定价权。只做代工，完整产业链的价值被海外品牌拿走；做自有品牌和全球市场，产业链能力才有机会被重新定价。</p>

<h2 id="human-capital">十、人力资本同样被低估：不是人才过剩，而是人才没有被充分定价</h2>

<p>中国工程师数量已经达到全球最高密度之一。狭义口径接近 2000 万，广义口径超过 6000 万；每年还有超过 1000 万大学毕业生，以及庞大的在读研究生群体。劳动人口中大专及以上学历占比也已经显著提高。这本应是人类历史上规模最大的高学历人才储备池之一。</p>

<p>但就业市场并没有给这批人才充分定价。过去几年，青年失业率长期处于较高位置，大量高学历者很难找到与能力匹配的岗位，只能继续考研、考公。国考报名人数从 2019 年约 140 万，上升到 2024 年约 296 万，说明许多人不是没有能力，而是缺少能够承接能力的定价体系。</p>

<p>这不是简单的人才过剩，而是人才价值被低估。完整产业链和高密度人才储备，在国内市场中被系统性压低，结果就是制造业利润微薄和大学生就业困难同时出现。</p>

<h2 id="global-market">十一、第三次红利的本质：把中国要素接入全球市场</h2>

<p>要素的真实价值从来不是由能力单方面决定的，而是由它服务的市场愿意为这种能力支付多少决定。仅靠 14 亿人口的国内市场，无论怎样刺激消费、投资和竞争，都很难完整消化中国这套全要素、全品类、高密度的生产能力和人才供给。</p>

<p>要让如此庞大的产业链和人才要素重新回归真实价值，只有一条路：接入更大的体系，让它们接受更充分的定价。这个更大的体系就是全球市场。</p>

<p>这与 2001 年的全球化不同。那一次是全球市场进入中国，跨国资本带来订单、品牌和技术，中国提供土地和劳动力，被定价为世界工厂。这一次则是中国主动走向全球市场，带着自己的产业链能力、工程师群体、产品能力和组织能力，直接服务全球消费者。</p>

<h2 id="going-global">十二、出海不是可选项，而是第三次红利的主通道</h2>

<p>所谓出海，不只是企业去海外开店，也不只是跨境电商和海外建厂。它更深层的意义，是中国被低估的组织要素和人力资本要素，离开国内低价内卷体系，进入更高支付能力、更大需求缺口、更完整品牌溢价的全球体系。</p>

<p>完整产业链只有接入 80 亿人的全球市场，才能找到足够大的需求空间；工程师和高学历人才也只有参与全球产品、全球品牌、全球技术服务和全球组织协同，才可能获得更合理的能力定价。</p>

<p>因此，第三次红利不是简单的“内需复苏”，也不是传统意义上的“外贸订单增加”。它是中国企业从代工者变成品牌者，从供应链节点变成全球组织者，从低利润制造变成高附加值产品和服务提供者的过程。</p>

<h2 id="risk-and-window">十三、为什么红利刚开始时，总是先被看成风险</h2>

<p>每一次要素重新定价的窗口期，最初都不会显得轻松。第一次人口红利中，背井离乡、离开土地、进入陌生工厂，本身就是风险；第二次城市化红利中，进入一线城市并购房，同样伴随不确定和压力。</p>

<p>今天的出海也是如此。许多人首先看到的是地缘冲突、陌生市场、文化差异、合规难度、海外渠道成本和汇率波动。风险真实存在，但这并不否定红利。恰恰因为风险存在，早期参与者才有可能获得超额回报；等所有人都确认它是机会，要素定价差往往已经被磨平。</p>

<p>回头看前两次红利，最大回报往往属于那些在不确定中先迈出去的人：第一批离开土地进入工业体系的人，第一批进入大城市并承接城市聚集效应的人。第三次红利中，类似的位置可能属于能把中国制造、工程师能力、产品设计和组织效率带向全球市场的人与企业。</p>

<h2 id="conclusion">十四、结论：第三次红利不是消失了，而是换了入口</h2>

<p>人口红利的本质，是劳动力从低效农业体系流向工业体系和全球市场；城市化红利的本质，是城市土地从行政容器中释放出来，承接产业升级和聚集效应。两次红利都不是凭空出现，而是关键生产要素从低估体系走向高估值体系。</p>

<p>今天，中国被低估的要素，已经从廉价劳动力和城市土地，转向完整产业链、工程师群体和高学历人才储备。国内市场无法单独完成这些要素的充分定价，全球市场才是它们重新估值的空间。</p>

<p>因此，中国第三次时代红利的关键词，是产业链出海、品牌出海、技术服务出海、组织能力出海和人才价值出海。它不是一个已经被证明无风险的确定性答案，而是一个正在打开的要素迁移过程。真正的问题不是还有没有时代红利，而是谁能理解这轮红利的底层逻辑，并在定价差仍然存在时完成迁移。</p>
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
      <stop offset="0.55" stop-color="#075985"/>
      <stop offset="1" stop-color="#22c55e"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="14" flood-color="#000" flood-opacity="0.34"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#fff" fill="none">
    <path d="M130 670 C300 540 450 610 620 480 C810 335 980 390 1150 260 C1300 145 1410 170 1500 95" stroke-width="8"/>
    <path d="M120 740 C340 650 560 690 790 575 C1010 465 1230 485 1490 315" stroke-width="4"/>
  </g>
  <g filter="url(#shadow)">
    <circle cx="365" cy="520" r="92" fill="#fef3c7"/>
    <circle cx="640" cy="455" r="92" fill="#bfdbfe"/>
    <circle cx="915" cy="390" r="92" fill="#bbf7d0"/>
    <circle cx="1190" cy="325" r="92" fill="#fde68a"/>
    <path d="M450 500 L555 475 M725 435 L830 410 M1000 370 L1105 345" stroke="#e0f2fe" stroke-width="18" stroke-linecap="round"/>
  </g>
  <g fill="#0f172a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="34" font-weight="800">
    <text x="309" y="532">劳动</text>
    <text x="584" y="467">土地</text>
    <text x="859" y="402">链条</text>
    <text x="1134" y="337">全球</text>
  </g>
  <text x="105" y="165" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="66" font-weight="800">中国第三次时代红利</text>
  <text x="110" y="245" fill="#dbeafe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">产业链 · 工程师 · 出海重估</text>
  <text x="110" y="805" fill="#ecfeff" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="700">从低估体系迁移到全球定价体系</text>
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
    forbidden = ['B站', 'bilibili', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主', '这期', '本期', '作者说', '他提到', '观看', '点赞', '下期', '欢迎收看', '感谢', '订阅', '老铁', '所长', 'Boden']
    for w in forbidden:
        if w in txt:
            failures.append(f'forbidden word in article: {w}')
    for concept in ['人口红利', '城市化红利', '生产要素', '乡镇企业', 'WTO', '产业链', '工程师', '出海', '全球市场']:
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
