from __future__ import annotations

import base64
import html
import json
import re
import subprocess
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path("/tmp/hermes-video-publish")
SITE = "https://zcxggmu.github.io"
SLUG = "korea-stock-market-ai-leverage-fomo-bubble-review"
URL_PATH = f"/2026/{SLUG}/"
FULL_URL = SITE + URL_PATH
TITLE = "韩国股市疯狂牛市复盘：AI 叙事、杠杆散户与人性泡沫"
DESC = "韩国股市从折价修复走向 18 个月 2.75 倍的狂热行情，AI 存储超级周期、政策背书、外资唱多与散户杠杆共同放大泡沫，也提供了识别顶部风险的经典样本。"
DATE = "2026-07-18"
PUB_DT = datetime(2026, 7, 18, 20, 25, tzinfo=timezone(timedelta(hours=8)))
CATEGORY = "投资研究"
SERIES = "海外市场观察"
TAGS = ["韩国股市", "AI", "存储芯片", "三星", "SK海力士", "杠杆", "FOMO", "泡沫", "散户", "华尔街", "估值", "风险控制"]
MINUTES = 10
COVER = f"/images/posts/{SLUG}/cover.svg"
PREV_URL = "/2026/coal-sector-right-side-seasonal-rebound/"
PREV_TITLE = "煤炭板块的右侧机会：800 元底部、旺季反弹与高股息修复"
CHANGED: set[str] = set()

ARTICLE = """
<h2 id="opening-thesis">活生生的泡沫样本，比历史教科书更有价值</h2>
<p>韩国股市这一轮行情，是一个正在发生的经典案例。它的疯狂程度，很容易让人联想到 A 股 2015 年的那轮疯牛：真实产业逻辑、政策叙事、全球资金、全民情绪、杠杆交易同时叠加，最终把一个原本有基本面支撑的行情，推向失控状态。</p>
<p>复盘这种案例的价值，不在于事后嘲笑谁愚蠢，也不在于把一切解释成阴谋。资本市场里最重要的力量，始终是人性。机构、外资、投行、政策叙事都只是推波助澜的角色，真正把泡沫推到极致的，是“这次不一样”的信念，是害怕错过的焦虑，是散户对完美故事的追逐。</p>
<p>这轮韩国股市大牛市并不是凭空出现的。AI 对存储芯片需求爆发是真实的，三星和 SK 海力士在高带宽存储领域的全球地位也是真实的，韩国政府推动企业价值提升和分红回购也是真实的。但真实逻辑不等于合理价格，更不等于任何价格都可以买入。泡沫最危险的地方，恰恰在于它通常建立在一个真实故事之上。</p>
<h2 id="korea-discount-reversal">从韩国折价到 18 个月 2.75 倍</h2>
<p>在 2025 年之前，韩国股市长期处在所谓“韩国折价”之中。公司治理、财阀结构、分红回购不足、市场透明度等问题，让韩国资产长期被全球投资者打折定价。这个折价本身为后续行情提供了修复空间。</p>
<p>2025 年之后，韩国股市直接起飞，走出史无前例的行情。韩国综合指数在大约 18 个月内上涨 2.75 倍，进入冲顶阶段后，走势像脱缰野马一样失控。2026 年单年度出现 7 次熔断，超过韩国股市此前历史上许多年累计熔断次数。一个指数在半年内频繁熔断，说明它已经不再是正常上涨，而是进入极端波动和情绪失控状态。</p>
<p>行情最初的驱动是合理的。AI 训练和推理需求带动 HBM 等高端存储需求爆发，三星与 SK 海力士是全球少数能大规模量产高带宽存储的厂商，两家公司垄断全球绝大部分高端存储供给，订单甚至排到 2028 年以后。对应到财务报表上，是利润快速改善和盈利预期大幅上修。</p>
<p>第二个引擎来自政策。韩国政府推出企业价值提升计划，鼓励分红、回购和公司治理改善，后来又提出国民分红构想。政策把估值修复从市场逻辑变成国家叙事，点燃了散户情绪。第三个引擎是叙事共振：真实业绩爆发、政府政策背书、投行持续唱多、全球资本寻找 AI 资产，四个因素同时发生，大量资金涌入，价格自然不断上升。</p>
<h2 id="index-concentration">指数被两家公司绑架，是繁荣也是风险</h2>
<p>韩国股市最异常的地方，是指数集中度过高。三星和 SK 海力士两家公司合计超过韩国综合指数一半以上市值，权重一度达到约 60%。一个国家的股票指数被两家公司深度绑定，本身就是非常反常、非常危险的结构。</p>
<p>高集中度在上涨阶段会放大利好。只要 AI 存储逻辑继续强化，只要三星和 SK 海力士继续上涨，整个指数就会被强行拉高，指数基金、被动资金、趋势资金都会进一步涌入。但同样的结构在下跌阶段会放大风险。一旦这两家公司出现估值回落、业绩低于预期或被动基金因单一持仓上限被迫减仓，整个指数都会被拖入剧烈波动。</p>
<p>指数集中度的危险并不只属于韩国。任何市场在牛市后期都会出现类似现象：龙头市值不断突破万亿，市场不断讲述“某某公司超越茅台”“某某行业诞生十万亿公司”的故事，指数权重不断向少数公司集中。集中度提升会让上涨看起来更有力量，也会让下跌来得更猛烈。</p>
<h2 id="wall-street-playbook">一边上调目标，一边高位卖出</h2>
<p>这一轮行情中，华尔街和全球投行扮演了典型角色：早期推动叙事，中期制造信心，后期一边唱多一边卖出。摩根大通、瑞银、高盛等机构不断上调韩国指数目标位，目标从 9200 点、10000 点、12000 点一路被喊到 15000 点。密集上调目标价的同时，实际资金却在净流出。</p>
<p>外资高位净卖出约 148 万亿韩元。表面上看，有些统计口径下外资持股比例并未明显下降，甚至略有上升，但这是一种统计幻觉：因为指数涨得太快，持仓市值膨胀速度超过了卖出速度。真正看三星、SK 海力士等核心公司的外资持股数量变化，可以看到明显下降。贝莱德韩国 ETF 单周也出现约 7 亿美元流出。</p>
<p>机构话术非常典型：韩国折价仍有修复空间，估值仍不算贵，剔除三星和 SK 海力士后动态市盈率只有 12 倍，ROE 将达到创纪录水平。这些说法并非完全没有道理，但关键在于权重最大的恰恰就是三星和 SK 海力士；当 ROE 已经极其好看时，往往意味着盈利已经充分兑现，价格也很可能已经透支了未来。</p>
<p>这不是新鲜剧本。机构在低位建仓，高位创造叙事，密集唱多帮助形成流动性，然后在散户冲进来时加速出货。把它简单理解为阴谋论并不准确，它更像资本市场的常规机制：专业资金更理性，散户更容易被故事打动；专业资金需要流动性离场，而高位最好的流动性，往往来自“再也没有机会”的全民狂热。</p>
<h2 id="retail-mania">全民炒股与杠杆狂热，把牛市推成绞肉机</h2>
<p>韩国散户的参与程度极高。一个约 5100 万人口的国家，活跃股票账户达到约 1 亿个，人均接近两个账户；还有大量未成年人持股。程序员把大部分资产投入股市，退休老人解约保险、退保入市，父母为婴儿开设股票账户，企业员工拿到奖金后继续投入股市。总统提出国民分红构想，也为这场全民狂欢提供了更强背书。</p>
<p>当最不该进入股市的钱也进入股市时，风险就已经非常高。养老钱、保险钱、家庭长期安全垫，本来不应该承受极高波动，但在 FOMO 情绪下，这些资金也会被卷入市场。更危险的是加杠杆。韩国投资者不仅买股票，还用信用贷款、融资、单一股票杠杆 ETF 等方式放大风险。</p>
<p>结果是剧烈波动下的大面积伤害。2026 年韩国股市半年出现 7 次熔断，而韩国股市历史熔断总次数本来并不多。对没有杠杆的人来说，指数回调十几个点已经很难受；对高位加仓、融资买入、借钱炒股的人来说，十几个点的指数回撤可能对应三四十个点甚至更大的账户损失。熔断不是简单的市场新闻，而是加杠杆者的财富绞肉机。</p>
<h2 id="who-buys-who-sells">谁在买，谁在卖</h2>
<p>顶部区域最重要的问题，不是故事讲得多好，而是谁在买、谁在卖。韩国这轮行情中，机构和外资在高位不断减仓，而散户和融资资金继续买入。外资卖出并不神秘：估值已经离谱，被动基金存在单一持仓上限，主动资金也有获利了结需求。真正承担接盘力量的，是相信完美叙事的散户。</p>
<p>散户继续买入，是因为故事太动人：AI 超级周期刚刚开始，全球高端存储供不应求，韩国政府亲自背书，投行目标点位不断上调，如果现在不上车，可能一生都没有这样的机会。这样的叙事最容易放大人性贪婪，也最容易让人忽略价格、估值、资金流和风险。</p>
<p>每一轮泡沫都有类似句式：“这次不一样。”互联网泡沫时如此，新能源泡沫时如此，AI 叙事也会如此。不同的是行业、资产和故事，相同的是人性：上涨带来信仰，信仰带来杠杆，杠杆带来脆弱，脆弱最终被波动击穿。</p>
<h2 id="a-share-comparison">与 A 股疯牛的相似处</h2>
<p>韩国 2026 年行情与 A 股 2015 年行情有很多相似处。A 股当年涨幅约 1.6 倍，韩国这轮涨幅达到约 2.75 倍；A 股当年是改革牛、资金牛，韩国是 AI 超级周期、韩国折价修复和政策推动；A 股当年有“4000 点是牛市起点”的叙事，韩国则出现“5000 点”和国民分红等政策口号。</p>
<p>杠杆工具也相似。A 股当年有场外配资和两融，韩国则有信用贷款、融资买入和单一股票杠杆 ETF。散户特征也相似：全民炒股、排队开户、财富效应扩散。不同的是，韩国的账户渗透率和未成年人参与程度更加极端。</p>
<p>结局层面，A 股 2015 年牛市结束后快速暴跌，随后进入漫长熊市，并需要国家队大规模救市。韩国市场也进入救市进行时，相关部门联合出手，处理保证金追缴和散户风险问题。历史并不会简单重复，但韵脚总是相似：资金、杠杆、情绪和政策叙事共同堆出的高塔，最终都要接受均值回归。</p>
<h2 id="ten-lessons">十条风险启示</h2>
<p>第一，当政府为股市设置点位时，需要格外警惕。一旦股市点位被当作政绩或政策目标，短期上涨可能会被过度鼓励，市场已有风险也容易被忽视。</p>
<p>第二，不要只听机构说什么，要看资金做什么。机构一边唱多一边卖出并不少见。真正重要的是资金流、持仓变化、估值和常识。</p>
<p>第三，指数集中度是巨大风险。少数公司权重过高，会让指数上涨阶段更漂亮，也会让下跌阶段更脆弱。牛市后期不断出现万亿市值、超越龙头、十万亿叙事时，要警惕集中度风险。</p>
<p>第四，不要加杠杆。杠杆会把普通回调变成生存危机。对刚进入市场的新散户来说，高位浮盈加仓再叠加杠杆，往往是最危险的组合。</p>
<p>第五，“这次不一样”通常只是泡沫语言。AI 需求不会消失，优秀公司也不会突然变差，但好公司和好行业不等于任何价格都合理。泡沫破裂往往不是因为坏消息出现，而是价格已经透支了所有好消息。</p>
<p>第六，FOMO 是散户最大的敌人。害怕错过机会，往往会让人买在最不该买的位置。市场每年都有机会，隔几年就会有一次很好的机会，真正稀缺的不是机会，而是等待机会的耐心。</p>
<p>第七，不要只盯着 K 线和价格，要看资金流、估值、仓位结构、杠杆水平和参与者构成。价格本身会制造情绪，但风险往往藏在价格背后的资金结构里。</p>
<p>第八，当最脆弱的钱也进入股市时，市场就很危险。养老钱、保险钱、家庭安全垫、借贷资金集中涌入，说明上涨已经从投资行为变成全民赌博。</p>
<p>第九，泡沫破裂不是因为逻辑消失，而是价格透支。AI 需求仍会存在，存储产业也仍有价值，但当市场把未来多年最好情形一次性打进价格，后面就只剩下均值回归。</p>
<p>第十，复盘历史是为了避免成为历史的一部分。看到别人犯错很容易，承认自己也可能犯同样错误很难。投资中最危险的，不是恐惧弥漫的时候，而是快速上涨、人人兴奋、所有人都觉得自己正确的时候。</p>
<h2 id="final-framework">真正要守住的是理性和常识</h2>
<p>韩国股市这一轮疯牛，并不是华尔街单方面主导的收割，也不是单纯的政策错误，更不是 AI 逻辑本身虚假。它是资本市场多种力量共同作用的结果：真实产业逻辑提供火种，政策叙事提供氧气，投行唱多提供信心，外资减仓提供对手盘，散户 FOMO 和杠杆最终把行情推向失控。</p>
<p>投资者真正要学到的，不是永远不买热门行业，也不是永远不碰 AI 资产，而是在好故事面前仍然保持常识。好行业也会有坏价格，好公司也会有估值透支，好政策也可能制造短期泡沫。最重要的不是预测顶部是哪一天，而是在明显过热、杠杆泛滥、全民入场、机构减仓、指数集中度畸高时，知道自己不该再做接盘者。</p>
<p>老投资者看到快速上涨会胆战心惊，新投资者看到快速上涨只看到赚钱效应。这种差异来自经验，也来自对人性的认识。资本的镰刀并不需要神秘阴谋，它只需要利用贪婪、恐惧和不愿错过的心理。真正能在市场里活下来的，是愿意尊重估值、尊重风险、承认错误、敢于反思的人。</p>
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
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#111827"/><stop offset="0.55" stop-color="#7f1d1d"/><stop offset="1" stop-color="#f97316"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.35"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.15" stroke="#fff" stroke-width="3"><path d="M120 700 H1480"/><path d="M120 575 H1480"/><path d="M120 450 H1480"/><path d="M120 325 H1480"/><path d="M300 245 V760"/><path d="M600 245 V760"/><path d="M900 245 V760"/><path d="M1200 245 V760"/></g>
  <g filter="url(#shadow)">
    <path d="M140 660 C305 560 445 650 590 480 C750 292 900 420 1050 245 C1190 80 1340 160 1490 94" fill="none" stroke="#fde68a" stroke-width="17" stroke-linecap="round"/>
    <path d="M1380 118 L1490 94 L1448 200" fill="none" stroke="#fff7ed" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    <rect x="110" y="555" width="500" height="128" rx="24" fill="#fff7ed" opacity="0.95"/>
    <text x="152" y="634" fill="#991b1b" font-family="Noto Sans SC, PingFang SC, Arial" font-size="43" font-weight="800">FOMO 与杠杆</text>
  </g>
  <text x="96" y="154" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="60" font-weight="800">{esc(TITLE)}</text>
  <text x="100" y="238" fill="#ffedd5" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">AI 存储 · 政策叙事 · 全民狂热</text>
  <text x="102" y="314" fill="#fee2e2" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="600">真正主导泡沫的，从来不是故事，而是人性</text>
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
    inserted = 0
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
    for must in [TITLE, "韩国股市", "AI", "三星", "SK海力士", "148 万亿", "FOMO", "杠杆", "泡沫"]:
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
    rec(ROOT / "tasks/publish-korea-stock-market-bubble-article.py")
    changed_path = ROOT / "tasks/publish-korea-stock-market-bubble-changed-files.json"
    all_changed = sorted(CHANGED | {"tasks/publish-korea-stock-market-bubble-article.py", "tasks/publish-korea-stock-market-bubble-changed-files.json"})
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
