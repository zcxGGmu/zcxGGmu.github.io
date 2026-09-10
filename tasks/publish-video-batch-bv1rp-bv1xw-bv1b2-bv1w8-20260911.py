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
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1ef-bv152-bv184-bv1nm-bv1ed-bv1co-bv1a4-20260909.py"
ASSET_ROOT = TASKS / "video-batch-20260911-bv1rp-bv1xw-bv1b2-bv1w8"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
POST_MANIFEST = DRAFTS / "20260911-video-batch-bv1rp-bv1xw-bv1b2-bv1w8-posts.json"
OUT_DIR = Path("/tmp/video-batch-bv1rp-bv1xw-bv1b2-bv1w8-20260911-output")

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
pub.base.DATE = "2026-09-11"
pub.base.BASE_DT = datetime(2026, 9, 11, 23, 59, 50, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/ecc-engineering-workflow-coding-agent/"
pub.base.PREV_EXISTING_TITLE = "ECC 深度拆解：把编码 Agent 变成可治理的工程流程"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1rp-bv1xw-bv1b2-bv1w8-20260911-changed-files.json"
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


GITHUB_TOKEN: str | None = None


def github_token() -> str:
    global GITHUB_TOKEN
    if GITHUB_TOKEN is None:
        result = subprocess.run(["gh", "auth", "token"], check=True, capture_output=True, text=True)
        GITHUB_TOKEN = result.stdout.strip()
        if not GITHUB_TOKEN:
            raise RuntimeError("GitHub token is empty")
    return GITHUB_TOKEN


def api_json(method: str, endpoint: str, payload: dict | None = None) -> dict:
    url = f"https://api.github.com/{endpoint}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token()}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "codex-publisher/2026-09-11",
    }
    retryable = {408, 409, 429, 500, 502, 503, 504}
    for attempt in range(6):
        try:
            response = requests.request(method, url, headers=headers, json=payload, timeout=(10, 180))
        except requests.RequestException as exc:
            if attempt < 5:
                time.sleep(2 + attempt * 3)
                continue
            raise RuntimeError(f"GitHub API request failed after retries: {method} {endpoint}: {exc}") from exc
        if response.status_code < 400:
            return response.json() if response.content else {}
        if attempt < 5 and response.status_code in retryable:
            time.sleep(2 + attempt * 3)
            continue
        raise RuntimeError(f"GitHub API {method} {endpoint} failed: {response.status_code} {response.text[:500]}")


def run_gh_requests_compat(args: list[str], payload: dict | None = None):
    filtered = [arg for arg in args if arg not in {"--input", "-"}]
    if len(filtered) >= 3 and filtered[0] == "-X":
        return api_json(filtered[1], filtered[2], payload)
    if len(filtered) == 1:
        return api_json("GET", filtered[0], payload)
    raise RuntimeError(f"Unsupported gh compatibility args: {args}")


pub.base.run_gh = run_gh_requests_compat


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = api_json(
            "POST",
            pub.base.endpoint("git/blobs"),
            {"content": base64.b64encode(content.encode("utf-8")).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    for path, content in sorted(binary_outputs.items()):
        blob = api_json(
            "POST",
            pub.base.endpoint("git/blobs"),
            {"content": base64.b64encode(content).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = api_json("POST", pub.base.endpoint("git/trees"), {"base_tree": ref.tree_sha, "tree": entries})
    commit = api_json(
        "POST",
        pub.base.endpoint("git/commits"),
        {"message": "Publish video-derived articles 2026-09-11 batch 1", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    api_json(
        "PATCH",
        pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"),
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
