from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import quote

from pinned_home import insert_home_card_after_pinned


ROOT = Path("/tmp/hermes-video-publish")
SLUG = "modern-single-men-happiest-generation-solitude-freedom"
URL = f"/2026/{SLUG}/"
ASSET_DIR = f"/images/posts/{SLUG}"

TITLE = "现代单身男性为什么可能是最快乐的一代：独处、自由与内在秩序"
DESCRIPTION = "单身不是情感失败，而是把时间、金钱、注意力、身体和精神重新交还给自己。真正成熟的亲密关系必须是选择，而不是依赖、恐惧或社会时间表。"
DATE = "2026-07-19"
PUB_DATE = "Sun, 19 Jul 2026 21:10:00 +0800"
LAST_BUILD = "2026-07-19T21:10:00+08:00"
CATEGORY = "个人成长"
SERIES = "人生主线"
TAGS = ["单身", "独处", "亲密关系", "情绪稳定", "财务自由", "自律", "人生选择", "男性成长", "内在秩序", "生活方式"]

OLDER_URL = "/2026/bullshit-jobs-information-industry-power-order/"
OLDER_TITLE = "毫无意义的工作：信息业、权力扩张与世界的草台班子"

SCRIPT_NAME = "publish-modern-single-men-happiness-article.py"
MANIFEST_NAME = "publish-modern-single-men-happiness-changed-files.json"


SECTIONS = [
    (
        "awakening",
        "单身不是迷失，而是从幻象中清醒",
        [
            "现代男性正在重新理解一个长期被压低的事实：单身并不天然意味着失败、孤独或无人选择。很多时候，它意味着一个人终于从被制造出来的幻象里走出来，不再把亲密关系当成获得认可、证明价值和填补空洞的唯一方式。",
            "一个人独自生活时，会更容易看清社会给幸福套上的模板。外界总在暗示，人生必须按某条时间线推进：恋爱、结婚、买房、生育、供养、忍耐，仿佛只有被纳入某种固定关系，一个男人才算完整。但真正的平静并不来自别人是否停留在身边，而来自一个人是否能够掌控自己的内心秩序。",
            "这种平静不是逃避，也不是冷漠。它是一种清醒：不再为了迎合别人而牺牲生活节奏，不再把被需要误认为被爱，不再把持续消耗误认为深情。一个人一旦体会过独处的安宁，就很难再把混乱包装成浪漫。",
            "独处给予男性最直接的礼物，是时间、注意力和精神状态的重新归位。没有反复的情绪拉扯，没有无休止的试探，也不必时时猜测别人未说出口的期待。生活重新从他人的反应，回到自己的目标、秩序和行动。",
        ],
    ),
    (
        "relationship-risk",
        "亲密关系的风险，已经不能只用浪漫叙事解释",
        [
            "亲密关系本应让人变得更完整，但在很多现实处境里，它已经变成情绪风险、财务风险和声誉风险交织的雷区。一次误解、一次指责、一次失控的公开表达，都可能让一个人多年建立的稳定生活被拖入混乱。",
            "社交媒体让私人生活变得可以被围观、剪裁和消费。越是在情感与财务上暴露得毫无边界，一个人越容易被操控、羞辱或反复索取。对许多男性来说，选择保持距离并不是出于怨恨，而是出于风险意识。",
            "低质量关系中常见的一种失衡，是一方被期待持续提供稳定、资源、情绪价值和安全感，却很少得到同等的尊重、责任和反馈。一个人可以做对很多事，依然被判定为不够好；可以努力沟通，依然被要求承担对方所有情绪后果；可以表达脆弱，却反而被贴上软弱、不成熟或有问题的标签。",
            "这种关系真正伤人的地方，不是偶尔争吵，而是逻辑失效。规则随情绪变化，边界随期待变化，付出被视为理所当然，疲惫却不被承认。长期留在这样的结构里，就是用内心平静去交换一场没有终点的消耗。",
            "拒绝失衡关系不等于排斥女性，也不等于否定爱情。它只是拒绝被不稳定的情绪、失控的依赖和不平等的契约吞没。真正值得进入的关系，必须让双方都更清醒、更稳定、更有力量，而不是让一个人成为另一个人的情绪容器。",
        ],
    ),
    (
        "marriage-myth",
        "婚姻不是人生完整的唯一证明",
        [
            "社会仍然反复灌输一种观念：男人只有结婚，人生才算完整。但这个判断来自一个已经变化的世界。婚姻曾经提供生活秩序、共同劳动、家庭保障和稳定分工；在今天，它越来越多地变成一种社会表演，一种看似稳定、实则掩盖妥协、怨恨和长期压力的生活安排。",
            "许多男人走进婚姻，并不是因为内心真正渴望那段关系，而是因为年龄到了、父母催促、身边人都结了、害怕被评价为失败。这样的婚姻从开始就带着外部压力，而不是主动选择。它看似完成了任务，却可能让人失去自由、目标和自我。",
            "几个世纪以来，男性的成就感并不只来自家庭角色。建设、探索、创造、承担、开拓，都是男性生命能量的重要出口。一个男人当然可以成为伴侣、丈夫和父亲，但他不应该被要求把全部价值压缩进供养者与保护者两个角色里。",
            "真正成熟的婚姻必须服务于双方成长，而不是制造负罪感。如果一段关系要求一个男人以牺牲自尊、自由、财富和精神安宁为代价来证明爱，那么这段关系并不神圣，只是换了一种语言包装的控制。",
            "一个男人的价值不取决于他是否有妻子或孩子，而取决于他是否拥有目标、自律、尊严、健康和清醒的判断力。婚姻可以是幸福的一种形式，却绝不是幸福的唯一入口。",
        ],
    ),
    (
        "financial-autonomy",
        "财务自主让生活重新变得可控",
        [
            "金钱往往比情绪更快揭示现实。单身男性最直接的优势，是可以掌控自己的财务结构。每一笔收入如何分配，是用于投资、健康、旅行、学习、创业，还是用于提升生活质量，都可以围绕自己的目标决定。",
            "没有共同债务的无底洞，没有不可预测的消费期待，也没有为了维持表面体面而不断扩张的开支。一个人可以选择极简生活，把钱花在真正重要的地方。极简不是寒酸，而是一种力量：它让人从外界评价体系里退出，把资源集中到长期成长上。",
            "婚姻一旦进入高消费结构，财务平衡很容易被打破。住房、车辆、家庭开销、孩子教育、医疗、双方父母、人情往来、节日消费，每一项都会长期吞噬现金流。更复杂的是，钱不再只是钱，每一次财务决定都可能变成情绪谈判。",
            "当一个男人意识到自己的大量精力被转化成账单时，很多梦想已经被推迟甚至放弃。想换工作不敢换，想停下来调整不敢停，想冒险尝试新机会不敢动，因为背后绑定着太多固定责任。",
            "单身并不是没有责任，而是责任首先回到自己身上。理性消费、持续储蓄、有目的地投资、照顾健康、建立安全垫，这些都不是自私，而是对自身生命负责。没有内心平静的金钱只是一堆噪音；在清醒状态下拥有的金钱，才会变成前行、选择和创造的自由。",
        ],
    ),
    (
        "health",
        "身心健康，是远离内耗之后最直接的回报",
        [
            "当情感冲突的喧嚣退去，一个人的身体会很快给出反馈。睡眠更深，专注力更稳定，训练更规律，精神状态更清爽。健身不再只是外貌管理，而成为一种每日确认自我掌控感的方式。",
            "单身男性往往更容易管理作息、饮食、训练、隐私和时间。没有突发的情绪拉扯，没有反复消耗注意力的争执，也没有因为长期压力造成的暴饮暴食、失眠和疲惫。身体开始从求生状态回到修复状态。",
            "不幸的亲密关系会把人长期放在应激里。醒来时疲惫，入睡时愤怒，每一天都在沉默的怨气里消耗。久而久之，身体会替精神买单。心血管压力、免疫下降、慢性疲劳、焦虑和抑郁，都可能从一段低质量关系里慢慢长出来。",
            "自由改变这一切。一个人可以训练、休息、读书、工作、独处，而不需要为照顾自己的需求感到内疚。自律逐渐变成自尊，健康则成为内在秩序的外在证明。",
            "婚姻本身并不会摧毁男人，真正摧毁人的，是长期失衡的情感结构。当一个人把精力从动荡关系中收回来，转向身体、精神和目标，健康就会成为清醒生活最诚实的证据。",
        ],
    ),
    (
        "emotional-independence",
        "情感独立，是不再把幸福外包",
        [
            "一个人停止从他人身上寻找幸福的那一刻，真正的成长才开始。情感独立不是把自己封闭起来，而是不管谁靠近、谁离开，都能维持内心重心的能力。",
            "单身让人不必为了获得赞许而表演，不必为了证明价值而讨价还价，也不必把舒适感误认为灵魂契合。独处时，一个人开始观察自己的思想，分辨真实需要和表面欲望，理解焦虑、嫉妒、控制欲和依赖感如何支配自己。",
            "这种转变是情感成熟的开始。没有持续不断的索取，一个男人可以发现，抛开所有关系角色之后，真实的自己究竟是什么样。他不再只是男朋友、提款机、拯救者或稳定情绪的工具，而是一个完整、清醒、具体的人。",
            "在这个空间里，真正的边界才会出现。可以毫无负担地说不，可以不为专注、沉默和距离感到抱歉，也可以不再把自我牺牲包装成深情。自尊是一切关系的基础；没有自尊，爱会变成妥协；有了自尊，关系才会成为选择。",
            "当幸福不再依赖另一个人时，一个人才获得了免于恐惧去爱的能力。他仍然可以关心，可以付出，可以亲近，但不会在关系中丢失自我。也可以在混乱出现时平静离开，不带怨恨，也不把离开解释成失败。",
        ],
    ),
    (
        "social-circle",
        "社交不再是依赖，而是主动选择",
        [
            "单身并不意味着社交世界缩小。相反，当一个人不再把所有情绪出口压在某段亲密关系上，他的社交世界反而可能变得更健康、更广阔、更稳定。",
            "低质量婚姻或关系容易让人孤立。社交圈缩小，朋友逐渐疏远，唯一的情绪出口只剩伴侣；一旦这段关系变得有毒，人就会陷入无处发声、无处修复的孤立状态。",
            "独立的男性会避开这种陷阱。他不再依靠某一个人获取安慰或身份认同，而是建立一个基于尊重、价值观和共同成长的人际网络。这样的关系更轻松，也更真实，因为它不依赖控制、捆绑和恐惧来维持。",
            "男人之间的友谊常常被低估，但它是情感力量的重要基础。共同训练、共同学习、坦诚反馈、互相提醒，比许多表演型亲密更扎实。真正的朋友不要求你扮演角色，只帮助你更清醒地成为自己。",
            "单身也不意味着拒绝亲密关系。一个女人仍然可以成为生活的一部分，但不再是世界的重心。陪伴可以存在，关怀可以存在，吸引可以存在，只是它们不再以占有、依赖和失控为代价。",
        ],
    ),
    (
        "freedom",
        "自由让生命重新变得宽阔",
        [
            "当一个男人不再被情感枷锁和社会时间表束缚，生活会重新打开。时间、金钱和精力回到自己手里，每一天都可以用于行动、建设、体验和探索，而不是用于取悦别人或修补别人的期待。",
            "他可以旅行，学习新技能，开启新事业，换城市，追逐机会，承担风险。无需反复征求许可，也不必为了别人的安全感放弃自己的成长。他开始凭好奇心生活，而不是凭恐惧生活。",
            "很多人把日复一日的平庸误认为稳定，把从不选择误认为负责。但真正的稳定不是僵死不动，而是拥有足够内在秩序，可以在变化中保持方向。冒险并不必然制造混乱，清醒的冒险反而会带来一种建立在成长之上的新秩序。",
            "自由不是任性，也不是背叛。自由是身心合一，是选择与价值观一致的生活。一个人醒来时没有怨气，入睡时问心无愧，知道今天所做的事出自自己的选择，而不是被迫执行别人的剧本，这就是非常具体的幸福。",
            "没有外部义务过度挤压，创造力会重新出现。阅读、写作、训练、研究、旅行、创业，过去被妥协掩埋的热爱会慢慢浮出水面。世界重新变得宽广，在别人只看到限制的地方，独立者能看到可能性。",
        ],
    ),
    (
        "happiness",
        "幸福不是被选中，而是选择自己",
        [
            "幸福并不藏在婚姻证书、社会地位或别人的认可里。它藏在一种清醒的从容里：知道自己的生命属于自己，知道自己不必为了完成外界期待而牺牲内在平静。",
            "这个世界不停告诉男人应该成为什么样的人：伴侣、供养者、保护者、父亲、问题解决者。但当这些期待一层层退去，剩下的才是最基本的事实：一个人本身就已经足够。他可以选择关系，但不需要靠关系证明存在。",
            "单身不是人际交往的失败，而是从幻觉中退出的自由。它是毫无愧疚地做决定的机会，是不背负情感债务去休息的权利，是把注意力投入目标而不是投入无尽解释的空间。",
            "社会仍然会嘲讽单身男性，说他们不成熟、胆怯、人生不完整。但很多独自前行的人，恰恰是把世界看得更清楚的人。他们不再用牺牲程度衡量成功，而是用财务自主、情绪稳定、身体健康、精神专注和内心契合度衡量人生质量。",
            "这不意味着拒绝爱和关系，而是带着清醒进入关系。可以开放，但不被占有；可以关怀，但不自我消失；可以深情，但不以恐惧为底色。真正强大的状态，是保持温度，同时守住核心。",
        ],
    ),
    (
        "conclusion",
        "保持单身，也可以是一条强大的路",
        [
            "不要再让社会替你安排人生时间表。不要急着迎合那些为上一代人设计的生活模具。时代变了，关系结构变了，婚姻成本变了，个体对自由、尊严和精神安宁的要求也变了。",
            "一个男人不欠世界一段婚姻，也不欠任何人一场为了证明正常而完成的表演。他真正欠自己的，是一份内心平静：过简单的生活，做深刻的思考，保护好精力，照顾好身体，管理好金钱，选择真正值得进入的人际关系。",
            "如果一个人此刻独自生活，不必把它看作空虚。它也可以是证据，证明自己足够强大，能够走出一条不靠依附、不靠认同、不靠恐惧维持的道路。",
            "幸福从来不只是被别人选中。更深的幸福，是在清醒之后选择自己。保持敏锐，保持沉稳，保持开放，也保持边界。当一段关系不能带来尊重、成长和安宁时，单身不是退路，而是一种更高级的自我保护。",
        ],
    ),
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, content: str) -> None:
    target = ROOT / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def term_href(kind: str, name: str) -> str:
    return f"/{kind}/{quote(name)}/"


def tag_links() -> str:
    return "&nbsp;".join(f'<a href="{term_href("tags", tag)}">{esc(tag)}</a>' for tag in TAGS)


def toc_html() -> str:
    return "".join(f'<a class="toc-link toc-level-2" href="#{anchor}">{esc(title)}</a>' for anchor, title, _paras in SECTIONS)


def body_html() -> str:
    chunks = [f'<p><img src="{ASSET_DIR}/cover.svg" alt="{esc(TITLE)}"></p>']
    intro = [
        "现代单身男性的幸福，并不来自冷漠，也不来自对亲密关系的否定，而来自一个更根本的变化：他们开始把人生的控制权从外界期待中拿回来。",
        "当婚姻、恋爱、供养、情绪劳动和社会评价不再自动拥有最高优先级，一个男人会重新看见自己真正拥有的东西：时间、注意力、身体、金钱、精神能量、自由选择的权利，以及不必用关系证明价值的尊严。",
        "这是一种被长期误解的幸福。它安静、克制、务实，并不依靠掌声。它不是拒绝爱，而是拒绝把依赖误认为爱；不是害怕责任，而是拒绝承担一份失衡、混乱、并且不再尊重彼此成长的责任。",
    ]
    chunks.extend(f"<p>{esc(paragraph)}</p>" for paragraph in intro)
    for anchor, heading, paragraphs in SECTIONS:
        chunks.append(f'<h2 id="{anchor}">{esc(heading)}</h2>')
        chunks.extend(f"<p>{esc(paragraph)}</p>" for paragraph in paragraphs)
    return "\n".join(chunks)


def cover_svg() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-labelledby="title desc">
  <title id="title">{esc(TITLE)}</title>
  <desc id="desc">{esc(DESCRIPTION)}</desc>
  <rect width="1200" height="630" fill="#f8fafc"/>
  <rect x="66" y="58" width="1068" height="514" rx="18" fill="#111827"/>
  <path d="M130 478 C245 380, 368 542, 505 430 S780 323, 1036 462" fill="none" stroke="#38bdf8" stroke-width="6" stroke-linecap="round"/>
  <path d="M130 514 C282 455, 416 512, 584 458 S825 385, 1038 510" fill="none" stroke="#22c55e" stroke-width="5" stroke-linecap="round"/>
  <text x="104" y="128" fill="#e5e7eb" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="28" font-weight="600">单身不是退场，而是重新掌控生活</text>
  <text x="104" y="218" fill="#ffffff" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="56" font-weight="800">现代单身男性</text>
  <text x="104" y="288" fill="#bfdbfe" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="40" font-weight="700">为什么可能是最快乐的一代</text>
  <g font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="24" font-weight="600">
    <rect x="104" y="352" width="168" height="56" rx="10" fill="#1e293b" stroke="#38bdf8"/>
    <text x="130" y="388" fill="#bae6fd">独处</text>
    <rect x="296" y="352" width="168" height="56" rx="10" fill="#1e293b" stroke="#22c55e"/>
    <text x="322" y="388" fill="#bbf7d0">自由</text>
    <rect x="488" y="352" width="192" height="56" rx="10" fill="#1e293b" stroke="#f59e0b"/>
    <text x="514" y="388" fill="#fde68a">财务自主</text>
    <rect x="704" y="352" width="192" height="56" rx="10" fill="#1e293b" stroke="#a78bfa"/>
    <text x="730" y="388" fill="#ddd6fe">情绪稳定</text>
  </g>
  <text x="104" y="548" fill="#cbd5e1" font-family="Noto Sans SC, PingFang SC, Arial, sans-serif" font-size="24">时间、金钱、注意力、身体和精神重新回到自己手里</text>
</svg>
'''


def replace_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    next_text, count = re.subn(pattern, lambda _m: replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"failed to replace {label}")
    return next_text


def article_html() -> str:
    page = read("2026/bullshit-jobs-information-industry-power-order/index.html")
    page = replace_once(page, r"<title>.*?</title>", f"<title>{esc(TITLE)} - zcxGGmu's Blog</title>", "title", re.S)
    page = replace_once(page, r'<meta name="description" content=".*?">', f'<meta name="description" content="{esc(DESCRIPTION)}">', "description", re.S)
    page = replace_once(page, r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://zcxggmu.github.io{URL}">', "og url", re.S)
    page = replace_once(page, r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{esc(TITLE)}">', "og title", re.S)
    page = replace_once(page, r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{esc(DESCRIPTION)}">', "og description", re.S)
    page = replace_once(page, r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://zcxggmu.github.io{URL}">', "canonical", re.S)
    page = replace_once(page, r"background-image:url\('.*?'\)", f"background-image:url('{ASSET_DIR}/cover.svg')", "hero image")
    title_block = (
        f'<div class="post-title">{esc(TITLE)}'
        f'<div class="post-subtitle">{esc(DESCRIPTION)}</div>'
        f'<div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;'
        f'<span class="meta-icon" aria-hidden="true">▣</span> <a href="{term_href("categories", CATEGORY)}">{esc(CATEGORY)}</a>&nbsp;&nbsp;'
        f'<span class="meta-icon" aria-hidden="true">◇</span> {tag_links()}&nbsp;&nbsp;'
        f'<span class="meta-icon" aria-hidden="true">◷</span> 18 min</div></div>'
    )
    page = replace_once(page, r'<div class="post-title">.*?</div>\s*</div>\s*<div class="post-body-wrapper">', f'{title_block}</div><div class="post-body-wrapper">', "post title", re.S)
    page = replace_once(page, r'<div class="toc-title">目录</div><nav>.*?</nav>', f'<div class="toc-title">目录</div><nav>{toc_html()}</nav>', "toc", re.S)
    pagination = '<nav class="post-pagination"><a class="newer-posts">下一篇<br>没有更新的文章</a>' + f'<a class="older-posts" href="{OLDER_URL}">上一篇<br>{esc(OLDER_TITLE)}</a></nav>'
    page = replace_once(
        page,
        r'<div class="post-body" v-pre>.*?</div></div><nav class="post-pagination">.*?</nav>\s*</article>',
        f'<div class="post-body" v-pre>{body_html()}</div></div>{pagination}</article>',
        "body and pagination",
        re.S,
    )
    return page


def post_card() -> str:
    return f"""<a href="{URL}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(TITLE)}</div>
            <div class="post-item-summary">{esc(DESCRIPTION)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> 18 min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{ASSET_DIR}/cover.svg')"></div></div>
        </div>
      </div>
    </a>
"""


def list_row() -> str:
    return f"""<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{URL}" style="font-size:16px;text-decoration:none">{esc(TITLE)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div>
"""


def archive_row() -> str:
    return f"""<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{URL}">{esc(TITLE)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(CATEGORY)}</span></span>
      </div>
"""


def remove_home_card(text: str) -> str:
    return re.sub(r'\s*<a href="' + re.escape(URL) + r'" class="a-block">.*?</a>\s*', "\n", text, count=1, flags=re.S)


def update_home() -> None:
    text = remove_home_card(read("index.html"))
    write("index.html", insert_home_card_after_pinned(text, post_card(), URL))


def update_rss() -> None:
    xml = read("index.xml")
    xml = re.sub(
        r"<item>\s*<title>.*?</title>\s*<link>https://zcxGGmu\.github\.io"
        + re.escape(URL)
        + r"</link>.*?</item>\s*",
        "",
        xml,
        count=1,
        flags=re.S | re.I,
    )
    item = f"""<item>
<title>{esc(TITLE)}</title>
<link>https://zcxggmu.github.io{URL}</link>
<guid>https://zcxggmu.github.io{URL}</guid>
<pubDate>{PUB_DATE}</pubDate>
<description>{esc(DESCRIPTION)}</description>
</item>
"""
    xml = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{LAST_BUILD}</lastBuildDate>", xml, count=1)
    xml = xml.replace("<item>", item + "<item>", 1)
    write("index.xml", xml)


def update_archive() -> None:
    text = read("archive/index.html")
    had = f'href="{URL}"' in text
    text = re.sub(
        r'\s*<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">[^<]+</span>&nbsp;\s*<a href="'
        + re.escape(URL)
        + r'">.*?</a>\s*<span style="margin-left:10px"><span style="color:#999;font-size:12px">.*?</span></span>\s*</div>\s*',
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    if not had:
        text = re.sub(
            r'(2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">)(\d+)( 篇</span>)',
            lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}",
            text,
            count=1,
        )
    marker = '<div style="padding:8px 0;font-size:15px">'
    idx = text.find(marker)
    if idx == -1:
        raise RuntimeError("archive insertion marker not found")
    write("archive/index.html", text[:idx] + archive_row() + text[idx:])


def term_page(kind: str, name: str, heading: str) -> str:
    escaped_name = esc(name)
    return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{escaped_name}"><meta property="og:title" content="{escaped_name} - zcxGGmu's Blog"><link rel="canonical" href="https://zcxggmu.github.io/{kind}/{quote(name)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{escaped_name} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{heading} {escaped_name}</h1><p style="color:#999;margin-bottom:30px">共 1 篇文章</p>{list_row()}</div></div></div><script src="/js/journal.js"></script></body></html>"""


def update_term_page(kind: str, name: str, heading: str) -> bool:
    rel = Path(kind) / name / "index.html"
    target = ROOT / rel
    if not target.exists():
        write(str(rel), term_page(kind, name, heading))
        return True

    text = target.read_text(encoding="utf-8")
    had = f'href="{URL}"' in text
    text = re.sub(
        r'\s*<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="'
        + re.escape(URL)
        + r'" style="font-size:16px;text-decoration:none">.*?</a>\s*<span style="color:#999;font-size:13px;margin-left:10px">[^<]+</span>\s*</div>\s*',
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    if not had:
        text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + 1} 篇文章", text, count=1)
    marker = '<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">'
    idx = text.find(marker)
    if idx == -1:
        text = text.replace("</div></div></div>", list_row() + "</div></div></div>", 1)
    else:
        text = text[:idx] + list_row() + text[idx:]
    target.write_text(text, encoding="utf-8")
    return not had


def update_taxonomy_index(rel: str, kind: str, name: str, added: bool, style: str) -> None:
    if not added:
        return
    text = read(rel)
    hrefs = {term_href(kind, name), f"/{kind}/{name}/"}
    href_pattern = "|".join(re.escape(h) for h in hrefs)
    name_pattern = re.escape(esc(name))
    pattern = rf'(<a href="(?:{href_pattern})"[^>]*>{name_pattern}<span[^>]*>\()(\d+)(\)</span></a>)'
    next_text, count = re.subn(pattern, lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", text, count=1)
    if count:
        write(rel, next_text)
        return
    if style == "tag":
        link = f'<a href="{term_href(kind, name)}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(name)}<span style="color:#999;font-size:12px;margin-left:4px">(1)</span></a>\n'
    else:
        link = f'<a href="{term_href(kind, name)}" class="a-block" style="padding:8px 0;font-size:18px">{esc(name)}<span style="color:#999;margin-left:8px">(1)</span></a>\n'
    if '<div style="line-height:2.5">' not in text:
        raise RuntimeError(f"taxonomy index marker not found: {rel}")
    write(rel, text.replace('<div style="line-height:2.5">', f'<div style="line-height:2.5">{link}', 1))


def update_taxonomies() -> None:
    category_added = update_term_page("categories", CATEGORY, "")
    update_taxonomy_index("categories/index.html", "categories", CATEGORY, category_added, "block")
    series_added = update_term_page("series", SERIES, "📚")
    update_taxonomy_index("series/index.html", "series", SERIES, series_added, "block")
    for tag in TAGS:
        tag_added = update_term_page("tags", tag, "🏷️")
        update_taxonomy_index("tags/index.html", "tags", tag, tag_added, "tag")


def update_older_pagination() -> None:
    target = ROOT / OLDER_URL.strip("/") / "index.html"
    text = target.read_text(encoding="utf-8")
    replacement = f'<a class="newer-posts" href="{URL}">下一篇<br>{esc(TITLE)}</a>'
    text = re.sub(r'<a class="newer-posts"[^>]*>下一篇<br>.*?</a>', replacement, text, count=1, flags=re.S)
    target.write_text(text, encoding="utf-8")


def changed_files() -> list[str]:
    paths = [
        f"2026/{SLUG}/index.html",
        "2026/bullshit-jobs-information-industry-power-order/index.html",
        "archive/index.html",
        "categories/index.html",
        f"categories/{CATEGORY}/index.html",
        f"images/posts/{SLUG}/cover.svg",
        "index.html",
        "index.xml",
        "series/index.html",
        f"series/{SERIES}/index.html",
        "tags/index.html",
        f"tasks/{SCRIPT_NAME}",
        f"tasks/{MANIFEST_NAME}",
    ]
    paths.extend(f"tags/{tag}/index.html" for tag in TAGS)
    return sorted(dict.fromkeys(paths))


def copy_script_and_manifest() -> None:
    tasks_dir = ROOT / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(__file__), tasks_dir / SCRIPT_NAME)
    (tasks_dir / MANIFEST_NAME).write_text(json.dumps(changed_files(), ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    write(f"images/posts/{SLUG}/cover.svg", cover_svg())
    write(f"2026/{SLUG}/index.html", article_html())
    update_home()
    update_rss()
    update_archive()
    update_taxonomies()
    update_older_pagination()
    copy_script_and_manifest()
    print(f"Published {URL}")


if __name__ == "__main__":
    main()
