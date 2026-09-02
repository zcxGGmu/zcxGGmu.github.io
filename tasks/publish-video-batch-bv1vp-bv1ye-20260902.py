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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1o8-bv1rp-bv1va-bv1bv-bv1ml-bv1rr-bv1x1-bv1q6-bv1s2-bv1sh-20260902.py"
ASSET_ROOT = TASKS / "video-batch-20260902-bv1vp-bv1ye"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1vp-bv1ye-20260902-output")

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
pub.base.DATE = "2026-09-02"
pub.base.BASE_DT = datetime(2026, 9, 2, 23, 58, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/dram-hbm-2027-price-upgrade-ai-memory-cycle/"
pub.base.PREV_EXISTING_TITLE = "DRAM 积极信号频出：2027 年 HBM 价格预期为何被上调"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1vp-bv1ye-20260902-changed-files.json"
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
        slug="shenghong-technology-goldman-next-gen-gpu-asic-ai-server-pcb-q2",
        title="胜宏科技：下一代 GPU 与 ASIC AI 服务器 PCB 驱动收入再加速",
        desc="二季度收入低于预期、毛利率承压，但库存、资本开支、AI PCB 市场规模上修和 550 元目标价共同指向下一代服务器 PCB 周期。",
        category="投资研究",
        series="AI算力产业链",
        tags=["胜宏科技", "AI PCB", "GPU", "ASIC", "高盛", "PCB", "资本开支", "覆铜板", "AI服务器"],
        minutes=6,
        body=body("BV1vPtM6SEA8"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["胜宏科技", "AI PCB", "GPU", "ASIC", "61.1 亿元", "32.1%", "59 亿元", "71 亿元", "550 元"],
        minimum=4300,
    ),
    pub.base.Post(
        slug="great-inflation-g20-trade-order-energy-security-ai-cost-repricing",
        title="大通胀避无可避：贸易秩序、能源安全与 AI 时代的成本重估",
        desc="通胀不只来自石油和 CPI，而来自全球分工被切开后，贸易秩序、能源安全、AI 硬件和关键资源共同触发的成本重估。",
        category="宏观经济",
        series="全球宏观观察",
        tags=["大通胀", "G20", "贸易秩序", "能源安全", "AI", "供应链", "CPI", "黄金", "人民币"],
        minutes=9,
        body=body("BV1YEt56eEbe"),
        accent=("#111827", "#dc2626", "#f59e0b"),
        required=["通胀", "G20", "贸易秩序", "能源安全", "AI", "CPI", "黄金", "供应链"],
        minimum=4000,
    ),
]


def chart_sources(slug: str) -> list[tuple[Path, str]]:
    return [(path, path.name) for path in sorted((CHART_ROOT / slug).glob("*.svg"))]


pub.SCREENSHOT_SOURCES = {post.slug: chart_sources(post.slug) for post in pub.base.POSTS}

FORBIDDEN = [
    "B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里",
    "本期", "这期", "作者说", "他提到", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "油管", "BV1",
    "下期", "欢迎收看", "感谢大家", "晴天AI实战",
]
previous.FORBIDDEN = FORBIDDEN
pub.FORBIDDEN = FORBIDDEN


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
        {"message": "Publish video-derived articles 2026-09-02", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
