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
#      uv run tasks/publish-video-batch-bv1fgt-20260830.py
# 3. Or make executable and run:
#      chmod +x tasks/publish-video-batch-bv1fgt-20260830.py && ./tasks/publish-video-batch-bv1fgt-20260830.py
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
PREV_WRAPPER = TASKS / "publish-video-batch-bv146-bv1elk-20260830.py"
ASSET_ROOT = TASKS / "video-batch-20260830-bv1fgt"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1fgt-20260830-output")

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
pub.base.DATE = "2026-08-30"
pub.base.BASE_DT = datetime(2026, 8, 30, 23, 20, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/shenghong-technology-margin-capex-ai-pcb/"
pub.base.PREV_EXISTING_TITLE = "胜宏科技中报：毛利率承压，AI PCB高资本开支换长期卡位"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1fgt-20260830-changed-files.json"
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
        slug="meituan-q2-unit-economics-profit-recovery",
        title="美团二季度超预期：外卖单位经济模型、到店竞争缓和与 Keeta 出海",
        desc="外卖单位利润修复、到店竞争缓和、Keeta 出海与低成本 AI，推动估值重定价。",
        category="投资研究",
        series="互联网平台",
        tags=["美团", "外卖", "单位经济模型", "本地生活", "到店酒旅", "即时零售", "Keeta", "LongCat", "AI", "高盛"],
        minutes=17,
        body=body("BV1FgtT6oEem"),
        accent=("#111827", "#f59e0b", "#0f766e"),
        required=["美团", "57 亿元", "34 亿元", "冲减收入", "单位经济模型", "单均", "到店", "Keeta", "即时零售", "LongCat", "123 港元", "77.50 港元"],
        minimum=5600,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "meituan-q2-unit-economics-profit-recovery": [],
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
            "message": "Publish video-derived article 2026-08-30",
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
