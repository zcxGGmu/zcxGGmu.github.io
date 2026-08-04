from __future__ import annotations

import html
import importlib.util
import json
import os
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True

ROOT_HINT = Path("/tmp/blog-publish-bv1j7-20260804.path")
ROOT = Path(os.environ.get("BLOG_ROOT") or ROOT_HINT.read_text(encoding="utf-8").strip())
BASE_PATH = Path(__file__).with_name("publish-physical-ai-three-article-batch.py")
if not BASE_PATH.exists():
    BASE_PATH = ROOT / "tasks" / "publish-physical-ai-three-article-batch.py"

spec = importlib.util.spec_from_file_location("base_publisher_anti_risk_investing", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY = """
<p><img src="/images/posts/anti-risk-investing-low-cost-diversification-long-term-system/cover.svg" alt="抗风险投资：低成本、分散化与长期持有的投资系统"></p>
<p>投资失败，往往不是因为不够聪明。很多人在金融市场里拥有漂亮学历、复杂模型、昂贵数据库和密集信息流，却仍然在危机时刻交出筹码，在反弹之后追悔莫及。真正的问题不是智商，而是把精力放在了错误的事情上：预测短期走势、寻找下一只暴涨标的、相信自己能在恐慌中保持绝对理性。</p>
<p>《抗风险投资》的核心，是把投资从“预测游戏”改造成“生存系统”。市场会反复崩盘，媒体会反复制造紧迫感，人性会反复在高点贪婪、低点恐惧。一个投资体系如果只能在顺风期成立，却在熊市第三个月崩掉，就不是真正的体系。</p>
<p>长期投资真正要解决的，不是如何在下个月跑赢别人，而是如何在几十年里尽量减少错误、降低成本、避开毁灭性行为，并让复利有足够时间工作。低成本、分散化、长期持有、自动扣款和定期再平衡，听起来朴素，却正是普通人最接近稳健财富积累的路径。</p>

<h2 id="smart-trap">一、聪明人的投资陷阱</h2>
<p>很多投资者被训练成相信“懂得越多，赚得越多”。于是他们研究宏观、行业、财报、政策、资金流、技术指标和市场情绪，希望从海量信息里找到确定答案。但市场不是考试，没有标准答案，也不会因为一个人足够努力就奖励他。</p>
<p>聪明反而可能成为负担。越聪明的人越容易相信自己能解释市场，越容易把一次预测成功当成能力，越容易在复杂模型里寻找安全感。真正危险的是方向错了还加倍努力：如果目标是预测不可预测的短期波动，投入越多，偏离越远。</p>
<p>投资的第一步，是承认边界。未来一年哪类资产涨得最好，下一次崩盘何时到来，某位基金经理是否还能继续领先，这些问题大多无法稳定回答。与其把投资建立在预测上，不如把系统建立在自己能控制的变量上：成本、分散、期限、行为和纪律。</p>

<h2 id="cost">二、费率是最确定的亏损来源</h2>
<p>投资里最容易被忽视的数字，是费率。1% 听起来很小，一百元里只拿走一元，似乎无关紧要。但复利世界里，长期费率差异会变成巨额结果差异。假设一百万本金在市场里长期获得 7% 年化回报，如果扣除 1% 费用，实际只剩 6% 复利，三十年后差距可能接近两百万元。</p>
<p>市场回报不确定，费率却几乎确定。你无法保证某只基金未来跑赢，但可以确定高费率每年都会从账户里拿走一部分结果。把长期财富交给高成本产品，本质上是在用确定成本购买不确定的超额收益。</p>
<p>挑投资品像挑工具，不一定要最贵，但必须先剔除高价低质的东西。高费率、低透明度、频繁换手、业绩基准模糊、销售话术过重，都是需要警惕的信号。成本不是唯一标准，却是最早能看见、最容易量化、也最值得先控制的标准。</p>
<p>费率的残酷之处在于，它不需要市场犯错就会发生。牛市里它会吃掉一部分上涨，熊市里它会加重亏损，震荡市里它会让原本平淡的结果更差。投资者常常愿意为“专业管理”付费，却很少把这笔费用放进三十年的复利表里计算。一旦把时间拉长，低成本不是小优化，而是核心收益来源之一。</p>

<h2 id="active-management">三、主动管理的难题：过去业绩不能购买未来</h2>
<p>很多人愿意为主动基金付高费率，是因为历史业绩漂亮。但过去业绩是已经发生的事情，买入时真正购买的是未来。问题在于，能持续跑赢市场的主动管理者非常少，而且事前很难辨认。</p>
<p>如果一只基金过去三年领先，很可能是能力，也可能是风格顺风、行业押注、运气集中或风险暴露刚好有效。等到投资者因为历史回报追进去，风格可能已经切换，规模可能已经变大，管理难度也可能上升。</p>
<p>主动管理不是没有价值，但普通投资者不应把长期计划完全押在“找到少数赢家”上。更稳的方式，是先用低成本指数基金拿到市场平均回报，再用很小比例尝试自己真正理解的主动机会。核心资产负责复利，卫星仓位负责认知实验。</p>

<h2 id="index">四、指数化投资的底层逻辑</h2>
<p>指数化投资的逻辑很简单：既然大多数人长期很难稳定战胜市场，就用低成本方式持有整个市场。它不承诺每一年领先，也不追求抓住每个热门赛道，而是接受市场整体增长带来的长期回报。</p>
<p>指数基金的优势来自三点。第一，成本低，长期拖累小。第二，分散化，避免单一公司或单一基金经理错误带来的毁灭性影响。第三，规则清晰，不依赖频繁判断和情绪操作。</p>
<p>这套方法的朴素之处，也正是它的力量。它不需要每天盯盘，不需要预测美联储下次决议，不需要知道下个季度哪家公司业绩超预期。它只要求投资者承认：市场长期会奖励资本和生产力增长，而普通人更适合用低成本方式分享这部分增长。</p>
<p>指数化还有一个隐含优势：它减少了身份焦虑。选择主动基金时，投资者总会忍不住比较谁更聪明、谁的经理更优秀、谁买到了更高回报的产品。指数化把问题拉回到资产类别本身，不再把长期计划押在某个英雄人物身上。它不需要你每年重新寻找赢家，只需要你持续留在市场里。</p>

<h2 id="enemy">五、投资组合最大的敌人通常是自己</h2>
<p>知道低成本、分散化和长期持有并不难，难的是在极端市场里仍然执行。2020 年 3 月的恐慌性下跌，许多人每天面对账户缩水、新闻轰炸、失业担忧和末日叙事。理性在那种环境里会变得非常稀缺。</p>
<p>人类大脑并不是为长期投资设计的。看到损失会本能逃跑，看到别人赚钱会本能跟随，看到群体恐慌会本能寻找出口。这些反应在现实危险中有用，在金融市场里却经常导致高买低卖。</p>
<p>更麻烦的是，媒体会放大这种本能。市场平稳上涨时，新闻语气温和；市场剧烈波动时，标题、音量和情绪密度都会提高，大脑会误以为“现在是特殊时刻，必须做点什么”。很多糟糕交易，就是在这种特殊感里发生的。</p>
<p>因此，投资者要提前区分两类信息。一类信息能改变长期资产配置，比如收入变化、家庭负债、退休时间、重大支出和风险承受能力；另一类只是市场噪声，比如一天的涨跌、某位分析师的短期判断、某个热点词的情绪发酵。长期组合不应该被第二类信息频繁改写。</p>

<h2 id="behavior">六、三种最常见的行为错误</h2>
<p>第一种是追涨杀跌。它不是因为投资者愚蠢，而是因为跟随群体符合人性。当身边所有人都在谈论某只基金、某个赛道、某类资产暴涨，不参与需要极强的意志力。可一旦买入理由只是“大家都在买”，风险已经埋下。</p>
<p>第二种是过度交易。每一次买卖都有成本，更重要的是买卖需要连续做对两次：先卖得对，再买得回来。很多人以为自己在优化组合，实际上是在用频繁操作增加错误概率。</p>
<p>第三种是把短期亏损解释为长期失败。市场下跌时，人会把眼前损失外推到未来，仿佛下跌会永远持续。长期投资最难的地方，正是在最痛苦的时候仍然承认：波动是市场的一部分，不是系统失效的证据。</p>

<h2 id="structure">七、靠意志力不如靠结构</h2>
<p>真正能帮助投资者穿越熊市的，不是临场理性，而是入场前建立的结构。自动扣款、明确配置比例、低成本基金、固定复盘周期和再平衡规则，都是把投资从情绪中隔离出来的结构。</p>
<p>在风暴里决定要不要系安全带，已经太晚了。安全带应该在出发前系好。投资也是如此，市场暴跌时再决定是否长期持有，往往会被恐惧打败；在平静时期就写下规则，并让系统自动执行，才更可靠。</p>
<p>许多普通人最后积累出可观资产，并不是因为他们选中了明星基金或踩准了牛熊切换，而是因为每个月自动投入一笔钱，长期不动，持续几十年。朴素、重复、低摩擦，往往比聪明和兴奋更接近复利。</p>

<h2 id="allocation">八、资产配置比单一选择更重要</h2>
<p>长期投资不能只讨论买什么基金，还要讨论股票和债券如何组合。股票提供长期增长，债券提供稳定性和再平衡弹药。一个经历过多次战争、通胀、经济衰退、互联网泡沫、金融危机和疫情冲击的组合，最重要的能力不是永远上涨，而是不让投资者提前出局。</p>
<p>一个简单而有效的思路，是根据自身年龄、收入稳定性、家庭责任和风险承受能力，设定长期股票与债券比例。年轻、现金流稳定、投资期限长，可以提高股票比例；接近退休、支出压力大、无法承受剧烈回撤，就需要更多防守资产。</p>
<p>资产配置的目标不是追求最刺激的回报，而是让自己能坚持。一个理论上收益更高、但会让你在下跌中崩溃的组合，并不适合你。适合自己的组合，才有机会真正持有到复利兑现。</p>
<p>这也是为什么“最优组合”不能只用历史回测决定。历史回测告诉你过去发生了什么，却不能告诉你在真实下跌中能否承受。一个人如果在账户回撤 20% 时已经睡不着，就不该配置一个可能回撤 50% 的组合。投资系统必须匹配人的心理承受力，否则纸面最优会变成现实最差。</p>

<h2 id="rebalance">九、再平衡：把低买高卖写进规则</h2>
<p>再平衡是一套简单但强大的机制。假设目标配置是 65% 股票和 35% 债券。当股票大涨，股票占比超过目标，就卖出一部分股票买债券；当股票大跌，股票占比低于目标，就卖出一部分债券买股票。</p>
<p>它的价值在于，把“低买高卖”从口号变成机械动作。市场狂热时，人性想加仓，再平衡要求你卖一点；市场恐慌时，人性想逃跑，再平衡要求你买一点。它不需要预测底部和顶部，只需要让组合回到既定比例。</p>
<p>再平衡不必太频繁。一年检查一次，或者当配置偏离目标达到一定幅度时行动，就足够了。频繁微调会增加成本和焦虑，规则越简单，越容易坚持。</p>

<h2 id="retirement">十、退休账户里的真正复利</h2>
<p>投资最动人的部分，不是少数人一夜暴富，而是普通人在几十年里通过纪律获得安全感。一个人在普通岗位上工作，每两周把一部分工资自动投入低成本组合，几十年不碰，退休时账户里积累出数十万美元，这就是复利最现实的样子。</p>
<p>这种路径并不耀眼，也很少出现在热门新闻里。它没有暴涨故事，没有惊险操作，也不需要每天证明自己比市场聪明。但它适合大多数人，因为大多数人真正需要的不是炫耀收益，而是未来生活的确定性。</p>
<p>复利最怕中断。高费率会侵蚀它，恐慌卖出会打断它，频繁交易会干扰它，过度集中会摧毁它。保护复利，就是保护时间、成本、分散和行为纪律。</p>

<h2 id="anti-risk">十一、抗风险不是没有波动，而是不被波动击穿</h2>
<p>抗风险投资不是追求账户永远不跌。没有波动的高收益通常不存在，承诺安全又高回报的产品更值得警惕。真正的抗风险，是在市场不可避免地下跌时，组合不会被单一风险击穿，投资者也不会被情绪迫使在最低点离场。</p>
<p>它包含三层防线。第一层是产品层：低成本、透明、分散。第二层是组合层：股票、债券、现金和不同资产之间合理配置。第三层是行为层：自动化、再平衡、少看噪声、不用短期情绪改长期计划。</p>
<p>很多人只重视第一层，忽视第二层和第三层。实际上，真正让人失败的往往不是产品本身，而是仓位过重、现金不足、急需用钱、恐慌卖出和追逐热点。抗风险要从账户设计延伸到生活现金流设计。</p>

<h2 id="practical-system">十二、普通人的执行系统</h2>
<p>第一，建立应急现金。至少覆盖几个月生活支出的现金缓冲，能避免在市场下跌时被迫卖出资产。没有现金垫，再好的长期组合也可能被短期生活压力击穿。</p>
<p>第二，选择低成本、宽基、透明的核心资产。不要把主要财富押在单一基金经理、单一行业或单一故事上。核心仓位应当尽量简单，越简单越容易坚持。</p>
<p>第三，设置自动投入。把投资行为从“想起来再做”变成工资到账后的固定动作。自动化不是为了偷懒，而是为了减少情绪干预。</p>
<p>第四，写下再平衡规则。比如每年固定一次，或者当股票比例偏离目标 5 个百分点以上时执行。规则写下来，市场极端时才有依靠。</p>
<p>第五，降低信息噪声。每天盯盘并不会提高长期收益，反而会增加操作冲动。长期投资者需要的是年度复盘，而不是小时级焦虑。</p>
<p>第六，把投资计划和家庭现金流放在一起。教育、养老、医疗、买房、失业风险和父母支持，都会影响投资期限。三年内要用的钱，不应该暴露在高波动资产里；十年以上不用的钱，才更适合承担股票波动。抗风险不是只看账户收益，而是让资产安排和生活责任彼此匹配。</p>
<p>第七，给自己写一份投资说明书。里面只需要写清楚四件事：为什么投资、买什么、什么时候再平衡、什么情况才允许改变计划。真正的作用不是让自己变得更专业，而是在市场最吵的时候，提醒自己不要临时发明一套新规则。</p>

<h2 id="annual-review">十三、年度复盘只问四个问题</h2>
<p>抗风险系统并不意味着一辈子不调整。真正的纪律不是僵硬，而是把调整限制在有理由、有节奏、有记录的框架内。年度复盘可以很简单，只问四个问题：收入和职业稳定性是否变化，未来三到五年的大额支出是否变化，家庭责任和负债结构是否变化，当前组合是否明显偏离既定配置。</p>
<p>如果答案都没有明显变化，就不要因为市场涨跌而重写计划。很多投资者每年真正需要做的事情，只是确认现金垫是否足够、继续自动投入、把偏离过大的资产调回目标比例。复盘的目的不是制造操作感，而是防止长期计划被短期情绪污染。</p>
<p>如果答案发生变化，也要先调整资产配置和现金流安排，而不是急着猜市场方向。比如失业风险上升，应先增加现金储备；孩子教育支出临近，应降低这部分资金的波动风险；退休时间提前，应逐步提高防守资产比例。投资系统服务于生活，而不是让生活被账户曲线牵着走。</p>

<h2 id="conclusion">十四、投资的终点是稳稳穿越周期</h2>
<p>《抗风险投资》提供的不是快速致富秘诀，而是一套让普通人少犯大错的系统。它的底层逻辑很清楚：不要把未来押在预测上，不要让高费率吃掉复利，不要相信自己能在恐慌中总是理性，不要让短期情绪摧毁长期计划。</p>
<p>真正有效的投资体系，应该能在牛市里不过度兴奋，在熊市里不被迫出局，在漫长平淡期仍然继续执行。低成本、分散化、长期持有、自动扣款和再平衡，正是把这些要求落到现实中的工具。</p>
<p>市场永远会有新的热点、新的危机和新的叙事，但普通人的核心问题很少改变：如何让今天的储蓄在未来变成安全感，如何在不确定世界里保住选择权。抗风险投资的答案并不复杂，却需要几十年如一日地执行。简单不等于容易，朴素也不等于平庸。能坚持的系统，才是最有价值的系统。</p>
"""


def _plain_text(html_text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(html_text))


def validate() -> None:
    _BASE_VALIDATE()
    failures: list[str] = []
    forbidden = [
        "B站", "bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中",
        "UP主", "up主", "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅",
        "投币", "收藏", "下期", "关注", "欢迎收看", "感谢大家", "三连", "BV1",
    ]
    post = base.INPUT_ORDER[0]
    article_path = base.ROOT / post.url_path.strip("/") / "index.html"
    article = article_path.read_text(encoding="utf-8")
    body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    plain = _plain_text(body_match.group(1)) if body_match else ""
    if len(plain) < 5200:
        failures.append(f"{post.slug}: body too short: {len(plain)}")
    for word in forbidden:
        if word in article:
            failures.append(f"{post.slug}: forbidden/source wording present: {word}")
    required_terms = [
        "抗风险投资", "低成本", "分散化", "长期持有", "指数基金", "主动管理",
        "费率", "复利", "自动扣款", "再平衡", "股票", "债券", "行为", "现金",
        "资产配置", "风险",
    ]
    for word in required_terms:
        if word not in article:
            failures.append(f"{post.slug}: missing required topic: {word}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links or len(h2) < 10:
        failures.append(f"{post.slug}: toc mismatch or too few h2: h2={len(h2)} links={len(links)}")
    cover_text = (base.ROOT / "images/posts" / post.slug / "cover.svg").read_text(encoding="utf-8")
    ET.fromstring(cover_text)
    for word in forbidden:
        if word in cover_text:
            failures.append(f"{post.slug}: forbidden/source wording present in cover: {word}")

    home = (base.ROOT / "index.html").read_text(encoding="utf-8")
    cards = re.findall(r'<a href="([^"]+)" class="a-block">', home)
    expected_cards = [
        "/ai-news-radar/",
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
        post.url_path,
        base.PREV_EXISTING_URL,
    ]
    if cards[: len(expected_cards)] != expected_cards:
        failures.append(f"homepage order mismatch: {cards[:len(expected_cards)]}")

    archive = (base.ROOT / "archive/index.html").read_text(encoding="utf-8")
    rss = (base.ROOT / "index.xml").read_text(encoding="utf-8")
    ET.parse(base.ROOT / "index.xml")
    if post.url_path not in archive:
        failures.append(f"archive missing {post.url_path}")
    if post.full_url not in rss:
        failures.append(f"rss missing {post.full_url}")
    taxonomy_expectations = [
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
    previous = (base.ROOT / base.PREV_EXISTING_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    if post.url_path not in previous:
        failures.append("previous existing article newer link missing")
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


base.ROOT = ROOT
base.DATE = "2026-08-04"
base.BASE_DT = datetime(2026, 8, 4, 11, 25, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/software-ai-application-investment-logic-agent-custom-software/"
base.PREV_EXISTING_TITLE = "软件与 AI 应用投资逻辑：从大模型商业化到 Agent 和定制软件"
base.SCRIPT_NAME = "publish-anti-risk-investing-system-20260804.py"
base.MANIFEST_NAME = "publish-anti-risk-investing-system-20260804-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="BV1j7Te65E9E",
        slug="anti-risk-investing-low-cost-diversification-long-term-system",
        title="抗风险投资：低成本、分散化与长期持有的投资系统",
        desc="把投资从预测游戏改造成生存系统：用低成本指数基金、分散化、自动扣款、资产配置和再平衡，降低情绪与高费率对复利的破坏。",
        category="投资体系",
        series="长期投资",
        tags=["抗风险投资", "指数基金", "长期投资", "低成本", "分散化", "资产配置", "再平衡", "复利", "行为金融", "风险管理"],
        minutes=22,
        body=BODY,
        cover_kicker="抗风险投资",
        cover_line="低成本 · 分散化 · 长期持有 · 再平衡",
        cover_theme=("#0f172a", "#0f766e", "#f59e0b"),
        duration=1775.308322,
        segments=799,
        chars=7798,
    )
]
base.PUBLISH_ORDER = list(reversed(base.INPUT_ORDER))
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    base.main()
