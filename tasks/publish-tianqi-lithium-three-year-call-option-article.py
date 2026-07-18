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
SLUG = "tianqi-lithium-35b-profit-gap-three-year-call-option"
URL_PATH = f"/2026/{SLUG}/"
FULL_URL = SITE + URL_PATH
TITLE = "天齐锂业的三年看涨期权：35 亿中报、97 亿缺口与机构翻倍目标价"
DESC = "天齐锂业上半年利润中值约 35 亿元，明显低于最乐观模型；机构仍给出接近翻倍目标价，关键在于下半年能否追回 97 亿元利润缺口，以及锂价高位窗口能否延续。"
DATE = "2026-07-18"
PUB_DT = datetime(2026, 7, 18, 22, 10, tzinfo=timezone(timedelta(hours=8)))
CATEGORY = "投资研究"
SERIES = "新能源周期"
TAGS = ["天齐锂业", "锂", "碳酸锂", "SC6", "格林布什", "周期股", "市盈率", "目标价", "业绩快报", "成本剪刀差", "新能源", "投资策略"]
MINUTES = 9
COVER = f"/images/posts/{SLUG}/cover.svg"
PREV_URL = "/2026/china-us-competition-institutional-synthesis/"
PREV_TITLE = "中美长期竞争的底层逻辑：中国为何可能走出新的制度合成"
CHANGED: set[str] = set()

ARTICLE = """
<h2 id="core-contradiction">35 亿中报与翻倍目标价，同时摆在台面上</h2>
<p>天齐锂业的矛盾点非常尖锐：上半年业绩快报显示，归母净利润预计落在 28.5 亿至 42.5 亿元之间，中值大约 35 亿元；而最乐观的机构目标价仍给到 93.18 元，相比 47.35 元的参考股价，隐含上涨空间接近一倍。</p>
<p>表面上看，这是“业绩低于预期但估值仍很便宜”的故事。但真正要紧的并不是目标价本身，而是目标价背后的利润假设。市场一致预期给出的 2026 年每股收益大约是 3.66 元，而乐观模型给到 7.77 元，两者几乎相差一倍。所谓 6 倍市盈率的便宜，只有在相信后者时才成立。</p>
<p>更直接的问题是全年利润缺口。乐观模型对天齐锂业 2026 年归母净利润的预测是 132 亿元，上半年中值只有 35 亿元。也就是说，下半年需要贡献接近 97 亿元净利润，差不多是上半年的三倍。这个缺口不能用一句“锂价回升”轻轻带过，必须拆到季度、成本和价格传导里重新计算。</p>
<h2 id="quarterly-pressure">二季度没有加速，反而暴露了环比压力</h2>
<p>周期股业绩修复的正常路径，通常应该是一季比一季好。价格从底部回升，库存消化完成，产品涨价逐步进入报表，利润弹性会连续释放。天齐锂业这次的问题在于，上半年数据拆开后并没有呈现这种顺畅修复。</p>
<p>根据机构推算，天齐锂业二季度隐含归母净利润中值约 16.7 亿元，而一季度约 18.3 亿元，环比下降约 11%。这意味着二季度并不是利润拐点向上的确认，反而是利润在成本压力下继续往下走。</p>
<p>如果三季度能够明显修复，这个 11% 的下滑还可以解释为价格传导的时间差；如果三季度继续环比走弱，那么下半年补足 97 亿元利润就会变得非常困难。问题的核心不在收入端有没有增长，而在成本端上涨速度是否超过产品端涨价。</p>
<h2 id="greenbushes-cost">格林布什自给，并不等于零成本</h2>
<p>天齐锂业最强的资源禀赋，是对格林布什锂矿的控制和供应保障。它是少数真正拥有上游优质锂矿资源、并能把矿端和锂化工加工端打通的公司。很多投资者容易因此形成一个直觉：既然原料来自自家矿山，矿价上涨就应该是利好，成本压力不应太明显。</p>
<p>这个直觉并不完整。自有矿不等于零成本，也不等于加工端可以无视市场价格。矿石开采出来后，在会计和内部结算上仍需要参考市场价格。SC6 锂精矿价格上涨时，天齐锂业自己的原料结算成本也会同步抬升。</p>
<p>这就像一家面包店背后还有自家的面粉厂。面粉市场价上涨 22%，面粉厂卖给面包店的内部价格也要按市场价确认；如果面包零售价只上涨 14%，中间 8 个百分点就会直接吞掉面包店的毛利。资源自给解决的是供应安全和长期资源壁垒，不代表短期利润表不会被成本剪刀差冲击。</p>
<h2 id="sc6-spread">SC6 涨 22%，锂化工产品只涨 14%：剪刀差吃掉毛利</h2>
<p>二季度最关键的数字，是 SC6 锂精矿价格环比上涨约 22%，而天齐锂业锂化工产品价格环比仅上涨约 14%。矿价跑赢产品价格约 8 个百分点，这就是利润环比下滑的直接解释。</p>
<p>锂化工产品往往存在长约、调价窗口和客户谈判周期。矿价上涨时，成本会先进入报表；产品端要等调价窗口打开，才能把成本压力向下游传导。短期内，矿端涨价越快，加工端毛利率越容易被挤压。</p>
<p>因此，下半年能不能完成利润追赶，关键不在于“锂价是不是上涨”这么简单，而在于产品价格能否追上矿价。如果锂化工产品涨价成功，全年 132 亿元利润仍有讨论空间；如果产品端追不上，全年净利润很可能连 100 亿元都站不稳。</p>
<h2 id="valuation-denominator">6 倍市盈率的关键，是分母到底用谁的 EPS</h2>
<p>机构给出的 2026 年市盈率约 6.1 倍、2027 年约 5.9 倍，看上去像周期底部的低估值机会。但估值倍数必须先看分母：这个 6.1 倍，是用 7.77 元的 2026 年每股收益预测除出来的。</p>
<p>如果用市场一致预期的 3.66 元每股收益，47.35 元股价对应的市盈率接近 13 倍。13 倍当然不是绝对昂贵，但它与 6 倍“白菜价”完全不是同一个投资故事。前者意味着市场还在等待业绩确认，后者意味着市场严重低估了即将释放的利润。</p>
<p>所以，天齐锂业当前估值争议并不是简单的“便宜还是不便宜”，而是“用哪套利润假设定价”。只要下半年 97 亿元利润缺口没有被季度报表验证，6 倍估值就更像乐观情景下的结果，而不是已经落地的事实。</p>
<h2 id="three-year-window">高利润窗口只被假设到 2028 年</h2>
<p>更值得警惕的是，乐观模型本身并没有把高利润状态外推得很远。它给出的净利润路径大致是：2026 年 132 亿元、2027 年 137 亿元、2028 年 124 亿元，然后到 2029 年骤降到 39.77 亿元。</p>
<p>收入端也类似。2028 年营收仍有约 411 亿元，2029 年直接降到约 192 亿元；EBIT 利润率则从 2028 年约 69% 回落到 2029 年约 43%。这不是温和回调，而是从高位锂价周期快速退潮。</p>
<p>这组预测意味着，93.18 元目标价并不是一张永久有效的价值支票，而更像一张三年期限的看涨期权。2026 至 2028 年，如果锂价维持高位、利润每年稳定在 120 亿至 130 亿元以上，股价向目标价靠拢有逻辑基础；但如果 2029 年回落预期被市场提前消化，这张期权会在到期前开始贬值。</p>
<h2 id="five-signals">五个信号，决定这张期权还值不值得拿</h2>
<p>天齐锂业不能用“买入后等翻倍”的静态方式处理。它更适合被当作一张周期期权，持续跟踪五个变量。</p>
<p>第一，看 SC6 锂精矿月度价格走势。只要矿价继续大幅跑赢锂化工产品，毛利率就会继续被压缩，下半年利润修复难度会越来越大。</p>
<p>第二，看电池级碳酸锂月度成交价。下半年价格能否稳定在 7 万元/吨以上，直接决定 132 亿元全年利润是不是空中楼阁；如果碳酸锂跌破 6.5 万元/吨，全年净利润连 100 亿元都可能守不住。</p>
<p>第三，看三季报、四季报中的产销量与库存周转。二季度 11% 的环比缺口，到底只是价格传导时间差，还是需求和利润结构变差，三季度数据会给出更直接答案。</p>
<p>第四，看电动车与储能电池排产。如果月度排产连续两个月下行，电动车电池需求走弱这条下行风险就会兑现，锂价高位假设也要重新评估。</p>
<p>第五，看锂行业并购活跃度。行业并购升温，往往是周期底部或拐点附近的先行信号。若天齐、赣锋等龙头开始趁低价买矿、买产能，说明产业内部正在用真金白银投票；如果并购突然转冷，说明连龙头也看不清短期方向。</p>
<h2 id="strategy">买入策略：分阶段验证，而不是一次性押注</h2>
<p>天齐锂业的策略重点，不是立刻判断目标价一定对或一定错，而是把仓位建立在验证过程上。当前股价已经部分消化了上半年业绩低于预期的事实，但下半年价格走势、产销量和利润弹性还没有完全被定价。</p>
<p>更稳健的做法，是把它分成三种状态处理。第一种是观察仓：当投资者认可锂价中枢回升、碳酸锂能稳定在 7 万元/吨附近、并且愿意承受周期股波动时，可以用小仓位跟踪这张期权的变化。</p>
<p>第二种是加仓确认：只有当锂化工产品价格开始追上 SC6 成本、三季度利润环比修复、产销量改善且库存周转健康时，乐观模型才从纸面预测变成报表验证。这个阶段加仓，胜率比单纯看目标价更高。</p>
<p>第三种是减仓或回避：若 SC6 继续跑赢产品端、碳酸锂跌破 6.5 万元/吨、三季度利润继续环比下滑，或者下游排产连续走弱，就要承认 132 亿元全年利润假设正在失效。此时再用 6 倍市盈率解释估值，已经是在使用错误分母。</p>
<h2 id="conclusion">真正的结论：跟踪比下结论更重要</h2>
<p>天齐锂业最大的吸引力，是格林布什这样的优质资源、锂价上行周期中的利润弹性，以及机构给出的高目标价空间。它最大的风险，则是上半年利润已经低于最乐观模型，下半年还需要补近 97 亿元净利润，而成本端剪刀差仍在挤压毛利率。</p>
<p>因此，这不是一个简单的低估值买入故事，而是一个带期限、带条件、带强验证要求的周期期权。目标价能否成立，取决于 2026 至 2028 年高位锂价窗口能否兑现；而市场是否愿意提前给估值，取决于三季度开始的数据能否证明利润正在追回来。</p>
<p>投资上最重要的不是迷信 93.18 元，也不是因为上半年只有 35 亿元利润就彻底否定公司，而是把五个变量持续放在桌面上：矿价、碳酸锂价格、产销量、下游排产、行业并购。任意两个关键变量同时转向，就应重新计算这张期权的价值。</p>
<p>本文仅基于公开信息进行分析，不构成任何投资建议。周期股的收益来自波动，风险也来自波动；仓位、节奏和验证纪律，比单一目标价更重要。</p>
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
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#111827"/><stop offset="0.5" stop-color="#365314"/><stop offset="1" stop-color="#0f766e"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.32"/></filter></defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.16" stroke="#ecfccb" stroke-width="3"><path d="M140 690 H1460"/><path d="M140 560 H1460"/><path d="M140 430 H1460"/><path d="M140 300 H1460"/><path d="M300 235 V760"/><path d="M590 235 V760"/><path d="M880 235 V760"/><path d="M1170 235 V760"/></g>
  <g filter="url(#shadow)">
    <path d="M220 645 C390 510 505 585 660 435 C820 280 940 345 1080 245 C1188 168 1290 150 1390 118" fill="none" stroke="#facc15" stroke-width="18" stroke-linecap="round"/>
    <path d="M220 610 C380 515 510 640 670 555 C820 475 930 580 1090 500 C1210 440 1310 455 1405 420" fill="none" stroke="#38bdf8" stroke-width="14" stroke-linecap="round" opacity="0.9"/>
    <rect x="118" y="610" width="700" height="118" rx="24" fill="#f7fee7" opacity="0.96"/>
    <text x="162" y="682" fill="#365314" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800">35 亿利润 × 97 亿缺口</text>
  </g>
  <text x="96" y="150" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="58" font-weight="800">{esc(TITLE)}</text>
  <text x="100" y="236" fill="#ecfccb" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">SC6 成本剪刀差 · EPS 分母 · 三年窗口</text>
  <text x="102" y="312" fill="#ccfbf1" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="600">跟踪矿价、碳酸锂、产销量、排产与并购五个变量</text>
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
    for must in [TITLE, "天齐锂业", "35 亿元", "97 亿元", "SC6", "格林布什", "碳酸锂", "6.1 倍", "三年期限", "五个变量"]:
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
    rec(ROOT / "tasks/publish-tianqi-lithium-three-year-call-option-article.py")
    changed_path = ROOT / "tasks/publish-tianqi-lithium-three-year-call-option-changed-files.json"
    all_changed = sorted(CHANGED | {"tasks/publish-tianqi-lithium-three-year-call-option-article.py", "tasks/publish-tianqi-lithium-three-year-call-option-changed-files.json"})
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
