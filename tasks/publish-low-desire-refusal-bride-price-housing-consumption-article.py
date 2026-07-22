from __future__ import annotations

import importlib.util
import json
import re
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path("/tmp/hermes-video-publish-20260721-triple")
BASE_PATH = ROOT / "tasks" / "publish-physical-ai-three-article-batch.py"
SCRIPT_NAME = "publish-low-desire-refusal-bride-price-housing-consumption-article.py"
MANIFEST_NAME = "publish-low-desire-refusal-bride-price-housing-consumption-changed-files.json"


spec = importlib.util.spec_from_file_location("base_publisher", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)


BODY_ARTICLE = """
<p><img src="/images/posts/low-desire-refusal-bride-price-housing-consumption/cover.svg" alt="当底层牛马不再入套：拒绝高彩礼、高房价与高消费"></p>
<p>高彩礼、高房价、高消费，曾经共同构成普通人生活里的三重套索。一个人刚进入社会，就被“精致生活”的广告语言推着消费；到了婚恋年龄，又被彩礼、婚礼、婚房和面子工程推着负债；进入家庭叙事之后，三十年房贷、孩子教育、医疗养老和职场服从，又把未来的时间一并抵押出去。</p>
<p>这套机制之所以能长期运转，不只是因为它会制造欲望，更因为它会制造恐惧。怕被同龄人甩开，怕结不了婚，怕没有房子就没有资格谈未来，怕孩子输在起跑线，怕失去工作后还不起贷款。恐惧一旦被制度、市场和舆论包装成“正常人生”，普通劳动者就会主动走进一条被设计好的流水线。</p>
<p>但当收入增长跟不上生活成本，当努力换不来对等回报，当买房、结婚和消费不再像过去那样带来安全感，底层群体开始出现一种安静而坚定的退出：不接盘，不入套，不为虚无的体面牺牲长期生存安全。真正让既得利益者紧张的，不是某一次抗议，而是越来越多人开始用合法、低成本、低欲望的方式拒绝继续燃烧自己。</p>

<h2 id="assembly-line">被设计好的生活流水线</h2>
<p>过去的普通人生轨迹，像一条被精密设计的流水线。二十多岁接受消费主义训练，用刚进入职场的微薄薪水购买身份标签；三十岁前在婚恋焦虑中面对高额彩礼和婚礼成本，甚至让父母掏空积蓄；随后为了婚房，把三十年的劳动时间打包抵押给银行，换来一张高位接盘的房产证。</p>
<p>这条流水线看起来是个人选择，实质上却是多方利益的合谋。品牌商需要年轻人持续消费，婚恋产业需要焦虑维持成交，房地产需要刚需接盘，银行需要长期房贷，地方财政曾经依赖土地出让，职场管理者也乐于拥有一批背负贷款、不敢轻易反抗的员工。</p>
<p>只要普通人相信“成家立业”只有这一种路径，相信房产是唯一门票，相信高消费代表体面，这台抽水机就能不断把底层劳动者的剩余价值向上输送。问题在于，当成本高到需要透支几代人的生命，这套叙事就会从人生指南变成债务陷阱。</p>

<h2 id="consumption">高消费退潮：精致叙事失去魔力</h2>
<p>最先受到冲击的是消费主义。过去，品牌只要制造身份差异，就能让年轻人为了手机、服饰、餐厅、旅行和轻奢品不断掏钱。营销语言把“不消费”包装成落伍，把“买不起”包装成失败，把“精致”包装成通往中产的通行证。</p>
<p>现在越来越多普通人开始反向消费。平替商品、大型折扣、二手交易、极简主义和低成本生活，正在替代过去那套面子消费。年轻人不再为了朋友圈的虚荣去支付溢价，不再为了品牌故事牺牲现金流，也不再相信一件商品能真正改变自己的阶层位置。</p>
<p>这让依赖焦虑营销的品牌商感到不适。失去庞大底层基底之后，再高级的营销故事也难以维持。所谓消费降级，表面是购买力下降，深层是信念退潮：普通人开始把长期安全感放在虚荣符号之前，把现金流放在面子之前，把真实生活放在广告叙事之前。</p>

<h2 id="bride-price">高彩礼退潮：婚姻不再自动绑定债务</h2>
<p>高彩礼把婚姻从亲密关系异化成资产转移。对于许多底层男性家庭而言，彩礼不是一次礼俗支出，而是沉重债务；对于一些家庭而言，彩礼又被纳入家庭财富再分配，甚至成为给儿子买房、偿还债务、维持面子的筹码。</p>
<p>当越来越多年轻人拒绝高彩礼、选择不婚不育，或者坚持低成本婚姻，传统婚恋利益链就会松动。婚庆公司、相亲机构、彩礼中介化的家庭算盘，以及依赖人口红利的长期结构，都会感受到压力。</p>
<p>更深层的变化在于，婚姻和生育不再被视为无条件义务。过去的道德话语常常把“不结婚”“不生育”定义成自私或失败，但当现实成本已经超过个体承受能力，拒绝繁衍不再是叛逆，而是一种对风险的自我保护。没有合理分配、平等尊重和基本保障，就很难要求底层继续提供下一代燃料。</p>

<h2 id="housing">高房价退潮：最大的接盘链条开始卡顿</h2>
<p>真正动摇财富分配结构的，是普通人对高房价的转身。房子长期不只是居住空间，而是绑定户籍、教育、医疗、婚姻资格和阶层想象的超级杠杆。正因为它被赋予太多意义，无数普通人才愿意背负三十年房贷，在不敢辞职、不敢生病、不敢反抗的状态里换取一份脆弱安全感。</p>
<p>房价泡沫能够维持，依赖的是一代又一代底层接盘者不断入场。房地产开发商依赖销售回款，金融机构依赖长期利息，地方财政曾经依赖土地收入，许多家庭也把房子当作唯一资产增值工具。只要普通人相信“再贵也得买”，泡沫就能继续滚动。</p>
<p>但当房价需要透支几代人的生命，当资产升值神话被现实打破，当租房、回县城、降低欲望成为更理性的选择，“不买房、不接盘”就会变成心照不宣的共识。售楼处冷清、成交下滑、开发商债务爆雷、银行优质房贷投放困难，背后都是同一个信号：底层燃料不愿继续燃烧。</p>

<h2 id="control">焦虑控制的核心：债务让人更容易被拿捏</h2>
<p>高彩礼、高房价和高消费之所以有效，是因为它们共同制造了债务和软肋。一个背着房贷、车贷、彩礼贷、消费贷，还要承担孩子教育和家庭开支的人，在职场上很难真正自由。他不敢轻易离职，不敢拒绝加班，不敢维护权益，也不敢和上级撕破脸。</p>
<p>这就是焦虑控制的核心。资源被人为变得稀缺，稀缺又被绑定到婚姻、住房、教育和身份上，最终转化成普通人的服从动力。所谓奋斗叙事，很多时候只是把结构性压力包装成个人责任，把分配问题转化为个人不够努力。</p>
<p>当一个人没有高负债，没有婚育焦虑，没有必须维持的高消费身份，管理者就很难用“不干就滚”来压制他。低欲望不一定意味着消沉，它也可能意味着劳动者重新获得议价空间。一个月薪不高但生活成本更低的人，反而更有底气拒绝不合理的加班、PUA 和末位淘汰。</p>

<h2 id="labor">低欲望不是躺倒，而是退出被收割的剧本</h2>
<p>低欲望常被批评为不奋斗、不上进、不负责任。但如果一套奋斗剧本的终点只是更高债务、更低安全感和更少人生选择，那么退出剧本本身就是理性行为。普通人不是不想过好生活，而是不愿再用未来几十年的自由去换一个被定价过高的体面符号。</p>
<p>这种退出通常不是激烈对抗，而是安静的不配合。不买不需要的商品，不为高彩礼妥协，不在高位接盘房产，不为了虚荣社交透支，不为了老板的画饼牺牲健康。这些选择单独看很小，汇集起来却会改变需求、利润和权力关系。</p>
<p>旧秩序最怕的并不是抱怨，而是沉默退出。抱怨仍然承认游戏重要，退出则意味着游戏失去玩家。当底层不再主动追逐那些被包装出来的目标，许多依赖焦虑运转的商业模式和管理方式都会失灵。</p>

<h2 id="panic">谁先慌了：资本、地产、婚恋与管理者</h2>
<p>最先慌的是依赖消费主义的品牌和平台。当年轻人减少冲动消费，营销话术的边际收益就会下降。第二个慌的是婚恋和婚庆产业。当高彩礼不再被自动接受，婚姻市场中的许多附加收费和中介环节都会被重新审视。</p>
<p>第三个慌的是房地产和金融链条。当普通人不愿高位接盘，房地产高周转模式就失去现金流支撑，土地财政、开发商债务和银行房贷资产都会受到影响。第四个慌的是习惯低成本用工的管理者。当年轻人不再被房贷和家庭支出牢牢锁住，职场控制就会变得更难。</p>
<p>这些群体的共同点，是长期把底层生活安全感当作可消耗资源。他们希望普通人消费、结婚、买房、生娃、加班，却很少真正关心普通人是否获得了对等回报。当普通人开始算账，许多曾经被包装成天经地义的要求，都会露出利益结构的本来面目。</p>

<h2 id="failed-persuasion">规劝失效：旧话术已经无法重新点燃欲望</h2>
<p>面对低欲望和不入套，旧秩序会本能地尝试规劝。舆论会批评年轻人不奋斗，专家会呼吁尽早买房和结婚，金融机构会降低首付比例，楼市会推出各种促销，婚恋市场也会呼吁彩礼降温，把旧商品重新包装成性价比更高的新选择。</p>
<p>但问题不在包装，而在信任已经消耗。普通人并不是看不懂优惠，而是不再相信优惠背后的长期账本。首付降低不等于总债务消失，彩礼降温不等于婚育成本可承受，促消费不等于收入稳定，鼓励奋斗不等于分配公平。</p>
<p>当现实反复证明努力与回报不匹配，单纯的舆论动员就会失效。底层清醒之后，对花式规劝的反应往往很简单：不争辩，不解释，只是不买、不结、不生、不背债、不配合。</p>

<h2 id="redistribution">真正的解法不是新诱饵，而是重新分配安全感</h2>
<p>如果社会希望普通人重新形成稳定预期，就不能只制造更精美的诱饵。真正的解法是提高劳动收入、降低住房负担、约束畸形彩礼、提供可信的教育医疗养老保障，并让普通人相信自己的努力能换来可持续的生活改善。</p>
<p>消费不是靠口号刺激出来的，而是靠收入、信心和安全感自然生长出来的。婚育也不是靠道德绑架推动的，而是靠公平关系、可承受成本和稳定未来支撑的。住房更不能依赖无限接盘，而应该回到居住属性，让人不必用一生自由换取栖身之所。</p>
<p>底层拒绝入套，表面看是经济问题，实质是尊严问题。一个人不愿再做燃料，不代表他不愿生活；他只是拒绝把全部人生交给一套永远让自己亏损的规则。尊重这种选择，才是社会重新健康运转的起点。</p>

<h2 id="conclusion">结论：当牛马不再入套，就重新成为人</h2>
<p>高彩礼、高房价、高消费的退潮，标志着旧式收割机制正在遭遇边界。普通人不是突然变懒，而是在长期现实教育中学会了算总账。透支未来换体面，透支父母换婚姻，透支自由换房产，透支健康换工资，这些交易越来越难被视为理所当然。</p>
<p>当底层牛马不再入套，他们就不再只是消费链条、房贷链条、婚恋链条和职场链条上的工具，而重新成为一个个有感受、有边界、有选择权的人。旧秩序真正需要面对的，不是如何把人重新赶回笼子，而是如何让人有理由相信，继续参与社会协作会得到公平回报。</p>
<p>这场无声变局的意义正在于此：当普通人开始拒绝无止境献祭，社会就必须从依赖焦虑和债务的增长模式，转向更合理的分配、更平等的尊重和更切实的保障。否则，所有规劝都会变成空话，所有诱饵都会失去效果。</p>
"""


def configure() -> None:
    base.__file__ = __file__
    base.ROOT = ROOT
    base.DATE = "2026-07-22"
    base.BASE_DT = datetime(2026, 7, 22, 23, 59, tzinfo=timezone(timedelta(hours=8)))
    base.PREV_EXISTING_URL = "/2026/ai-connector-domestic-computing-ascend-supernode/"
    base.PREV_EXISTING_TITLE = "AI 连接器巨变：国产算力、昇腾超节点与高价值互联"
    base.SCRIPT_NAME = SCRIPT_NAME
    base.MANIFEST_NAME = MANIFEST_NAME
    base.CHANGED = set()

    post = base.Post(
        source_id="BV1BAVd6REcy",
        slug="low-desire-refusal-bride-price-housing-consumption",
        title="当底层牛马不再入套：拒绝高彩礼、高房价与高消费",
        desc="高彩礼、高房价和高消费曾共同塑造普通人的债务流水线；当越来越多劳动者选择低欲望、不接盘和不入套，消费、婚恋、地产与职场控制逻辑都会被迫重估。",
        category="社会观察",
        series="社会经济",
        tags=["高彩礼", "高房价", "高消费", "低欲望", "消费主义", "不婚不育", "房贷", "劳动者", "社会分配", "阶层焦虑", "社会观察"],
        minutes=13,
        body=BODY_ARTICLE,
        cover_kicker="不入套",
        cover_line="高彩礼 · 高房价 · 高消费退潮",
        cover_theme=("#111827", "#991b1b", "#f97316"),
        duration=807.4275,
        segments=295,
        chars=3909,
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
        "转述",
    ]
    failures: list[str] = []
    for post in base.INPUT_ORDER:
        path = ROOT / post.url_path.strip("/") / "index.html"
        text = path.read_text(encoding="utf-8")
        body = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', text, re.S)
        body_text = body.group(1) if body else text
        plain = re.sub(r"<[^>]+>", "", body_text)
        if len(plain) < 3200:
            failures.append(f"{post.slug}: body too short {len(plain)}")
        for word in forbidden:
            if word in text:
                failures.append(f"{post.slug}: forbidden word {word}")
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
