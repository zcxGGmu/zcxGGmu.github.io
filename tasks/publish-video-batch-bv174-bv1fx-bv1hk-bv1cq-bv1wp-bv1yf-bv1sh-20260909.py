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
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv16k-bv1qt-bv1hm-bv1lk-20260908.py"
ASSET_ROOT = TASKS / "video-batch-20260909-bv174-bv1fx-bv1hk-bv1cq-bv1wp-bv1yf-bv1sh"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
POST_MANIFEST = DRAFTS / "20260909-video-batch-bv174-bv1fx-bv1hk-bv1cq-bv1wp-bv1yf-bv1sh-posts.json"
OUT_DIR = Path("/tmp/video-batch-bv174-bv1fx-bv1hk-bv1cq-bv1wp-bv1yf-bv1sh-20260909-output")

spec = importlib.util.spec_from_file_location("previous_video_publisher", PREV_WRAPPER)
previous = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = previous
spec.loader.exec_module(previous)

pub = previous.pub


def body(bvid: str) -> str:
    return (DRAFTS / f"{bvid}-body.html").read_text(encoding="utf-8")


def load_posts() -> list:
    payload = json.loads(POST_MANIFEST.read_text(encoding="utf-8"))
    posts = []
    for item in payload:
        posts.append(
            pub.base.Post(
                slug=item["slug"],
                title=item["title"],
                desc=item["desc"],
                category=item["category"],
                series=item["series"],
                tags=item["tags"],
                minutes=item["minutes"],
                body=body(item["bvid"]),
                accent=tuple(item["accent"]),
                required=item["required"],
                minimum=item["minimum"],
            )
        )
    return posts


cursor = previous
while True:
    if hasattr(cursor, "OUT_DIR"):
        cursor.OUT_DIR = OUT_DIR
    if not hasattr(cursor, "previous"):
        break
    cursor = cursor.previous

pub.base.__file__ = __file__
pub.base.DATE = "2026-09-09"
pub.base.BASE_DT = datetime(2026, 9, 9, 23, 59, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/shenghong-tech-h1-2026-rubin-expansion-valuation/"
pub.base.PREV_EXISTING_TITLE = "胜宏科技还值得持有吗：半年报、扩产与 Rubin 需求的兑现题"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv174-bv1fx-bv1hk-bv1cq-bv1wp-bv1yf-bv1sh-20260909-changed-files.json"
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
pub.base.POSTS = load_posts()


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


def run_gh_cli_compat(args: list[str], payload: dict | None = None):
    cursor = previous
    while True:
        if hasattr(cursor, "run_gh_cli_compat"):
            return cursor.run_gh_cli_compat(args, payload)
        if not hasattr(cursor, "previous"):
            break
        cursor = cursor.previous
    raise RuntimeError("run_gh_cli_compat was not found in publisher chain")


pub.base.run_gh = run_gh_cli_compat


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = run_gh_cli_compat(
            ["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"],
            {"content": base64.b64encode(content.encode("utf-8")).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    for path, content in sorted(binary_outputs.items()):
        blob = run_gh_cli_compat(
            ["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"],
            {"content": base64.b64encode(content).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = run_gh_cli_compat(
        ["-X", "POST", pub.base.endpoint("git/trees"), "--input", "-"],
        {"base_tree": ref.tree_sha, "tree": entries},
    )
    commit = run_gh_cli_compat(
        ["-X", "POST", pub.base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish video-derived articles 2026-09-09", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    run_gh_cli_compat(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
