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
SCRIPT_NAME = "publish-compound-interest-inflection-point-article-20260726.py"
MANIFEST_NAME = "publish-compound-interest-inflection-point-article-20260726-changed-files.json"


spec = importlib.util.spec_from_file_location("base_publisher", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load base publisher: {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)


SLUG = "compound-interest-cruel-truth-life-inflection-point"
TITLE = "复利最残酷的真相：熬过前半段，才等得到人生拐点"


BODY_ARTICLE = f"""
<p><img src="/images/posts/{SLUG}/cover.svg" alt="{TITLE}"></p>
<p>复利最残酷的地方，不在于公式难懂，而在于它把最好的回报几乎全部放在后半段。财富、知识、影响力、人际关系、声誉和健康，都不是靠短期爆发完成跃迁，而是靠长期持续的正向积累，在时间里被不断放大。</p>
<p>问题在于，指数曲线的前半段往往非常平。人已经投入了很多时间，结果却像一条贴着地面走的横线：资产没明显增长，作品没人注意，能力没有外界认可，关系和信用也看不到可量化回报。大多数人不是输在不聪明，而是熬不过这段看起来没有进展的时期。</p>
<p>真正决定一个人能不能等到拐点的，不是短期收益率有多高，而是能否在一个合理的正期望系统里长期存在：不频繁重启，不被情绪带走，不把自己清零，不用即时满足交换未来几十年的复利结果。</p>

<h2 id="compound-is-not-finance-only">复利不是理财技巧，而是人生回报的底层结构</h2>
<p>很多人把复利理解成理财里的利滚利：本金产生收益，收益继续变成本金，于是长期滚动。但金钱只是复利最粗糙、最容易被看见的版本。更底层的复利，发生在认知、技能、信任、声誉和协作关系里。</p>
<p>认知会复利。一个人长期阅读、思考、写作、复盘，前几年可能看不出区别，但每一次理解都会成为下一次理解的基础。到后来，他不是多知道几条信息，而是拥有更强的判断框架，能更快识别机会、风险和底层规律。</p>
<p>技能会复利。真正复杂的能力，往往不是靠一次训练获得，而是在重复实践中不断压缩错误、提高效率、形成直觉。十年后，高手和普通人的差距不是“多练了一点”，而是每一次练习都叠加在此前积累之上，最终形成指数级差距。</p>
<p>关系和声誉也会复利。稳定合作、持续兑现承诺、一次次证明可靠，会让别人更愿意把机会、信息和资源交给你。信用不是一次性资产，而是长期重复行为的结果。只要一次严重失信，很多年积累的信任都可能被摧毁。</p>

<h2 id="front-half">指数曲线的前半段，最考验人性</h2>
<p>复利曲线的前半段之所以残酷，是因为它几乎不给反馈。人类的大脑喜欢即时回报：做了事，就希望马上看见结果；投入时间，就希望立刻获得确认；承受痛苦，就希望痛苦能马上变成收益。</p>
<p>但指数增长不是这样运作的。它在前期看起来非常慢，慢到像没有增长。一个人写了几十篇文章，可能没人读；学习一门复杂技能，可能一年后仍然笨拙；经营一个长期事业，可能连续很久都没有外界认可。此时最容易产生怀疑：是不是方向错了，是不是自己不适合，是不是换一条路更快。</p>
<p>真正的问题在于，很多人放弃的位置，恰好离拐点已经不远。他们在一个方向上投入一段时间，看不到结果，于是重新开始；新方向同样有漫长前半段，于是再换一次。反复切换之后，人生一直停留在复利曲线的底部，永远没有进入陡峭上升区。</p>
<p>复利不会提前提醒你“快到了”。它不会在拐点前给出明确的信号，也不会因为你快撑不住了就提前支付奖励。它只是安静地等待：谁能长期留在同一个正向系统里，谁就有机会拿走后半段的回报。</p>

<h2 id="frequent-switching">频繁换赛道，是对复利最大的浪费</h2>
<p>长期投入并不等于固执，而是要在值得做的事情上持续叠加。纳瓦尔式的长期游戏观，核心是和长期的人，在长期的系统里，做长期的事。只有这样，时间才会真正帮你放大收益。</p>
<p>事业上频繁追热点，很容易让人永远停留在新手阶段。今天看某个行业火，就从头开始；明天看到另一个机会更热，又重新开始。每一次切换都像把此前积累的土壤翻掉重新播种，短期看似灵活，长期却很难形成独特能力。</p>
<p>人际关系上也是如此。真正有价值的信任，不是靠一次认识建立，而是靠多年合作、反复兑现、共同经历风险和收益沉淀出来的。如果关系总是被随意消耗、被短期利益切断，就很难形成长期互相托举的网络。</p>
<p>声誉更不能频繁重启。一个人说到做到，长期稳定，别人会越来越愿意相信他；一个人总是承诺很多、兑现很少，信用就会逐渐被透支。声誉的增长很慢，毁掉却很快。</p>

<h2 id="long-term-games">长期游戏的门槛，是愿意在同一件事上叠加很多年</h2>
<p>复利真正昂贵的成本，是时间和耐心。不是所有事情都值得坚持，但一旦选择了正期望方向，就必须给它足够长的生长周期。</p>
<p>一个好的长期系统，至少具备三个特征。第一，它是正向积累的：今天做的事不会在明天完全归零，而是会留下知识、资产、关系、作品、流程或声誉。第二，它可以自我增强：越做越熟，越熟越快，越快越有机会获得更好的资源和反馈。第三，它允许长期存在：不依赖一次赌博式结果，也不会因为短期波动把人直接淘汰。</p>
<p>符合这些条件的事情，往往一开始都不性感。读书、写作、训练、深耕行业、维护关系、保持健康、积累本金、打磨产品、建立信用，都很慢，也不容易在短期赢得掌声。但正是这些事情，最可能在长期里产生无法追赶的差距。</p>
<p>短期爆发当然令人兴奋，但爆发很少能替代积累。真正可靠的跃迁，通常不是突然发生的奇迹，而是大量看不见的前期投入，在某个时刻被外界集中看见。</p>

<h2 id="do-not-get-zeroed">复利的第一前提：不要把自己清零</h2>
<p>复利只有在你还留在局里时才会发生。真正危险的，不是增长速度慢，而是因为短视决策把自己直接淘汰出局。财富、信用、健康和关系，只要被一次重大错误清零，后面的复利就失去了载体。</p>
<p>财富上，过度杠杆和赌博式重仓最容易清零。一个人花很多年积累本金，却为了快速翻倍把所有筹码压在单一机会中，一次判断错误就可能把前面的努力全部抹掉。高收益率并不一定比长期存活更重要，因为本金毁灭后，任何收益率都无法继续复利。</p>
<p>声誉上，一次严重失信也可能清零。信用的积累是漫长的，毁灭却常常发生在一件事里。欺骗、背叛、承诺不兑现，都会让过去多年建立的信任瞬间失效。一个没有信用的人，即使短期占到便宜，也会失去长期合作网络。</p>
<p>健康上，长期熬夜、透支身体、用未来换眼前的小成绩，也是一种清零。身体是所有长期游戏的底层账户。健康崩掉之后，事业、财富和关系都很难继续承载复利。</p>
<p>因此，复利的门槛不是找到多高的年化收益，而是在合理的正期望系统里持续存在几十年。先不被淘汰，再谈增长速度。</p>

<h2 id="emotion-risk">情绪会打断复利的齿轮</h2>
<p>复利看似是时间和系统的问题，本质上也考验情绪管理。焦虑、嫉妒、愤怒，都会把人从长期轨道上推开。</p>
<p>焦虑会让人追逐短期暴利。看到别人快速赚钱，自己就开始怀疑慢方法是不是错了，于是加杠杆、追热点、做看不懂的事。焦虑最危险的地方，是它会把“想快一点”伪装成“抓住机会”。</p>
<p>嫉妒会让人频繁换方向。别人做某件事赚钱了，就觉得自己也该做；别人换赛道成功了，就认为自己当前的积累没有价值。嫉妒让人把别人的阶段性结果，当成自己的行动指令。</p>
<p>愤怒会破坏关系和声誉。长期合作需要稳定、克制和可信。人在愤怒中说出伤人的话、做出失控的决定，可能会毁掉多年积累的信任。情绪不是小事，它会直接切断复利链条。</p>
<p>能够长期复利的人，并不是没有情绪，而是不会让情绪决定方向、仓位、承诺和关系。他们把短期波动当作系统内的一部分，而不是把每一次波动都当作必须立刻反应的信号。</p>

<h2 id="time-horizon">人总是高估一两年，低估十年二十年</h2>
<p>大多数人会高估自己一两年能做到的事，却低估自己十年、二十年能做到的事。这个错配，是许多失败和焦虑的来源。</p>
<p>一两年的时间，足够人开始一件事，却不一定足够看到巨大结果。复杂能力、长期事业、深度关系、可靠声誉，都很难在短时间内开花结果。如果把一两年的回报设得过高，就很容易失望、怀疑、放弃。</p>
<p>但十年、二十年的时间足以改变一切。一个方向正确、每天进步一点、不断减少错误的人，长期会和原地打转的人拉开巨大差距。这个差距不是线性的，而是积累到一定程度后突然显现出来。</p>
<p>熬不到复利拐点的人，并不一定输给了别人，很多时候是输给了自己的即时满足。他们用短期情绪安慰，交换掉本来可以在二十年后彻底不同的人生轨迹。</p>

<h2 id="choose-system">选择正期望系统，而不是盲目坚持</h2>
<p>强调长期，不等于什么都要坚持。错误方向上的坚持，只会放大错误。复利需要一个前提：你所处的系统本身具备正期望。</p>
<p>正期望系统通常有几个信号。第一，投入会留下沉淀，而不是每次归零。第二，能力会随着时间提高，而不是永远重复低价值劳动。第三，信誉和关系会不断积累，而不是靠一次性交易透支。第四，风险可控，不会因为单次失败让人出局。</p>
<p>反过来，如果一件事长期没有任何沉淀，只消耗时间和精力；如果每一次努力都不能提高下一次效率；如果需要不断欺骗、透支关系或冒巨大风险才能维持收益，那么它就不是适合复利的系统。</p>
<p>长期主义最难的部分，不是“坚持”两个字，而是先判断什么值得坚持。选错系统，耐心会变成消耗；选对系统，耐心才会变成优势。</p>

<h2 id="practical-rules">普通人的复利实践规则</h2>
<p>第一，减少频繁重启。每年都换方向，看似在追机会，实际上是在不断回到指数曲线的起点。真正重要的能力，要给它三年、五年、十年的时间。除非确定方向不再正期望，否则不要因为短期没有掌声就轻易放弃。</p>
<p>第二，把积累对象具体化。不要抽象地说“我要成长”，而要明确积累什么：本金、作品、专业能力、行业认知、客户信任、健康指标、长期关系、可复用方法。只有积累对象具体，才知道每天该做什么。</p>
<p>第三，为自己设定不清零规则。财富上不重仓赌博、不滥用杠杆；声誉上不承诺做不到的事；健康上不长期透支；关系上不因短期利益背叛长期信任。这些规则看似保守，却是复利能继续发生的保险丝。</p>
<p>第四，用输入指标替代短期结果。前半段没有外部回报时，只盯结果会让人崩溃。更可靠的做法，是盯输入：读了多少、写了多少、训练了多少、复盘了多少、交付了多少、关系维护了多少。只要输入在正期望系统里持续，结果会在后半段集中显现。</p>
<p>第五，远离让人不断比较的环境。比较会放大焦虑，焦虑会诱发换方向、加杠杆、追热点和自我否定。长期游戏需要稳定心态，稳定心态需要控制信息摄入和社交参照。</p>

<h2 id="flat-stage">平坦期不是无效期，而是蓄力期</h2>
<p>复利前半段最容易被误判为无效。因为结果不明显，人会以为投入没有意义。但很多真正重要的变化，恰恰发生在看不见的地方。</p>
<p>学习初期，知识点看似零散；写作初期，表达看似笨拙；投资初期，本金增长很慢；关系初期，信任尚未稳固。外界看不到成果，自己也容易看不到进步。但这些阶段其实是在建立底层结构。</p>
<p>等到结构逐渐稳定，速度才会改变。认知框架形成后，学习新东西会更快；能力组合成熟后，机会会主动靠近；信用积累到一定程度后，合作成本会下降；本金足够厚后，同样的收益率会带来更大的绝对金额。</p>
<p>前半段不是没有回报，而是回报还没有以显性方式出现。它先变成能力、判断、信任和结构，最后才变成看得见的财富、影响力和人生选择权。</p>

<h2 id="persist-or-quit">什么时候坚持，什么时候退出</h2>
<p>长期主义最容易被误用的地方，是把所有痛苦都解释成“前半段”。事实上，有些痛苦来自增长前的沉淀，有些痛苦只是错误系统在消耗人。区分两者，非常重要。</p>
<p>值得坚持的平坦期，通常有内部进步。外部结果可能不明显，但自己能感到判断更准、动作更熟、错误更少、作品更稳、合作更顺，或者别人对自己的信任正在缓慢增加。这说明投入正在沉淀，只是还没进入显性回报阶段。</p>
<p>应该警惕的消耗期，则没有任何复用价值。每天都很忙，但能力没有提升；每次都从零开始，经验不能迁移；关系只被透支，信用没有增加；风险越来越大，却没有更稳的系统。这样的状态不是复利前夜，而是负复利。</p>
<p>因此，最成熟的做法不是盲目坚持，也不是轻易放弃，而是定期做系统体检：方向是否仍然正期望，投入是否产生沉淀，风险是否可承受，自己是否还能长期存在。只要这四个答案仍然成立，短期平淡就不必急着否定；如果答案已经崩塌，就要尽快止损，重新选择可积累的系统。</p>

<h2 id="conclusion">结论：时间只奖励能长期留在正向系统里的人</h2>
<p>复利不会奖励所有坚持者，它只奖励那些在正向系统里长期存在的人。方向要对，系统要能积累，风险要可控，情绪要稳定，健康和信用不能被清零。</p>
<p>真正的成功，关键在于能否在看不到结果的时候继续投入。最难的不是理解复利，而是在曲线还平的时候相信长期结构，在别人追逐短期反馈时守住自己的节奏，在焦虑和嫉妒出现时不轻易重启人生。</p>
<p>时间不是天然的朋友。只有当一个人做着能自我增强的事，并且长期不被淘汰，时间才会成为最强大的盟友。熬过前半段，拐点才有可能出现；熬不过前半段，就永远只能站在复利曲线的起点重新开始。</p>
<p><em>本文为个人成长与长期主义方法研究，不构成任何投资、职业或人生决策建议。每个人的资源、阶段和风险承受能力不同，长期选择仍需结合自身情况独立判断。</em></p>
"""


def configure() -> None:
    base.__file__ = __file__
    base.ROOT = ROOT
    base.DATE = "2026-07-26"
    base.BASE_DT = datetime(2026, 7, 26, 23, 59, tzinfo=timezone(timedelta(hours=8)))
    base.PREV_EXISTING_URL = "/2026/innovative-drugs-high-prosperity-new-pillar-biopharma-investment/"
    base.PREV_EXISTING_TITLE = "创新药持续高景气：新兴支柱产业定位下的医药投资主线"
    base.SCRIPT_NAME = SCRIPT_NAME
    base.MANIFEST_NAME = MANIFEST_NAME
    base.CHANGED = set()

    post = base.Post(
        source_id="BV1V93u67ED1",
        slug=SLUG,
        title=TITLE,
        desc="复利最残酷的地方，是前半段几乎没有反馈。真正能等到人生拐点的人，不是短期爆发更强，而是能在正期望系统里长期存在、不频繁重启、不被情绪带走、不把自己清零。",
        category="个人成长",
        series="长期主义",
        tags=["复利", "长期主义", "纳瓦尔", "人生策略", "时间", "耐心", "不被清零", "情绪管理", "认知积累", "声誉"],
        minutes=8,
        body=BODY_ARTICLE,
        cover_kicker="复利",
        cover_line="前半段平坦 · 后半段陡峭",
        cover_theme=("#111827", "#92400e", "#facc15"),
        duration=495.8389375,
        segments=194,
        chars=2645,
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
        "节目",
        "收听",
    ]
    required = ["复利", "指数曲线", "前半段", "长期游戏", "不被清零", "情绪", "正期望", "时间", "拐点"]
    failures: list[str] = []
    if len(plain) < 4600:
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
