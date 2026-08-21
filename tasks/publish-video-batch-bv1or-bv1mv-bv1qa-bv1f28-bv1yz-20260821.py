from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1zr-bv1y1-bv1yr-bv18y-20260821.py"
ASSET_ROOT = TASKS / "video-batch-20260821-bv1or-bv1mv-bv1qa-bv1f28-bv1yz"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1or-bv1mv-bv1qa-bv1f28-bv1yz-20260821-output")

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
pub.base.DATE = "2026-08-21"
pub.base.BASE_DT = datetime(2026, 8, 21, 15, 0, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/montage-technology-memory-interface-chip-valuation-safety-margin/"
pub.base.PREV_EXISTING_TITLE = "澜起科技投资价值分析：好生意、好公司，但价格才是关键"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1or-bv1mv-bv1qa-bv1f28-bv1yz-20260821-changed-files.json"
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
        slug="wuxi-three-brothers-apptec-biologics-xdc-cxo-map",
        title="药明三兄弟：药明康德、药明生物与药明合联的同源生意",
        desc="从李革创业、三家公司业务边界、CXO 卖水模式、政策风险和股权结构，拆解药明体系的一家买卖与三家生意。",
        category="投资研究",
        series="医药产业",
        tags=["药明康德", "药明生物", "药明合联", "CXO", "CDMO", "ADC", "创新药", "医药外包"],
        minutes=14,
        body=body("BV1oR8M6aEui"),
        accent=("#0f172a", "#0f766e", "#d97706"),
        required=["药明康德", "药明生物", "药明合联", "李革", "CXO", "ADC", "股权", "政策风险"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="ai-capex-boom-token-cost-application-roi-investment-framework",
        title="AI 一定会改变世界，但投资回报不能只看热度",
        desc="AI 是基础设施革命，也是一场资本开支竞赛。真正需要判断的是 token 成本、上游价值捕获、应用 ROI 和现金流纪律。",
        category="科技产业",
        series="AI投资",
        tags=["AI", "资本开支", "token", "云计算", "算力", "投资框架", "人工智能"],
        minutes=12,
        body=body("BV1mVgJ6hE1a"),
        accent=("#111827", "#dc2626", "#2563eb"),
        required=["AI", "8300 亿美元", "token", "硬件成本", "资本开支", "现金流", "上游"],
        minimum=3100,
    ),
    pub.base.Post(
        slug="goldman-ai-labor-market-impact-four-industries-entry-level-workers",
        title="AI 抢走工作了吗：冲击正在集中于四个行业和一类人",
        desc="AI 对就业的影响尚未全面体现在总量数据中，但呼叫中心、软件出版、管理咨询、广告服务和初级岗位已经先被改写。",
        category="宏观经济",
        series="AI就业",
        tags=["AI就业", "劳动力市场", "高盛", "初级岗位", "生成式AI", "机器人", "宏观经济"],
        minutes=12,
        body=body("BV1qa8N6QEp2"),
        accent=("#0f172a", "#16a34a", "#7c3aed"),
        required=["AI", "呼叫中心", "软件出版", "管理咨询", "广告服务", "初级岗位", "就业"],
        minimum=3100,
    ),
    pub.base.Post(
        slug="mrna-cancer-vaccine-phase-iii-domestic-supply-chain-repricing",
        title="mRNA 肿瘤疫苗 III 期成功之后：国内产业链重估逻辑",
        desc="mRNA 肿瘤疫苗验证的是平台化机会：AI 抗原设计、LNP 递送、核酸修饰、上游原料和个性化生产共同决定产业链价值。",
        category="投资研究",
        series="医药产业",
        tags=["mRNA", "肿瘤疫苗", "LNP", "康希诺", "云顶新耀", "创新药", "医药产业链"],
        minutes=12,
        body=body("BV1F28K6cEGS"),
        accent=("#111827", "#be123c", "#0891b2"),
        required=["mRNA", "肿瘤疫苗", "LNP", "AI 抗原设计", "康希诺", "云顶新耀", "产业链"],
        minimum=3000,
    ),
    pub.base.Post(
        slug="unitree-rare-earth-optimus-humanoid-robot-mass-production-race",
        title="宇树、稀土与擎天柱：人形机器人第一名到底看什么",
        desc="人形机器人竞争不能只看发布会。样机、量产、成本和具身智能，才是宇树、特斯拉和全球同行真正要跨过的四道门槛。",
        category="科技产业",
        series="机器人",
        tags=["宇树科技", "人形机器人", "稀土", "擎天柱", "具身智能", "供应链", "机器人"],
        minutes=15,
        body=body("BV1yz876eE84"),
        accent=("#0f172a", "#f97316", "#2563eb"),
        required=["宇树", "人形机器人", "稀土", "擎天柱", "量产", "成本", "具身智能"],
        minimum=3800,
    ),
]

pub.SCREENSHOT_SOURCES = {
    "wuxi-three-brothers-apptec-biologics-xdc-cxo-map": [
        (ASSET_ROOT / "BV1oR8M6aEui-article-images" / "final-02-shareholding-map.jpg", "01-shareholding-map.jpg"),
    ],
    "ai-capex-boom-token-cost-application-roi-investment-framework": [
        (ASSET_ROOT / "BV1mVgJ6hE1a-article-images" / "final-01-capex-scale.jpg", "01-capex-scale.jpg"),
        (ASSET_ROOT / "BV1mVgJ6hE1a-article-images" / "final-02-token-cost.jpg", "02-token-cost.jpg"),
    ],
    "goldman-ai-labor-market-impact-four-industries-entry-level-workers": [],
    "mrna-cancer-vaccine-phase-iii-domestic-supply-chain-repricing": [],
    "unitree-rare-earth-optimus-humanoid-robot-mass-production-race": [],
}


if __name__ == "__main__":
    pub.main()
