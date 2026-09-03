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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1vp-bv1ye-20260902.py"
ASSET_ROOT = TASKS / "video-batch-20260903-bv13s-bv1lz-bv1dr-bv1mf-bv1dxm-bv1dxu"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv13s-bv1lz-bv1dr-bv1mf-bv1dxm-bv1dxu-20260903-output")

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
pub.base.DATE = "2026-09-03"
pub.base.BASE_DT = datetime(2026, 9, 3, 23, 40, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/ai-job-search-local-career-workflow/"
pub.base.PREV_EXISTING_TITLE = "ai-job-search：把求职资料、岗位匹配与申请准备连成可审计工作流"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv13s-bv1lz-bv1dr-bv1mf-bv1dxm-bv1dxu-20260903-changed-files.json"
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
        slug="ordinary-people-long-downcycle-strategy",
        title="普通人如何穿过经济下行长周期：别等拐点，先重建自己的安全垫",
        desc="从8到10年的下行周期假设、全球分工、输入型通胀、内需偏弱和个人行动清单，拆解普通人如何先保住身体和现金流。",
        category="社会观察",
        series="普通人经济周期课",
        tags=["普通人", "经济下行", "内卷", "消费", "通胀", "就业", "投资学习", "现金流"],
        minutes=14,
        body=body("BV13stU6bEBr"),
        accent=("#111827", "#0f766e", "#f97316"),
        required=["8 到 10 年", "2035", "资源", "生产", "消费", "通胀", "现金流", "身体"],
        minimum=4700,
    ),
    pub.base.Post(
        slug="china-us-consumption-gap-three-adjustments",
        title="中美消费差距不是20倍：从统计口径、汇率到购买力的三次校准",
        desc="用2024年官方消费数据逐层校准统计单位、支出范围、汇率和购买力，解释20倍、7倍与3.5倍差距分别意味着什么。",
        category="宏观经济",
        series="中美生活账本",
        tags=["中美消费", "购买力", "汇率", "消费支出", "统计口径", "生活成本", "住房", "医疗保险"],
        minutes=24,
        body=body("BV1Lzt76mE8a"),
        accent=("#111827", "#2563eb", "#f59e0b"),
        required=["78,535 美元", "28,221 元", "2.4 人", "9,797 美元", "2,292 美元", "27,686 美元", "7 倍", "3.5 倍"],
        minimum=5000,
    ),
    pub.base.Post(
        slug="us-treasury-high-yield-dollar-liquidity-reset",
        title="美债高利率的真正压力：强美元叙事退潮后的流动性拐点",
        desc="十年期美债收益率迫近5%的背后，是供给增加、需求回落、安全资产叙事松动和新接盘资金的重新定价。",
        category="宏观经济",
        series="全球宏观观察",
        tags=["美债", "美元流动性", "强美元", "黄金", "有色", "中国核心资产", "地产", "消费"],
        minutes=15,
        body=body("BV1DRt96GEwJ"),
        accent=("#111827", "#dc2626", "#f59e0b"),
        required=["美债", "5%", "9 月 18 日", "强美元", "银行接盘", "黄金", "有色", "中国核心资产"],
        minimum=4400,
    ),
    pub.base.Post(
        slug="a-share-ai-earnings-liquidity-2026",
        title="A股下半场：盈利复苏、去杠杆出清与AI再定价",
        desc="A股下半年主线是盈利15%修复、科技去杠杆、国产算力追赶、居民理财分层入市，以及AI模型从算力叙事转向Token ROI。",
        category="投资研究",
        series="A股策略",
        tags=["A股", "AI", "国产算力", "盈利复苏", "ETF", "公募基金", "互联网", "Token ROI", "港股"],
        minutes=96,
        body=body("BV1mft96zEox"),
        accent=("#111827", "#7c3aed", "#0ea5e9"),
        required=["A股", "15%", "30%", "国产 GPU", "4900 亿元", "Token ROI", "互联网", "港股"],
        minimum=6000,
    ),
    pub.base.Post(
        slug="global-macro-inflation-bear-flattening-2026",
        title="通胀重新定价全球市场：从油价冲击到收益率曲线熊式平坦化",
        desc="2026年9月初油价和通胀预期重新上行，推动收益率曲线熊式平坦化，股债黄金加密资产同步去杠杆。",
        category="宏观经济",
        series="全球宏观观察",
        tags=["通胀", "油价", "收益率曲线", "美联储", "欧洲央行", "日本央行", "新兴市场", "去杠杆"],
        minutes=10,
        body=body("BV1DXt96CEmd"),
        accent=("#111827", "#dc2626", "#2563eb"),
        required=["通胀", "熊式平坦化", "4.85%", "95.14 美元", "90.22 美元", "黄金", "欧元区", "套息交易"],
        minimum=4600,
    ),
    pub.base.Post(
        slug="humanoid-robots-brain-data-commercialization-2026",
        title="人形机器人下半场：会跑只是起点，真正的胜负在大脑",
        desc="人形机器人从运动展示走向真实任务，自主执行、第一视角数据、世界模型和商业化闭环决定下一阶段估值。",
        category="产业观察",
        series="AI机器人产业链",
        tags=["人形机器人", "AI", "莫拉维克悖论", "世界模型", "第一视角数据", "灵巧手", "供应链", "商业化"],
        minutes=11,
        body=body("BV1DXt96CEUQ"),
        accent=("#111827", "#0f766e", "#8b5cf6"),
        required=["人形机器人", "8.64 秒", "莫拉维克", "666", "19,000 台", "270%", "97%", "大脑"],
        minimum=4700,
    ),
]


def chart_sources(slug: str) -> list[tuple[Path, str]]:
    return [(path, path.name) for path in sorted((CHART_ROOT / slug).glob("*.svg"))]


pub.SCREENSHOT_SOURCES = {post.slug: chart_sources(post.slug) for post in pub.base.POSTS}

FORBIDDEN = [
    "B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里",
    "本期", "这期", "作者说", "他提到", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "油管",
    "下期", "欢迎收看", "感谢大家", "晴天AI实战", "BV1",
]
previous.FORBIDDEN = FORBIDDEN
pub.FORBIDDEN = FORBIDDEN
if hasattr(pub.base, "FORBIDDEN"):
    pub.base.FORBIDDEN = FORBIDDEN


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
        {"message": "Publish video-derived articles 2026-09-03", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
