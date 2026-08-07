from __future__ import annotations

import base64
import html
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote


OWNER = "zcxGGmu"
REPO = "zcxGGmu.github.io"
BRANCH = "gh-pages"
SITE = "https://zcxggmu.github.io"

DATE = "2026-08-08"
BASE_DT = datetime(2026, 8, 8, 2, 35, 0, tzinfo=timezone(timedelta(hours=8)))
SLUG = "pi-agent-minimal-harness-custom-agent-engine"
URL_PATH = f"/2026/{SLUG}/"
FULL_URL = SITE + URL_PATH
TITLE = "Pi Agent 的真正价值：极简 Harness、深度定制与可嵌入的 Agent 引擎"
DESC = "从极简系统提示词、四个基础工具、Skill 与 Extension，到 Sub-agent、多模型和 SDK 嵌入，理解 Agent Harness 为什么决定模型之外的效率。"
CATEGORY = "AI工具"
SERIES = "AI Agent"
TAGS = ["Pi Agent", "Agent Harness", "Claude Code", "Codex", "Skill", "Extension", "Sub-agent", "SDK", "Vibe Coding", "AI工具", "自动化", "多模型"]
MINUTES = 8
SOURCE_ID = "BV1gaN96UEVQ"
PREV_EXISTING_URL = "/2026/copper-price-new-high-valuation-low-three-logic-repricing/"
PREV_EXISTING_TITLE = "铜价新高、估值新低：铜板块三重逻辑共振下的重估窗口"

TASKS = Path(__file__).resolve().parent
BODY_FILE = TASKS / f"{SLUG}-body.html"
DRAFT_ARTICLE = TASKS.parent / "blog-site" / "blog" / "2026" / SLUG / "index.html"
SCRIPT_NAME = Path(__file__).name
MANIFEST_NAME = "publish-pi-agent-minimal-harness-custom-agent-engine-20260808-changed-files.json"

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
    cmd = ["gh", "api", *args]
    proc = subprocess.run(
        cmd,
        input=json.dumps(payload, ensure_ascii=False) if payload is not None else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gh api failed: {' '.join(cmd)}\n{proc.stderr}")
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
    proc = subprocess.run(
        ["gh", "api", endpoint(f"contents/{api_path}?ref={BRANCH}")],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
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
    if BODY_FILE.exists():
        body = BODY_FILE.read_text(encoding="utf-8")
    else:
        draft = DRAFT_ARTICLE.read_text(encoding="utf-8")
        match = re.search(r'<div class="post-body" v-pre>(.*?)<hr id="EOF">', draft, re.S)
        if not match:
            raise RuntimeError(f"Cannot extract post body from {DRAFT_ARTICLE}")
        body = match.group(1)
    return body.replace(
        f"/images/posts/{SLUG}/cover.png",
        f"/images/posts/{SLUG}/cover.svg",
    )


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
    c1, c2, c3 = "#0b1220", "#334155", "#22c55e"
    title_lines = TITLE.replace("：", "：\n", 1).split("\n")
    title_svg = "".join(
        f'<text x="96" y="{150 + i * 70}" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="{54 if i == 0 else 46}" font-weight="800">{esc(line)}</text>'
        for i, line in enumerate(title_lines[:2])
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">{esc(TITLE)}</title>
  <desc id="desc">{esc(DESC)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="0.55" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.30"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#dcfce7" stroke-width="3">
    <path d="M180 640 H1420"/><path d="M180 520 H1420"/><path d="M180 400 H1420"/>
    <path d="M420 250 V740"/><path d="M760 250 V740"/><path d="M1100 250 V740"/>
  </g>
  <g filter="url(#shadow)">
    <rect x="105" y="560" width="430" height="130" rx="26" fill="#f8fafc" opacity="0.95"/>
    <text x="145" y="635" fill="#0f172a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800">4 个基础工具</text>
    <text x="145" y="674" fill="#166534" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="700">读 · 写 · 编辑 · 终端</text>
    <rect x="1020" y="555" width="430" height="130" rx="26" fill="#052e16" opacity="0.78"/>
    <text x="1060" y="632" fill="#dcfce7" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="800">Skill + Extension</text>
    <text x="1060" y="674" fill="#bbf7d0" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="700">方法与运行层同时可改</text>
    <path d="M250 475 C430 350 560 400 720 310 C880 220 1030 340 1220 210 C1335 135 1430 145 1510 98" fill="none" stroke="#f8fafc" stroke-width="13" stroke-linecap="round" opacity="0.86"/>
    <circle cx="720" cy="310" r="38" fill="#86efac"/><circle cx="1220" cy="210" r="46" fill="#f8fafc"/>
  </g>
  {title_svg}
  <text x="100" y="316" fill="#dcfce7" opacity="0.95" font-family="Noto Sans SC, PingFang SC, Arial" font-size="34" font-weight="700">极简 Harness · 深度定制 · 可嵌入 Agent 引擎</text>
  <text x="102" y="382" fill="#e2e8f0" font-family="Noto Sans SC, PingFang SC, Arial" font-size="27" font-weight="600">{esc(DESC[:48])}</text>
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


def new_term_page(kind: str, term: str, prefix: str, emoji: str) -> str:
    label = f"{prefix}: {term}" if prefix else term
    h1 = f"{emoji} {term}" if emoji else label
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p>{tax_item()}</div></div></div><script src="/js/journal.js"></script></body></html>'''


def update_term_page(text: str | None, kind: str, term: str) -> tuple[str, int]:
    if text is None:
        prefix = "分类" if kind == "categories" else "标签" if kind == "tags" else ""
        emoji = "🏷️" if kind == "tags" else "📚" if kind == "series" else ""
        return new_term_page(kind, term, prefix, emoji), 1
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
    body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    body_html = body_match.group(1) if body_match else ""
    plain = plain_text(body_html)
    if len(plain) < 4500:
        failures.append(f"body too short: {len(plain)}")
    for word in FORBIDDEN:
        if word in article or word in outputs[f"images/posts/{SLUG}/cover.svg"]:
            failures.append(f"forbidden/source wording present: {word}")
    required = ["Pi Agent", "Claude Code", "Codex", "Harness", "Token", "Skill", "Extension", "Sub-agent", "SDK", "DeepSeek", "权限", "安全", "四个基础工具", "可嵌入"]
    for term in required:
        if term not in article:
            failures.append(f"missing required topic: {term}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links or len(h2) < 10:
        failures.append(f"toc mismatch or too few h2: h2={len(h2)} links={len(links)}")
    ET.fromstring(outputs[f"images/posts/{SLUG}/cover.svg"])
    ET.fromstring(outputs["index.xml"])
    home_cards = []
    for match in re.finditer(r'<a href="([^"]+)" class="a-block">', outputs["index.html"]):
        href = match.group(1)
        if href not in home_cards:
            home_cards.append(href)
    expected_prefix = [
        "/ai-news-radar/",
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
        URL_PATH,
        PREV_EXISTING_URL,
    ]
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
    for path, term in [("categories/index.html", CATEGORY), ("series/index.html", SERIES), *[("tags/index.html", tag) for tag in TAGS]]:
        if term not in outputs[path]:
            failures.append(f"{path} missing {term}")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str]) -> None:
    out_dir = Path("/tmp/pi-agent-minimal-harness-custom-agent-engine-publish-output")
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
        {
            "message": "Publish Pi Agent harness article",
            "tree": tree["sha"],
            "parents": [ref.commit_sha],
        },
    )
    run_gh(["-X", "PATCH", endpoint(f"git/refs/heads/{BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def main() -> None:
    ref = get_ref()
    outputs = collect_outputs()
    validate(outputs)
    write_outputs(outputs)
    commit_sha = create_commit(outputs, ref)
    print(json.dumps({"pushed": commit_sha, "source_id": SOURCE_ID, "url": FULL_URL}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    main()
