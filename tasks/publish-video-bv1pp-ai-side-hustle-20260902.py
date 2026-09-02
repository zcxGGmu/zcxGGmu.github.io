#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
#     "pillow",
# ]
# ///

from __future__ import annotations

import base64
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET

import requests


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1bet-bv1n5t-bv1clt-bv1let-bv1uft-bv1bvt-bv1mlt-20260901.py"
ASSET_ROOT = TASKS / "video-single-20260902-bv1pp-ai-side-hustle"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-bv1pp-ai-side-hustle-20260902-output")

spec = importlib.util.spec_from_file_location("previous_video_publisher", PREV_WRAPPER)
previous = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = previous
spec.loader.exec_module(previous)

pub = previous.pub


def body(bvid: str) -> str:
    return (DRAFTS / f"{bvid}-body.html").read_text(encoding="utf-8")


cursor = previous
while True:
    if hasattr(cursor, "OUT_DIR"):
        cursor.OUT_DIR = OUT_DIR
    if not hasattr(cursor, "previous"):
        break
    cursor = cursor.previous

FORBIDDEN = [
    "B站",
    "bilibili",
    "Bilibili",
    "哔哩",
    "UP主",
    "up主",
    "原视频",
    "视频中",
    "视频里",
    "音频中",
    "音频里",
    "本期",
    "这期",
    "作者说",
    "他提到",
    "观看",
    "点赞",
    "投币",
    "收藏",
    "订阅",
    "关注",
    "三连",
    "油管",
    "BV1",
]

pub.FORBIDDEN = FORBIDDEN
pub.base.FORBIDDEN = FORBIDDEN
pub.base.__file__ = __file__
pub.base.DATE = "2026-09-02"
pub.base.BASE_DT = datetime(2026, 9, 2, 11, 30, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/archify-verifiable-agent-diagrams-workflow/"
pub.base.PREV_EXISTING_TITLE = "Archify：把 Agent 架构图变成可校验、可追溯的工程交付物"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-bv1pp-ai-side-hustle-20260902-changed-files.json"
pub.base.PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
    "/2026/original-accumulation-time-autonomy-ordinary-people/",
    "/2026/next-decade-wealth-leap-deflation-rmb-ai-cashflow/",
]

SLUG = "ai-side-hustle-feishu-bitable-template-enterprise-system"

pub.base.POSTS = [
    pub.base.Post(
        slug=SLUG,
        title="AI副业观察: 从飞书多维表格模板到企业智能化系统定制",
        desc="从个人目标管理模板、内容获客、小团队系统定制到一人公司协作网络，拆解 AI 工具副业如何从低客单标准品升级为高客单服务。",
        category="商业思维",
        series="AI副业观察",
        tags=["AI副业", "飞书多维表格", "低代码", "模板产品", "企业服务", "小微企业", "内容获客", "自由职业", "一人公司"],
        minutes=20,
        body=body("BV1Pp416uEfq"),
        accent=("#0f172a", "#2563eb", "#f97316"),
        required=["AI副业观察", "AI 副业", "飞书多维表格", "模板", "50 万", "10 万", "50+", "小微团队", "内容获客", "一人公司"],
        minimum=5200,
    )
]


def chart_sources(slug: str) -> list[tuple[Path, str]]:
    return [(path, path.name) for path in sorted((CHART_ROOT / slug).glob("*.svg"))]


pub.SCREENSHOT_SOURCES = {SLUG: chart_sources(SLUG)}


def write_outputs(outputs: dict[str, str | None], binary_outputs: dict[str, bytes]) -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        if content is None:
            continue
        path = OUT_DIR / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for rel, content in binary_outputs.items():
        path = OUT_DIR / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(
        json.dumps(
            {
                "local_output": str(OUT_DIR),
                "text_files": len([v for v in outputs.values() if v is not None]),
                "binary_files": len(binary_outputs),
                "deleted": len([v for v in outputs.values() if v is None]),
                "urls": [post.full_url for post in pub.base.POSTS],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def render_asset_check() -> None:
    for post in pub.base.POSTS:
        cover = OUT_DIR / f"images/posts/{post.slug}/cover.svg"
        cover_content = cover.read_text(encoding="utf-8")
        ET.fromstring(cover_content)
        bad_cover = [word for word in FORBIDDEN if word in cover_content]
        if bad_cover:
            raise RuntimeError(f"forbidden wording in cover {post.slug}: {bad_cover}")
        cover_png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(cover), "--out", str(cover_png)], check=True, capture_output=True, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(cover_png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe or cover_png.stat().st_size < 4096:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")
        if len(pub.SCREENSHOT_SOURCES[post.slug]) < 8:
            raise RuntimeError(f"too few chapter charts: {post.slug}")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            chart = OUT_DIR / f"images/posts/{post.slug}/{dest}"
            content = chart.read_text(encoding="utf-8")
            ET.fromstring(content)
            bad = [word for word in FORBIDDEN if word in content]
            if bad:
                raise RuntimeError(f"forbidden wording in chart {post.slug}/{dest}: {bad}")
            chart_png = Path(f"/tmp/{post.slug}-{chart.stem}.png")
            subprocess.run(["sips", "-s", "format", "png", str(chart), "--out", str(chart_png)], check=True, capture_output=True, text=True)
            chart_probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(chart_png)], check=True, stdout=subprocess.PIPE, text=True).stdout
            if "pixelWidth: 1200" not in chart_probe or "pixelHeight: 675" not in chart_probe or chart_png.stat().st_size < 8192:
                raise RuntimeError(f"chart render failed: {post.slug}/{dest}: {chart_probe}")


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = pub.base.run_gh(
            ["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"],
            {"content": base64.b64encode(content.encode("utf-8")).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    for path, content in sorted(binary_outputs.items()):
        blob = pub.base.run_gh(
            ["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"],
            {"content": base64.b64encode(content).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = pub.base.run_gh(["-X", "POST", pub.base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = pub.base.run_gh(
        ["-X", "POST", pub.base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish AI side hustle article 2026-09-02", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def remote_file(path: str, commit_sha: str) -> str:
    data = pub.base.run_gh([pub.base.endpoint(f"contents/{quote(path, safe='/')}?ref={commit_sha}")])
    return base64.b64decode(data["content"]).decode("utf-8")


def expect_http(url: str, status: int = 200) -> None:
    for _ in range(8):
        response = requests.get(url, timeout=20)
        if response.status_code == status:
            return
        time.sleep(5)
    raise RuntimeError(f"public HTTP check failed: {url} expected {status}, got {response.status_code}")


def verify_remote_publish(commit_sha: str, card_count: int, total_pages: int, binary_outputs: dict[str, bytes]) -> None:
    tree = pub.base.run_gh([pub.base.endpoint(f"git/trees/{commit_sha}?recursive=1")])["tree"]
    paths = {entry["path"] for entry in tree}
    if any("__pycache__" in path for path in paths):
        raise RuntimeError("remote tree includes __pycache__")

    home = remote_file("index.html", commit_sha)
    rss = remote_file("index.xml", commit_sha)
    sitemap = remote_file("sitemap.xml", commit_sha)
    home_hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', home)
    expected_prefix = pub.base.PINNED_PREFIX + [post.url_path for post in pub.base.POSTS] + [pub.base.PREV_EXISTING_URL]
    if home_hrefs[: len(expected_prefix)] != expected_prefix:
        raise RuntimeError(f"homepage prefix mismatch: {home_hrefs[:len(expected_prefix)]}")
    rss_links = re.findall(r"<link>(https://zcxggmu.github.io/2026/[^<]+/)</link>", rss)
    if rss_links[: len(pub.base.POSTS)] != [post.full_url for post in pub.base.POSTS]:
        raise RuntimeError(f"rss order mismatch: {rss_links[:len(pub.base.POSTS)]}")

    cards: list[str] = []
    for page in range(1, total_pages + 1):
        path = "index.html" if page == 1 else f"page/{page}/index.html"
        if path not in paths:
            raise RuntimeError(f"remote pagination page missing: {path}")
        cards.extend(re.findall(r'<a href="([^"]+)" class="a-block">', remote_file(path, commit_sha)))
    if len(cards) != card_count or len(cards) != len(set(cards)):
        raise RuntimeError("remote pagination coverage failed")

    for post in pub.base.POSTS:
        article_path = f"2026/{post.slug}/index.html"
        if article_path not in paths:
            raise RuntimeError(f"remote article missing: {article_path}")
        article = remote_file(article_path, commit_sha)
        if post.title not in article:
            raise RuntimeError(f"remote article title missing: {post.slug}")
        bad = [word for word in FORBIDDEN if word in article]
        if bad:
            raise RuntimeError(f"remote forbidden wording in {post.slug}: {bad}")
        if article.count('<h2 id="') != 8:
            raise RuntimeError(f"remote h2 count mismatch: {post.slug}")
        if article.count('<figure class="post-figure">') != len(pub.SCREENSHOT_SOURCES[post.slug]):
            raise RuntimeError(f"remote figure count mismatch: {post.slug}")
        if post.full_url not in sitemap:
            raise RuntimeError(f"sitemap missing {post.slug}")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            rel = f"images/posts/{post.slug}/{dest}"
            data = pub.base.run_gh([pub.base.endpoint(f"contents/{quote(rel, safe='/')}?ref={commit_sha}")])
            raw = base64.b64decode(data["content"])
            ET.fromstring(raw.decode("utf-8"))
            if raw != binary_outputs[rel]:
                raise RuntimeError(f"remote chart bytes mismatch: {rel}")

    for _ in range(18):
        try:
            build = pub.base.run_gh([pub.base.endpoint("pages/builds/latest")])
            error = build.get("error") or {}
            message = error.get("message") if isinstance(error, dict) else error
            if build.get("commit") == commit_sha and build.get("status") == "built" and not message:
                break
            if build.get("commit") == commit_sha and message:
                raise RuntimeError(f"GitHub Pages build failed: {message}")
        except RuntimeError as exc:
            if "Not Found" not in str(exc):
                raise
        time.sleep(5)
    else:
        raise RuntimeError("GitHub Pages build did not reach built state")

    post = pub.base.POSTS[0]
    expect_http(post.full_url)
    expect_http("https://zcxggmu.github.io/index.xml")
    expect_http("https://zcxggmu.github.io/sitemap.xml")
    expect_http("https://zcxggmu.github.io/page/2/")
    expect_http(f"https://zcxggmu.github.io/page/{total_pages}/")
    expect_http("https://zcxggmu.github.io/page/0/", 404)
    for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
        expect_http(f"https://zcxggmu.github.io/images/posts/{post.slug}/{dest}")


pub.write_outputs = write_outputs
pub.render_asset_check = render_asset_check
pub.create_commit = create_commit
pub.verify_remote_publish = verify_remote_publish


if __name__ == "__main__":
    pub.main()
