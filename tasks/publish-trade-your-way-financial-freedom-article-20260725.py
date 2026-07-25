from __future__ import annotations

import importlib.util
import json
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path("/tmp/hermes-video-publish-20260721-triple")
BASE_PATH = ROOT / "tasks" / "publish-physical-ai-three-article-batch.py"
SCRIPT_NAME = "publish-trade-your-way-financial-freedom-article-20260725.py"
MANIFEST_NAME = "publish-trade-your-way-financial-freedom-article-20260725-changed-files.json"


spec = importlib.util.spec_from_file_location("base_publisher", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)


SLUG = "trade-your-way-financial-freedom-positive-expectancy-r-multiple-position-sizing"
TITLE = "放下胜率执念：用正向期望、R 倍数和头寸规模构建交易系统"


BODY_ARTICLE = f"""
<p><img src="/images/posts/{SLUG}/cover.svg" alt="{TITLE}"></p>
<p>交易领域最危险的幻觉之一，是以为只要把买点找得足够准，就能通向财务自由。大量投资者花费绝大部分精力研究指标、形态、消息、宏观判断和所谓最佳入场信号，真正想要的其实只有一件事：每次都做对。</p>
<p>但市场不是考试。日常生活中，90% 的正确率意味着优秀；在金融市场里，90% 的胜率也可能把账户带向破产。决定一个交易系统能否长期活下来的核心，不是单次判断是否正确，而是整套系统的正向期望、亏损边界、盈利扩张能力、头寸规模和执行者本人的心理契合度。</p>
<p>《通向财务自由之路》的价值，正是把交易从主观预测、情绪反应和运气崇拜，拉回到概率系统、风险单位和可重复流程。它不承诺任何市场秘籍，也不崇拜高胜率，而是要求交易者像工程师一样设计系统：先定义风险，再控制亏损，让盈利奔跑，最后用合适的头寸规模把正向期望转化为长期复利。</p>

<h2 id="win-rate-trap">胜率陷阱：高正确率也可能亏到破产</h2>
<p>进入市场之后，人最本能的需求就是“我要判断正确”。买入后上涨会带来掌控感，买入后下跌会带来认错痛苦。于是很多人把交易能力等同于胜率，把系统评价简化为“十次能对几次”。</p>
<p>这种思路在金融市场里极其危险。假设一个系统胜率高达 90%，100 次交易里有 90 次盈利，每次赚 1000 元；剩下 10 次亏损，如果每次因为死扛、逆势加仓或没有止损而亏掉 15000 元，那么 90 次盈利带来 9 万元，10 次亏损拿走 15 万元，最终仍然亏损 6 万元。</p>
<p>这就是典型的破产陷阱。许多看似稳定的策略，例如卖出无保护的虚值期权，或者采用马丁格尔式加仓，短期会呈现几乎每天盈利的漂亮曲线。真正的风险不是平常的小波动，而是一次极端行情把此前所有微利全部吞掉，甚至直接爆仓。</p>
<p>高胜率策略之所以诱人，是因为它迎合人类不愿承认错误的本能。散户买入后被套，常常会关掉账户、拒绝复盘，告诉自己“不卖就不算亏”。这实际上是在用未来无限风险，换取当下不用面对失败的心理安慰。长期生存的第一课，就是承认自己不需要频繁做对，只需要在做错时亏得足够小，在做对时赚得足够多。</p>

<h2 id="expectancy">正向期望：交易系统的真正生命线</h2>
<p>评估一个策略是否值得执行，核心指标是期望收益，也就是一套策略在大量重复之后，平均每次交易能产生多少净回报。它不是单看胜率，也不是单看某次暴利，而是把胜率、亏损概率、平均盈利和平均亏损放在同一张表里计算。</p>
<p>一个简单的摸球游戏可以说明问题。袋子里有 100 个球，60 个蓝球代表亏损，40 个红球代表盈利。摸到蓝球亏 1 元，摸到红球赚 10 元。这个游戏的胜率只有 40%，大多数单次体验都是失败；但它的期望收益是 40% × 10 - 60% × 1 = 3.4 元。只要重复足够多次，大数定律会让正向期望显现出来。</p>
<p>趋势跟踪系统也有类似特征。很多优秀趋势交易者的历史胜率只有 30% 到 40%，大部分时间都在用小额亏损试探市场方向。但一旦捕捉到大级别趋势，单笔收益可能达到初始风险的 5 倍、10 倍甚至 20 倍。少数大额盈利覆盖大量小亏，才是系统长期盈利的来源。</p>
<p>因此，成熟交易者关注的不是“下一笔会不会涨”，而是“如果我把这套规则重复一千次，它是否具备正期望”。当策略在数学上为正，短期连续亏损就只是概率分布中的噪音；当策略在数学上为负，再高的单次自信也只是运气。</p>

<h2 id="entry-signal">入场信号被高估：买点只是概率游戏的门票</h2>
<p>普通投资者往往把 80% 的精力放在入场信号上：技术指标交叉、形态突破、宏观数据、消息验证、估值分位、资金流向，所有努力都指向一个目标：找到最好的买点。</p>
<p>但随机入场实验揭示了一个反直觉事实：在长周期交易中，入场本身的重要性远低于离场和头寸管理。交易员汤姆·巴索曾与范·K·撒普合作，设计过完全随机的入场系统：面对一篮子流动性较好的期货品种，用抛硬币决定做多还是做空，完全不参考技术指标和基本面。</p>
<p>这个系统并没有因为随机入场而破产。原因在于，它配备了严格的离场规则和仓位管理：亏损达到预设边界就退出，趋势正确时则让利润继续奔跑。随机入场带来大量小亏，但机械化离场避免了灾难性亏损；一旦碰上大趋势，盈利端的非对称收益足以覆盖摩擦成本。</p>
<p>这个实验并不是鼓励随便买卖，而是打破预测神话。入场信号只是给交易者一张参与概率游戏的门票。真正决定最终结果的，是入场之后如何处理错误、如何保护利润、如何根据风险调整仓位。把全部注意力放在预测上，本质上是在和随机性硬碰硬；把系统建立在离场和风险单位上，才是在利用随机性。</p>

<h2 id="r-multiple">R 倍数：把所有盈亏统一成风险单位</h2>
<p>交易记录如果只写“赚了 3000 元”或“亏了 10%”，很容易误导自己。绝对金额无法说明这笔交易承担了多少初始风险，也无法比较不同资产、不同账户规模和不同波动环境下的决策质量。</p>
<p>R 倍数提供了一套统一语言。这里的 R，代表入场前预先定义的最大亏损金额，也就是初始风险。所有交易结果都用 R 的倍数衡量：赚 3R，说明用 1 个风险单位换回 3 个风险单位；亏 1R，说明损失控制在预设边界内。</p>
<p>假设以每股 100 元买入一只股票，止损设在 90 元，每股初始风险为 10 元，买入 100 股，则总初始风险为 1000 元，这就是 1R。如果最终在 130 元卖出，总盈利 3000 元，这笔交易就是 +3R。</p>
<p>另一个人同样赚了 3000 元，但如果他买入 100 股时把止损设在 50 元，总初始风险是 5000 元，那么这笔交易只有 +0.6R。账面盈利相同，风险效率完全不同。R 倍数让交易者从“我赚了多少钱”转向“我用多少风险换回多少收益”。</p>
<p>更重要的是，R 倍数能过滤绝对金额带来的恐惧和贪婪。无论是交易高波动商品期货，还是交易低波动蓝筹股，记录本里都只有一件事：每一笔投入了多少 R，回收了多少 R。交易因此从情绪判断变成工程化概率管理。</p>

<h2 id="stop-loss">止损离场：亏损边界必须在入场前完成</h2>
<p>止损不是亏损后的临时决定，而是买入前就必须完成的系统设计。很多人会在下单前口头说“跌到哪里就卖”，但当价格真正触及红线时，大脑会立刻开始找借口：基本面没变、只是洗盘、再等等、补仓摊低成本。一次普通亏损，就这样被拖成灾难性回撤。</p>
<p>合格的止损规则，首先要把止损视为买入假设失效的客观条件，而不是心理安慰。止损位要根据资产波动、结构位置和策略逻辑提前计算，并且必须反向决定持仓数量。</p>
<p>例如账户总资金 100 万元，单笔最大风险限定为 1%，即 1 万元。如果买入一只小盘股，当前价格 50 元，合理止损空间需要留出 5 元，那么持仓数量最多为 2000 股。因为 2000 股 × 5 元 = 1 万元，刚好等于 1R。如果买入波动更低的大盘股，止损空间只需要 1 元，则可以持有 1 万股。</p>
<p>这说明止损不是买完以后再考虑卖点，而是在入场前就锁定最大损失，并由最大损失反推出仓位。只要这道边界被执行，即使连续遭遇坏运气，账户也仍然保留继续参与市场的资格。</p>

<h2 id="profit-exit">盈利离场：让利润奔跑，而不是落袋为安上瘾</h2>
<p>如果止损负责截断错误，盈利离场就负责扩大利润。普通投资者常见的行为，是股票刚刚上涨一点就害怕利润回吐，急忙卖出，把账户里堆满 +0.5R、+0.8R 的小盈利。问题在于，这些小盈利根本无法覆盖必然出现的 -1R 亏损。</p>
<p>具备正向期望的系统，必须在盈利端引入机械化规则，让利润有机会扩张到 3R、5R、10R 甚至更高。趋势跟踪系统常见做法，是不提前预测目标价，而是让离场信号随着价格上涨动态上移。只要趋势没有客观破坏，就继续持有；一旦跌破规则定义的结构位置，再退出。</p>
<p>海龟交易法的经典通道退出规则，就是这一逻辑的代表。入场可以基于突破，盈利离场则完全不依赖主观预测。价格保持强势时，系统强制持有；价格跌破过去一段时间的低点时，系统退出。震荡期会带来大量小亏和微利，单边趋势期则可能捕捉少数巨大 R 倍数收益。</p>
<p>盈利离场本质上是一场对抗人性的训练。人天然厌恶账面利润回撤，容易把短暂安全感看得比长期期望更重要。真正的系统交易，要求交易者容忍利润回吐的一部分，以换取捕捉大趋势的机会。</p>

<h2 id="position-sizing">头寸规模：决定账户生死和财富量级</h2>
<p>在正向期望和离场规则之后，真正决定账户曲线的，是头寸规模。它回答的问题不是买什么，也不是何时买，而是“这一笔到底投入多少风险”。</p>
<p>拉尔夫·文斯曾做过一个经典模拟：40 位高学历参与者玩一个胜率 60%、盈亏比 1:1 的正向期望游戏，每人 1000 美元初始资金，连续交易 100 次。按理说，只要每次下注比例很小，大多数人最终会盈利；结果 40 人中有 38 人破产。原因不是方向错误，而是下注比例失控。</p>
<p>人在连续亏损后急于回本，会加大下注；连续盈利后害怕失去利润，又缩小下注。这样的资金分配方式，让一个原本正期望的游戏变成了破产机器。市场并不需要真正打败交易者，只要给出几次正常连亏，就能摧毁过度下注的人。</p>
<p>专业资金管理通常把单笔 1R 控制在总权益的 1% 到 2% 之间。账户 50 万元，单笔风险 1%，就是每笔最多亏 5000 元。即使连续 10 次止损，回撤也大约在 10% 左右，仍然可恢复；如果单笔风险是 10%，同样 10 次连亏足以让账户腰斩，数学和心理都会陷入困境。</p>

<h2 id="drawdown">回撤不对称：先活下来才有复利</h2>
<p>亏损和盈利不是对称的。亏 10%，需要涨 11.1% 才能回本；亏 25%，需要涨 33.3%；亏 50%，需要涨 100%。回撤越大，回本所需收益率呈非线性上升。</p>
<p>这就是为什么头寸规模比预测更重要。一个稍差但风险受控的系统，有机会长期修正；一个看似聪明但频繁重仓的系统，只需要一次黑天鹅就可能结束。宏观政策、公司造假、流动性冻结、隔夜跳空、交易系统故障，都可能让价格直接越过止损位。只有在原始仓位足够小的前提下，滑点和突发风险才不会摧毁账户。</p>
<p>投资的第一目标不是赚快钱，而是不被淘汰。只有留在牌桌上，正向期望才有机会通过时间发挥作用；一旦本金被毁灭，再好的系统也没有执行载体。</p>

<h2 id="personal-fit">个人契合：最好的系统必须适合执行者</h2>
<p>同一套策略，给不同人使用，结果可能完全相反。有人能长期执行并取得稳定收益，有人却在几次亏损后自行修改规则，最终把系统优势破坏掉。差异不在策略，而在个人契合。</p>
<p>趋势跟踪策略通常胜率不高，经常小亏，还要求交易者在盈利回撤时继续持有。如果一个人极度需要高正确率，无法忍受连续止损，或者看到账面利润回吐就焦虑，那么再优秀的趋势系统也不适合他。强行执行，只会引发自我破坏：该止损时扛单，该持有时提前卖出，该轻仓时重仓。</p>
<p>建立系统前，必须先清点自己。每天能花多少时间复盘？最大回撤到多少会影响睡眠？能否接受连续亏损？更适合短周期还是长周期？是否能严格执行规则？真正有效的投资框架，必须像量身定制的衣服，贴合交易者的心理承受力、时间结构和资金目标。</p>
<p>系统与人匹配之后，纪律才不再是痛苦的自我压迫，而会变成自然的一致性。长期财富不是来自某个神奇指标，而是来自规则和执行者之间的稳定配合。</p>

<h2 id="system-checklist">一套可执行交易系统的检查清单</h2>
<p>第一，定义市场与周期。系统交易哪些资产，持仓周期多长，适合趋势、震荡还是价值回归。第二，定义入场条件。入场可以简单，但必须可重复，不能每次靠临场感觉。第三，定义初始风险 R。每笔交易下单前，就要知道错在哪里、亏多少必须退出。</p>
<p>第四，定义止损规则。止损位置不能随情绪移动，必须服务于假设失效。第五，定义盈利离场。利润如何奔跑，何时移动保护线，何时确认趋势破坏。第六，定义头寸规模。单笔 1R 占账户权益多少，总组合最大风险暴露多少，相关性资产如何合并计算。</p>
<p>第七，定义复盘制度。每笔交易都记录入场理由、初始风险、结果 R 倍数、是否执行规则。第八，定义暂停条件。当连续亏损、回撤超过阈值、心理状态失控或市场环境明显变化时，系统如何降速。第九，定义个人契合。规则是否适合自己的时间、性格、资金和睡眠质量。</p>
<p>只有这些问题被写下来，并能在真实交易中被执行，交易才从主观博弈走向概率系统。</p>

<h2 id="ordinary-investor">普通投资者如何使用这套框架</h2>
<p>这套方法并不只属于期货交易者或职业短线交易者。普通股票投资者同样需要把每一次买入转化为风险单位。买入前先写下三个数字：入场价格、假设失效价格、愿意承担的最大账户亏损比例。只要这三个数字没有写清楚，买入就不是交易计划，而是情绪下注。</p>
<p>长期投资者也需要 R 倍数思维。价值投资不是不止损，也不是永远持有，而是要区分价格波动与投资假设失效。如果一家公司的竞争优势、盈利能力、资产负债表或行业逻辑已经恶化，却仍然用“长期主义”拒绝退出，本质上仍是在把小错拖成大错。</p>
<p>同样，指数投资者也可以借鉴头寸规模。宽基指数长期可能具备更高胜率，但如果在短期高估、收入不稳、备用金不足时一次性重仓，仍然会因为回撤和现金流压力被迫低位卖出。正向期望必须配合可承受的仓位，才能真正穿越周期。</p>
<p>因此，这套框架的普适意义是：任何投资行为都要先问风险，再问收益；先问系统能否重复，再问单次机会是否诱人；先问自己能否执行，再问市场是否配合。</p>

<h2 id="conclusion">结论：财务自由来自可重复的正期望系统</h2>
<p>市场充满随机性，因此预测永远不可能成为稳定自由的根基。真正可靠的道路，是建立一套可重复、可度量、可执行、与自己契合的正向期望系统。</p>
<p>放下胜率执念，并不意味着放弃研究，而是把研究重心从“我能不能每次都猜对”转向“我做错时亏多少，做对时赚多少，长期重复是否为正”。R 倍数让风险被统一计量，止损离场控制亏损，盈利离场扩大利润，头寸规模保护生存权，个人契合保证规则能被执行。</p>
<p>交易最终不是预测市场，而是管理自己与概率之间的关系。财务自由也不是某次暴利带来的奇迹，而是在不确定市场中持续执行正期望系统后，时间给出的复利结果。</p>
<p><em>本文为交易系统与投资方法研究，不构成任何个性化投资建议。金融市场存在本金损失风险，任何策略都需经过充分回测、压力测试和小规模验证后再执行。</em></p>
"""


def configure() -> None:
    base.__file__ = __file__
    base.ROOT = ROOT
    base.DATE = "2026-07-25"
    base.BASE_DT = datetime(2026, 7, 25, 23, 59, tzinfo=timezone(timedelta(hours=8)))
    base.PREV_EXISTING_URL = "/2026/housing-as-durable-consumer-good-depreciation-k-shaped-market/"
    base.PREV_EXISTING_TITLE = "房子为什么必然是消费品：耐用消费品定位、折旧逻辑与楼市 K 型分化"
    base.SCRIPT_NAME = SCRIPT_NAME
    base.MANIFEST_NAME = MANIFEST_NAME
    base.CHANGED = set()

    post = base.Post(
        source_id="BV1BtEG67Ea7",
        slug=SLUG,
        title=TITLE,
        desc="交易长期盈利不靠预测神话和高胜率崇拜，而靠正向期望、R 倍数、止损离场、盈利离场、头寸规模与个人心理契合，共同构成可重复执行的概率系统。",
        category="投资研究",
        series="交易系统",
        tags=["通向财务自由之路", "交易系统", "正向期望", "胜率", "盈亏比", "R倍数", "止损", "头寸规模", "趋势跟踪", "行为金融"],
        minutes=16,
        body=BODY_ARTICLE,
        cover_kicker="交易系统",
        cover_line="正向期望 · R 倍数 · 头寸规模",
        cover_theme=("#020617", "#4c1d95", "#38bdf8"),
        duration=1957.558313,
        segments=773,
        chars=8581,
    )
    base.INPUT_ORDER = [post]
    base.PUBLISH_ORDER = [post]
    base.copy_script_and_manifest = copy_script_and_manifest


def copy_script_and_manifest() -> None:
    tasks_dir = ROOT / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve()
    dst = (tasks_dir / SCRIPT_NAME).resolve()
    if src != dst:
        shutil.copyfile(src, dst)
    base.rec(tasks_dir / SCRIPT_NAME)
    manifest_path = tasks_dir / MANIFEST_NAME
    all_changed = sorted(
        base.CHANGED
        | {
            "categories/index.html",
            "series/index.html",
            "tags/index.html",
            f"tasks/{SCRIPT_NAME}",
            f"tasks/{MANIFEST_NAME}",
        }
    )
    manifest_path.write_text(json.dumps(all_changed, ensure_ascii=False, indent=2), encoding="utf-8")
    base.rec(manifest_path)


def extra_validate() -> None:
    post = base.INPUT_ORDER[0]
    article_path = ROOT / post.url_path.strip("/") / "index.html"
    article = article_path.read_text(encoding="utf-8")
    body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
    body = body_match.group(1) if body_match else article
    plain = re.sub(r"<[^>]+>", "", body)
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
    ]
    required = ["正向期望", "R 倍数", "头寸规模", "止损", "盈利离场", "胜率", "盈亏比", "个人契合"]
    failures: list[str] = []
    if len(plain) < 5600:
        failures.append(f"{post.slug}: body too short {len(plain)}")
    for word in forbidden:
        if word in article:
            failures.append(f"{post.slug}: forbidden wording {word}")
    for word in required:
        if word not in article:
            failures.append(f"{post.slug}: missing required term {word}")
    if post.source_id in article or "source_id" in article:
        failures.append(f"{post.slug}: source id leaked into article")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    toc = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != toc:
        failures.append(f"{post.slug}: toc mismatch")
    ET.fromstring((ROOT / "images/posts" / post.slug / "cover.svg").read_text(encoding="utf-8"))
    manifest_path = ROOT / "tasks" / MANIFEST_NAME
    manifest = set(json.loads(manifest_path.read_text(encoding="utf-8")))
    missing = [p for p in base.CHANGED if p not in manifest]
    if missing:
        failures.append(f"manifest missing changed files: {missing[:10]}")
    if failures:
        raise SystemExit("\n".join(failures))


def main() -> None:
    configure()
    for pycache in ROOT.rglob("__pycache__"):
        shutil.rmtree(pycache)
    base.main()
    extra_validate()


if __name__ == "__main__":
    main()
