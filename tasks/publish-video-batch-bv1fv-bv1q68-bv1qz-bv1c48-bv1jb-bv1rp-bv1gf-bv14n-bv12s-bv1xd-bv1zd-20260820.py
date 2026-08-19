from __future__ import annotations

import base64
import importlib.util
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PUB_SCRIPT = TASKS / "publish-video-batch-bv1ut-bv1ee-bv1fx-20260816.py"
ASSET_ROOT = TASKS / "video-batch-20260819-bv1fv-bv1q68-bv1qz-bv1c48-bv1jb-bv1rp-bv1gf-bv14n-bv12s-bv1xd-bv1zd"
DRAFTS = TASKS / "drafts"

spec = importlib.util.spec_from_file_location("video_publisher_base", PUB_SCRIPT)
pub = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = pub
spec.loader.exec_module(pub)

_run_gh = pub.base.run_gh


def run_gh_with_extra_retry(args: list[str], payload: dict | None = None):
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


pub.base.run_gh = run_gh_with_extra_retry
pub.base.__file__ = __file__
pub.base.DATE = "2026-08-20"
pub.base.BASE_DT = datetime(2026, 8, 20, 0, 20, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/antifragile-chaos-wild-growth/"
pub.base.PREV_EXISTING_TITLE = "反脆弱：不要追求稳定，要在混沌中野蛮生长"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1fv-bv1q68-bv1qz-bv1c48-bv1jb-bv1rp-bv1gf-bv14n-bv12s-bv1xd-bv1zd-20260820-changed-files.json"
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

POST_SPECS = [
    dict(
        bvid="BV1fv8u6NErK",
        slug="housing-provident-fund-real-estate-financialization-wealth-transfer",
        title="住房公积金的隐秘底层逻辑：从福利工具到房地产金融拐杖",
        desc="从福利分房退场、公积金资金池、低息房贷和商业银行压力，拆解这套制度怎样影响普通人的住房账本。",
        category="房地产",
        series="中国经济",
        tags=["住房公积金", "房地产", "房贷", "福利分房", "商业银行", "家庭资产负债表"],
        minutes=11,
        accent=("#0f172a", "#2563eb", "#f59e0b"),
        required=["公积金", "福利分房", "房地产", "低息贷款", "商业银行", "买房"],
        minimum=3000,
    ),
    dict(
        bvid="BV1q68n6hEcY",
        slug="picc-property-casualty-insurance-float-roe-valuation",
        title="中国财险为什么值得重估：浮存资金、承保利润与ROE修复",
        desc="围绕承保利润、综合成本率、浮存资金、资本市场回报和分红潜力，理解财险龙头的重估逻辑。",
        category="投资研究",
        series="保险行业",
        tags=["中国财险", "保险", "浮存资金", "ROE", "综合成本率", "分红"],
        minutes=13,
        accent=("#111827", "#0f766e", "#60a5fa"),
        required=["中国财险", "承保", "浮存资金", "ROE", "综合成本率", "分红"],
        minimum=2800,
    ),
    dict(
        bvid="BV1qz8n6wErg",
        slug="ai-hard-tech-investment-cloud-semiconductor-packaging-optical",
        title="AI+硬科技投资机会再梳理：从云、半导体设备到光通信",
        desc="从大模型付费、云基础设施、半导体测试、先进封装、光通信和国产替代，梳理 AI+硬科技的产业链机会。",
        category="投资研究",
        series="AI产业链",
        tags=["AI", "硬科技", "半导体", "先进封装", "光通信", "云计算"],
        minutes=14,
        accent=("#0f172a", "#7c3aed", "#0891b2"),
        required=["AI", "硬科技", "半导体", "先进封装", "光通信", "国产"],
        minimum=2600,
    ),
    dict(
        bvid="BV1C48n6gETq",
        slug="buffett-munger-thinking-learning-real-business-cases",
        title="巴菲特与芒格的学习方法：阅读、思考和真实商业案例",
        desc="学习不是收集金句，而是在阅读、案例、财报和独立思考里训练判断力，逐步形成可迁移的商业认知。",
        category="投资方法",
        series="长期主义",
        tags=["巴菲特", "芒格", "阅读", "学习方法", "商业案例", "投资方法"],
        minutes=7,
        accent=("#1f2937", "#b45309", "#2563eb"),
        required=["阅读", "学习", "巴菲特", "芒格", "思考", "商业"],
        minimum=2200,
    ),
    dict(
        bvid="BV1jbM26EEWx",
        slug="insilico-medicine-ai-drug-discovery-clinical-pipeline",
        title="英矽智能：AI制药掘金者的高风险与高上限",
        desc="从 AI 靶点发现、分子设计、临床验证和管线价值，理解英矽智能这类 AI 制药公司的上限与风险。",
        category="投资研究",
        series="AI制药",
        tags=["英矽智能", "AI制药", "药物发现", "临床管线", "创新药", "Biotech"],
        minutes=8,
        accent=("#0f172a", "#16a34a", "#7c3aed"),
        required=["英矽智能", "AI", "制药", "靶点", "分子", "临床"],
        minimum=2600,
    ),
    dict(
        bvid="BV1RpuA64EAA",
        slug="x-talpi-ai-science-drug-discovery-platform",
        title="晶泰科技：AI制药时代的卖铲人",
        desc="从 AI for Science 平台、药物发现服务、晶型预测和年度盈利，理解晶泰科技的商业模式与估值核心。",
        category="投资研究",
        series="AI制药",
        tags=["晶泰科技", "AI for Science", "AI制药", "药物发现", "卖铲人", "平台型公司"],
        minutes=8,
        accent=("#111827", "#0891b2", "#22c55e"),
        required=["晶泰科技", "AI", "卖铲人", "药物", "平台", "盈利"],
        minimum=2600,
    ),
    dict(
        bvid="BV1GF8j6VEim",
        slug="post-80s-90s-deleveraging-pain-household-balance-sheet",
        title="80后、90后为什么成了去杠杆最痛苦的一代",
        desc="在房价、学历、就业、家庭责任和资产负债表的共同作用下，80后、90后承受了增长叙事退潮后的去杠杆压力。",
        category="社会观察",
        series="代际结构",
        tags=["80后", "90后", "去杠杆", "房贷", "资产负债表", "就业"],
        minutes=9,
        accent=("#1f2937", "#dc2626", "#f59e0b"),
        required=["80 后", "90 后", "去杠杆", "房贷", "资产", "增长"],
        minimum=2400,
    ),
    dict(
        bvid="BV14N8G6pEAf",
        slug="companionship-commercialization-modern-intimacy-consumption",
        title="商务漂流、陪玩与虚拟角色：现代亲密关系为什么越来越商品化",
        desc="亲密关系被拆成陪伴、情绪价值、角色扮演和即时服务，背后是孤独、压抑、消费能力和关系成本的共同变化。",
        category="社会观察",
        series="亲密关系",
        tags=["陪伴经济", "亲密关系", "情绪价值", "陪玩", "消费", "孤独"],
        minutes=14,
        accent=("#111827", "#db2777", "#7c3aed"),
        required=["商务漂流", "陪伴", "亲密关系", "情绪价值", "消费", "孤独"],
        minimum=2600,
    ),
    dict(
        bvid="BV12sgW6zEGT",
        slug="age-30-to-40-leverage-assets-naval-framework",
        title="30到40岁：普通人从出卖时间到建立资产的关键十年",
        desc="把纳瓦尔关于杠杆、判断力和资产的框架放进普通人的人生阶段，30到40岁是从时间收入切换到资产收入的关键窗口。",
        category="个人成长",
        series="人生策略",
        tags=["30岁", "40岁", "纳瓦尔", "杠杆", "资产", "个人成长"],
        minutes=12,
        accent=("#0f172a", "#2563eb", "#d97706"),
        required=["30", "40", "纳瓦尔", "杠杆", "资产", "时间"],
        minimum=2500,
    ),
    dict(
        bvid="BV1xDEh65Eg9",
        slug="cash-will-be-precious-2026-2030-cycle-choice",
        title="2026到2030年，现金为什么会比想象中更金贵",
        desc="在通缩、资产重估、就业不确定和周期出清阶段，现金不只是低收益资产，更是选择权、抗风险能力和未来进攻筹码。",
        category="个人财务",
        series="现金流管理",
        tags=["现金", "存钱", "2026", "2030", "周期", "个人财务"],
        minutes=8,
        accent=("#111827", "#059669", "#f59e0b"),
        required=["现金", "2026", "2030", "存钱", "选择权", "周期"],
        minimum=2300,
    ),
    dict(
        bvid="BV1zDuc68EhH",
        slug="switch-from-learning-system-to-money-system",
        title="成长最快的方式，是从学习系统切换到赚钱系统",
        desc="真正有效的成长不是无限输入，而是进入市场反馈：研究赚钱、设计产品、找到客户、验证价值，并用现金流校准认知。",
        category="商业思维",
        series="普通人赚钱方法",
        tags=["赚钱", "学习系统", "市场反馈", "副业", "商业思维", "现金流"],
        minutes=8,
        accent=("#0f172a", "#ea580c", "#16a34a"),
        required=["学习系统", "赚钱系统", "市场", "客户", "产品", "现金流"],
        minimum=2300,
    ),
]

pub.base.POSTS = [
    pub.base.Post(
        slug=spec["slug"],
        title=spec["title"],
        desc=spec["desc"],
        category=spec["category"],
        series=spec["series"],
        tags=spec["tags"],
        minutes=spec["minutes"],
        body=body(spec["bvid"]),
        accent=spec["accent"],
        required=spec["required"],
        minimum=spec["minimum"],
    )
    for spec in POST_SPECS
]

pub.SCREENSHOT_SOURCES = {post.slug: [] for post in pub.base.POSTS}


def create_commit_20260820(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = pub.base.run_gh(["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    for path, content in sorted(binary_outputs.items()):
        blob = pub.base.run_gh(["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"], {"content": base64.b64encode(content).decode("ascii"), "encoding": "base64"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = pub.base.run_gh(["-X", "POST", pub.base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = pub.base.run_gh(
        ["-X", "POST", pub.base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish video-derived articles 2026-08-20", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


pub.create_commit = create_commit_20260820


if __name__ == "__main__":
    pub.main()
