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
#      uv run publish-video-batch-bv1g58-bv11t-bv1bf-bv1mphetm-bv1mphekk-bv18i-bv1qn-bv1aj-20260824.py
# 3. Or make executable and run:
#      chmod +x publish-video-batch-bv1g58-bv11t-bv1bf-bv1mphetm-bv1mphekk-bv18i-bv1qn-bv1aj-20260824.py && ./publish-video-batch-bv1g58-bv11t-bv1bf-bv1mphetm-bv1mphekk-bv18i-bv1qn-bv1aj-20260824.py
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
PREV_WRAPPER = TASKS / "publish-video-batch-bv15k-bv15m-bv1dl-20260823.py"
ASSET_ROOT = TASKS / "video-batch-20260824-bv1g58-bv11t-bv1bf-bv1mphetm-bv1mphekk-bv18i-bv1qn-bv1aj"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1g58-bv11t-bv1bf-bv1mphetm-bv1mphekk-bv18i-bv1qn-bv1aj-20260824-output")

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
pub.base.DATE = "2026-08-24"
pub.base.BASE_DT = datetime(2026, 8, 24, 22, 15, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/skill-compound-return-language-self-investment/"
pub.base.PREV_EXISTING_TITLE = "普通人最值得投的，是能长期复利的技能"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1g58-bv11t-bv1bf-bv1mphetm-bv1mphekk-bv18i-bv1qn-bv1aj-20260824-changed-files.json"
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
        slug="technology-resources-dividend-opportunities-market-strategy",
        title="科技、资源与红利机会：当前位置的市场策略框架",
        desc="从 AI 硬件分化、利润池迁移、资源全球定价和红利资产重估出发，建立当前位置的组合配置框架。",
        category="投资研究",
        series="市场策略",
        tags=["市场策略", "AI", "科技股", "资源品", "黄金", "红利", "红码", "资产配置"],
        minutes=12,
        body=body("BV1G58m6PEj1"),
        accent=("#111827", "#dc2626", "#f59e0b"),
        required=["科技", "AI", "硬件", "软件", "Token", "资源", "黄金", "红利", "红码", "分红率"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="two-worlds-of-post-90s-wealth-concentration-flexible-employment",
        title="90后的两个世界：财富集中、灵活就业与普通人的安全感",
        desc="同一代人一边面对失业和现金流脆弱，另一边站上机器人与高端制造财富浪潮；分化背后是增长模型的改变。",
        category="社会观察",
        series="年轻人选择",
        tags=["90后", "财富分化", "灵活就业", "机器人", "青年就业", "现金流", "安全感"],
        minutes=13,
        body=body("BV11T8v6JERr"),
        accent=("#111827", "#2563eb", "#16a34a"),
        required=["90后", "失业", "机器人", "财富", "存款", "灵活就业", "现金流", "债务", "技能", "安全感"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="us-treasury-shock-global-markets-a-share-hong-kong-response",
        title="美债扰动全球市场：A股与港股该如何应对",
        desc="从美债期限溢价、AI 融资压力、财政部回购局限、全球资产轮动和中国权益配置，拆解 A 股与港股的应对框架。",
        category="宏观经济",
        series="全球市场",
        tags=["美债", "A股", "港股", "AI融资", "期限溢价", "资产配置", "黄金", "亚洲市场"],
        minutes=17,
        body=body("BV1bf8e6dEZa"),
        accent=("#0f172a", "#2563eb", "#f59e0b"),
        required=["美债", "期限溢价", "财政部", "回购", "AI", "融资", "A股", "港股", "黄金", "轮动"],
        minimum=5000,
    ),
    pub.base.Post(
        slug="four-turning-points-a-share-second-half-market-outlook",
        title="四重拐点交织：A股下半年行情怎么看",
        desc="从估值、盈利、政策、外部利率和行业景气切换出发，判断 A 股下半年行情的弹性、约束和配置顺序。",
        category="投资研究",
        series="A股策略",
        tags=["A股", "下半年行情", "行业轮动", "估值", "盈利", "政策", "流动性", "资源品"],
        minutes=16,
        body=body("BV1mP8v6HETm"),
        accent=("#172554", "#dc2626", "#14b8a6"),
        required=["A股", "四重拐点", "估值", "盈利", "政策", "流动性", "行业", "轮动", "原油", "配置"],
        minimum=4800,
    ),
    pub.base.Post(
        slug="why-us-treasury-buybacks-failed-bond-market-storm",
        title="美债回购为何失效：本轮美债风暴的结构拆解",
        desc="财政部回购只能缓和交易摩擦，却不能消除债务供给、期限溢价、通胀尾部风险和政策不确定性带来的长端利率压力。",
        category="宏观经济",
        series="美元体系",
        tags=["美债", "长端利率", "回购", "期限溢价", "财政赤字", "通胀", "美联储", "AI融资"],
        minutes=18,
        body=body("BV1mP8v6HEKk"),
        accent=("#0f172a", "#7c3aed", "#f97316"),
        required=["美债", "回购", "长端", "期限溢价", "财政", "通胀", "美联储", "AI", "融资", "风暴"],
        minimum=5000,
    ),
    pub.base.Post(
        slug="why-acquaintances-do-not-recognize-your-success",
        title="为什么熟人看见你的风光，却不肯公开认可",
        desc="熟人圈的沉默往往不是没看见，而是比较、嫉妒、稀缺心态和身份排序共同作用；真正的成长不必依赖熟人掌声。",
        category="个人成长",
        series="关系心理",
        tags=["熟人关系", "比较心理", "嫉妒", "边界感", "自我成长", "认可", "人际关系"],
        minutes=8,
        body=body("BV18i8v68ES4"),
        accent=("#1f2937", "#db2777", "#f59e0b"),
        required=["熟人", "风光", "认可", "比较", "嫉妒", "稀缺", "陌生人", "边界", "成长"],
        minimum=2400,
    ),
    pub.base.Post(
        slug="micron-ai-memory-supercycle-us-answer",
        title="美光科技深度拆解：AI存储超级周期下的美国答案",
        desc="AI 服务器把存储从周期品推向战略品，美光在 HBM、DRAM、NAND 和美国供应链中的位置决定了利润弹性和估值边界。",
        category="投资研究",
        series="AI产业链",
        tags=["美光科技", "AI存储", "HBM", "DRAM", "NAND", "存储周期", "半导体", "美国供应链"],
        minutes=12,
        body=body("BV1Qn846BE5a"),
        accent=("#111827", "#2563eb", "#22c55e"),
        required=["美光", "AI", "存储", "HBM", "DRAM", "NAND", "超级周期", "供给", "价格", "估值"],
        minimum=3600,
    ),
    pub.base.Post(
        slug="midstream-economic-data-industry-comparison-rotation-strategy",
        title="中观经济数据视角下的行业比较与轮动策略",
        desc="用中观数据连接宏观叙事与行业配置，从需求、供给、价格、利润和库存变化中寻找更可靠的轮动线索。",
        category="投资研究",
        series="行业比较",
        tags=["中观数据", "行业比较", "轮动策略", "库存", "价格", "利润", "需求", "资产配置"],
        minutes=13,
        body=body("BV1aJ846uEUL"),
        accent=("#0f172a", "#0f766e", "#f97316"),
        required=["中观", "经济数据", "行业", "比较", "轮动", "需求", "供给", "价格", "利润", "库存"],
        minimum=4000,
    ),
]

pub.SCREENSHOT_SOURCES = {post.slug: [] for post in pub.base.POSTS}


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
        {"message": "Publish video-derived articles 2026-08-24", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
