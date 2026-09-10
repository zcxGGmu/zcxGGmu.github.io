from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
TEMPLATE = TASKS / "publish-ai-skills-voice-studio-20260905.py"
DRAFT = TASKS / "drafts" / "BV1n8YT6rEJH-body.html"

spec = importlib.util.spec_from_file_location("publish_voice_studio", TEMPLATE)
publisher = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = publisher
spec.loader.exec_module(publisher)

pub = publisher.pub
pub.base.__file__ = __file__
pub.base.DATE = "2026-09-11"
pub.base.BASE_DT = datetime(2026, 9, 11, 6, 30, tzinfo=timezone(timedelta(hours=8)))
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-ai-skills-grok-build-20260911-changed-files.json"
pub.base.PREV_EXISTING_URL = "/2026/labor-dispatch-outsourcing-hollowed-work/"
pub.base.PREV_EXISTING_TITLE = "劳务派遣为何掏空工作：从用工结构到劳动议价"
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

SLUG = "grok-build-codex-claude-code-coding-agent-comparison"
pub.base.POSTS = [
    pub.base.Post(
        slug=SLUG,
        title="Grok Build、Codex 与 Claude Code：三类编码 Agent 的工作流边界",
        desc="从全屏终端任务台、计划模式、子 Agent、工作树、规则兼容、权限沙箱到后台自动化，拆解三类编码 Agent 的真实差别与选型方法。",
        category="AI工具",
        series="AI Agent 工具链",
        tags=["AI Agent", "AI Skills", "Grok Build", "Codex", "Claude Code", "编码工具", "工作流", "开源项目"],
        minutes=11,
        body=DRAFT.read_text(encoding="utf-8"),
        accent=("#111827", "#0369a1", "#b45309"),
        required=["Grok Build", "Codex", "Claude Code", "计划模式", "工作树", "AGENTS.md", "沙箱", "ACP"],
        minimum=4000,
    )
]

pub.SCREENSHOT_SOURCES = {SLUG: []}
FORBIDDEN = [
    "B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里",
    "本期", "这期", "作者说", "他提到", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "BV1",
]
publisher.previous.FORBIDDEN = FORBIDDEN
pub.FORBIDDEN = FORBIDDEN
pub.base.FORBIDDEN = FORBIDDEN

if __name__ == "__main__":
    publisher.pub.main()
