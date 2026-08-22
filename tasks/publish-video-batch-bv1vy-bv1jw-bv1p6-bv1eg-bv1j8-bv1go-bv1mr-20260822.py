from __future__ import annotations

import base64
import importlib.util
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1zr-bv1y1-bv1yr-bv18y-20260821.py"
ASSET_ROOT = TASKS / "video-batch-20260822-bv1vy-bv1jw-bv1p6-bv1eg-bv1j8-bv1go-bv1mr"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1vy-bv1jw-bv1p6-bv1eg-bv1j8-bv1go-bv1mr-20260822-output")

spec = importlib.util.spec_from_file_location("previous_video_publisher", PREV_WRAPPER)
previous = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = previous
spec.loader.exec_module(previous)

pub = previous.pub


def body(bvid: str) -> str:
    return (DRAFTS / f"{bvid}-body.html").read_text(encoding="utf-8")


previous.OUT_DIR = OUT_DIR
pub.base.__file__ = __file__
pub.base.DATE = "2026-08-22"
pub.base.BASE_DT = datetime(2026, 8, 22, 16, 35, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/wuxi-three-brothers-apptec-biologics-xdc-cxo-map/"
pub.base.PREV_EXISTING_TITLE = "药明三兄弟：药明康德、药明生物与药明合联的同源生意"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1vy-bv1jw-bv1p6-bv1eg-bv1j8-bv1go-bv1mr-20260822-changed-files.json"
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
        slug="kangbo-cycle-depression-vs-recovery-institutional-debate",
        title="康波周期之辩：萧条期未尽，还是回升期开启",
        desc="从长波阶段、增长通胀、生产效率、AI 扩散、债务出清和地缘政治，判断当前仍更接近康波萧条期中后段。",
        category="宏观经济",
        series="康波周期",
        tags=["康波周期", "宏观经济", "AI", "通胀", "债务", "黄金", "地缘政治", "资产配置"],
        minutes=16,
        body=body("BV1vY8A6GETK"),
        accent=("#111827", "#d97706", "#2563eb"),
        required=["康波", "萧条期", "回升期", "AI", "通胀", "债务", "地缘政治", "黄金"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="tungsten-supply-demand-gap-price-center-resource-revaluation",
        title="钨供需缺口持续：价格中枢上移与资源重估逻辑",
        desc="钨价上涨不只是短期补库，海外增量不及预期、中国资源地位、军工与高端制造需求共同推动战略资源重估。",
        category="投资研究",
        series="资源品",
        tags=["钨", "资源品", "战略金属", "供需缺口", "军工", "高端制造", "价格中枢"],
        minutes=9,
        body=body("BV1jw8w6yEVV"),
        accent=("#0f172a", "#059669", "#22c55e"),
        required=["钨", "供需缺口", "价格中枢", "资源重估", "军工", "中国", "海外"],
        minimum=2300,
    ),
    pub.base.Post(
        slug="rockchip-aiot-chip-leader-or-design-service-company",
        title="瑞芯微：AIoT 芯片龙头，还是代工型设计公司",
        desc="围绕分红率、研发费用率、核心 IP、风险披露和机器人主控期权，拆解瑞芯微估值重估前必须兑现的条件。",
        category="投资研究",
        series="半导体",
        tags=["瑞芯微", "AIoT", "边缘AI", "芯片", "机器人", "研发费用", "分红", "估值"],
        minutes=10,
        body=body("BV1p6866AEDK"),
        accent=("#111827", "#b91c1c", "#f97316"),
        required=["瑞芯微", "AIoT", "分红", "研发", "护城河", "RK3588", "机器人", "估值"],
        minimum=2500,
    ),
    pub.base.Post(
        slug="zoomlion-diversification-cycle-stock-valuation-repricing",
        title="中联重科再分析：多元化转型难掩周期股本质",
        desc="装备制造平台叙事要靠分部数据、协同效应、毛利率、ROE 和现金流验证；在此之前，中联重科仍应按周期股定价。",
        category="投资研究",
        series="工程机械",
        tags=["中联重科", "工程机械", "周期股", "高空作业平台", "农机", "工业车辆", "分红", "估值"],
        minutes=8,
        body=body("BV1eG8B6CE8t"),
        accent=("#1f2937", "#dc2626", "#2563eb"),
        required=["中联重科", "周期股", "高空作业平台", "农机", "工业车辆", "分红", "ROE", "平台"],
        minimum=2100,
    ),
    pub.base.Post(
        slug="us-ai-double-bubble-internet-2000-subprime-2008",
        title="美国 AI 的双重泡沫：一边复刻互联网狂热，一边重演次贷逻辑",
        desc="AI 既有真实技术变革，也正在叠加高估值、巨额资本开支、GPU 抵押、信用担保和循环融资风险。",
        category="科技产业",
        series="AI投资",
        tags=["AI", "泡沫", "OpenAI", "CoreWeave", "NVIDIA", "数据中心", "GPU", "资本开支", "信用风险"],
        minutes=11,
        body=body("BV1J88E68Eks"),
        accent=("#0f172a", "#7c3aed", "#06b6d4"),
        required=["AI", "泡沫", "互联网", "次贷", "GPU", "数据中心", "资本开支", "信用"],
        minimum=2700,
    ),
    pub.base.Post(
        slug="investment-goal-first-why-before-what-to-buy",
        title="投资第五课：先回答为什么，再谈买什么",
        desc="投资目标决定本金底线、收益要求、期限长度、风险承受力、工具选择和交易纪律；没有目标，指标都会变成噪音。",
        category="投资方法",
        series="投资基础课",
        tags=["投资目标", "本金", "风险", "资产配置", "成长股", "红利资产", "投资纪律"],
        minutes=8,
        body=body("BV1GouM6zEdF"),
        accent=("#111827", "#1d4ed8", "#16a34a"),
        required=["投资目标", "本金", "期限", "风险", "工具", "纪律", "财富自由"],
        minimum=2200,
    ),
    pub.base.Post(
        slug="why-i-do-not-buy-active-funds-investor-protection",
        title="为什么不买主动基金：普通投资者需要先保护自己",
        desc="主动基金的根本问题是利益错位：投资者要净值增长，机构要规模和管理费，风格漂移、赎回压力和费用会侵蚀长期收益。",
        category="投资方法",
        series="基金投资",
        tags=["主动基金", "基金经理", "管理费", "规模陷阱", "风格漂移", "投资者保护", "长期投资"],
        minutes=10,
        body=body("BV1mRu16vEtN"),
        accent=("#172554", "#7f1d1d", "#f97316"),
        required=["主动基金", "基金经理", "管理费", "规模", "风格漂移", "赎回", "保护"],
        minimum=2600,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "kangbo-cycle-depression-vs-recovery-institutional-debate": [],
    "tungsten-supply-demand-gap-price-center-resource-revaluation": [
        (ASSET_ROOT / "BV1jw8w6yEVV-article-images" / "final-01-resource-revaluation.jpg", "01-resource-revaluation.jpg"),
    ],
    "rockchip-aiot-chip-leader-or-design-service-company": [
        (ASSET_ROOT / "BV1p6866AEDK-article-images" / "final-01-dividend-warning.jpg", "01-dividend-warning.jpg"),
        (ASSET_ROOT / "BV1p6866AEDK-article-images" / "final-02-catalyst-conditions.jpg", "02-catalyst-conditions.jpg"),
    ],
    "zoomlion-diversification-cycle-stock-valuation-repricing": [
        (ASSET_ROOT / "BV1eG8B6CE8t-article-images" / "final-01-cycle-narrative.jpg", "01-cycle-narrative.jpg"),
        (ASSET_ROOT / "BV1eG8B6CE8t-article-images" / "final-02-platform-premium-risk.jpg", "02-platform-premium-risk.jpg"),
    ],
    "us-ai-double-bubble-internet-2000-subprime-2008": [],
    "investment-goal-first-why-before-what-to-buy": [
        (ASSET_ROOT / "BV1GouM6zEdF-article-images" / "final-01-goal-risk-spectrum.jpg", "01-goal-risk-spectrum.jpg"),
        (ASSET_ROOT / "BV1GouM6zEdF-article-images" / "final-02-three-questions.jpg", "02-three-questions.jpg"),
    ],
    "why-i-do-not-buy-active-funds-investor-protection": [
        (ASSET_ROOT / "BV1mRu16vEtN-article-images" / "final-01-size-trap.jpg", "01-size-trap.jpg"),
        (ASSET_ROOT / "BV1mRu16vEtN-article-images" / "final-02-premium-takeover.jpg", "02-premium-takeover.jpg"),
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
            img = Image.open(image_path).convert("RGB")
            if img.width < 1000 or img.height < 450:
                raise RuntimeError(f"screenshot dimensions too small: {post.slug}/{dest}: {img.size}")
            if image_path.stat().st_size < 20_000:
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
        {"message": "Publish video-derived articles 2026-08-22", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.create_commit = create_commit
pub.render_asset_check = render_asset_check


if __name__ == "__main__":
    pub.main()
