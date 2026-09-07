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
PREV_WRAPPER = TASKS / "publish-video-batch-bv1lc-bv1vr-bv1vo-bv1rk-20260906.py"
ASSET_ROOT = TASKS / "video-batch-20260907-bv143-bv1fc-bv1s6-bv12v-bv1m5-bv1ux"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
OUT_DIR = Path("/tmp/video-batch-bv143-bv1fc-bv1s6-bv12v-bv1m5-bv1ux-20260907-output")

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
pub.base.DATE = "2026-09-07"
pub.base.BASE_DT = datetime(2026, 9, 7, 23, 59, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/money-psychology-wealth-human-nature-time-freedom/"
pub.base.PREV_EXISTING_TITLE = "《金钱心理学》：财富的终点，是把时间还给自己"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv143-bv1fc-bv1s6-bv12v-bv1m5-bv1ux-20260907-changed-files.json"
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
        slug="ai-bull-market-internet-bubble-chain-signals",
        title="AI牛市是否接近尾声：互联网泡沫对照、产业链分化与下一组信号",
        desc="把AI行情放回互联网泡沫参照系，拆解云厂商资本开支、模型公司收入、价格战、训练推理芯片、存储光模块周期和资金再平衡。",
        category="AI观察",
        series="AI产业周期",
        tags=["AI牛市", "互联网泡沫", "半导体", "云计算", "模型公司", "资本开支", "科技周期", "红利资产"],
        minutes=30,
        body=body("BV143tB64EvF"),
        accent=("#111827", "#2563eb", "#f97316"),
        required=["AI牛市", "互联网泡沫", "5倍", "80%", "7000亿美元", "ARR", "价格战", "CUDA", "10%", "红利"],
        minimum=6600,
    ),
    pub.base.Post(
        slug="us-nonfarm-162k-seasonal-adjustment-rate-cut-signal",
        title="美国非农16.2万背后：就业降温、季调扰动与降息路径",
        desc="拆解美国8月非农16.2万的季调扰动、医疗就业降温、数据修正风险、实际工资压力和通胀对利率路径的最终约束。",
        category="宏观经济",
        series="美国宏观观察",
        tags=["非农", "美联储", "降息", "通胀", "美国就业", "美债", "黄金", "实际工资"],
        minutes=8,
        body=body("BV1FcbE64EzV"),
        accent=("#0f172a", "#7c3aed", "#0ea5e9"),
        required=["16.2万", "5.5万", "5.9万", "4.2万", "1.3万", "4.1%", "3.1%", "3.4%", "9月11日"],
        minimum=3900,
    ),
    pub.base.Post(
        slug="gold-investment-window-real-rates-liquidity-macro-lines",
        title="黄金的黄金投资期结束了吗：实际利率、流动性与九月宏观主线",
        desc="用实际利率、美元体系、美债信用、黄金与美股关系、短中长期窗口、中国PMI、促消费和地缘油价重新拆解黄金配置。",
        category="宏观经济",
        series="黄金与大类资产",
        tags=["黄金", "实际利率", "美债", "美元", "流动性", "PMI", "促消费", "地缘冲突", "G20"],
        minutes=65,
        body=body("BV1s6bw6REN1"),
        accent=("#111827", "#d97706", "#0f766e"),
        required=["黄金", "实际利率", "美元体系", "美债", "AI", "49.8%", "40.4%", "32.8%", "28.7%", "95.9美元", "G20"],
        minimum=7600,
    ),
    pub.base.Post(
        slug="asset-strategy-framework-liquidity-valuation-cycle-independent-boom",
        title="资产策略框架总论：利率、估值、经济周期与独立景气",
        desc="重建资产策略框架：旧经验失效、公募定价权下降、TMT成交上限抬升、流动性指标边界、三类资产和不同卖出规则。",
        category="投资策略",
        series="策略框架课",
        tags=["资产配置", "A股策略", "TMT", "流动性", "估值", "PB", "ROE", "PEG", "红利", "AI"],
        minutes=70,
        body=body("BV12vbs64EDq"),
        accent=("#0f172a", "#0f766e", "#7c3aed"),
        required=["资产策略", "20%", "5万亿", "34万亿", "40%", "4.7", "-0.13", "0.4", "PB", "ROE", "PEG", "15%"],
        minimum=7900,
    ),
    pub.base.Post(
        slug="us-financial-fragility-strength-stock-bond-correlation-liquidity",
        title="美国金融市场的脆弱与坚强：股债相关性、政策拆弹与全球流动性",
        desc="从股债相关性、耶伦拆弹、日元和美债压力、美国工具箱、中国量价线索、居民存款活化与全球资金流，理解美国市场的强弱共存。",
        category="宏观经济",
        series="全球金融观察",
        tags=["美国金融市场", "股债相关性", "美债", "耶伦", "流动性", "地产政策", "居民存款", "港股", "PMI"],
        minutes=33,
        body=body("BV1m5bA6hEQb"),
        accent=("#111827", "#dc2626", "#2563eb"),
        required=["股债相关性", "2000", "2008", "耶伦", "4.7", "49.8%", "61.6", "76%", "56%", "321"],
        minimum=5600,
    ),
    pub.base.Post(
        slug="tencent-ai-workbench-agent-operating-system-open-ecosystem",
        title="腾讯AI新生态：从办公智能体到Agent操作系统",
        desc="腾讯AI生态从办公工具升级为全场景AI工作台，围绕Agent、专家、Skill、连接器、MCP和硬件入口构建操作系统级平台。",
        category="AI观察",
        series="AI产品与生态",
        tags=["腾讯", "AI工作台", "Agent", "智能体", "MCP", "硬件", "Skill", "企业服务", "AI办公"],
        minutes=23,
        body=body("BV1uXbc6ZEMi"),
        accent=("#0f172a", "#2563eb", "#06b6d4"),
        required=["腾讯", "AI工作台", "Agent", "操作系统", "30个品牌", "硬件", "专家", "Skill", "连接器", "MCP"],
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
        {"message": "Publish video-derived articles 2026-09-07", "tree": tree["sha"], "parents": [ref.commit_sha]},
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
        expected_figures = len(pub.SCREENSHOT_SOURCES[post.slug])
        if article.count('<figure class="post-figure">') != expected_figures:
            raise RuntimeError(f"remote figure count mismatch: {post.slug}")
        if len(re.findall(r'<h2 id="', article)) != expected_figures:
            raise RuntimeError(f"remote h2/figure mismatch: {post.slug}")
        if post.full_url not in sitemap:
            raise RuntimeError(f"sitemap missing {post.slug}")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            rel = f"images/posts/{post.slug}/{dest}"
            data = pub.base.run_gh([pub.base.endpoint(f"contents/{quote(rel, safe='/')}?ref={commit_sha}")])
            raw = base64.b64decode(data["content"])
            root = ET.fromstring(raw.decode("utf-8"))
            if root.attrib.get("width") != "1200" or root.attrib.get("height") != "675":
                raise RuntimeError(f"remote svg dimensions mismatch: {rel}")
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
