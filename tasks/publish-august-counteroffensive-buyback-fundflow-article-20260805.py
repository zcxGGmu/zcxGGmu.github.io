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

ROOT_HINT = Path("/tmp/blog-publish-bv1ch-20260805.path")
if not ROOT_HINT.exists():
    fallback = Path("/tmp/blog-publish-bv1j7-20260804.path")
    if fallback.exists():
        ROOT_HINT.write_text(fallback.read_text(encoding="utf-8").strip(), encoding="utf-8")
ROOT = Path(os.environ.get("BLOG_ROOT") or ROOT_HINT.read_text(encoding="utf-8").strip())
BASE_PATH = Path(__file__).with_name("publish-physical-ai-three-article-batch.py")
if not BASE_PATH.exists():
    BASE_PATH = ROOT / "tasks" / "publish-physical-ai-three-article-batch.py"

spec = importlib.util.spec_from_file_location("base_publisher_august_counteroffensive", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY = """
<p><img src="/images/posts/august-a-share-counteroffensive-buyback-fundflow-window/cover.svg" alt="8月A股反攻窗口：回购新高、资金低点与配置节奏"></p>
<p>8 月市场最关键的变化，不是指数已经给出多么强的右侧信号，而是多项底部区间指标开始同时靠近可配置位置。估值、股债性价比、成交活跃度、行业动量、个股交易位置、回购和资金流向，都在经历 7 月调整后进入重新评估阶段。</p>
<p>这组信号共同指向一个判断：市场已经不再处于前期过热阶段，配置窗口正在打开。它并不意味着马上出现单边急涨，也不意味着所有行业都能同步修复。更准确的说法是，风险收益比正在改善，三季度应当比 7 月调整中更积极一些。</p>
<p>真正需要把握的是节奏。当前市场底部条件在增多，但交易量、换手率和行业动量并没有全部回到极端冰点，因此反攻更可能是逐步酝酿，而不是一根长阳解决所有问题。投资上要从“恐慌中减仓”转向“低位中择优配置”。</p>

<h2 id="equity-bond">一、股债性价比重新回到有吸引力的位置</h2>
<p>判断权益资产是否值得配置，不能只看指数点位，更要看它相对于债券的吸引力。股债性价比的核心，是用权益隐含收益率与长期债券收益率比较，观察承担股票波动是否能够获得足够补偿。</p>
<p>7 月调整之后，主要股债联动指标明显改善。部分指标已经回到历史偏低区间，说明权益资产相对于债券的吸引力正在上升。虽然还没有达到过去几个极端底部的水平，但相较前期高位，风险补偿已经明显修复。</p>
<p>这一点很重要。市场真正危险的时候，往往是股债性价比被压低、风险补偿不足、投资者仍然兴奋。现在的状态相反：价格经历调整，预期有所降温，隐含回报开始抬升。对于中长期资金，配置价值已经比 7 月之前更清晰。</p>

<h2 id="absolute-valuation">二、绝对估值：多数宽基指数并不贵</h2>
<p>从绝对估值看，多数宽基指数仍处在相对可接受区间。沪深 300、中证 500、中证 1000 等指数的估值分位并不高，创业板相关指数估值相对更高，但也需要结合成长性、行业结构和未来盈利弹性来判断。</p>
<p>估值不是短期涨跌的充分条件，却是中期配置的安全垫。当大部分指数估值处在历史中低位置，市场继续大幅向下的空间会受到约束。尤其在政策、回购和资金面边际改善时，低估值更容易成为反弹基础。</p>
<p>需要区分的是，指数估值不贵，不等于所有个股便宜。结构性分化仍然存在，部分高景气赛道和主题品种估值仍高，低估值板块也可能缺乏盈利弹性。配置应当从整体估值安全垫出发，再落到行业景气和公司质量。</p>

<h2 id="valuation-dispersion">三、估值分化收敛，市场开始回到均衡</h2>
<p>估值分化程度是观察市场情绪的重要指标。行情火热时，高估值股票与低估值股票的差距会被拉大；市场调整时，估值分化会逐步收敛，说明前期拥挤交易正在降温。</p>
<p>当前全市场估值变异系数已经回落到较低区域，意味着高估值品种相对低估值品种的溢价不再像前期那么极端。这不是单纯的坏事，反而说明市场正在从单一风格过热转向更均衡的状态。</p>
<p>估值分化收敛后，后续机会会更依赖基本面兑现，而不是估值继续拔高。业绩能够改善、回购能够支撑、资金能够流入的方向，会比纯主题交易更有持续性。</p>

<h2 id="turnover">四、交易指标降温，但还不是极端冰点</h2>
<p>换手率和成交活跃度在 7 月明显回落，已经处于 2025 年以来区间低位附近。交易热度下降，说明前期过度活跃的短线资金正在退潮，市场从高情绪交易转向冷静定价。</p>
<p>不过，当前换手率仍高于 2023、2024 年一些更极端的低点。月度最大成交额相对前高的比例也只是回落，并没有降到历史深度冰点。这说明市场已经降温，但并没有完全失去交易活力。</p>
<p>这种状态适合逐步配置，而不是等待所有指标都打到最低。真正的绝对冰点往往难以精准捕捉，一旦等到所有指标都完美，价格可能已经提前反弹。更现实的策略，是在交易降温后分批进入，把仓位节奏和信号强弱匹配起来。</p>

<h2 id="industry-momentum">五、行业动量回到中低位置，分化修复正在酝酿</h2>
<p>行业层面的动量指标也在回落。以 MACD 为代表的趋势指标看，当前只有一部分行业仍保持正向动量，多数行业处在负动量状态。这说明市场并不是全面强势，而是经历了较充分的行业层面调整。</p>
<p>行业动量回落到中低位置后，下一阶段的重点不是追逐已经很强的方向，而是观察哪些行业率先从负动量中修复。真正值得配置的方向，往往是在市场冷却后仍能出现订单、盈利、政策或资金支撑的板块。</p>
<p>如果行业动量后续从低位扩散，市场反攻的广度会提升；如果只有少数主题反弹，行情仍会偏结构性。因此，8 月不宜只看指数，还要看行业扩散和强弱切换。</p>

<h2 id="stock-position">六、个股层面已经出现明显回落</h2>
<p>从个股交易位置看，站在年线上方的股票比例已经明显下降，接近过去弱势阶段的可比水平。相比指数，个股层面的回落更加充分，说明很多股票已经提前经历了较大幅度调整。</p>
<p>这类指标的意义在于，它能揭示指数背后的真实温度。指数可能因为权重股支撑看起来没有太弱，但大量个股已经跌回低位，说明微观层面的风险释放更充分。</p>
<p>个股位置回落后，后续反弹不会平均分配。现金流稳、盈利预期改善、回购积极、估值合理的公司，更容易在资金回流时率先修复；纯粹缺乏基本面支撑的低位股，则可能只是短期反抽。</p>

<h2 id="buyback">七、回购规模年内新高，是重要的底部支撑</h2>
<p>回购是判断市场底部力量的重要信号。企业愿意在低位回购，说明上市公司对自身价值和现金流有一定信心，也能在弱市中为股价提供边际支撑。</p>
<p>近期回购规模稳中有升，并达到年内较高水平。与此同时，减持规模出现收窄。回购增加、减持收敛，意味着产业资本层面对市场的态度正在改善。</p>
<p>这类信号通常不会立刻改变指数趋势，却会改善底部结构。市场最脆弱的时候，是价格下跌、回购不足、减持压力大、资金持续外流同时出现；当前至少在产业资本层面，已经开始出现更积极的边际变化。</p>

<h2 id="fund-flow">八、三大资金流向处于低点，反向信号开始出现</h2>
<p>资金流向指标同样值得重视。外资、融资资金、ETF 或其他场内资金代表不同类型投资者的风险偏好。当这些资金流向同步回落到低位时，往往意味着市场情绪已经较为谨慎。</p>
<p>当前综合资金流向指标已经回落到 2025 年以来低点附近，接近过去弱势阶段的水平。资金面看似偏弱，但从反向角度看，也说明卖压和谨慎情绪已经释放较多。</p>
<p>底部并不是资金已经全面流入时才出现。很多时候，配置窗口出现在资金流向最冷、但估值和回购开始改善的时候。等资金重新明显流入，价格往往已经完成一段修复。</p>

<h2 id="configuration-window">九、配置窗口打开，但需要分批和择优</h2>
<p>多项指标共同指向一个结论：市场已经具备配置价值。股债性价比改善，估值不贵，估值分化收敛，交易热度降温，行业动量回落，个股位置下降，回购上行，资金流向低位，这些信号叠加后，风险收益比明显好于前期。</p>
<p>但配置窗口不等于满仓冲锋。因为成交和换手并未降到极端低位，行业动量还需要修复，资金流入也没有完全确认，所以更适合采用分批买入、回撤加仓、右侧确认后提高仓位的方式。</p>
<p>方向上，应优先寻找三类资产：一是估值合理、盈利稳定、回购积极的核心资产；二是政策和产业趋势支撑明确、调整充分的成长方向；三是现金流较好、股息或回购能提供底部保护的公司。</p>

<h2 id="execution">十、执行节奏：先左侧底仓，再等待右侧扩散</h2>
<p>配置窗口打开后，最容易犯的错误是把“值得配置”理解为“立刻重仓”。更稳妥的做法，是先建立左侧底仓，用低位赔率参与潜在反攻；如果后续行业动量扩散、资金流向转正、成交温和放大，再逐步提高仓位。</p>
<p>左侧底仓更适合放在低估值、有回购、有现金流、有产业逻辑的方向。右侧加仓则应等待市场给出确认，例如站上关键均线的个股比例上升、更多行业 MACD 转正、回购继续维持高位、资金流向从低点回升。</p>
<p>这套节奏的好处是，不需要猜到最低点，也不需要在情绪最冷时一次性押注。只要指标继续改善，就有加仓依据；如果反攻失败，也能通过分批仓位保留防守空间。</p>

<h2 id="checklist">十一、后续跟踪清单：五个信号决定反攻质量</h2>
<p>第一，看回购是否持续。单月回购新高是积极信号，但如果后续不能延续，支撑力度会下降。连续性比单点规模更重要。</p>
<p>第二，看资金流向是否从低位修复。低点本身代表情绪冷却，转正才代表风险偏好回升。资金流向从低位改善，是反攻从酝酿走向确认的重要条件。</p>
<p>第三，看行业动量能否扩散。如果只有少数权重或主题拉指数，反弹质量有限；如果更多行业从负动量转正，行情持续性会更强。</p>
<p>第四，看成交是否温和放大。成交太弱说明资金参与不足，成交过热又容易回到拥挤交易。理想状态是温和放量，而不是情绪化爆量。</p>
<p>第五，看盈利预期是否稳定。估值底和资金底可以提供弹性，但真正支撑中期行情的还是盈利。如果盈利预期继续下修，反攻只能按交易修复处理；如果盈利预期稳定甚至上修，配置逻辑才会更扎实。</p>

<h2 id="risk">十二、风险：不要把底部指标误读为无风险</h2>
<p>底部指标改善，只说明赔率变好，不代表风险消失。若后续宏观数据继续走弱、政策力度低于预期、海外流动性重新收紧，或者市场成交继续萎缩，反攻节奏仍可能被拉长。</p>
<p>估值低也可能继续低估值运行，资金流向低点也可能在低位徘徊。真正的右侧确认，需要看到行业动量扩散、成交稳定回升、回购持续增强，以及资金流向从低位转正。</p>
<p>因此，8 月策略的关键词不是激进，而是积极。相比 7 月调整中的被动防守，当前更应该为反攻做准备；但相比牛市加速阶段，也必须保留仓位弹性和风险控制。</p>

<h2 id="conclusion">十三、结论：8 月酝酿反攻，三季度保持积极</h2>
<p>7 月调整之后，市场的多项指标已经回到可以配置的时间窗口。股债性价比改善、估值分化收敛、交易热度下降、个股位置回落、回购规模上行、资金流向处于低点，共同构成了 8 月酝酿反攻的基础。</p>
<p>这不是一句简单的看多口号，而是基于风险收益比改善后的策略转向。短期仍可能反复，但中期配置价值已经抬升。三季度应当在态度上更积极，在执行上更分批，在方向上更重视低位、高质量和资金边际改善的资产。</p>
<p>市场最好的窗口，往往出现在情绪尚未完全恢复、但底部指标已经开始转好的阶段。当前正接近这样的阶段。真正重要的不是猜到最低点，而是在赔率改善时把仓位和方向准备好。</p>
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
    if len(plain) < 3600:
        failures.append(f"{post.slug}: body too short: {len(plain)}")
    for word in forbidden:
        if word in article:
            failures.append(f"{post.slug}: forbidden/source wording present: {word}")
    required_terms = ["8 月", "反攻", "回购", "资金流向", "股债性价比", "估值", "换手率", "行业动量", "配置窗口", "三季度"]
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

    ET.parse(base.ROOT / "index.xml")
    rss = (base.ROOT / "index.xml").read_text(encoding="utf-8")
    archive = (base.ROOT / "archive/index.html").read_text(encoding="utf-8")
    if post.full_url not in rss:
        failures.append(f"rss missing {post.full_url}")
    if post.url_path not in archive:
        failures.append(f"archive missing {post.url_path}")
    for rel in [
        f"categories/{post.category}/index.html",
        f"series/{post.series}/index.html",
        f"tags/{post.tags[0]}/index.html",
    ]:
        if post.url_path not in (base.ROOT / rel).read_text(encoding="utf-8"):
            failures.append(f"{rel} missing {post.url_path}")
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
base.DATE = "2026-08-05"
base.BASE_DT = datetime(2026, 8, 5, 9, 30, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/tech-rebound-ai-computing-volume-growth-strategy/"
base.PREV_EXISTING_TITLE = "科技调整后的渐进式反弹：从涨价逻辑转向量增逻辑"
base.SCRIPT_NAME = "publish-august-counteroffensive-buyback-fundflow-article-20260805.py"
base.MANIFEST_NAME = "publish-august-counteroffensive-buyback-fundflow-article-20260805-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="BV1chMr6kEKD",
        slug="august-a-share-counteroffensive-buyback-fundflow-window",
        title="8月A股反攻窗口：回购新高、资金低点与配置节奏",
        desc="7月调整后，股债性价比、估值分化、交易热度、行业动量、回购规模和资金流向共同指向配置窗口打开，三季度应保持积极但分批执行。",
        category="投资研究",
        series="A股策略",
        tags=["8月反攻", "A股策略", "回购", "资金流向", "配置窗口", "估值", "换手率", "行业动量", "股债性价比", "三季度"],
        minutes=7,
        body=BODY,
        cover_kicker="8月反攻窗口",
        cover_line="回购新高 · 资金低点 · 配置节奏",
        cover_theme=("#111827", "#0f766e", "#facc15"),
        duration=395.064313,
        segments=271,
        chars=2526,
    )
]
base.PUBLISH_ORDER = list(reversed(base.INPUT_ORDER))
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    base.main()
