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
#      uv run tasks/publish-video-batch-bv1rp-bv1mn-20260831.py
# 3. Or make executable and run:
#      chmod +x tasks/publish-video-batch-bv1rp-bv1mn-20260831.py && ./tasks/publish-video-batch-bv1rp-bv1mn-20260831.py
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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1fgt-20260830.py"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1rp-bv1mn-20260831-output")

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
pub.base.BASE_DT = datetime(2026, 8, 31, 22, 40, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/meituan-q2-unit-economics-profit-recovery/"
pub.base.PREV_EXISTING_TITLE = "美团二季度超预期：外卖单位经济模型、到店竞争缓和与 Keeta 出海"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1rp-bv1mn-20260831-changed-files.json"
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
        slug="forty-year-mortgage-lower-payment-higher-lifetime-debt",
        title="40年房贷不是便宜了：月供少616元，代价是多背10年债",
        desc="贷款期限从30年拉长到40年，月供少了约616元，却增加了利息和人生被债务锁定的时间。",
        category="宏观经济",
        series="房地产",
        tags=["房贷", "房地产", "居民负债", "银行", "存量房贷", "中国楼市", "现金流", "房价"],
        minutes=23,
        body=body("BV1rp4X6HEV1"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["40 年房贷", "月供", "616 元", "24.29 万元", "115.92 万元", "主办银行", "存量房贷", "房价", "银行", "时间换空间"],
        minimum=6000,
    ),
    pub.base.Post(
        slug="china-low-desire-society-more-severe-than-japan",
        title="中国低欲望社会：为什么可能比日本更剧烈",
        desc="低欲望不是年轻人不努力，而是未富先衰、房价压力、就业不稳、养老负担和数字娱乐共同推动的社会性撤退。",
        category="宏观经济",
        series="中国经济",
        tags=["低欲望社会", "日本", "年轻人", "消费", "生育率", "房地产", "就业", "社会信任"],
        minutes=20,
        body=body("BV1MN4r6NEyt"),
        accent=("#0f172a", "#7c3aed", "#0f766e"),
        required=["低欲望社会", "日本", "未富先衰", "草食男", "悟世代", "数字娱乐", "养老", "不婚", "生育率", "社会信任"],
        minimum=5200,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "forty-year-mortgage-lower-payment-higher-lifetime-debt": [],
    "china-low-desire-society-more-severe-than-japan": [],
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
            "message": "Publish video-derived articles 2026-08-31",
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
