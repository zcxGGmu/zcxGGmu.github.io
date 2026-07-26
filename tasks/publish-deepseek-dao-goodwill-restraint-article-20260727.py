# -*- coding: utf-8 -*-
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
SCRIPT_NAME = "publish-deepseek-dao-goodwill-restraint-article-20260727.py"
MANIFEST_NAME = "publish-deepseek-dao-goodwill-restraint-article-20260727-changed-files.json"


spec = importlib.util.spec_from_file_location("base_publisher", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)


SLUG = "deepseek-dao-goodwill-restraint-open-source-agi"
TITLE = "DeepSeek 的道：善意、克制、开源与 AGI 主线"


BODY_ARTICLE = f"""
<p><img src="/images/posts/{SLUG}/cover.svg" alt="{TITLE}"></p>
<p>理解 DeepSeek，不能只看模型跑分、API 价格、融资金额、用户流量或者开源热度。真正决定这家公司气质的，是一套更底层的“道”：怀着对世界的善意做 AI，把愿景放在利益之前，把克制当成战略，把开源当成扩大人类智能底座的方式，把全部资源尽量压到 AGI 主线上。</p>
<p>这套逻辑与典型商业公司不同。典型商业公司会把增长、留存、变现、入口、估值和市场份额放在第一位；DeepSeek 的运行方式更像一个面向长期目标的研究型组织。它当然需要商业收入，也需要融资、算力、人才和服务能力，但这些不是终点，而是支撑长期研发的燃料。</p>
<p>所以，DeepSeek 的关键不只是“模型强”或“价格低”，而是为什么它能在没有巨大初始资源、没有巨量显卡、没有顶级声量的情况下，形成一种让行业震动的力量。答案并不在短期技巧里，而在愿景、组织、克制与开源这几件事之间的互相支撑。</p>

<h2 id="vision">愿景不是标语，而是实际运行方式</h2>
<p>愿景不是挂在墙上的口号，也不是融资材料里的漂亮句子。愿景真正起作用的时候，表现为一个组织每天怎样选择、怎样取舍、怎样分钱、怎样定价、怎样面对外界诱惑。</p>
<p>很多组织也会谈使命，但一旦遇到商业利益，就会迅速转向利润最大化、流量最大化和估值最大化。DeepSeek 特别之处在于，它把“对人类有用”“对世界怀有善意”放进了实际行为里。模型做出来，不是为了尽量贵地卖给少数客户，而是希望足够好、足够便宜、足够开放，让更多人能够真正使用。</p>
<p>这与“画大饼”完全不同。画大饼的底层驱动力是利益：未来给你更多钱、更多期权、更高职位、更大回报。利益当然重要，但只靠利益聚合起来的团队，最终也容易因为利益散掉。别人给得更多，人就会离开；内部利益分配不均，组织就开始猜忌；每个人都把个人收益最大化放在第一位，公司就会越来越像一台争夺机器。</p>
<p>真正的愿景驱动，是让人相信自己不是在替某个老板打工，而是在完成自己也认同的事情。这样的组织不需要时时刻刻用外部奖励驱赶成员，因为工作本身就带有意义。愿景不是口头承诺，而是让一群有共同方向的人愿意长期站在一起。</p>

<h2 id="yi-and-li">义与利：优秀组织靠意义凝聚</h2>
<p>“君子喻于义，小人喻于利。”这句话放在现代公司里，并不是说公司不要赚钱，而是区分两种组织方式：一种靠利益交换聚合，一种靠意义共识凝聚。</p>
<p>靠利益交换聚合的组织，管理核心往往是指标、考核、淘汰、奖惩和控制。它会非常在意如何防止员工钻空子，如何防止团队 reward hacking，如何让每个人朝着 KPI 走。但越是这样，越容易让组织陷入指标游戏：表面结果越来越好，真实目标却可能越来越远。</p>
<p>大模型训练里存在 reward hacking，人类组织里同样存在。只要奖励函数设计得不够好，人就会围绕指标套利，而不是围绕真实目标创造价值。把 benchmark 做高，不等于模型真正变强；把报表做漂亮，也不等于公司真正接近长期愿景。</p>
<p>愿景驱动的组织不是不要管理，而是管理重心不同。它更关心怎样吸引真正认同目标的人，怎样让他们保持自主性，怎样让他们把工作当成自己的事业。刘邦聚拢英才，曹操求贤若渴，本质都不是靠防人、控人、算人，而是靠一个更大的方向把人吸引进来。最高层次的组织管理，不是把所有人训练成服从指标的机器，而是让有能力的人愿意为共同愿景投入自己。</p>

<h2 id="restraint">克制不是保守，而是战略</h2>
<p>DeepSeek 的第二个关键词是克制。克制不是消极，也不是不懂商业，而是为了更大目标主动放弃一部分眼前利益。前面遍地都是芝麻，西瓜还在更远的地方。越能克制，越可能走到更远处。</p>
<p>AI 行业里诱惑非常多：流量诱惑、融资诱惑、应用诱惑、估值诱惑、短期收入诱惑、舆论声量诱惑。任何一个诱惑都足以让组织偏离主线。很多公司不是没有能力，而是在太多可赚钱的岔路上分散了自己。</p>
<p>克制的本质，是知道什么不做。真正稀缺的不是机会，而是注意力、算力、人才和组织耐心。如果一个团队每看到一个热点就冲进去，每看到一个短期收益就改方向，它就很难在最难、最长、最重要的主线上积累。</p>
<p>DeepSeek 的克制体现在几个方面：不追所有热门应用，不抢 C 端流量，不急着做超级 App，不把开源变成先免费后封闭的策略，不为了短期利润牺牲长期生态。它不是没有看到这些机会，而是清楚这些机会并不是终点。</p>

<h2 id="agi-mainline">坚守 AGI 主线：应用出口不是智能入口</h2>
<p>DeepSeek 的主线是通往 AGI 的模型能力本身，而不是每一个看起来很热的 AI 应用。3D 生成、视频生成、世界模型等方向当然有商业价值，也可能产生很大收入，但商业价值不等于它们一定处在 AGI 主线的入口处。</p>
<p>视频生成可以非常赚钱，也可以非常吸引眼球，但它本质上仍然主要是在学习像素序列和视觉模式。一个球在画面里弹跳，模型可以生成得很像，却未必真正理解重力、动量、碰撞、因果关系和物理约束。它掌握的可能是相关性，而不是对世界的可推理理解。</p>
<p>AGI 的核心路线首先需要模型学会推理。思维链、复杂问题拆解、代码能力、数学能力、工具调用、持续学习，这些能力更接近智能形成的底层结构。应用可以是出口，但不一定是入口。把所有精力投向最热的应用，很容易在商业上热闹，在智能主线上偏离。</p>
<p>这也是 DeepSeek 不追逐所有热点的原因。它要做的不是成为每个 AI 应用赛道里的产品公司，而是在模型能力本身上持续逼近智能上限。只要基础模型能力足够强，应用自然会长出来；如果基础能力没有突破，再多应用包装也只是短期流量。</p>

<h2 id="traffic">不抢流量：C 端用户不是终点</h2>
<p>当用户突然涌入时，互联网公司的本能通常是留存、促活、转化、会员、广告、生态闭环和超级 App。DeepSeek 没有把这条路当成主线。C 端用户很多当然是好事，但如果公司为了留住这些用户而不断消耗资源，主线就会被用户需求牵着走。</p>
<p>流量是一种枝叶。它能带来声量和收入，也能制造巨大负担。用户越多，客服、产品、运营、合规、内容、商业化和舆论管理的压力就越大。一个基础模型公司如果过早被 C 端流量绑住，很容易从研究型组织变成互联网运营公司。</p>
<p>DeepSeek 的克制，是不把短期流量当成胜利本身。外界可以拿流量曲线判断热度，但热度不是 AGI 进程的核心指标。真正重要的是模型能力是否提升、成本是否下降、开源生态是否扩大、研发主线是否更接近下一阶段。</p>
<p>不抢流量并不等于不服务用户，而是用户服务必须服从长期目标。能够让更多人用上模型当然重要，但不能为了做入口而牺牲模型主线。C 端是枝，AGI 是根。根稳住，枝叶才有意义。</p>

<h2 id="opensource">开源不是战术，而是战略</h2>
<p>开源常被误读为落后者的竞争策略：先免费、先低价、先打击对手，等超过之后再闭源收费。这种理解过于狭窄。对 DeepSeek 来说，开源不是临时战术，而是与愿景一致的战略。</p>
<p>如果 AI 未来会占据人类社会极大的生产力份额，那么任何想独占全部利益的组织，都会站到历史趋势的反面。越想拿得多，越容易被愿意拿得少、愿意让更多人受益的组织击败。哪怕大家还没有真正拿到钱，只要愿景是“我要拿最多”，就已经在更高层面输了。</p>
<p>开源意味着主动让出一部分利益，也意味着让更多企业、开发者、研究者和普通用户站在同一个智能底座上。它会让第三方部署模型、改造模型、使用模型，也会让生态更快扩散。短期看，这可能减少一部分商业独占收益；长期看，它会扩大模型的影响面和信任基础。</p>
<p>真正的开源还具有道德和组织意义。团队成员会看到自己的工作不是被锁在一家公司内部变现，而是在帮助更多人获得智能工具。这样的成就感，与单纯利润激励完全不同。开源不是“少赚钱”，而是把赚钱放在更大的社会价值之后。</p>

<h2 id="team">团队稳定来自共同愿景，而不只是高薪</h2>
<p>AI 行业的人才争夺异常激烈，高薪、期权、头衔和资源都可以成为挖人的工具。一个组织如果完全靠钱留人，就会陷入无休止竞价。别人给得更高，核心成员就可能流失；市场一热，团队就容易被拆散。</p>
<p>DeepSeek 的团队稳定，说明愿景在真实发挥作用。成员不是只因为短期收入留在这里，而是因为他们相信这件事值得做，相信 AGI 主线值得押注，相信开源和低成本模型能让更多人受益。</p>
<p>这并不意味着物质激励不重要。融资、收入和公司价值提升，可以减少成员面对外部诱惑和生活压力时的负担。真正理想的状态，是基本物质安全得到保障之后，人可以专心做自己认为有意义的事情。</p>
<p>有理想的人并非不需要钱，而是不愿意只为钱工作。组织必须让人既能解决现实生活问题，又能保持长期精神动力。只有这样，团队才不会在短期利益前分崩离析。</p>

<h2 id="compute">中国 AI 的瓶颈是算力，不是人才</h2>
<p>中美 AI 差距的核心，不是中国没有人才，而是算力资源仍然受限。算力少，能做的实验就少；实验少，模型迭代速度就慢；训练规模受限，很多大模型路线就无法全面展开。</p>
<p>这也是为什么 DeepSeek 需要集中力量突破，而不是到处撒网。美国头部实验室可以用庞大算力堆更大规模模型，国内公司必须在有限资源里做更高效率的选择。编码能力、推理能力、工程效率、模型压缩、推理成本优化，都是可以集中突破的方向。</p>
<p>算力问题是短期瓶颈，但不是永恒命运。只要产业链继续推进，国产算力、集群工程、模型效率和软件栈持续改善，约束会逐渐缓解。真正重要的是在资源受限阶段仍然保持主线，不因为暂时不能全面硬碰硬，就放弃技术突破。</p>
<p>DeepSeek 的意义也在这里：它证明了在算力并不占优的情况下，仍然可以通过路线选择、工程效率、成本控制和组织克制，做出世界级影响。这种经验本身，会反过来增强中国 AI 产业的信心。</p>

<h2 id="fear">为什么开源模型会引发恐惧</h2>
<p>中国开源模型真正让对手恐惧的，不只是某一个模型分数高，而是它改变了全球 AI 扩散方式。闭源模型把能力集中在少数公司手里，使用者必须通过 API 调用、接受价格、接受限制、接受数据边界。开源模型则让更多国家、公司和个人拥有本地部署、本地改造、本地审计的可能性。</p>
<p>这会削弱技术垄断。过去，强模型能力主要掌握在少数美国公司手中；开源模型越强，越多组织就越不必完全依赖闭源 API。尤其在安全、隐私、金融、医疗、工业和政府场景，本地部署具有天然吸引力。</p>
<p>所谓安全风险也不能简单归因于开源。闭源模型同样可能被攻破、被滥用、被绕过安全机制；开源模型也可以用于防御，例如在本地分析日志、定位漏洞、帮助修复系统，而不把账号、密码、密钥和敏感数据交给外部平台。真正的问题不是开源与闭源的简单二分，而是谁掌握能力、谁定义规则、谁拥有审计权。</p>
<p>从这个角度看，对中国开源模型的封禁冲动，本质上是一种对能力扩散的恐惧。开源让更多人获得智能工具，也让全球技术秩序不再完全受少数闭源巨头控制。得道者多助，失道者寡助。越多企业和开发者依赖开源能力，越说明这种路线有现实生命力。</p>

<h2 id="future-work">AI 不会简单取代人，而会放大人类资本</h2>
<p>AI 会重塑就业市场，但不必然造成简单意义上的大规模失业。它更像人类资本的放大器：让一个人的知识、判断、创造力、管理能力和执行能力被放大，让更多普通人拥有过去只有大公司才能使用的能力。</p>
<p>如果 AI 能够普惠大众，人类社会整体劳动生产率会大幅提高。生产率提高之后，社会会变得更富有，人们也会重新思考就业的意义。工作不一定只是为了生存，也可能更多转向创造、服务、探索、连接和自我实现。</p>
<p>这也是开源和低价的重要性。如果 AI 只属于少数资本和少数平台，它会扩大不平等；如果 AI 被更多人使用，它就可能成为普通人的能力杠杆。DeepSeek 的善意，并不是抽象情绪，而是让智能能力尽量不被少数人垄断。</p>
<p>未来竞争的关键，不是谁把 AI 锁得更紧，而是谁能让更多人用得起、用得好、用得安全，并在此基础上继续推进模型能力。让 AI 普惠，不是反商业，而是更大的商业与社会价值。</p>

<h2 id="conclusion">结论：善意、克制和开源，构成 DeepSeek 的长期竞争力</h2>
<p>DeepSeek 的“道”，可以概括为四句话：用善意定义方向，用愿景凝聚团队，用克制守住主线，用开源扩大智能的社会基础。</p>
<p>善意让公司不把 AI 只当成利润机器；愿景让组织不只是靠利益分配维系；克制让资源不被短期诱惑带偏；开源让模型能力进入更大的生态。四者合在一起，才解释了为什么 DeepSeek 不是普通意义上的 AI 创业公司，而更像一个有长期文明视角的技术组织。</p>
<p>这种路线并不轻松。它需要持续面对算力不足、外部封锁、商业诱惑、人才争夺、舆论误解和技术不确定性。但也正因为难，才更能体现战略选择的价值。短期利益会不断出现，长期主线却只有一条。</p>
<p>真正值得关注的，不是 DeepSeek 某一次流量高低，也不是某一个榜单位置，而是它是否继续沿着 AGI 主线推进，是否继续保持开源和低成本的生态路线，是否继续用克制换取更大的长期可能。只要这条道不变，DeepSeek 的意义就不只是做出一个强模型，而是推动智能能力更广泛地进入世界。</p>
"""


def configure() -> None:
    base.__file__ = __file__
    base.ROOT = ROOT
    base.DATE = "2026-07-27"
    base.BASE_DT = datetime(2026, 7, 27, 1, 25, tzinfo=timezone(timedelta(hours=8)))
    base.PREV_EXISTING_URL = "/2026/slow-rich-value-patience-time-control/"
    base.PREV_EXISTING_TITLE = "慢慢变富：戒掉一夜暴富幻想，靠价值、等待和时间重建掌控权"
    base.SCRIPT_NAME = SCRIPT_NAME
    base.MANIFEST_NAME = MANIFEST_NAME
    base.CHANGED = set()

    post = base.Post(
        source_id="BV1z53L6ME1d",
        slug=SLUG,
        title=TITLE,
        desc="DeepSeek 的长期竞争力不是单一模型参数，而是由善意、愿景、克制、开源和 AGI 主线共同构成的组织哲学与战略选择。",
        category="AI工具",
        series="AI产业",
        tags=["DeepSeek", "梁文锋", "AGI", "开源", "大模型", "算力", "组织管理", "长期主义", "人工智能", "AI伦理"],
        minutes=15,
        body=BODY_ARTICLE,
        cover_kicker="DeepSeek 的道",
        cover_line="善意 · 克制 · 开源 · AGI 主线",
        cover_theme=("#0f172a", "#065f46", "#38bdf8"),
        duration=1001.7785,
        segments=524,
        chars=4966,
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
        "B站", "bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主",
        "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅", "投币", "收藏", "下期", "评论区",
        "BV1z53L6ME1d", "source_id",
    ]
    required = [
        "DeepSeek", "善意", "愿景", "克制", "开源", "AGI", "算力", "主线", "长期主义", "人工智能", "义与利",
    ]
    failures: list[str] = []
    if len(plain) < 5200:
        failures.append(f"{post.slug}: body too short {len(plain)}")
    for word in forbidden:
        if word in article:
            failures.append(f"{post.slug}: forbidden wording {word}")
    for word in required:
        if word not in article:
            failures.append(f"{post.slug}: missing required term {word}")
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
