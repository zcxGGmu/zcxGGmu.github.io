from __future__ import annotations

import importlib.util
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE = TASKS / "publish-ai-skills-two-source-20260815.py"
spec = importlib.util.spec_from_file_location("taste_daily_template", TEMPLATE)
template = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = template
spec.loader.exec_module(template)

base = template.base
base.__file__ = __file__
base.DATE = "2026-09-01"
base.BASE_DT = datetime(2026, 9, 1, 6, 0, tzinfo=timezone(timedelta(hours=8)))
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-taste-skill-anti-slop-20260901-changed-files.json"
base.PREV_EXISTING_URL = "/2026/shenghong-technology-nomura-q2-margin-capex-ai-pcb/"
base.PREV_EXISTING_TITLE = "胜宏科技二季度拆解：利润增长、毛利率承压与 AI PCB 资本开支"
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

SLUG = "taste-skill-anti-slop-frontend-design-system"
BODY = (TASKS / "taste-skill-anti-slop-frontend-design-system-body-20260901.html").read_text(encoding="utf-8")
base.POSTS = [
    base.Post(
        slug=SLUG,
        title="Taste Skill：让 AI 前端摆脱模板化的设计规范与落地边界",
        desc="拆解 Taste Skill 的三档设计参数、前置设计判断、反模板规则与交付检查，并讨论它在营销页、后台和品牌系统中的适用边界。",
        category="AI工具",
        series="AI Agent",
        tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "前端开发", "设计系统", "工作流"],
        minutes=6,
        body=BODY,
        accent=("#111827", "#0f766e", "#b45309"),
        required=["Taste Skill", "DESIGN_VARIANCE", "MOTION_INTENSITY", "VISUAL_DENSITY", "Skill", "验证"],
        minimum=3000,
    )
]

template.EXPECTED_LINKS = {SLUG: {"https://github.com/Leonxlnx/taste-skill"}}
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
