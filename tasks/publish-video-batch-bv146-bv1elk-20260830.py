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
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1tq-bv1d1-bv1mht-bv1yc-20260829.py"
ASSET_ROOT = TASKS / "video-batch-20260829-bv146-bv1elk"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv146-bv1elk-20260830-output")

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
pub.base.BASE_DT = datetime(2026, 8, 30, 22, 30, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/kangbo-wealth-cycle-boundary/"
pub.base.PREV_EXISTING_TITLE = "康波不是财富密码：周期、位置与普通人的投资边界"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv146-bv1elk-20260830-changed-files.json"
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
        slug="shenghong-technology-margin-capex-ai-pcb",
        title="胜宏科技中报：毛利率承压，AI PCB高资本开支换长期卡位",
        desc="胜宏科技上半年收入和利润保持增长，但扣非利润与毛利率承压；71亿元级资本开支押注 AI PCB 与下一轮平台升级，估值能否兑现取决于产能、订单和现金流。",
        category="投资研究",
        series="AI算力产业链",
        tags=["胜宏科技", "AI PCB", "PCB", "毛利率", "资本开支", "覆铜板", "Blackwell", "Rubin", "估值", "风险"],
        minutes=4,
        body=body("BV1464261EWB"),
        accent=("#111827", "#1d4ed8", "#0f766e"),
        required=["胜宏科技", "AI PCB", "毛利率", "扣非净利润", "资本开支", "覆铜板", "Blackwell", "Rubin", "CoWoS", "现金流"],
        minimum=3500,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "shenghong-technology-margin-capex-ai-pcb": [
        (ASSET_ROOT / "article-images" / "01-quick-note-clean-large.jpg", "01-quick-note.jpg"),
    ],
}


def render_asset_check() -> None:
    from PIL import Image

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
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            image_path = OUT_DIR / f"images/posts/{post.slug}/{dest}"
            image = Image.open(image_path).convert("RGB")
            if image.width < 1200 or image.height < 480:
                raise RuntimeError(f"screenshot dimensions too small: {post.slug}/{dest}: {image.size}")
            if image_path.stat().st_size < 40_000:
                raise RuntimeError(f"screenshot file unexpectedly small: {post.slug}/{dest}")
            edge_lines = [
                [image.getpixel((x, 0)) for x in range(image.width)],
                [image.getpixel((x, image.height - 1)) for x in range(image.width)],
                [image.getpixel((0, y)) for y in range(image.height)],
                [image.getpixel((image.width - 1, y)) for y in range(image.height)],
            ]
            dark_line = max(
                sum(1 for r, g, b in line if r < 18 and g < 18 and b < 18) / len(line)
                for line in edge_lines
            )
            if dark_line >= 0.95:
                raise RuntimeError(f"screenshot black-edge check failed: {post.slug}/{dest}: dark_line={dark_line:.3f}")


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
