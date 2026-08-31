#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
#     "pillow",
# ]
# ///

# ─── How to run ───
# 1. Install uv (if not installed):
#      curl -LsSf https://astral.sh/uv/install.sh | sh
# 2. Run directly (no venv, no pip install needed):
#      uv run tasks/publish-video-batch-bv1qy-bv1ug-followup-20260831.py
# 3. Or make executable and run:
#      chmod +x tasks/publish-video-batch-bv1qy-bv1ug-followup-20260831.py && ./tasks/publish-video-batch-bv1qy-bv1ug-followup-20260831.py
# ──────────────────

from __future__ import annotations

import base64
import importlib.util
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1rp-bv1mn-20260831.py"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1qy-bv1ug-followup-20260831-output")

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
pub.base.DATE = "2026-08-31"
pub.base.BASE_DT = datetime(2026, 8, 31, 23, 10, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/forty-year-mortgage-lower-payment-higher-lifetime-debt/"
pub.base.PREV_EXISTING_TITLE = "40年房贷不是便宜了：月供少616元，代价是多背10年债"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1qy-bv1ug-followup-20260831-changed-files.json"
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
        slug="shenghong-technology-nomura-q2-margin-capex-ai-pcb",
        title="胜宏科技二季度拆解：利润增长、毛利率承压与 AI PCB 资本开支",
        desc="表观利润高增与扣非利润下滑同时出现，关键变量是毛利率、71 亿元资本开支与下一代 AI PCB 产能卡位。",
        category="投资研究",
        series="AI算力产业链",
        tags=["胜宏科技", "AI PCB", "毛利率", "资本开支", "Blackwell", "Rubin", "覆铜板", "野村", "AI资本开支", "投资研究"],
        minutes=17,
        body=body("BV1qYtP65Ezg"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["胜宏科技", "263", "389", "毛利率", "扣非净利润", "11.6 亿元", "71 亿元", "Blackwell", "Rubin", "CoWoS", "资本开支"],
        minimum=5200,
    ),
    pub.base.Post(
        slug="poor-economics-choice-risk-policy-execution",
        title="贫穷的本质：看似不理性的选择，背后是被压缩的选择空间",
        desc="贫穷不是单纯收入不足，而是营养、健康、教育、风险、信贷、储蓄、工作和政策执行共同压缩选择空间。",
        category="读书",
        series="经典阅读",
        tags=["贫穷", "贫困", "发展经济学", "随机对照实验", "小额信贷", "储蓄", "教育", "健康", "社会观察", "认知"],
        minutes=73,
        body=body("BV1Ug4R6MEA5"),
        accent=("#111827", "#0f766e", "#d97706"),
        required=["贫穷的本质", "Odino", "化肥", "随机对照实验", "营养", "疫苗", "教育", "小额信贷", "储蓄", "乌干达", "电子投票", "选择空间"],
        minimum=9000,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "shenghong-technology-nomura-q2-margin-capex-ai-pcb": [],
    "poor-economics-choice-risk-policy-execution": [],
}


def render_asset_check() -> None:
    for post in pub.base.POSTS:
        svg = OUT_DIR / f"images/posts/{post.slug}/cover.svg"
        png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(
            ["sips", "-s", "format", "png", str(svg), "--out", str(png)],
            check=True,
            capture_output=True,
            text=True,
        )
        probe = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(png)],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        ).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe or png.stat().st_size < 4096:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = pub.base.run_gh(
            ["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"],
            {"content": content, "encoding": "utf-8"},
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
        {
            "message": "Publish follow-up video-derived articles 2026-08-31",
            "tree": tree["sha"],
            "parents": [ref.commit_sha],
        },
    )
    pub.base.run_gh(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
