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
import json
import re
import requests
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
PREV_WRAPPER = TASKS / "publish-video-batch-bv143-bv1fc-bv1s6-bv12v-bv1m5-bv1ux-20260907.py"
ASSET_ROOT = TASKS / "video-batch-20260908-bv17e-bv1a4-bv1sd-bv1j3-bv1ja-bv1la-bv1ct-bv1mh-bv15f-bv1m6-bv1fq"
CHART_ROOT = ASSET_ROOT / "generated-slide-charts"
DRAFTS = TASKS / "drafts"
POST_MANIFEST = DRAFTS / "20260908-video-batch-posts.json"
OUT_DIR = Path("/tmp/video-batch-bv17e-bv1a4-bv1sd-bv1j3-bv1ja-bv1la-bv1ct-bv1mh-bv15f-bv1m6-bv1fq-20260908-output")

spec = importlib.util.spec_from_file_location("previous_video_publisher", PREV_WRAPPER)
previous = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = previous
spec.loader.exec_module(previous)

pub = previous.pub


def body(bvid: str) -> str:
    return (DRAFTS / f"{bvid}-body.html").read_text(encoding="utf-8")


def load_posts() -> list:
    payload = json.loads(POST_MANIFEST.read_text(encoding="utf-8"))
    posts = []
    for item in payload:
        posts.append(
            pub.base.Post(
                slug=item["slug"],
                title=item["title"],
                desc=item["desc"],
                category=item["category"],
                series=item["series"],
                tags=item["tags"],
                minutes=item["minutes"],
                body=body(item["bvid"]),
                accent=tuple(item["accent"]),
                required=item["required"],
                minimum=item["minimum"],
            )
        )
    return posts


cursor = previous
while True:
    if hasattr(cursor, "OUT_DIR"):
        cursor.OUT_DIR = OUT_DIR
    if not hasattr(cursor, "previous"):
        break
    cursor = cursor.previous

pub.base.__file__ = __file__
pub.base.DATE = "2026-09-08"
pub.base.BASE_DT = datetime(2026, 9, 8, 23, 59, 0, tzinfo=timezone(timedelta(hours=8)))
pub.base.PREV_EXISTING_URL = "/2026/ai-bull-market-internet-bubble-chain-signals/"
pub.base.PREV_EXISTING_TITLE = "AI牛市是否接近尾声：互联网泡沫对照、产业链分化与下一组信号"
pub.base.SCRIPT_NAME = Path(__file__).name
pub.base.MANIFEST_NAME = "publish-video-batch-bv17e-bv1a4-bv1sd-bv1j3-bv1ja-bv1la-bv1ct-bv1mh-bv15f-bv1m6-bv1fq-20260908-changed-files.json"
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
pub.base.POSTS = load_posts()


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

old_validate = pub.validate


def validate(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], card_count: int, total_pages: int) -> None:
    old_validate(outputs, binary_outputs, card_count, total_pages)
    failures: list[str] = []
    for post in pub.base.POSTS:
        article = outputs[f"2026/{post.slug}/index.html"] or ""
        expected = len(pub.SCREENSHOT_SOURCES[post.slug])
        if expected < 6:
            failures.append(f"{post.slug}: too few charts {expected}")
        if len(re.findall(r'<h2 id="', article)) != expected:
            failures.append(f"{post.slug}: h2/chart count mismatch")
        for _, dest in pub.SCREENSHOT_SOURCES[post.slug]:
            if f"/images/posts/{post.slug}/{dest}" not in article:
                failures.append(f"{post.slug}: missing chart reference {dest}")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str | None], binary_outputs: dict[str, bytes]) -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        if content is None:
            continue
        path = OUT_DIR / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for rel, content in binary_outputs.items():
        path = OUT_DIR / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(json.dumps({"local_output": str(OUT_DIR), "text_files": len([v for v in outputs.values() if v is not None]), "binary_files": len(binary_outputs), "deleted": len([v for v in outputs.values() if v is None]), "urls": [post.full_url for post in pub.base.POSTS]}, ensure_ascii=False, indent=2))


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
            root = ET.fromstring(content)
            if root.attrib.get("width") != "1200" or root.attrib.get("height") != "675":
                raise RuntimeError(f"chart dimensions mismatch: {post.slug}/{dest}")
            bad = [word for word in FORBIDDEN if word in content]
            if bad:
                raise RuntimeError(f"forbidden wording in chart {post.slug}/{dest}: {bad}")
            chart_png = Path(f"/tmp/{post.slug}-{chart.stem}.png")
            subprocess.run(["sips", "-s", "format", "png", str(chart), "--out", str(chart_png)], check=True, capture_output=True, text=True)
            chart_probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(chart_png)], check=True, stdout=subprocess.PIPE, text=True).stdout
            if "pixelWidth: 1200" not in chart_probe or "pixelHeight: 675" not in chart_probe or chart_png.stat().st_size < 8192:
                raise RuntimeError(f"chart render failed: {post.slug}/{dest}: {chart_probe}")


GITHUB_TOKEN: str | None = None


def github_token() -> str:
    global GITHUB_TOKEN
    if GITHUB_TOKEN is None:
        result = subprocess.run(["gh", "auth", "token"], check=True, capture_output=True, text=True)
        GITHUB_TOKEN = result.stdout.strip()
        if not GITHUB_TOKEN:
            raise RuntimeError("GitHub token is empty")
    return GITHUB_TOKEN


def api_json(method: str, endpoint: str, payload: dict | None = None) -> dict:
    url = f"https://api.github.com/{endpoint}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token()}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "codex-publisher/2026-09-08",
    }
    retryable = {408, 409, 429, 500, 502, 503, 504}
    for attempt in range(6):
        try:
            response = requests.request(method, url, headers=headers, json=payload, timeout=(10, 60))
        except requests.RequestException as exc:
            if attempt < 5:
                time.sleep(2 + attempt * 3)
                continue
            raise RuntimeError(f"GitHub API request failed after retries: {method} {endpoint}: {exc}") from exc
        if response.status_code < 400:
            return response.json() if response.content else {}
        if attempt < 5 and response.status_code in retryable:
            time.sleep(2 + attempt * 3)
            continue
        raise RuntimeError(f"GitHub API {method} {endpoint} failed: {response.status_code} {response.text[:500]}")


def run_gh_requests_compat(args: list[str], payload: dict | None = None):
    filtered = [arg for arg in args if arg not in {"--input", "-"}]
    if len(filtered) >= 3 and filtered[0] == "-X":
        return api_json(filtered[1], filtered[2], payload)
    if len(filtered) == 1:
        return api_json("GET", filtered[0], payload)
    raise RuntimeError(f"Unsupported gh compatibility args: {args}")


def run_gh_cli_compat(args: list[str], payload: dict | None = None):
    input_text = json.dumps(payload, ensure_ascii=False) if payload is not None else None
    retryable = ("stream error", "cancel", "connection", "reset", "timeout", "temporarily", "tls")
    for attempt in range(5):
        proc = subprocess.run(
            ["gh", "api", *args],
            input=input_text,
            capture_output=True,
            text=True,
            timeout=180,
        )
        if proc.returncode == 0:
            return json.loads(proc.stdout) if proc.stdout.strip() else {}
        msg = (proc.stderr or proc.stdout or "").lower()
        if attempt < 4 and any(token in msg for token in retryable):
            time.sleep(2 + attempt * 3)
            continue
        raise RuntimeError(f"gh api failed: {' '.join(args)}: {proc.stderr[:800] or proc.stdout[:800]}")


def create_commit_cli(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = run_gh_cli_compat(
            ["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"],
            {"content": base64.b64encode(content.encode("utf-8")).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    for path, content in sorted(binary_outputs.items()):
        blob = run_gh_cli_compat(
            ["-X", "POST", pub.base.endpoint("git/blobs"), "--input", "-"],
            {"content": base64.b64encode(content).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = run_gh_cli_compat(
        ["-X", "POST", pub.base.endpoint("git/trees"), "--input", "-"],
        {"base_tree": ref.tree_sha, "tree": entries},
    )
    commit = run_gh_cli_compat(
        ["-X", "POST", pub.base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish video-derived articles 2026-09-08", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    run_gh_cli_compat(
        ["-X", "PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), "--input", "-"],
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


def create_commit(outputs: dict[str, str | None], binary_outputs: dict[str, bytes], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = api_json(
            "POST",
            pub.base.endpoint("git/blobs"),
            {"content": base64.b64encode(content.encode("utf-8")).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    for path, content in sorted(binary_outputs.items()):
        blob = api_json(
            "POST",
            pub.base.endpoint("git/blobs"),
            {"content": base64.b64encode(content).decode("ascii"), "encoding": "base64"},
        )
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = api_json("POST", pub.base.endpoint("git/trees"), {"base_tree": ref.tree_sha, "tree": entries})
    commit = api_json(
        "POST",
        pub.base.endpoint("git/commits"),
        {"message": "Publish video-derived articles 2026-09-08", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    api_json("PATCH", pub.base.endpoint(f"git/refs/heads/{pub.base.BRANCH}"), {"sha": commit["sha"], "force": False})
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


pub.validate = validate
pub.write_outputs = write_outputs
pub.render_asset_check = render_asset_check
pub.create_commit = create_commit_cli
pub.verify_remote_publish = verify_remote_publish
pub.base.run_gh = run_gh_cli_compat


if __name__ == "__main__":
    pub.main()
