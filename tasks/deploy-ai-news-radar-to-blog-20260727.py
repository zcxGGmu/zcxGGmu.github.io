from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path("/tmp/hermes-video-publish-20260727-bv16-bv1gr.s5tOc3")
SRC = Path("/tmp/ai-news-radar-api.MtOaxS/extract")
APP = ROOT / "ai-news-radar"
SITE = "https://zcxggmu.github.io"
APP_URL = f"{SITE}/ai-news-radar/"
SCRIPT_NAME = "deploy-ai-news-radar-to-blog-20260727.py"
MANIFEST_NAME = "deploy-ai-news-radar-to-blog-20260727-changed-files.json"
CHANGED: set[str] = set()


TEXT_SUFFIXES = {".html", ".js", ".css", ".json", ".svg", ".webmanifest", ".md", ".txt", ".xml"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def rec(path: Path) -> None:
    CHANGED.add(rel(path))


def ensure_clean_dir(path: Path) -> None:
    if not path.exists():
        path.mkdir(parents=True)
        return
    if not path.is_dir():
        path.unlink()
        path.mkdir(parents=True)
        return
    for child in path.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    rec(dst)


def copy_tree(src_dir: Path, dst_dir: Path, include_suffixes: set[str] | None = None) -> None:
    for src in sorted(src_dir.rglob("*")):
        if not src.is_file():
            continue
        if include_suffixes is not None and src.suffix not in include_suffixes:
            continue
        copy_file(src, dst_dir / src.relative_to(src_dir))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    rec(path)


def rewrite_html(path: Path, canonical: str) -> None:
    text = read_text(path)
    text = re.sub(r'<link rel="canonical" href="[^"]*" />', f'<link rel="canonical" href="{canonical}" />', text)
    text = re.sub(r'<meta property="og:url" content="[^"]*" />', f'<meta property="og:url" content="{canonical}" />', text)
    text = re.sub(r'<meta property="og:site_name" content="AI News Radar" />', '<meta property="og:site_name" content="zcxGGmu · AI News Radar" />', text)
    write_text(path, text)


def install_app() -> None:
    if not SRC.exists():
        raise RuntimeError(f"source repo missing: {SRC}")
    ensure_clean_dir(APP)

    # Runtime files for the static app. The GitHub Actions, tests, scripts, docs,
    # skills and source research reports are intentionally not deployed; the
    # hosted app only needs HTML/CSS/JS/assets/data plus license.
    for name in ["index.html", "site.webmanifest", "LICENSE"]:
        copy_file(SRC / name, APP / name)
    for name in ["app.js", "motion.js", "styles.css", "view-mode.js", "view-switch.css", "logo.svg"]:
        copy_file(SRC / "assets" / name, APP / "assets" / name)
    copy_tree(SRC / "assets/icons", APP / "assets/icons")
    for top in ["classic", "legacy", "data"]:
        copy_tree(SRC / top, APP / top)

    # Keep the app self-contained under /ai-news-radar/.
    rewrite_html(APP / "index.html", APP_URL)
    rewrite_html(APP / "classic/index.html", f"{APP_URL}classic/")
    rewrite_html(APP / "legacy/index.html", f"{APP_URL}legacy/")


def cover_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">AI News Radar</title>
  <desc id="desc">24 小时 AI 更新雷达置顶入口</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#111827"/><stop offset="0.55" stop-color="#064e3b"/><stop offset="1" stop-color="#f59e0b"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="20" stdDeviation="20" flood-color="#000" flood-opacity="0.28"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.16" stroke="#f8fafc" stroke-width="3">
    <path d="M120 710 H1480"/><path d="M120 570 H1480"/><path d="M120 430 H1480"/><path d="M120 290 H1480"/>
    <path d="M260 180 V780"/><path d="M530 180 V780"/><path d="M800 180 V780"/><path d="M1070 180 V780"/><path d="M1340 180 V780"/>
  </g>
  <g filter="url(#shadow)">
    <circle cx="1210" cy="390" r="190" fill="#f8fafc" opacity="0.92"/>
    <circle cx="1210" cy="390" r="126" fill="#10b981" opacity="0.92"/>
    <path d="M1125 390 L1190 455 L1305 320" fill="none" stroke="#ffffff" stroke-width="36" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M170 635 C330 520 470 570 630 460 C795 346 940 405 1080 320" fill="none" stroke="#f8fafc" stroke-width="14" stroke-linecap="round" opacity="0.9"/>
    <circle cx="630" cy="460" r="36" fill="#fbbf24"/><circle cx="1080" cy="320" r="42" fill="#f8fafc"/>
  </g>
  <text x="112" y="210" fill="#f8fafc" font-family="Inter, Noto Sans SC, PingFang SC, Arial" font-size="88" font-weight="900">AI News Radar</text>
  <text x="118" y="296" fill="#d1fae5" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800">24 小时 AI 更新雷达</text>
  <text x="120" y="380" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="34" font-weight="700">精选 / 全量 · 模型 / 产品 / 开发者 / 行业 / 论文</text>
  <text x="120" y="448" fill="#e5e7eb" font-family="Noto Sans SC, PingFang SC, Arial" font-size="28" font-weight="600">静态部署在 zcxggmu.github.io，直接读取项目内 data/*.json</text>
</svg>'''


def install_cover() -> None:
    write_text(ROOT / "images/posts/ai-news-radar/cover.svg", cover_svg())


def pinned_card() -> str:
    title = "AI News Radar：24 小时 AI 更新雷达"
    summary = "自动整理过去 24 小时值得关注的 AI、模型、产品和开发者工具更新，支持精选/全量切换、栏目筛选、热点榜、来源健康和经典版视图。"
    return f'''<a href="/ai-news-radar/" class="a-block">
      <div class="post-item-wrapper post-item-pinned">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{html.escape(title)}</div>
            <div class="post-item-summary">{html.escape(summary)}</div>
            <div class="post-item-meta"><span class="pin-badge">📌 置顶</span> AI Radar <span class="meta-icon" aria-hidden="true">▣</span> Static App </div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('/images/posts/ai-news-radar/cover.svg')"></div></div>
        </div>
      </div>
    </a>
'''


def update_home() -> None:
    path = ROOT / "index.html"
    text = read_text(path)
    # Remove any previous AI News Radar card before re-inserting at the front of
    # the stream. This makes the script idempotent.
    text = re.sub(r'\s*<a href="/ai-news-radar/" class="a-block">.*?</a>\s*', "\n", text, count=1, flags=re.S)
    first_card = re.search(r'<a href="[^"]+" class="a-block">', text)
    if not first_card:
        raise RuntimeError("homepage card block not found")
    text = text[: first_card.start()] + pinned_card() + text[first_card.start():]
    write_text(path, text)


def copy_script_and_manifest() -> None:
    target = ROOT / "tasks" / SCRIPT_NAME
    shutil.copyfile(Path(__file__), target)
    rec(target)
    manifest = ROOT / "tasks" / MANIFEST_NAME
    manifest.write_text(json.dumps(sorted(CHANGED | {f"tasks/{MANIFEST_NAME}"}), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rec(manifest)


def is_binary(path: Path) -> bool:
    try:
        path.read_text(encoding="utf-8")
        return False
    except UnicodeDecodeError:
        return True


def validate() -> None:
    assert (APP / "index.html").exists()
    assert (APP / "assets/app.js").exists()
    assert (APP / "data/latest-24h.json").exists()
    assert (APP / "classic/index.html").exists()
    assert (APP / "legacy/index.html").exists()
    index = read_text(APP / "index.html")
    assert APP_URL in index
    assert "https://news.learnprompt.pro/" not in index
    classic = read_text(APP / "classic/index.html")
    assert f"{APP_URL}classic/" in classic
    home = read_text(ROOT / "index.html")
    hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', home)[:7]
    expected = [
        "/ai-news-radar/",
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
        "/2026/agentteams-collaborative-multi-agent-os-openclaw-hermes/",
    ]
    assert hrefs == expected, hrefs
    manifest = json.loads((ROOT / "tasks" / MANIFEST_NAME).read_text(encoding="utf-8"))
    missing = [p for p in manifest if not (ROOT / p).exists()]
    assert not missing, missing
    pycache = [p.as_posix() for p in APP.rglob("__pycache__")] + [p.as_posix() for p in APP.rglob("*.pyc")]
    assert not pycache, pycache[:5]
    binary_count = sum(1 for p in manifest if is_binary(ROOT / p))
    print(json.dumps({
        "app_url": APP_URL,
        "manifest_count": len(manifest),
        "binary_files": binary_count,
        "homepage_first_7": hrefs,
        "app_files": sum(1 for _ in APP.rglob("*") if _.is_file()),
    }, ensure_ascii=False, indent=2))


def main() -> None:
    install_app()
    install_cover()
    update_home()
    copy_script_and_manifest()
    validate()


if __name__ == "__main__":
    main()
