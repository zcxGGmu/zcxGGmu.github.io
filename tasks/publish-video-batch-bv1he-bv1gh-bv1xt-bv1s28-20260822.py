from __future__ import annotations

import base64
import importlib.util
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1vy-bv1jw-bv1p6-bv1eg-bv1j8-bv1go-bv1mr-20260822.py"
ASSET_ROOT = TASKS / "video-batch-20260822-bv1he-bv1gh-bv1xt-bv1s28"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1he-bv1gh-bv1xt-bv1s28-20260822-output")

spec = importlib.util.spec_from_file_location("previous_video_publisher", PREV_WRAPPER)
previous = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = previous
spec.loader.exec_module(previous)

pub = previous.pub


def body(bvid: str) -> str:
    return (DRAFTS / f"{bvid}-body.html").read_text(encoding="utf-8")


previous.OUT_DIR = OUT_DIR
if hasattr(previous, "previous"):
    previous.previous.OUT_DIR = OUT_DIR
pub.base.__file__ = __file__
pub.base.DATE = "2026-08-22"
pub.base.BASE_DT = datetime(2026, 8, 22, 19, 20, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/kangbo-cycle-depression-vs-recovery-institutional-debate/"
pub.base.PREV_EXISTING_TITLE = "康波周期之辩：萧条期未尽，还是回升期开启"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1he-bv1gh-bv1xt-bv1s28-20260822-changed-files.json"
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
        slug="technology-revolutions-financial-bubbles-new-economic-paradigm",
        title="技术革命、金融泡沫与经济新范式",
        desc="从运河、铁路、电力、汽车、互联网到 AI，拆解技术革命如何催化金融泡沫，并推动生产模式、分配关系和制度框架重构。",
        category="宏观经济",
        series="技术革命",
        tags=["技术革命", "金融泡沫", "AI", "生产率", "制度变革", "分配", "经济范式"],
        minutes=12,
        body=body("BV1he8y6XEkS"),
        accent=("#111827", "#f59e0b", "#2563eb"),
        required=["技术革命", "金融泡沫", "AI", "生产率", "分配", "制度", "循环融资", "基础设施"],
        minimum=3800,
    ),
    pub.base.Post(
        slug="us-treasury-long-bond-buybacks-curve-distortion-next-stage",
        title="长债回购加量、利率曲线扭曲与美债下一阶段",
        desc="短端交易降息，长端交易期限溢价、政策不确定性、通胀尾部风险和 AI 流动性虹吸；财政部长债回购加量改变了曲线定价。",
        category="宏观经济",
        series="美元体系",
        tags=["美债", "长债回购", "利率曲线", "期限溢价", "美联储", "财政部", "AI", "通胀"],
        minutes=10,
        body=body("BV1Gh8y6REeZ"),
        accent=("#0f172a", "#2563eb", "#14b8a6"),
        required=["美债", "长端", "期限溢价", "财政部", "回购", "通胀", "AI", "流动性"],
        minimum=3400,
    ),
    pub.base.Post(
        slug="beijing-stock-exchange-four-board-structure-niche-champions-valuation-repair",
        title="北交所再认知：四板块格局下，细分赛道冠军从估值洼地走向定价修复",
        desc="主板、科创板、创业板和北交所错位互补；专精特新、小巨人、单项冠军、流动性改善和机构配置共同推动北交所重估。",
        category="投资研究",
        series="资本市场",
        tags=["北交所", "专精特新", "单项冠军", "新三板", "科创板", "创业板", "估值修复", "机构配置"],
        minutes=13,
        body=body("BV1XT8u6WEwo"),
        accent=("#172554", "#dc2626", "#f97316"),
        required=["北交所", "主板", "科创板", "创业板", "专精特新", "单项冠军", "估值修复", "新三板"],
        minimum=4300,
    ),
    pub.base.Post(
        slug="unigroup-guoxin-micro-special-ic-fpga-smart-security-valuation",
        title="紫光国微：特种集成电路、FPGA 与智能安全芯片的再定价",
        desc="从现金流、研发投入、特种集成电路、FPGA、高安全芯片、eSIM、汽车电子、功率器件和 AI 算力布局，理解紫光国微估值修复条件。",
        category="投资研究",
        series="半导体",
        tags=["紫光国微", "特种集成电路", "FPGA", "智能安全芯片", "eSIM", "汽车电子", "功率器件", "估值"],
        minutes=16,
        body=body("BV1S28N63ExP"),
        accent=("#111827", "#7c3aed", "#0ea5e9"),
        required=["紫光国微", "特种集成电路", "FPGA", "智能安全芯片", "eSIM", "汽车电子", "毛利率", "估值"],
        minimum=5000,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "technology-revolutions-financial-bubbles-new-economic-paradigm": [],
    "us-treasury-long-bond-buybacks-curve-distortion-next-stage": [],
    "beijing-stock-exchange-four-board-structure-niche-champions-valuation-repair": [],
    "unigroup-guoxin-micro-special-ic-fpga-smart-security-valuation": [],
}


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
        {"message": "Publish video-derived articles 2026-08-22", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
