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
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1px-bv16p-bv1qz-bv1g1-bv1pu-20260905.py"
ASSET_ROOT = TASKS / "video-batch-20260906-bv18a-bv1xx-bv1rd"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv18a-bv1xx-bv1rd-20260906-output")

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

pub.base.__file__ = __file__
pub.base.DATE = "2026-09-06"
pub.base.BASE_DT = datetime(2026, 9, 6, 23, 50, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/wage-doubles-real-purchasing-power-free-surplus-gap/"
pub.base.PREV_EXISTING_TITLE = "工资翻倍之后，购买力为何可能翻四倍：真实节余决定生活分层"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv18a-bv1xx-bv1rd-20260906-changed-files.json"
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

pub.base.POSTS = [
    pub.base.Post(
        slug="g20-19-to-1-china-manufacturing-resident-consumption-rebalance",
        title="G20“19:1”背后：中国制造下半场必须回答普通人的位置",
        desc="从G20外部失衡争议出发，重新理解中国生产、世界消费的旧全球化模式为何触顶，以及居民收入、保障和内需再平衡为何成为工业下半场的核心问题。",
        category="宏观经济",
        series="中国经济观察",
        tags=["G20", "贸易顺差", "居民消费", "中国制造", "内需", "收入分配", "社会保障", "全球化", "工业化"],
        minutes=21,
        body=body("BV18Atm69ExL"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["G20", "19:1", "外部失衡", "贸易顺差", "居民消费", "40%", "56%", "1.4万亿", "工业下半场"],
        minimum=5600,
    ),
    pub.base.Post(
        slug="ai-replaces-work-basic-income-human-purpose",
        title="当 AI 不再需要人类工作，普通人靠什么活着",
        desc="AI工作流和机器人正在重新定义生产力，真正的挑战不是机器是否统治人类，而是当岗位需求下降后，财富、基本保障、时间和人的价值如何重新分配。",
        category="AI观察",
        series="AI与社会",
        tags=["AI", "机器人", "工作流", "就业", "基本收入", "生产关系", "财富分配", "人文主义", "未来社会"],
        minutes=13,
        body=body("BV1xxbj6aEkp"),
        accent=("#111827", "#7c3aed", "#0ea5e9"),
        required=["AI", "机器人", "工作流", "20多分钟", "办公室", "程序员", "物理世界", "基本需求", "生产关系"],
        minimum=4400,
    ),
    pub.base.Post(
        slug="china-ai-infrastructure-chip-hbm-system-breakthrough",
        title="中国AI基础设施爆发：真正瓶颈是晶圆与HBM",
        desc="Token需求近千倍增长之后，先进晶圆、良率、HBM、Chiplet、CANN、超级节点、液冷和电力系统共同决定本土算力突围。",
        category="产业观察",
        series="AI算力产业链",
        tags=["AI基础设施", "AI芯片", "HBM", "Chiplet", "先进封装", "CANN", "液冷", "数据中心", "储能"],
        minutes=20,
        body=body("BV1RDtd6XEe6"),
        accent=("#0f172a", "#7c3aed", "#0ea5e9"),
        required=["Token", "1000倍", "80%", "1400万颗", "200万颗", "500万颗", "HBM", "Chiplet", "CANN", "液冷"],
        minimum=5300,
    ),
]


def chart_sources(slug: str) -> list[tuple[Path, str]]:
    return [(path, path.name) for path in sorted((CHART_ROOT / slug).glob("*.svg"))]


pub.SCREENSHOT_SOURCES = {post.slug: chart_sources(post.slug) for post in pub.base.POSTS}

FORBIDDEN = [
    "B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里",
    "本期", "这期", "作者说", "他提到", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "油管",
    "下期", "欢迎收看", "感谢大家", "晴天AI实战", "BV1",
]
previous.FORBIDDEN = FORBIDDEN
pub.FORBIDDEN = FORBIDDEN
if hasattr(pub.base, "FORBIDDEN"):
    pub.base.FORBIDDEN = FORBIDDEN


def render_asset_check() -> None:
    for post in pub.base.POSTS:
        cover = OUT_DIR / f"images/posts/{post.slug}/cover.svg"
        cover_png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(cover), "--out", str(cover_png)], check=True, capture_output=True, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(cover_png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe or cover_png.stat().st_size < 4096:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")
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
    tree = pub.base.run_gh(
        ["-X", "POST", pub.base.endpoint("git/trees"), "--input", "-"],
        {"base_tree": ref.tree_sha, "tree": entries},
    )
    commit = pub.base.run_gh(
        ["-X", "POST", pub.base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish video-derived articles 2026-09-06", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


old_verify_remote_publish = pub.verify_remote_publish


def remote_file(path: str, commit_sha: str) -> str:
    data = pub.base.run_gh([pub.base.endpoint(f"contents/{quote(path, safe='/')}?ref={commit_sha}")])
    return base64.b64decode(data["content"]).decode("utf-8")


def verify_remote_publish(commit_sha: str, card_count: int, total_pages: int, binary_outputs: dict[str, bytes]) -> None:
    old_verify_remote_publish(commit_sha, card_count, total_pages, binary_outputs)
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
    for post in pub.base.POSTS:
        article = remote_file(f"2026/{post.slug}/index.html", commit_sha)
        bad = [word for word in FORBIDDEN if word in article]
        if bad:
            raise RuntimeError(f"forbidden wording in remote article {post.slug}: {bad}")
        if article.count('<figure class="post-figure">') != len(pub.SCREENSHOT_SOURCES[post.slug]):
            raise RuntimeError(f"remote figure count mismatch: {post.slug}")
        if len(re.findall(r'<h2 id="', article)) < 7:
            raise RuntimeError(f"remote h2 count too low: {post.slug}")
        if post.full_url not in sitemap:
            raise RuntimeError(f"sitemap missing {post.slug}")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            rel = f"images/posts/{post.slug}/{dest}"
            data = pub.base.run_gh([pub.base.endpoint(f"contents/{quote(rel, safe='/')}?ref={commit_sha}")])
            raw = base64.b64decode(data["content"])
            root = ET.fromstring(raw.decode("utf-8"))
            if root.attrib.get("width") != "1200" or root.attrib.get("height") != "675":
                raise RuntimeError(f"remote svg dimensions mismatch: {rel}")
    for _ in range(12):
        try:
            build = pub.base.run_gh([pub.base.endpoint("pages/builds/latest")])
            error = build.get("error") or {}
            message = error.get("message") if isinstance(error, dict) else error
            if build.get("commit") == commit_sha and build.get("status") == "built" and not message:
                return
            if build.get("commit") == commit_sha and message:
                raise RuntimeError(f"GitHub Pages build failed: {message}")
        except RuntimeError as exc:
            if "Not Found" not in str(exc):
                raise
        time.sleep(5)
    raise RuntimeError("GitHub Pages build did not reach built state")


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit
pub.verify_remote_publish = verify_remote_publish


if __name__ == "__main__":
    pub.main()
