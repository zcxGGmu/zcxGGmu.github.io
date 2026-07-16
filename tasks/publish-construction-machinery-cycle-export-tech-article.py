from pathlib import Path
from urllib.parse import quote
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
import html
import re
import xml.etree.ElementTree as ET

ROOT = Path('/tmp/hermes-video-publish')
SLUG = 'construction-machinery-cycle-domestic-export-tech-upgrade'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
TITLE = '工程机械的周期拐点：内需、出海与技术升级的三重共振'
DESC = '工程机械正在从单一周期复苏，走向内需更新、海外扩张、电动化与智能化共同驱动的新阶段；指数工具则提供了更分散、更贴近产业 beta 的配置方式。'
DATE = '2026-07-16'
PUB_DT = datetime(2026, 7, 16, 16, 10, tzinfo=timezone(timedelta(hours=8)))
PUB_RSS = format_datetime(PUB_DT)
CATEGORY = '投资'
SERIES = '产业投资'
TAGS = ['工程机械', '周期投资', '内需复苏', '出海', '电动化', '智能化', '设备更新', '基建', '中证工程机械主题指数', 'ETF']
READING_MIN = 15
COVER = f'/images/posts/{SLUG}/cover.svg'
OLDER_URL = '/2026/keep-doing-hard-right-things-without-feedback/'
OLDER_TITLE = '在看不到希望时，怎样坚持做难而正确的事'

ARTICLE_HTML = r'''
<p>工程机械不是一个只看短期行情波动的板块。它是国民经济建设中的基础性产业之一，和基建、地产、矿业、能源、城镇化、设备更新以及资本开支周期高度相关。这个行业具备明显的周期性，也具备很强的“二阶导”属性：总量需求不仅取决于下游有多大，更取决于下游景气度和资本开支增量是否发生变化。</p>

<p>当下理解工程机械，不能只停留在“涨了一段是否结束”这一层。更重要的问题是：行业处在周期的什么位置，复苏由什么推动，国内需求是否足够扎实，海外市场是不是还能继续扩张，电动化和智能化会不会改变估值逻辑，以及普通投资者该怎样避免个股选择中的极端风险。</p>

<p>结论可以先放在前面：工程机械这一轮并不是单纯由交易情绪推动的反弹，而是内需底部反转、出海持续加速、技术升级带来估值溢价的三重共振。行情中间会有波动，甚至会有比较剧烈的回撤，但产业逻辑仍处在持续验证的过程当中。</p>

<h2 id="cycle-position">一、工程机械仍在景气上行周期中</h2>

<p>工程机械上一轮行业高点出现在 2021 年前后。随后，伴随地产链条下行、国内需求收缩和库存消化，板块经历了数年的深度调整。2021 年二季度到 2024 年一季度，是行业压力比较集中的阶段，需求端收缩明显，很多企业都需要经历订单、产能、盈利和估值的重新出清。</p>

<p>从 2024 年开始，行业出现了明显回暖。尤其是 2024 年 9 月之后，板块累计涨幅一度超过 45%。虽然 2026 年 5 月中旬之后又出现调整，但近期又有抬升趋势。单看价格波动，容易误判周期已经结束；放回基本面看，工程机械更像是从深度调整进入底部修复，再逐步走向景气回升的阶段。</p>

<p>过去二十多年，工程机械经历过几轮典型大周期。2008 年金融危机之后，四万亿投资刺激落地，工程机械产销量大幅提升。2016 年到 2020 年，基建持续发力、地产政策阶段性宽松，又叠加上一轮设备更新高峰，行业产销数据持续向好。2021 年之后，地产下行和需求收缩让行业重新进入调整。现在的新变化是，国内更新需求开始回归，政策资金提供支撑，海外扩张又构成第二增长曲线。</p>

<p>因此，工程机械不能简单按“传统地产后周期”去理解。地产固然仍有影响，但当前推动板块的主变量已经更丰富：内需端有设备更新和基建项目，外需端有新兴市场和发达市场突破，技术端有电动化、智能化和无人化升级。这些因素叠加后，板块的盈利弹性和估值框架都在发生变化。</p>

<h2 id="domestic-demand">二、内需不是弱复苏，而是底部反转</h2>

<p>国内工程机械需求目前呈现出典型的底部反转特征。这个判断主要来自三条线索：换机潮、政策支持和行业涨价。</p>

<p>第一条线索是换机潮。工程机械整机的典型使用寿命通常在 8 到 10 年左右。上一轮国内销售高峰大致集中在 2016 年到 2021 年，这意味着从 2026 年开始，上一轮高峰期销售的设备正陆续进入更新周期。挖掘机在工程机械中占比较高，又具备一定前瞻性，因此挖机更新需求常被视作观察行业的重要指标。</p>

<p>根据测算，2026 年挖机更新需求可能在 15 万台左右，对应增速约 25%；本轮内需换新周期可能在 2028 年达到阶段性高点。相较 2025 年内销约 12 万台的水平，后续仍有较大上行空间。最新数据也在验证这一方向：5 月挖机内销数量约 11628 台，同比增长 38.6%。这类数据说明，内需复苏并非只存在于预期中，而是在销量层面逐步体现。</p>

<p>第二条线索是政策支持。2026 年政府工作报告安排超长期特别国债资金，大规模支持设备更新。截至 4 月末，相关资金下发完成度已经达到较高水平。除此之外，中央预算内投资、超长期特别国债、重大基础设施项目，都会对工程机械新增需求形成支撑。</p>

<p>重大项目也很关键。雅江水电站约 1.2 万亿投资、人工运河相关工程、新藏铁路等项目，都会带来挖机、装载机、起重设备、混凝土设备等需求。工程机械的需求并不只来自房地产开工，还来自水利、农田、交通、能源和城市更新等更广泛场景。</p>

<p>第三条线索是行业涨价。2026 年 5 月以来，多家头部主机厂发布挖掘机涨价函，涨价幅度约在 3% 到 5%。涨价一方面与钢铁等上游成本变化有关，另一方面更重要的是，涨价没有对销量造成明显冲击。如果需求很弱，涨价很容易压制订单；如果涨价后销售仍保持较好状态，就能从侧面说明需求韧性较强。</p>

<p>换机潮解决“为什么有量”，政策资金解决“需求从哪里来”，行业涨价则验证“价格能不能站住”。这三者合在一起，构成国内需求底部反转的基本盘。</p>

<h2 id="export-engine">三、出海是远超预期的第二增长曲线</h2>

<p>如果只看国内复苏，工程机械仍然是传统周期行业；但加上出海，行业的成长曲线就明显不同。海外市场已经成为工程机械非常强劲的增长引擎，且收入占比仍在持续提升。</p>

<p>2026 年 1 到 4 月，工程机械累计出口额约 218 亿元，同比增长超过 20%。其中，非洲、一带一路相关地区、新兴经济体需求韧性最强，也是出口量较高的区域。过去几年，中国工程机械在中东、非洲、东南亚以及俄语区的份额提升十分明显。</p>

<p>表面上看，这是大型挖掘机和其他设备出口增加；本质上看，是亚非拉地区矿业开发、能源建设、城市化推进、基建项目落地，共同带动了中国工程机械的市场占有率。同时，国内基建能力和工程承包出海，也会自然带动设备出海。工程、人员、服务体系和设备供应链往往是一起走出去的。</p>

<p>海外增长首先来自矿产和能源需求。中东、非洲、东南亚、俄语区等需求旺盛的区域，矿业和能源是非常重要的下游应用。全球矿产品位持续下降，矿业资本开支可能进入新一轮上行周期。按照相关预测，2024 年到 2030 年，全球矿产资本开支预计增长约 50%。矿业资本开支增加，会直接带动挖掘、装载、运输、破碎、起重等设备需求。</p>

<p>海外增长还来自中国厂商竞争力的提升。发达市场长期被卡特彼勒、小松等国际龙头占据，这些企业有稳定的渠道、品牌、服务和客户黏性。客户更换品牌的成本较高，因此中国主机厂进入北美、欧洲等市场并不容易。但近些年，中国厂商依靠技术缩小差距、价格优势、服务差异化和更有吸引力的保修政策，正在逐步打开空间。</p>

<p>以部分国产挖机为例，与国际主流品牌相比，价格可能低 30% 到 40%。价格只是第一层优势，真正重要的是价格、服务、技术三者组合起来，形成可持续竞争力。单纯便宜只能打开门，持续服务和稳定质量才能留住客户。</p>

<h2 id="emerging-and-developed-markets">四、新兴市场和发达市场都有空间</h2>

<p>新兴市场已经取得较高份额后，是否还有扩张空间？答案仍然是有，而且空间并不小。原因在于许多新兴经济体当前仍由二手机主导需求。比如越南、菲律宾、马来西亚等市场从日本进口的挖机中，二手机占比高达 90% 以上。</p>

<p>二手机主导意味着市场还处在早期阶段。随着这些国家进入更高速度的发展阶段，工程机械需求会逐步从二手机转向新机。这个转换过程，会给中国主机厂提供新的市占率提升机会。中国设备相较欧美日品牌价格更具吸引力，相较旧设备又有性能、能耗、可靠性和售后优势，因此正好卡在新兴市场升级换代的关键位置。</p>

<p>发达市场则是另一种逻辑。欧美市场当前中国品牌渗透率仍然不高，进入壁垒也更高，但一旦突破，空间更大、含金量更高。发达市场关注的不只是初始采购价格，还包括排放、能耗、售后响应、设备在线率、融资租赁、数据管理和全生命周期成本。</p>

<p>这也是为什么电动化会成为中国厂商突破发达市场的重要工具。欧洲排放标准严格，油价高企、能源转型和环保要求都会推动电动设备应用。中国在新能源产业链上的积累，使工程机械企业有机会绕开传统燃油设备的竞争壁垒，建立新的比较优势。</p>

<p>一季度数据已经显示出这种突破迹象：西欧、大洋洲等发达市场增量较快。新兴市场提供规模，发达市场提供品牌升级和估值重估空间。工程机械出海正在从“性价比出海”，逐步转向全球市场的系统性突破。</p>

<h2 id="technology-upgrade">五、技术升级改变工程机械的估值逻辑</h2>

<p>传统工程机械的估值主要跟周期盈利走。销量上行、产能利用率提升、毛利修复，估值就抬升；周期下行、订单减少、利润承压，估值就回落。但电动化和智能化会给行业带来第二层估值支撑。</p>

<p>电动化在内需和外需两端都有意义。国内方面，北京、重庆等地的补贴政策、换机周期和排放标准提升，会推动电动工程机械需求增长。海外方面，电动化成为国产主机厂进入发达市场、提升份额的重要手段。传统燃油设备拼的是几十年积累的发动机、液压、渠道和品牌；电动设备则更依赖电池、电控、电驱、能源补给和智能控制，这些正是中国制造的优势区间。</p>

<p>智能化同样值得重视。头部主机厂已经在电动装载机、电动矿卡、电动宽体车、无人挖机等方向加速布局。矿山场景尤其适合无人化、远程操控和电动化协同，因为矿山环境危险、作业强度高、路线相对固定，对安全和效率提升需求强烈。</p>

<p>政策端也在推动这一方向。到 2026 年，煤矿智能化产能占比要求不低于 60%，危险繁重岗位智能装备替代率不低于 30%。这意味着矿山无人化、远程操控和智能装备不只是概念，而是中期产业变量。</p>

<p>发达市场的技术工人短缺，也是智能化的推动力。以英国为例，行业面临较明显的技能短缺问题，约 60% 企业表示难以招聘到足够熟练的技术工人。劳动力不足会提高自动化、远程化和智能辅助设备的价值。</p>

<p>因此，工程机械板块的估值驱动正在从单纯周期性盈利，逐步叠加技术升级和产品升级带来的估值溢价。周期决定短期弹性，技术升级决定中长期天花板。</p>

<h2 id="index-tool">六、用指数工具布局，核心是抓产业 beta</h2>

<p>工程机械个股选择并不容易。主机厂、零部件、液压件、海外收入占比、产品结构、成本弹性、汇率敞口、订单节奏都可能影响股价。对于多数投资者而言，直接押注单一个股容易踩到经营波动或估值波动的风险。指数工具的价值，就是用更分散的方式获取行业 beta。</p>

<p>中证工程机械主题指数，是当前更便于布局工程机械板块的方向之一。指数覆盖工程机械整机制造、零部件制造、上游原材料、核心零部件、中游制造厂商等相关领域，呈现“主机为主、零部件为辅”的结构特征。</p>

<p>这个指数的一个重要特点是龙头效应突出。工程机械行业本身就是龙头效应很强的领域，头部公司在品牌、渠道、海外网络、研发、规模和售后体系上优势明显。因此，指数前十大成分股合计权重约 70%，前五大成分股约 60%，能够更直接反映行业龙头的周期弹性和全球竞争力。</p>

<p>权重设计也体现了产业相关性。主机厂和核心液压件权重上限较高，其他细分方向权重上限较低。液压件与工程机械相关性较强，且国产化程度较高，放在指数里有助于捕捉核心零部件的国产替代和景气弹性。</p>

<p>ETF 工具还具备交易便利、分散个股极端风险、成本相对透明等特点。对于想要配置工程机械周期，但又不希望在单一公司上承担过多不确定性的投资者，指数化工具更适合作为观察和参与产业趋势的入口。</p>

<h2 id="risk-return">七、高收益与高波动并存，不能只看上行逻辑</h2>

<p>工程机械指数能够较好反映行业周期，与主机厂盈利能力变化高度相关，也能捕捉工程机械周期投资的大逻辑。但这类指数通常呈现高收益、高波动特征。</p>

<p>高波动来自几个方面。第一，行业本身周期属性强，需求容易受到基建节奏、地产变化、政策资金、海外项目、矿业资本开支影响。第二，板块 beta 高，市场风险偏好变化时，涨跌都会被放大。第三，出口占比提升后，还会受到汇率、海外政策、贸易摩擦、运输成本、区域政治风险影响。第四，技术升级虽然提升长期估值，但短期投入也可能压制利润率。</p>

<p>因此，工程机械不是适合无脑追高的板块。更合理的策略，是把它当作周期成长型资产：在基本面底部反转、订单数据持续验证、估值尚未充分透支时分批配置；在短期涨幅过大、预期过热、数据验证跟不上时降低追涨冲动。</p>

<h2 id="allocation-strategy">八、配置策略：用分批和数据跟踪替代情绪交易</h2>

<p>工程机械的核心买点，不是某一天的股价涨跌，而是周期位置和数据验证。配置时应重点跟踪六类指标。</p>

<p>第一，挖机内销数据。挖机具有较强前瞻性，内销增速能直接反映国内更新周期是否持续。第二，出口金额和出口结构。尤其要看非洲、一带一路地区、新兴经济体以及欧美发达市场的变化。第三，头部主机厂订单和涨价执行情况。涨价能否落地，是需求强度的重要验证。第四，重大项目开工和设备更新资金落地节奏。政策资金下发不等于需求立刻释放，还要看项目施工和设备采购进度。第五，电动化、智能化设备渗透率。技术升级能否从样机、概念走向真实订单，是估值能否重构的关键。第六，指数估值和市场情绪。当基本面向上但估值不贵，风险收益比较好；当市场已经把远期乐观预期一次性打满，就要留出安全边际。</p>

<p>具体配置上，更适合采用分批方式，而不是一次性重仓。第一笔仓位用于建立观察位，确认自己能承受板块波动；第二笔仓位等待内销、出口或订单数据继续验证；第三笔仓位留给市场回撤或基本面超预期。这样做不一定买在最低点，但能避免在短期情绪最热时把仓位打满。</p>

<p>对于风险承受能力较低的投资者，工程机械更适合作为组合中的卫星仓位，而不是核心底仓。它的优点是弹性足、产业逻辑清晰、内外需共振；缺点是波动大、周期性强、短期容易受情绪影响。真正适合参与的人，是能接受波动、愿意跟踪数据、理解周期位置的人。</p>

<h2 id="conclusion">九、结论：工程机械的机会，不止是周期修复</h2>

<p>工程机械当前的投资逻辑，可以概括为三句话。</p>

<p>第一，国内需求处在底部反转阶段。2016 年到 2021 年销售高峰带来的换机需求正在释放，政策资金和重大项目形成支撑，行业涨价验证需求韧性。第二，出海正在成为第二增长曲线。新兴市场从二手机向新机升级，发达市场依靠电动化、服务和价格优势逐步突破。第三，技术升级正在改变估值框架。电动化、智能化、无人化和远程操控，使工程机械不再只是传统周期股，也具备一定产业升级属性。</p>

<p>这并不意味着工程机械没有风险。它仍然是高波动行业，仍然会受到宏观周期、政策节奏、出口环境、矿业资本开支和估值情绪影响。但从产业逻辑看，板块正在从“地产链周期修复”转向“内需更新 + 全球扩张 + 技术升级”的复合逻辑。</p>

<p>对投资者来说，关键不是追逐每一次短期上涨，而是在周期底部反转的过程中，用数据验证逻辑，用分批配置管理波动，用指数工具降低个股风险。工程机械真正值得关注的地方，不只是当下景气回升，而是中国高端制造在全球市场继续提高份额的长期路径。</p>

<p>本文仅用于产业研究和投资框架梳理，不构成任何投资建议。市场有风险，配置需结合自身风险承受能力和资金期限。</p>
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
      <stop offset="0.48" stop-color="#14532d"/>
      <stop offset="1" stop-color="#ca8a04"/>
    </linearGradient>
    <linearGradient id="road" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#334155"/>
      <stop offset="1" stop-color="#64748b"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="16" stdDeviation="12" flood-color="#000" flood-opacity="0.32"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <path d="M0 700 C280 620 430 665 680 565 C930 465 1160 430 1600 300 L1600 900 L0 900 Z" fill="#172554" opacity="0.42"/>
  <path d="M0 760 C270 690 520 705 760 610 C980 522 1230 502 1600 390 L1600 900 L0 900 Z" fill="url(#road)" opacity="0.95"/>
  <g stroke="#fef3c7" stroke-width="5" opacity="0.42">
    <path d="M175 742 L320 711"/>
    <path d="M470 690 L620 648"/>
    <path d="M790 594 L952 548"/>
    <path d="M1120 506 L1290 455"/>
  </g>
  <g filter="url(#shadow)" transform="translate(815 445)">
    <rect x="0" y="110" width="360" height="88" rx="22" fill="#f59e0b"/>
    <rect x="62" y="44" width="182" height="84" rx="18" fill="#fbbf24"/>
    <rect x="248" y="86" width="210" height="34" rx="17" fill="#fde68a"/>
    <path d="M442 102 L546 54 L574 84 L488 136 Z" fill="#facc15"/>
    <circle cx="86" cy="208" r="54" fill="#111827"/>
    <circle cx="86" cy="208" r="25" fill="#94a3b8"/>
    <circle cx="286" cy="208" r="54" fill="#111827"/>
    <circle cx="286" cy="208" r="25" fill="#94a3b8"/>
  </g>
  <g fill="none" stroke="#bbf7d0" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" opacity="0.9">
    <path d="M1050 285 C1150 235 1190 245 1280 175 C1360 115 1430 110 1505 72"/>
    <path d="M1490 72 L1508 69 L1503 88"/>
  </g>
  <text x="96" y="150" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="64" font-weight="800">工程机械的周期拐点</text>
  <text x="100" y="230" fill="#fef3c7" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">内需更新 · 全球出海 · 技术升级</text>
  <text x="102" y="300" fill="#dcfce7" font-family="Noto Sans SC, PingFang SC, Arial" font-size="32" font-weight="600">从传统周期股到中国制造全球化 beta</text>
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
    forbidden = ['B站', 'bilibili', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主', '这期', '本期', '作者说', '他提到', '观看', '点赞', '下期', '欢迎收看', '感谢', '订阅', '老铁']
    for w in forbidden:
        if w in txt:
            failures.append(f'forbidden word in article: {w}')
    for concept in ['工程机械', '内需', '出海', '换机潮', '电动化', '智能化', '中证工程机械主题指数', '高收益、高波动']:
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
