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
#      uv run publish-video-batch-bv1tq-bv1d1-bv1mht-bv1yc-20260829.py
# 3. Or make executable and run:
#      chmod +x publish-video-batch-bv1tq-bv1d1-bv1mht-bv1yc-20260829.py && ./publish-video-batch-bv1tq-bv1d1-bv1mht-bv1yc-20260829.py
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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1hs-bv1os-bv1du-bv1bd-bv12r-20260829.py"
ASSET_ROOT = TASKS / "video-batch-20260829-bv1tq-bv1d1-bv1mht-bv1yc"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1tq-bv1d1-bv1mht-bv1yc-20260829-output")

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
pub.base.PREV_EXISTING_URL = "/2026/memory-interconnect-chip-market-position/"
pub.base.PREV_EXISTING_TITLE = "澜起科技2026中报深度分析：高速互联芯片、护城河与成长风险"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1tq-bv1d1-bv1mht-bv1yc-20260829-changed-files.json"
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
        slug="kangbo-wealth-cycle-boundary",
        title="康波不是财富密码：周期、位置与普通人的投资边界",
        desc="从周金涛和康德拉季耶夫长波谈起，拆解周期理论如何解释经济波动、产业分化与资产回报，也说明普通投资者为什么不能拿长周期替高杠杆背书。",
        category="投资研究",
        series="周期认知",
        tags=["康波", "周金涛", "康德拉季耶夫", "房地产周期", "资产配置", "AI", "周期投资"],
        minutes=17,
        body=body("BV1tq426mEMG"),
        accent=("#0f172a", "#0f766e", "#b45309"),
        required=["康波", "周金涛", "房地产周期", "固定资产投资周期", "库存周期", "资产配置", "AI", "周期"],
        minimum=3200,
    ),
    pub.base.Post(
        slug="kingboard-ai-ccl-repricing",
        title="建滔积层板的AI重估：覆铜板、资本开支与利润弹性",
        desc="花旗调研显示，建滔集团正把资本开支更多投向 AI 相关玻纤、覆铜板和铜箔产能，利润、分红和估值都在重新定价。",
        category="投资研究",
        series="AI算力材料",
        tags=["建滔集团", "建滔积层板", "CCL", "覆铜板", "玻纤", "资本开支", "分红", "估值"],
        minutes=18,
        body=body("BV1D1hw6uEw5"),
        accent=("#111827", "#2563eb", "#f59e0b"),
        required=["建滔集团", "建滔积层板", "AI", "CCL", "玻纤", "覆铜板", "资本开支", "分红", "估值", "风险"],
        minimum=3000,
    ),
    pub.base.Post(
        slug="semiconductor-equipment-power-grid",
        title="半导体设备的天花板不是芯片，而是电力",
        desc="摩根士丹利把 2026/2027 年 WFE 支出预期大幅上调，行业真正的上限正在从光刻机转向电网、能源和数据中心负荷。",
        category="投资研究",
        series="半导体设备",
        tags=["半导体设备", "WFE", "2nm", "DRAM", "HBM", "NAND", "台积电", "英特尔", "电力"],
        minutes=23,
        body=body("BV1MhtN6vEyp"),
        accent=("#0f172a", "#7c3aed", "#0891b2"),
        required=["半导体设备", "WFE", "2nm", "DRAM", "HBM", "NAND", "台积电", "英特尔", "电力", "数据中心"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="hawkish-theater-debt-inflation-market",
        title="鹰派表演挡不住债务：通胀、美元与金银的真实反应",
        desc="沃什的鹰派演讲推高了金银波动和美元，但真正没有被正面回答的仍然是 40 万亿债务、贸易摩擦和高杠杆周期的后果。",
        category="宏观经济",
        series="美元与通胀",
        tags=["美联储", "沃什", "通胀", "黄金", "白银", "美元", "AI失业", "West Marine", "关税", "债务"],
        minutes=27,
        body=body("BV1yC426CERZ"),
        accent=("#111827", "#b91c1c", "#ca8a04"),
        required=["美联储", "沃什", "40 万亿美元", "通胀", "黄金", "白银", "美元", "关税", "AI", "West Marine"],
        minimum=4300,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "kangbo-wealth-cycle-boundary": [
        (ASSET_ROOT / "article-images" / "BV1tq426mEMG-120-clean-large.jpg", "01-nested-cycles.jpg"),
        (ASSET_ROOT / "article-images" / "BV1tq426mEMG-240-clean-large.jpg", "02-strategic-positioning.jpg"),
        (ASSET_ROOT / "article-images" / "BV1tq426mEMG-480-clean-large.jpg", "03-cycle-resonance-table.jpg"),
        (ASSET_ROOT / "article-images" / "BV1tq426mEMG-600-clean-large.jpg", "04-recession-structure.jpg"),
        (ASSET_ROOT / "article-images" / "BV1tq426mEMG-960-clean-large.jpg", "05-cycle-landing.jpg"),
    ],
    "kingboard-ai-ccl-repricing": [],
    "semiconductor-equipment-power-grid": [],
    "hawkish-theater-debt-inflation-market": [],
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
        {"message": "Publish video-derived articles 2026-08-29", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
