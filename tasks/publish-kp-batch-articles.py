from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path("/tmp/hermes-video-publish")
ARTICLE_ROOT = Path("/tmp/bili-batch-kp/articles")
SITE = "https://zcxggmu.github.io"
DATE = "2026-07-18"
BASE_DT = datetime(2026, 7, 18, 19, 30, tzinfo=timezone(timedelta(hours=8)))
PREV_EXISTING_URL = "/2026/tianqi-lithium-raw-material-price-mismatch-cycle-rebound/"
PREV_EXISTING_TITLE = "天齐锂业的周期错配：原料自给为何仍被利润挤压"
CHANGED: set[str] = set()


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    desc: str
    category: str
    series: str
    tags: list[str]
    minutes: int
    article_file: str
    cover_theme: tuple[str, str, str]
    cover_kicker: str
    cover_line: str
    source_id: str
    duration: str
    segments: int
    chars: int

    @property
    def url_path(self) -> str:
        return f"/2026/{self.slug}/"

    @property
    def full_url(self) -> str:
        return SITE + self.url_path

    @property
    def cover(self) -> str:
        return f"/images/posts/{self.slug}/cover.svg"


POSTS = [
    Post(
        slug="coal-sector-right-side-seasonal-rebound",
        title="煤炭板块的右侧机会：800 元底部、旺季反弹与高股息修复",
        desc="资金卖压接近尾声、港口煤价 800 元/吨阶段底确认、旺季需求回升和高股息估值支撑，共同构成煤炭板块右侧配置窗口。",
        category="投资研究",
        series="周期行业观察",
        tags=["煤炭", "煤价", "煤炭ETF", "高股息", "红利资产", "周期股", "能源", "供需格局", "旺季反弹"],
        minutes=9,
        article_file="coal-sector-right-side-seasonal-rebound.html",
        cover_theme=("#111827", "#854d0e", "#facc15"),
        cover_kicker="800 元阶段底",
        cover_line="资金面 · 基本面 · 估值",
        source_id="BV13mKP6EEEX",
        duration="694.266",
        segments=318,
        chars=3671,
    ),
    Post(
        slug="changxin-ipo-memory-equipment-capex-cycle",
        title="长鑫 IPO 的产业链重估：存储扩产、HBM 与国产设备周期",
        desc="长鑫超募 660 亿元不仅打开存储龙头市值天花板，更把国产设备、HBM 价值量和存储资本开支周期推向新一轮重估。",
        category="投资研究",
        series="半导体产业链",
        tags=["长鑫", "存储", "半导体设备", "HBM", "DRAM", "国产替代", "资本开支", "科创板", "先进封装"],
        minutes=10,
        article_file="changxin-ipo-memory-equipment-capex-cycle.html",
        cover_theme=("#0f172a", "#1d4ed8", "#38bdf8"),
        cover_kicker="存储扩产",
        cover_line="IPO · HBM · 国产设备",
        source_id="BV1Q1KP6SEow",
        duration="1262.133",
        segments=574,
        chars=6969,
    ),
    Post(
        slug="investment-thinking-compound-life",
        title="投资思维与复利人生：少做差价，多种果树",
        desc="投机赚的是差价，投资拥有的是资产。真正能穿越牛熊的，是低估买入好公司、长期持有，并让时间成为复利的朋友。",
        category="投资研究",
        series="长期主义",
        tags=["投资思维", "复利", "长期主义", "价值投资", "周期股", "成长股", "价值股", "投机", "资产配置"],
        minutes=9,
        article_file="investment-thinking-compound-life.html",
        cover_theme=("#14532d", "#166534", "#86efac"),
        cover_kicker="复利人生",
        cover_line="少做差价，多种果树",
        source_id="BV17kKM6MEFs",
        duration="873.884",
        segments=440,
        chars=4264,
    ),
]


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


def meta_links(post: Post) -> str:
    cat = f'<a href="{term_url("categories", post.category)}">{esc(post.category)}</a>'
    tags = "&nbsp;".join(f'<a href="{term_url("tags", tag)}">{esc(tag)}</a>' for tag in post.tags)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min'


def article_body(post: Post) -> str:
    return (ARTICLE_ROOT / post.article_file).read_text(encoding="utf-8")


def build_toc(body: str) -> str:
    links = [
        f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>'
        for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    ]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + "".join(links) + "</nav></div></div>"


def cover_svg(post: Post) -> str:
    c1, c2, c3 = post.cover_theme
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="0.56" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.32"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.14" stroke="#fff" stroke-width="3">
    <path d="M120 690 H1480"/><path d="M120 570 H1480"/><path d="M120 450 H1480"/><path d="M120 330 H1480"/>
    <path d="M300 240 V760"/><path d="M600 240 V760"/><path d="M900 240 V760"/><path d="M1200 240 V760"/>
  </g>
  <g filter="url(#shadow)">
    <path d="M180 650 C360 560 490 620 650 485 C820 340 990 455 1160 305 C1290 190 1400 205 1500 130" fill="none" stroke="#f8fafc" stroke-width="15" stroke-linecap="round" opacity="0.86"/>
    <circle cx="650" cy="485" r="42" fill="{c3}"/><circle cx="1160" cy="305" r="50" fill="#f8fafc" opacity="0.92"/>
    <rect x="112" y="560" width="470" height="122" rx="24" fill="#f8fafc" opacity="0.94"/>
    <text x="152" y="635" fill="{c2}" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800">{esc(post.cover_kicker)}</text>
  </g>
  <text x="96" y="154" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="61" font-weight="800">{esc(post.title)}</text>
  <text x="100" y="238" fill="#f8fafc" opacity="0.9" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="700">{esc(post.cover_line)}</text>
  <text x="102" y="314" fill="#e5e7eb" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="600">{esc(post.desc[:42])}</text>
</svg>'''


def pagination_for(index: int) -> tuple[str, str, str, str]:
    newer_url = ""
    newer_title = ""
    if index > 0:
        newer_url = POSTS[index - 1].url_path
        newer_title = POSTS[index - 1].title
    older_url = PREV_EXISTING_URL
    older_title = PREV_EXISTING_TITLE
    if index < len(POSTS) - 1:
        older_url = POSTS[index + 1].url_path
        older_title = POSTS[index + 1].title
    return newer_url, newer_title, older_url, older_title


def build_article_page(post: Post, index: int) -> None:
    template = (ROOT / PREV_EXISTING_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    start = template.find('<article class="post">')
    end = template.find("</article>", start) + len("</article>")
    head, tail = template[:start], template[end:]
    replacements = {
        r"<title>.*?</title>": f"<title>{esc(post.title)} - zcxGGmu's Blog</title>",
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(post.desc)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(post.full_url)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(post.title)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(post.desc)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(post.full_url)}">',
    }
    for pattern, repl in replacements.items():
        head = re.sub(pattern, repl, head, flags=re.S)
    body = article_body(post)
    newer_url, newer_title, older_url, older_title = pagination_for(index)
    newer = '<a class="newer-posts">下一篇<br>没有更新的文章</a>'
    if newer_url:
        newer = f'<a class="newer-posts" href="{newer_url}">下一篇<br>{esc(newer_title)}</a>'
    older = f'<a class="older-posts" href="{older_url}">上一篇<br>{esc(older_title)}</a>'
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{post.cover}')"><div class="post-title">{esc(post.title)}<div class="post-subtitle">{esc(post.desc)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links(post)}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{body}</div></div><nav class="post-pagination">{newer}{older}</nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(body), tail, flags=re.S)
    write(ROOT / "2026" / post.slug / "index.html", head + article + tail)


def update_existing_previous() -> None:
    path = ROOT / PREV_EXISTING_URL.strip("/") / "index.html"
    text = path.read_text(encoding="utf-8")
    target = POSTS[-1]
    text = re.sub(
        r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>',
        f'<a class="newer-posts" href="{target.url_path}">下一篇<br>{esc(target.title)}</a>',
        text,
        count=1,
        flags=re.S,
    )
    write(path, text)


def home_card(post: Post) -> str:
    return f'''<a href="{post.url_path}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(post.title)}</div>
            <div class="post-item-summary">{esc(post.desc)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{post.cover}')"></div></div>
        </div>
      </div>
    </a>'''


def update_home() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    for post in POSTS:
        text = re.sub(rf'<a href="{re.escape(post.url_path)}" class="a-block">.*?</a>\s*', "", text, flags=re.S)
    pos = text.find(f'<a href="{PREV_EXISTING_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError("homepage insertion marker not found")
    block = "\n".join(home_card(post) for post in POSTS) + "\n"
    write(path, text[:pos] + block + text[pos:])


def update_rss() -> None:
    path = ROOT / "index.xml"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{format_datetime(BASE_DT)}</lastBuildDate>", text)
    for post in POSTS:
        text = re.sub(rf"<item>\s*<title>{re.escape(esc(post.title))}</title>.*?</item>\s*", "", text, flags=re.S)
    items = []
    for offset, post in enumerate(POSTS):
        pub_dt = BASE_DT - timedelta(minutes=offset)
        items.append(f'''<item>
<title>{esc(post.title)}</title>
<link>{post.full_url}</link>
<guid>{post.full_url}</guid>
<pubDate>{format_datetime(pub_dt)}</pubDate>
<description>{esc(post.desc)}</description>
</item>
''')
    write(path, text.replace("<item>", "".join(items) + "<item>", 1))


def update_archive() -> None:
    path = ROOT / "archive/index.html"
    text = path.read_text(encoding="utf-8")
    new_count = sum(1 for post in POSTS if post.url_path not in text)
    if new_count:
        text = re.sub(
            r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>',
            lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + new_count} 篇</span>',
            text,
            count=1,
        )
    for post in POSTS:
        text = re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(post.url_path)}">.*?</div>\s*', "", text, flags=re.S)
    items = "".join(
        f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{post.url_path}">{esc(post.title)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(post.category)}</span></span>
      </div> '''
        for post in POSTS
    )
    pos = text.find(f'<a href="{PREV_EXISTING_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    write(path, text[:start] + items + text[start:])


def tax_item(post: Post) -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{post.url_path}" style="font-size:16px;text-decoration:none">{esc(post.title)}</a>
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
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">({delta})</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">({delta})</span></a>\n'
        pos = text.find("</div></div></div>")
        text = text[:pos] + item + text[pos:]
    write(path, text)


def update_term(kind: str, term: str, posts: list[Post], prefix: str, emoji: str) -> None:
    path = ROOT / kind / term / "index.html"
    inserted = 0
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for post in posts:
            text = re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(post.url_path)}".*?</div>\s*', "", text, flags=re.S)
        inserted = sum(1 for post in posts if post.url_path not in path.read_text(encoding="utf-8"))
        if inserted:
            text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + inserted} 篇文章", text, count=1)
        first = text.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
        if first == -1:
            first = text.find("</div></div></div>")
        text = text[:first] + "".join(tax_item(post) for post in posts) + text[first:]
    else:
        inserted = len(posts)
        label = f"{prefix}: {term}" if prefix else term
        h1 = f"{emoji} {term}" if emoji else label
        text = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 {len(posts)} 篇文章</p>{"".join(tax_item(post) for post in posts)}</div></div></div><script src="/js/journal.js"></script></body></html>'''
    write(path, text)
    update_term_index(kind, term, inserted)


def update_taxonomies() -> None:
    by_category: dict[str, list[Post]] = {}
    by_series: dict[str, list[Post]] = {}
    by_tag: dict[str, list[Post]] = {}
    for post in POSTS:
        by_category.setdefault(post.category, []).append(post)
        by_series.setdefault(post.series, []).append(post)
        for tag in post.tags:
            by_tag.setdefault(tag, []).append(post)
    for term, posts in by_category.items():
        update_term("categories", term, posts, "分类", "")
    for term, posts in by_series.items():
        update_term("series", term, posts, "", "📚")
    for term, posts in by_tag.items():
        update_term("tags", term, posts, "标签", "🏷️")


def validate() -> None:
    failures: list[str] = []
    forbidden = ["B站", "bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主", "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅", "欢迎回到", "下集见"]
    expected_home = [
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
    ] + [post.url_path for post in POSTS] + [PREV_EXISTING_URL]
    for post in POSTS:
        article_path = ROOT / post.url_path.strip("/") / "index.html"
        article = article_path.read_text(encoding="utf-8")
        for word in forbidden:
            if word in article:
                failures.append(f"{post.slug}: forbidden {word}")
        for must in [post.title, post.desc, post.tags[0], post.category]:
            if must not in article:
                failures.append(f"{post.slug}: missing {must}")
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != links:
            failures.append(f"{post.slug}: toc mismatch")
        if not (ROOT / "images/posts" / post.slug / "cover.svg").exists():
            failures.append(f"{post.slug}: missing cover")
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    order = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)[:9]
    if order != expected_home:
        failures.append(f"home order mismatch: {order}")
    ET.parse(ROOT / "index.xml")
    for post in POSTS:
        for path in [
            ROOT / "archive/index.html",
            ROOT / "categories" / post.category / "index.html",
            ROOT / "series" / post.series / "index.html",
            ROOT / "tags" / post.tags[0] / "index.html",
        ]:
            text = path.read_text(encoding="utf-8")
            if post.url_path not in text:
                failures.append(f"{path}: missing {post.url_path}")
    previous = (ROOT / PREV_EXISTING_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    if POSTS[-1].url_path not in previous:
        failures.append("previous existing article newer link missing")
    if failures:
        raise SystemExit("\n".join(failures))
    print("validation passed")


def main() -> None:
    for index, post in enumerate(POSTS):
        write(ROOT / "images/posts" / post.slug / "cover.svg", cover_svg(post))
        build_article_page(post, index)
    update_existing_previous()
    update_home()
    update_rss()
    update_archive()
    update_taxonomies()
    rec(ROOT / "tasks/publish-kp-batch-articles.py")
    validate()
    changed_path = ROOT / "tasks/publish-kp-batch-changed-files.json"
    all_changed = sorted(CHANGED | {"tasks/publish-kp-batch-articles.py"})
    write(changed_path, json.dumps(all_changed, ensure_ascii=False, indent=2))
    print(json.dumps({"urls": [post.full_url for post in POSTS], "changed": len(all_changed)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
