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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1xn-bv1bv-bv1q2-20260903.py"
ASSET_ROOT = TASKS / "video-batch-20260904-bv1va-bv1py-bv1rd-bv16n-bv16p"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1va-bv1py-bv1rd-bv16n-bv16p-20260904-output")

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
pub.base.DATE = "2026-09-04"
pub.base.BASE_DT = datetime(2026, 9, 4, 23, 58, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/openmaic-interactive-course-agent-workflow/"
pub.base.PREV_EXISTING_TITLE = "OpenMAIC：把主题与资料转成可审查的多 Agent 互动课程"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1va-bv1py-bv1rd-bv16n-bv16p-20260904-changed-files.json"
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
        slug="young-people-intimacy-needs-love-offline-relationship",
        title="把亲密需求拆开：年轻人如何从压抑走向真实连接",
        desc="从身体需求、情感缺口、线下接触、外在管理到主动边界，拆解年轻人如何把亲密焦虑转成真实连接能力。",
        category="情感关系",
        series="年轻人亲密关系",
        tags=["亲密关系", "情感需求", "年轻人", "线下社交", "恋爱", "缺爱", "边界感", "自我成长"],
        minutes=11,
        body=body("BV1vato6RENj"),
        accent=("#111827", "#db2777", "#2563eb"),
        required=["亲密", "身体需求", "情感需求", "长期陪伴", "缺爱", "线下", "边界", "主动"],
        minimum=4200,
    ),
    pub.base.Post(
        slug="china-dual-speed-economy-policy-property-tech-focus",
        title="中国经济的双速格局：政策微调、地产重构与科技机会",
        desc="政策更偏向预算执行和结构微调，地产信用从开发商转向购房者，出口与科技韧性和内需压力共同构成双速经济。",
        category="宏观经济",
        series="中国经济观察",
        tags=["中国经济", "政策微调", "房地产", "双速经济", "出口", "内需", "美联储", "科技板块"],
        minutes=8,
        body=body("BV1PYtv61EgW"),
        accent=("#111827", "#2563eb", "#f59e0b"),
        required=["政策微调", "房地产", "双速经济", "出口", "内需", "美联储", "科技", "50%", "60%", "40 年"],
        minimum=3800,
    ),
    pub.base.Post(
        slug="china-ai-infrastructure-chip-hbm-system-breakthrough",
        title="中国AI基础设施爆发：真正瓶颈是晶圆与HBM",
        desc="Token需求近千倍增长之后，先进晶圆、良率、HBM、Chiplet、CANN、超级节点、液冷和电力系统共同决定本土算力突围。",
        category="产业观察",
        series="AI算力产业链",
        tags=["AI基础设施", "AI芯片", "HBM", "Chiplet", "先进封装", "CANN", "液冷", "数据中心", "储能"],
        minutes=20,
        body=body("BV1RDtd6XEe6"),
        accent=("#0f172a", "#7c3aed", "#0ea5e9"),
        required=["Token", "1000倍", "80%", "1400万颗", "200万颗", "500万颗", "HBM", "Chiplet", "CANN", "液冷"],
        minimum=5300,
    ),
    pub.base.Post(
        slug="kingboard-laminates-ai-ccl-vertical-integration-material-bottleneck",
        title="AI算力的材料瓶颈：高端覆铜板为何成为服务器供应链的新定价核心",
        desc="Low Dk、Low CTE、特种玻纤布、垂直一体化和结构性扩产，让高端覆铜板从周期材料变成AI服务器关键保供环节。",
        category="投资研究",
        series="AI算力产业链",
        tags=["建滔积层板", "覆铜板", "AI CCL", "玻纤布", "Low Dk", "Low CTE", "AI服务器", "垂直一体化"],
        minutes=17,
        body=body("BV16NtU63EfW"),
        accent=("#111827", "#0f766e", "#f97316"),
        required=["覆铜板", "建滔积层板", "1888.HK", "Low Dk", "Low CTE", "161%", "48亿美元", "9500万米", "2027年第三季度"],
        minimum=4700,
    ),
    pub.base.Post(
        slug="life-change-identity-nine-cognitive-levels",
        title="想改变人生，先改写你对自己的定义",
        desc="真正改变不是先改行为，而是识别旧身份、隐藏目标和从众脚本，用反愿景、九层认知和理想一天重建生活方向。",
        category="认知方法",
        series="人生操作系统",
        tags=["自我成长", "身份", "认知层级", "反愿景", "拖延", "人生选择", "自由", "行动方法"],
        minutes=28,
        body=body("BV16PbF6rE9Y"),
        accent=("#111827", "#7c3aed", "#10b981"),
        required=["身份", "拖延", "反愿景", "九层认知", "从众", "自主", "个体化", "理想的一天", "成功"],
        minimum=5500,
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
        {"message": "Publish video-derived articles 2026-09-04", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
