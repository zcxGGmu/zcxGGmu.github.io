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
#      uv run publish-video-batch-bv1ku-bv14s-bv1nq-20260828.py
# 3. Or make executable and run:
#      chmod +x publish-video-batch-bv1ku-bv14s-bv1nq-20260828.py && ./publish-video-batch-bv1ku-bv14s-bv1nq-20260828.py
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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1pe-bv1ij-bv1eb-bv1ga-20260826.py"
ASSET_ROOT = TASKS / "video-batch-20260828-bv1ku-bv14s-bv1nq"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1ku-bv14s-bv1nq-20260828-output")

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
pub.base.DATE = "2026-08-28"
pub.base.BASE_DT = datetime(2026, 8, 28, 22, 30, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/awesome-gpt-image-2-532-cases-prompt-engineering/"
pub.base.PREV_EXISTING_TITLE = "awesome-gpt-image-2：532 个案例如何变成可复用的图像提示词系统"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1ku-bv14s-bv1nq-20260828-changed-files.json"
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
        slug="six-industries-ground-level-macro-micro-employment-advice",
        title="六个行业的真实体感：宏观下行、微观分化与就业选择",
        desc="从加油站、潮玩设计、美妆设计、文物保护、基础制造业和深圳酒店六个样本，看行业分化、现金流压力和普通人的职业安全感。",
        category="社会观察",
        series="行业体感",
        tags=["行业体感", "就业", "加油站", "潮玩", "美妆", "文物", "制造业", "酒店", "AI"],
        minutes=13,
        body=body("BV1kuhj6FEuS"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["加油站", "潮玩", "美妆", "文物", "制造业", "酒店", "AI", "就业", "现金流", "地方财政"],
        minimum=4200,
    ),
    pub.base.Post(
        slug="goldman-china-growth-engine-shift-long-term-risk",
        title="真正值得担心的不是短期放缓，而是中国增长动力正在改变",
        desc="围绕高盛对中国经济的判断，拆解国债收益率、钢铁价格、服务消费、企业还债压力、就业分项和政策传导效率。",
        category="宏观经济",
        series="中国经济",
        tags=["中国经济", "高盛", "内需", "通缩", "国债收益率", "服务消费", "民营企业", "供给侧"],
        minutes=11,
        body=body("BV14s8o67EyM"),
        accent=("#0f172a", "#0f766e", "#dc2626"),
        required=["高盛", "GDP", "国债收益率", "钢铁", "服务消费", "还本付息", "PMI", "供给侧", "内需", "通缩"],
        minimum=3300,
    ),
    pub.base.Post(
        slug="global-supply-chain-labor-complaints-germany-mexico-policy-shift",
        title="全球供应链新变量：劳工审查、德国联盟与墨西哥政策转向",
        desc="劳工举报、德国供应链卡点和墨西哥关税政策共同说明，全球贸易战正在从单一关税走向劳工、技术和区域联盟组合。",
        category="全球贸易",
        series="供应链重构",
        tags=["全球贸易", "供应链", "强迫劳动", "欧盟", "德国", "墨西哥", "关税", "半导体", "汽车"],
        minutes=12,
        body=body("BV1nQ4d6FEMn"),
        accent=("#172554", "#7c2d12", "#16a34a"),
        required=["强迫劳动", "欧盟", "德国", "墨西哥", "供应链", "关税", "半导体", "EUV", "汽车", "全球协作"],
        minimum=3800,
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
        {"message": "Publish video-derived articles 2026-08-28", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()

