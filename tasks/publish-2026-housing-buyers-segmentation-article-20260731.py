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
spec = importlib.util.spec_from_file_location("base_publisher_housing_buyers_2026", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
_BASE_VALIDATE = base.validate


BODY = """
<p><img src="/images/posts/who-is-still-buying-houses-2026-property-market-segmentation/cover.svg" alt="2026 年，到底谁还在买房：楼市分化时代的四类真实需求"></p>
<p>2026 年的楼市，已经不是全民狂热的楼市。房价不再被默认上涨，买房也不再被默认等同于财富跃迁。年轻人不再轻易掏空六个钱包，刚需也不再因为焦虑而盲目上车，投资客更不敢像过去那样靠高杠杆搏短期暴涨。</p>
<p>舆论场里的主流声音很清楚：房价还可能继续分化，二手房流动性不足，远郊库存压力仍在，烂尾和交付风险依旧需要警惕，买房不再是闭眼赚钱的选择。于是很多人得出一个简单结论：都这个时候了，应该没人买房了。</p>
<p>但真实市场从来不是一句口号能概括的。投机退潮之后，并不是所有成交都消失了。相反，核心城市的改善盘、品质新房、优质学区房、高端住宅和稀缺核心资产，仍然有稳定成交。楼市真正发生的变化，不是“没人买房”，而是“乱买房的人少了，真正有需求、看得懂分化的人还在买”。</p>

<h2 id="end-of-speculation">一、全民炒房结束，结构性买房开始</h2>
<p>过去十几年，买房曾经被很多人理解为一张单边上涨的彩票。只要上车，就能享受城市扩张、信贷宽松、土地财政和人口流入带来的资产红利。那个阶段里，刚需、改善、投资、投机常常混在一起，很多人买房并不关心居住体验，只关心未来能不能涨。</p>
<p>2026 年的市场逻辑已经完全不同。投资投机型购房占比明显下降，炒房套利的空间被压缩，老破小、远郊盘、低品质库存和缺乏流动性的房源持续承压。楼市不再是统一上涨的红利市场，而是极致分化的价值市场。</p>
<p>这种分化意味着两个事实同时成立：一方面，很多房子确实不值得买，尤其是缺乏地段、配套、产品力和流通性的资产；另一方面，仍然有一部分房子具备居住价值、稀缺价值和抗跌价值。理解这一点，才能看懂为什么市场冷了，成交却没有完全停止。</p>
<p>真正的拐点，不是价格从上涨变成下跌，而是买房逻辑从“资产普涨”变成“资产筛选”。过去买房更像跟随大趋势，普通人只要不买得太离谱，就可能被周期托起来；现在买房更像做一次家庭资产审计，必须判断这套房在未来十年能不能住、能不能租、能不能卖、能不能承载家庭变化。</p>
<p>因此，判断 2026 年楼市不能只看成交量，也不能只看平均价格。平均数会掩盖分层：好地段的好产品仍然有人抢，差地段的差产品即使降价也难成交；大城市核心资产仍然有需求，小城市人口流出区域的房子可能长期缺乏接盘者。楼市从此更像一个分层市场，而不是一个统一市场。</p>

<h2 id="improvement-buyers">二、第一类买房人：36 到 45 岁的成熟改善家庭</h2>
<p>当下楼市最核心的购买力量，早已不是刚毕业的年轻人，而是 36 到 45 岁之间的成熟改善群体。他们经历过上一轮楼市周期，见过房价上涨，也见过市场降温，因此不再相信“买了就一定暴涨”。他们买房的理由非常现实：自住升级、生活迭代、家庭托底。</p>
<p>这批人往往在二十多岁时买过第一套房。那时预算有限、经验不足，只能选择面积偏小、地段偏远、物业一般、户型局促的刚需房。几年之后，家庭结构发生变化：结婚、生子、老人同住、孩子入学、工作半径稳定，原来的小房子已经支撑不了新的生活。</p>
<p>改善需求不是冲动消费。孩子需要更稳定的教育环境，老人需要更好的采光、通风、电梯和医疗配套，夫妻需要更高效的通勤和更完整的社区服务。对这类家庭而言，房子不是金融筹码，而是一整套生活系统。</p>
<p>更关键的是，2026 年给了改善家庭一个相对友好的置换窗口。经过多年调整，部分城市的房价水分已经被挤出，房贷利率处于低位，限购和交易政策不断优化，税费、补贴和置换政策也更加积极。对手里有积蓄、收入稳定、资产规划成熟的中年家庭来说，这是用更低成本完成居住升级的机会。</p>
<p>他们不是在盲目接盘，而是在做资产优化：卖掉流动性变差、品质落后、居住体验不足的老房子，换成核心地段、优质户型、好物业和强配套的改善房。楼市下行并没有消灭这类需求，只是让它变得更理性、更挑剔、更重视确定性。</p>
<p>改善置换还隐藏着一个重要逻辑：旧房越难卖，越要尽早承认资产质量差异。很多家庭不愿意降价卖出老房，结果被低流动性拖住，错过更好的改善窗口。真正成熟的置换，不是执着于过去买入价，而是比较未来十年的生活质量和资产质量。如果旧房长期跑输核心改善房，那么及时换仓，本身就是减少机会成本。</p>

<h2 id="settlement-demand">三、第二类买房人：追求城市扎根的真实刚需</h2>
<p>年轻人的购房意愿确实下降，长期租房也越来越被接受。但这并不等于所有刚需都消失了。对一部分城市定居者、新市民、外来打拼家庭来说，房子仍然不是投资品，而是安全感、归属感和城市权益的承载物。</p>
<p>租房解决的是居住空间，未必解决长期稳定。房租可能上涨，房东可能收回房源，合同到期可能被迫搬家，孩子落户、上学、就医、社区资源和长期生活安排，都可能因为租住状态而充满不确定。租房可以灵活，但灵活本身并不等于稳定。</p>
<p>因此，真正的刚需不会因为房价涨跌完全消失。他们买房不是为了短期赚钱，而是为了结束长期漂泊：不用频繁搬家，不用再看房东脸色，孩子能更稳妥地入学，家庭能在一座城市真正落地。</p>
<p>不过，2026 年的刚需也和过去不同。他们不再追求一步到位，不再迷信远郊规划，不再被低总价和概念包装带着走。更成熟的选择标准是：优先现房，优先成熟配套，优先地铁和通勤，优先主城或强产业片区，优先流动性，远离交付不确定和长期无人接盘的房源。</p>
<p>买得起并不等于必须买，但如果一个家庭的工作、教育、户籍和长期生活都已经绑定某座城市，那么在合理价格、低利率和可控风险下买一套能长期居住的房子，仍然是一种务实选择。</p>
<p>刚需最需要警惕的是“为了买而买”。真正的刚需不是任何房子都能满足。通勤过长、配套空心、交付不稳、物业混乱、学区不确定、二手市场无人问津的房子，即使总价低，也可能把家庭锁进更大的不确定性。刚需买房的底线，不是便宜，而是能稳定生活、风险可控、未来仍有退出通道。</p>

<h2 id="high-net-worth">四、第三类买房人：高净值人群的核心资产配置</h2>
<p>普通人讨论房子时，常常只盯涨跌；高净值人群看房子时，更重视资产避险、财富保值、抗通胀和家庭资产压舱。对他们来说，买房不是为了短线赚差价，而是为了把一部分资产放进长期稳定、稀缺、可使用、可传承的载体里。</p>
<p>2026 年的宏观环境并不轻松。股市波动，理财收益下降，存款利率持续走低，现金的实际购买力受到通胀和机会成本侵蚀。并不是所有资产都能同时具备稳定性、使用性和稀缺性。核心城市优质住宅，尤其是一线和强二线核心地段的大平层、洋房、别墅和稀缺好宅，仍然是部分资金愿意配置的硬资产。</p>
<p>这也解释了市场中看似矛盾的现象：远郊刚需盘、低品质库存持续降价无人问津，而核心地段的高端住宅仍然有价有市。富人并不是不知道楼市分化，恰恰是因为看懂了分化，才会避开普通资产，集中选择稀缺资产。</p>
<p>高净值买房的核心逻辑不是普涨，而是筛选。他们不买缺乏配套的远郊故事，不买流动性差的低质资产，不买无法穿越周期的普通库存。他们买的是城市中心资源、不可复制地段、稀缺景观、优质物业、长期圈层和家庭资产安全垫。</p>
<p>在普涨时代结束后，优质核心资产反而更能体现稀缺性。差房子越来越难卖，好房子越来越被挑剔资金集中选择。楼市不是没有价值，而是价值从“买什么都涨”回到了“只有少数资产值得长期持有”。</p>
<p>这种选择背后还有一个财富管理思路：资产组合不能只有高波动资产，也不能只有不断贬值的现金。优质不动产虽然流动性不如股票和基金，但它的使用价值、抵押价值和家庭传承属性，是其他资产难以完全替代的。高净值资金并不追求每一项资产都最高收益，而是追求资产负债表在周期里的稳定性。</p>

<h2 id="rational-investors">五、第四类买房人：看租金和流动性的理性投资者</h2>
<p>今天仍然买房的投资者，已经不再是过去那种高杠杆囤房、赌短期暴涨的投机客。真正留下来的，是极度谨慎、重视现金流和确定性的理性投资者。他们买房不靠故事，靠租金、地段、流动性和长期价值。</p>
<p>这类人不会追远郊新区，也不会相信概念包装。他们只看核心城市、核心地段、成熟配套、稳定租赁需求和可退出能力。优质小户型、地铁沿线、产业人口密集区域、学校和医院等资源附近的房源，才可能进入他们的选择范围。</p>
<p>在存款利率下降、理财收益走低的环境中，一部分闲置资金会寻找低波动的长期配置。核心城市优质小户型如果租赁需求稳定、空置风险较低、总价可控、流动性尚可，仍然能成为一种稳健资产。当然，这不再是暴利游戏，而是细水长流的资产管理。</p>
<p>理性投资和盲目炒房的区别，就在于是否尊重现金流和退出路径。不能稳定出租的房子，不能快速出售的房子，不能支撑家庭资产负债表的房子，即使价格便宜，也可能是陷阱。真正理性的投资者，不赌全民狂欢，只选择确定性更高的细分资产。</p>
<p>对普通投资者来说，还要把税费、装修、空置、维修、物业、贷款利息和机会成本全部算进去。很多看似有租金收益的房子，扣掉综合成本后并不划算。只有在租售比、持有成本、资金成本和未来流动性之间能形成基本平衡时，房产投资才有讨论价值。否则，所谓稳健只是一种错觉。</p>

<h2 id="not-buying-bad-houses">六、“别买房”的真实含义，是别买烂房</h2>
<p>今天网络上大量“别买房”的声音，本质上并不是否定所有居住需求，而是在提醒人们不要再用过去炒房的心态买房。别买烂房，别买劣质房，别买远郊无兑现能力的概念房，别买交付风险高的期房，别买缺乏流动性的资产，别用高杠杆赌短期上涨。</p>
<p>但很多人容易把“不要乱买房”理解成“永远不要买房”。这是一种新的极端。过去的极端是闭眼上车，现在的极端是全盘否定。真正清醒的判断，不是跟着情绪摆动，而是回到需求、价格、资产质量和家庭承受能力。</p>
<p>房子从来不只是金融产品。它同时承载居住、教育、通勤、养老、家庭关系、城市资源和心理稳定。只要有人需要定居，需要落户，需要孩子上学，需要照顾父母，需要在城市里建立长期生活秩序，楼市就不会彻底没有需求。</p>
<p>所以更准确的判断是：房子仍然重要，但不再神圣；买房仍然可能正确，但不再天然正确。过去很多家庭把买房当成人生标准答案，现在应该把它还原成一道具体的家庭决策题。答案因城市而异，因收入而异，因家庭阶段而异，也因具体房源而异。</p>

<h2 id="value-criteria">七、2026 年买房，只能买价值而不是买想象</h2>
<p>新的楼市规则很简单：价值能留下，想象会褪色。过去买房可以靠规划、概念、人口故事和信贷扩张；现在买房必须回到更硬的指标：地段是否真实稀缺，产业是否支撑人口，学校和医院是否已经存在，交通是否已兑现，物业是否可靠，户型是否好住，二手流动性是否足够。</p>
<p>一个房子能不能买，不能只看总价低不低，更要看它未来有没有接盘者。便宜但无人要的资产，可能不是机会，而是流动性陷阱。贵但稀缺、好住、有配套、有稳定需求的资产，反而可能更抗跌。</p>
<p>这就是 2026 年买房最重要的变化：买房不再考验胆量，而是考验筛选能力。过去敢买就可能赚钱；现在只有买对才可能守住价值。楼市从 beta 时代进入 alpha 时代，普通人更需要避开低质量资产。</p>

<h2 id="rent-or-buy">八、租还是买，关键看人生阶段和确定性</h2>
<p>租房和买房并不是天然对立。对工作城市不确定、收入不稳定、家庭结构未定、未来可能迁移的人来说，租房可以保留自由度，避免被错误资产锁住。买房不应该成为焦虑驱动的动作，更不应该成为面子工程。</p>
<p>但对已经确定城市、确定职业半径、确定家庭需求的人来说，长期租房的隐性成本也不能忽视。搬家成本、孩子入学、老人照护、生活稳定性、社区关系和心理安全感，都会进入家庭决策。买房有金融成本，租房也有不确定成本。</p>
<p>真正成熟的选择，是承认两者都有适用场景。买不起时不要硬买，买得起时也不必为了舆论证明自己清醒而拒绝一切购买。是否买房，最终取决于家庭现金流、城市确定性、居住周期、教育养老需求和标的质量，而不是别人一句“现在不能买”。</p>

<h2 id="final-framework">九、普通人的买房决策框架</h2>
<p>普通人如果在 2026 年考虑买房，至少要回答六个问题。第一，这套房解决的是刚性居住问题、改善问题，还是单纯投资冲动？第二，家庭现金流能否覆盖首付、月供、装修、税费和至少一到两年的风险缓冲？第三，房源是否已经具备真实配套，而不是依赖远期规划？</p>
<p>第四，二手市场是否有流动性，未来万一需要置换能不能卖得出去？第五，房子本身是否好住，包括户型、采光、通风、楼层、物业、社区品质和通勤效率？第六，买完之后，家庭生活质量是提升，还是被月供长期压垮？</p>
<p>如果这些问题回答不清楚，就不该急着买。如果答案足够清晰，且标的确实处在核心地段、成熟配套和可承受价格之间，那么买房仍然可能是理性选择。未来楼市不奖励冲动，只奖励清醒。</p>
<p>还有一条纪律必须放在最后：不要让月供吞掉生活。买房的目的，是让生活更稳定，而不是让家庭长期处在现金流窒息中。即使是优质房源，也要留足失业、降薪、疾病、老人照护和孩子教育的缓冲。没有缓冲的买房，本质上是在用家庭安全感交换资产焦虑。</p>
<p>真正好的买房决策，应该让家庭在心理上更踏实、在现金流上更稳健、在居住体验上更舒适、在未来选择上更有余地。如果买完之后只剩紧张、透支和后悔，那么即使房子位置不错，也未必是适合这个家庭的选择。</p>

<h2 id="conclusion">十、结语：不是没人买房，而是只有清醒的人还在买</h2>
<p>2026 年还在买房的人，并不是没有听见市场变化，也不是逆着时代情绪盲目冲进去。他们大多有明确的需求、清晰的预算、成熟的资产观和更严格的筛选标准。</p>
<p>改善家庭买的是生活升级，城市定居者买的是扎根底盘，高净值人群买的是核心资产和长期安全垫，理性投资者买的是租金、流动性和稳健价值。四类人共同说明一个事实：楼市的投机时代结束了，但居住需求、资产配置需求和核心城市稀缺资产的价值，并没有消失。</p>
<p>未来楼市不会回到全民狂欢，也很难简单走向全面崩盘。更可能出现的，是长期分化、价值重估、劣质出清、优质坚挺。看懂分层，看清需求，尊重现金流和家庭承受能力，才能真正看透这一轮楼市的底层逻辑。</p>
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
    if len(plain) < 5200:
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
    required = ["楼市", "改善", "刚需", "高净值", "核心资产", "租房", "学区", "利率", "流动性", "分化"]
    for word in required:
        if word not in article:
            failures.append(f"missing required topic: {word}")
    h2 = re.findall(r'<h2 id="([^"]+)">', article)
    links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
    if h2 != links or len(h2) < 9:
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

    cover_text = (base.ROOT / "images/posts" / post.slug / "cover.svg").read_text(encoding="utf-8")
    ET.fromstring(cover_text)
    for word in forbidden:
        if word in cover_text:
            failures.append(f"forbidden/source wording present in cover: {word}")
    ET.parse(base.ROOT / "index.xml")
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


base.ROOT = Path("/tmp/bv1ka-bv169-sparse.Nkhbld")
base.DATE = "2026-07-31"
base.BASE_DT = datetime(2026, 7, 31, 2, 30, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/anti-aging-life-blood-vessel-glycation-sleep-exercise/"
base.PREV_EXISTING_TITLE = "《抗老生活》：真正的抗老，是让血管重新年轻"
base.SCRIPT_NAME = "publish-2026-housing-buyers-segmentation-article-20260731.py"
base.MANIFEST_NAME = "publish-2026-housing-buyers-segmentation-article-20260731-changed-files.json"
base.CHANGED = set()
base.INPUT_ORDER = [
    base.Post(
        source_id="public-audio-bv1pr316we7n-20260731",
        slug="who-is-still-buying-houses-2026-property-market-segmentation",
        title="2026 年，到底谁还在买房：楼市分化时代的四类真实需求",
        desc="楼市投机退潮之后，并不是没人买房，而是只有改善家庭、城市定居刚需、高净值资产配置者和理性投资者仍在用更严格的标准筛选价值。",
        category="楼市观察",
        series="房地产周期",
        tags=["楼市", "买房决策", "改善需求", "刚需", "高净值", "核心资产", "租房", "学区房", "房贷利率", "房地产周期"],
        minutes=13,
        body=BODY,
        cover_kicker="2026 楼市分化",
        cover_line="改善 · 刚需 · 高净值 · 理性投资",
        cover_theme=("#111827", "#0f766e", "#f59e0b"),
        duration=784.576,
        segments=501,
        chars=4009,
    )
]
base.PUBLISH_ORDER = list(base.INPUT_ORDER)
base.validate = validate
base.copy_script_and_manifest = copy_script_and_manifest


if __name__ == "__main__":
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
    base.main()
    shutil.rmtree(Path(__file__).with_name("__pycache__"), ignore_errors=True)
