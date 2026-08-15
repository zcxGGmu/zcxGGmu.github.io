from __future__ import annotations

import base64
import importlib.util
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote


sys.dont_write_bytecode = True

TASKS = Path(__file__).resolve().parent
BASE_SCRIPT = TASKS / "publish-three-life-business-articles-20260809.py"

spec = importlib.util.spec_from_file_location("publish_base", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = base
spec.loader.exec_module(base)

_base_run_gh = base.run_gh


def run_gh_with_retry(args: list[str], payload: dict | None = None):
    for attempt in range(5):
        try:
            return _base_run_gh(args, payload)
        except RuntimeError as exc:
            msg = str(exc).lower()
            if attempt < 4 and any(token in msg for token in ["stream error", "connection", "reset", "timeout", "temporarily"]):
                time.sleep(2 + attempt * 3)
                continue
            raise


base.run_gh = run_gh_with_retry
base.__file__ = __file__
base.DATE = "2026-08-15"
base.BASE_DT = datetime(2026, 8, 15, 23, 40, 0, tzinfo=timezone(timedelta(hours=8)))
base.PREV_EXISTING_URL = "/2026/lithium-battery-storage-second-wave-catl-valuation-cycle/"
base.PREV_EXISTING_TITLE = "锂电第二波主升浪：储能接棒，宁德时代 15 倍估值仍有安全边际"
base.SCRIPT_NAME = Path(__file__).name
base.MANIFEST_NAME = "publish-hongshu-career-selfmedia-eight-articles-20260815-changed-files.json"
base.PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
    "/2026/original-accumulation-time-autonomy-ordinary-people/",
    "/2026/next-decade-wealth-leap-deflation-rmb-ai-cashflow/",
]

PAGE1_SIZE = 24
PAGE_SIZE = 10
_active_ref = None


def get_file_at_active_ref(path: str) -> str | None:
    if _active_ref is None:
        raise RuntimeError("active remote ref is not set")
    try:
        data = base.run_gh([base.endpoint(f"contents/{quote(path, safe='/')}?ref={_active_ref.commit_sha}")])
    except RuntimeError as exc:
        if "Not Found" in str(exc):
            return None
        raise
    return base64.b64decode(data["content"]).decode("utf-8")


BODY_FIRST_POT = r'''
<p>普通人的第一桶金越来越难，不是因为机会完全消失了，而是因为起点低的人，再想靠正常努力慢慢换回超额结果，已经越来越不现实。正常上班、正常休息、正常社交、正常试错，最后换来的也大概率只是正常收入。</p>
<p>第一桶金的残酷之处在于：当本金、资源、经验、圈层都很薄的时候，常规努力并不够。真正能把收入上限打开的，往往不是“再努力一点”，而是愿意在一个阶段里透支时间、社交、家庭陪伴、体力和心理安全感。</p>

<h2 id="overdraft-not-effort">一、透支不是努力，而是不给自己留太多退路</h2>
<p>努力和透支不是一回事。努力通常还保留着退路：项目能不能成不知道，但态度上尽力；结果好不好不知道，但至少自己没有太难看。透支则完全不同，它更接近 all in，把有限的时间、精力和资源集中压到一件事情上。</p>
<p>刚开始创业时，每周工作不少于 80 个小时，半年几乎没有社交，生活动线压缩到学校、工作、房间、书桌之间反复循环。白天做事，晚上继续做事，拍内容、直播、交付、咨询都挤在同一个空间里完成。这种状态并不浪漫，它就是一种真实透支。</p>
<p>但对普通人来说，起点低的时候，如果还想事事稳妥、处处留余地，目标本身就和手段矛盾。钱没了可以再赚，账号没了可以重开，方向错了可以换；真正不能浪费的是年轻阶段还能高强度试错的时间窗口。</p>

<h2 id="risk-of-being-too-safe">二、输不起的人，很难拿到高回报</h2>
<p>很多人做事反复权衡，本质上不是谨慎，而是输不起。因为输不起，所以不敢投入；因为不敢投入，所以没有结果；没有结果以后，又进一步证明自己不能冒险。</p>
<p>第一桶金往往不来自完美方案，而来自敢把所有资源压进一个方向。成长不是坐在安全区里等待成熟，而是在真刀真枪的反馈里，被市场、客户、项目和失败一次次打磨。</p>
<p>普通人没有垄断技术，也没有垄断资源，如果还追求高确定性和高回报同时存在，那几乎只剩幻想。高确定性和高回报，对普通人天然矛盾。想要更高回报，就必须接受更低确定性。</p>

<h2 id="help-stronger-people">三、成全别人，本质上是在成全自己</h2>
<p>普通人完全靠自己拿到第一桶金，难度很高。更现实的路径，是找到一个比自己更强、资源更多、位置更高的人，在关键阶段成全他，等他飞升之后顺手拉自己一把。</p>
<p>在公司里，真正的好项目并不平均分配。每个季度、每半年都有很多项目，但领导其实很清楚：哪些项目绑定集团核心战略，哪些项目只是探索，哪些项目大概率只是凑数。资源分配前，信息差天然存在。</p>
<p>最好的项目不一定给能力最强的人。能力强但总想证明自己比领导更聪明的人，容易被安排去做不确定性更高的探索项目。真正容易拿到核心项目的人，是懂得成全领导的人：脏活苦活自己干，事情做成后 90% 功劳给领导，5% 留给自己，5% 分给协作伙伴和团队其他人。</p>
<p>这不是卑微，而是理解组织运行。核心项目绑定的人很多，领导、上级、协作部门都希望它成功，资源、指导和协作都会向它倾斜。当身边所有人都希望你成功时，成功会容易很多；当位置无人看见，甚至周围人并不希望你出头时，做什么都会有阻力。</p>

<h2 id="choose-the-right-leader">四、选对人，比单纯证明自己更重要</h2>
<p>成全别人不是随便抱大腿，而是识别谁有上升趋势、谁握有关键资源、谁愿意在自己上升之后反哺团队。选错人，再努力也可能只是在帮别人消耗自己；选对人，很多资源会顺着项目和信任自然流过来。</p>
<p>所以职场里的聪明，不只是把事情做漂亮，还包括识别项目背后的资源结构。真正值得投入的项目，往往和核心战略绑定，能拿到跨部门协作，能被上级持续追踪，也能让参与者共享一部分上升收益。</p>

<h2 id="escape-certainty">五、摆脱确定性，才有机会打开收入上限</h2>
<p>打工人的困境，是很容易把努力和确定回报绑定在一起。加班到 11 点、12 点，一整层楼只剩自己的工位亮着，当然很努力。但只要收入来自确定工资，收入天花板也基本被确定了。</p>
<p>项目帮公司赚钱，超额收益大部分属于公司；项目给公司亏钱，亏损也不用员工承担。确定工资的好处是稳定，代价是无法享受完整上行空间。</p>
<p>创业或副业的区别在于，没有人兜底，失败自己承担，但一旦做成，上行收益也属于自己。第一个产品失败、转化率只有 3% 到 4%，就换方向继续试。过去一年尝试七八种方向，大多数失败，但只要有一次成功，带来的红利就可能够吃半年甚至一年。</p>

<h2 id="before-thirty">六、三十岁之前最大的资产，是能失败很多次</h2>
<p>三十岁之前最珍贵的，不是已经有多少资源，而是还有时间失败很多次。失败三次、五次并不可怕，只要一次成功的收益足够覆盖前面的试错成本，路径就能继续往前走。</p>
<p>如果一直摆脱不了对确定性的执着，就永远不敢真正开始。机会不会在纸上变得安全，能力也不会在旁观中自然形成。只有进入真实市场，接受反馈、失败、调整和再出发，第一桶金才可能出现。</p>

<h2 id="choose-one-thing">七、普通人最怕的，是同时给自己留十条路</h2>
<p>很多人说自己想赚钱，但每天都在换方向。今天觉得 AI 有机会，明天觉得自媒体有机会，后天又想做电商、考证、投资、跳槽。表面看是选择多，本质上是没有真正承担任何一个选择的成本。</p>
<p>资源少的时候，最需要集中。不要同时做十件事，而是挑一个自己愿意连续投入三个月、六个月甚至一年的方向。只有投入足够深，才会遇到真实问题；只有遇到真实问题，能力才会增长。</p>
<p>第一桶金不需要一开始就选到终局答案，但需要选到一个能持续试错的方向。方向错了可以调整，最糟糕的是一直站在路口，永远没有走进任何一条路。</p>

<h2 id="execution-list">八、可执行的三步：押注、借势、试错</h2>
<p>第一步，押注一件事。把时间表、现金流和精力重新分配，让自己每天都在向同一个目标推进。第二步，借势一个人或一个平台。找到更强的人、核心项目或上升行业，让自己的努力站在更大的势能上。</p>
<p>第三步，持续试错。不要把失败理解成否定，而要把失败当成市场反馈。一次产品失败，就换表达；一次方向不行，就换切口；一次成交困难，就重新打磨价值主张。</p>
<p>普通人真正能做的，不是保证每一步都赢，而是保证自己一直在高密度反馈里进化。第一桶金往往就是这种连续进化后的副产品。</p>

<h2 id="final-view">九、结论：第一桶金不是等来的，是用资源换来的</h2>
<p>第一桶金越来越难，是因为普通人的常规努力正在变得越来越便宜。想要跨过这个阶段，就要明白三件事：第一，必要时透支自己，把资源集中到一件事上；第二，成全更强的人，借助别人的上升势能；第三，摆脱对确定性的依赖，允许自己反复失败。</p>
<p>这条路不轻松，也不适合所有人。但如果目标真的是拿到第一桶金，就不能只用安全、体面、稳定的方式去要一个不安全、不稳定、超额的结果。</p>
'''


BODY_CAREER = r'''
<p>找工作的第一反应，不能只停留在“钱多、事少、离家近”。这套标准没有错，但如果脑子里只有这套标准，很容易错过未来十年最好的机会。</p>
<p>一份真正值得投入的工作，至少要回答三个问题：能不能学到东西，能不能交到朋友，能不能赚到钱。三点都满足，是理想工作；满足两点，也值得考虑；如果只能满足一点，甚至一点都没有，那就要谨慎。</p>

<h2 id="what-is-good-job">一、好工作有三个标准：学习、连接、收入</h2>
<p>能学到东西，意味着这份工作会让能力持续增值，而不是只消耗已有技能。能交到朋友，意味着这份工作会把人带入更好的协作网络和信息环境。能赚到钱，意味着当下收入、未来上升空间或商业转化可能性足够明确。</p>
<p>如果一份工作只能给钱，但能力没有积累，人脉没有升级，它更像一次短期现金流交换。如果一份工作很有情怀，但学不到东西、赚不到钱、也没有连接价值，那只是用时间补贴别人。</p>
<p>真正好的工作，是能让今天的时间变成明天的筹码。工资只是其中一部分，更重要的是它把人放到了什么行业、什么趋势、什么项目和什么人群里。</p>

<h2 id="trend-matters">二、个人努力必须踩在趋势上</h2>
<p>一个长期发展的问题，不能只用个人努力解释。努力当然重要，但努力如果踩在退潮行业里，结果很容易被行业天花板压住；努力如果踩在上升趋势里，同样的投入会被放大。</p>
<p>所谓“势”，就是趋势的势。新质生产力、智能制造、智慧医疗、低空经济、数字化供应链、AI 应用落地，这些方向背后不是概念，而是产业、资本、政策和人才需求共同推动的岗位变化。</p>
<p>找工作不是盲目追热词，而是判断某个行业是否正在获得更多资源：有没有资本投入，有没有政策支撑，有没有真实招聘需求，有没有长期岗位扩张。如果答案是肯定的，个人努力才更容易结出果实。</p>

<h2 id="wrong-standard">三、只盯轻松，容易错过上升入口</h2>
<p>很多人想找轻松工作，这很正常。但刚进入职场或准备换赛道时，如果第一优先级就是轻松，很可能把自己排除在核心机会之外。</p>
<p>真正能带来长期回报的岗位，早期通常不会太舒服。它可能节奏快、要求高、变化多，但也会让人更快接触项目、客户、工具、行业逻辑和关键人。如果只筛选“事少”，往往也把成长空间一起筛掉了。</p>
<p>轻松不是不能要，而是要分阶段。能力没有复利之前，过早追求轻松，容易换来长期平庸；能力已经形成之后，再用选择权换取更舒服的工作状态，才更划算。</p>

<h2 id="matching-role">四、找工作是匹配，不是海投</h2>
<p>找工作最重要的不是投得越多越好，而是匹配效率。岗位、行业、能力、城市、薪资、发展路径如果完全不匹配，投再多简历也只是消耗情绪。</p>
<p>真正有效的找工作，要先确定方向：想进入什么行业，愿意做什么职能，能接受什么强度，未来三年想积累什么能力。方向越清楚，简历、面试表达和岗位筛选越容易形成合力。</p>
<p>很多人的问题不是没有机会，而是没有把自己的经历翻译成岗位需要的语言。企业关心的是你能解决什么问题，而不是你自己觉得多努力。</p>

<h2 id="use-tools">五、工具能提升效率，但不能替代判断</h2>
<p>招聘平台、行业信息、岗位推荐、面试辅导都能提高效率。专业平台可以帮助减少信息差，把更多岗位推到面前，也能让人更快看到行业变化。</p>
<p>但工具只能放大判断，不能替代判断。如果不知道自己要什么，也不知道行业趋势在哪里，再多岗位推荐也只是噪音。先有方向，再借助工具，效率才会真正提升。</p>
<p>找工作不是把自己丢进市场里碰运气，而是主动选择战场。趋势、岗位、公司、领导、团队、项目，这些因素共同决定一份工作的真实质量。</p>

<h2 id="screening-method">六、筛岗位时，先看行业，再看公司，再看岗位</h2>
<p>很多人找工作先看薪资，薪资差不多再看通勤，最后才看行业。更有效的顺序应该反过来：先看行业是否在上升，再看公司是否在行业里有位置，最后看岗位是否能接触核心业务。</p>
<p>同样是运营、销售、产品、研发，处在上升行业和下行行业，三年后的履历价值完全不同。同样是大公司，核心部门和边缘部门，能接触到的资源也完全不同。</p>
<p>面试时也要围绕这三个问题反问：这个岗位服务公司哪条增长线？这个团队过去一年扩张还是收缩？这个岗位能接触客户、数据、产品还是核心项目？答案越具体，岗位质量越容易判断。</p>

<h2 id="avoid-comfort-trap">七、不要把舒服误认为稳定</h2>
<p>有些工作看起来稳定，只是因为它短期没有变化；但行业下行、团队边缘、能力停滞，本身就是长期风险。真正的稳定不是今天不辛苦，而是三年后仍然有选择权。</p>
<p>如果一份工作既学不到东西，也认识不到更优秀的人，还没有收入提升空间，它给的轻松只是短期舒适。长期看，这种舒适会消耗人的议价能力。</p>
<p>职业选择最重要的不是避开所有压力，而是选择值得承受的压力。能把人推向更高能力、更好圈层和更强收入结构的压力，才有意义。</p>

<h2 id="final-view">八、结论：工作不是目的，是进入趋势的门票</h2>
<p>钱多、事少、离家近可以作为筛选项，但不能成为全部标准。真正值得选择的工作，应该让人学到东西、交到朋友、赚到钱，并且尽可能站在趋势的上升侧。</p>
<p>个人努力只有踩到时代的势上，才会被放大。找工作的核心，不是找一个看起来舒服的位置，而是找一个能让未来十年更宽的位置。</p>
'''


BODY_XHS = r'''
<p>小红书不能只被理解成一个种草平台，也不能只被理解成情绪争议场。它真正值得重视的地方，在于聚集了大量年轻、女性、一二线城市、消费决策能力强的人群。</p>
<p>很多人只看到了争议，却忽略了平台背后的用户结构和商业价值。一个平台是否值得投入，不只看流量总量，更要看流量是否精准，用户是否有消费能力，内容是否能降低成交成本。</p>

<h2 id="user-structure">一、用户结构决定平台价值</h2>
<p>小红书的月活规模已经很大，约 3.5 亿级别。更关键的是结构：男女比例大约 3 比 7，女性用户明显更多；95 后占比超过 50%；一二线城市用户占比也超过 50%。</p>
<p>这意味着它不是一个泛泛的娱乐平台，而是聚集了大量年轻女性消费决策者。她们对生活方式、审美、教育、职场、情感、家居、旅游、护肤、穿搭、母婴、宠物、个人成长都有强需求。</p>
<p>理解这一点，很多争议就能重新解释。平台讨论多、情绪强、观点密集，恰恰说明用户愿意表达、愿意参与、愿意围绕生活决策交换信息。</p>

<h2 id="gender-discussion">二、性别议题背后，是用户需求的真实表达</h2>
<p>围绕女性、两性关系、婚恋、消费和生活方式的讨论，常常被外界简单贴上“对立”的标签。但从产品视角看，这些内容背后是用户在表达真实困惑：关系怎么处理，消费怎么选择，生活怎么安排，怎样让自己过得更好。</p>
<p>年轻女性用户越集中，平台上的表达就越鲜明。外部的人如果只用嘲讽眼光看，就会错过理解用户的机会。真正要做内容或商业转化的人，应该把这些讨论当成用户需求样本，而不是只当成情绪噪音。</p>

<h2 id="male-perspective">三、理解女性用户，也是在理解消费决策</h2>
<p>无论做内容、卖产品，还是改善两性关系，都应该理解女性用户。因为在大量消费场景中，女性不仅是购买者，也是决策者、筛选者和传播者。</p>
<p>很多男性用户不愿意研究小红书，觉得那里离自己很远。问题在于，如果不了解女性用户如何表达需求、如何比较产品、如何做决策，就很难理解今天消费市场的一部分核心逻辑。</p>
<p>平台里的笔记、评论、经验分享、避坑内容，都在呈现真实需求。谁能从里面读出问题，谁就更容易做出被需要的内容和产品。</p>

<h2 id="precise-traffic">四、流量不一定最大，但足够精准</h2>
<p>小红书的流量未必比所有大平台都大，但它的价值在于精准。这里的用户往往有明确问题、明确场景和明确消费意愿。她们不是随便刷到一个热闹内容，而是在寻找答案、经验、产品和参考。</p>
<p>精准流量的商业价值很高。一个用户主动搜索、主动比较、主动私信，和一个用户只是被动刷到内容，转化成本完全不同。</p>
<p>所以做转化时，不一定需要极大流量。只要内容足够具体、足够可信、足够贴近场景，用户就会主动进入主页、查看产品、提出问题，销售和交付的运营成本会明显降低。</p>

<h2 id="content-style">五、内容要具体，不要空泛表演</h2>
<p>小红书更适合具体内容：真实经验、清晰步骤、前后对比、避坑清单、场景化建议、个人案例。空泛鸡汤和宏大叙事很难长期形成信任。</p>
<p>这类平台的用户会看细节，会比较，会问问题，也会根据评论和主页判断一个人是否可信。因此内容不能只追求热闹，而要能解决一个具体问题。</p>
<p>比如做职场、情感、家居、教育、个人成长或副业内容，最重要的是把问题拆细。越具体，越容易让用户觉得“这就是我的情况”。</p>

<h2 id="low-cost-conversion">六、低成本成交来自信任，而不是话术</h2>
<p>小红书的成交并不只靠挂商品，也不只靠强销售。很多时候，内容本身就是信任建立过程。用户先通过内容判断专业度，再通过主页判断稳定性，最后才决定是否咨询或购买。</p>
<p>如果内容做得足够好，即便不直接销售，也会产生后续转化。因为用户看到的是一个持续解决问题的人，而不是一个只想成交的人。</p>
<p>这也是平台适合长期经营的原因。内容越垂直，表达越真实，用户越容易沉淀。沉淀下来的不是泛流量，而是有明确需求的人。</p>

<h2 id="business-fit">七、什么样的业务更适合在小红书做</h2>
<p>适合小红书的业务，通常有几个特点：用户愿意比较，决策需要经验，结果与生活质量相关，购买前需要信任。教育、咨询、女性消费、家居、旅行、本地生活、职业成长、情感关系、个人形象，都比较符合这些条件。</p>
<p>不适合的业务也很明显：纯低价冲动消费、缺少差异化的标品、无法讲清楚价值的服务、交付质量不稳定的产品。因为用户越会比较，越会放大信任优势，也越会放大交付问题。</p>
<p>所以进入这个平台之前，先不要问能不能起量，而要问自己的产品能不能经得起用户比较。经得起比较，内容才会变成放大器；经不起比较，流量越大，风险越大。</p>

<h2 id="operating-method">八、运营方法：问题前置，案例证明，路径清晰</h2>
<p>有效内容通常先把问题说准，再给出判断，最后给出路径。比如用户为什么焦虑、为什么踩坑、为什么不知道怎么选，这些问题越具体，越容易建立连接。</p>
<p>案例比口号更有说服力。前后对比、真实场景、决策过程、错误示范、清单总结，都能降低理解成本。用户不是不愿意付费，而是不愿意为模糊价值付费。</p>
<p>路径清晰也很重要。内容解决认知，主页承接信任，私信承接问题，产品承接需求，交付承接口碑。每一步都顺，转化才会自然。</p>

<h2 id="final-view">九、结论：不能忽略这个平台</h2>
<p>小红书值得重视，不是因为它没有争议，而是因为它的用户结构、消费意愿、内容场景和转化路径都很鲜明。年轻女性、一二线城市、消费能力、精准需求，这些因素叠加在一起，构成了很强的商业基础。</p>
<p>不管是想理解女性、改善关系，还是想在 2026 年多赚一些小钱，都不能忽略这个平台。真正有价值的不是刷热闹，而是从用户表达里读出需求，从需求里找到内容和产品机会。</p>
'''


BODY_PERSONALITY = r'''
<p>自媒体做不起来，很多时候不是因为缺少技巧。选题技巧、爆款公式、拍摄方法当然有用，但大部分人真正倒下的地方，不是技术，而是性格上的弱点。</p>
<p>一个人想把自媒体做起来，至少要过三道关。第一关是敢不敢开始，第二关是能不能长期面对失败，第三关是能不能持续向前看。这三关表面是运营问题，本质是人性问题。</p>

<h2 id="not-tech-first">一、不要把所有问题都归因于技术</h2>
<p>很多人学了很多课程，也拍了很多内容，结果仍然做不起来。于是继续研究技巧，继续找模板，继续等一个万能公式。但如果底层状态没有变，技巧越多，反而越容易拖延。</p>
<p>真正的问题是：怕丢脸，怕没人看，怕被熟人评价，怕失败以后证明自己不行。只要这些心理没有被突破，再多方法都很难落地。</p>
<p>自媒体是一个高度公开反馈的场域。内容发出去以后，数据好坏、评论冷暖、粉丝增减都会直接打到人身上。技术能解决一部分问题，但扛反馈的能力必须自己长出来。</p>

<h2 id="first-barrier-start">二、第一关：先开始，而不是先完美</h2>
<p>很多人卡在开始之前，总想等方向更明确、设备更好、文案更成熟、形象更自然。结果等来等去，真正发出的内容少得可怜。</p>
<p>自媒体的起点不是完美，而是进入反馈。只有内容发出去，才知道用户对什么有反应，自己适合什么表达，哪个方向能持续生产。</p>
<p>刚开始一定会粗糙，这很正常。表达会不顺，节奏会奇怪，选题会跑偏，数据也可能很差。但这些不是失败，而是入场费。没有这些早期笨拙，就没有后面的熟练。</p>

<h2 id="second-barrier-feedback">三、第二关：承受低数据和负反馈</h2>
<p>很多人真正难受的不是创作，而是创作之后没有反馈。辛苦准备的内容，数据平平；认真表达的观点，没有多少人回应；偶尔还有刺耳评价。这时最容易怀疑自己。</p>
<p>但低数据不是终点，它只是信息。它说明选题、表达、标题、节奏或受众匹配有问题。一个内容没起，不代表人不行；十个内容没起，也不代表方向彻底错了。</p>
<p>真正能继续做的人，会把每一次反馈当成调整依据，而不是人格审判。数据差，就复盘；表达弱，就练；选题不准，就换。难点不是知道这些道理，而是在情绪上不被击垮。</p>

<h2 id="third-barrier-forward">四、第三关：失败 100 次，仍然向前看</h2>
<p>自媒体最消耗人的地方，是失败会不断出现。一个内容不行，下一条还可能不行；一个方向刚有起色，过一段时间又失效。平台、用户、热点和竞争都会变化。</p>
<p>真正的规则，是允许自己失败 100 次，然后继续向前看。不要把精力花在反复纠结已经发出去的内容上，而是思考下一条怎样更好。</p>
<p>持续创作的人，必须学会快速翻篇。过去的内容只负责提供经验，不负责定义自己。能不能从失败里拿走信息，然后继续生产，是能否做起来的关键。</p>

<h2 id="custom-growth">五、困境往往针对性格弱点而来</h2>
<p>做着做着会发现，遇到的每一个困境，几乎都在击中自己的性格弱点。怕被评价的人，会遇到公开表达；怕失败的人，会遇到低数据；容易自我怀疑的人，会遇到长期波动；太爱面子的人，会遇到无人理会。</p>
<p>这也是自媒体像修行的原因。它不只是打磨技术，也在逼人处理羞耻感、胜负心、拖延、脆弱、自恋和恐惧。</p>
<p>当意识到困境是为成长量身定制的，努力方向就清楚了。不是单纯学更多技巧，而是补上自己性格里的短板。</p>

<h2 id="training-method">六、训练方法：用流程对抗情绪</h2>
<p>情绪不稳定时，最需要流程。比如固定每天选题，固定写一版文案，固定发布，固定复盘三项数据：用户为什么停留，哪里流失，评论或私信暴露了什么需求。</p>
<p>流程的作用，是让人不必每天靠热情启动。自媒体一旦靠心情做，很快就会断。靠流程做，哪怕状态一般，也能完成最低限度的生产。</p>
<p>复盘也要克制。不要把每条内容都上升到自我价值，只看可以调整的变量：选题是否具体，开头是否清楚，表达是否有冲突，结尾是否给出明确判断。</p>

<h2 id="do-not-hide">七、越怕什么，越要把它变成训练场</h2>
<p>怕表达，就多表达；怕没人回应，就练习在低反馈里继续；怕别人评价，就降低面子成本。自媒体不会绕开这些弱点，它会把弱点全部摆出来。</p>
<p>能做起来的人，不一定一开始更外向、更自信、更会表达，而是更愿意把不舒服的部分变成训练。每一次发布，都是一次对恐惧的脱敏。</p>
<p>当人不再被面子、低数据和失败牵着走，内容能力才会进入真正的复利阶段。</p>

<h2 id="final-view">八、结论：做自媒体，先过人性关</h2>
<p>自媒体当然需要选题、表达、剪辑和运营，但真正决定能不能长期做下去的，是人。能不能开始，能不能承受反馈，能不能失败 100 次还继续向前，这些比公式更底层。</p>
<p>如果想做自媒体或副业，不要只把它当成技术训练。它也是一场个人修行。每一次卡住，都在提示一个需要被解决的性格弱点。</p>
'''


BODY_US_CHINA = r'''
<p>中美对抗之下，很多国家看起来很安静，不是因为他们没有立场，也不是因为他们看不见变化，而是因为旧规则正在松动，新规则还没有完全形成。大家都在判断，谁会赢，谁能提供更稳定的秩序，谁能代表下一阶段的产业能力。</p>
<p>理解这一轮变化，不能只看单个事件。关税战、地缘冲突、资源争夺、美元体系、制造业竞争、高端技术封锁，背后都指向同一个问题：美国过去主导的自由贸易规则正在被它自己改写。</p>

<h2 id="old-rule">一、旧规则的核心，是自由贸易和美元体系</h2>
<p>过去几十年，全球化的底层规则大致是自由贸易、产业分工、美元结算和美国主导的安全秩序。美国掌握高端技术、金融体系和规则解释权，其他国家在分工中寻找自己的位置。</p>
<p>这套规则对很多国家都有好处。资源国卖资源，制造国做制造，消费市场承接商品，美元体系负责结算和储备。只要规则稳定，大家都有动力继续参与。</p>
<p>但问题在于，当规则主导者开始频繁使用关税、制裁、金融工具和安全议题去重塑分配格局时，其他国家就会意识到：旧规则不再只是中性的交易框架，也可能变成竞争工具。</p>

<h2 id="tariff-war">二、关税战意味着美国亲手打破部分旧规则</h2>
<p>当美国发起关税战，它打破的不只是某些商品的价格体系，也是在削弱自己过去倡导的自由贸易原则。过去说市场开放、贸易自由、规则优先，现在开始强调本土产业、关税保护和供应链安全。</p>
<p>这不是简单的政策摇摆，而是结构性变化。美国发现，单靠金融、消费和高端技术优势，未必能继续压住中国制造的追赶速度，于是开始用规则外的手段重新划线。</p>
<p>关税战的信号是：旧时代正在结束。新的规则还没有完全成型，所以其他国家不会急着站队。他们更愿意安静观察，等待更清楚的力量对比。</p>

<h2 id="why-others-quiet">三、外国安静，是因为谁都不想过早押错</h2>
<p>许多国家并不是没有想法，而是不愿意过早押错。美国仍然拥有金融、军事、科技和盟友体系优势；中国则拥有完整工业体系、超大市场、基础设施能力和制造升级速度。</p>
<p>站在第三方国家角度，最理性的选择往往不是高调表态，而是在两边之间寻找利益最大化。能从美国拿安全和金融资源，也能从中国拿基础设施、制造能力、商品和市场机会。</p>
<p>安静不是没有判断，而是在等待结果。谁能提供更稳定、更低成本、更有增长性的合作，谁就会在新规则里获得更多支持。</p>

<h2 id="manufacturing-core">四、真正的竞争核心，是制造业能力</h2>
<p>这一轮中美竞争，表面是关税、科技和地缘，底层是制造业。制造业决定军工、能源、交通、电子、芯片、装备、消费品和供应链韧性。</p>
<p>中国过去十年在制造业上的进展，不能只用“低端代工”理解。新能源车、动力电池、光伏、风电、工程机械、船舶、高铁、通信设备，都已经进入全球竞争前列。</p>
<p>接下来更难的部分，是高端制造：芯片设备、航空发动机、高端机床、工业软件、先进材料、精密仪器。这些领域才是美国长期死守的高壁垒部分。</p>

<h2 id="china-manufacturing-2025">五、重新看中国制造 2025，会发现路径并不差</h2>
<p>回头看中国制造 2025，会发现过去十年并不是空转。很多当时看起来遥远的方向，已经变成现实产业：新能源汽车全球化，电池产业链领先，光伏成本大幅下降，船舶订单增强，工业体系继续补链。</p>
<p>当然，短板也很清楚。越往高端走，越会遇到美国的技术封锁和规则压力。因为这不再是普通制造竞争，而是对核心优势区的冲击。</p>
<p>中美竞争真正进入深水区，是中国开始挑战美国仍然保持优势的那些领域。只要这些领域被逐步突破，双方就不再是简单上下游关系，而是更接近平起平坐的竞争关系。</p>

<h2 id="new-order">六、新时代会更不确定，也更需要产业判断</h2>
<p>旧规则松动，新规则未定，未来十年会充满不确定性。贸易规则、地缘冲突、能源安全、金融结算、科技封锁，都可能反复变化。</p>
<p>但越是不确定，越要回到硬实力。一个国家能不能稳定提供商品，能不能组织供应链，能不能突破高端制造，能不能保持市场和产业协同，决定它在新规则里的位置。</p>
<p>对普通人来说，宏大叙事不能只停留在情绪上。真正有意义的是看清产业方向：哪些行业会被重塑，哪些岗位会出现，哪些能力会更有价值。</p>

<h2 id="third-party-countries">七、第三方国家看的是利益，不是口号</h2>
<p>很多国家的安静，本质上是现实主义。它们会看谁能提供市场，谁能提供投资，谁能提供安全，谁能提供基础设施，谁能提供更低成本的工业品。</p>
<p>如果某个国家同时依赖美国金融和中国制造，它就不会轻易把话说满。表态太早，意味着未来谈判空间变小；保持弹性，反而能在新旧规则交替时争取更多利益。</p>
<p>所以不要把国际关系理解成简单情绪选择。国家之间首先看利益结构，其次看风险，最后才是叙事。谁能在产业和规则上提供更稳定的利益，谁就能获得更多实际合作。</p>

<h2 id="personal-position">八、个人应该看产业，而不是只看冲突</h2>
<p>宏观冲突会带来情绪，但真正改变个人命运的，是产业迁移和岗位变化。高端制造、国产替代、能源安全、工业软件、机器人、半导体、先进材料，都可能在新规则里获得更高权重。</p>
<p>这意味着职业选择、投资判断和学习方向都要围绕产业能力展开。未来十年，懂产业链、懂工程、懂供应链、懂海外市场、懂技术商业化的人，会更容易吃到结构性红利。</p>
<p>对普通人来说，参与历史不一定是喊口号，也可以是进入一个真正有长期需求的行业，把自己的能力放到国家和产业都需要的位置上。</p>

<h2 id="final-view">九、结论：旧时代落幕，新规则正在形成</h2>
<p>中美对抗让很多国家保持安静，是因为全球正在从旧规则进入新规则。美国仍然强大，但它开始亲手修改过去维护的自由贸易原则；中国仍有短板，但制造业升级已经持续推进。</p>
<p>接下来的十年，是高端制造、供应链安全和产业规则重新定价的十年。每个人既是参与者，也是见证者。真正值得做的，不是只看热闹，而是在产业变化中找到自己的位置。</p>
'''


BODY_RENT_BUY = r'''
<p>房租 2800，月供 3000，买房还是租房？这个问题看起来很简单：月供只比房租多 200，似乎买房更划算。但如果只这么算，很容易在一次重大选择上算错。</p>
<p>买房和租房不是只比较月供和房租，而是比较现金流、首付、机会成本、流动性、风险承受能力、生活稳定性，以及那个最容易被忽略的东西：人生的可能性。</p>

<h2 id="not-monthly-payment">一、不能只看月供和房租差 200</h2>
<p>月租 2800，月供 3000，表面差额只有 200。很多人会本能觉得，既然每个月多付一点就能拥有房子，那当然买房。</p>
<p>问题在于，月供不是买房的全部成本。买房还需要首付、税费、装修、家具家电、物业、维修、贷款利息和长期持有成本。租房虽然没有资产沉淀，但也没有那么高的初始资金占用。</p>
<p>所以真正要比较的，不是 2800 和 3000，而是买房这件事会锁住多少现金，未来多少年不能轻易移动，以及这些现金如果不买房还能创造什么可能。</p>

<h2 id="down-payment">二、首付才是最大变量</h2>
<p>月供差额很小，首付却可能很大。几十万甚至上百万首付，一旦放进房子里，就变成低流动性资产。它不是不能变现，而是变现成本高、周期长，还受到市场价格影响。</p>
<p>如果手里本来就有充足现金，买房后仍然有安全垫，压力会小很多。但如果买房需要掏空家庭积蓄，甚至还要借钱凑首付，那月供再接近房租，也不能说明这笔决策轻松。</p>
<p>现金流紧张时，房子会从安全感变成压力源。工作变化、收入下降、家庭支出增加、城市迁移需求，都可能让原本看似稳妥的选择变得被动。</p>

<h2 id="opportunity-cost">三、机会成本决定这笔钱是否被锁死</h2>
<p>买房最大的隐性成本，是机会成本。首付如果不买房，可以用于投资、学习、创业、换城市、换职业、做副业、保留现金流，或者给家庭更多缓冲。</p>
<p>这不是说买房一定不好，而是要看房子是否真的比其他选择更值得。房价上涨时期，房子既是居住，也是资产增值工具；但如果房价横盘甚至下行，房子更像消费品和稳定器，而不是高收益投资。</p>
<p>对年轻人来说，机会成本尤其重要。一个城市、一份工作、一段关系、一个创业机会，都可能因为房子被锁住。房子提供确定性，也会减少选择权。</p>

<h2 id="x-factor">四、真正要问的是：你的 X 是什么</h2>
<p>买房与租房之间，有一个变量叫 X。这个 X 可能是稳定感，可能是孩子上学，可能是家庭关系，可能是父母安心，可能是城市归属，也可能是人生自由度。</p>
<p>如果你的 X 是稳定，是扎根，是给家人确定生活，那么买房可能值得。即便财务上不一定最优，但心理价值和家庭价值可以补足一部分差额。</p>
<p>如果你的 X 是自由，是职业迁移，是创业试错，是把现金流留在手里，那么租房可能更适合。租房不是失败，买房也不是成功，它们只是服务不同人生目标的工具。</p>

<h2 id="family-decision">五、房子是家庭决策，不是单人算术题</h2>
<p>对 90% 以上的中国家庭来说，买房、租房、卖房都是最重要的决定之一。它牵涉的不只是个人偏好，还包括父母、伴侣、孩子、工作、城市和家庭资产负债表。</p>
<p>所以不能只凭一张简单账单决定，也不能只听某一种价值观。有人觉得有房才安全，有人觉得现金流才安全；有人追求学区，有人追求职业机会；有人愿意背贷款，有人更重视流动性。</p>
<p>真正稳妥的做法，是把现金流、首付、风险、城市发展、家庭需求和未来五年规划放在一起讨论。房子不是单点选择，而是会影响很长时间的系统选择。</p>

<h2 id="when-to-buy">六、什么情况下更适合买</h2>
<p>如果工作和城市基本稳定，家庭现金流充足，首付之后仍然留有安全垫，房子能解决教育、通勤、照顾老人或长期居住问题，那么买房就不只是财务问题，也是在购买生活秩序。</p>
<p>尤其是家庭成员都需要稳定空间时，房子的价值不能只用租售比衡量。它可能减少搬家成本，减少不确定性，也让家庭关系更容易围绕固定空间展开。</p>
<p>但即便适合买，也要控制杠杆。不要因为月供看起来接近房租，就忽视收入波动。一套房子如果让家庭没有任何现金缓冲，它带来的安全感会被贷款压力抵消。</p>

<h2 id="when-to-rent">七、什么情况下更适合租</h2>
<p>如果职业还在变化，城市还没确定，未来几年可能换行业、换公司、创业或迁移，那么租房的流动性更有价值。租房让人保留选择权，能更快响应新的机会。</p>
<p>如果首付会掏空积蓄，或者买房后现金流长期紧张，也更适合先租。人生不是只有房产一条资产路径，现金、能力、事业和人脉同样可能成为未来的安全垫。</p>
<p>租房不是没有根，买房也不是自动上岸。真正重要的是让居住选择服务人生目标，而不是让人生被居住选择反向锁住。</p>

<h2 id="final-view">八、结论：买房不是答案，可能性才是答案</h2>
<p>房租 2800、月供 3000，并不能直接推出买房更划算。关键在于首付占用、机会成本、现金流安全和人生目标。差额 200 只是表层，真正重要的是买房会不会让生活变窄。</p>
<p>人生不过三万多天，房屋千万座，睡觉所需空间并不大。有人梦想中的 X 就是一套属于自己的房子，那就勇敢追求；但也要承认，人生还有很多种可能性，不一定只通向一套房子。</p>
'''


BODY_SELF_MEDIA_SYSTEM = r'''
<p>做好自媒体，不需要一开始就有巨大优势、特别人设或清晰方向。更现实的路径，是把自己已经拥有的技能、项目、经验或稳定收入来源，迁移到内容平台上，让内容成为业务放大器。</p>
<p>自媒体不是凭空重新创业，而是把已有价值重新包装、传播、交付和变现。没有产品，再大的流量也容易浪费；没有信任，再好的产品也很难成交。</p>

<h2 id="start-with-existing-value">一、先从已有优势开始，而不是凭空找赛道</h2>
<p>如果是打工人，本身有赖以为生的技能，就从技能开始。如果是小老板，本身有稳定收入项目，就从项目开始。不要一上来就把自媒体理解成完全陌生的赛道。</p>
<p>真正高效的起点，是把正在赚钱的技能或项目搬到线上。职场经验、行业知识、咨询能力、教育能力、产品能力、服务能力，都可以通过内容表达出来。</p>
<p>没有优势的人，也不是不能开始。可以先从记录学习、拆解案例、整理资料、输出思考开始。重点是进入持续表达，而不是等待一个完美定位。</p>

<h2 id="three-business-models">二、自媒体商业化主要看三类收入</h2>
<p>常见变现方式大致分三类：咨询服务、课程产品、广告合作。不同业务模型，对内容、直播、私域和交付的要求不同。</p>
<p>咨询服务更依赖信任和专业度，内容负责筛选客户，私域负责沟通和成交，交付质量决定复购与口碑。课程产品需要内容、直播和私域配合，因为课程通常不是一次简单购买，而是一个信任逐步建立的过程。</p>
<p>广告合作主要看账号人设、内容垂直度和播放量中位数。它更依赖内容表现，与私域和直播关系相对弱一些。</p>

<h2 id="short-video-core">三、短视频是多数业务的核心入口</h2>
<p>无论是接咨询、卖课程还是接广告，短视频都很关键。它既能带来潜在咨询客户，也能给课程积累信任，还能直接影响商业合作。</p>
<p>对口播型账号来说，短视频包含选题、文案、拍摄、剪辑、投放五个环节。其中最重要的通常是选题和文案。因为内容能不能击中用户，先取决于说什么，再取决于怎么说。</p>
<p>如果不做投放，完全依靠自然流量，选题和文案就更重要。一个超级个体的资源主要是时间，时间应该投入到最能影响收入的环节。</p>

<h2 id="delegate-low-leverage-work">四、把低杠杆工作交出去，把时间留给核心环节</h2>
<p>当业务跑通之后，要学会拆分工作。拍摄、剪辑、流程运营、课服、资料整理、交付辅助，都可以逐步交给助理或团队。</p>
<p>真正不能轻易交出去的，是最核心的价值环节。对一个以表达和观点为核心的账号来说，选题、文案、认知判断和关键交付，往往仍然要自己把控。</p>
<p>清楚重点在哪里，就知道什么可以交出去。释放出来的时间，应该继续投入到高杠杆环节，而不是被新的琐事填满。</p>

<h2 id="product-ladder">五、搭建产品矩阵，服务不同层级用户</h2>
<p>用户可以按付费意愿和付费能力拆成四类：有能力也有意愿，有能力但无意愿，无能力但有意愿，既无能力也无意愿。不同人群需要不同服务策略。</p>
<p>没有意愿的用户，需要先理解趋势、看到收益、建立信任，这主要靠内容。有意愿但付费能力弱的人，需要低门槛产品，比如价格不高但体系完整的课程。有能力且有强需求的人，则可能需要定制化咨询或线下课。</p>
<p>一套 398 元左右的课程，可以承担低门槛、高性价比、系统入门的角色；4K 到 1W 的咨询服务，更适合解决点状问题；线下课则可以服务那些想要更深度交流、更强个性化反馈的用户。</p>

<h2 id="trust-and-product">六、自媒体最终是产品和 IP 信任度的生意</h2>
<p>自媒体表面是内容和流量，底层是产品和信任。内容可以让人看见你，流量可以带来机会，但产品和服务决定这件事能不能长期做。</p>
<p>如果产品有问题，交付有问题，承诺和结果不匹配，信任会快速崩塌。越是公开平台，好事传播快，坏事传播也快。</p>
<p>所以自媒体不是只研究怎么起号，也不是只研究怎么成交。真正长期的做法，是持续提供好内容、好产品、好服务，并且不断提升自己的专业能力。</p>

<h2 id="stage-path">七、不同阶段，重点完全不同</h2>
<p>冷启动阶段，最重要的是找到能持续表达的方向。不要一开始就追求团队化、精细化和复杂产品，先证明自己能持续生产内容，并且有人愿意反馈。</p>
<p>增长阶段，最重要的是找出带来精准用户的内容结构。哪些选题能带来咨询，哪些表达能带来信任，哪些内容只是热闹但不带来业务，都要分清楚。</p>
<p>变现阶段，最重要的是产品和交付。流量来了以后，如果产品承接不住，反而会暴露问题。长期阶段，最重要的是复购、口碑和团队协作，因为一个人不可能永远靠体力硬扛。</p>

<h2 id="content-to-cash">八、从内容到成交，中间要有完整链路</h2>
<p>内容负责吸引对的人，主页负责解释你是谁，私域负责承接具体问题，产品负责提供解决方案，交付负责建立口碑。任何一个环节断掉，商业化都会变难。</p>
<p>很多账号内容数据不错，但赚不到钱，是因为没有产品；有些账号产品不错，但内容不稳定，是因为入口不足；还有一些账号成交不错，但交付差，最后信任被透支。</p>
<p>做自媒体要把链路画出来：用户从哪里来，为什么相信，买什么，怎样交付，交付后怎样复购或转介绍。链路清楚，才知道该优化哪里。</p>

<h2 id="final-view">九、结论：自媒体不是流量游戏，而是业务系统</h2>
<p>做好自媒体，要从已有价值开始，用内容获取精准用户，用短视频建立入口，用私域和直播承接信任，用产品矩阵服务不同层级需求，再用交付质量支撑长期口碑。</p>
<p>流量只是开始，产品和信任才是终局。把它当成一个完整业务系统，而不是单纯流量游戏，才有机会长期做成。</p>
'''


BODY_ONE_MILLION = r'''
<p>人生第一个 100 万，难的不是数字本身，而是思维模式。没赚到过的人，会觉得一个月要赚十几万像天文数字；赚到过的人，会发现它不是神话，而是一套可以拆解、验证、迭代的商业系统。</p>
<p>100 万不是靠一句口号达成的，它背后有生活方式、业务模型、关键环节、产品矩阵、风险承担和机缘。真正跨过去的人，往往不是突然变聪明，而是把赚钱这件事从愿望变成系统。</p>

<h2 id="life-behind-million">一、百万背后，先是生活方式的改变</h2>
<p>年入百万听起来光鲜，但真实生活可能并不轻松。高收入背后通常是高工作强度、高自我要求和长期不确定性。</p>
<p>当一个人把自己变成超级个体，时间会被业务高度占据。每周工作 60 多个小时并不夸张，选题、文案、内容、直播、私域、咨询、课程、交付都会挤到同一个系统里。</p>
<p>所以第一个问题不是“想不想赚 100 万”，而是“愿不愿意接受这种生活方式”。如果仍然希望用轻松稳定的状态换来极高回报，预期本身就不匹配。</p>

<h2 id="short-video-business">二、短视频支撑了所有收入入口</h2>
<p>在一个以内容为核心的业务模型里，短视频是底层入口。它可以带来咨询客户，可以卖课，可以接广告，也可以沉淀信任。</p>
<p>咨询服务看专业和信任，课程销售看内容、直播和私域，广告合作看账号人设和播放表现。三个板块都离不开短视频，因为短视频决定用户最初从哪里认识你。</p>
<p>如果每周 60 多小时工作，其中 40 多小时投入短视频，真正投入最多的又是选题和文案，这不是偶然。选题决定用户愿不愿意停下，文案决定用户愿不愿意相信。</p>

<h2 id="course-data">三、数据会告诉你业务重点在哪里</h2>
<p>从实际业务看，课程卖出 1800 多份，其中 70% 的销量来自直播间；而直播间销售里，95% 又来自粉丝。这说明直播很重要，但直播成交的前提仍然是前端内容带来的信任积累。</p>
<p>非粉丝直接成交只有 5%，意味着陌生人第一次接触就下单的比例很低。真正的成交路径，是内容先建立认知，粉丝关系沉淀信任，直播或私域再完成转化。</p>
<p>这组数据会倒逼资源分配：如果短视频支撑所有业务收入，就要把最多时间放在短内容系统；如果选题和文案最重要，就要把最多精力放在选题和文案。</p>

<h2 id="product-matrix">四、产品矩阵要覆盖不同需求层级</h2>
<p>只有一套低价课，容易承接入门用户，但很难服务高需求用户。398 元左右的课程适合做高性价比入口，提供完整体系、配套工具和基础服务。</p>
<p>但有一部分人付费能力更强，也需要更定制化的服务。他们可能先买课程，觉得还不够，再购买 4K 到 1W 的咨询服务。咨询能解决点状问题，但时间短，不适合长期陪伴。</p>
<p>这时就需要新的产品层级，例如线下课。线下课可以更深度地服务高意愿、高能力用户，也更适合建立强连接。产品矩阵越清晰，业务收入越不依赖单一产品。</p>

<h2 id="delegate-and-focus">五、把可拆分工作交出去，把自己留在关键位置</h2>
<p>当业务增长后，一个人不可能长期包办所有环节。拍摄、剪辑、私域流程运营、课服、课程运营，都可以逐步拆分给助理。</p>
<p>但关键位置不能轻易丢掉。对超级个体来说，最核心的资产是认知、选题、文案、表达和关键交付。把这些交出去，就可能丢掉业务灵魂。</p>
<p>正确的扩张不是盲目招人，而是明确哪些环节最影响收入，哪些环节只是必要但低杠杆的执行。释放时间后，要把时间重新投入到最重要的地方。</p>

<h2 id="risk-and-chance">六、机缘来自尝试，不来自等待</h2>
<p>新的业务尝试一定伴随风险。它可能成功，也可能失败。但不尝试，就不会遇到新的机缘。机缘往往不是凭空降临，而是在已经行动的人身上发生。</p>
<p>曾经做自媒体没有起来，后来因为一次同事分享副业经历，重新看到机会，于是冒着风险尝试。三个月收到三十单 1999 元咨询，第一次通过自媒体完成商业闭环，也获得了离开原有工作的底气。</p>
<p>这件事不是从一开始就百分百确定能成。它发生在不熟悉、不擅长、没有完全验证的方法里。正因为愿意冒风险尝试，才间接促成后面的百万跨越。</p>

<h2 id="four-stages">七、从 0 到 100 万，要经历四个阶段</h2>
<p>第一阶段是验证需求：有没有人愿意为你的内容、咨询、课程或服务付费。第二阶段是验证入口：什么内容能稳定带来精准用户。第三阶段是验证交付：用户付费之后，能不能真正得到结果。第四阶段是验证复制：这套模式能不能在不完全依赖体力的情况下继续扩大。</p>
<p>很多人卡在第一阶段，因为一直没有真实成交；也有人卡在第二阶段，因为靠偶然爆发，无法持续获取用户；还有人卡在第三阶段，因为卖得出去但交付跟不上。</p>
<p>第一个 100 万不是单纯销售额，而是一个系统逐步跑通的结果。系统越稳定，收入越不像偶然。</p>

<h2 id="risk-control">八、冒险不是乱来，而是控制风险地尝试</h2>
<p>承担风险不等于盲目all in。真正有效的冒险，是用可承受的成本换取高价值反馈。比如先用业余时间验证副业，先用小产品验证需求，先用咨询验证用户痛点，再决定是否投入更多资源。</p>
<p>风险控制的关键，是不要让一次失败直接出局。现金流要留安全垫，产品要小步试错，方向要根据数据调整。敢冒险和会算账并不矛盾。</p>
<p>超级个体最需要的能力，是在不确定性里持续行动，又不被单次失败击穿。这样才有机会等到机缘，也有能力接住机缘。</p>

<h2 id="final-view">九、结论：第一个 100 万，是系统和机缘的叠加</h2>
<p>赚到人生第一个 100 万，不是单点爆发，而是系统能力和机缘叠加。短视频提供入口，直播和私域完成转化，课程与咨询承接需求，产品矩阵提高客单，交付质量维持信任。</p>
<p>但系统之外，还需要持续尝试带来的机缘。一个人只有不断进入真实市场，承担风险，接住反馈，才可能遇到改变命运的关键节点。超级个体的商业变现，本质上就是把个人能力、内容能力、产品能力和行动勇气组合起来。</p>
'''


base.POSTS = [
    base.Post(
        slug="ordinary-first-pot-gold-overdraft-certainty",
        title="普通人的第一桶金为什么越来越难：透支、成全别人和摆脱确定性",
        desc="第一桶金不是等常规努力自然发生，而是普通人在起点低时集中资源、借势强者、接受不确定性的结果。",
        category="成长",
        series="普通人破局",
        tags=["第一桶金", "普通人", "副业", "职场", "创业", "确定性", "个人成长"],
        minutes=11,
        body=BODY_FIRST_POT,
        accent=("#111827", "#7c3aed", "#f59e0b"),
        required=["80 个小时", "半年", "成全别人", "90%", "5%", "确定性", "三十岁之前", "七八种"],
        minimum=2500,
    ),
    base.Post(
        slug="job-search-trend-matching-new-productivity",
        title="找工作的核心思路：匹配风口、锚定趋势，而不是只盯钱多事少",
        desc="好工作要同时看学习、连接和收入，更要看个人努力是否踩在新质生产力与产业趋势的上升侧。",
        category="职场",
        series="职业选择",
        tags=["找工作", "职业选择", "新质生产力", "趋势", "智能制造", "智慧医疗", "低空经济"],
        minutes=8,
        body=BODY_CAREER,
        accent=("#0f172a", "#2563eb", "#14b8a6"),
        required=["钱多", "事少", "离家近", "学到东西", "交到朋友", "赚到钱", "新质生产力", "智能制造", "智慧医疗", "低空经济"],
        minimum=1950,
    ),
    base.Post(
        slug="xiaohongshu-young-female-consumption-decision-platform",
        title="为什么一定要重视小红书：年轻女性、消费决策和精准流量",
        desc="小红书的价值不只是流量，而是年轻女性、一二线城市、消费能力和低成本信任转化共同形成的商业土壤。",
        category="商业",
        series="内容平台",
        tags=["小红书", "内容平台", "女性用户", "消费决策", "精准流量", "商业转化"],
        minutes=10,
        body=BODY_XHS,
        accent=("#111827", "#db2777", "#f97316"),
        required=["小红书", "3.5 亿", "3 比 7", "95 后", "一二线城市", "女性用户", "消费能力", "精准流量"],
        minimum=2100,
    ),
    base.Post(
        slug="self-media-personality-weakness-three-barriers",
        title="自媒体做不起来，不是技巧不够，而是性格弱点挡在三道关前",
        desc="自媒体的关键不只是选题和公式，而是能否开始、承受反馈、允许失败并持续向前。",
        category="成长",
        series="自媒体方法论",
        tags=["自媒体", "内容创作", "性格弱点", "选题", "表达", "失败", "副业"],
        minutes=7,
        body=BODY_PERSONALITY,
        accent=("#111827", "#0891b2", "#84cc16"),
        required=["三道关", "选题", "失败 100 次", "性格弱点", "人性", "修行"],
        minimum=1750,
    ),
    base.Post(
        slug="china-us-rules-manufacturing-new-order-quiet-countries",
        title="中美对抗为什么外国都很安静：旧规则失效与高端制造新秩序",
        desc="关税战、自由贸易原则松动和制造业升级，正在把全球带入旧规则退场、新规则形成的阶段。",
        category="观察",
        series="全球秩序",
        tags=["中美关系", "关税战", "自由贸易", "制造业", "中国制造2025", "高端制造", "全球化"],
        minutes=12,
        body=BODY_US_CHINA,
        accent=("#111827", "#dc2626", "#f59e0b"),
        required=["自由贸易", "关税战", "制造业", "中国制造 2025", "高端制造", "旧规则", "新规则"],
        minimum=2200,
    ),
    base.Post(
        slug="rent-2800-mortgage-3000-buy-or-rent-life-possibility",
        title="房租 2800、月供 3000：买房还是租房，关键不在月供差 200",
        desc="买房与租房不能只比月供和房租，还要看首付、机会成本、流动性、家庭需求和人生可能性。",
        category="生活",
        series="家庭资产",
        tags=["买房", "租房", "房贷", "现金流", "机会成本", "家庭资产", "生活选择"],
        minutes=8,
        body=BODY_RENT_BUY,
        accent=("#111827", "#0f766e", "#22c55e"),
        required=["2800", "3000", "月供", "首付", "机会成本", "流动性", "X", "三万多天"],
        minimum=1900,
    ),
    base.Post(
        slug="how-to-build-self-media-business-system-product-trust",
        title="怎么做自媒体：从优势迁移到产品矩阵和 IP 信任",
        desc="自媒体不是单纯流量游戏，而是把已有价值搬到线上，用内容、私域、产品和交付构成完整业务系统。",
        category="商业",
        series="自媒体方法论",
        tags=["自媒体", "短视频", "私域", "直播", "课程", "咨询", "产品矩阵", "IP信任"],
        minutes=12,
        body=BODY_SELF_MEDIA_SYSTEM,
        accent=("#111827", "#4f46e5", "#06b6d4"),
        required=["打工人", "小老板", "短视频", "直播", "私域", "398", "4K 到 1W", "产品矩阵", "IP 信任"],
        minimum=2000,
    ),
    base.Post(
        slug="first-one-million-super-individual-business-review",
        title="如何赚到人生第一个 100 万：超级个体、产品矩阵与机缘",
        desc="第一个 100 万来自内容入口、产品承接、私域转化、交付信任和持续尝试带来的机缘。",
        category="商业",
        series="普通人破局",
        tags=["100万", "超级个体", "自媒体", "课程", "咨询", "私域", "商业变现", "副业"],
        minutes=14,
        body=BODY_ONE_MILLION,
        accent=("#111827", "#9333ea", "#22c55e"),
        required=["100 万", "60 多个小时", "1800 多份", "70%", "95%", "398", "4K 到 1W", "三十单", "1999", "超级个体", "机缘"],
        minimum=2200,
    ),
]


def cards_from(text: str) -> list[str]:
    return re.findall(r'<a href="[^"]+" class="a-block">.*?</a>', text, re.S)


def card_href(card: str) -> str:
    match = re.match(r'<a href="([^"]+)" class="a-block">', card)
    if match is None:
        raise RuntimeError("card href missing")
    return match.group(1)


def pagination_nav(page: int, total: int) -> str:
    previous = "" if page == 1 else "/" if page == 2 else f"/page/{page - 1}/"
    nxt = f"/page/{page + 1}/" if page < total else ""
    left = f'<a class="pagination-action" href="{previous}"><span class="pagination-action-icon" aria-hidden="true">‹</span></a>' if previous else '<span class="pagination-action disabled"><span class="pagination-action-icon" aria-hidden="true">‹</span></span>'
    right = f'<a class="pagination-action" href="{nxt}"><span class="pagination-action-icon" aria-hidden="true">›</span></a>' if nxt else '<span class="pagination-action disabled"><span class="pagination-action-icon" aria-hidden="true">›</span></span>'
    return f'''<div class="pagination">
    <a id="globalBackToTop" class="pagination-action animated-visibility invisible" href="#top"><span class="pagination-action-icon" aria-hidden="true">↑</span></a>
    {left}
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">{page}<br><div style="display:inline-block;transform:rotate(-28deg);margin:2px 0">-</div><br>{total}</span></div>
    {right}
  </div></div>
    <div class="pagination">
    {left}
    <div class="pagination-indicator"><span style="text-align:center;line-height:1.2em">{page}/{total}</span></div>
    {right}
  </div>'''


def page_html(template: str, cards: list[str], page: int, total: int) -> str:
    first = template.find('<a href="', template.find('post-list-container'))
    matches = list(re.finditer(r'<a href="[^"]+" class="a-block">.*?</a>', template, re.S))
    if first == -1 or not matches:
        raise RuntimeError("pagination card markers missing")
    result = template[:first] + "\n".join(cards) + template[matches[-1].end():]
    result = re.sub(
        r'(<div id="extraContainer" class="extra-container"><div class="toc-wrapper"></div>).*?(<div id="single-column-footer">)',
        lambda m: m.group(1) + pagination_nav(page, total) + "\n    " + m.group(2),
        result,
        count=1,
        flags=re.S,
    )
    url = base.SITE + ("/" if page == 1 else f"/page/{page}/")
    result = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', result, count=1)
    return re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', result, count=1)


def rebuild_pagination(outputs: dict[str, str | None]) -> tuple[int, int]:
    template = outputs["index.html"]
    cards = cards_from(template)
    previous_pages = 1
    for page in range(2, 200):
        source = get_file_at_active_ref(f"page/{page}/index.html")
        if source is None:
            break
        previous_pages = page
        cards.extend(cards_from(source))
    unique_cards: list[str] = []
    seen: set[str] = set()
    for card in cards:
        href = card_href(card)
        if href not in seen:
            seen.add(href)
            unique_cards.append(card)
    cards = unique_cards
    total = 1 + ((max(0, len(cards) - PAGE1_SIZE) + PAGE_SIZE - 1) // PAGE_SIZE)
    outputs["index.html"] = page_html(template, cards[:PAGE1_SIZE], 1, total)
    cursor = PAGE1_SIZE
    for page in range(2, total + 1):
        outputs[f"page/{page}/index.html"] = page_html(template, cards[cursor:cursor + PAGE_SIZE], page, total)
        cursor += PAGE_SIZE
    for page in range(total + 1, previous_pages + 1):
        outputs[f"page/{page}/index.html"] = None
    return len(cards), total


def create_commit(outputs: dict[str, str | None], ref) -> str:
    entries = []
    for path, content in sorted(outputs.items()):
        if content is None:
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        blob = base.run_gh(["-X", "POST", base.endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = base.run_gh(["-X", "POST", base.endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": entries})
    commit = base.run_gh(
        ["-X", "POST", base.endpoint("git/commits"), "--input", "-"],
        {"message": "Publish eight life and self media articles", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    base.run_gh(["-X", "PATCH", base.endpoint(f"git/refs/heads/{base.BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def validate_extra(outputs: dict[str, str | None], card_count: int, total_pages: int) -> None:
    failures: list[str] = []
    forbidden = [
        "Bilibili", "哔哩哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主", "这期", "本期",
        "作者说", "他提到", "观看", "点赞", "订阅", "投币", "收藏", "下期", "关注", "欢迎收看", "感谢大家", "三连", "BV1",
    ]
    for post in base.POSTS:
        article = outputs[f"2026/{post.slug}/index.html"] or ""
        cover = outputs[f"images/posts/{post.slug}/cover.svg"] or ""
        for word in forbidden:
            if word in article or word in cover:
                failures.append(f"{post.slug}: forbidden wording {word}")
    all_hrefs: list[str] = []
    for page in range(1, total_pages + 1):
        path = "index.html" if page == 1 else f"page/{page}/index.html"
        html = outputs.get(path) or ""
        hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', html)
        all_hrefs.extend(hrefs)
        if page == 1 and len(hrefs) != PAGE1_SIZE:
            failures.append(f"homepage card count {len(hrefs)} != {PAGE1_SIZE}")
        if page > 1 and page < total_pages and len(hrefs) != PAGE_SIZE:
            failures.append(f"{path} card count {len(hrefs)} != {PAGE_SIZE}")
    if len(all_hrefs) != card_count or len(all_hrefs) != len(set(all_hrefs)):
        failures.append("pagination coverage/duplicates failed")
    expected_prefix = base.PINNED_PREFIX + [post.url_path for post in base.POSTS] + [base.PREV_EXISTING_URL]
    home_hrefs = re.findall(r'<a href="([^"]+)" class="a-block">', outputs["index.html"] or "")
    if home_hrefs[: len(expected_prefix)] != expected_prefix:
        failures.append(f"homepage prefix mismatch: {home_hrefs[:len(expected_prefix)]}")
    if failures:
        raise SystemExit("\n".join(failures))


def render_cover_check(outputs: dict[str, str | None]) -> None:
    out_dir = Path("/tmp/hongshu-career-selfmedia-eight-articles-20260815-output")
    for post in base.POSTS:
        svg = out_dir / f"images/posts/{post.slug}/cover.svg"
        png = Path(f"/tmp/{post.slug}-cover.png")
        subprocess.run(["sips", "-s", "format", "png", str(svg), "--out", str(png)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        probe = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(png)], check=True, stdout=subprocess.PIPE, text=True).stdout
        if "pixelWidth: 1600" not in probe or "pixelHeight: 900" not in probe:
            raise RuntimeError(f"cover render failed: {post.slug}: {probe}")


def write_outputs(outputs: dict[str, str | None]) -> None:
    out_dir = Path("/tmp/hongshu-career-selfmedia-eight-articles-20260815-output")
    if out_dir.exists():
        import shutil
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        if content is None:
            continue
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(json.dumps({"local_output": str(out_dir), "files": len([v for v in outputs.values() if v is not None]), "deleted": len([v for v in outputs.values() if v is None]), "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))


def main() -> None:
    global _active_ref
    for attempt in range(3):
        ref = base.get_ref()
        _active_ref = ref
        base.get_file = get_file_at_active_ref
        outputs = base.collect_outputs()
        card_count, total_pages = rebuild_pagination(outputs)
        outputs[f"tasks/{base.MANIFEST_NAME}"] = json.dumps(sorted(path for path, content in outputs.items() if content is not None), ensure_ascii=False, indent=2)
        base.validate(outputs)
        validate_extra(outputs, card_count, total_pages)
        write_outputs(outputs)
        render_cover_check(outputs)
        if base.get_ref().commit_sha != ref.commit_sha:
            continue
        try:
            commit_sha = create_commit(outputs, ref)
        except RuntimeError as exc:
            if attempt < 2 and "Reference update failed" in str(exc):
                time.sleep(2)
                continue
            raise
        print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "cards": card_count, "pages": total_pages, "urls": [post.full_url for post in base.POSTS]}, ensure_ascii=False, indent=2))
        return
    raise RuntimeError("remote reference changed during all attempts")


if __name__ == "__main__":
    main()
