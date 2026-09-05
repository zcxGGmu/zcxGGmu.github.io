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
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv1va-bv1py-bv1rd-bv16n-bv16p-20260904.py"
ASSET_ROOT = TASKS / "video-batch-20260905-bv1px-bv16p-bv1qz-bv1g1-bv1pu"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv1px-bv16p-bv1qz-bv1g1-bv1pu-20260905-output")

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
pub.base.DATE = "2026-09-05"
pub.base.BASE_DT = datetime(2026, 9, 5, 23, 50, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/voicestudio-local-ai-voice-workbench/"
pub.base.PREV_EXISTING_TITLE = "VoiceStudio：本地 AI 配音工作台的能力边界与落地路径"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv1px-bv16p-bv1qz-bv1g1-bv1pu-20260905-changed-files.json"
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
        slug="wage-doubles-real-purchasing-power-free-surplus-gap",
        title="工资翻倍之后，购买力为何可能翻四倍：真实节余决定生活分层",
        desc="用家庭人均可支配收入、刚性成本、自由节余、负债和风险缓冲，重新理解工资差距如何变成更大的真实购买力差距。",
        category="宏观经济",
        series="社会经济观察",
        tags=["收入分层", "购买力", "自由节余", "贫富差距", "家庭收入", "负债", "消费", "社会观察"],
        minutes=20,
        body=body("BV1PXtV6pEpK"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["购买力", "家庭人均可支配收入", "10,150", "55,586", "101,378", "3,500", "4.3 倍", "12 倍", "负债"],
        minimum=5600,
    ),
    pub.base.Post(
        slug="life-change-identity-nine-cognitive-levels",
        title="你想度过怎样的人生：先改写身份，再把理想生活放进今天",
        desc="改变人生不是先改行为，而是识别旧身份、隐藏目标、从众脚本和反愿景，再用理想的一天重建生活方向。",
        category="认知方法",
        series="人生操作系统",
        tags=["自我成长", "身份", "认知层级", "反愿景", "拖延", "人生选择", "自由", "行动方法"],
        minutes=28,
        body=body("BV16PbF6rE9Y"),
        accent=("#111827", "#7c3aed", "#10b981"),
        required=["身份", "拖延", "反愿景", "九层认知", "从众", "自主", "理想的一天", "成功"],
        minimum=5500,
    ),
    pub.base.Post(
        slug="pcb-supercycle-material-price-domestic-substitution-ai-server",
        title="PCB超级周期：AI服务器升级、材料提价与国产替代共振",
        desc="Rubin、Switch、1.6T光模块、CCL、电子布、铜箔、树脂和设备耗材共同进入升级周期，三季度业绩与价格成为验证窗口。",
        category="投资研究",
        series="AI算力产业链",
        tags=["PCB", "CCL", "电子布", "铜箔", "PTFE", "Rubin", "Switch", "树脂", "设备耗材", "国产替代"],
        minutes=55,
        body=body("BV1qZtT69EAR"),
        accent=("#0f172a", "#0f766e", "#f97316"),
        required=["PCB", "CCL", "PTFE", "M9", "M10", "Rubin", "Switch", "Low Dk", "H-VLP", "眉山", "10%", "2028"],
        minimum=6800,
    ),
    pub.base.Post(
        slug="ai-compute-power-gap-gas-turbine-hrsg-hot-end-parts",
        title="AI算力缺口传导至电力：HRSG、燃气轮机与热端部件的订单拐点",
        desc="数据中心用电把燃气轮机、HRSG和热端部件推到供需紧张位置，博盈特焊与应流股份分别体现配套设备和高端铸件逻辑。",
        category="投资研究",
        series="AI电力产业链",
        tags=["AI电力", "燃气轮机", "HRSG", "博盈特焊", "应流股份", "热端部件", "油气复合管", "核电", "航空发动机"],
        minutes=20,
        body=body("BV1g1tB6PEik"),
        accent=("#111827", "#dc2626", "#0ea5e9"),
        required=["HRSG", "博盈特焊", "应流股份", "燃气轮机", "越南", "2030", "60%", "20%", "15 亿元"],
        minimum=6400,
    ),
    pub.base.Post(
        slug="electronic-gases-memory-expansion-wf6-argon-price-cycle",
        title="存储扩产引爆电子气体：六氟化钨涨价、电子大宗卡位与氩气弹性",
        desc="电子特气看六氟化钨涨价，电子大宗看长约独供和国产替代，传统工业气体看氩气价格修复带来的利润弹性。",
        category="投资研究",
        series="半导体材料",
        tags=["电子气体", "电子特气", "电子大宗", "六氟化钨", "存储扩产", "氩气", "中船特气", "广钢气体", "杭氧股份"],
        minutes=13,
        body=body("BV1PUte61E6a"),
        accent=("#111827", "#7c3aed", "#16a34a"),
        required=["电子特气", "电子大宗", "六氟化钨", "15 年", "70%-75%", "8,000-9,000 吨", "200 多万元/吨", "氩气", "3,000 元/吨"],
        minimum=5400,
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


def render_asset_check() -> None:
    for post in pub.base.POSTS:
        cover = OUT_DIR / f"images/posts/{post.slug}/cover.svg"
        cover_png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(cover), "--out", str(cover_png)], check=True, capture_output=True, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(cover_png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe or cover_png.stat().st_size < 4096:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            chart = OUT_DIR / f"images/posts/{post.slug}/{dest}"
            content = chart.read_text(encoding="utf-8")
            ET.fromstring(content)
            bad = [word for word in FORBIDDEN if word in content]
            if bad:
                raise RuntimeError(f"forbidden wording in chart {post.slug}/{dest}: {bad}")
            chart_png = Path(f"/tmp/{post.slug}-{chart.stem}.png")
            subprocess.run(["sips", "-s", "format", "png", str(chart), "--out", str(chart_png)], check=True, capture_output=True, text=True)
            chart_probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(chart_png)], check=True, stdout=subprocess.PIPE, text=True).stdout
            if "pixelWidth: 1200" not in chart_probe or "pixelHeight: 675" not in chart_probe or chart_png.stat().st_size < 8192:
                raise RuntimeError(f"chart render failed: {post.slug}/{dest}: {chart_probe}")


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
        {"message": "Publish video-derived articles 2026-09-05", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    pub.base.run_gh(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


old_verify_remote_publish = pub.verify_remote_publish


def remote_file(path: str, commit_sha: str) -> str:
    data = pub.base.run_gh([pub.base.endpoint(f"contents/{quote(path, safe='/')}?ref={commit_sha}")])
    return base64.b64decode(data["content"]).decode("utf-8")


def verify_remote_publish(commit_sha: str, card_count: int, total_pages: int, binary_outputs: dict[str, bytes]) -> None:
    old_verify_remote_publish(commit_sha, card_count, total_pages, binary_outputs)
    home = remote_file("index.html", commit_sha)
    rss = remote_file("index.xml", commit_sha)
    sitemap = remote_file("sitemap.xml", commit_sha)
    home_hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', home)
    expected_prefix = pub.base.PINNED_PREFIX + [post.url_path for post in pub.base.POSTS] + [pub.base.PREV_EXISTING_URL]
    if home_hrefs[: len(expected_prefix)] != expected_prefix:
        raise RuntimeError(f"homepage prefix mismatch: {home_hrefs[:len(expected_prefix)]}")
    rss_links = re.findall(r"<link>(https://zcxggmu.github.io/2026/[^<]+/)</link>", rss)
    if rss_links[: len(pub.base.POSTS)] != [post.full_url for post in pub.base.POSTS]:
        raise RuntimeError(f"rss order mismatch: {rss_links[:len(pub.base.POSTS)]}")
    for post in pub.base.POSTS:
        article = remote_file(f"2026/{post.slug}/index.html", commit_sha)
        bad = [word for word in FORBIDDEN if word in article]
        if bad:
            raise RuntimeError(f"forbidden wording in remote article {post.slug}: {bad}")
        if article.count('<figure class="post-figure">') != len(pub.SCREENSHOT_SOURCES[post.slug]):
            raise RuntimeError(f"remote figure count mismatch: {post.slug}")
        if len(re.findall(r'<h2 id="', article)) < 5:
            raise RuntimeError(f"remote h2 count too low: {post.slug}")
        if post.full_url not in sitemap:
            raise RuntimeError(f"sitemap missing {post.slug}")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            rel = f"images/posts/{post.slug}/{dest}"
            data = pub.base.run_gh([pub.base.endpoint(f"contents/{quote(rel, safe='/')}?ref={commit_sha}")])
            raw = base64.b64decode(data["content"])
            ET.fromstring(raw.decode("utf-8"))
    for _ in range(12):
        try:
            build = pub.base.run_gh([pub.base.endpoint("pages/builds/latest")])
            error = build.get("error") or {}
            message = error.get("message") if isinstance(error, dict) else error
            if build.get("commit") == commit_sha and build.get("status") == "built" and not message:
                return
            if build.get("commit") == commit_sha and message:
                raise RuntimeError(f"GitHub Pages build failed: {message}")
        except RuntimeError as exc:
            if "Not Found" not in str(exc):
                raise
        time.sleep(5)
    raise RuntimeError("GitHub Pages build did not reach built state")


pub.render_asset_check = render_asset_check
pub.create_commit = create_commit
pub.verify_remote_publish = verify_remote_publish


if __name__ == "__main__":
    pub.main()
