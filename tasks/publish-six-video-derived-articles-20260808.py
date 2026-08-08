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
BASE_DT = datetime(2026, 8, 8, 18, 30, 0, tzinfo=timezone(timedelta(hours=8)))
PREV_EXISTING_URL = "/2026/pi-agent-minimal-harness-custom-agent-engine/"
PREV_EXISTING_TITLE = "Pi Agent 的真正价值：极简 Harness、深度定制与可嵌入的 Agent 引擎"
TASKS = Path(__file__).resolve().parent
SCRIPT_NAME = Path(__file__).name
MANIFEST_NAME = "publish-six-video-derived-articles-20260808-changed-files.json"

PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
]

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


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    desc: str
    category: str
    series: str
    tags: list[str]
    minutes: int
    body_file: str
    accent: tuple[str, str, str]
    required: list[str]

    @property
    def url_path(self) -> str:
        return f"/2026/{self.slug}/"

    @property
    def full_url(self) -> str:
        return SITE + self.url_path


POSTS = [
    Post(
        slug="gold-price-monetary-logic-a-share-repair-opportunities",
        title="金价暴涨背后的货币逻辑：央行买金、去美元化与 A 股修复机会",
        desc="从央行买金、美元信用、实际利率与降息周期，理解黄金长期重估，并梳理 A 股黄金股、科技修复和资源股机会。",
        category="投资",
        series="市场策略",
        tags=["黄金", "金价", "央行买金", "去美元化", "降息周期", "A股", "黄金股", "紫金矿业", "山东黄金", "资源股"],
        minutes=8,
        body_file="gold-price-monetary-logic-a-share-repair-opportunities-body.html",
        accent=("#111827", "#92400e", "#f59e0b"),
        required=["黄金", "央行", "去美元化", "降息", "A 股", "紫金矿业", "山东黄金"],
    ),
    Post(
        slug="emotional-freedom-abc-rational-emotive-therapy",
        title="情绪为何总被他人左右：ABC 理论、病态思维与情绪自由",
        desc="用理性情绪行为疗法拆解焦虑、愤怒、低落和内疚，识别恐怖化、应该化与合理化，重建情绪主动权。",
        category="心理成长",
        series="读书笔记",
        tags=["情绪管理", "理性情绪疗法", "ABC理论", "阿尔伯特·埃利斯", "内耗", "焦虑", "精神独立", "认知重建"],
        minutes=12,
        body_file="emotional-freedom-abc-rational-emotive-therapy-body.html",
        accent=("#172554", "#7c3aed", "#f97316"),
        required=["ABC", "理性情绪", "恐怖化", "应该", "合理化", "情绪自由"],
    ),
    Post(
        slug="openai-symphony-codex-task-orchestration-workflow",
        title="OpenAI Symphony：把 Codex 从聊天窗口推进任务流水线",
        desc="围绕任务系统、隔离工作区、依赖 DAG、PR、CI 与 review，理解 Coding Agent 如何从 session 走向工程流水线。",
        category="AI工具",
        series="AI Agent",
        tags=["OpenAI", "Codex", "Symphony", "Agent编排", "Coding Agent", "Linear", "CI", "PR", "Workflow", "软件工程"],
        minutes=12,
        body_file="openai-symphony-codex-task-orchestration-workflow-body.html",
        accent=("#020617", "#2563eb", "#22c55e"),
        required=["Symphony", "Codex", "Linear", "workspace", "DAG", "CI", "review"],
    ),
    Post(
        slug="human-agent-teams-context-roles-trust-workflow",
        title="Human-Agent Teams：人类与 Agent 共事的上下文、职责与信任机制",
        desc="团队型 Agent 的关键不是接入工具，而是公开上下文、明确 roster、北极星目标、渐进授权、审计和验证机制。",
        category="AI工具",
        series="AI Agent",
        tags=["Claude", "Anthropic", "Claude Tag", "Human-Agent Teams", "团队协作", "Agent协作", "上下文", "权限", "Doer-Verifier"],
        minutes=10,
        body_file="human-agent-teams-context-roles-trust-workflow-body.html",
        accent=("#18181b", "#0f766e", "#facc15"),
        required=["Agent", "roster", "北极星", "Doer-Verifier", "权限", "审计"],
    ),
    Post(
        slug="tax-ai-codex-self-improving-business-agent-loop",
        title="Tax AI：Codex 如何进入会自进化的业务闭环",
        desc="从报税准备、专家修正、结构化证据、评测体系到 Codex 工程修复，拆解业务智能体持续变好的闭环。",
        category="AI工具",
        series="AI Agent",
        tags=["OpenAI", "Codex", "Tax AI", "业务智能体", "自进化", "评测", "结构化证据", "会计", "自动化"],
        minutes=8,
        body_file="tax-ai-codex-self-improving-business-agent-loop-body.html",
        accent=("#0f172a", "#0369a1", "#84cc16"),
        required=["Tax AI", "Codex", "评测", "结构化证据", "自进化", "报税"],
    ),
    Post(
        slug="codexmaxxing-durable-threads-goals-automation-work-system",
        title="Codexmaxxing：把 Codex 用成长期工作系统",
        desc="通过 Durable Threads、文件记忆、语音输入、工具连接器、Skills、Automations 和 Goals，把 Codex 从助手升级为工作系统。",
        category="AI工具",
        series="AI Agent",
        tags=["Codex", "Codexmaxxing", "Durable Threads", "Goals", "Automation", "Voice Input", "MCP", "Skills", "工作流"],
        minutes=9,
        body_file="codexmaxxing-durable-threads-goals-automation-work-system-body.html",
        accent=("#111827", "#9333ea", "#06b6d4"),
        required=["Codexmaxxing", "Durable Threads", "Goals", "Automation", "Skills", "语音"],
    ),
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
        if attempt < 2 and any(token in (proc.stderr + proc.stdout).lower() for token in ["timeout", "timed out", "connection", "reset", "temporarily"]):
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


def load_body(post: Post) -> str:
    body = (TASKS / post.body_file).read_text(encoding="utf-8")
    return body.replace(f"/images/posts/{post.slug}/cover.png", f"/images/posts/{post.slug}/cover.svg")


def meta_links(post: Post) -> str:
    cat = f'<a href="/categories/{quote(post.category)}/">{esc(post.category)}</a>'
    tags = "&nbsp;".join(f'<a href="/tags/{quote(tag)}/">{esc(tag)}</a>' for tag in post.tags)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min'


def build_toc(body: str) -> str:
    links = [
        f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>'
        for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    ]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + "".join(links) + "</nav></div></div>"


def cover_svg(post: Post) -> str:
    c1, c2, c3 = post.accent
    title = post.title.replace("：", "：\n", 1)
    lines = title.split("\n")[:2]
    title_svg = "".join(
        f'<text x="92" y="{145 + i * 70}" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="{50 if i == 0 else 43}" font-weight="800">{esc(line)}</text>'
        for i, line in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">{esc(post.title)}</title>
  <desc id="desc">{esc(post.desc)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="0.55" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.26"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#ffffff" stroke-width="2">
    <path d="M120 655 H1480"/><path d="M120 535 H1480"/><path d="M120 415 H1480"/>
    <path d="M390 260 V750"/><path d="M760 260 V750"/><path d="M1130 260 V750"/>
  </g>
  <g filter="url(#shadow)">
    <path d="M170 650 C360 510 510 570 690 425 C870 280 1035 390 1220 245 C1320 168 1420 145 1500 108" fill="none" stroke="#f8fafc" stroke-width="13" stroke-linecap="round" opacity="0.86"/>
    <circle cx="690" cy="425" r="34" fill="#ffffff" opacity="0.92"/><circle cx="1220" cy="245" r="44" fill="#f8fafc" opacity="0.96"/>
    <rect x="94" y="585" width="470" height="132" rx="26" fill="#ffffff" opacity="0.92"/>
    <text x="132" y="660" fill="#0f172a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="800">{esc(post.category)} · {esc(post.series)}</text>
    <text x="132" y="700" fill="{c2}" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="700">{esc(str(post.minutes))} min 深度梳理</text>
  </g>
  {title_svg}
  <text x="96" y="322" fill="#e5e7eb" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="700">{esc(post.desc[:54])}</text>
</svg>'''


def article_nav(post: Post, index: int) -> str:
    if index == 0:
        newer = '<a class="newer-posts">下一篇<br>没有更新的文章</a>'
    else:
        newer_post = POSTS[index - 1]
        newer = f'<a class="newer-posts" href="{newer_post.url_path}">下一篇<br>{esc(newer_post.title)}</a>'
    if index + 1 < len(POSTS):
        older_post = POSTS[index + 1]
        older = f'<a class="older-posts" href="{older_post.url_path}">上一篇<br>{esc(older_post.title)}</a>'
    else:
        older = f'<a class="older-posts" href="{PREV_EXISTING_URL}">上一篇<br>{esc(PREV_EXISTING_TITLE)}</a>'
    return newer + older


def build_article_page(post: Post, body: str, template: str, index: int) -> str:
    start = template.find('<article class="post">')
    end = template.find("</article>", start) + len("</article>")
    if start == -1 or end == -1:
        raise RuntimeError("article template not found")
    head, tail = template[:start], template[end:]
    replacements = {
        r"<title>.*?</title>": f"<title>{esc(post.title)} - zcxGGmu's Blog</title>",
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(post.desc)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(post.full_url)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(post.title)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(post.desc)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(post.full_url)}">',
    }
    for pattern, replacement in replacements.items():
        head = re.sub(pattern, replacement, head, count=1, flags=re.S)
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('/images/posts/{post.slug}/cover.svg')"><div class="post-title">{esc(post.title)}<div class="post-subtitle">{esc(post.desc)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links(post)}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{body}</div></div><nav class="post-pagination">{article_nav(post, index)}</nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(body), tail, count=1, flags=re.S)
    return head + article + tail


def update_previous_article(text: str) -> str:
    last_post = POSTS[-1]
    return re.sub(
        r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>',
        f'<a class="newer-posts" href="{last_post.url_path}">下一篇<br>{esc(last_post.title)}</a>',
        text,
        count=1,
        flags=re.S,
    )


def home_card(post: Post) -> str:
    return f'''<a href="{post.url_path}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(post.title)}</div>
            <div class="post-item-summary">{esc(post.desc)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('/images/posts/{post.slug}/cover.svg')"></div></div>
        </div>
      </div>
    </a>'''


def strip_home_card(text: str, url_path: str) -> str:
    return re.sub(rf'<a href="{re.escape(url_path)}" class="a-block">.*?</a>\s*', "", text, flags=re.S)


def update_home(text: str) -> str:
    for post in POSTS:
        text = strip_home_card(text, post.url_path)
    pos = text.find(f'<a href="{PREV_EXISTING_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError("homepage insertion marker not found")
    block = "\n".join(home_card(post) for post in POSTS) + "\n"
    return text[:pos] + block + text[pos:]


def pub_date(index: int) -> datetime:
    return BASE_DT - timedelta(minutes=index)


def update_rss(text: str) -> str:
    text = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{format_datetime(BASE_DT)}</lastBuildDate>", text, count=1)
    for post in POSTS:
        text = re.sub(rf"<item>\s*<title>{re.escape(esc(post.title))}</title>.*?</item>\s*", "", text, flags=re.S)
    block = "".join(
        f'''<item>
<title>{esc(post.title)}</title>
<link>{post.full_url}</link>
<guid>{post.full_url}</guid>
<pubDate>{format_datetime(pub_date(i))}</pubDate>
<description>{esc(post.desc)}</description>
</item>
'''
        for i, post in enumerate(POSTS)
    )
    return text.replace("<item>", block + "<item>", 1)


def update_sitemap(text: str) -> str:
    for post in POSTS:
        text = re.sub(rf"\s*<url><loc>{re.escape(post.full_url)}</loc></url>", "", text)
    block = "".join(f"  <url><loc>{post.full_url}</loc></url>\n" for post in POSTS)
    return text.replace("</urlset>", block + "</urlset>")


def archive_item(post: Post) -> str:
    return f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{post.url_path}">{esc(post.title)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(post.category)}</span></span>
      </div> '''


def remove_archive_item(text: str, post: Post) -> str:
    return re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(post.url_path)}">.*?</div>\s*', "", text, flags=re.S)


def update_archive(text: str) -> str:
    original = text
    for post in POSTS:
        text = remove_archive_item(text, post)
    delta = sum(1 for post in POSTS if post.url_path not in original)
    if delta:
        text = re.sub(
            r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>',
            lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + delta} 篇</span>',
            text,
            count=1,
        )
    pos = text.find(f'<a href="{PREV_EXISTING_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    if start == -1:
        raise RuntimeError("archive insertion marker not found")
    block = "".join(archive_item(post) for post in POSTS)
    return text[:start] + block + text[start:]


def tax_item(post: Post) -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{post.url_path}" style="font-size:16px;text-decoration:none">{esc(post.title)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''


def remove_tax_item(text: str, post: Post) -> str:
    return re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(post.url_path)}".*?</div>\s*', "", text, flags=re.S)


def new_term_page(kind: str, term: str, posts: list[Post]) -> str:
    prefix = "分类" if kind == "categories" else "标签" if kind == "tags" else "系列"
    label = f"{prefix}: {term}"
    items = "".join(tax_item(post) for post in posts)
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(term)}</h1><p style="color:#999;margin-bottom:30px">共 {len(posts)} 篇文章</p>{items}</div></div></div><script src="/js/journal.js"></script></body></html>'''


def update_term_page(text: str | None, kind: str, term: str, posts: list[Post]) -> tuple[str, int]:
    if text is None:
        return new_term_page(kind, term, posts), len(posts)
    original = text
    for post in posts:
        text = remove_tax_item(text, post)
    delta = sum(1 for post in posts if post.url_path not in original)
    if delta:
        text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + delta} 篇文章", text, count=1)
    marker = '<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">'
    first = text.find(marker)
    if first == -1:
        first = text.find("</div></div></div>")
    if first == -1:
        raise RuntimeError(f"term page insertion point not found: {kind}/{term}")
    block = "".join(tax_item(post) for post in posts)
    return text[:first] + block + text[first:], delta


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


def collect_term_posts() -> dict[tuple[str, str], list[Post]]:
    mapping: dict[tuple[str, str], list[Post]] = {}
    for post in POSTS:
        for kind, term in [("categories", post.category), ("series", post.series), *[("tags", tag) for tag in post.tags]]:
            mapping.setdefault((kind, term), []).append(post)
    return mapping


def collect_outputs() -> dict[str, str]:
    outputs: dict[str, str] = {}
    template = get_file(PREV_EXISTING_URL.strip("/") + "/index.html")
    if template is None:
        raise RuntimeError("article template missing")

    for i, post in enumerate(POSTS):
        body = load_body(post)
        outputs[f"2026/{post.slug}/index.html"] = build_article_page(post, body, template, i)
        outputs[f"images/posts/{post.slug}/cover.svg"] = cover_svg(post)
        outputs[f"tasks/{post.body_file}"] = body

    outputs[f"tasks/{SCRIPT_NAME}"] = Path(__file__).read_text(encoding="utf-8")

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
    for (kind, term), posts in collect_term_posts().items():
        term_path = f"{kind}/{term}/index.html"
        term_source = outputs.get(term_path) or get_file(term_path)
        term_page, delta = update_term_page(term_source, kind, term, posts)
        outputs[term_path] = term_page
        index_path = f"{kind}/index.html"
        index_text = index_cache.get(index_path) or outputs.get(index_path) or get_file(index_path)
        if index_text is None:
            raise RuntimeError(f"{index_path} missing")
        index_cache[index_path] = update_term_index(index_text, kind, term, delta)
    outputs.update(index_cache)

    manifest_files = sorted(outputs.keys() | {f"tasks/{MANIFEST_NAME}"})
    outputs[f"tasks/{MANIFEST_NAME}"] = json.dumps(manifest_files, ensure_ascii=False, indent=2)
    return outputs


def validate(outputs: dict[str, str]) -> None:
    failures: list[str] = []
    minimums = {
        "gold-price-monetary-logic-a-share-repair-opportunities": 3000,
        "emotional-freedom-abc-rational-emotive-therapy": 3800,
        "openai-symphony-codex-task-orchestration-workflow": 3700,
        "human-agent-teams-context-roles-trust-workflow": 3500,
        "tax-ai-codex-self-improving-business-agent-loop": 3300,
        "codexmaxxing-durable-threads-goals-automation-work-system": 3600,
    }
    for post in POSTS:
        article = outputs[f"2026/{post.slug}/index.html"]
        cover = outputs[f"images/posts/{post.slug}/cover.svg"]
        body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
        body_html = body_match.group(1) if body_match else ""
        plain = plain_text(body_html)
        if len(plain) < minimums[post.slug]:
            failures.append(f"{post.slug}: body too short: {len(plain)}")
        for word in FORBIDDEN:
            if word in article or word in cover:
                failures.append(f"{post.slug}: forbidden/source wording present: {word}")
        for term in post.required:
            if term not in article:
                failures.append(f"{post.slug}: missing required topic: {term}")
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != links or len(h2) < 8:
            failures.append(f"{post.slug}: toc mismatch or too few h2: h2={len(h2)} links={len(links)}")
        ET.fromstring(cover)

    ET.fromstring(outputs["index.xml"])
    home_cards: list[str] = []
    for match in re.finditer(r'<a href="([^"]+)" class="a-block">', outputs["index.html"]):
        href = match.group(1)
        if href not in home_cards:
            home_cards.append(href)
    expected_prefix = PINNED_PREFIX + [post.url_path for post in POSTS] + [PREV_EXISTING_URL]
    if home_cards[: len(expected_prefix)] != expected_prefix:
        failures.append(f"homepage order mismatch: {home_cards[:len(expected_prefix)]}")
    rss_links = re.findall(r"<link>(https://zcxggmu.github.io/2026/[^<]+/)</link>", outputs["index.xml"])
    if rss_links[: len(POSTS)] != [post.full_url for post in POSTS]:
        failures.append(f"rss order mismatch: {rss_links[:len(POSTS)]}")
    for post in POSTS:
        if post.url_path not in outputs["archive/index.html"]:
            failures.append(f"archive missing {post.slug}")
        if post.full_url not in outputs["sitemap.xml"]:
            failures.append(f"sitemap missing {post.slug}")
        for kind, term in [("categories", post.category), ("series", post.series), *[("tags", tag) for tag in post.tags]]:
            term_path = f"{kind}/{term}/index.html"
            if post.url_path not in outputs[term_path]:
                failures.append(f"{term_path} missing {post.slug}")
            if term not in outputs[f"{kind}/index.html"]:
                failures.append(f"{kind}/index.html missing {term}")
    previous = outputs[PREV_EXISTING_URL.strip("/") + "/index.html"]
    if POSTS[-1].url_path not in previous:
        failures.append("previous article newer link missing")
    for i, post in enumerate(POSTS):
        article = outputs[f"2026/{post.slug}/index.html"]
        if i and POSTS[i - 1].url_path not in article:
            failures.append(f"{post.slug}: newer link missing")
        if i + 1 < len(POSTS) and POSTS[i + 1].url_path not in article:
            failures.append(f"{post.slug}: older link missing")
        if i + 1 == len(POSTS) and PREV_EXISTING_URL not in article:
            failures.append(f"{post.slug}: previous older link missing")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str]) -> None:
    out_dir = Path("/tmp/six-video-derived-articles-20260808-publish-output")
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(json.dumps({"local_output": str(out_dir), "files": len(outputs), "urls": [post.full_url for post in POSTS]}, ensure_ascii=False, indent=2))


def create_commit(outputs: dict[str, str], ref: RemoteRef) -> str:
    tree_entries = []
    for path, content in sorted(outputs.items()):
        blob = run_gh(["-X", "POST", endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        tree_entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = run_gh(["-X", "POST", endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": tree_entries})
    commit = run_gh(
        ["-X", "POST", endpoint("git/commits"), "--input", "-"],
        {"message": "Publish six video-derived blog articles", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    run_gh(["-X", "PATCH", endpoint(f"git/refs/heads/{BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def main() -> None:
    ref = get_ref()
    outputs = collect_outputs()
    validate(outputs)
    write_outputs(outputs)
    commit_sha = create_commit(outputs, ref)
    print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "urls": [post.full_url for post in POSTS]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
