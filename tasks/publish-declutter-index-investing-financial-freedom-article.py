#!/usr/bin/env python3
"""Validation helper for the declutter/index-investing financial freedom article.

The article files are static HTML generated during the publish workflow. This helper
keeps the key publishing invariants auditable after generation.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'declutter-index-investing-financial-freedom-at-33'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
OLDER_URL = '/2026/gold-silver-multimonth-rally-secular-bull-market/'
TITLE = '不看盘反而赚更多：从一万件囤积物到 33 岁财务自由'
FORBIDDEN = [
    'B站', 'bilibili', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主',
    '这期', '本期', '作者说', '他提到', '观看', '点赞', '下期', '欢迎收看', '感谢',
    '订阅', '老铁', '所长', 'Mani', '小燕', '理财资优生'
]
KEY_FILES = [
    f'2026/{SLUG}/index.html',
    f'images/posts/{SLUG}/cover.svg',
    'index.html',
    'index.xml',
    'archive/index.html',
    'categories/个人财务/index.html',
    'series/财务自由/index.html',
    'tags/财务自由/index.html',
    'tags/指数化投资/index.html',
    'tags/断舍离/index.html',
]


def main() -> None:
    failures = []
    for rel in KEY_FILES:
        if not (ROOT / rel).exists():
            failures.append(f'missing {rel}')
    article_path = ROOT / '2026' / SLUG / 'index.html'
    article = article_path.read_text(encoding='utf-8')
    for word in FORBIDDEN:
        if word in article:
            failures.append(f'forbidden article wording: {word}')
    for concept in ['补偿性消费', '金钱脚本', '指数化投资', '33 岁财务自由', '被动收入大于支出']:
        if concept not in article:
            failures.append(f'missing article concept: {concept}')
    home = (ROOT / 'index.html').read_text(encoding='utf-8')
    links = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)
    expected = [
        '/2026/codeinsights-local-first-agent-workbench/',
        '/2026/what-you-need-to-learn-from-claw-code-repo/',
        '/2026/gaojingqi-investment-system/',
        '/2026/ai-revolution-permanent-underclass-career-selection/',
        '/2026/live-longer-than-earn-fast-investment-infinite-game/',
        URL_PATH,
        OLDER_URL,
    ]
    if links[:7] != expected:
        failures.append(f'homepage order mismatch: {links[:7]}')
    rss = (ROOT / 'index.xml').read_text(encoding='utf-8')
    ET.fromstring(rss)
    if FULL_URL not in rss:
        failures.append('rss missing article url')
    if TITLE not in (ROOT / 'archive/index.html').read_text(encoding='utf-8'):
        failures.append('archive missing title')
    if failures:
        raise SystemExit('\n'.join(failures))
    print('validation passed')


if __name__ == '__main__':
    main()
