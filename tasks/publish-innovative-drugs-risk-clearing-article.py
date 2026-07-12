from pathlib import Path
from urllib.parse import quote
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
import html
import re
import xml.etree.ElementTree as ET

ROOT = Path('/tmp/hermes-video-publish')
SLUG = 'innovative-drugs-risk-clearing-license-out-2026-strategy'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
TITLE = '创新药风险出清了吗：出海趋势、政策扰动与下半年配置策略'
DESC = '从创新药 License-out 出海、跨国药企专利悬崖、美国政策扰动、ASCO 临床数据分歧、医保与商保衔接，到 CXO 订单、资金轮动和分批配置策略，重估创新药板块的风险与机会。'
DATE = '2026-07-12'
PUB_DT = datetime(2026, 7, 12, 16, 22, tzinfo=timezone(timedelta(hours=8)))
PUB_RSS = format_datetime(PUB_DT)
CATEGORY = '投资'
SERIES = '医药投资'
TAGS = ['创新药', '医药', 'License-out', 'BD出海', 'CXO', '医保', '商保', '生物科技', '科创创新药', '投资策略']
READING_MIN = 13
COVER = f'/images/posts/{SLUG}/cover.svg'
OLDER_URL = '/2026/declutter-index-investing-financial-freedom-at-33/'
OLDER_TITLE = '不看盘反而赚更多：从一万件囤积物到 33 岁财务自由'

ARTICLE_HTML = r'''
<p>创新药板块在上半年经历了持续调整。表面看，市场像是在担心出海逻辑降温、政策风险抬升、临床数据不及预期；但如果把产业数据、跨国药企需求、国内政策变化、融资环境、资金轮动和估值位置放在一起看，结论并不悲观：创新药的产业趋势没有结束，风险更多是在估值和情绪层面被重新定价。</p>

<p>当前更准确的判断不是“马上全面反转”，也不是“继续无底下跌”，而是：板块已经进入逐步磨底和悲观修复阶段。短期反弹可以来自风险偏好和资金轮动，中期持续性则要看重磅临床数据、BD 里程碑收入、销售分成兑现以及 CXO 订单和业绩能否继续验证。</p>

<h2 id="license-out-trend">一、出海趋势没有降温，只是股价先调整了</h2>

<p>过去两年，市场交易创新药最核心的主线，是出海和对外授权。上半年板块虽然调整，但产业端热度并没有明显下降。按照医药魔方一类数据口径，今年上半年国内创新药对外 BD 总金额约 997 亿美元，已经达到上一年全年约 73%，也大约相当于 2024 年全年的两倍；相比去年同期，仍然有四成以上增长。</p>

<p>这说明 License-out 并不是一个短期故事。去年全年金额已经出现过大幅跃升，今年增速从极高基数上回落很正常，但增长趋势本身仍在延续。市场下跌，更多反映的是估值、政策和临床数据预期的重估，而不是产业趋势突然熄火。</p>

<p>出海能够持续，背后有一个很硬的产业逻辑：全球大型跨国药企正在面对专利悬崖。过去贡献现金流的重磅药物陆续面临仿制药冲击，跨国药企必须寻找新的创新资产来补充管线。中国创新药资产具有“量大、质优、成本低”的特征，管线数量多，临床推进效率高，研发和试验成本相对海外更低，因此自然成为跨国药企寻找资产的重要来源。</p>

<h2 id="china-advantage">二、中国创新药的优势来自效率、成本和工程师红利</h2>

<p>中国创新药之所以被全球药企重视，不只是因为价格便宜，而是因为研发体系正在形成规模优势。国内医药研发投入从 2020 年约 260 亿美元，增长到 2025 年接近 390 亿美元，占全球药企研发投入的比例已经达到 10% 以上。</p>

<p>从 2020 年开始，中国进入临床阶段的创新药数量已经位居全球前列，并持续高于欧美一些主要地区。在 ADC、双抗、多抗等前沿赛道，中国企业拥有大量候选药物和技术储备。也正因为中国创新药实力和全球产业链地位持续提升，海外政策层面对中国生物医药资产的关注和警惕也在增强。</p>

<p>更关键的是，国内创新药在临床前研究、临床试验、患者入组和工程化执行方面具备效率优势。国内患者入组效率高，研发人员和工程师红利仍然明显，整体研发成本相比海外有显著优势。对于跨国药企而言，很难完全绕开中国创新药资产，也很难绕开中国医药产业链在研发和生产中的作用。</p>

<h2 id="policy-risk">三、政策扰动是估值压力，但也反映了产业地位上升</h2>

<p>上半年板块调整，政策扰动是重要原因之一。美国方面，从 2 月开始就有议员提出扩充对外投资国家安全监管，把生物医药纳入管控范围；随后 5 月、6 月也陆续出现相关法案和意见，试图把生物药纳入对外投资安全审查。</p>

<p>这类政策对 A 股和港股医药公司的投资情绪都会产生压制。再加上一些国内 CXO 公司被列入美国国防相关名单，限制联邦资金资助项目与其合作，市场自然会担心国内医药企业在全球合作中的不确定性。</p>

<p>但从另一面看，这些政策也说明中国创新药和医药产业链的重要性正在上升。只有当一个产业在全球竞争中变得不可忽视时，才会引发更多监管和安全层面的关注。政策风险需要重视，但不能简单理解成产业逻辑被否定。</p>

<p>国内方面，医疗反腐、核心技术海外转让审查趋严，也在短期影响市场情绪。无论是此前一些交易受阻，还是其他行业技术出口审查，都让市场联想到创新药出海是否会受到限制。但从当前数据看，对外授权仍在推进，趋势尚未被打断。</p>

<h2 id="asco-data">四、临床数据分歧，是上半年最直接的情绪冲击</h2>

<p>除了政策，上半年创新药板块还有一个显著压力来自重磅会议数据披露后的预期落差。市场原本对部分龙头创新药公司的临床数据期待较高，尤其是国内创新药首次进入国际肿瘤学重要全体大会的范围，关注度本来就很高。</p>

<p>但数据披露之后，市场出现了较多质疑。以依沃西单抗相关研究为例，Harmony-6 的数据中，总生存期 OS 的 HR 看起来超出部分市场预期，但质疑点也很集中：入组患者年龄结构、性别结构以及老年群体获益是否足够明确。</p>

<p>在相关试验中，入组患者集中在 75 岁以下，而 65 岁以上人群的 OS 风险比接近 0.93，明显弱于总体结果。考虑到美国非小细胞肺癌确诊患者中位年龄大约 68 岁，如果老年患者获益不够显著，海外市场对适用人群和峰值销售的预期就会被压制。</p>

<p>因此，下半年更值得关注的是 Harmony-3 这类全球三期数据。尤其要看 PFS 无进展生存期能否有效转化为 OS 总生存期获益。如果后续 OS 数据表现足够扎实，将有助于修复市场对国内创新药临床质量和全球商业化潜力的信心；如果不及预期，板块情绪还会受到冲击。</p>

<h2 id="drug-price-pressure">五、美国药价压力，会压制出海资产的峰值预期</h2>

<p>中国创新药出海最大的市场仍然是美国。国内医保支付压力较大，商业保险渗透率仍然偏低，而美国创新药市场容量更大、支付体系更成熟，因此很多资产的商业化想象空间来自海外。</p>

<p>但美国自身也在反复讨论压降药品价格。国会、议员和监管层不断提出降低药价的方案和提案，这会影响市场对创新药峰值销售额的预期。即使一款药能够出海，最终能拿到多高价格、对应多大销售峰值，仍然存在不确定性。</p>

<p>所以，出海趋势可以继续，但出海资产的估值不能简单线性外推。市场未来会更重视首付款、里程碑付款、销售分成和真实商业化进展，而不是只看一个大额总交易金额。</p>

<h2 id="domestic-policy-support">六、国内医保和商保衔接，正在改善创新药支付路径</h2>

<p>下半年创新药仍有积极因素。国内政策对创新药发展的支持并没有改变，医保目录调整工作方案也在优化创新药进入支付体系的路径。</p>

<p>医保推出预申报机制，可以使药品申报节奏提前大约一个月；同时，进入商保创新药目录后，可以更顺畅地衔接医保目录。这意味着高价值创新药可以先通过商业保险承担一部分支付，再逐步进入医保覆盖范围。</p>

<p>续约和定价规则的优化，也有助于提高药企未来收入预期的清晰度。对于投资而言，创新药公司最大的难点之一，是未来现金流难以估算。如果续约规则更加明确、商保与医保路径更顺畅，市场对收入和利润的贴现就会更有依据。</p>

<h2 id="cxo-orders">七、CXO 率先反弹，原因在于订单和融资先有验证</h2>

<p>近期创新药相关行情中，CXO 板块率先表现，背后并不是单纯情绪，而是订单和融资数据提供了基本面支撑。</p>

<p>国内创新药一级市场融资在 6 月同比增长两倍以上，上半年融资规模同比增长约 188%。如果把一级和二级市场融资合并计算，上半年累计融资同比也有约 35% 增长。海外市场同样不弱，6 月生物医药一级市场融资同比增长约 166%，上半年同比增长约 32%。</p>

<p>融资活跃，意味着更多创新药项目能够立项，并进入临床前和临床试验阶段。对 CXO 公司来说，这会转化为新的订单和收入预期。截至一季度，国内多家 CXO 公司在手订单同比增速基本在 20% 以上，后续二季度财报如果继续验证 20% 至 30% 甚至更高的订单增长，板块基本面支撑会更强。</p>

<p>因此，在创新药大板块里，CXO 可能是业绩确定性相对更高的方向。它不一定拥有最高弹性，但如果订单恢复和收入兑现持续出现，估值修复会更扎实。</p>

<h2 id="market-rotation">八、资金轮动正在给创新药提供阶段性窗口</h2>

<p>除了基本面，资金层面的轮动也很重要。前期市场高度拥挤在 AI 硬件、算力、存储等方向，近期这些方向出现明显波动。市场开始担心算力供给、AI 资本开支节奏、存储价格上涨对产业链成本的影响，以及部分高位公司的估值消化压力。</p>

<p>当高位科技方向出现波动，资金会寻找新的成长板块承接。创新药、机器人以及其他有业绩支撑和成长属性的方向，都会成为资金轮动的候选。创新药前期调整时间长，机构重仓拥挤度下降，科创创新药指数估值回到历史中位数附近，这使得它具备承接资金的条件。</p>

<p>这也是为什么下半年创新药行情可能比上半年更好。板块并不需要所有风险立刻消失，只要估值合理、筹码不拥挤、产业趋势未变，资金就有动力在低位重新配置。</p>

<h2 id="liquidity">九、流动性环境也开始从压制转向边际改善</h2>

<p>创新药估值对流动性敏感。上半年油价阶段性上行、地缘冲突和通胀预期抬升，一度推高加息预期，对创新药估值形成压制。但近期随着油价从高位回落，通胀预期也开始下降，美联储继续加息的概率在边际降低。</p>

<p>美国就业数据虽然仍有韧性，但从非农数据变化看，劳动力市场也出现降温迹象。中长期看，未来一两年仍然存在降息可能。对创新药这类长久期成长资产而言，流动性环境从紧张转向缓和，会改善估值弹性。</p>

<p>当然，流动性不是创新药的全部逻辑。真正决定持续性的，仍然是临床数据、BD 兑现、医保支付和业绩确认。但在低估值和低拥挤度阶段，流动性边际改善会成为行情的重要助推。</p>

<h2 id="us-biotech-difference">十、不能简单照搬美股 Biotech 的上涨逻辑</h2>

<p>美股生物科技板块近期表现较强，一个重要原因是并购事件活跃。专利悬崖临近，跨国药企在北美市场对 Biotech 公司进行溢价并购，投资者会给潜在被收购公司一定并购溢价。</p>

<p>但国内创新药和美股 Biotech 的主逻辑并不完全相同。国内创新药出海更多是对外授权、联合开发和里程碑付款，而不是整家公司被并购。因此，国内创新药的估值重估，不能完全照搬美股 Biotech 的并购溢价逻辑。</p>

<p>License-out、NewCo 等合作形式仍会增加，交易金额和事件数量也在持续增长，但定价权在很大程度上仍掌握在跨国药企手中。再叠加药价压力、政策扰动和地缘风险，创新药出海会是一个螺旋向上的过程，而不是线性上行。</p>

<h2 id="valuation-stage">十一、当前更像磨底和悲观修复，而不是全面主升</h2>

<p>当前创新药板块的定位，可以理解为进入逐步磨底阶段。近期反弹反映了部分过度悲观预期的修复，包括政策担忧、临床数据争议、出海 BD 放缓担忧以及资金过度低配的修复。</p>

<p>但要进入更持续的主升行情，还需要更多硬催化。三季度和下半年，可以观察重磅临床数据披露，尤其是欧洲肿瘤学相关大会可能带来的新数据；更长期则要看已经 BD 出去的药品能否兑现里程碑收入，上市后能否形成销售分成。</p>

<p>对于已经有药品上市、逐步实现扭亏为盈的创新药公司，估值会从 PS 或管线估值，慢慢切换到 PE 和利润兑现逻辑。对于中小 Biotech，则仍然需要依靠临床数据、BD 事件和里程碑兑现来完成价值重估。</p>

<h2 id="strategy">十二、配置策略：低位分批，而不是一次性押注</h2>

<p>中长期看，创新药板块仍然值得重视。估值处在历史中位数附近，相比部分估值已经较高的 AI 硬件和科技产业链方向，创新药并不算贵；同时，出海趋势、融资恢复、医保支持、CXO 订单和资金轮动，都在提供正面因素。</p>

<p>但行业仍然存在风险，包括海外政策扰动、国内技术出海审查、临床数据不确定、美国药价压力以及出海交易定价权受制于跨国药企。因此，策略上不适合一次性重仓追涨，更适合在回调中分批配置。</p>

<p>更稳健的方向，可以关注订单和业绩确定性更强的 CXO；弹性更大的方向，则是科创创新药指数、创新药 ETF 以及具备鲜明 Biotech 属性的创新药组合。科创创新药指数中包含较多科创板代表性创新药公司，创新属性更纯，波动也会更大，上涨和下跌阶段的弹性都更强。</p>

<p>在执行上，可以把创新药当作中长期成长板块来配置，而不是短线题材来追。低位分批、回调补仓、控制仓位、跟踪关键临床数据和 BD 兑现，是更合理的方式。</p>

<h2 id="conclusion">十三、结论：创新药风险没有消失，但性价比正在改善</h2>

<p>创新药的核心矛盾，并不是产业趋势结束，而是趋势向上过程中伴随政策、临床、支付、定价和资金波动。上半年板块下跌，已经把很多担忧计入价格；下半年如果产业数据和临床数据继续验证，板块有机会从悲观修复走向更扎实的估值修复。</p>

<p>出海 BD 金额仍在增长，跨国药企专利悬崖仍然存在，中国创新药的效率和成本优势没有消失，医保与商保衔接也在改善支付路径。风险同样不能忽视：政策、药价、临床数据和出海定价权，都会影响估值上限和行情节奏。</p>

<p>因此，当前创新药更适合用“风险逐步出清、低位分批配置”的思路看待。真正的机会不在于赌某一天是最低点，而在于在产业趋势仍然向上、估值已经回到合理区间、筹码拥挤度下降的时候，耐心布局那些能用数据、订单、里程碑和利润兑现自身价值的公司与工具。</p>
'''


def esc(s):
    return html.escape(s, quote=True)

def term_url(kind, term):
    return f'/{kind}/{quote(term)}/'

def meta_links():
    cat=f'<a href="{term_url("categories", CATEGORY)}">{esc(CATEGORY)}</a>'
    tag_links='&nbsp;'.join(f'<a href="{term_url("tags", t)}">{esc(t)}</a>' for t in TAGS)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tag_links}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {READING_MIN} min'

def build_toc(body):
    links=[]
    for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body):
        links.append(f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>')
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>'+''.join(links)+'</nav></div></div>'

def make_cover():
    d=ROOT/'images/posts'/SLUG
    d.mkdir(parents=True, exist_ok=True)
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#101827"/><stop offset="0.48" stop-color="#1e3a8a"/><stop offset="1" stop-color="#38bdf8"/></linearGradient>
    <linearGradient id="line" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22c55e"/><stop offset="0.5" stop-color="#a7f3d0"/><stop offset="1" stop-color="#facc15"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#000" flood-opacity="0.32"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.16" stroke="#ffffff" fill="none"><path d="M120 650 C280 510 430 720 610 560 C780 410 920 470 1070 350 C1240 215 1380 260 1500 160" stroke-width="8"/><path d="M120 735 C330 640 510 690 710 610 C940 520 1100 560 1480 360" stroke-width="4"/></g>
  <g filter="url(#shadow)">
    <rect x="180" y="470" width="210" height="180" rx="18" fill="#dbeafe" opacity="0.96"/>
    <rect x="430" y="390" width="210" height="260" rx="18" fill="#bfdbfe" opacity="0.96"/>
    <rect x="680" y="330" width="210" height="320" rx="18" fill="#93c5fd" opacity="0.96"/>
    <rect x="930" y="250" width="210" height="400" rx="18" fill="#86efac" opacity="0.96"/>
    <rect x="1180" y="200" width="210" height="450" rx="18" fill="#fde68a" opacity="0.96"/>
  </g>
  <path d="M210 610 C370 560 500 530 650 470 C820 405 960 345 1125 280 C1255 230 1355 205 1450 160" fill="none" stroke="url(#line)" stroke-width="18" stroke-linecap="round" filter="url(#shadow)"/>
  <circle cx="1450" cy="160" r="46" fill="#facc15" filter="url(#shadow)"/>
  <text x="120" y="175" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="66" font-weight="800">创新药风险出清了吗</text>
  <text x="124" y="254" fill="#dbeafe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">出海趋势 · 政策扰动 · 下半年配置策略</text>
  <g fill="#0f172a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="700">
    <text x="214" y="575">BD</text><text x="458" y="505">医保</text><text x="713" y="455">CXO</text><text x="965" y="400">数据</text><text x="1208" y="352">分批</text>
  </g>
</svg>'''
    (d/'cover.svg').write_text(svg, encoding='utf-8')

def build_article_page():
    template=(ROOT/OLDER_URL.strip('/')/'index.html').read_text(encoding='utf-8')
    head=template[:template.find('<article class="post">')]
    tail=template[template.find('</article>', template.find('<article class="post">'))+len('</article>'):]
    head=re.sub(r'<title>.*?</title>', f'<title>{esc(TITLE)} - zcxGGmu\'s Blog</title>', head, flags=re.S)
    head=re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(DESC)}">', head)
    head=re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{esc(FULL_URL)}">', head)
    head=re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(TITLE)}">', head)
    head=re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(DESC)}">', head)
    head=re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{esc(FULL_URL)}">', head)
    article=f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{COVER}')"><div class="post-title">{esc(TITLE)}<div class="post-subtitle">{esc(DESC)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links()}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{ARTICLE_HTML}</div></div><nav class="post-pagination"><a class="newer-posts">下一篇<br>没有更新的文章</a><a class="older-posts" href="{OLDER_URL}">上一篇<br>{esc(OLDER_TITLE)}</a></nav>\n    </article>'''
    tail=re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(ARTICLE_HTML), tail, flags=re.S)
    out=ROOT/'2026'/SLUG/'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head+article+tail, encoding='utf-8')
    older=ROOT/OLDER_URL.strip('/')/'index.html'
    txt=older.read_text(encoding='utf-8')
    txt=re.sub(r'<a class="newer-posts">下一篇<br>没有更新的文章</a>', f'<a class="newer-posts" href="{URL_PATH}">下一篇<br>{esc(TITLE)}</a>', txt)
    older.write_text(txt, encoding='utf-8')

def home_card(url, title, desc, cover, minutes):
    return f'''<a href="{url}" class="a-block">\n      <div class="post-item-wrapper ">\n        <div class="post-item post-item-no-divider">\n          <div class="post-item-info-wrapper">\n            <div class="post-item-title">{esc(title)}</div>\n            <div class="post-item-summary">{esc(desc)}</div>\n            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {minutes} min&nbsp;&nbsp;</div>\n          </div>\n          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{cover}')"></div></div>\n        </div>\n      </div>\n    </a>'''

def update_home():
    p=ROOT/'index.html'
    txt=p.read_text(encoding='utf-8')
    if URL_PATH not in txt:
        marker=f'<a href="{OLDER_URL}" class="a-block">'
        pos=txt.find(marker)
        if pos==-1:
            raise RuntimeError('older homepage marker not found')
        txt=txt[:pos]+home_card(URL_PATH,TITLE,DESC,COVER,READING_MIN)+'\n'+txt[pos:]
    p.write_text(txt, encoding='utf-8')

def update_rss():
    p=ROOT/'index.xml'
    txt=p.read_text(encoding='utf-8')
    txt=re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{PUB_RSS}</lastBuildDate>', txt)
    item=f'''<item>\n<title>{esc(TITLE)}</title>\n<link>{FULL_URL}</link>\n<guid>{FULL_URL}</guid>\n<pubDate>{PUB_RSS}</pubDate>\n<description>{esc(DESC)}</description>\n</item>\n'''
    if FULL_URL not in txt:
        txt=txt.replace('<item>', item+'<item>', 1)
    p.write_text(txt, encoding='utf-8')

def update_archive():
    p=ROOT/'archive/index.html'
    txt=p.read_text(encoding='utf-8')
    if URL_PATH not in txt:
        txt=re.sub(r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>', lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1))+1} 篇</span>', txt, count=1)
        item=f'''<div style="padding:8px 0;font-size:15px">\n        <span style="color:#999">{DATE}</span>&nbsp;\n        <a href="{URL_PATH}">{esc(TITLE)}</a>\n        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(CATEGORY)}</span></span>\n      </div> '''
        marker=f'<div style="padding:8px 0;font-size:15px">\n        <span style="color:#999">2026-07-12</span>&nbsp;\n        <a href="{OLDER_URL}">'
        pos=txt.find(marker)
        if pos==-1:
            raise RuntimeError('archive marker not found')
        txt=txt[:pos]+item+txt[pos:]
    p.write_text(txt, encoding='utf-8')

def list_page(kind, term, title_prefix=None, emoji=''):
    d=ROOT/kind/term
    d.mkdir(parents=True, exist_ok=True)
    p=d/'index.html'
    if p.exists():
        txt=p.read_text(encoding='utf-8')
        if URL_PATH not in txt:
            txt=re.sub(r'共 (\d+) 篇文章', lambda m: f'共 {int(m.group(1))+1} 篇文章', txt, count=1)
            item=f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">\n        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>\n        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>\n      </div> '''
            insert=txt.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
            if insert==-1:
                insert=txt.find('</div></div></div>')
            txt=txt[:insert]+item+txt[insert:]
        p.write_text(txt, encoding='utf-8')
        return
    label=f'{title_prefix}: {term}' if title_prefix else term
    h1=f'{emoji} {term}' if emoji else label
    txt=f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="https://zcxggmu.github.io/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Noto+Sans+SC:wght@400;500;700&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons&amp;display=swap"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p><div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">\n        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>\n        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>\n      </div> </div></div></div><script src="/js/journal.js"></script></body></html>'''
    p.write_text(txt, encoding='utf-8')

def update_index_count(path, term):
    p=ROOT/path/'index.html'
    txt=p.read_text(encoding='utf-8')
    url=f'/{path}/{quote(term)}/'
    pattern=rf'(<a href="{re.escape(url)}"[^>]*>{re.escape(term)}<span[^>]*>\()(\d+)(\)</span></a>)'
    m=re.search(pattern, txt)
    if m:
        txt=txt[:m.start(2)]+str(int(m.group(2))+1)+txt[m.end(2):]
    else:
        if path=='tags':
            item=f' <a href="/{path}/{quote(term)}/" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">(1)</span></a>'
        else:
            item=f' <a href="/{path}/{quote(term)}/" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">(1)</span></a>'
        pos=txt.rfind('</div></div></div></div>')
        if pos==-1:
            pos=txt.rfind('</div></div></div>')
        txt=txt[:pos]+item+txt[pos:]
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
    failures=[]
    article=ROOT/'2026'/SLUG/'index.html'
    txt=article.read_text(encoding='utf-8')
    forbidden=['B站','bilibili','视频里','视频中','原视频','音频里','音频中','UP主','up主','这期','本期','作者说','他提到','观看','点赞','下期','欢迎收看','感谢','订阅','老铁','所长','机构调研会议']
    for w in forbidden:
        if w in txt:
            failures.append(f'forbidden word in article: {w}')
    for concept in ['License-out','997 亿美元','专利悬崖','依沃西单抗','CXO','医保','低位分批']:
        if concept not in txt:
            failures.append(f'missing concept: {concept}')
    for p in [article, ROOT/'index.html', ROOT/'index.xml', ROOT/'archive/index.html', ROOT/'categories'/CATEGORY/'index.html', ROOT/'series'/SERIES/'index.html']:
        if not p.exists():
            failures.append(f'missing {p}')
    home=(ROOT/'index.html').read_text(encoding='utf-8')
    links=re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)
    expected=['/2026/codeinsights-local-first-agent-workbench/','/2026/what-you-need-to-learn-from-claw-code-repo/','/2026/gaojingqi-investment-system/','/2026/ai-revolution-permanent-underclass-career-selection/','/2026/live-longer-than-earn-fast-investment-infinite-game/',URL_PATH,OLDER_URL]
    if links[:7]!=expected:
        failures.append(f'homepage order mismatch: {links[:7]}')
    ET.parse(ROOT/'index.xml')
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
