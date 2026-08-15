from __future__ import annotations

import base64
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote


sys.dont_write_bytecode = True

OWNER = "zcxGGmu"
REPO = "zcxGGmu.github.io"
BRANCH = "gh-pages"
SITE = "https://zcxggmu.github.io"
PAGE1_SIZE = 24
PAGE_SIZE = 10
SCRIPT_NAME = Path(__file__).name
MANIFEST_NAME = "pin-two-existing-posts-20260815-changed-files.json"

TARGETS = [
    "/2026/original-accumulation-time-autonomy-ordinary-people/",
    "/2026/next-decade-wealth-leap-deflation-rmb-ai-cashflow/",
]

PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
]

CARD_RE = re.compile(r'\s*<a href="[^"]+" class="a-block">.*?</a>\s*', re.S)
HREF_RE = re.compile(r'<a href="([^"]+)" class="a-block">')
PINNED_RE = re.compile(r'post-item-pinned|pin-badge')


def run_gh(args: list[str], payload: dict | None = None):
    for attempt in range(5):
        proc = subprocess.run(
            ["gh", "api", *args],
            input=json.dumps(payload) if payload is not None else None,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if proc.returncode == 0:
            return json.loads(proc.stdout) if proc.stdout.strip() else None
        msg = (proc.stderr or proc.stdout).strip()
        if attempt < 4 and any(token in msg.lower() for token in ["stream error", "connection", "reset", "timeout"]):
            time.sleep(2 + attempt * 3)
            continue
        raise RuntimeError(msg)


def endpoint(path: str) -> str:
    return f"repos/{OWNER}/{REPO}/{path}"


def get_ref() -> tuple[str, str]:
    item = run_gh([endpoint(f"git/ref/heads/{BRANCH}")])
    commit_sha = item["object"]["sha"]
    commit = run_gh([endpoint(f"git/commits/{commit_sha}")])
    return commit_sha, commit["tree"]["sha"]


def get_tree(commit_sha: str) -> dict[str, str]:
    tree = run_gh([endpoint(f"git/trees/{commit_sha}?recursive=1")])
    return {item["path"]: item["sha"] for item in tree["tree"] if item.get("type") == "blob"}


def read_remote(path: str, commit_sha: str) -> str:
    item = run_gh([endpoint(f"contents/{quote(path, safe='/')}?ref={commit_sha}")])
    return base64.b64decode(item["content"]).decode("utf-8")


def card_href(card: str) -> str:
    match = HREF_RE.search(card)
    if not match:
        raise RuntimeError("card href missing")
    return match.group(1)


def is_pinned(card: str) -> bool:
    return bool(PINNED_RE.search(card))


def mark_pinned(card: str) -> str:
    next_card = card
    if "post-item-pinned" not in next_card:
        next_card, count = re.subn(r'class="post-item-wrapper\s*"', 'class="post-item-wrapper post-item-pinned"', next_card, count=1)
        if count == 0:
            next_card = next_card.replace('class="post-item-wrapper ', 'class="post-item-wrapper post-item-pinned ', 1)
    if "pin-badge" not in next_card:
        next_card = next_card.replace(
            '<div class="post-item-meta">',
            '<div class="post-item-meta"><span class="pin-badge">📌 置顶</span> ',
            1,
        )
    return next_card


def cards_from(html: str) -> list[str]:
    return [match.group(0).strip() for match in CARD_RE.finditer(html)]


def pagination_paths(tree_paths: list[str]) -> list[str]:
    paths = ["index.html"]
    numbered: list[tuple[int, str]] = []
    for path in tree_paths:
        match = re.fullmatch(r"page/(\d+)/index\.html", path)
        if match and int(match.group(1)) >= 2:
            numbered.append((int(match.group(1)), path))
    paths.extend(path for _, path in sorted(numbered))
    return paths


def nav(page: int, total: int) -> str:
    previous = "" if page == 1 else "/" if page == 2 else f"/page/{page - 1}/"
    nxt = f"/page/{page + 1}/" if page < total else ""
    left = (
        f'<a class="pagination-action" href="{previous}"><span class="pagination-action-icon" aria-hidden="true">‹</span></a>'
        if previous
        else '<span class="pagination-action disabled"><span class="pagination-action-icon" aria-hidden="true">‹</span></span>'
    )
    right = (
        f'<a class="pagination-action" href="{nxt}"><span class="pagination-action-icon" aria-hidden="true">›</span></a>'
        if nxt
        else '<span class="pagination-action disabled"><span class="pagination-action-icon" aria-hidden="true">›</span></span>'
    )
    return f'''<div class="pagination">
    <a id="globalBackToTop" class="pagination-action animated-visibility invisible" href="#top"><span class="pagination-action-icon" aria-hidden="true">↑</span></a>
    {left}
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">{page}<br><div style="display:inline-block;transform:rotate(-28deg);margin:2px 0">-</div><br>{total}</span></div>
    {right}
  </div></div>
    <div class="pagination">
    {left}
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">{page}/{total}</span></div>
    {right}
  </div>'''


def page_html(template: str, page_cards: list[str], page: int, total: int) -> str:
    first = template.find('<a href="', template.find("post-list-container"))
    matches = list(CARD_RE.finditer(template))
    if first == -1 or not matches:
        raise RuntimeError("homepage card markers missing")
    result = template[: first] + "\n".join(page_cards) + template[matches[-1].end() :]
    result = re.sub(
        r'(<div id="extraContainer" class="extra-container"><div class="toc-wrapper"></div>).*?(<div id="single-column-footer">)',
        lambda m: m.group(1) + nav(page, total) + "\n    " + m.group(2),
        result,
        count=1,
        flags=re.S,
    )
    url = SITE + ("/" if page == 1 else f"/page/{page}/")
    result = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', result, count=1)
    return re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', result, count=1)


def build_outputs(commit_sha: str, tree_paths: list[str]) -> dict[str, str | None]:
    source_paths = pagination_paths(tree_paths)
    source_pages = {path: read_remote(path, commit_sha) for path in source_paths}
    ordered_cards: list[str] = []
    seen: set[str] = set()
    for path in source_paths:
        for card in cards_from(source_pages[path]):
            href = card_href(card)
            if href not in seen:
                seen.add(href)
                ordered_cards.append(card)

    by_href = {card_href(card): card for card in ordered_cards}
    missing = [target for target in TARGETS if target not in by_href]
    if missing:
        raise RuntimeError(f"target cards missing: {missing}")

    existing_pinned = [card for card in ordered_cards if is_pinned(card) and card_href(card) not in TARGETS]
    existing_pinned_hrefs = [card_href(card) for card in existing_pinned]
    if existing_pinned_hrefs[: len(PINNED_PREFIX)] != PINNED_PREFIX:
        raise RuntimeError(f"unexpected pinned prefix: {existing_pinned_hrefs[:len(PINNED_PREFIX)]}")

    target_cards = [mark_pinned(by_href[target]) for target in TARGETS]
    excluded = set(existing_pinned_hrefs) | set(TARGETS)
    normal_cards = [card for card in ordered_cards if card_href(card) not in excluded]
    final_cards = existing_pinned + target_cards + normal_cards

    expected_hrefs = [card_href(card) for card in ordered_cards]
    final_hrefs = [card_href(card) for card in final_cards]
    if len(final_hrefs) != len(set(final_hrefs)):
        raise RuntimeError("duplicate cards after pinning")
    if set(final_hrefs) != set(expected_hrefs):
        raise RuntimeError("card set changed unexpectedly")

    total_pages = 1 + ((max(0, len(final_cards) - PAGE1_SIZE) + PAGE_SIZE - 1) // PAGE_SIZE)
    template = source_pages["index.html"]
    outputs: dict[str, str | None] = {"index.html": page_html(template, final_cards[:PAGE1_SIZE], 1, total_pages)}
    cursor = PAGE1_SIZE
    for page in range(2, total_pages + 1):
        outputs[f"page/{page}/index.html"] = page_html(template, final_cards[cursor : cursor + PAGE_SIZE], page, total_pages)
        cursor += PAGE_SIZE

    existing_max = max([1] + [int(match.group(1)) for path in tree_paths if (match := re.fullmatch(r"page/(\d+)/index\.html", path))])
    for page in range(total_pages + 1, existing_max + 1):
        outputs[f"page/{page}/index.html"] = None

    outputs[f"tasks/{SCRIPT_NAME}"] = Path(__file__).read_text(encoding="utf-8")
    manifest_path = f"tasks/{MANIFEST_NAME}"
    outputs[manifest_path] = json.dumps(sorted(outputs.keys()), ensure_ascii=False, indent=2)
    validate(outputs, final_cards, total_pages)
    write_local_outputs(outputs)
    return outputs


def validate(outputs: dict[str, str | None], final_cards: list[str], total_pages: int) -> None:
    failures: list[str] = []
    home = outputs.get("index.html") or ""
    home_hrefs = [card_href(card) for card in cards_from(home)]
    expected = PINNED_PREFIX + TARGETS
    if home_hrefs[: len(expected)] != expected:
        failures.append(f"homepage prefix mismatch: {home_hrefs[:len(expected)]}")
    for target in TARGETS:
        card = next(card for card in cards_from(home) if card_href(card) == target)
        if not is_pinned(card):
            failures.append(f"target is not visually pinned: {target}")
    all_page_hrefs: list[str] = []
    for page in range(1, total_pages + 1):
        path = "index.html" if page == 1 else f"page/{page}/index.html"
        html = outputs.get(path)
        if not html:
            failures.append(f"missing output page: {path}")
            continue
        hrefs = [card_href(card) for card in cards_from(html)]
        all_page_hrefs.extend(hrefs)
        expected_count = PAGE1_SIZE if page == 1 else PAGE_SIZE
        if page < total_pages and len(hrefs) != expected_count:
            failures.append(f"{path}: expected {expected_count} cards, got {len(hrefs)}")
        if page == total_pages and not hrefs:
            failures.append(f"{path}: empty final page")
    final_hrefs = [card_href(card) for card in final_cards]
    if all_page_hrefs != final_hrefs:
        failures.append("rebuilt pagination order does not match final card order")
    if len(all_page_hrefs) != len(set(all_page_hrefs)):
        failures.append("duplicate cards in rebuilt pagination")
    if failures:
        raise SystemExit("\n".join(failures))


def write_local_outputs(outputs: dict[str, str | None]) -> None:
    out_dir = Path("/tmp/pin-two-existing-posts-20260815-output")
    if out_dir.exists():
        import shutil

        shutil.rmtree(out_dir)
    for path, content in outputs.items():
        if content is None:
            continue
        target = out_dir / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    print(json.dumps({"local_output": str(out_dir), "files": len([v for v in outputs.values() if v is not None]), "deleted": len([v for v in outputs.values() if v is None])}, ensure_ascii=False))


def create_commit(outputs: dict[str, str | None], parent: str, tree_sha: str) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = run_gh(["-X", "POST", endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = run_gh(["-X", "POST", endpoint("git/trees"), "--input", "-"], {"base_tree": tree_sha, "tree": entries})
    commit = run_gh(
        ["-X", "POST", endpoint("git/commits"), "--input", "-"],
        {"message": "Pin two existing homepage articles", "tree": tree["sha"], "parents": [parent]},
    )
    run_gh(["-X", "PATCH", endpoint(f"git/refs/heads/{BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def git_blob_sha(content: str) -> str:
    data = content.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    for attempt in range(3):
        parent, tree_sha = get_ref()
        remote_tree = get_tree(parent)
        outputs = build_outputs(parent, sorted(remote_tree.keys()))
        current, _ = get_ref()
        if current != parent:
            continue
        try:
            pushed = create_commit(outputs, parent, tree_sha)
        except RuntimeError as exc:
            if attempt < 2 and "Reference update failed" in str(exc):
                continue
            raise
        latest_tree = get_tree(pushed)
        mismatches = []
        for path, content in outputs.items():
            if content is None:
                if path in latest_tree:
                    mismatches.append(path)
            elif latest_tree.get(path) != git_blob_sha(content):
                mismatches.append(path)
        if mismatches:
            raise RuntimeError(f"remote output mismatch: {mismatches[:5]}")
        print(json.dumps({"parent": parent, "pushed": pushed, "files": len(outputs), "targets": TARGETS}, ensure_ascii=False, indent=2))
        return
    raise RuntimeError("remote reference advanced during all attempts")


if __name__ == "__main__":
    main()
