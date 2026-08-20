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
DRAFTS = TASKS / "drafts"

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
pub.base.DATE = "2026-08-20"
pub.base.BASE_DT = datetime(2026, 8, 20, 10, 20, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/diagram-design-27-editorial-diagram-types-ai-visualization/"
pub.base.PREV_EXISTING_TITLE = "Diagram Design：用 27 种专业图表规则把 AI 输出变成可交付文档"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1ks-bv19a-20260820-changed-files.json"
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
        slug="marriage-script-loosening-men-women-cost-account",
        title="婚姻脚本松动：普通人为什么不再把结婚当成默认选项",
        desc="从普通男性的还债账、普通女性的小资压力、以及旧脚本失效之后的新脚本空白，重新理解婚姻观念的松动。",
        category="社会观察",
        series="婚育结构",
        tags=["婚姻", "结婚", "单身", "婚恋", "房贷", "彩礼", "婚育结构"],
        minutes=4,
        body=body("BV1ksMD6qEEU"),
        accent=("#111827", "#2563eb", "#f59e0b"),
        required=["婚姻", "房贷", "彩礼", "单身", "人生没有标准答案", "无欲则刚"],
        minimum=2200,
    ),
    pub.base.Post(
        slug="high-salary-marriage-market-choice-rights",
        title="年薪 200 万的稀缺幻觉：婚恋市场里的选择权从哪来",
        desc="从极端稀缺收入、选择权错觉、婚姻成本与伴侣责任，拆开“看不上”背后的现实边界。",
        category="社会观察",
        series="婚育结构",
        tags=["年薪200万", "婚恋市场", "选择权", "婚姻成本", "择偶", "社会阶层"],
        minutes=4,
        body=body("BV19au86NEXP"),
        accent=("#111827", "#7c3aed", "#dc2626"),
        required=["年薪 200 万", "选择权", "婚姻", "丈夫", "伴侣", "现实"],
        minimum=2200,
    ),
]

pub.SCREENSHOT_SOURCES = {post.slug: [] for post in pub.base.POSTS}


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
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


pub.create_commit = create_commit


if __name__ == "__main__":
    pub.main()
