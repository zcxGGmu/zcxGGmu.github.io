# -*- coding: utf-8 -*-
from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path('/tmp/hermes-video-publish')
DATA = Path('/tmp/bv-two-20260719/posts.json')
SITE = 'https://zcxggmu.github.io'
DATE = '2026-07-19'
SCRIPT_REL = 'tasks/publish-work-freedom-bullshit-jobs-batch.py'
CHANGED_REL = 'tasks/publish-work-freedom-bullshit-jobs-changed-files.json'
PINNED = [
    '/2026/codeinsights-local-first-agent-workbench/',
    '/2026/what-you-need-to-learn-from-claw-code-repo/',
    '/2026/gaojingqi-investment-system/',
    '/2026/ai-revolution-permanent-underclass-career-selection/',
    '/2026/live-longer-than-earn-fast-investment-infinite-game/',
]
PREV_ORIGINAL_URL = '/2026/economic-cycles-interest-debt-human-nature/'
PREV_ORIGINAL_TITLE = '逃不开的经济周期：利率、债务与人性，如何反复收割普通人'
PUB_START = datetime(2026, 7, 19, 10, 0, tzinfo=timezone(timedelta(hours=8)))
POSTS = json.loads(DATA.read_text(encoding='utf-8'))
CHANGED: set[str] = set()


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def rec(path: Path) -> None:
    CHANGED.add(path.relative_to(ROOT).as_posix())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
    rec(path)


def term_url(kind: str, term: str) -> str:
    return f'/{kind}/{quote(term)}/'


def prepare_posts() -> None:
    for post in POSTS:
        post['url'] = f'/2026/{post["slug"]}/'
        post['cover'] = f'/images/posts/{post["slug"]}/cover.svg'


def meta_links(post: dict) -> str:
    cat = f'<a href="{term_url("categories", post["category"])}">{esc(post["category"])}</a>'
    tags = '&nbsp;'.join(f'<a href="{term_url("tags", tag)}">{esc(tag)}</a>' for tag in post['tags'])
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post["minutes"]} min'


def build_toc(article: str) -> str:
    links = [f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>' for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', article)]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + ''.join(links) + '</nav></div></div>'


def title_lines(title: str) -> tuple[str, str]:
    if '：' in title:
        a, b = title.split('：', 1)
        return a, b
    if ':' in title:
        a, b = title.split(':', 1)
        return a, b
    return title[:18], title[18:]


def cover_svg(post: dict, idx: int) -> str:
    palettes = [
        ('#111827', '#1f2937', '#0891b2', '#e0f2fe'),
        ('#18181b', '#4c1d95', '#f97316', '#ffedd5'),
    ]
    a, b, c, d = palettes[idx % len(palettes)]
    line1, line2 = title_lines(post['title'])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="0.58" stop-color="{b}"/><stop offset="1" stop-color="{c}"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.34"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.13" stroke="#f8fafc" stroke-width="3"><path d="M130 690 H1470"/><path d="M130 560 H1470"/><path d="M130 430 H1470"/><path d="M130 300 H1470"/><path d="M340 235 V760"/><path d="M660 235 V760"/><path d="M980 235 V760"/><path d="M1300 235 V760"/></g>
  <g filter="url(#shadow)">
    <path d="M170 630 C320 520 430 575 560 455 C730 298 880 418 1050 300 C1200 195 1320 176 1450 132" fill="none" stroke="{d}" stroke-width="18" stroke-linecap="round"/>
    <rect x="112" y="610" width="1040" height="118" rx="24" fill="#ffffff" opacity="0.94"/>
    <text x="156" y="682" fill="{b}" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800">{esc(post['cover_sub'])}</text>
  </g>
  <text x="96" y="145" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="60" font-weight="800">{esc(line1)}</text>
  <text x="96" y="224" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="46" font-weight="760">{esc(line2)}</text>
  <text x="100" y="304" fill="{d}" font-family="Noto Sans SC, PingFang SC, Arial" font-size="32" font-weight="700">{esc(post['cover_note'])}</text>
</svg>'''


def build_article(post: dict, prev_url: str, prev_title: str, next_url: str | None, next_title: str | None) -> None:
    template = (ROOT / PREV_ORIGINAL_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    start = template.find('<article class="post">')
    end = template.find('</article>', start) + len('</article>')
    head, tail = template[:start], template[end:]
    full_url = SITE + post['url']
    replacements = {
        r'<title>.*?</title>': f'<title>{esc(post["title"])} - zcxGGmu\'s Blog</title>',
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(post["desc"])}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(full_url)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(post["title"])}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(post["desc"])}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(full_url)}">',
    }
    for pattern, repl in replacements.items():
        head = re.sub(pattern, repl, head, flags=re.S)
    newer = f'<a class="newer-posts" href="{next_url}">下一篇<br>{esc(next_title or "")}</a>' if next_url else '<a class="newer-posts">下一篇<br>没有更新的文章</a>'
    older = f'<a class="older-posts" href="{prev_url}">上一篇<br>{esc(prev_title)}</a>'
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{post['cover']}')"><div class="post-title">{esc(post['title'])}<div class="post-subtitle">{esc(post['desc'])}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links(post)}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{post['article']}</div></div><nav class="post-pagination">{newer}{older}</nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(post['article']), tail, flags=re.S)
    write(ROOT / post['url'].strip('/') / 'index.html', head + article + tail)


def update_original_prev(new_url: str, new_title: str) -> None:
    path = ROOT / PREV_ORIGINAL_URL.strip('/') / 'index.html'
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>', f'<a class="newer-posts" href="{new_url}">下一篇<br>{esc(new_title)}</a>', text, count=1, flags=re.S)
    write(path, text)


def home_card(post: dict) -> str:
    return f'''<a href="{post['url']}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(post['title'])}</div>
            <div class="post-item-summary">{esc(post['desc'])}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post['minutes']} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{post['cover']}')"></div></div>
        </div>
      </div>
    </a>'''


def update_home() -> None:
    path = ROOT / 'index.html'
    text = path.read_text(encoding='utf-8')
    for post in POSTS:
        text = re.sub(rf'<a href="{re.escape(post["url"])}" class="a-block">.*?</a>\s*', '', text, flags=re.S)
    pos = text.find(f'<a href="{PREV_ORIGINAL_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError('homepage insertion marker not found')
    cards = '\n'.join(home_card(post) for post in reversed(POSTS)) + '\n'
    write(path, text[:pos] + cards + text[pos:])


def update_rss() -> None:
    path = ROOT / 'index.xml'
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{format_datetime(PUB_START + timedelta(minutes=len(POSTS)))}</lastBuildDate>', text)
    for post in POSTS:
        text = re.sub(rf'<item>\s*<title>{re.escape(esc(post["title"]))}</title>.*?</item>\s*', '', text, flags=re.S)
    items = []
    for i, post in enumerate(reversed(POSTS)):
        dt = PUB_START + timedelta(minutes=len(POSTS) - i)
        full_url = SITE + post['url']
        items.append(f'<item>\n<title>{esc(post["title"])}</title>\n<link>{full_url}</link>\n<guid>{full_url}</guid>\n<pubDate>{format_datetime(dt)}</pubDate>\n<description>{esc(post["desc"])}</description>\n</item>\n')
    write(path, text.replace('<item>', ''.join(items) + '<item>', 1))


def update_archive() -> None:
    path = ROOT / 'archive/index.html'
    text = path.read_text(encoding='utf-8')
    missing = sum(1 for post in POSTS if post['url'] not in text)
    if missing:
        text = re.sub(r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>', lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + missing} 篇</span>', text, count=1)
    for post in POSTS:
        text = re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(post["url"])}">.*?</div>\s*', '', text, flags=re.S)
    items = []
    for post in reversed(POSTS):
        items.append(f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{post['url']}">{esc(post['title'])}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(post['category'])}</span></span>
      </div> ''')
    pos = text.find(f'<a href="{PREV_ORIGINAL_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    if pos == -1 or start == -1:
        raise RuntimeError('archive insertion marker not found')
    write(path, text[:start] + ''.join(items) + text[start:])


def tax_item(post: dict) -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{post['url']}" style="font-size:16px;text-decoration:none">{esc(post['title'])}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''


def update_term_index(kind: str, term: str, delta: int) -> None:
    if not delta:
        return
    path = ROOT / kind / 'index.html'
    text = path.read_text(encoding='utf-8')
    href = f'/{kind}/{quote(term)}/'
    if href in text:
        pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span style="color:#999[^>]*>\()(\d+)(\)</span></a>)')
        text = pattern.sub(lambda m: f'{m.group(1)}{int(m.group(2)) + delta}{m.group(3)}', text, count=1)
    else:
        if kind == 'tags':
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">({delta})</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">({delta})</span></a>\n'
        pos = text.find('</div></div></div>')
        if pos == -1:
            raise RuntimeError(f'term index insertion marker not found: {kind}')
        text = text[:pos] + item + text[pos:]
    write(path, text)


def update_term(kind: str, term: str, prefix: str, emoji: str, posts: list[dict]) -> None:
    path = ROOT / kind / term / 'index.html'
    if path.exists():
        old = path.read_text(encoding='utf-8')
        inserted = sum(1 for post in posts if post['url'] not in old)
        text = old
        for post in posts:
            text = re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(post["url"])}".*?</div>\s*', '', text, flags=re.S)
        if inserted:
            text = re.sub(r'共 (\d+) 篇文章', lambda m: f'共 {int(m.group(1)) + inserted} 篇文章', text, count=1)
        first = text.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
        if first == -1:
            first = text.find('</div></div></div>')
        if first == -1:
            raise RuntimeError(f'term insertion marker not found: {kind}/{term}')
        text = text[:first] + ''.join(tax_item(post) for post in reversed(posts)) + text[first:]
    else:
        inserted = len(posts)
        label = f'{prefix}: {term}' if prefix else term
        h1 = f'{emoji} {term}' if emoji else label
        text = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons&display=swap"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 {len(posts)} 篇文章</p>{''.join(tax_item(post) for post in reversed(posts))}</div></div></div><script src="/js/journal.js"></script></body></html>'''
    write(path, text)
    update_term_index(kind, term, inserted)


def update_taxonomies() -> None:
    groups: dict[tuple[str, str, str, str], list[dict]] = {}
    for post in POSTS:
        groups.setdefault(('categories', post['category'], '分类', ''), []).append(post)
        groups.setdefault(('series', post['series'], '', '📚'), []).append(post)
        for tag in post['tags']:
            groups.setdefault(('tags', tag, '标签', '🏷️'), []).append(post)
    for (kind, term, prefix, emoji), posts in groups.items():
        update_term(kind, term, prefix, emoji, posts)


def validate() -> None:
    failures = []
    forbidden = ['B站', 'bilibili', '哔哩', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主', '这期', '本期', '作者说', '他提到', '观看', '点赞', '订阅', '欢迎来到', '感谢你看到', '下期再见', '一键三连', '投币']
    for post in POSTS:
        article = (ROOT / post['url'].strip('/') / 'index.html').read_text(encoding='utf-8')
        for word in forbidden:
            if word in article:
                failures.append(f'{post["slug"]} forbidden {word}')
        for must in [post['title'], *post['must']]:
            if must not in article:
                failures.append(f'{post["slug"]} missing {must}')
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        toc = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != toc:
            failures.append(f'{post["slug"]} toc mismatch')
    home = (ROOT / 'index.html').read_text(encoding='utf-8')
    order = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)[:8]
    expected = PINNED + [post['url'] for post in reversed(POSTS)] + [PREV_ORIGINAL_URL]
    if order != expected:
        failures.append(f'home order mismatch {order}')
    ET.parse(ROOT / 'index.xml')
    previous = (ROOT / PREV_ORIGINAL_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    if POSTS[0]['url'] not in previous:
        failures.append('previous newer link missing')
    for i, post in enumerate(POSTS):
        text = (ROOT / post['url'].strip('/') / 'index.html').read_text(encoding='utf-8')
        if i < len(POSTS) - 1 and POSTS[i + 1]['url'] not in text:
            failures.append(f'{post["slug"]} newer missing')
        if i > 0 and POSTS[i - 1]['url'] not in text:
            failures.append(f'{post["slug"]} older missing')
        for rel in ['archive/index.html', f'categories/{post["category"]}/index.html', f'series/{post["series"]}/index.html', f'tags/{post["tags"][0]}/index.html']:
            path = ROOT / rel
            if not path.exists():
                failures.append(f'missing {rel}')
            elif post['url'] not in path.read_text(encoding='utf-8'):
                failures.append(f'{rel} missing {post["url"]}')
        cover = ROOT / post['cover'].strip('/')
        if not cover.exists() or cover.stat().st_size < 1000:
            failures.append(f'bad cover {post["slug"]}')
        else:
            ET.parse(cover)
    if failures:
        raise SystemExit('\n'.join(failures))
    print(json.dumps({'validation': 'passed', 'articles': len(POSTS), 'home_top': order}, ensure_ascii=False, indent=2))


def publish_changed_list() -> None:
    rec(ROOT / SCRIPT_REL)
    all_changed = sorted(CHANGED | {SCRIPT_REL, CHANGED_REL})
    write(ROOT / CHANGED_REL, json.dumps(all_changed, ensure_ascii=False, indent=2))
    print(json.dumps({'changed': len(all_changed), 'urls': [SITE + post['url'] for post in POSTS]}, ensure_ascii=False, indent=2))


def main() -> None:
    prepare_posts()
    for i, post in enumerate(POSTS):
        write(ROOT / post['cover'].strip('/'), cover_svg(post, i))
    for i, post in enumerate(POSTS):
        prev_url = PREV_ORIGINAL_URL if i == 0 else POSTS[i - 1]['url']
        prev_title = PREV_ORIGINAL_TITLE if i == 0 else POSTS[i - 1]['title']
        next_url = POSTS[i + 1]['url'] if i < len(POSTS) - 1 else None
        next_title = POSTS[i + 1]['title'] if i < len(POSTS) - 1 else None
        build_article(post, prev_url, prev_title, next_url, next_title)
    update_original_prev(POSTS[0]['url'], POSTS[0]['title'])
    update_home()
    update_rss()
    update_archive()
    update_taxonomies()
    validate()
    publish_changed_list()


if __name__ == '__main__':
    main()
