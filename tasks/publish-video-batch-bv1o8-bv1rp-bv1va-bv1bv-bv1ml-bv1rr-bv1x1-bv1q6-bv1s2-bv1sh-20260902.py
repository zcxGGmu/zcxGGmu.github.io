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
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1bet-bv1n5t-bv1clt-bv1let-bv1uft-bv1bvt-bv1mlt-20260901.py"
ASSET_ROOT = TASKS / "video-batch-20260902-bv1o8-bv1rp-bv1va-bv1bv-bv1ml-bv1rr-bv1x1-bv1q6-bv1s2-bv1sh"
NEW_CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
OLD_CHART_ROOT = TASKS / "video-batch-20260901-bv1bet-bv1n5t-bv1clt-bv1let-bv1uft-bv1bvt-bv1mlt" / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1o8-bv1rp-bv1va-bv1bv-bv1ml-bv1rr-bv1x1-bv1q6-bv1s2-bv1sh-20260902-output")

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
pub.base.DATE = "2026-09-02"
pub.base.BASE_DT = datetime(2026, 9, 2, 23, 50, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/ai-side-hustle-feishu-bitable-template-enterprise-system/"
pub.base.PREV_EXISTING_TITLE = "AI副业观察: 从飞书多维表格模板到企业智能化系统定制"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1o8-bv1rp-bv1va-bv1bv-bv1ml-bv1rr-bv1x1-bv1q6-bv1s2-bv1sh-20260902-changed-files.json"
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
        slug="dram-hbm-2027-price-upgrade-ai-memory-cycle",
        title="DRAM 积极信号频出：2027 年 HBM 价格预期为何被上调",
        desc="韩国 DRAM 出口高增、服务器 BMC 拉动、现货与长协涨价、终端需求承压和 HBM 价格上修，共同指向存储周期的结构性分化。",
        category="投资研究",
        series="AI算力产业链",
        tags=["DRAM", "HBM", "存储芯片", "SK海力士", "高盛", "AI服务器", "BMC", "半导体"],
        minutes=18,
        body=body("BV1o8tV6TEQU"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["DRAM", "HBM", "2027", "SK 海力士", "高盛", "400%", "BMC", "AI"],
        minimum=4700,
    ),
    pub.base.Post(
        slug="china-japan-lost-thirty-years-property-productivity-transition",
        title="中国会重演日本失去三十年吗：房地产、产业转型与低增长陷阱",
        desc="比较日本泡沫破裂后的资产负债表衰退与中国房地产退潮后的产业转型，真正的问题是适应能力、生产率和制度弹性。",
        category="宏观经济",
        series="经济通识课",
        tags=["中国经济", "日本经济", "失去三十年", "房地产", "资产负债表衰退", "生产率", "低增长", "宏观经济"],
        minutes=38,
        body=body("BV1rPtj6QEvK"),
        accent=("#111827", "#0f766e", "#f59e0b"),
        required=["日本", "中国", "房地产", "资产负债表", "生产力", "三十年", "低增长"],
        minimum=4700,
    ),
    pub.base.Post(
        slug="critical-thinking-evidence-standards-trust-verification",
        title="凭什么相信它是真的：证据标准与批判性思维的基础训练",
        desc="从相关性、可靠性、充分性、可验证性和独立性出发，建立一套判断证据质量、识别伪事实和校准信任的基础方法。",
        category="认知方法",
        series="思维训练",
        tags=["批判性思维", "证据标准", "事实核查", "可靠性", "可验证性", "信息判断", "认知方法", "信任"],
        minutes=30,
        body=body("BV1vAtM6nETR"),
        accent=("#111827", "#7c3aed", "#06b6d4"),
        required=["证据", "相关性", "可靠性", "充分性", "可验证性", "独立性", "批判性思维"],
        minimum=4300,
    ),
    pub.base.Post(
        slug="cpo-equipment-orders-domestic-supply-chain-lianxun",
        title="CPO 设备产业链：订单翻倍预期、国产设备布局与联讯仪器盈利拐点",
        desc="明年 CPO 设备订单翻倍预期明确，测试、固晶、耦合、键合等国产设备环节持续布局，联讯仪器中报验证盈利和订单弹性。",
        category="投资研究",
        series="光通信产业链",
        tags=["CPO", "光模块", "联讯仪器", "猎奇智能", "快克智能", "1.6T", "2.4T", "设备国产化"],
        minutes=11,
        body=body("BV1bVtM6CEbc"),
        accent=("#111827", "#0ea5e9", "#ec4899"),
        required=["CPO", "联讯仪器", "72.68%", "303%", "1.6T", "2.4T", "猎奇智能", "快克智能"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="semiconductor-communication-q2-ai-storage-iot-valuation",
        title="半导体与通信 Q2 业绩兑现：AI 算力、存储与物联网模组的三条景气线",
        desc="AI 硬件需求未见明确拐点，存储业绩与估值匹配度提升，物联网模组进入左侧修复，构成半导体与通信的三条景气线。",
        category="投资研究",
        series="半导体与通信",
        tags=["半导体", "通信", "AI算力", "存储", "物联网模组", "长鑫科技", "美格智能", "东山精密", "HBM"],
        minutes=24,
        body=body("BV1MLtM6VE8p"),
        accent=("#0f172a", "#7c3aed", "#14b8a6"),
        required=["AI 算力", "存储", "物联网模组", "长鑫科技", "美格智能", "东山精密", "HBM", "分红"],
        minimum=4000,
    ),
    pub.base.Post(
        slug="ai-prosperity-five-layer-transmission-capital-efficiency",
        title="AI 景气五层传导框架：从需求扩张到资本效率验证",
        desc="用需求基础、商业化闭环、资本开支、融资约束和资本效率五层框架，判断 AI 景气是继续扩散还是进入再定价阶段。",
        category="投资研究",
        series="AI产业观察",
        tags=["AI", "资本开支", "云计算", "模型收入", "订单", "融资", "资本效率", "产业链"],
        minutes=21,
        body=body("BV1Rrt76LEyC"),
        accent=("#111827", "#2563eb", "#22c55e"),
        required=["AI", "需求", "收入", "订单", "资本开支", "融资", "资本效率"],
        minimum=3900,
    ),
    pub.base.Post(
        slug="k-shaped-a-share-hong-kong-etf-allocation-rebalance",
        title="K 型分化之后：A 股、港股与 ETF 配置的再平衡路线图",
        desc="A 股、港股和 ETF 资金在地缘扰动与 AI 景气中走出 K 型分化，后续配置重点转向均值修复、产业弹性和仓位纪律。",
        category="投资研究",
        series="市场策略",
        tags=["A股", "港股", "ETF", "K型分化", "AI行情", "资产配置", "再平衡", "市场策略"],
        minutes=30,
        body=body("BV1X1t76kELU"),
        accent=("#0f172a", "#0891b2", "#f97316"),
        required=["K 型", "A 股", "港股", "ETF", "AI", "再平衡"],
        minimum=3800,
    ),
    pub.base.Post(
        slug="montage-technology-memory-interface-upgrade-new-products-growth",
        title="澜起科技：内存接口升级与新产品放量的成长曲线",
        desc="内存接口芯片在 DDR5 升级中强化基本盘，MRDIMM、CKD、PCIe 与 CXL 新产品决定澜起科技下一段成长斜率。",
        category="投资研究",
        series="AI算力产业链",
        tags=["澜起科技", "内存接口", "DDR5", "MRDIMM", "CKD", "PCIe", "CXL", "半导体"],
        minutes=7,
        body=body("BV1Q6tL6MEr1"),
        accent=("#111827", "#0f766e", "#2563eb"),
        required=["澜起科技", "DDR5", "内存接口", "MRDIMM", "PCIe", "CXL", "毛利率"],
        minimum=4000,
    ),
    pub.base.Post(
        slug="lower-tier-consumption-supply-demand-iteration-new-growth",
        title="下沉市场消费：供需迭代，何以向新？",
        desc="下沉市场不再只是低价渠道，而是人口回流、供给渗透、线上线下融合和万店模型共同推动的内需消费基本盘。",
        category="商业分析",
        series="消费观察",
        tags=["下沉市场", "消费", "内需", "供给迭代", "万店模型", "零售", "县域商业", "商业分析"],
        minutes=40,
        body=body("BV1S2tL6PEvK"),
        accent=("#111827", "#16a34a", "#f97316"),
        required=["下沉市场", "消费", "万店", "供给", "需求", "线上线下"],
        minimum=4300,
    ),
    pub.base.Post(
        slug="wanhua-chemical-supercycle-mdi-petrochemical-lfp-valuation",
        title="万华化学超级周期：基本盘、修复盘与成长盘共振",
        desc="MDI 基本盘、石化修复、新材料成长、磷酸铁锂布局和资本开支纪律，共同构成万华化学新一轮周期重估框架。",
        category="投资研究",
        series="化工产业链",
        tags=["万华化学", "MDI", "石化", "新材料", "磷酸铁锂", "资本开支", "杠杆", "估值"],
        minutes=14,
        body=body("BV1shtG6mEso"),
        accent=("#111827", "#dc2626", "#f59e0b"),
        required=["万华化学", "MDI", "石化", "新材料", "资本开支", "杠杆", "估值"],
        minimum=4600,
    ),
]


def chart_sources(slug: str) -> list[tuple[Path, str]]:
    root = OLD_CHART_ROOT if slug in {
        "cpo-equipment-orders-domestic-supply-chain-lianxun",
        "semiconductor-communication-q2-ai-storage-iot-valuation",
    } else NEW_CHART_ROOT
    return [(path, path.name) for path in sorted((root / slug).glob("*.svg"))]


pub.SCREENSHOT_SOURCES = {post.slug: chart_sources(post.slug) for post in pub.base.POSTS}

FORBIDDEN = [
    "B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里",
    "本期", "这期", "作者说", "他提到", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "油管", "BV1",
    "下期", "欢迎收看", "感谢大家", "晴天AI实战",
]
previous.FORBIDDEN = FORBIDDEN
pub.FORBIDDEN = FORBIDDEN


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = pub.base.run_gh(
            ["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"],
            {"content": base64.b64encode(content.encode("utf-8")).decode("ascii"), "encoding": "base64"},
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
        {"message": "Publish video-derived articles 2026-09-02", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
