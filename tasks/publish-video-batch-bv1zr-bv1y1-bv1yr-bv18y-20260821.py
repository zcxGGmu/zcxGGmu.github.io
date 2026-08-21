from __future__ import annotations

import base64
import importlib.util
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PUB_SCRIPT = TASKS / "publish-video-batch-bv1ut-bv1ee-bv1fx-20260816.py"
ASSET_ROOT = TASKS / "video-batch-20260821-bv1zr-bv1y1-bv1yr-bv18y"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1zr-bv1y1-bv1yr-bv18y-20260821-output")

spec = importlib.util.spec_from_file_location("video_publisher_base", PUB_SCRIPT)
pub = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = pub
spec.loader.exec_module(pub)

_run_gh = pub.base.run_gh


def run_gh_with_retry(args: list[str], payload: dict | None = None):
    for attempt in range(6):
        try:
            return _run_gh(args, payload)
        except RuntimeError as exc:
            msg = str(exc).lower()
            retryable = [
                "504",
                "502",
                "503",
                "respond to your request in time",
                "bad gateway",
                "service unavailable",
                "timeout",
                "timed out",
                "stream error",
                "connection",
                "reset",
                "temporarily",
                "can't assign requested address",
            ]
            if attempt < 5 and any(token in msg for token in retryable):
                time.sleep(2 + attempt * 3)
                continue
            raise


def body(bvid: str) -> str:
    return (DRAFTS / f"{bvid}-body.html").read_text(encoding="utf-8")


pub.base.run_gh = run_gh_with_retry
pub.base.__file__ = __file__
pub.base.DATE = "2026-08-21"
pub.base.BASE_DT = datetime(2026, 8, 21, 11, 45, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/semantica-accountable-ai-context-decision-provenance/"
pub.base.PREV_EXISTING_TITLE = "Semantica：为 AI 决策建立可追溯的上下文与证据图谱"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1zr-bv1y1-bv1yr-bv18y-20260821-changed-files.json"
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
        slug="montage-technology-memory-interface-chip-valuation-safety-margin",
        title="澜起科技投资价值分析：好生意、好公司，但价格才是关键",
        desc="从内存接口芯片寡头格局、Fabless 现金流、JEDEC 标准制定权、DDR5 与 AI 服务器需求，重新计算澜起科技的估值安全边际。",
        category="投资研究",
        series="半导体",
        tags=["澜起科技", "内存接口芯片", "DDR5", "AI服务器", "芯片", "估值", "自由现金流"],
        minutes=12,
        body=body("BV1zRGc6iE7Y"),
        accent=("#0f172a", "#2563eb", "#f97316"),
        required=["澜起科技", "内存接口芯片", "Fabless", "JEDEC", "DDR5", "自由现金流", "80 到 100 元", "100 倍"],
        minimum=4200,
    ),
    pub.base.Post(
        slug="bank-of-ningbo-quality-bank-low-valuation-risk-analysis",
        title="宁波银行投资价值分析：好公司、好生意与低估值背后的风险",
        desc="围绕资产质量、拨备覆盖率、ROE、净息差、个人贷款风险和资本充足率，拆解宁波银行低估值的机会与约束。",
        category="投资研究",
        series="银行业",
        tags=["宁波银行", "银行股", "城商行", "不良率", "拨备覆盖率", "ROE", "估值"],
        minutes=12,
        body=body("BV1Y1GF6REYq"),
        accent=("#111827", "#0f766e", "#ef4444"),
        required=["宁波银行", "不良率", "拨备覆盖率", "ROE", "净息差", "个人贷款", "资本充足率", "7 倍"],
        minimum=4000,
    ),
    pub.base.Post(
        slug="us-debt-40-trillion-fiscal-interest-rate-endgame",
        title="美债逼近40万亿之后：利息、赤字与美元体系的下一步",
        desc="从美债收益率、利息支出、日元套息交易、财政节流、关税开源、私人资本扩张与国家资产端，理解美国债务困局。",
        category="宏观经济",
        series="美元体系",
        tags=["美债", "美国财政", "美元体系", "利率", "赤字", "日元", "全球宏观"],
        minutes=10,
        body=body("BV1Yr8j65ExQ"),
        accent=("#1f2937", "#4f46e5", "#f59e0b"),
        required=["美债", "40 万亿美元", "利息支出", "赤字", "日元", "私人资本", "美元体系"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="population-decline-real-estate-long-cycle-demand-turning-point",
        title="人口减少之后，中国房地产的大麻烦才刚开始",
        desc="房地产长期看人口。年轻人口、婚姻、居民贷款、继承房、老龄化和高层住宅维护，共同决定下一阶段房价分化。",
        category="房地产",
        series="人口结构",
        tags=["房地产", "人口减少", "老龄化", "城市化", "房价", "土地财政", "存量房"],
        minutes=11,
        body=body("BV18Ybf6dEXt"),
        accent=("#0f172a", "#be123c", "#f97316"),
        required=["人口减少", "房地产", "城市化", "老龄化", "继承房", "高层住宅", "土地财政", "长期分化"],
        minimum=3400,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "montage-technology-memory-interface-chip-valuation-safety-margin": [
        (ASSET_ROOT / "BV1zRGc6iE7Y-article-images" / "01-global-oligopoly.jpg", "01-global-oligopoly.jpg"),
        (ASSET_ROOT / "BV1zRGc6iE7Y-article-images" / "02-valuation-framework.jpg", "02-valuation-framework.jpg"),
    ],
    "bank-of-ningbo-quality-bank-low-valuation-risk-analysis": [
        (ASSET_ROOT / "BV1Y1GF6REYq-article-images" / "01-asset-quality.jpg", "01-asset-quality.jpg"),
        (ASSET_ROOT / "BV1Y1GF6REYq-article-images" / "02-peer-valuation.jpg", "02-peer-valuation.jpg"),
    ],
    "us-debt-40-trillion-fiscal-interest-rate-endgame": [],
    "population-decline-real-estate-long-cycle-demand-turning-point": [],
}


def write_outputs(outputs: dict[str, str | None], binary_outputs: dict[str, bytes]) -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        if content is None:
            continue
        path = OUT_DIR / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for rel, content in binary_outputs.items():
        path = OUT_DIR / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(
        json.dumps(
            {
                "local_output": str(OUT_DIR),
                "text_files": len([v for v in outputs.values() if v is not None]),
                "binary_files": len(binary_outputs),
                "deleted": len([v for v in outputs.values() if v is None]),
                "urls": [post.full_url for post in pub.base.POSTS],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def render_asset_check() -> None:
    from PIL import Image

    for post in pub.base.POSTS:
        svg = OUT_DIR / f"images/posts/{post.slug}/cover.svg"
        png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(svg), "--out", str(png)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe or png.stat().st_size < 4096:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            image_path = OUT_DIR / f"images/posts/{post.slug}/{dest}"
            img = Image.open(image_path).convert("RGB")
            if img.width < 1200 or img.height < 460:
                raise RuntimeError(f"screenshot dimensions too small: {post.slug}/{dest}: {img.size}")
            if image_path.stat().st_size < 16_000:
                raise RuntimeError(f"screenshot file unexpectedly small: {post.slug}/{dest}")
            w, h = img.size
            edge_pixels = []
            for x in range(w):
                edge_pixels.extend([img.getpixel((x, 0)), img.getpixel((x, h - 1))])
            for y in range(h):
                edge_pixels.extend([img.getpixel((0, y)), img.getpixel((w - 1, y))])
            dark_edge = sum(1 for r, g, b in edge_pixels if r < 18 and g < 18 and b < 18)
            lower = img.crop((0, int(h * 0.82), w, h))
            lower_red = sum(1 for r, g, b in lower.getdata() if r > 190 and g < 120 and b < 120)
            lower_yellow = sum(1 for r, g, b in lower.getdata() if r > 200 and g > 160 and b < 80)
            if dark_edge or lower_red or lower_yellow:
                raise RuntimeError(f"screenshot cleanliness check failed: {post.slug}/{dest}: dark={dark_edge}, red={lower_red}, yellow={lower_yellow}")


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
        {"message": "Publish video-derived articles 2026-08-21", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.write_outputs = write_outputs
pub.render_asset_check = render_asset_check
pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()

