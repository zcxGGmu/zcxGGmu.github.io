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
#      uv run publish-video-batch-bv1pe-bv1ij-bv1eb-bv1ga-20260826.py
# 3. Or make executable and run:
#      chmod +x publish-video-batch-bv1pe-bv1ij-bv1eb-bv1ga-20260826.py && ./publish-video-batch-bv1pe-bv1ij-bv1eb-bv1ga-20260826.py
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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1g58-bv11t-bv1bf-bv1mphetm-bv1mphekk-bv18i-bv1qn-bv1aj-20260824.py"
ASSET_ROOT = TASKS / "video-batch-20260826-bv1pe-bv1ij-bv1eb-bv1ga"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1pe-bv1ij-bv1eb-bv1ga-20260826-output")

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
pub.base.DATE = "2026-08-26"
pub.base.BASE_DT = datetime(2026, 8, 26, 21, 30, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/technology-resources-dividend-opportunities-market-strategy/"
pub.base.PREV_EXISTING_TITLE = "科技、资源与红利机会：当前位置的市场策略框架"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1pe-bv1ij-bv1eb-bv1ga-20260826-changed-files.json"
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
        slug="youth-national-optimism-personal-pessimism-structural-framework",
        title="青年的国家乐观与个人悲观：从宏观叙事到个人处境",
        desc="用《国家与革命》中的国家、阶级、分配和折衷主义框架，解释为什么宏观上升与个人挤压会同时出现。",
        category="社会观察",
        series="青年处境",
        tags=["青年", "国家乐观", "个人悲观", "国家与革命", "列宁", "阶级", "劳动者", "分配结构"],
        minutes=11,
        body=body("BV1pE3c6uEB7"),
        accent=("#111827", "#dc2626", "#2563eb"),
        required=["国家", "乐观", "悲观", "列宁", "恩格斯", "国家与革命", "阶级", "国家机器", "劳动者", "分配"],
        minimum=3000,
    ),
    pub.base.Post(
        slug="productivity-improved-why-working-hours-do-not-fall",
        title="生产力大幅提升，为什么工作时长降不下来",
        desc="从生产资料归属、市场竞争、AI 军备竞赛和个人商业闭环出发，解释技术红利为什么不会自动变成闲暇。",
        category="社会观察",
        series="工作与生产力",
        tags=["生产力", "工作时长", "AI", "生产资料", "市场竞争", "长工时", "个人商业闭环", "时间自由"],
        minutes=10,
        body=body("BV1iJhN6XE8s"),
        accent=("#0f172a", "#2563eb", "#16a34a"),
        required=["生产力", "工作时长", "凯恩斯", "生产资料", "技术红利", "竞争", "AI", "时间决定权", "商业闭环"],
        minimum=3000,
    ),
    pub.base.Post(
        slug="why-chinese-people-are-so-tired-working-hours-consumption-share",
        title="中国人为什么这么累：工作时间、消费占比与内需困境",
        desc="从亨利·福特五天工作制、居民消费率、美国工时史和中国长工时结构，理解扩大内需为什么离不开收入与闲暇。",
        category="宏观经济",
        series="内需与劳动",
        tags=["内需", "工作时间", "居民消费率", "亨利福特", "五天工作制", "996", "消费占比", "劳动权益"],
        minutes=12,
        body=body("BV1EBhK68ERD"),
        accent=("#111827", "#0f766e", "#f97316"),
        required=["内需", "消费", "亨利·福特", "工作时间", "五天工作制", "居民消费", "996", "大萧条", "劳动者", "闲暇"],
        minimum=3200,
    ),
    pub.base.Post(
        slug="how-much-tax-do-chinese-people-pay-fiscal-resource-structure",
        title="中国人到底交了多少税：从 12.6% 到接近三成的资源账本",
        desc="把税收、公共预算、社保、土地出让金和国有资本放进同一张资源账本，理解普通人的真实负担感来自哪里。",
        category="宏观经济",
        series="财政结构",
        tags=["税收", "财政", "社保", "土地财政", "国有资本", "居民收入", "增值税", "GDP分配"],
        minutes=13,
        body=body("BV1GAhV6qEba"),
        accent=("#0f172a", "#dc2626", "#f59e0b"),
        required=["税收", "GDP", "增值税", "公共预算", "社保", "土地出让金", "国有资本", "居民", "工资", "资源"],
        minimum=3600,
    ),
]

pub.SCREENSHOT_SOURCES = {post.slug: [] for post in pub.base.POSTS}


def render_asset_check() -> None:
    for post in pub.base.POSTS:
        svg = OUT_DIR / f"images/posts/{post.slug}/cover.svg"
        png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(
            ["sips", "-s", "format", "png", str(svg), "--out", str(png)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
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
        blob = pub.base.run_gh(["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
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
        {"message": "Publish video-derived articles 2026-08-26", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
