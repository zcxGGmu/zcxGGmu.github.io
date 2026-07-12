from pathlib import Path
from urllib.parse import quote
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
import html
import re
import xml.etree.ElementTree as ET

ROOT = Path('/tmp/hermes-video-publish')
SLUG = 'labor-alienation-human-nature-abstract-work'
URL_PATH = f'/2026/{SLUG}/'
FULL_URL = 'https://zcxggmu.github.io' + URL_PATH
TITLE = '劳动为什么从人的天性变成了强制'
DESC = '从泰勒制、动作分析、流水线、抽象劳动与具体劳动的冲突，到马克思关于异化劳动的判断，理解现代人为什么会像躲避瘟疫一样躲避劳动。'
DATE = '2026-07-12'
PUB_DT = datetime(2026, 7, 12, 22, 8, tzinfo=timezone(timedelta(hours=8)))
PUB_RSS = format_datetime(PUB_DT)
CATEGORY = '思想'
SERIES = '社会理论'
TAGS = ['劳动', '异化劳动', '马克思', '泰勒制', '抽象劳动', '具体劳动', '流水线', '资本主义', '管理科学', '王德峰']
READING_MIN = 8
COVER = f'/images/posts/{SLUG}/cover.svg'
OLDER_URL = '/2026/basic-materials-2026h1-earnings-value-revaluation/'
OLDER_TITLE = '基础材料板块价值重估：铜、黄金、铝、锂的半年报主线'

ARTICLE_HTML = r'''
<p>劳动本来应当是人的第一需要。人有双腿就要行走，有四肢就要活动，有头脑就要思考；如果不让人走路、不让人学习、不让人把自己的体力和智力发挥出来，那就是对人的压抑。人之所以能把自己同动物区分开来，根本处就在于劳动：通过劳动，人把自己的能力、理解、想象和创造注入世界。</p>

<p>可是现代社会里，人们又如此厌恶劳动。只要肉体的强制、制度的强制、生活压力的强制一停止，人们往往会像躲避瘟疫一样躲避劳动。问题不在于人天生懒惰，而在于现代生产方式改变了劳动的性质：劳动不再首先是人的自我实现，而变成了外在于人的强制活动。</p>

<h2 id="taylorism">一、泰勒制从提高效率开始，也从剥离个性开始</h2>

<p>现代管理科学的一个标志性人物是泰勒。泰勒制最早关心的问题，是如何提高劳动效率。提高效率的第一步，就是提高劳动者的熟练程度；提高熟练程度，就要研究劳动过程中哪些动作是必要的，哪些动作是多余的。</p>

<p>在摄影技术可以应用之后，这件事情就变得更容易。把熟练工人的劳动过程拍下来，再把不够熟练的劳动者的劳动过程拍下来，两相比较，就会发现后者有许多“多余动作”。管理科学的任务，就是把这些多余动作清理掉，让劳动过程更标准、更快、更可复制。</p>

<p>从效率角度看，这当然有效。可是问题也恰恰从这里出现：所谓多余动作，未必真的多余。它们可能正是具体劳动中人的个性、节奏、手艺和乐趣所在。</p>

<h2 id="tailor-wife">二、所谓“多余动作”，可能正是劳动的全部乐趣</h2>

<p>泰勒制的荒诞性，可以通过一个很有意味的例子看出来。一个擅长动作分析的人回家观察妻子织毛衣，发现她在织毛衣时有大量动作并不符合效率原则，于是告诉她：你之所以花这么多时间，是因为大约 80% 的动作都是多余的。</p>

<p>可是对织毛衣的人来说，那些被效率标准判定为“多余”的动作，恰恰可能就是织毛衣的全部乐趣。手的停顿、眼睛的观察、节奏的变化、身体和材料之间的配合，并不只是完成一个结果的手段。它们构成了劳动作为具体活动的感性内容。</p>

<p>当管理科学只问“怎样更快”，它就会把劳动中不合效率的部分都视为浪费。但对劳动者本人而言，劳动并不只是产出一个对象，更是体力、智力、手艺、判断和个性的展开。把这些东西清洗掉，劳动就变成了只剩下技术流程的空壳。</p>

<h2 id="abstract-concrete">三、抽象劳动压倒具体劳动，劳动就不再属于劳动者</h2>

<p>资本主义生产方式中的劳动，有一个根本变化：为了提高抽象劳动意义上的效率，具体劳动必须不断减少自己的个性特征。手艺的要素被清理，人的节奏被压低，剩下的是可计算、可比较、可替换的技术流程。</p>

<p>具体劳动是有感性内容的劳动。它带着个人的熟练程度、身体习惯、判断力、创造性和情绪投入。抽象劳动则把这些差异抹平，只留下可以计量的劳动时间、劳动强度和劳动效率。现代生产越追求抽象效率，就越要压制具体劳动的丰富性。</p>

<p>当劳动被抽象劳动统治时，每一种劳动表面上仍然是劳动者在做，实际上却越来越不属于劳动者本人。劳动者只是按照外部规定的节奏、标准和目标执行动作。劳动不再是人的自我表达，而是外在于人的活动。</p>

<h2 id="machine-line">四、机器和流水线把人变成系统的附属物</h2>

<p>当手艺被技术替代到一定程度，下一步就是机器替代人手。工人不再是劳动过程的主人，而是在机器旁边成为机器系统的协助者、看守者或补充部件。流水线就是这种变化的集中表现。</p>

<p>流水线的残酷之处在于，它以一个高速度、强节奏、不可由个人决定的方式向前推进。人在它旁边工作，必须在固定速度下机械地完成所有必要动作。劳动者的身体不再按照自己的节奏活动，而是被生产线的节奏牵引。</p>

<p>在这种状态下，最大的“幸福”甚至可能只是流水线上有一个零件掉下来，工人弯腰去捡一下。因为那一瞬间，他终于从机械重复中获得了一点点偏离。一个人竟然会把弯腰捡零件当成喘息，这就说明劳动已经不再是自由活动，而是压迫性的重复。</p>

<h2 id="sweatshop">五、血汗工厂的本质，是劳动变成自我折磨</h2>

<p>所谓血汗工厂，并不只是工资低、时间长、条件差。更深层的问题，是劳动在这种生产方式中变成了自我牺牲和自我折磨。劳动者在劳动中不是肯定自己，而是否定自己；不是感到幸福，而是感到不幸；不是自由发挥体力和智力，而是肉体受折磨、精神受摧残。</p>

<p>马克思关于异化劳动的判断非常准确：工人只有在劳动之外才感到自在，在劳动中反而感到不自在；不劳动时觉得舒畅，劳动时反而不舒畅。因此，这种劳动不是自愿劳动，而是被迫的强制劳动。</p>

<p>劳动一旦变成这种状态，就不再是满足人的需要，而只是满足劳动以外那些需要的一种手段。人不是因为劳动本身而劳动，而是为了工资、生活、身份、安全感和外部压力而劳动。劳动的意义被转移到了劳动之外。</p>

<h2 id="alienated-labor">六、异化劳动的标志，是强制一停止就想逃离</h2>

<p>异化劳动最清楚的标志，就是强制一停止，人立刻想逃离劳动。如果劳动本身是人的自我实现，那么人会在劳动中找到自己的力量、对象和创造性；但如果劳动只是外部强加的负担，那么人自然会像躲避痛苦一样躲避它。</p>

<p>这不是道德问题，不是简单的“现在的人吃不了苦”。现代人厌恶劳动，是因为大量劳动已经被组织成外在的、重复的、抽象的、压迫性的活动。人在其中不能成为自己，只能把自己交给流程、指标、时间表和管理系统。</p>

<p>因此，劳动的异化不是劳动本身造成的，而是特定生产方式造成的。劳动作为人的本质活动，本应让人确认自己；异化劳动却让人在劳动中失去自己。</p>

<h2 id="labor-nature">七、劳动本是人的第一需要，这不是幻想</h2>

<p>说劳动是人的第一需要，并不是浪漫幻想。一个人有身体，就需要活动；有能力，就需要发挥；有头脑，就需要理解和创造。完全禁止一个人行动、学习、思考和创造，必然是一种迫害。</p>

<p>儿童对劳动常常有天然的兴趣，正说明劳动本身符合人的本性。孩子看到成年人做事，会想试一试。他并不是先把劳动理解成谋生手段，而是把它理解成一种能让自己参与世界的活动。刷墙、搬东西、做手工、模仿大人的动作，都可能带来快乐。</p>

<p>这种快乐来自活动本身：身体在运动，感官在参与，头脑在判断，手在改变材料，世界因为自己的动作发生变化。劳动的原初意义，就在这种创造性和参与感里。</p>

<h2 id="paint-story">八、刷油漆的故事：劳动为什么会吸引人</h2>

<p>一个孩子被父亲要求给很长的篱笆刷油漆。起初他还觉得开心，可很快发现工作量太大，今天明天都做不完，于是开始想办法。邻居家的孩子过来看他在干什么，他便故意把刷油漆表现得很有趣：刷一下，左右看看，笑一笑，再继续刷，仿佛这是一件特别值得参与的事情。</p>

<p>邻居家的孩子被吸引了，也想来刷。于是原本承担任务的孩子提出交换：你想刷也可以，把手里的苹果给我。对方答应了，把苹果交出来，自己开始刷油漆，而且一开始也刷得很开心。</p>

<p>这个故事说明，劳动之所以能吸引人，是因为它可以表现为一种创造性活动。它让人在活动中投入体力和智力，让人把自己的个性注入对象。哪怕只是刷油漆，只要它还保留游戏性、创造性和自主性，就可能成为乐趣。</p>

<h2 id="why-adults-hate-work">九、为什么长大后劳动变成了苦役</h2>

<p>小时候看到成年人劳动，常常也想试试；长大后才知道，许多劳动只剩下苦役。这种转变不是因为劳动本身变坏了，而是因为劳动被纳入了抽象劳动统治的体系。</p>

<p>在这个体系中，劳动被计量、被切割、被标准化、被加速。个体的节奏、手艺和创造性被当成效率障碍。劳动者不再拥有劳动过程，不再拥有劳动节奏，也不再拥有劳动目的。他只是把自己的时间和身体交给一个外在系统。</p>

<p>于是，劳动从人的第一需要变成了谋生压力；从自我实现变成了外在强制；从创造活动变成了重复动作。现代人不是厌恶劳动本身，而是厌恶这种被剥夺了主体性的劳动形式。</p>

<h2 id="conclusion">十、重新理解劳动：问题不在劳动，而在劳动怎样被组织</h2>

<p>劳动本身并不必然痛苦。真正令人痛苦的，是劳动被组织成外在的、强制的、抽象的效率过程。泰勒制、动作分析、流水线和机器体系所追求的，是去掉多余动作、压低个人差异、提高可计算效率；但被清洗掉的，往往正是劳动的乐趣、手艺、个性和人的自我确认。</p>

<p>因此，现代人厌恶劳动，并不能简单归结为懒惰或意志薄弱。更根本的问题是：劳动在何种制度和生产方式中发生？劳动者是否能在劳动中肯定自己？劳动是否还能容纳创造、节奏、判断和个性？</p>

<p>当劳动重新成为人的能力展开，而不是外在系统对人的支配，劳动才可能回到它原本的位置：不是折磨人的苦役，而是人把自己对象化、把世界改造出来、并在其中确认自身存在的活动。</p>
'''


def esc(s):
    return html.escape(s, quote=True)


def term_url(kind, term):
    return f'/{kind}/{quote(term)}/'


def meta_links():
    cat = f'<a href="{term_url("categories", CATEGORY)}">{esc(CATEGORY)}</a>'
    tag_links = '&nbsp;'.join(f'<a href="{term_url("tags", t)}">{esc(t)}</a>' for t in TAGS)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tag_links}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {READING_MIN} min'


def build_toc(body):
    links = []
    for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body):
        links.append(f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>')
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + ''.join(links) + '</nav></div></div>'


def make_cover():
    d = ROOT / 'images/posts' / SLUG
    d.mkdir(parents=True, exist_ok=True)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#111827"/>
      <stop offset="0.55" stop-color="#4b5563"/>
      <stop offset="1" stop-color="#f97316"/>
    </linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#000" flood-opacity="0.35"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.18" stroke="#fff" stroke-width="3">
    <path d="M0 690H1600"/><path d="M0 590H1600"/><path d="M0 490H1600"/>
    <path d="M250 290v470"/><path d="M520 250v510"/><path d="M790 215v545"/><path d="M1060 250v510"/><path d="M1330 290v470"/>
  </g>
  <g filter="url(#shadow)">
    <rect x="260" y="420" width="1080" height="86" rx="18" fill="#1f2937"/>
    <rect x="260" y="548" width="1080" height="86" rx="18" fill="#1f2937"/>
    <rect x="260" y="676" width="1080" height="86" rx="18" fill="#1f2937"/>
    <circle cx="390" cy="462" r="48" fill="#fbbf24"/>
    <circle cx="675" cy="590" r="48" fill="#fbbf24"/>
    <circle cx="960" cy="718" r="48" fill="#fbbf24"/>
    <path d="M390 462H1260M675 590H1260M960 718H1260" stroke="#fb923c" stroke-width="18" stroke-linecap="round"/>
  </g>
  <g fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial">
    <text x="110" y="160" font-size="70" font-weight="800">劳动为什么从人的天性</text>
    <text x="110" y="250" font-size="70" font-weight="800">变成了强制</text>
    <text x="116" y="325" font-size="34" font-weight="700" fill="#fed7aa">泰勒制 · 流水线 · 抽象劳动 · 异化劳动</text>
  </g>
  <g fill="#111827" font-family="Noto Sans SC, PingFang SC, Arial" font-size="28" font-weight="800">
    <text x="344" y="472">动作</text>
    <text x="629" y="600">效率</text>
    <text x="914" y="728">异化</text>
  </g>
</svg>'''
    (d / 'cover.svg').write_text(svg, encoding='utf-8')


def build_article_page():
    template = (ROOT / OLDER_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    head = template[:template.find('<article class="post">')]
    tail = template[template.find('</article>', template.find('<article class="post">')) + len('</article>'):]
    head = re.sub(r'<title>.*?</title>', f"<title>{esc(TITLE)} - zcxGGmu's Blog</title>", head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(DESC)}">', head)
    head = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{esc(FULL_URL)}">', head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(TITLE)}">', head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(DESC)}">', head)
    head = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{esc(FULL_URL)}">', head)
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{COVER}')"><div class="post-title">{esc(TITLE)}<div class="post-subtitle">{esc(DESC)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links()}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{ARTICLE_HTML}</div></div><nav class="post-pagination"><a class="newer-posts">下一篇<br>没有更新的文章</a><a class="older-posts" href="{OLDER_URL}">上一篇<br>{esc(OLDER_TITLE)}</a></nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(ARTICLE_HTML), tail, flags=re.S)
    out = ROOT / '2026' / SLUG / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head + article + tail, encoding='utf-8')
    older = ROOT / OLDER_URL.strip('/') / 'index.html'
    txt = older.read_text(encoding='utf-8')
    txt = re.sub(r'<a class="newer-posts">下一篇<br>没有更新的文章</a>', f'<a class="newer-posts" href="{URL_PATH}">下一篇<br>{esc(TITLE)}</a>', txt)
    older.write_text(txt, encoding='utf-8')


def home_card(url, title, desc, cover, minutes):
    return f'''<a href="{url}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(title)}</div>
            <div class="post-item-summary">{esc(desc)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {minutes} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{cover}')"></div></div>
        </div>
      </div>
    </a>'''


def update_home():
    p = ROOT / 'index.html'
    txt = p.read_text(encoding='utf-8')
    if URL_PATH not in txt:
        marker = f'<a href="{OLDER_URL}" class="a-block">'
        pos = txt.find(marker)
        if pos == -1:
            raise RuntimeError('older homepage marker not found')
        txt = txt[:pos] + home_card(URL_PATH, TITLE, DESC, COVER, READING_MIN) + '\n' + txt[pos:]
    p.write_text(txt, encoding='utf-8')


def update_rss():
    p = ROOT / 'index.xml'
    txt = p.read_text(encoding='utf-8')
    txt = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{PUB_RSS}</lastBuildDate>', txt)
    item = f'''<item>
<title>{esc(TITLE)}</title>
<link>{FULL_URL}</link>
<guid>{FULL_URL}</guid>
<pubDate>{PUB_RSS}</pubDate>
<description>{esc(DESC)}</description>
</item>
'''
    if FULL_URL not in txt:
        txt = txt.replace('<item>', item + '<item>', 1)
    p.write_text(txt, encoding='utf-8')


def update_archive():
    p = ROOT / 'archive/index.html'
    txt = p.read_text(encoding='utf-8')
    if URL_PATH not in txt:
        txt = re.sub(r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>', lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + 1} 篇</span>', txt, count=1)
        item = f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{URL_PATH}">{esc(TITLE)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(CATEGORY)}</span></span>
      </div> '''
        marker = f'<div style="padding:8px 0;font-size:15px">\n        <span style="color:#999">2026-07-12</span>&nbsp;\n        <a href="{OLDER_URL}">'
        pos = txt.find(marker)
        if pos == -1:
            raise RuntimeError('archive marker not found')
        txt = txt[:pos] + item + txt[pos:]
    p.write_text(txt, encoding='utf-8')


def list_page(kind, term, title_prefix=None, emoji=''):
    d = ROOT / kind / term
    d.mkdir(parents=True, exist_ok=True)
    p = d / 'index.html'
    if p.exists():
        txt = p.read_text(encoding='utf-8')
        if URL_PATH not in txt:
            txt = re.sub(r'共 (\d+) 篇文章', lambda m: f'共 {int(m.group(1)) + 1} 篇文章', txt, count=1)
            item = f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''
            insert = txt.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
            if insert == -1:
                insert = txt.find('</div></div></div>')
            txt = txt[:insert] + item + txt[insert:]
        p.write_text(txt, encoding='utf-8')
        return
    label = f'{title_prefix}: {term}' if title_prefix else term
    h1 = f'{emoji} {term}' if emoji else label
    txt = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="https://zcxggmu.github.io/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Noto+Sans+SC:wght@400;500;700&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons&amp;display=swap"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p><div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL_PATH}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> </div></div></div><script src="/js/journal.js"></script></body></html>'''
    p.write_text(txt, encoding='utf-8')


def update_index_count(kind, term):
    p = ROOT / kind / 'index.html'
    if not p.exists():
        return
    txt = p.read_text(encoding='utf-8')
    href = f'/{kind}/{quote(term)}/'
    if href in txt:
        pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(term)}<span style="color:#999[^>]*>\()(\d+)(\)</span></a>)')
        txt = pattern.sub(lambda m: f'{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}', txt, count=1)
    else:
        if kind == 'tags':
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">(1)</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">(1)</span></a>\n'
        marker = '</div></div></div>'
        pos = txt.find(marker)
        if pos == -1:
            raise RuntimeError(f'{kind} index insertion marker not found')
        txt = txt[:pos] + item + txt[pos:]
    p.write_text(txt, encoding='utf-8')


def update_taxonomy():
    list_page('categories', CATEGORY, '分类')
    update_index_count('categories', CATEGORY)
    list_page('series', SERIES, None, '📚')
    update_index_count('series', SERIES)
    for tag in TAGS:
        list_page('tags', tag, '标签', '🏷️')
        update_index_count('tags', tag)


def validate():
    failures = []
    article = ROOT / '2026' / SLUG / 'index.html'
    txt = article.read_text(encoding='utf-8')
    forbidden = ['B站', 'bilibili', '视频里', '视频中', '原视频', '音频里', '音频中', 'UP主', 'up主', '这期', '本期', '作者说', '他提到', '观看', '点赞', '下期', '欢迎收看', '感谢', '订阅', '老铁', '所长']
    for w in forbidden:
        if w in txt:
            failures.append(f'forbidden word in article: {w}')
    for concept in ['泰勒制', '抽象劳动', '具体劳动', '流水线', '马克思', '异化劳动', '刷油漆', '人的第一需要']:
        if concept not in txt:
            failures.append(f'missing concept: {concept}')
    for p in [article, ROOT / 'index.html', ROOT / 'index.xml', ROOT / 'archive/index.html', ROOT / 'categories' / CATEGORY / 'index.html', ROOT / 'series' / SERIES / 'index.html']:
        if not p.exists():
            failures.append(f'missing {p}')
    home = (ROOT / 'index.html').read_text(encoding='utf-8')
    links = re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">', home)
    expected = ['/2026/codeinsights-local-first-agent-workbench/', '/2026/what-you-need-to-learn-from-claw-code-repo/', '/2026/gaojingqi-investment-system/', '/2026/ai-revolution-permanent-underclass-career-selection/', '/2026/live-longer-than-earn-fast-investment-infinite-game/', URL_PATH, OLDER_URL]
    if links[:7] != expected:
        failures.append(f'homepage order mismatch: {links[:7]}')
    older = (ROOT / OLDER_URL.strip('/') / 'index.html').read_text(encoding='utf-8')
    if f'href="{URL_PATH}"' not in older:
        failures.append('older article does not link to new article')
    try:
        ET.parse(ROOT / 'index.xml')
    except Exception as e:
        failures.append(f'rss xml parse failed: {e}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print('validation passed')


def main():
    make_cover()
    build_article_page()
    update_home()
    update_rss()
    update_archive()
    update_taxonomy()
    validate()
    print('published local files for', FULL_URL)


if __name__ == '__main__':
    main()
