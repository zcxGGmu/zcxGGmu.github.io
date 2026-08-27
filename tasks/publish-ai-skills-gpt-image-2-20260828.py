from __future__ import annotations

import importlib.util
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

TASKS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("daily", TASKS / "publish-ai-skills-two-source-20260818.py")
daily = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = daily
spec.loader.exec_module(daily)
base = daily.base
base.__file__ = __file__
base.DATE = "2026-08-28"
base.BASE_DT = datetime(2026, 8, 28, 6, 30, tzinfo=timezone(timedelta(hours=8)))
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-ai-skills-gpt-image-2-20260828-changed-files.json"
base.PREV_EXISTING_URL = "/2026/generation-burden-east-asia-catch-up-population-dividend/"
base.PREV_EXISTING_TITLE = "这一代人在承受什么：人口红利、社会结构与代际差异"
BODY = (TASKS / "ai-skills-gpt-image-2-body-20260828.html").read_text(encoding="utf-8")
SLUG = "awesome-gpt-image-2-532-cases-prompt-engineering"
base.POSTS = [base.Post(slug=SLUG, title="awesome-gpt-image-2：532 个案例如何变成可复用的图像提示词系统", desc="从案例检索、21 套模板到 Agent Skill，拆解如何把 GPT-Image-2 的视觉生成从反复试错变成可复盘、可授权、可交付的工作流。", category="AI工具", series="AI Agent", tags=["AI Skills", "AI Agent", "开源项目", "GitHub", "GPT-Image-2", "图像生成", "提示词工程", "工作流"], minutes=9, body=BODY, accent=("#111827", "#0f766e", "#f59e0b"), required=["532", "21", "Skill", "提示词", "授权", "验证"], minimum=2800)]
base.FORBIDDEN = ["B站", "bilibili", "Bilibili", "哔哩", "UP主", "up主", "原视频", "视频中", "视频里", "音频中", "音频里", "本期", "这期", "观看", "点赞", "投币", "收藏", "订阅", "关注", "三连", "BV1"]
daily.EXPECTED_LINKS = {SLUG: {"https://github.com/freestylefly/awesome-gpt-image-2"}}
daily.template.EXPECTED_LINKS = daily.EXPECTED_LINKS
daily.template.FORBIDDEN = base.FORBIDDEN
old_validate = base.validate
def validate(outputs):
    old_validate(outputs)
    article = outputs[f"2026/{SLUG}/index.html"]
    body = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    links = set(re.findall(r'https://github\.com/[^"<]+', body.group(1) if body else ""))
    if links != daily.EXPECTED_LINKS[SLUG]:
        raise SystemExit(f"GitHub link coverage mismatch: {links}")
base.validate = validate
if __name__ == "__main__":
    daily.template.main()
