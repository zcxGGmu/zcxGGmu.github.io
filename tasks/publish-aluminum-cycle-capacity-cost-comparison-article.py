from __future__ import annotations

import html
import json
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path("/tmp/hermes-video-publish")
SITE = "https://zcxggmu.github.io"
SLUG = "aluminum-cycle-capacity-ceiling-yunlv-shenhuo-hongqiao"
URL_PATH = f"/2026/{SLUG}/"
FULL_URL = SITE + URL_PATH
TITLE = "电解铝周期正在变形：产能天花板、绿电成本与三家公司的盈利分化"
DESC = "中国电解铝产能接近政策天花板后，行业逻辑从传统扩产周期转向存量产能、低价电、氧化铝成本、绿电比例和自由现金流的比较。云铝、神火与宏桥展示了三种不同的盈利结构。"
DATE = "2026-07-18"
PUB_DT = datetime(2026, 7, 18, 23, 5, tzinfo=timezone(timedelta(hours=8)))
CATEGORY = "投资研究"
SERIES = "有色金属周期"
TAGS = ["电解铝", "铝", "云铝股份", "神火股份", "中国宏桥", "宏桥控股", "氧化铝", "绿电", "低价电", "产能天花板", "周期股", "有色金属"]
MINUTES = 14
COVER = f"/images/posts/{SLUG}/cover.svg"
PREV_URL = "/2026/tianqi-lithium-35b-profit-gap-three-year-call-option/"
PREV_TITLE = "天齐锂业的三年看涨期权：35 亿中报、97 亿缺口与机构翻倍目标价"
CHANGED: set[str] = set()

ARTICLE = """
<h2 id="new-aluminum-logic">电解铝的核心变化：传统周期正在被产能天花板改写</h2>
<p>电解铝行业最重要的变化，不是某一家公司单季利润好不好，而是整个行业的供给框架发生了变化。过去的铝周期，是价格上涨、企业扩产、产能过剩、价格下跌，再进入新一轮出清。这个循环之所以反复出现，是因为供给能够较快跟随价格扩张。</p>
<p>现在的关键不同在于，中国电解铝产能已经逼近政策天花板。中国原铝产量占全球接近六成，销量也占全球六成以上；当全球最低成本、最大规模的中国供给不再继续扩张时，铝价的周期弹性会从“产能扩张压制价格”，逐步转向“存量产能享受需求增长”。</p>
<p>这并不意味着铝价从此只涨不跌，也不意味着行业完全没有波动。更准确的说法是，传统大开大合的供给周期被削弱了。未来决定企业盈利差异的，不再只是有没有产能，而是谁的电价更低、氧化铝暴露更少、绿电比例更高、资本开支是否接近尾声、加工业务是否真正挣钱。</p>
<h2 id="demand-and-supply">需求仍在增长，新增供给却越来越难</h2>
<p>铝的需求端并没有明显走弱。新能源车轻量化、电网投资、储能、光伏支架、风电部件、无人机和高端制造，都在持续增加铝的使用场景。能源革命越深入，交通、电力和制造体系对轻量化、导电性和可加工材料的需求越强。</p>
<p>供给端却没有同样顺畅。中国煤电和绿电成本在全球范围内都有竞争力，这使中国电解铝成为全球最低成本产能之一。欧洲受高电价约束，中东虽有能源成本优势，却受地缘冲突和新增产能周期影响；印尼等地新项目建设周期长、政策和资源风险也不低。</p>
<p>在这种结构下，铝价如果维持高位，并不是因为短期炒作，而是因为中国低成本产能被锁在总量约束内，新增需求只能依靠海外高成本产能、再生铝或更高价格来平衡。氧化铝则相反，随着电解铝新增产能受限，氧化铝更容易进入供给过剩和低价状态。</p>
<h2 id="profit-drivers">电解铝利润的本质：氧化铝、电力和产能位置</h2>
<p>电解铝公司的利润表，核心看两项成本：氧化铝和电力。氧化铝是全球市场定价，价格大幅波动会直接影响采购成本；电力则更依赖地区资源禀赋和政策环境，低价电能长期拉开企业间的毛利差距。</p>
<p>这也是为什么同样是电解铝公司，盈利弹性会完全不同。氧化铝价格在 2024 年高位时，拥有较多氧化铝产能的企业能赚到上游利润；但当氧化铝价格在 2025 年后回落，氧化铝资产就从利润贡献变成拖累。反过来，完全外采氧化铝的企业，在氧化铝大跌、铝价上涨时反而弹性更大。</p>
<p>电力成本的影响更长期。新疆低价电、云南绿电、山东电价、清洁能源比例和单吨电耗，都会进入最终成本。电解铝行业看起来是资源品，实质上也是能源成本竞争。企业再怎么精密制造、管理优化，如果电价不够低，盈利能力仍会落后。</p>
<h2 id="yunlv">云铝股份：最轻负担的生产型公司</h2>
<p>云铝股份的优势，是业务结构清晰、费用负担极低、绿电比例高，并且加工业务并非单纯拖累。按照年报数据，公司电解铝产量约 308 万吨，氧化铝约 140 万吨，粗略估算仍有约 240 万吨电解铝对应的氧化铝需要外采。在氧化铝大幅下跌、铝价上涨的背景下，这种结构提供了较高业绩弹性。</p>
<p>一季度的盈利增长达到约 269%，很大程度来自氧化铝成本回落叠加电解铝价格上涨。更重要的是，公司费用率极低。在约 163 亿元营收基础上，销售费用仅一千多万元，管理费用约 1.8 亿元，财务费用和研发费用也很低，合计费用率约 1.2%。因此，31% 左右的毛利率能够转化成约 25% 的净利率，几乎呈现“毛利接近净利”的状态。</p>
<p>云铝另一个容易被忽视的点，是铝加工居然能赚钱。很多铝加工业务利润薄如刀片，神火的铝箔业务几十亿元收入只贡献很低利润；但云铝 2025 年铝加工产品在约 252 亿元营收基础上贡献约 38 亿元毛利，即使把全年销售、管理、研发、财务费用和税金都压到这一块，仍有较可观营业利润。</p>
<p>这说明云铝的加工并不只是低端延伸，而是受益于合金零部件、中高端棒材、光伏棒、高品质铝锭和高精铝等产品结构提升。公司经营计划也明确继续以合金作为增长引擎。</p>
<p>云铝的资源和地域也相对清爽。铝土矿资源集中在云南文山州，并继续在云南及周边找矿，海外矿权和海外建厂风险较低。公司绿电比例约 87.5%，在行业内处于高位；依托中铝集团的原材料和销售渠道，再叠加南方电网供电支持，云铝更像一家专注生产和精密制造的低负担电解铝企业。</p>
<h2 id="shenhuo">神火股份：没有氧化铝，反而带来更高弹性</h2>
<p>神火股份的特点，是电解铝产能约 170 万吨，氧化铝基本全部外采。这个结构在氧化铝高价阶段不占便宜，但在氧化铝价格下跌时反而非常舒服。公司只参股一家氧化铝企业，对利润影响并不大，年采购量占自身需求比例也不高。</p>
<p>因此，一季度神火业绩弹性明显。氧化铝价格下跌减少成本，电解铝售价上涨提升收入，利润弹性被放大。公司一季度盈利约 22 亿元，参股氧化铝企业带来的投资收益变化在整体利润中影响有限。</p>
<p>真正的核心优势仍是新疆低价电。公司新疆和云南两块电解铝资产对比明显：云南神火在 90 万吨产能情况下，盈利能力不如 80 万吨产能的新疆煤电。即使在电解铝高价时，云南电解铝盈利能力也至少低一截；若铝价回落，低电价地区的优势会更明显。</p>
<p>神火没有明确出海计划，在当前印尼、非洲等资源地政策和项目不确定性升高的背景下，反而可以被视为稳健。公司也明确暂时没有氧化铝投资计划，避免在氧化铝产能过剩阶段逆势增加上游包袱。</p>
<p>煤炭和铝箔业务则不宜给予过高估值。煤炭业务面临资源储备少、开采条件变差、成本上升等问题，能在某些阶段贡献利润是额外红包，不能作为长期核心。铝箔业务虽有高端客户和多年积累，但产能扩张和竞争加剧导致毛利很薄。归根到底，神火最有价值的资产仍是低电价下的电解铝产能。</p>
<h2 id="hongqiao">宏桥体系：最大产能、云南布局与现金流释放</h2>
<p>宏桥体系需要分清两个层次：A 股主体的宏桥控股，核心是国内氧化铝、电解铝和部分铝加工业务；港股中国宏桥除持有 A 股主体大部分股权外，还包含国内电力、轻量化、新能源板块，以及印尼氧化铝、几内亚项目等海外业务。</p>
<p>宏桥的关键动作，是提前布局云南。国家要求到 2027 年电解铝清洁能源使用比例达到 30% 以上，而公司 2025 年电解铝产量约 654 万吨，其中云南已投产约 217 万吨，比例已经超过 30%。这意味着它在清洁能源改造上的约束相对小于许多后来者。</p>
<p>云南项目大部分已经完成，剩余投入压力在下降。云南项目累计投入约 258 亿元，超过三分之二已经完工；2026 年预计资本开支约 90 亿元，核心仍是云南区域项目。若这一轮大工程接近尾声，后续自由现金流会明显改善。</p>
<p>云南搬迁还带来所得税率变化。部分云南生产企业享受所得税优惠，生产子公司中较大比例适用 15% 及以下税率。粗略看，随着云南产能释放，公司所得税率有可能从此前较高水平下降。若以 200 亿元利润总额计算，税率下降 5 个百分点，一年就可能多释放约 10 亿元净利润。</p>
<p>宏桥还有一个很好的商业模式特征：液态铝销售占比超过六成。铝水几乎不可能形成库存，客户通常围绕产能配套，这种销售结构减少了库存压力。相比之下，深加工铝产品会有更高库存占用和跌价风险。</p>
<h2 id="green-power">绿电不是口号，而是资本开支、税率和电费的综合变量</h2>
<p>电解铝行业的绿电转型，不能只理解为环保指标。它同时影响资本开支、电价、所得税优惠、估值折扣和长期竞争力。</p>
<p>云铝绿电比例约 87.5%，已经具备非常高的清洁能源标签。宏桥通过云南布局，使清洁能源比例提前达到政策要求，并可能获得更低税率和更低电费。那些前期清洁能源改造投入不足的公司，未来一两年仍可能面临不小资本开支。</p>
<p>电费下降是否可持续，也值得持续跟踪。原材料、人工和运费大多很难由企业单方面控制，但单吨电耗下降、清洁能源使用提升、区域电价优化，都是企业可以持续推进的成本改善方向。对电解铝这种高耗能行业而言，每一分钱电费差距都会被巨大产量放大成利润差距。</p>
<h2 id="high-price-sustainability">高铝价能否持续：价格高位不等于盈利恶化</h2>
<p>市场对高铝价能否持续存在分歧。短期看，铝价高位会让下游提货和备货变得谨慎，社会库存改善也可能出现反复，股价会受到情绪和机构价格预测调整影响。但从行业利润角度看，即使部分机构微调未来两年铝价预测，全行业现金利润仍可能保持健康。</p>
<p>如果吨铝现金利润维持在 5000 元以上，电解铝公司就具备很强的分红和现金流基础。中国宏桥股息率预期达到较高水平，正是这种现金利润的体现。问题不在于铝价每天怎么波动，而在于产能天花板能否让行业盈利中枢维持在更高位置。</p>
<p>高管和产业人士能判断行业景气，但不一定能判断股价。股票短期受资金、情绪、估值切换和宏观预期影响，产业景气与股价并不总是同步。因此，对电解铝投资而言，既要跟踪行业现金利润，也不能把短期股价波动当作行业逻辑的唯一证据。</p>
<h2 id="valuation">估值框架：不要只看 PE，更要看利润质量和周期位置</h2>
<p>当前主要铝业公司的市盈率普遍不高，很多处在 8 至 10 倍区间。如果“传统铝周期弱化、行业利润中枢上移”的判断成立，这样的估值并不算高。但低 PE 不能直接等于买入理由，因为不同公司的利润质量差异很大。</p>
<p>云铝的优势在于费用低、绿电比例高、加工业务质量较好、集团体系支持强。神火的优势在于外采氧化铝带来的成本弹性，以及新疆低价电构成的长期护城河。宏桥的优势在于规模最大、云南布局接近完成、液态铝销售占比高、未来自由现金流改善空间大。</p>
<p>需要回避的是给非核心业务过高估值。煤炭、铝箔、普通深加工、氧化铝高价阶段的临时利润，都不应被简单线性外推。真正应当高估值的，是在产能受限、低电价、低资本开支和高现金流条件下稳定释放利润的电解铝资产。</p>
<h2 id="strategy">买入策略：用行业逻辑定方向，用公司结构选标的</h2>
<p>电解铝板块的买入策略，可以拆成三层。</p>
<p>第一层，看行业逻辑。只要中国电解铝产能天花板不松动，新能源、电网、储能和高端制造需求继续增长，行业利润中枢就有机会维持在过去周期经验之上。若政策突然放松产能，或者需求端连续走弱，这个逻辑就需要重新评估。</p>
<p>第二层，看成本结构。低电价、绿电比例、氧化铝暴露和资本开支，是筛选公司的核心指标。氧化铝下行阶段，外采氧化铝的电解铝公司弹性更高；电价越低，低铝价环境下安全垫越厚；绿电比例越高，未来政策约束和改造支出越小。</p>
<p>第三层，看现金流和分红。电解铝产能受限后，最优秀的公司应当逐步从资本开支扩张型企业，转向高现金流、高分红、低负担的存量资产运营企业。宏桥云南项目接近尾声、云铝费用极低、神火不盲目上氧化铝和海外项目，都是值得放进现金流框架里观察的信号。</p>
<h2 id="risk">风险：没有周期，不等于没有波动</h2>
<p>“没有铝周期”更像一种方向判断，而不是字面意义上的价格永不下跌。短期库存、下游提货、宏观需求、出口政策、机构铝价假设、海外地缘冲突、氧化铝价格、煤电价格和资金风格，都会让股价剧烈波动。</p>
<p>如果社会库存持续累积、下游高价备货意愿下降、铝价跌破行业现金利润舒适区，或者产能政策发生变化，板块估值都可能被重新定价。若企业仍有大额海外项目、清洁能源改造支出或非核心业务拖累，也会削弱投资回报。</p>
<p>因此，电解铝投资的关键不是喊出“周期结束”，而是持续验证三件事：产能天花板是否仍然有效，需求增长是否仍能吸收存量供给，企业成本结构是否足够优秀。只有这三件事同时成立，低估值才有可能转化为长期收益。</p>
<h2 id="conclusion">结论：寻找最干净、最低成本、最能分红的电解铝资产</h2>
<p>电解铝行业正在从传统周期品，向带有资源约束和现金流属性的存量行业过渡。产能天花板削弱了无序扩产，新能源和电力系统需求支撑了长期消费，低价电和绿电比例决定了企业盈利分层。</p>
<p>云铝股份代表的是低费用、绿电高比例和加工质量改善；神火股份代表的是外采氧化铝带来的利润弹性和新疆低价电优势；宏桥体系代表的是最大规模、云南绿电布局和资本开支接近尾声后的现金流释放。</p>
<p>真正值得关注的，不是所有铝业公司一起买，而是在同一行业逻辑下筛选最干净、最低成本、最少负担、最能持续分红的电解铝资产。产能不再无限扩张之后，行业的胜负手从“谁扩得快”变成“谁的存量产能最优质”。</p>
<p>本文仅基于公开信息进行分析，不构成任何投资建议。周期股仍然有价格波动和估值回撤风险，仓位管理和持续跟踪比单次判断更重要。</p>
"""


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def rec(path: Path) -> None:
    CHANGED.add(path.relative_to(ROOT).as_posix())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    rec(path)


def term_url(kind: str, term: str) -> str:
    return f"/{kind}/{quote(term)}/"


def meta_links() -> str:
    cat = f'<a href="{term_url("categories", CATEGORY)}">{esc(CATEGORY)}</a>'
    tags = "&nbsp;".join(f'<a href="{term_url("tags", tag)}">{esc(tag)}</a>' for tag in TAGS)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {MINUTES} min'


def build_toc() -> str:
    links = [
        f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>'
        for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', ARTICLE)
    ]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + "".join(links) + "</nav></div></div>"


def cover_svg() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f172a"/><stop offset="0.48" stop-color="#334155"/><stop offset="1" stop-color="#0f766e"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.34"/></filter></defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.15" stroke="#e2e8f0" stroke-width="3"><path d="M130 690 H1470"/><path d="M130 560 H1470"/><path d="M130 430 H1470"/><path d="M130 300 H1470"/><path d="M340 235 V760"/><path d="M660 235 V760"/><path d="M980 235 V760"/><path d="M1300 235 V760"/></g>
  <g filter="url(#shadow)">
    <path d="M190 625 C355 585 450 500 590 520 C765 545 850 355 1020 355 C1180 355 1260 265 1410 215" fill="none" stroke="#f59e0b" stroke-width="18" stroke-linecap="round"/>
    <rect x="132" y="606" width="768" height="118" rx="24" fill="#f8fafc" opacity="0.96"/>
    <text x="176" y="678" fill="#0f766e" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800">产能天花板 × 低价电 × 绿电</text>
    <circle cx="1115" cy="535" r="88" fill="#22c55e" opacity="0.88"/>
    <circle cx="1270" cy="455" r="88" fill="#38bdf8" opacity="0.84"/>
    <circle cx="1398" cy="350" r="88" fill="#f97316" opacity="0.86"/>
  </g>
  <text x="96" y="150" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="58" font-weight="800">{esc(TITLE)}</text>
  <text x="100" y="236" fill="#ccfbf1" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">云铝 · 神火 · 宏桥</text>
  <text x="102" y="312" fill="#e0f2fe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="600">传统扩产周期弱化后，谁的存量产能更优质</text>
</svg>'''


def build_article() -> None:
    template = (ROOT / PREV_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    start = template.find('<article class="post">')
    end = template.find("</article>", start) + len("</article>")
    head, tail = template[:start], template[end:]
    replacements = {
        r"<title>.*?</title>": f"<title>{esc(TITLE)} - zcxGGmu's Blog</title>",
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(DESC)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(FULL_URL)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(TITLE)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(DESC)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(FULL_URL)}">',
    }
    for pattern, repl in replacements.items():
        head = re.sub(pattern, repl, head, flags=re.S)
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{COVER}')"><div class="post-title">{esc(TITLE)}<div class="post-subtitle">{esc(DESC)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links()}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{ARTICLE}</div></div><nav class="post-pagination"><a class="newer-posts">下一篇<br>没有更新的文章</a><a class="older-posts" href="{PREV_URL}">上一篇<br>{esc(PREV_TITLE)}</a></nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(), tail, flags=re.S)
    write(ROOT / "2026" / SLUG / "index.html", head + article + tail)


def update_prev() -> None:
    path = ROOT / PREV_URL.strip("/") / "index.html"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>',
        f'<a class="newer-posts" href="{URL_PATH}">下一篇<br>{esc(TITLE)}</a>',
        text,
        count=1,
        flags=re.S,
    )
    write(path, text)


def home_card() -> str:
    return f'''<a href="{URL_PATH}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(TITLE)}</div>
            <div class="post-item-summary">{esc(DESC)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {MINUTES} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{COVER}')"></div></div>
        </div>
      </div>
    </a>'''


def update_home() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = re.sub(rf'<a href="{re.escape(URL_PATH)}" class="a-block">.*?</a>\s*', "", text, flags=re.S)
    pos = text.find(f'<a href="{PREV_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError("homepage insertion marker not found")
    write(path, text[:pos] + home_card() + "\n" + text[pos:])


def update_rss() -> None:
    path = ROOT / "index.xml"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{format_datetime(PUB_DT)}</lastBuildDate>", text)
    text = re.sub(rf"<item>\s*<title>{re.escape(esc(TITLE))}</title>.*?</item>\s*", "", text, flags=re.S)
    item = f'''<item>
<title>{esc(TITLE)}</title>
<link>{FULL_URL}</link>
<guid>{FULL_URL}</guid>
<pubDate>{format_datetime(PUB_DT)}</pubDate>
<description>{esc(DESC)}</description>
</item>
'''
    write(path, text.replace("<item>", item + "<item>", 1))


def update_archive() -> None:
    path = ROOT / "archive/index.html"
    text = path.read_text(encoding="utf-8")
    if URL_PATH not in text:
        text = re.sub(
            r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>',
            lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + 1} 篇</span>',
            text,
            count=1,
        )
    text = re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(URL_PATH)}">.*?</div>\s*', "", text, flags=re.S)
    item = f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{URL_PATH}">{esc(TITLE)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(CATEGORY)}</span></span>
      </div> '''
    pos = text.find(f'<a href="{PREV_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    write(path, text[:start] + item + text[start:])


def tax_item() -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''


def update_term_index(kind: str, term: str, delta: int) -> None:
    if not delta:
        return
    path = ROOT / kind / "index.html"
    text = path.read_text(encoding="utf-8")
    href = f"/{kind}/{quote(term)}/"
    if href in text:
        pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span style="color:#999[^>]*>\()(\d+)(\)</span></a>)')
        text = pattern.sub(lambda m: f"{m.group(1)}{int(m.group(2)) + delta}{m.group(3)}", text, count=1)
    else:
        if kind == "tags":
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">(1)</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">(1)</span></a>\n'
        pos = text.find("</div></div></div>")
        text = text[:pos] + item + text[pos:]
    write(path, text)


def update_term(kind: str, term: str, prefix: str, emoji: str) -> None:
    path = ROOT / kind / term / "index.html"
    if path.exists():
        old = path.read_text(encoding="utf-8")
        inserted = 0 if URL_PATH in old else 1
        text = re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(URL_PATH)}".*?</div>\s*', "", old, flags=re.S)
        if inserted:
            text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + 1} 篇文章", text, count=1)
        first = text.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
        if first == -1:
            first = text.find("</div></div></div>")
        text = text[:first] + tax_item() + text[first:]
    else:
        inserted = 1
        label = f"{prefix}: {term}" if prefix else term
        h1 = f"{emoji} {term}" if emoji else label
        text = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p>{tax_item()}</div></div></div><script src="/js/journal.js"></script></body></html>'''
    write(path, text)
    update_term_index(kind, term, inserted)


def update_taxonomies() -> None:
    update_term("categories", CATEGORY, "分类", "")
    update_term("series", SERIES, "", "📚")
    for tag in TAGS:
        update_term("tags", tag, "标签", "🏷️")


def validate() -> None:
    failures: list[str] = []
    forbidden = ["B站", "bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主", "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅", "欢迎回到", "下次再见", "公众号"]
    article = (ROOT / URL_PATH.strip("/") / "index.html").read_text(encoding="utf-8")
    for word in forbidden:
        if word in article:
            failures.append(f"forbidden {word}")
    for must in [TITLE, "电解铝", "产能天花板", "云铝股份", "神火股份", "中国宏桥", "宏桥控股", "氧化铝", "绿电", "低价电"]:
        if must not in article:
            failures.append(f"missing {must}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links:
        failures.append("toc mismatch")
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    order = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)[:7]
    expected = [
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
        URL_PATH,
        PREV_URL,
    ]
    if order != expected:
        failures.append(f"home order mismatch {order}")
    ET.parse(ROOT / "index.xml")
    for path in [
        ROOT / "archive/index.html",
        ROOT / "categories" / CATEGORY / "index.html",
        ROOT / "series" / SERIES / "index.html",
        ROOT / "tags" / TAGS[0] / "index.html",
        ROOT / "images/posts" / SLUG / "cover.svg",
    ]:
        if not path.exists():
            failures.append(f"missing {path}")
        elif path.suffix == ".html" and URL_PATH not in path.read_text(encoding="utf-8"):
            failures.append(f"{path} missing url")
    previous = (ROOT / PREV_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    if URL_PATH not in previous:
        failures.append("previous article newer link missing")
    if failures:
        raise SystemExit("\n".join(failures))
    print("validation passed")


def publish_changed_list() -> None:
    rec(ROOT / "tasks/publish-aluminum-cycle-capacity-cost-comparison-article.py")
    changed_path = ROOT / "tasks/publish-aluminum-cycle-capacity-cost-comparison-changed-files.json"
    all_changed = sorted(CHANGED | {"tasks/publish-aluminum-cycle-capacity-cost-comparison-article.py", "tasks/publish-aluminum-cycle-capacity-cost-comparison-changed-files.json"})
    write(changed_path, json.dumps(all_changed, ensure_ascii=False, indent=2))
    print(json.dumps({"url": FULL_URL, "changed": len(all_changed)}, ensure_ascii=False, indent=2))


def main() -> None:
    write(ROOT / "images/posts" / SLUG / "cover.svg", cover_svg())
    build_article()
    update_prev()
    update_home()
    update_rss()
    update_archive()
    update_taxonomies()
    validate()
    publish_changed_list()


if __name__ == "__main__":
    main()
