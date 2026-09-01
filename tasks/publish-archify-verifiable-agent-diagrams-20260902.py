from __future__ import annotations

import importlib.util
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE = TASKS / "publish-ai-skills-two-source-20260815.py"
spec = importlib.util.spec_from_file_location("archify_template", TEMPLATE)
template = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = template
spec.loader.exec_module(template)

base = template.base
base.__file__ = __file__
base.DATE = "2026-09-02"
base.BASE_DT = datetime(2026, 9, 2, 6, 0, tzinfo=timezone(timedelta(hours=8)))
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-archify-verifiable-agent-diagrams-20260902-changed-files.json"
base.PREV_EXISTING_URL = "/2026/kingboard-laminates-ai-ccl-glass-fabric-65-hkd/"
base.PREV_EXISTING_TITLE = "建滔积层板的 AI CCL 机会：高频高速材料、玻纤布与估值重估"
base.PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
    "/2026/original-accumulation-time-autonomy-ordinary-people/",
    "/2026/next-decade-wealth-leap-deflation-rmb-ai-cashflow/",
]

SLUG = "archify-verifiable-agent-diagrams-workflow"
BODY = (TASKS / "archify-verifiable-agent-diagrams-body-20260902.html").read_text(encoding="utf-8")
base.POSTS = [base.Post(
    slug=SLUG,
    title="Archify：把 Agent 架构图变成可校验、可追溯的工程交付物",
    desc="从有类型 JSON、确定性渲染、布局校验到 Architecture Delta，拆解 Archify 如何让架构表达进入可复查的工程流程。",
    category="AI工具",
    series="AI Agent",
    tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "架构设计", "系统设计", "工作流"],
    minutes=9,
    body=BODY,
    accent=("#111827", "#0f766e", "#b45309"),
    required=["Archify", "JSON", "校验", "Architecture Delta", "HTML", "证据"],
    minimum=3200,
)]

template.EXPECTED_LINKS = {SLUG: {"https://github.com/tt-a1i/archify"}}
template.FORBIDDEN = [
    "B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里",
    "音频中", "音频里", "本期", "这期", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "BV1",
]

old_validate = base.validate


def validate(outputs):
    old_validate(outputs)
    article = outputs[f"2026/{SLUG}/index.html"]
    body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    links = set(re.findall(r'https://github\.com/[^"<]+', body_match.group(1) if body_match else ""))
    if links != template.EXPECTED_LINKS[SLUG]:
        raise SystemExit(f"GitHub link coverage mismatch: {links}")


base.validate = validate

if __name__ == "__main__":
    template.main()
