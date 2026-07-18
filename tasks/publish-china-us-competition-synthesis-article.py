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
SLUG = "china-us-competition-institutional-synthesis"
URL_PATH = f"/2026/{SLUG}/"
FULL_URL = SITE + URL_PATH
TITLE = "中美长期竞争的底层逻辑：中国为何可能走出新的制度合成"
DESC = "中美竞争不是两个国家的单点较量，而是国力结构、同盟体系、货币财政、公共部门效率和文明制度基因之间的长期竞争。中国真正的胜负手，在于把动员能力与市场活力合成为一种新模式。"
DATE = "2026-07-18"
PUB_DT = datetime(2026, 7, 18, 21, 20, tzinfo=timezone(timedelta(hours=8)))
CATEGORY = "社会观察"
SERIES = "大国竞争"
TAGS = ["中美竞争", "全球秩序", "同盟体系", "制度比较", "公共部门", "财政赤字", "货币体系", "民本主义", "战略思维", "再分配", "全球化", "国家能力"]
MINUTES = 12
COVER = f"/images/posts/{SLUG}/cover.svg"
PREV_URL = "/2026/korea-stock-market-ai-leverage-fomo-bubble-review/"
PREV_TITLE = "韩国股市疯狂牛市复盘：AI 叙事、杠杆散户与人性泡沫"
CHANGED: set[str] = set()

ARTICLE = """
<h2 id="power-structure">世界国力分布不是均匀的，而是强者恒强</h2>
<p>观察当今世界力量格局，最重要的不是把国家一字排开，而是理解国力分布本身的结构。许多关键指标都呈现出类似马太效应的状态：第一名占据巨大空间，第二名占据剩余空间中的相当部分，再往后的国家则挤在很窄的区间里。这种结构看起来不平衡，但在真实世界中反而常常是一种稳定均衡。</p>
<p>在 GDP、财政开支、军费开支、互联网平台、独角兽企业、线上经济、顶级大学、博士学位、顶尖学者、研发投入、国际专利、人工智能和先进装备等多个维度上，美国仍然保持第一，中国紧随其后，两者与其他经济体之间存在明显断层。美国仍有许多领先指标，中国也在越来越多指标上接近或超过美国。</p>
<p>也有一些领域，中国仍未真正成为全球第二。例如全球舆论影响力、国际组织影响力，以及货币金融体系中的国际化程度。美元仍占据全球货币体系的核心地位，欧元次之，人民币、日元和英镑处在更低层级。这些领域的落后，并不代表中国综合国力不足，而是因为历史发力较晚，制度和网络外部性积累还不够。</p>
<p>与此同时，中国在出口贸易、国内消费市场、理工科大学生规模、中等收入群体、汽车市场、智能手机销售、互联网接入用户、制造业增加值、B2C 互联网业务、无人机、高超音速装备、能源消费、资源消耗、全球 500 强企业席位和 5G 技术等方面，已经超过美国或正在快速接近。一旦这些指标完成反超，并不会长期停留在并驾齐驱状态，而可能进入中国一家独大的新结构。</p>
<h2 id="two-centers">世界未必走向多极化，反而正在形成双中心</h2>
<p>中国长期主张世界多极化，但现实未必真正朝多极化发展。更准确地说，世界正在形成两个明显中心：以美国为中心的体系，以及以中国为中心的体系。其他力量虽然重要，却大多不是全面型力量。</p>
<p>俄罗斯在军事领域仍是重要玩家，但经济体量不足；欧洲在政治席位、意识形态和国际组织中有影响力，但缺乏统一的战略执行能力；印度拥有巨大人口规模，但现代化竞争中真正重要的不是总人口，而是受过较好教育、能够参与全球市场分工和竞争的中产阶级人口规模与质量。若社会改造、教育体系和产业组织能力跟不上，人口规模本身不能直接转化为国力。</p>
<p>中美不同之处在于，两者都是政治、经济、科技、教育、文化、军事等多领域的全面型、全球型力量。因此，真正决定未来世界秩序的，不是某个单一指标的排名，而是中美两个全面体系谁能在更长周期内保持组织能力、创新能力、财政能力、产业能力和联盟能力。</p>
<h2 id="before-after-2035">2035 前后，战略心态应当发生切换</h2>
<p>中美竞争的时间维度不能只看眼前。到 2035 年前，美国及其盟友总体上仍会给人相对占优的感觉。这个阶段，中国最重要的是坚定信心、敢于竞争、敢于出招，不被对方的舆论、金融、军事和同盟体系压力吓住。</p>
<p>但如果到 2035 年后，美国出现一系列深度去杠杆过程，内部治理、外部阵营、财政金融结构都发生明显倒退，中国的心态反而要转向谦逊、谨慎和适可而止。强者真正危险的时刻，不是尚未取胜时，而是看似即将彻底取胜时。历史上有许多战术成功导致战略困境的教训。</p>
<p>一个大国追求的，不应是一切人反对一切人的丛林状态，也不应是把某个对手斩尽杀绝后的复仇式胜利。真正有利的世界格局，是超支配的大国均衡与共生状态。尤其在 2035 年至 2050 年之间，如果美国权势明显衰退，其他大国关系也可能发生不利翻转。越是在优势扩大时，越要避免战略过度扩张。</p>
<h2 id="alliance-system">美国真正的优势，是同盟体系这个杠杆</h2>
<p>中美竞争不是两个国家之间的单独竞争，而是两个体系之间的竞争。美国对外行动常常以“盟友利益”为理由，它擅长把自身意志包装在同盟体系中，通过盟友网络分摊成本、扩大影响、制造合法性。</p>
<p>美国同盟体系有类似罗马同盟大战略的特征。罗马击败对手后，常常迅速提供协议：成为我的盟友，我提供和平与繁荣，别人欺负你时报我名字；但当我去征服别人时，你也要加入我的阵营。进入这个体系之后，每个盟友都与盟主保持依附性友好关系，但盟友之间并不一定相互友好，甚至经常存在矛盾，而盟主恰恰通过操控这些矛盾维持中心地位。</p>
<p>今天美国在东亚的体系也有类似特点。日本与韩国之间存在矛盾，韩国与中国之间存在矛盾，日本与中国之间也存在矛盾，许多矛盾并非自然消失，而是被中心国家精心维持。过去中国一度深度嵌入这一体系，如今正在从其中独立出来，新的阵营关系也在悄然浮现。</p>
<p>美国最大的战略失误之一，是在赢得冷战后，没有避免中俄形成背靠背的战略协作。美国许多战略思想家曾反复强调，必须防止中俄联手，但现实却是美国的自大与战略错误，把两个有漫长边界和深层安全关切的大国推向更紧密的协作。</p>
<h2 id="leverage-analogy">同盟体系本质上也是一种杠杆</h2>
<p>美国同盟体系不仅是政治结构，也是杠杆结构。美国利用货币体系获取全球财富，是金融杠杆；利用同盟体系放大自身力量，是战略杠杆。中美竞争中，中国主要依靠自己的资源、产业、储备和能力，而美国则把欧洲、日本、韩国、澳大利亚等盟友都拉入其体系。</p>
<p>表面看，双方处于均衡状态。但若用金融市场的语言理解，美国一方其实带有更高杠杆。多空双方对峙时，若一方主要靠自有资金，另一方必须不断加杠杆、借外部力量维持均衡，那么后者的处境更脆弱。只要时间拉长，杠杆成本就会不断上升。</p>
<p>一旦中国也开始更主动地使用自己的外部关系、伙伴体系和经济影响力，美国同盟体系中的薄弱环节就可能承压。美国对某一个盟友的安全承诺或经济承诺，一旦无法兑现，就可能损害其对所有盟友的战略信用。类似金融机构爆仓，杠杆越高，信任断裂越快。</p>
<p>对付高杠杆对手，不一定要正面硬碰硬。更有效的方式，是让其使用杠杆的边际成本不断上升。盟友会向美国索取利息、补偿和安全承诺；当这些成本超过美国从盟友身上获得的收益，同盟体系就会从资产变成负债。</p>
<h2 id="domestic-redistribution">真正的内功，是做好国内再分配</h2>
<p>大国竞争不能只看外部博弈。中国必须做好国内自己的事情，而这里最重要的，是再分配和结构调整。第一层再分配，是中央与地方之间的再分配。中央政府应该主动承担更多低利率、长期限债务，利用自己的国内外信用创造更稳定的国债体系；地方政府则应减少高息债务负担。</p>
<p>1971 年之后，世界进入信用货币时代。黄金不再是货币体系核心，大国主权信用成为货币创造的基础。在这种体系中，中央政府适度增加长期低息国债，本身就是在创造金融资产、创造货币锚，并为实体产能提供匹配的虚拟经济基础。若中国实体产能已经足够强，却仍主要依赖外部需求和外部主权信用来吸纳产出，就会被他国货币体系牵制。</p>
<p>第二层再分配，是区域之间的再分配。东南沿海应向内地、北方进行更多转移支付，以平衡产业、人口和财政能力差异。第三层调整，是央行资产负债表结构。中国应逐渐减少对外汇储备的依赖，减少对美欧日国债的持有，把更多资源投向一带一路沿线的股权和债权，尤其是股权投资，与外围地区年轻人和增长潜力更深地绑定。</p>
<h2 id="money-wealth-cognition">走出重商主义的财富错觉</h2>
<p>中国社会还需要改变对货币和财富的认知。贫穷带来的伤害至少有两轮：第一轮是匮乏本身的痛苦，第二轮是匮乏记忆和恐惧导致的行为扭曲。个人会非理性地执着于金钱，国家也可能陷入对外汇、顺差和外部债务承诺的过度执着。</p>
<p>在贵金属本位时代，一个国家多积累黄金白银还有一定政策价值，因为贵金属价值相对稳定。但 1971 年之后，世界进入无锚货币时代，货币价值基础变成其他国家的主权信用。在这种背景下，如果继续用本土资源、年轻人的时间和劳动，去换取别国可以低成本无限创造的货币，就不再是精明，而是短视。</p>
<p>一旦摆脱重商主义的贪婪和愚蠢，愿意接受本币计价下适度财政赤字，愿意放弃每年几千亿美元贸易盈余的执念，中国国内市场规模就可能出现数倍扩张。真正的大国，不应只追求成为他国消费体系的供应商，而应让自身主权信用、国内市场和产业能力形成闭环。</p>
<h2 id="dao-and-institution">大国竞争还有“道”的层面</h2>
<p>中美长期竞争，不只发生在 GDP、军费、科技和贸易数据上，也发生在制度与文明层面的精神特质上。美国制度源自新教文明和海洋文明，底层逻辑是个体价值本位和自下而上的自由选择。政治上表现为选举政治和三权分立，经济上表现为私有产权和自由市场。</p>
<p>与之相对，人类文明中长期存在另一类大陆色彩更强的制度关系。它强调集体价值本位，把国家、社会和民族视为生命有机体，个体则是有机体中的细胞。因此，它更重视自上而下的管控、分配和动员，更强调整体目标、组织能力和危机应对。</p>
<p>这两类制度逻辑在人类历史上长期竞争。西方可以追溯到古希腊与古波斯的对立，中国古代可以追溯到春秋战国时期不同治国之道的竞争。商鞅变法代表自上而下的机体本位，管仲之治则更强调商业竞争和市场逻辑。20 世纪后半期，美苏冷战也体现了市场竞争逻辑与组织动员逻辑之间的较量。</p>
<h2 id="soviet-american-synthesis">中国的独特性：学习苏联，也学习美国</h2>
<p>1949 年之后，中国经历了非常特殊的制度学习过程。前 30 年学习苏联的动员体制，建立自上而下的社会组织能力，形成强大的国家机器。后 30 年学习美国及其盟友的市场经济经验，释放私人部门活力，成为全球最大的工业国、贸易国、债权国、消费市场之一。</p>
<p>前 30 年的意义，是把公共部门能力的底边建立起来。传统农业社会往往是小政府，国家能力相对社会较弱，王权对底层社会的控制力有限。建国之后，中国建立起能够有效组织、动员和提供公共产品的国家机器，这使得安全、基础设施、教育、工业体系和社会治理能力迅速提升。</p>
<p>但苏联体制的问题，是综合税点过高。为了提供公共产品，公共部门占用社会资源过多，私人部门投射出来的经济活动就会很小。后 30 年学习市场经济，把综合税点大幅拉低，于是庞大、复杂、繁荣的私人部门得以成长。</p>
<p>因此，不能用前 30 年否定后 30 年，也不能用后 30 年否定前 30 年。更重要的是看到两者各自的不完美。新时代真正的任务，是把强大的公共部门与繁荣的私人部门结合起来，把苏联式动员能力和美国式市场活力合成为新的制度形态。</p>
<h2 id="public-private-triangle">公共部门越强、效率越高，私人部门空间越大</h2>
<p>理解国家与市场关系，可以用一个三角结构：底边是公共部门提供的公共产品，上方是私人部门能够展开的经济活动。一个国家发展得好不好，关键取决于公共部门两个特质。</p>
<p>第一，公共部门能做的事越多越好，国家能力越强越好，也就是底边越长越好。底边越长，私人部门能够在其上展开的经济活动越多。没有安全、基础设施、教育、法治、能源、通信和产业政策，私人部门很难凭空繁荣。</p>
<p>第二，公共部门效率越高越好，也就是综合税点越低越好。如果公共部门为了提供公共产品消耗过多社会资源，私人部门就会被挤压。理想状态不是小政府或大政府的简单二分，而是强能力、高效率的公共部门，支撑广阔而有活力的私人部门。</p>
<p>中国的制度合成之所以重要，正在于它试图同时拥有这两个优势：既保留强大的组织动员和公共产品供给能力，又保留市场经济带来的竞争、创新和效率。若这一合成能够完成，中国就可能在长期竞争中形成不同于美国、也不同于苏联的新模式。</p>
<h2 id="final-thesis">胜负手不是简单超越美国，而是创造新的模式</h2>
<p>中国为何可能在中美长期竞争中胜出？答案不只是人口多、制造业强、市场大、工程师多，也不只是某些指标正在反超美国。更深层的答案，是中国同时具有“道”的优势和“质”的优势：既有庞大的实体经济、产业体系、中等收入群体和工程技术人才，也有把不同制度基因重新组合的历史机缘。</p>
<p>真正的挑战，是避免两种错误。一种错误，是在落后时缺乏勇气，不敢竞争、不敢出招；另一种错误，是在优势扩大后过度自信，陷入复仇冲动和战略扩张。前者会错失历史窗口，后者会制造新的长期困境。</p>
<p>未来的竞争，不是把美国模式复制一遍，也不是回到苏联模式，而是建立一种新的合成：强大的公共部门、低成本的主权信用、深度的国内市场、繁荣的私人部门、有效的再分配，以及更有耐心的外部伙伴体系。这样的模式如果能够成熟，中国赢得长期竞争就不只是规模问题，而是制度创造力问题。</p>
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
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f172a"/><stop offset="0.52" stop-color="#7f1d1d"/><stop offset="1" stop-color="#b45309"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.34"/></filter></defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.14" stroke="#f8fafc" stroke-width="3"><path d="M130 690 H1470"/><path d="M130 560 H1470"/><path d="M130 430 H1470"/><path d="M130 300 H1470"/><path d="M340 235 V760"/><path d="M660 235 V760"/><path d="M980 235 V760"/><path d="M1300 235 V760"/></g>
  <g filter="url(#shadow)">
    <circle cx="460" cy="570" r="120" fill="#dc2626" opacity="0.92"/><circle cx="1120" cy="430" r="120" fill="#2563eb" opacity="0.88"/>
    <path d="M560 560 C710 405 865 595 1020 440" fill="none" stroke="#fde68a" stroke-width="16" stroke-linecap="round"/>
    <rect x="102" y="612" width="650" height="112" rx="24" fill="#fff7ed" opacity="0.96"/>
    <text x="146" y="683" fill="#991b1b" font-family="Noto Sans SC, PingFang SC, Arial" font-size="40" font-weight="800">动员能力 × 市场活力</text>
  </g>
  <text x="96" y="150" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="58" font-weight="800">{esc(TITLE)}</text>
  <text x="100" y="236" fill="#ffedd5" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">国力结构 · 同盟杠杆 · 制度合成</text>
  <text x="102" y="312" fill="#e0f2fe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="600">长期竞争的胜负手，是创造一种更有效的新模式</text>
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
    for must in [TITLE, "中美竞争", "2035", "同盟体系", "公共部门", "无锚货币", "苏联", "市场经济", "制度合成"]:
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
    rec(ROOT / "tasks/publish-china-us-competition-synthesis-article.py")
    changed_path = ROOT / "tasks/publish-china-us-competition-synthesis-changed-files.json"
    all_changed = sorted(CHANGED | {"tasks/publish-china-us-competition-synthesis-article.py", "tasks/publish-china-us-competition-synthesis-changed-files.json"})
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
