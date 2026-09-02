from __future__ import annotations

import importlib.util
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE = TASKS / "publish-ai-skills-two-source-20260815.py"
spec = importlib.util.spec_from_file_location("ai_job_search_template", TEMPLATE)
template = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = template
spec.loader.exec_module(template)

base = template.base
base.__file__ = __file__
base.DATE = "2026-09-03"
base.BASE_DT = datetime(2026, 9, 3, 6, 0, tzinfo=timezone(timedelta(hours=8)))
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-ai-job-search-20260903-changed-files.json"
base.PREV_EXISTING_URL = "/2026/shenghong-technology-goldman-next-gen-gpu-asic-ai-server-pcb-q2/"
base.PREV_EXISTING_TITLE = "胜宏科技：Goldman Sachs、下一代 GPU/ASIC 与 AI 服务器 PCB"
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

SLUG = "ai-job-search-local-career-workflow"
BODY = (TASKS / "ai-job-search-local-career-workflow-body-20260903.html").read_text(encoding="utf-8")
base.POSTS = [base.Post(
    slug=SLUG,
    title="ai-job-search：把求职资料、岗位匹配与申请准备连成可审计工作流",
    desc="从个人资料、岗位筛选、事实核对到简历生成和人工批准，拆解 ai-job-search 在海外与中文求职场景中的能力边界。",
    category="AI工具",
    series="AI Agent",
    tags=["AI Agent", "AI Skills", "开源项目", "GitHub", "求职工具", "工作流", "隐私保护", "自动化"],
    minutes=11,
    body=BODY,
    accent=("#111827", "#0f766e", "#b45309"),
    required=["ai-job-search", "求职", "匹配", "事实", "隐私", "人工", "验证"],
    minimum=3000,
)]

template.EXPECTED_LINKS = {SLUG: {"https://github.com/MadsLorentzen/ai-job-search"}}
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
