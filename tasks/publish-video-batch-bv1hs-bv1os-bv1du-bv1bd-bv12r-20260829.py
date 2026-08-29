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
#      uv run publish-video-batch-bv1hs-bv1os-bv1du-bv1bd-bv12r-20260829.py
# 3. Or make executable and run:
#      chmod +x publish-video-batch-bv1hs-bv1os-bv1du-bv1bd-bv12r-20260829.py && ./publish-video-batch-bv1hs-bv1os-bv1du-bv1bd-bv12r-20260829.py
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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1ku-bv14s-bv1nq-20260828.py"
ASSET_ROOT = TASKS / "video-batch-20260829-bv1hs-bv1os-bv1du-bv1bd-bv12r"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1hs-bv1os-bv1du-bv1bd-bv12r-20260829-output")

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
pub.base.DATE = "2026-08-29"
pub.base.BASE_DT = datetime(2026, 8, 29, 22, 30, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/six-industries-ground-level-macro-micro-employment-advice/"
pub.base.PREV_EXISTING_TITLE = "六个行业的真实体感：宏观下行、微观分化与就业选择"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1hs-bv1os-bv1du-bv1bd-bv12r-20260829-changed-files.json"
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
        slug="memory-interconnect-chip-market-position",
        title="澜起科技2026中报深度分析：高速互联芯片、护城河与成长风险",
        desc="从高速互联芯片的产业链位置、DDR5 市场格局、AI 服务器信号需求和轻资产财务结构出发，拆解澜起科技的增长曲线与风险边界。",
        category="投资研究",
        series="半导体",
        tags=["澜起科技", "高速互联芯片", "内存接口", "DDR5", "AI服务器", "半导体", "护城河", "中报"],
        minutes=7,
        body=body("BV1Hs4C6FEfq"),
        accent=("#111827", "#2563eb", "#14b8a6"),
        required=["澜起科技", "高速互联芯片", "DDR5", "JEDEC", "AI服务器", "毛利率", "现金流", "客户集中"],
        minimum=3100,
    ),
    pub.base.Post(
        slug="liquid-cooling-core-companies",
        title="液冷三强对比：英维克、同飞股份与申菱环境谁更值得跟踪",
        desc="比较英维克、同飞股份与申菱环境的液冷切入方式、客户结构、订单兑现、盈利质量和出海能力，建立确定性、稳健性与弹性的跟踪框架。",
        category="投资研究",
        series="算力基础设施",
        tags=["液冷", "英维克", "同飞股份", "申菱环境", "数据中心", "CDU", "算力", "出海"],
        minutes=7,
        body=body("BV1oShg6qEUH"),
        accent=("#0f172a", "#0f766e", "#f97316"),
        required=["液冷", "英维克", "同飞股份", "申菱环境", "CDU", "数据中心", "合同负债", "海外"],
        minimum=3000,
    ),
    pub.base.Post(
        slug="abf-substrate-three-companies",
        title="ABF载板三强对比：深南电路、兴森科技与华正新材",
        desc="围绕 FCBGA 载板、ABF 材料、客户认证、产能爬坡和资本开支，比较深南电路、兴森科技与华正新材的确定性、拐点和弹性。",
        category="投资研究",
        series="半导体封装",
        tags=["ABF载板", "深南电路", "兴森科技", "华正新材", "FCBGA", "封装基板", "国产替代", "PCB"],
        minutes=6,
        body=body("BV1du8m6iEho"),
        accent=("#111827", "#1d4ed8", "#7c3aed"),
        required=["ABF载板", "深南电路", "兴森科技", "华正新材", "FCBGA", "客户认证", "产能", "国产替代"],
        minimum=2800,
    ),
    pub.base.Post(
        slug="small-metals-three-companies",
        title="小金属低估值高增长对比：翔鹭钨业、中矿资源与兴业银锡",
        desc="从钨、锂、锡、银的供需周期、资源品位、成本曲线和资产负债表出发，比较三家小金属公司的盈利弹性、护城河与估值风险。",
        category="投资研究",
        series="资源周期",
        tags=["小金属", "翔鹭钨业", "中矿资源", "兴业银锡", "钨", "锂", "锡", "银", "资源股"],
        minutes=5,
        body=body("BV1Bd8J6hELY"),
        accent=("#1f2937", "#b45309", "#0f766e"),
        required=["翔鹭钨业", "中矿资源", "兴业银锡", "钨", "锂", "锡", "毛利率", "资源储量"],
        minimum=2600,
    ),
    pub.base.Post(
        slug="shenghong-technology",
        title="胜宏科技半年报：AI算力PCB龙头的订单、产能与利润修复",
        desc="从半年报利润质量、人工与折旧、存货结构、AI 服务器 PCB 升级、订单能见度和高端电镀线瓶颈，判断胜宏科技的扩产兑现路径。",
        category="投资研究",
        series="AI算力产业链",
        tags=["胜宏科技", "AI算力", "PCB", "高端多层板", "MSAP", "产能扩张", "订单", "毛利率"],
        minutes=7,
        body=body("BV12RtP6FEZi"),
        accent=("#0f172a", "#0891b2", "#14b8a6"),
        required=["胜宏科技", "AI算力", "PCB", "MSAP", "订单", "产能", "毛利率", "2027 年"],
        minimum=3300,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "memory-interconnect-chip-market-position": [
        (ASSET_ROOT / "article-images" / "BV1Hs4C6FEfq-56.jpg", "01-business-position.jpg"),
        (ASSET_ROOT / "article-images" / "BV1Hs4C6FEfq-140.jpg", "02-global-share.jpg"),
    ],
    "liquid-cooling-core-companies": [
        (ASSET_ROOT / "article-images" / "BV1oShg6qEUH-56-clean.jpg", "01-company-profiles.jpg"),
        (ASSET_ROOT / "article-images" / "BV1oShg6qEUH-168-clean.jpg", "02-leading-indicators.jpg"),
    ],
    "abf-substrate-three-companies": [
        (ASSET_ROOT / "article-images" / "BV1du8m6iEho-56.jpg", "02-company-profiles.jpg"),
        (ASSET_ROOT / "article-images" / "BV1du8m6iEho-140.jpg", "01-business-model.jpg"),
    ],
    "small-metals-three-companies": [
        (ASSET_ROOT / "article-images" / "BV1Bd8J6hELY-56.jpg", "01-company-profiles.jpg"),
        (ASSET_ROOT / "article-images" / "BV1Bd8J6hELY-140.jpg", "02-growth-comparison.jpg"),
    ],
    "shenghong-technology": [
        (ASSET_ROOT / "article-images" / "BV12RtP6FEZi-56-clean3.jpg", "01-half-year-overview.jpg"),
        (ASSET_ROOT / "article-images" / "BV12RtP6FEZi-140-clean3.jpg", "02-growth-drivers.jpg"),
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
            "message": "Publish video-derived articles 2026-08-29",
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
