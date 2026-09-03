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
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv13s-bv1lz-bv1dr-bv1mf-bv1dxm-bv1dxu-20260903.py"
ASSET_ROOT = TASKS / "video-batch-20260903-bv1xn-bv1bv-bv1q2"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1xn-bv1bv-bv1q2-20260903-output")

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
pub.base.DATE = "2026-09-03"
pub.base.BASE_DT = datetime(2026, 9, 3, 23, 50, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/ordinary-people-long-downcycle-strategy/"
pub.base.PREV_EXISTING_TITLE = "普通人如何穿过经济下行长周期：别等拐点，先重建自己的安全垫"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1xn-bv1bv-bv1q2-20260903-changed-files.json"
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
        slug="pcb-upgrade-ai-server-single-machine-value-growth",
        title="PCB升级：单机价值量提升如何驱动AI服务器产业链增长",
        desc="AI服务器把PCB从低价值承载件推成高速连接系统，胜宏科技的目标价、资本开支、HDI与mSAP产能共同指向单机价值量重估。",
        category="投资研究",
        series="AI算力产业链",
        tags=["PCB", "AI服务器", "胜宏科技", "高盛", "HDI", "mSAP", "CoWoP", "资本开支", "AI算力"],
        minutes=19,
        body=body("BV1XntU6cEzf"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["胜宏科技", "PCB", "550 元", "232.98 元", "136.1%", "200 亿元", "66 亿元", "32.1%", "27.46 元"],
        minimum=4600,
    ),
    pub.base.Post(
        slug="shenghong-technology-q2-goldman-nomura-bofa-debate",
        title="胜宏科技Q2财报拆解：高盛、野村、美银到底在争什么",
        desc="同样维持买入判断，目标价却从367元到550元分化。真正差异在估值锚、竞争权重、成本层级和自由现金流。",
        category="投资研究",
        series="AI算力产业链",
        tags=["胜宏科技", "AI PCB", "高盛", "野村", "美银", "Rubin", "覆铜板", "资本开支", "现金流"],
        minutes=10,
        body=body("BV1bvtE6uE1X"),
        accent=("#111827", "#0f766e", "#f59e0b"),
        required=["61.1 亿元", "15.68 亿元", "32.1%", "389 元", "550 元", "367 元", "71 亿元", "50%"],
        minimum=3900,
    ),
    pub.base.Post(
        slug="americas-semiconductor-upcycle-compute-demand-2028",
        title="算力需求驱动美洲半导体上行周期延续至2028年",
        desc="缺电缺地、ASIC与CPU回归、先进封装设备、存储短缺、模拟芯片分化和EDA智能化，共同拉长美洲半导体上行周期。",
        category="投资研究",
        series="全球半导体周期",
        tags=["半导体", "AI算力", "ASIC", "CPU", "WFE", "先进封装", "存储", "EDA", "美洲半导体"],
        minutes=13,
        body=body("BV1q2tG6qE1w"),
        accent=("#111827", "#7c3aed", "#0ea5e9"),
        required=["2028", "1500 亿美元", "2800 亿美元", "5%", "5.9%", "3.9%", "37 亿美元", "2030"],
        minimum=4300,
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
        {"message": "Publish video-derived articles 2026-09-03", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
