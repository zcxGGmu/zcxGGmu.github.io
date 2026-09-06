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
PREV_WRAPPER = TASKS / "publish-video-batch-bv18a-bv1xx-bv1rd-20260906.py"
ASSET_ROOT = TASKS / "video-batch-20260906-bv1lc-bv1vr-bv1ju-bv1vo-bv1rk"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1lc-bv1vr-bv1vo-bv1rk-20260906-output")

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
pub.base.BASE_DT = datetime(2026, 9, 6, 23, 59, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/g20-19-to-1-china-manufacturing-resident-consumption-rebalance/"
pub.base.PREV_EXISTING_TITLE = "G20“19:1”背后：中国制造下半场必须回答普通人的位置"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1lc-bv1vr-bv1vo-bv1rk-20260906-changed-files.json"
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
        slug="money-psychology-wealth-human-nature-time-freedom",
        title="《金钱心理学》：财富的终点，是把时间还给自己",
        desc="用私人经济史、运气、知足、复利、生存、尾部赢家、现金缓冲和时间自由，重新理解普通人怎样把财富从数字变成选择权。",
        category="个人财务",
        series="财富认知课",
        tags=["金钱心理学", "个人财务", "复利", "储蓄", "风险管理", "时间自由", "行为金融", "财富观", "家庭理财"],
        minutes=62,
        body=body("BV1LctJ6HEsW"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["金钱心理学", "1700 平米", "75%", "私人经济史", "1%", "80%", "5000 万", "845 亿美元", "815 亿美元", "时间自由"],
        minimum=6500,
    ),
    pub.base.Post(
        slug="island-economics-fish-capital-money-debt-crisis",
        title="《小岛经济学》：从一条鱼看懂增长、货币、债务与危机",
        desc="从徒手抓鱼、鱼网、储蓄、银行和鱼券讲到政府、外部资金、棚屋泡沫、定量鱼券与最终买单者，回到真实资源和生产率。",
        category="宏观经济",
        series="经济学入门",
        tags=["小岛经济学", "宏观经济", "货币", "储蓄", "银行", "债务", "通胀", "房地产泡沫", "经济危机"],
        minutes=132,
        body=body("BV1vr8u6cEje"),
        accent=("#0f172a", "#0f766e", "#f97316"),
        required=["小岛经济学", "爱博", "贝克", "查理", "鱼网", "储蓄", "鱼券", "官鱼", "中岛", "棚屋", "定量鱼券"],
        minimum=8200,
    ),
    pub.base.Post(
        slug="company-valuation-china-framework-price-value-dcf",
        title="股票到底值多少钱：估值中国化的第一性原理",
        desc="从价格不等于价值出发，用达摩达兰估值框架、中国市场参数、DCF 与相对估值方法，建立普通投资者可复用的公司估值顺序。",
        category="投资研究",
        series="估值中国化",
        tags=["估值", "DCF", "PE", "PB", "PEG", "PS", "EV/EBITDA", "A股", "港股", "达摩达兰"],
        minutes=9,
        body=body("BV1VotU6iEDK"),
        accent=("#111827", "#7c3aed", "#0ea5e9"),
        required=["估值", "价格不等于价值", "达摩达兰", "纽约大学", "27 节", "DCF", "PE", "PB", "PEG", "PS", "EV/EBITDA"],
        minimum=4300,
    ),
    pub.base.Post(
        slug="rich-dad-poor-dad-china-wealth-action-map-risk-correction",
        title="《富爸爸穷爸爸》中国版财富行动地图：能学什么，不能照搬什么",
        desc="区分资产、负债、现金流、职业、事业、公司结构、投资机会和技能组合，同时把美国案例放回中国家庭的合规与风险边界。",
        category="个人财务",
        series="财富认知课",
        tags=["富爸爸穷爸爸", "资产", "负债", "现金流", "财商", "个人财务", "公司制", "税务", "财富自由"],
        minutes=80,
        body=body("BV1RK3T6rE8B"),
        accent=("#111827", "#dc2626", "#0ea5e9"),
        required=["富爸爸", "穷爸爸", "51种语言", "109个国家", "4000万册", "资产", "负债", "现金流", "麦当劳", "公司", "税前"],
        minimum=6200,
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
        expected_figures = len(pub.SCREENSHOT_SOURCES[post.slug])
        if article.count('<figure class="post-figure">') != expected_figures:
            raise RuntimeError(f"remote figure count mismatch: {post.slug}")
        if len(re.findall(r'<h2 id="', article)) != expected_figures:
            raise RuntimeError(f"remote h2/figure mismatch: {post.slug}")
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
