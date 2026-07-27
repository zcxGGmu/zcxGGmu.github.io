from __future__ import annotations

import html
import json
import os
import re
import shutil
import tarfile
import tempfile
import urllib.request
from pathlib import Path


SITE = "https://zcxggmu.github.io"
APP_URL = f"{SITE}/ai-news-radar/"
ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd())).resolve()
APP = ROOT / "ai-news-radar"
TARBALL_URL = os.environ.get(
    "AI_NEWS_RADAR_TARBALL_URL",
    "https://github.com/LearnPrompt/ai-news-radar/archive/refs/heads/master.tar.gz",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        if not path.is_dir() or path.is_symlink():
            raise RuntimeError(f"refusing to replace non-directory: {path}")
        if path.name != "ai-news-radar":
            raise RuntimeError(f"refusing to clear unexpected directory: {path}")
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def download_upstream() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="ai-news-radar-upstream-"))
    tarball = tmp / "source.tar.gz"
    req = urllib.request.Request(
        TARBALL_URL,
        headers={"User-Agent": "zcxggmu-ai-news-radar-sync"},
    )
    with urllib.request.urlopen(req, timeout=120) as response:
        tarball.write_bytes(response.read())
    with tarfile.open(tarball, "r:gz") as archive:
        for member in archive.getmembers():
            target = (tmp / member.name).resolve()
            if not target.is_relative_to(tmp.resolve()):
                raise RuntimeError(f"unsafe archive member path: {member.name}")
        archive.extractall(tmp)
    roots = [p for p in tmp.iterdir() if p.is_dir() and p.name.startswith("ai-news-radar-")]
    if len(roots) != 1:
        raise RuntimeError(f"unexpected upstream archive layout: {[p.name for p in roots]}")
    return roots[0]


def copy_file(src: Path, dst: Path) -> None:
    if not src.exists():
        raise RuntimeError(f"upstream runtime file missing: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def should_copy_asset(path: Path, src_root: Path) -> bool:
    rel = path.relative_to(src_root).as_posix()
    if rel.startswith("assets/screenshots/"):
        return False
    return True


def copy_tree(src_dir: Path, dst_dir: Path, predicate=None) -> None:
    if not src_dir.exists():
        raise RuntimeError(f"upstream runtime directory missing: {src_dir}")
    for src in sorted(src_dir.rglob("*")):
        if not src.is_file():
            continue
        if predicate is not None and not predicate(src):
            continue
        copy_file(src, dst_dir / src.relative_to(src_dir))


def rewrite_html(path: Path, canonical: str) -> None:
    text = read_text(path)
    text = re.sub(
        r'(<link\s+rel="canonical"\s+href=")[^"]*("\s*/?>)',
        rf"\1{canonical}\2",
        text,
        count=1,
    )
    text = re.sub(
        r'(<meta\s+property="og:url"\s+content=")[^"]*("\s*/?>)',
        rf"\1{canonical}\2",
        text,
        count=1,
    )
    text = re.sub(
        r'<meta\s+property="og:site_name"\s+content="AI News Radar"\s*/?>',
        '<meta property="og:site_name" content="zcxGGmu · AI News Radar" />',
        text,
    )
    write_text(path, text)


def install_app(src: Path) -> None:
    ensure_clean_dir(APP)
    for name in ["index.html", "site.webmanifest", "LICENSE"]:
        copy_file(src / name, APP / name)
    copy_tree(src / "assets", APP / "assets", lambda p: should_copy_asset(p, src))
    for name in ["classic", "legacy", "data"]:
        copy_tree(src / name, APP / name)

    rewrite_html(APP / "index.html", APP_URL)
    rewrite_html(APP / "classic/index.html", f"{APP_URL}classic/")
    rewrite_html(APP / "legacy/index.html", f"{APP_URL}legacy/")


def cover_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
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
</svg>"""


def install_cover() -> None:
    write_text(ROOT / "images/posts/ai-news-radar/cover.svg", cover_svg())


def pinned_card() -> str:
    title = "AI News Radar：24 小时 AI 更新雷达"
    summary = "自动整理过去 24 小时值得关注的 AI、模型、产品和开发者工具更新，支持精选/全量切换、栏目筛选、热点榜、来源健康和经典版视图。"
    return f"""<a href="/ai-news-radar/" class="a-block">
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
"""


def update_home() -> None:
    path = ROOT / "index.html"
    text = read_text(path)
    text = re.sub(r'\s*<a href="/ai-news-radar/" class="a-block">.*?</a>\s*', "\n", text, count=1, flags=re.S)
    first_card = re.search(r'<a href="[^"]+" class="a-block">', text)
    if not first_card:
        raise RuntimeError("homepage card block not found")
    text = text[: first_card.start()] + pinned_card() + text[first_card.start() :]
    write_text(path, text)


def parse_json_outputs() -> dict[str, str]:
    timestamps: dict[str, str] = {}
    for path in sorted((APP / "data").glob("*.json")):
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
        if isinstance(data, dict):
            generated = data.get("generated_at") or data.get("updated_at")
            if generated:
                timestamps[path.name] = generated
    return timestamps


def validate() -> None:
    required = [
        APP / "index.html",
        APP / "classic/index.html",
        APP / "legacy/index.html",
        APP / "assets/app.js",
        APP / "assets/styles.css",
        APP / "data/latest-24h.json",
        APP / "data/stories-merged.json",
        APP / "site.webmanifest",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(f"missing deployed runtime files: {missing}")

    for rel in ["index.html", "classic/index.html", "legacy/index.html"]:
        text = read_text(APP / rel)
        if "https://news.learnprompt.pro/" in text or "https://learnprompt.github.io/ai-news-radar/" in text:
            raise RuntimeError(f"source canonical URL leaked in ai-news-radar/{rel}")
        if APP_URL not in text:
            raise RuntimeError(f"blog canonical URL missing in ai-news-radar/{rel}")

    home = read_text(ROOT / "index.html")
    hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', home)
    if not hrefs or hrefs[0] != "/ai-news-radar/":
        raise RuntimeError(f"AI News Radar is not the first homepage card: {hrefs[:5]}")
    if hrefs.count("/ai-news-radar/") != 1:
        raise RuntimeError("AI News Radar homepage card is duplicated")

    illegal = [
        p.relative_to(APP).as_posix()
        for p in APP.rglob("*")
        if p.is_file()
        and (
            p.relative_to(APP).as_posix().startswith(".github/")
            or p.relative_to(APP).as_posix().startswith("scripts/")
            or p.relative_to(APP).as_posix().startswith("tests/")
            or p.name == "CNAME"
        )
    ]
    if illegal:
        raise RuntimeError(f"unexpected upstream non-runtime files copied: {illegal[:10]}")

    timestamps = parse_json_outputs()
    print(json.dumps({
        "app_url": APP_URL,
        "data_files": len(list((APP / "data").glob("*.json"))),
        "app_files": sum(1 for p in APP.rglob("*") if p.is_file()),
        "homepage_first": hrefs[0],
        "generated_at": timestamps.get("latest-24h.json"),
        "persona_generated_at": timestamps.get("top3-personas.json"),
    }, ensure_ascii=False, indent=2))


def main() -> None:
    src = download_upstream()
    install_app(src)
    install_cover()
    update_home()
    validate()


if __name__ == "__main__":
    main()
