from __future__ import annotations

import base64
import html
import json
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote


sys.dont_write_bytecode = True

OWNER = "zcxGGmu"
REPO = "zcxGGmu.github.io"
BRANCH = "gh-pages"
SITE = "https://zcxggmu.github.io"
DATE = "2026-08-08"
BASE_DT = datetime(2026, 8, 8, 19, 20, 0, tzinfo=timezone(timedelta(hours=8)))

SLUG = "codegraph-code-map-coding-agent-token-efficient-codebase-understanding"
URL_PATH = f"/2026/{SLUG}/"
FULL_URL = SITE + URL_PATH
TITLE = "CodeGraph：给 Coding Agent 一张代码地图，少翻文件、少烧 Token、改得更准"
DESC = "从 Tree-sitter、SQLite/FTS5、本地知识图谱到 MCP 工具，理解 CodeGraph 如何让 Coding Agent 先查结构，再读源码。"
CATEGORY = "AI工具"
SERIES = "AI Agent"
TAGS = ["CodeGraph", "Coding Agent", "MCP", "Tree-sitter", "SQLite", "FTS5", "Claude Code", "Codex", "Cursor", "代码图谱", "Token", "软件工程"]
MINUTES = 10
SOURCE_ID = "BV1n7716gEpq"
PREV_EXISTING_URL = "/2026/gold-price-monetary-logic-a-share-repair-opportunities/"
PREV_EXISTING_TITLE = "金价暴涨背后的货币逻辑：央行买金、去美元化与 A 股修复机会"

PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
]

TASKS = Path(__file__).resolve().parent
BODY_FILE = TASKS / f"{SLUG}-body.html"
SCRIPT_NAME = Path(__file__).name
MANIFEST_NAME = "publish-codegraph-code-map-coding-agent-article-20260808-changed-files.json"

FORBIDDEN = [
    "B站",
    "bilibili",
    "哔哩",
    "视频里",
    "视频中",
    "原视频",
    "音频里",
    "音频中",
    "UP主",
    "up主",
    "这期",
    "本期",
    "作者说",
    "他提到",
    "观看",
    "点赞",
    "订阅",
    "投币",
    "收藏",
    "下期",
    "关注",
    "欢迎收看",
    "感谢大家",
    "三连",
    "BV1",
]


@dataclass
class RemoteRef:
    commit_sha: str
    tree_sha: str


def run_gh(args: list[str], payload: dict | None = None) -> dict | list | str:
    proc = None
    for attempt in range(3):
        proc = subprocess.run(
            ["gh", "api", *args],
            input=json.dumps(payload, ensure_ascii=False) if payload is not None else None,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode == 0:
            break
        message = (proc.stderr + proc.stdout).lower()
        if attempt < 2 and any(token in message for token in ["timeout", "timed out", "connection", "reset", "temporarily"]):
            time.sleep(2 + attempt * 3)
            continue
        break
    assert proc is not None
    if proc.returncode != 0:
        raise RuntimeError(f"gh api failed: {' '.join(args)}\n{proc.stderr or proc.stdout}")
    out = proc.stdout.strip()
    if not out:
        return ""
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return out


def endpoint(path: str) -> str:
    return f"repos/{OWNER}/{REPO}/{path}"


def get_ref() -> RemoteRef:
    ref = run_gh([endpoint(f"git/ref/heads/{BRANCH}")])
    commit_sha = ref["object"]["sha"]
    commit = run_gh([endpoint(f"git/commits/{commit_sha}")])
    return RemoteRef(commit_sha=commit_sha, tree_sha=commit["tree"]["sha"])


def get_file(path: str) -> str | None:
    api_path = quote(path, safe="/")
    proc = None
    for attempt in range(3):
        proc = subprocess.run(
            ["gh", "api", endpoint(f"contents/{api_path}?ref={BRANCH}")],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode == 0:
            break
        message = (proc.stderr + proc.stdout).lower()
        if "not found" in message:
            break
        if attempt < 2 and any(token in message for token in ["timeout", "timed out", "connection", "reset", "temporarily"]):
            time.sleep(2 + attempt * 3)
            continue
        break
    assert proc is not None
    if proc.returncode != 0:
        if "Not Found" in proc.stderr or "Not Found" in proc.stdout:
            return None
        raise RuntimeError(f"fetch failed for {path}: {proc.stderr or proc.stdout}")
    data = json.loads(proc.stdout)
    return base64.b64decode(data["content"]).decode("utf-8")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def plain_text(html_text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(html_text))


def load_body() -> str:
    return BODY_FILE.read_text(encoding="utf-8").replace(f"/images/posts/{SLUG}/cover.png", f"/images/posts/{SLUG}/cover.svg")


def meta_links() -> str:
    cat = f'<a href="/categories/{quote(CATEGORY)}/">{esc(CATEGORY)}</a>'
    tags = "&nbsp;".join(f'<a href="/tags/{quote(tag)}/">{esc(tag)}</a>' for tag in TAGS)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {MINUTES} min'


def build_toc(body: str) -> str:
    links = [
        f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>'
        for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    ]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + "".join(links) + "</nav></div></div>"


def cover_svg() -> str:
    c1, c2, c3 = "#020617", "#0f766e", "#38bdf8"
    lines = TITLE.replace("：", "：\n", 1).split("\n")[:2]
    title_svg = "".join(
        f'<text x="90" y="{145 + i * 70}" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="{52 if i == 0 else 43}" font-weight="800">{esc(line)}</text>'
        for i, line in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">{esc(TITLE)}</title>
  <desc id="desc">{esc(DESC)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="0.56" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.30"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.20" stroke="#e0f2fe" stroke-width="3" fill="none">
    <path d="M270 585 C430 470 520 470 680 350 C835 233 985 330 1135 210 C1250 120 1390 125 1495 86"/>
    <path d="M180 650 H1420"/><path d="M180 520 H1420"/><path d="M180 390 H1420"/>
    <path d="M430 255 V742"/><path d="M760 255 V742"/><path d="M1090 255 V742"/>
  </g>
  <g filter="url(#shadow)">
    <rect x="96" y="575" width="455" height="134" rx="24" fill="#f8fafc" opacity="0.94"/>
    <text x="136" y="650" fill="#0f172a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="39" font-weight="800">Tree-sitter · SQLite</text>
    <text x="136" y="693" fill="#0f766e" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="700">本地知识图谱 + FTS5</text>
    <rect x="1010" y="568" width="440" height="142" rx="24" fill="#082f49" opacity="0.82"/>
    <text x="1050" y="645" fill="#e0f2fe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="39" font-weight="800">MCP Tools</text>
    <text x="1050" y="689" fill="#bae6fd" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="700">search · trace · impact</text>
    <circle cx="680" cy="350" r="34" fill="#f8fafc" opacity="0.95"/><circle cx="1135" cy="210" r="44" fill="#bae6fd" opacity="0.98"/>
  </g>
  {title_svg}
  <text x="94" y="322" fill="#dbeafe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="31" font-weight="700">{esc(DESC[:54])}</text>
</svg>'''


def build_article_page(body: str, template: str) -> str:
    start = template.find('<article class="post">')
    end = template.find("</article>", start) + len("</article>")
    if start == -1 or end == -1:
        raise RuntimeError("article template not found")
    head, tail = template[:start], template[end:]
    replacements = {
        r"<title>.*?</title>": f"<title>{esc(TITLE)} - zcxGGmu's Blog</title>",
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(DESC)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(FULL_URL)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(TITLE)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(DESC)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(FULL_URL)}">',
    }
    for pattern, replacement in replacements.items():
        head = re.sub(pattern, replacement, head, count=1, flags=re.S)
    newer = '<a class="newer-posts">下一篇<br>没有更新的文章</a>'
    older = f'<a class="older-posts" href="{PREV_EXISTING_URL}">上一篇<br>{esc(PREV_EXISTING_TITLE)}</a>'
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('/images/posts/{SLUG}/cover.svg')"><div class="post-title">{esc(TITLE)}<div class="post-subtitle">{esc(DESC)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links()}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{body}</div></div><nav class="post-pagination">{newer}{older}</nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(body), tail, count=1, flags=re.S)
    return head + article + tail


def update_previous_article(text: str) -> str:
    return re.sub(
        r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>',
        f'<a class="newer-posts" href="{URL_PATH}">下一篇<br>{esc(TITLE)}</a>',
        text,
        count=1,
        flags=re.S,
    )


def home_card() -> str:
    return f'''<a href="{URL_PATH}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(TITLE)}</div>
            <div class="post-item-summary">{esc(DESC)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {MINUTES} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('/images/posts/{SLUG}/cover.svg')"></div></div>
        </div>
      </div>
    </a>'''


def update_home(text: str) -> str:
    text = re.sub(rf'<a href="{re.escape(URL_PATH)}" class="a-block">.*?</a>\s*', "", text, flags=re.S)
    pos = text.find(f'<a href="{PREV_EXISTING_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError("homepage insertion marker not found")
    return text[:pos] + home_card() + "\n" + text[pos:]


def update_rss(text: str) -> str:
    text = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{format_datetime(BASE_DT)}</lastBuildDate>", text, count=1)
    text = re.sub(rf"<item>\s*<title>{re.escape(esc(TITLE))}</title>.*?</item>\s*", "", text, flags=re.S)
    item = f'''<item>
<title>{esc(TITLE)}</title>
<link>{FULL_URL}</link>
<guid>{FULL_URL}</guid>
<pubDate>{format_datetime(BASE_DT)}</pubDate>
<description>{esc(DESC)}</description>
</item>
'''
    return text.replace("<item>", item + "<item>", 1)


def update_sitemap(text: str) -> str:
    loc = f"  <url><loc>{FULL_URL}</loc></url>\n"
    text = re.sub(rf"\s*<url><loc>{re.escape(FULL_URL)}</loc></url>", "", text)
    return text.replace("</urlset>", loc + "</urlset>")


def archive_item() -> str:
    return f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{URL_PATH}">{esc(TITLE)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(CATEGORY)}</span></span>
      </div> '''


def update_archive(text: str) -> str:
    already = URL_PATH in text
    text = re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(URL_PATH)}">.*?</div>\s*', "", text, flags=re.S)
    if not already:
        text = re.sub(
            r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>',
            lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + 1} 篇</span>',
            text,
            count=1,
        )
    pos = text.find(f'<a href="{PREV_EXISTING_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    if start == -1:
        raise RuntimeError("archive insertion marker not found")
    return text[:start] + archive_item() + text[start:]


def tax_item() -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''


def update_term_index(text: str, kind: str, term: str, delta: int) -> str:
    if delta == 0:
        return text
    hrefs = [f"/{kind}/{quote(term)}/", f"/{kind}/{term}/"]
    for href in hrefs:
        pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span[^>]*>\()(\d+)(\)</span></a>)')
        text, count = pattern.subn(lambda m: f"{m.group(1)}{int(m.group(2)) + delta}{m.group(3)}", text, count=1)
        if count:
            return text
    href = f"/{kind}/{quote(term)}/"
    if kind == "tags":
        item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">({delta})</span></a>\n'
    else:
        item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">({delta})</span></a>\n'
    pos = text.find("</div></div></div><script")
    if pos == -1:
        pos = text.find("</div></div></div>")
    if pos == -1:
        raise RuntimeError(f"term index insertion point not found for {kind}/{term}")
    return text[:pos] + item + text[pos:]


def new_term_page(kind: str, term: str) -> str:
    prefix = "分类" if kind == "categories" else "标签" if kind == "tags" else "系列"
    label = f"{prefix}: {term}"
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(term)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p>{tax_item()}</div></div></div><script src="/js/journal.js"></script></body></html>'''


def update_term_page(text: str | None, kind: str, term: str) -> tuple[str, int]:
    if text is None:
        return new_term_page(kind, term), 1
    already = URL_PATH in text
    text = re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(URL_PATH)}".*?</div>\s*', "", text, flags=re.S)
    if not already:
        text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + 1} 篇文章", text, count=1)
    marker = '<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">'
    first = text.find(marker)
    if first == -1:
        first = text.find("</div></div></div>")
    if first == -1:
        raise RuntimeError(f"term page insertion point not found: {kind}/{term}")
    return text[:first] + tax_item() + text[first:], 0 if already else 1


def collect_outputs() -> dict[str, str]:
    body = load_body()
    outputs: dict[str, str] = {}
    template = get_file(PREV_EXISTING_URL.strip("/") + "/index.html")
    if template is None:
        raise RuntimeError("article template missing")
    outputs[f"2026/{SLUG}/index.html"] = build_article_page(body, template)
    outputs[f"images/posts/{SLUG}/cover.svg"] = cover_svg()
    outputs[f"tasks/{SCRIPT_NAME}"] = Path(__file__).read_text(encoding="utf-8")
    outputs[f"tasks/{BODY_FILE.name}"] = body

    current_home = get_file("index.html")
    current_rss = get_file("index.xml")
    current_archive = get_file("archive/index.html")
    current_sitemap = get_file("sitemap.xml") or '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n'
    previous = get_file(PREV_EXISTING_URL.strip("/") + "/index.html")
    if None in (current_home, current_rss, current_archive, previous):
        raise RuntimeError("required remote files missing")
    outputs["index.html"] = update_home(current_home)
    outputs["index.xml"] = update_rss(current_rss)
    outputs["archive/index.html"] = update_archive(current_archive)
    outputs["sitemap.xml"] = update_sitemap(current_sitemap)
    outputs[PREV_EXISTING_URL.strip("/") + "/index.html"] = update_previous_article(previous)

    index_cache: dict[str, str] = {}
    for kind, term in [("categories", CATEGORY), ("series", SERIES), *[("tags", tag) for tag in TAGS]]:
        term_path = f"{kind}/{term}/index.html"
        term_page, inserted = update_term_page(get_file(term_path), kind, term)
        outputs[term_path] = term_page
        index_path = f"{kind}/index.html"
        index_text = index_cache.get(index_path) or outputs.get(index_path) or get_file(index_path)
        if index_text is None:
            raise RuntimeError(f"{index_path} missing")
        index_cache[index_path] = update_term_index(index_text, kind, term, inserted)
    outputs.update(index_cache)

    manifest_files = sorted(outputs.keys() | {f"tasks/{MANIFEST_NAME}"})
    outputs[f"tasks/{MANIFEST_NAME}"] = json.dumps(manifest_files, ensure_ascii=False, indent=2)
    return outputs


def validate(outputs: dict[str, str]) -> None:
    failures: list[str] = []
    article = outputs[f"2026/{SLUG}/index.html"]
    cover = outputs[f"images/posts/{SLUG}/cover.svg"]
    body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    body_html = body_match.group(1) if body_match else ""
    plain = plain_text(body_html)
    if len(plain) < 5000:
        failures.append(f"body too short: {len(plain)}")
    for word in FORBIDDEN:
        if word in article or word in cover:
            failures.append(f"forbidden/source wording present: {word}")
    for term in ["CodeGraph", "Tree-sitter", "SQLite", "FTS5", "MCP", "Claude Code", "Codex", "Cursor", "callers", "callees", "impact", "本地"]:
        if term not in article:
            failures.append(f"missing required topic: {term}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links or len(h2) < 10:
        failures.append(f"toc mismatch or too few h2: h2={len(h2)} links={len(links)}")
    ET.fromstring(cover)
    ET.fromstring(outputs["index.xml"])

    home_cards: list[str] = []
    for match in re.finditer(r'<a href="([^"]+)" class="a-block">', outputs["index.html"]):
        href = match.group(1)
        if href not in home_cards:
            home_cards.append(href)
    expected_prefix = PINNED_PREFIX + [URL_PATH, PREV_EXISTING_URL]
    if home_cards[: len(expected_prefix)] != expected_prefix:
        failures.append(f"homepage order mismatch: {home_cards[:len(expected_prefix)]}")
    if FULL_URL not in outputs["index.xml"]:
        failures.append("rss missing new article")
    if URL_PATH not in outputs["archive/index.html"]:
        failures.append("archive missing new article")
    if URL_PATH not in outputs[PREV_EXISTING_URL.strip("/") + "/index.html"]:
        failures.append("previous article newer link missing")
    for path in [f"categories/{CATEGORY}/index.html", f"series/{SERIES}/index.html", *[f"tags/{tag}/index.html" for tag in TAGS]]:
        if URL_PATH not in outputs[path]:
            failures.append(f"{path} missing new article")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str]) -> None:
    out_dir = Path("/tmp/codegraph-code-map-coding-agent-publish-output")
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(json.dumps({"local_output": str(out_dir), "files": len(outputs), "url": FULL_URL}, ensure_ascii=False, indent=2))


def create_commit(outputs: dict[str, str], ref: RemoteRef) -> str:
    tree_entries = []
    for path, content in sorted(outputs.items()):
        blob = run_gh(["-X", "POST", endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        tree_entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = run_gh(["-X", "POST", endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": tree_entries})
    commit = run_gh(
        ["-X", "POST", endpoint("git/commits"), "--input", "-"],
        {"message": "Publish CodeGraph code map article", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    run_gh(["-X", "PATCH", endpoint(f"git/refs/heads/{BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def main() -> None:
    ref = get_ref()
    outputs = collect_outputs()
    validate(outputs)
    write_outputs(outputs)
    commit_sha = create_commit(outputs, ref)
    print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "source_id": SOURCE_ID, "url": FULL_URL}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
