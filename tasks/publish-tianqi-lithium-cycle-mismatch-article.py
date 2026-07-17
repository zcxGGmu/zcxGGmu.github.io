from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path('/tmp/hermes-video-publish')
SITE = 'https://zcxggmu.github.io'
SLUG = 'tianqi-lithium-raw-material-price-mismatch-cycle-rebound'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = SITE + URL_PATH
TITLE = '天齐锂业的周期错配：原料自给为何仍被利润挤压'
DESC = 'Greenbushes 带来深厚资源壁垒，但 SC6 原料涨幅跑赢锂化工产品，叠加澳洲矿山定价、权利金和税费机制，解释了天齐锂业短期利润承压与 2026 修复逻辑。'
DATE = '2026-07-17'
PUB_DT = datetime(2026, 7, 17, 18, 5, tzinfo=timezone(timedelta(hours=8)))
CATEGORY = '投资研究'
SERIES = '锂电产业链'
TAGS = ['天齐锂业', '锂', '锂矿', '锂电产业链', 'Greenbushes', 'SC6', '电动车', '储能', '周期反弹', '资源股', '资本开支', '瑞银']
MINUTES = 8
COVER = f'/images/posts/{SLUG}/cover.svg'
PREV_URL = '/2026/china-innovative-drug-2026h1-policy-earnings-valuation-bottom/'
PREV_TITLE = '中国创新药 2026 半年复盘：政策底、业绩底与估值底'
ARTICLE = Path('/tmp/bv1xxkj6felf/article.html').read_text(encoding='utf-8')
CHANGED: set[str] = set()

def esc(s: str) -> str:
    return html.escape(s, quote=True)

def rec(path: Path) -> None:
    CHANGED.add(path.relative_to(ROOT).as_posix())

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
    rec(path)

def term_url(kind: str, term: str) -> str:
    return f'/{kind}/{quote(term)}/'

def meta_links() -> str:
    cat = f'<a href="{term_url("categories", CATEGORY)}">{esc(CATEGORY)}</a>'
    tags = '&nbsp;'.join(f'<a href="{term_url("tags", tag)}">{esc(tag)}</a>' for tag in TAGS)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {MINUTES} min'

def build_toc() -> str:
    links = [f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>' for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', ARTICLE)]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + ''.join(links) + '</nav></div></div>'

def cover_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#102a43"/><stop offset="0.5" stop-color="#0f766e"/><stop offset="1" stop-color="#a16207"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="16" flood-color="#000" flood-opacity="0.32"/></filter></defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#d9f99d" stroke-width="4"><path d="M120 690 H1480"/><path d="M120 570 H1480"/><path d="M120 450 H1480"/><path d="M120 330 H1480"/><path d="M320 250 V750"/><path d="M620 250 V750"/><path d="M920 250 V750"/><path d="M1220 250 V750"/></g>
  <g filter="url(#shadow)"><path d="M210 655 C365 545 500 620 650 500 C800 380 960 475 1110 350 C1235 245 1355 260 1480 185" fill="none" stroke="#bef264" stroke-width="16" stroke-linecap="round"/><rect x="260" y="555" width="280" height="110" rx="22" fill="#ecfeff"/><text x="300" y="625" fill="#0f766e" font-family="JetBrains Mono, Arial" font-size="44" font-weight="800">SC6</text><circle cx="1110" cy="350" r="46" fill="#fde047"/><circle cx="1480" cy="185" r="54" fill="#fb923c"/></g>
  <text x="96" y="154" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="64" font-weight="800">天齐锂业的周期错配</text>
  <text x="100" y="236" fill="#d9f99d" font-family="Noto Sans SC, PingFang SC, Arial" font-size="39" font-weight="700">原料自给 · 价格错配 · V 型修复</text>
  <text x="102" y="310" fill="#e0f2fe" font-family="Noto Sans SC, PingFang SC, Arial" font-size="31" font-weight="600">护城河不是免疫周期，而是改变承压方式</text>
</svg>'''

def build_article() -> None:
    template = (ROOT / PREV_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    start = template.find('<article class="post">')
    end = template.find('</article>', start) + len('</article>')
    head, tail = template[:start], template[end:]
    replacements = {
        r'<title>.*?</title>': f'<title>{esc(TITLE)} - zcxGGmu\'s Blog</title>',
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(DESC)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(FULL_URL)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(TITLE)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(DESC)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(FULL_URL)}">',
    }
    for pattern, repl in replacements.items():
        head = re.sub(pattern, repl, head, flags=re.S)
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{COVER}')"><div class="post-title">{esc(TITLE)}<div class="post-subtitle">{esc(DESC)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links()}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{ARTICLE}</div></div><nav class="post-pagination"><a class="newer-posts">下一篇<br>没有更新的文章</a><a class="older-posts" href="{PREV_URL}">上一篇<br>{esc(PREV_TITLE)}</a></nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(), tail, flags=re.S)
    write(ROOT / '2026' / SLUG / 'index.html', head + article + tail)

def update_prev() -> None:
    path = ROOT / PREV_URL.strip('/') / 'index.html'
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'<a class="newer-posts">下一篇<br>没有更新的文章</a>', f'<a class="newer-posts" href="{URL_PATH}">下一篇<br>{esc(TITLE)}</a>', text, count=1)
    write(path, text)

def home_card() -> str:
    return f'''<a href="{URL_PATH}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(TITLE)}</div>
            <div class="post-item-summary">{esc(DESC)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {MINUTES} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{COVER}')"></div></div>
        </div>
      </div>
    </a>'''

def update_home() -> None:
    path = ROOT / 'index.html'
    text = path.read_text(encoding='utf-8')
    text = re.sub(rf'<a href="{re.escape(URL_PATH)}" class="a-block">.*?</a>\s*', '', text, flags=re.S)
    pos = text.find(f'<a href="{PREV_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError('homepage insertion marker not found')
    write(path, text[:pos] + home_card() + '\n' + text[pos:])

def update_rss() -> None:
    path = ROOT / 'index.xml'
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{format_datetime(PUB_DT)}</lastBuildDate>', text)
    text = re.sub(rf'<item>\s*<title>{re.escape(esc(TITLE))}</title>.*?</item>\s*', '', text, flags=re.S)
    item = f'''<item>
<title>{esc(TITLE)}</title>
<link>{FULL_URL}</link>
<guid>{FULL_URL}</guid>
<pubDate>{format_datetime(PUB_DT)}</pubDate>
<description>{esc(DESC)}</description>
</item>
'''
    write(path, text.replace('<item>', item + '<item>', 1))

def update_archive() -> None:
    path = ROOT / 'archive/index.html'
    text = path.read_text(encoding='utf-8')
    is_new = URL_PATH not in text
    if is_new:
        text = re.sub(r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>', lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + 1} 篇</span>', text, count=1)
    item = f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{URL_PATH}">{esc(TITLE)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(CATEGORY)}</span></span>
      </div> '''
    pos = text.find(f'<a href="{PREV_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    write(path, text[:start] + item + text[start:])

def tax_item() -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''

def update_term_index(kind: str, term: str, delta: int) -> None:
    if not delta:
        return
    path = ROOT / kind / 'index.html'
    if not path.exists():
        return
    text = path.read_text(encoding='utf-8')
    href = f'/{kind}/{quote(term)}/'
    if href in text:
        pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span style="color:#999[^>]*>\()(\d+)(\)</span></a>)')
        text = pattern.sub(lambda m: f'{m.group(1)}{int(m.group(2)) + delta}{m.group(3)}', text, count=1)
    else:
        if kind == 'tags':
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">(1)</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">(1)</span></a>\n'
        pos = text.find('</div></div></div>')
        text = text[:pos] + item + text[pos:]
    write(path, text)

def update_term(kind: str, term: str, prefix: str, emoji: str) -> None:
    path = ROOT / kind / term / 'index.html'
    inserted = 1
    if path.exists():
        text = path.read_text(encoding='utf-8')
        inserted = 0 if URL_PATH in text else 1
        if inserted:
            text = re.sub(r'共 (\d+) 篇文章', lambda m: f'共 {int(m.group(1)) + 1} 篇文章', text, count=1)
        first = text.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
        if first == -1:
            first = text.find('</div></div></div>')
        text = text[:first] + tax_item() + text[first:]
    else:
        label = f'{prefix}: {term}' if prefix else term
        h1 = f'{emoji} {term}' if emoji else label
        text = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p>{tax_item()}</div></div></div><script src="/js/journal.js"></script></body></html>'''
    write(path, text)
    update_term_index(kind, term, inserted)

def update_tax() -> None:
    update_term('categories', CATEGORY, '分类', '')
    update_term('series', SERIES, '', '📚')
    for tag in TAGS:
        update_term('tags', tag, '标签', '🏷️')

def validate() -> None:
    failures = []
    article = (ROOT / URL_PATH.strip('/') / 'index.html').read_text(encoding='utf-8')
    forbidden = ['B站', 'bilibili', '哔哩', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主', '这期', '本期', '作者说', '他提到', '观看', '点赞', '订阅', '欢迎回到', '下集见', '播客']
    for word in forbidden:
        if word in article:
            failures.append(f'forbidden {word}')
    for must in [TITLE, '天齐锂业', 'Greenbushes', 'SC6', '22%', '14%', '28.5 亿至 42.5 亿元', '93.18 元']:
        if must not in article:
            failures.append(f'missing {must}')
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links:
        failures.append('toc mismatch')
    home = (ROOT / 'index.html').read_text(encoding='utf-8')
    order = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)[:7]
    expected = ['/2026/codeinsights-local-first-agent-workbench/', '/2026/what-you-need-to-learn-from-claw-code-repo/', '/2026/gaojingqi-investment-system/', '/2026/ai-revolution-permanent-underclass-career-selection/', '/2026/live-longer-than-earn-fast-investment-infinite-game/', URL_PATH, PREV_URL]
    if order != expected:
        failures.append(f'home order {order}')
    prev = (ROOT / PREV_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    if URL_PATH not in prev:
        failures.append('previous article newer link missing')
    ET.parse(ROOT / 'index.xml')
    for path in [ROOT / URL_PATH.strip('/') / 'index.html', ROOT / 'images/posts' / SLUG / 'cover.svg', ROOT / 'archive/index.html', ROOT / 'categories' / CATEGORY / 'index.html', ROOT / 'series' / SERIES / 'index.html']:
        if not path.exists():
            failures.append(f'missing {path}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print('validation passed')

def main() -> None:
    write(ROOT / 'images/posts' / SLUG / 'cover.svg', cover_svg())
    build_article()
    update_prev()
    update_home()
    update_rss()
    update_archive()
    update_tax()
    validate()
    changed_path = ROOT / 'tasks/publish-tianqi-lithium-cycle-mismatch-changed-files.json'
    all_changed = sorted(CHANGED | {'tasks/publish-tianqi-lithium-cycle-mismatch-article.py'})
    write(changed_path, json.dumps(all_changed, ensure_ascii=False, indent=2))
    print(json.dumps({'url': FULL_URL, 'changed': len(all_changed)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
