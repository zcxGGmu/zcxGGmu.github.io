from __future__ import annotations

import base64
import importlib.util
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1he-bv1gh-bv1xt-bv1s28-20260822.py"
ASSET_ROOT = TASKS / "video-batch-20260823-bv15k-bv15m-bv1dl"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv15k-bv15m-bv1dl-20260823-output")

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
pub.base.DATE = "2026-08-23"
pub.base.BASE_DT = datetime(2026, 8, 23, 14, 45, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/technology-revolutions-financial-bubbles-new-economic-paradigm/"
pub.base.PREV_EXISTING_TITLE = "技术革命、金融泡沫与经济新范式"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv15k-bv15m-bv1dl-20260823-changed-files.json"
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
        slug="skill-compound-return-language-self-investment",
        title="普通人最值得投的，是能长期复利的技能",
        desc="从语言学习、海外打工、销售沟通和成人职场表达出发，理解为什么真正值得长期投入的是能扩大选择权的技能。",
        category="个人成长",
        series="自我投资",
        tags=["自我投资", "语言学习", "英语", "技能复利", "职场表达", "学习方法", "个人成长"],
        minutes=13,
        body=body("BV15kBYB7Esf"),
        accent=("#111827", "#2563eb", "#16a34a"),
        required=["自我投资", "语言", "英语", "考试", "海外", "销售", "滞后", "真实场景", "输出", "反馈"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="lifespan-economics-time-allocation-life-experience",
        title="寿命经济学：活得更久，不等于人生更值",
        desc="寿命变长并不代表体验线性增加。时间配置、机会成本、健康寿命、延迟满足和回忆复利，共同决定人生如何更值。",
        category="生活方式",
        series="时间价值",
        tags=["寿命经济学", "时间配置", "机会成本", "延迟满足", "健康寿命", "人生体验", "生活方式"],
        minutes=14,
        body=body("BV15m8F6KEXN"),
        accent=("#111827", "#dc2626", "#f97316"),
        required=["寿命", "生命价值", "多巴胺", "体能", "加里·贝克尔", "时间配置", "机会成本", "延迟满足", "五十岁", "八十岁"],
        minimum=3900,
    ),
    pub.base.Post(
        slug="do-not-rush-house-car-marriage-child-young-people",
        title="买房、买车、结婚、生娃，都不要着急",
        desc="房价、汽车金融、婚育成本和就业压力都在变化。重大人生决策不是抢答题，普通人更需要现金流、安全垫和自己的节奏。",
        category="社会观察",
        series="年轻人选择",
        tags=["买房", "买车", "结婚", "生育", "青年就业", "现金流", "低负债", "社会观察"],
        minutes=11,
        body=body("BV1dL8K6HEm3"),
        accent=("#1f2937", "#0f766e", "#f59e0b"),
        required=["买房", "买车", "结婚", "孩子", "楼市", "租房", "月供", "现金流", "低负债", "不要着急"],
        minimum=3300,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "skill-compound-return-language-self-investment": [],
    "lifespan-economics-time-allocation-life-experience": [
        (ASSET_ROOT / "BV15m8F6KEXN-article-images" / "final-01-experience-capacity-curve.jpg", "01-experience-capacity-curve.jpg"),
        (ASSET_ROOT / "BV15m8F6KEXN-article-images" / "final-02-life-value-curve.jpg", "02-life-value-curve.jpg"),
    ],
    "do-not-rush-house-car-marriage-child-young-people": [],
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
            img = Image.open(image_path).convert("RGB")
            if img.width < 1200 or img.height < 650:
                raise RuntimeError(f"screenshot dimensions too small: {post.slug}/{dest}: {img.size}")
            if image_path.stat().st_size < 40_000:
                raise RuntimeError(f"screenshot file unexpectedly small: {post.slug}/{dest}")
            w, h = img.size
            edge_pixels = []
            for x in range(w):
                edge_pixels.extend([img.getpixel((x, 0)), img.getpixel((x, h - 1))])
            for y in range(h):
                edge_pixels.extend([img.getpixel((0, y)), img.getpixel((w - 1, y))])
            dark_edge = sum(1 for r, g, b in edge_pixels if r < 18 and g < 18 and b < 18)
            if dark_edge:
                raise RuntimeError(f"screenshot black-edge check failed: {post.slug}/{dest}: dark={dark_edge}")


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
        {"message": "Publish video-derived articles 2026-08-23", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
