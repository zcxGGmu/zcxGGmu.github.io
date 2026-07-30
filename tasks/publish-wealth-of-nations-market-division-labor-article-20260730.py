from __future__ import annotations

import html
import importlib.util
import json
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path


sys.dont_write_bytecode = True
BASE_PATH = Path(__file__).with_name("publish-physical-ai-three-article-batch.py")
spec = importlib.util.spec_from_file_location("base_publisher_wealth_nations", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY = """
<p><img src="/images/posts/wealth-of-nations-market-division-labor-money-logic/cover.svg" alt="读懂《国富论》：财富、分工、市场与普通人的赚钱逻辑"></p>
<p>两百多年过去，很多国家的经济发展、普通人的赚钱路径、商业财富的流转规律，仍然绕不开亚当·斯密在《国富论》中提出的底层框架。一个人为什么长期努力却难以变富，一个行业为什么从暴利走向内卷，一个国家为什么从封闭走向停滞，又为什么在开放分工后迅速崛起，都可以在这套框架里找到解释。</p>
<p>很多人把一生困在“勤劳就能致富”的误区里。勤奋当然重要，但勤奋只是下限，真正决定财富上限的，是是否理解财富的本质、分工的力量、市场的供需、资本的回报、自由贸易的效率，以及自身比较优势的位置。蛮力对抗规律，结果往往是越努力越疲惫；读懂规律、顺势积累，普通人才能让每一份付出真正转化为价值。</p>
<p>《国富论》不是一本只属于经济学课堂的书。它讨论的是国家财富，但落到个人身上，就是一套关于工作、收入、专业能力、副业、创业、投资和长期积累的财富方法论。</p>

<h2 id="money-is-not-wealth">一、货币不是财富，真正的财富是商品与服务</h2>
<p>在亚当·斯密之前，欧洲长期被重商主义支配。许多国家和统治者相信，一个国家是否富裕，取决于国库里黄金、白银等贵金属储备有多少。于是，各国限制商品流出，鼓励贵金属流入，试图把金银锁在本国土地上。</p>
<p>这个逻辑看似合理，结果却经不起现实检验。西班牙曾经从海外掠夺大量黄金白银，国库堆满贵金属，却没有因此长期强盛，反而经历物价飞涨、产业衰败和经济失衡。原因很简单：金银本身不能吃、不能穿、不能住，也不能提供医疗、教育和生活服务。</p>
<p>《国富论》真正颠覆性的起点，是把货币从财富本身降格为财富凭证。货币只是交换工具，真正的财富，是一个社会能够持续生产出来的有用商品和服务。面包、衣服、住房、医疗、教育、交通、工具、知识和便利服务，才是改善生活的真实内容。</p>
<p>孤岛上堆满黄金却没有粮食和住所，人仍然无法生存；孤岛上没有黄金，却有稳定食物、舒适居所和完整生活资料，这才是真正富裕。一个国家如此，一个人也如此。账户里的数字不是财富终点，能持续创造价值、支配资源、获得有用商品与服务的能力，才是财富本体。</p>
<p>这也解释了通货膨胀为什么会让人变穷。表面上存款数字没有减少，但同样货币能够兑换的商品和服务变少了，财富凭证的购买力下降了。它同样解释了实体经济为什么是国家根基，因为只有真实生产和真实服务能创造真正财富，金融和货币只是辅助流转。</p>

<h2 id="personal-wealth">二、个人真正该积累的，是持续创造价值的能力</h2>
<p>把货币误认为财富，会让普通人走向错误的财富策略：只想着存钱、省钱、抠成本，却忽略自身创造价值的能力。存款是必要的安全垫，但它只是暂时的财富凭证；专业技能、行业理解、可迁移能力、人脉信用、可复用经验，才是不会轻易贬值的长期资产。</p>
<p>真正的富人，不是因为单纯存了更多钱而富有，而是拥有持续创造财富、组织资源、提供稀缺价值的能力。财富是能力兑现后的结果，而不是凭空出现的数字。</p>
<p>放到普通人的职业路径上，最重要的问题不是“我如何多攒一点”，而是“我能不能提供别人需要、市场愿意付费、短期难以替代的价值”。当个人能力能够持续生产服务、解决问题、提升效率，收入才有长期来源。</p>
<p>这也是读懂《国富论》后最现实的一条提醒：不要只盯着钱本身，要盯着创造钱的能力。钱会被通胀稀释，岗位会被周期影响，行业会从红利走向竞争，但真正沉淀在自己身上的能力和判断力，会在不同周期中反复变现。</p>

<h2 id="division-of-labor">三、劳动分工是财富倍增的第一生产力</h2>
<p>《国富论》中最经典的案例，是制针工厂。若让一个工人独立完成拉丝、裁断、磨尖、打孔、抛光、成形等所有流程，即使非常努力，一天也只能做出很少数量的针。但如果把制针拆成十几道工序，让每个人只负责其中一道，十个工人一天可以生产出数万根针。</p>
<p>同样的人、同样的工具、同样的时间，因为分工方式不同，产出出现数量级差距。这就是劳动分工的力量：它让熟练度提高，让切换成本下降，让工具创新发生，让劳动效率从线性增长变成倍数增长。</p>
<p>分工首先提升熟练度。长期重复专注一件事，肌肉记忆、操作节奏、思维框架都会快速迭代。一个总是在不同任务之间切换的人，很难在任何单点上形成深度积累；而一个长期深耕细分领域的人，会逐渐形成别人难以追赶的专业壁垒。</p>
<p>分工还减少切换损耗。许多人一天忙得疲惫，却在写文案、回消息、做表格、对接客户、处理临时事务之间反复切换，真正有效产出很低。每次切换都要重新进入状态，这些隐形成本吞掉了大量精力。分工的价值，就是让人持续处在同一类工作状态中，把精力集中在高价值动作上。</p>
<p>分工还会催生工具和方法。长期做剪辑的人会形成快捷键和模板，长期做销售的人会沉淀话术和客户判断，长期写作的人会形成结构化框架。专注带来专业，专业推动工具化，工具化继续放大效率。</p>

<h2 id="specialization">四、普通人不要做全能杂工，要做细分领域的深耕者</h2>
<p>劳动分工给个人最大的启发，是不要把“什么都会一点”误认为竞争力。许多职场人想同时做运营、文案、行政、对接、项目、数据，表面上能力很全面，实际上每一项都不够深，最终只能拿基础薪资，随时面对替代。</p>
<p>高收入人群往往是极致分工的受益者。资深设计师深耕设计，顶级程序员深耕代码，专业运营深耕流量，优秀销售深耕客户关系。他们把有限时间集中在一个能形成复利的位置上，最终形成稀缺能力。</p>
<p>普通人最低成本的逆袭路径，不是面面俱到，而是单点突破。选择一个足够细分、市场有需求、自己有基础优势的方向，长期投入、反复打磨、形成作品和方法论，让自己成为某个具体问题的高质量解决者。</p>
<p>越贫穷的地方，分工越粗糙；越成熟的城市和行业，分工越细致。个人发展同样如此：越粗糙的能力结构，越容易陷入低价竞争；越清晰的专业定位，越容易获得溢价。</p>

<h2 id="exchange-and-market">五、分工来自交换，分工上限取决于市场范围</h2>
<p>分工不是凭空产生的，它起源于人类互通有无、彼此交换的能力。你擅长种地，我擅长织布；你生产粮食，我生产衣物；通过交换，双方都能用更低成本获得更丰富的生活资料。交换让每个人专注自己更擅长的事，分工因此形成。</p>
<p>分工的上限，取决于市场范围。小村庄的需求有限，一个小店老板往往必须身兼数职：进货、销售、记账、整理店铺都要自己做，因为市场规模支撑不起精细分工。但在人口密集、需求多元的一线城市，一个项目可以拆成几十个岗位，每个人只负责极窄的环节，最终创造巨大商业价值。</p>
<p>国家发展也是同样逻辑。市场越开放，交易越自由，分工越细，效率越高，财富越容易涌现。封闭的小市场限制了分工，限制了专业化，也限制了生产率；开放的大市场则把更多人、更多资源、更多技术连接起来，让每个环节都能在更高效率上运转。</p>
<p>这也是普通人选择城市、行业和平台时必须考虑的因素。不是所有努力都在同一市场范围内获得同样回报。更大的市场、更细的分工、更强的交易密度，往往意味着更高的收入上限。</p>

<h2 id="invisible-hand">六、看不见的手：利己如何推动社会协作</h2>
<p>《国富论》最著名的概念，是“看不见的手”。它不是神秘力量，而是自由市场中的价格机制和供需机制。每个人都在追求自己的利益，却在无形中推动资源流向更有效率的位置。</p>
<p>面包师烤面包，不是因为抽象的善意，而是因为卖面包可以养家糊口；酿酒师酿酒，不是为了无偿奉献，而是为了获得利润；裁缝做衣服，也是为了靠手艺谋生。每个人的出发点都是利己，但结果却形成了稳定供给，让社会中的其他人能够低成本获得所需商品和服务。</p>
<p>价格机制会自动传递信号。当某类商品供不应求，价格上涨，利润空间变大，资本和劳动会涌入，供给增加后价格回落；当某类商品供过于求，价格下跌，利润收缩，资源会退出，市场重新寻找平衡。这个过程不需要每一步都由外部命令指挥。</p>
<p>直播带货、新能源、AI 工具、内容平台、社区团购等行业的起落，都能用这套逻辑解释。早期供给不足、需求旺盛，利润较高；大量人涌入后，供给过剩，竞争加剧，利润被摊薄，能力不足者被淘汰，行业回归理性。</p>

<h2 id="market-misunderstanding">七、不要道德绑架市场，也不要盲目跟风市场</h2>
<p>理解看不见的手，首先要放下对商业的简单道德化。商人追求利润，不必然等于邪恶。正因为利润存在，才有人愿意投入成本、承担风险、提高效率、改善服务。没有利润信号，生产和服务会失去动力，市场也会停滞。</p>
<p>但尊重市场，不等于盲目崇拜任何风口。很多普通人做副业、创业、投资，总是等到一个赛道人人都知道赚钱时才入局。可当所有人都知道机会存在，供给往往已经开始过剩，红利已经被迅速摊薄，后来者很容易变成高位接盘者。</p>
<p>真正的机会，常常出现在供需即将失衡但尚未饱和的阶段。需求已经出现，供给还不充分；问题足够明确，解决方案还不成熟；市场愿意付费，但参与者还没有拥挤。这才是普通人应该重点识别的窗口。</p>
<p>因此，顺势而为不是追热点，而是读懂供需。逆势硬扛和盲目跟风，本质上都是不理解市场信号。</p>

<h2 id="price-wage-income">八、价格、工资与收入：你的薪资由什么决定</h2>
<p>亚当·斯密认为，商品价格最终由三部分构成：工资、利润和地租。劳动者靠劳动获得工资，资本所有者靠资本承担风险获得利润，资源所有者靠土地等稀缺资源获得地租。社会收入大体围绕这三类来源展开。</p>
<p>斯密还区分了自然价格和市场价格。自然价格是由成本和合理利润构成的长期价值中枢，市场价格则会围绕它上下波动，受供需、政策、情绪和周期影响。</p>
<p>放到个人身上，能力、经验、作品、解决问题的水平，就是一个人的自然价格；行业风口、岗位缺口、城市需求和资本周期，则决定短期市场价格。几年前互联网行业需求旺盛，人才缺口大，很多中等能力从业者也能拿到高薪，因为市场价格高于自然价格。行业逐渐饱和后，市场价格回落，只有真正具备核心能力的人才能维持高收入。</p>
<p>这说明，工资高低并不取决于老板良心，也不单纯取决于辛苦程度，而取决于劳动力供需关系和个人稀缺性。门槛低、人人可做的岗位，即使很辛苦，薪资也很难长期上行；稀缺、复杂、难替代的能力，才会让市场愿意支付溢价。</p>
<p>普通人想提高收入，只有两条路最有效：提升自己的自然价格，也就是打磨核心能力；进入市场价格高于自然价格的行业或岗位，借助供需红利放大收入。努力决定下限，稀缺性决定上限。</p>

<h2 id="capital-profit">九、资本与利润：规模化生产需要资源整合</h2>
<p>很多人天然排斥资本和利润，认为资本就是剥削，利润就是暴利。但《国富论》的观点更客观：资本是财富积累的杠杆，没有资本投入，就没有规模化生产、设备升级、组织协作和产业迭代。</p>
<p>劳动是创造财富的基础，但资本可以放大劳动效率。一个人单独劳动，只能获得单次收益；资本投入设备、组织团队、搭建流程、连接市场，可以让劳动效率成倍提高，从而创造更多增量财富。</p>
<p>利润则是资本承担风险、整合资源、优化效率后的回报。员工提供劳动，通常拿相对确定的工资；经营者投入本金，承担亏损风险，组织资源，承担失败后果。风险越大、整合资源越多、效率提升越明显，对应收益也更高。</p>
<p>但斯密也指出，自由市场中的利润会趋向平均。新兴行业、蓝海赛道、早期供给不足时，利润空间较高；随着大量资本和人群涌入，竞争加剧，利润被压缩，最终回到社会平均水平。真正的高利润往往存在于尚未饱和、尚未被大众充分识别的细分领域。</p>

<h2 id="national-wealth">十、国家财富增长的四个支柱</h2>
<p>《国富论》对国家财富增长的解释，可以概括为四个支柱：分工细化、资本积累、自由贸易、合理治理。</p>
<p>分工细化提升效率，效率创造增量财富。资本积累让一部分财富不被立即消费，而是投入设备、技术、教育、组织和长期资产，推动下一轮增长。自由贸易扩大市场范围，让不同地区和国家发挥各自优势，通过交换实现总财富提升。</p>
<p>合理治理则是市场健康运转的底线。亚当·斯密并不是无政府主义者。他强调政府应该保卫国家安全，维护司法与公平，保护财产和交易秩序，建设公共基础设施，普及公共教育，惩治欺诈、垄断和暴力。</p>
<p>市场负责高效创造财富，政府负责守住秩序和公平。政府如果过度干预正常竞争，会压制效率；如果完全缺位，又会放任欺诈、垄断和无序竞争。真正有效的治理，是守底线、搭平台、保公平，让看不见的手在可持续秩序中运行。</p>

<h2 id="comparative-advantage">十一、比较优势：普通人选择赛道的关键</h2>
<p>绝对优势，是你比别人做得更好、效率更高、成本更低。比较优势，则不要求你样样比别人强，而是看你在自己所有能力里，哪一项机会成本最低、投入产出比最高、最值得长期深耕。</p>
<p>很多人痛苦的根源，是总拿自己的短板去对标别人的长板，盲目内卷，盲目补课，结果精力耗尽却没有形成核心竞争力。《国富论》的启发是：赚钱的最高境界，不是补齐所有短板，而是持续放大自己的比较优势。</p>
<p>一个人不需要面面俱到，只需要找到自己相对最擅长、市场又需要的一件事，把它做到足够深，形成可识别、可交付、可复用的价值。哪怕整体能力并不突出，只要在某个细分位置有比较优势，就可以参与市场分工并获得收入。</p>
<p>国家如此，个人也如此。科技强的国家发展高端技术，劳动力充足的国家发展制造业，资源和旅游优势明显的地区发展服务业。每个主体都应该找到自己的低机会成本位置，进入交换网络，而不是盲目复制他人的路径。</p>

<h2 id="personal-framework">十二、普通人可以长期使用的财富框架</h2>
<p>读懂《国富论》，普通人至少可以建立五条长期原则。</p>
<p>第一，重新定义财富。真正的财富不是货币数字，而是持续创造价值的能力、能够支配的资源、能够提供的稀缺服务。投资自己、打磨能力、积累信用，是最不容易贬值的财富策略。</p>
<p>第二，相信分工。不要做全能杂工，要做细分领域的深耕者。越细分、越专注、越能形成复利，个人效率和收入上限越高。</p>
<p>第三，敬畏市场。不要用道德想象替代供需规律，也不要在红海里盲目跟风。真正的机会藏在供给不足、需求上升、尚未拥挤的细分位置。</p>
<p>第四，理解价值交换。商业不是自我感动，收入来自为他人解决问题。能创造多少可被市场认可的价值，就有机会获得多少财富回报。</p>
<p>第五，懂得积累与复利。消费会消耗财富，积累和投资才会放大财富。资金、能力、认知、人脉和作品都需要长期复利，时间会放大真正有方向的投入。</p>

<h2 id="conclusion">结语：财富不是蛮力的奖赏，而是顺应规律的结果</h2>
<p>《国富论》的底层逻辑并未过时。个人赚钱、职场晋升、副业创业、行业起落、国家经济、全球贸易，都仍然受到财富本质、劳动分工、市场供需、资本积累、自由交换和比较优势的约束。</p>
<p>许多人努力却迷茫，不是因为不够勤奋，而是用蛮力对抗规律，把货币误当财富，把忙碌误当价值，把跟风误当机会，把全能误当竞争力。真正的成长，是读懂规律、顺应趋势、深耕价值、长期积累。</p>
<p>从今天开始，与其只问“怎样赚更多钱”，不如先问五个问题：我能创造什么真实价值？我在哪个细分领域最有比较优势？我的能力是否稀缺？我所在赛道供需关系如何？我是否在持续积累可复利的资产？这些问题的答案，才是普通人穿越周期、提升收入、摆脱无效内卷的底层密码。</p>
"""


def _plain_text(html_text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(html_text))


def validate() -> None:
    _BASE_VALIDATE()
    post = base.INPUT_ORDER[0]
    article_path = base.ROOT / post.url_path.strip("/") / "index.html"
    article = article_path.read_text(encoding="utf-8")
    body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    plain = _plain_text(body_match.group(1)) if body_match else ""
    failures: list[str] = []
    if len(plain) < 5000:
        failures.append(f"body too short: {len(plain)}")
    forbidden = [
        "B站",
        "bilibili",
        "哔哩",
        "视频里",
        "视频中",
        "原视频",
        "音频里",
        "音频中",
        "UP主",
        "up主",
        "这期",
        "本期",
        "作者说",
        "他提到",
        "观看",
        "点赞",
        "订阅",
        "投币",
        "收藏",
        "下期",
        "BV1",
    ]
    for word in forbidden:
        if word in article:
            failures.append(f"forbidden/source wording present: {word}")
    required = ["国富论", "亚当·斯密", "货币", "财富", "劳动分工", "看不见的手", "工资", "资本", "自由贸易", "比较优势"]
    for word in required:
        if word not in article:
            failures.append(f"missing required topic: {word}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links or len(h2) < 10:
        failures.append(f"toc mismatch or too few h2: h2={len(h2)} links={len(links)}")

    home = (base.ROOT / "index.html").read_text(encoding="utf-8")
    cards = re.findall(r'<a href="([^"]+)" class="a-block">', home)
    expected = [
        "/ai-news-radar/",
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
        post.url_path,
        base.PREV_EXISTING_URL,
    ]
    if cards[: len(expected)] != expected:
        failures.append(f"homepage order mismatch: {cards[:len(expected)]}")

    taxonomy_expectations = [
        ("archive/index.html", post.url_path),
        ("index.xml", post.url_path),
        ("categories/index.html", post.category),
        ("series/index.html", post.series),
        ("tags/index.html", post.tags[0]),
        (f"categories/{post.category}/index.html", post.url_path),
        (f"series/{post.series}/index.html", post.url_path),
        (f"tags/{post.tags[0]}/index.html", post.url_path),
    ]
    for rel, expected_text in taxonomy_expectations:
        path = base.ROOT / rel
        if expected_text not in path.read_text(encoding="utf-8"):
            failures.append(f"{rel} missing {expected_text}")

    ET.fromstring((base.ROOT / "images/posts" / post.slug / "cover.svg").read_text(encoding="utf-8"))
    ET.parse(base.ROOT / "index.xml")
    pycache = [str(p) for p in base.ROOT.rglob("__pycache__")]
    if pycache:
        failures.append(f"__pycache__ present: {pycache[:3]}")
    if failures:
        raise SystemExit("\n".join(failures))


def copy_script_and_manifest() -> None:
    tasks_dir = base.ROOT / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    script_path = tasks_dir / base.SCRIPT_NAME
    source_script = Path(__file__)
    if source_script.resolve() != script_path.resolve():
        shutil.copyfile(source_script, script_path)
    base.rec(script_path)
    for rel in ["categories/index.html", "series/index.html", "tags/index.html"]:
        base.rec(base.ROOT / rel)
    manifest_path = tasks_dir / base.MANIFEST_NAME
    all_changed = sorted(base.CHANGED | {f"tasks/{base.SCRIPT_NAME}", f"tasks/{base.MANIFEST_NAME}"})
    manifest_path.write_text(json.dumps(all_changed, ensure_ascii=False, indent=2), encoding="utf-8")
    base.rec(manifest_path)


base.ROOT = Path("/tmp/bv1ka-bv169-sparse.Nkhbld")
base.DATE = "2026-07-30"
base.BASE_DT = datetime(2026, 7, 30, 21, 35, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/employment-crisis-wealth-concentration-common-prosperity-distribution/"
base.PREV_EXISTING_TITLE = "就业困境的根源：财富集中、降本增效与共同富裕的再分配命题"
base.SCRIPT_NAME = "publish-wealth-of-nations-market-division-labor-article-20260730.py"
base.MANIFEST_NAME = "publish-wealth-of-nations-market-division-labor-article-20260730-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="public-audio-bv1wxga6wet1-20260730",
        slug="wealth-of-nations-market-division-labor-money-logic",
        title="读懂《国富论》：财富、分工、市场与普通人的赚钱逻辑",
        desc="《国富论》的核心不是抽象经济学，而是理解财富本质、劳动分工、看不见的手、工资与资本、自由贸易和比较优势的一套底层框架。",
        category="读书笔记",
        series="经典阅读",
        tags=["国富论", "亚当斯密", "财富观", "劳动分工", "看不见的手", "市场机制", "工资", "资本", "自由贸易", "比较优势"],
        minutes=18,
        body=BODY,
        cover_kicker="国富论",
        cover_line="财富 · 分工 · 市场 · 比较优势",
        cover_theme=("#0f172a", "#7c2d12", "#f59e0b"),
        duration=1777.5804375,
        segments=237,
        chars=9516,
    )
]
base.PUBLISH_ORDER = list(base.INPUT_ORDER)
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
    base.main()
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
