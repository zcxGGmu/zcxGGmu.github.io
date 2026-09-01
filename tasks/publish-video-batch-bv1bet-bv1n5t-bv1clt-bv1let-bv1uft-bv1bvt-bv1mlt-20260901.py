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


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1qy-bv1ug-followup-20260831.py"
ASSET_ROOT = TASKS / "video-batch-20260901-bv1bet-bv1n5t-bv1clt-bv1let-bv1uft-bv1bvt-bv1mlt"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1bet-bv1n5t-bv1clt-bv1let-bv1uft-bv1bvt-bv1mlt-20260901-output")

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
pub.base.DATE = "2026-09-01"
pub.base.BASE_DT = datetime(2026, 9, 1, 23, 40, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/taste-skill-anti-slop-frontend-design-system/"
pub.base.PREV_EXISTING_TITLE = "Taste Skill：让 AI 前端摆脱模板化的设计规范与落地边界"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1bet-bv1n5t-bv1clt-bv1let-bv1uft-bv1bvt-bv1mlt-20260901-changed-files.json"
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
        slug="kingboard-laminates-ai-ccl-glass-fabric-65-hkd",
        title="建滔积层板：玻纤布瓶颈、AI CCL 占比抬升与 65 港元目标价",
        desc="覆铜板涨价、玻纤布供给瓶颈和 AI 高端材料占比提升，共同推动建滔积层板从周期材料向算力基础材料重估。",
        category="投资研究",
        series="AI算力产业链",
        tags=["建滔积层板", "覆铜板", "玻纤布", "AI CCL", "AI服务器", "PCB", "美银", "投资研究"],
        minutes=19,
        body=body("BV1bEtH6mEyW"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["建滔积层板", "65 港元", "玻纤布", "覆铜板", "AI CCL", "13x", "2027"],
        minimum=3900,
    ),
    pub.base.Post(
        slug="montage-technology-ai-demand-interconnect-2027",
        title="澜起科技：AI 服务器需求、内存接口现金牛与 2027 高速互联放量",
        desc="EPS 大幅超预期与毛利率短期承压并存，关键在 DDR5 RCD、MRDIMM、PCIe 与 CXL 新产品能否在 2027 年放量。",
        category="投资研究",
        series="AI算力产业链",
        tags=["澜起科技", "DDR5", "MRDIMM", "PCIe", "CXL", "Retimer", "AI服务器", "数据中心"],
        minutes=16,
        body=body("BV1n5ta6cEXG"),
        accent=("#111827", "#0f766e", "#2563eb"),
        required=["澜起科技", "0.94 元", "61.8%", "DDR5", "MRDIMM", "PCIe", "CXL", "2027", "377 元"],
        minimum=3900,
    ),
    pub.base.Post(
        slug="montage-technology-ddr5-pcie-cxl-data-center-highway",
        title="澜起科技：DDR5 代际爬坡、PCIe 7.0 与 CXL 打开数据中心高速公路",
        desc="从 DDR5 Gen6 9200 MT/s、MRCD/MDB 到 PCIe Switch 与 CXL 3.2，澜起科技正在构建 AI 数据中心高速互联产品组合。",
        category="投资研究",
        series="AI算力产业链",
        tags=["澜起科技", "DDR5", "MRCD", "MDB", "PCIe 7.0", "CXL 3.2", "高盛", "半导体"],
        minutes=22,
        body=body("BV1cLta6hEik"),
        accent=("#0f172a", "#7c3aed", "#06b6d4"),
        required=["澜起科技", "DDR5", "9200 MT/s", "MRCD", "MDB", "PCIe 7.0", "CXL 3.2", "572 港元"],
        minimum=3700,
    ),
    pub.base.Post(
        slug="shennan-circuits-pcb-ic-substrate-ai-growth",
        title="深南电路：PCB 与 IC 载板双轮驱动，AI 算力把制造底座重新定价",
        desc="上半年营收、净利润和毛利率同步改善，PCB 高端化与 IC 载板三位数增长，共同支撑深南电路的 AI 算力底座逻辑。",
        category="投资研究",
        series="AI算力产业链",
        tags=["深南电路", "PCB", "IC载板", "ABF", "AI服务器", "毛利率", "国产替代", "投资研究"],
        minutes=12,
        body=body("BV1LetP6CEqw"),
        accent=("#111827", "#16a34a", "#2563eb"),
        required=["深南电路", "152.96 亿元", "22.5 亿元", "32.6%", "PCB", "IC 载板", "ABF", "518 元", "43%"],
        minimum=3700,
    ),
    pub.base.Post(
        slug="economic-machine-debt-credit-consumption-cycle",
        title="经济机器如何突然衰退：债务、信贷、消费与去杠杆循环",
        desc="从交易、信用、生产率、短期债务周期和长期债务周期出发，解释繁荣为什么会突然转向衰退，以及去杠杆如何发生。",
        category="宏观经济",
        series="经济通识课",
        tags=["经济周期", "债务", "信贷", "消费", "去杠杆", "生产率", "中央银行", "宏观经济"],
        minutes=31,
        body=body("BV1Ufth63EnD"),
        accent=("#0f172a", "#0891b2", "#f59e0b"),
        required=["交易", "信用", "债务", "生产率", "短期债务周期", "长期债务周期", "去杠杆", "75-100 年"],
        minimum=4400,
    ),
    pub.base.Post(
        slug="cpo-equipment-orders-domestic-supply-chain-lianxun",
        title="CPO 设备产业链：订单翻倍预期、国产设备布局与联讯仪器盈利拐点",
        desc="明年 CPO 设备订单翻倍预期明确，测试、固晶、耦合、键合等国产设备环节持续布局，联讯仪器中报验证盈利和订单弹性。",
        category="投资研究",
        series="光通信产业链",
        tags=["CPO", "光模块", "联讯仪器", "猎奇智能", "快克智能", "1.6T", "2.4T", "设备国产化"],
        minutes=11,
        body=body("BV1bVtM6CEbc"),
        accent=("#111827", "#0ea5e9", "#ec4899"),
        required=["CPO", "联讯仪器", "72.68%", "303%", "1.6T", "2.4T", "猎奇智能", "快克智能"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="semiconductor-communication-q2-ai-storage-iot-valuation",
        title="半导体与通信 Q2 业绩兑现：AI 算力、存储与物联网模组的三条景气线",
        desc="AI 硬件需求未见明确拐点，存储业绩与估值匹配度提升，物联网模组进入左侧修复，构成半导体与通信的三条景气线。",
        category="投资研究",
        series="半导体与通信",
        tags=["半导体", "通信", "AI算力", "存储", "物联网模组", "长鑫科技", "美格智能", "东山精密", "HBM"],
        minutes=24,
        body=body("BV1MLtM6VE8p"),
        accent=("#0f172a", "#7c3aed", "#14b8a6"),
        required=["AI 算力", "存储", "物联网模组", "长鑫科技", "美格智能", "东山精密", "HBM", "分红"],
        minimum=4000,
    ),
]


def chart_sources(slug: str) -> list[tuple[Path, str]]:
    return [(path, path.name) for path in sorted((CHART_ROOT / slug).glob("*.svg"))]


pub.SCREENSHOT_SOURCES = {post.slug: chart_sources(post.slug) for post in pub.base.POSTS}


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


FORBIDDEN = [
    "B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里",
    "本期", "这期", "作者说", "他提到", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "油管", "BV1",
]

pub.FORBIDDEN = FORBIDDEN


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
    tree = pub.base.run_gh(["-X", "POST", pub.base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = pub.base.run_gh(
        ["-X", "POST", pub.base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish video-derived articles 2026-09-01", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
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
        if len(re.findall(r'<h2 id="', article)) < 5:
            raise RuntimeError(f"remote h2 count too low: {post.slug}")
        if post.full_url not in sitemap:
            raise RuntimeError(f"sitemap missing {post.slug}")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            rel = f"images/posts/{post.slug}/{dest}"
            data = pub.base.run_gh([pub.base.endpoint(f"contents/{quote(rel, safe='/')}?ref={commit_sha}")])
            raw = base64.b64decode(data["content"])
            ET.fromstring(raw.decode("utf-8"))
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


pub.write_outputs = write_outputs
pub.render_asset_check = render_asset_check
pub.create_commit = create_commit
pub.verify_remote_publish = verify_remote_publish


if __name__ == "__main__":
    pub.main()
