from __future__ import annotations

import importlib.util
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE = TASKS / "publish-ai-skills-two-source-20260815.py"
spec = importlib.util.spec_from_file_location("openmaic_template", TEMPLATE)
template = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = template
spec.loader.exec_module(template)

base = template.base
base.__file__ = __file__
base.DATE = "2026-09-04"
base.BASE_DT = datetime(2026, 9, 4, 6, 0, tzinfo=timezone(timedelta(hours=8)))
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-openmaic-interactive-course-agent-workflow-20260904-changed-files.json"
base.PREV_EXISTING_URL = "/2026/pcb-upgrade-ai-server-single-machine-value-growth/"
base.PREV_EXISTING_TITLE = "PCB升级：单机价值量提升如何驱动AI服务器产业链增长"
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

SLUG = "openmaic-interactive-course-agent-workflow"
BODY = (TASKS / "openmaic-interactive-course-agent-workflow-body-20260904.html").read_text(encoding="utf-8")
REMOTE_SNAPSHOT = Path("/tmp/zcxgh-pages-20260904-v2")
base.POSTS = [base.Post(
    slug=SLUG,
    title="OpenMAIC：把主题与资料转成可审查的多 Agent 互动课程",
    desc="从课程大纲、材料输入、互动场景到可恢复任务与导出，拆解 OpenMAIC 如何把 AI 课程生成放进可验证工作流。",
    category="AI工具",
    series="AI Agent",
    tags=["AI Agent", "AI Skills", "开源项目", "GitHub", "教育科技", "课程设计", "工作流", "多Agent", "自动化"],
    minutes=13,
    body=BODY,
    accent=("#111827", "#2563eb", "#0f766e"),
    required=["OpenMAIC", "课程", "大纲", "材料", "互动", "审核", "导出", "模型"],
    minimum=3600,
)]

template.EXPECTED_LINKS = {SLUG: {"https://github.com/THU-MAIC/OpenMAIC"}}
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

# The snapshot was cloned from the API-checked remote head immediately before
# generation. Reading its unchanged pages avoids dozens of sequential API reads
# while the template still checks the ref before the non-forced update.
_remote_get_file = template.get_file_at_active_ref


def get_file_at_active_ref(path: str):
    local_path = REMOTE_SNAPSHOT / path
    if local_path.is_file():
        return local_path.read_text(encoding="utf-8")
    return _remote_get_file(path)


template.get_file_at_active_ref = get_file_at_active_ref

if __name__ == "__main__":
    template.main()
