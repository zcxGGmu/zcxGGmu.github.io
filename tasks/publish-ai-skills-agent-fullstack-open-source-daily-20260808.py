from __future__ import annotations

import html
import importlib.util
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
BASE_SCRIPT = TASKS / "publish-codegraph-code-map-coding-agent-article-20260808.py"

spec = importlib.util.spec_from_file_location("blog_publish_base", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["blog_publish_base"] = base
spec.loader.exec_module(base)

base.__file__ = __file__
base.TASKS = TASKS
base.DATE = "2026-08-09"
base.BASE_DT = datetime(2026, 8, 9, 0, 52, 0, tzinfo=timezone(timedelta(hours=8)))
base.SLUG = "ai-skills-agent-fullstack-open-source-daily-20260808"
base.URL_PATH = f"/2026/{base.SLUG}/"
base.FULL_URL = base.SITE + base.URL_PATH
base.TITLE = "8月8日 AI Skills/Agent 全栈开源项目速览：从技能标准到云端电脑"
base.DESC = "围绕 47 个热门开源项目，拆解 Skills 标准、Agent 框架、浏览器与数据工具、RAG、记忆、Claude/Codex 生态和 UI/UX 设计系统。"
base.CATEGORY = "AI工具"
base.SERIES = "AI Agent"
base.TAGS = [
    "AI Skills",
    "AI Agent",
    "开源项目",
    "Agent框架",
    "Claude Code",
    "Codex",
    "LangChain",
    "RAGFlow",
    "Firecrawl",
    "browser-use",
    "Cloudflare",
    "UI/UX",
]
base.MINUTES = 16
base.SOURCE_ID = "BV1ZMuM6GE4g"
base.PREV_EXISTING_URL = "/2026/codegraph-code-map-coding-agent-token-efficient-codebase-understanding/"
base.PREV_EXISTING_TITLE = "CodeGraph：给 Coding Agent 一张代码地图，少翻文件、少烧 Token、改得更准"
base.BODY_FILE = TASKS / f"{base.SLUG}-body.html"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-ai-skills-agent-fullstack-open-source-daily-20260808-changed-files.json"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def cover_svg() -> str:
    title_lines = ["8月8日 AI Skills/Agent", "全栈开源项目速览"]
    title_svg = "".join(
        f'<text x="92" y="{148 + i * 78}" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="{56 if i == 0 else 54}" font-weight="850">{esc(line)}</text>'
        for i, line in enumerate(title_lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">{esc(base.TITLE)}</title>
  <desc id="desc">{esc(base.DESC)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#020617"/><stop offset="0.48" stop-color="#123c69"/><stop offset="1" stop-color="#16a34a"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="20" stdDeviation="18" flood-color="#000" flood-opacity="0.32"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#dbeafe" stroke-width="3" fill="none">
    <path d="M170 630 H1430"/><path d="M170 500 H1430"/><path d="M170 370 H1430"/>
    <path d="M420 238 V742"/><path d="M760 238 V742"/><path d="M1100 238 V742"/>
    <path d="M250 620 C420 470 560 540 720 385 C875 235 1020 350 1198 220 C1335 120 1435 150 1510 94"/>
  </g>
  {title_svg}
  <text x="96" y="332" fill="#bbf7d0" font-family="Noto Sans SC, PingFang SC, Arial" font-size="31" font-weight="750">Skills 标准化 · Agent 基础设施 · 全栈 AI 工具链</text>
  <g filter="url(#shadow)">
    <rect x="96" y="520" width="398" height="132" rx="22" fill="#f8fafc" opacity="0.96"/>
    <text x="132" y="592" fill="#0f172a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="39" font-weight="850">47 个项目</text>
    <text x="132" y="635" fill="#047857" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="720">7 大板块系统拆解</text>
    <rect x="602" y="520" width="398" height="132" rx="22" fill="#ecfeff" opacity="0.92"/>
    <text x="638" y="592" fill="#0f172a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="37" font-weight="850">Skills</text>
    <text x="638" y="635" fill="#0369a1" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="720">专家经验可安装化</text>
    <rect x="1108" y="520" width="398" height="132" rx="22" fill="#052e16" opacity="0.82"/>
    <text x="1144" y="592" fill="#dcfce7" font-family="Noto Sans SC, PingFang SC, Arial" font-size="37" font-weight="850">Agent Stack</text>
    <text x="1144" y="635" fill="#bbf7d0" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="720">记忆 · 浏览器 · 云端电脑</text>
  </g>
  <text x="96" y="740" fill="#e2e8f0" font-family="Noto Sans SC, PingFang SC, Arial" font-size="27" font-weight="650">{esc(base.DESC[:58])}</text>
</svg>'''


def plain_text(html_text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(html_text))


def validate(outputs: dict[str, str]) -> None:
    failures: list[str] = []
    article = outputs[f"2026/{base.SLUG}/index.html"]
    cover = outputs[f"images/posts/{base.SLUG}/cover.svg"]
    body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    body_html = body_match.group(1) if body_match else ""
    body_plain = plain_text(body_html)
    if len(body_plain) < 8500:
        failures.append(f"body too short: {len(body_plain)}")
    for word in base.FORBIDDEN:
        if word in article or word in cover:
            failures.append(f"forbidden/source wording present: {word}")
    required = [
        "obra/superpowers",
        "anthropics/skills",
        "NousResearch/hermes-agent",
        "Agent-Reach",
        "PrimeIntellect-ai/prime-agent",
        "Firecrawl",
        "browser-use",
        "cloudflare/computer",
        "LangChain",
        "RAGFlow",
        "mem0",
        "Claude Code",
        "Codex",
        "UI/UX",
    ]
    for term in required:
        if term not in article:
            failures.append(f"missing required topic: {term}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links or len(h2) < 9:
        failures.append(f"toc mismatch or too few h2: h2={len(h2)} links={len(links)}")
    ET.fromstring(cover)
    ET.fromstring(outputs["index.xml"])
    home_cards = []
    for match in re.finditer(r'<a href="([^"]+)" class="a-block">', outputs["index.html"]):
        href = match.group(1)
        if href not in home_cards:
            home_cards.append(href)
    expected_prefix = base.PINNED_PREFIX + [base.URL_PATH, base.PREV_EXISTING_URL]
    if home_cards[: len(expected_prefix)] != expected_prefix:
        failures.append(f"homepage order mismatch: {home_cards[:len(expected_prefix)]}")
    if base.FULL_URL not in outputs["index.xml"]:
        failures.append("rss missing new article")
    if base.URL_PATH not in outputs["archive/index.html"]:
        failures.append("archive missing new article")
    prev_path = base.PREV_EXISTING_URL.strip("/") + "/index.html"
    if base.URL_PATH not in outputs[prev_path]:
        failures.append("previous article newer link missing")
    for path in [f"categories/{base.CATEGORY}/index.html", f"series/{base.SERIES}/index.html", *[f"tags/{tag}/index.html" for tag in base.TAGS]]:
        if base.URL_PATH not in outputs[path]:
            failures.append(f"{path} missing new article")
    if failures:
        raise SystemExit("\n".join(failures))


def main() -> None:
    base.cover_svg = cover_svg
    base.validate = validate
    base.write_outputs = write_outputs
    base.main()


def write_outputs(outputs: dict[str, str]) -> None:
    out_dir = Path("/tmp/ai-skills-agent-fullstack-open-source-daily-20260808-publish-output")
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(json.dumps({"local_output": str(out_dir), "files": len(outputs), "url": base.FULL_URL}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
