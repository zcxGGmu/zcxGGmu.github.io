from __future__ import annotations

import base64
import html
import json
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote


sys.dont_write_bytecode = True

OWNER = "zcxGGmu"
REPO = "zcxGGmu.github.io"
BRANCH = "gh-pages"
SITE = "https://zcxggmu.github.io"
DATE = "2026-08-09"
BASE_DT = datetime(2026, 8, 9, 20, 30, 0, tzinfo=timezone(timedelta(hours=8)))
PREV_EXISTING_URL = "/2026/ai-skills-agent-fullstack-open-source-daily-20260808/"
PREV_EXISTING_TITLE = "8月8日 AI Skills/Agent 全栈开源项目速览：从技能标准到云端电脑"
TASKS = Path(__file__).resolve().parent
SCRIPT_NAME = Path(__file__).name
MANIFEST_NAME = "publish-three-life-business-articles-20260809-changed-files.json"

PINNED_PREFIX = [
    "/ai-news-radar/",
    "/2026/codeinsights-local-first-agent-workbench/",
    "/2026/what-you-need-to-learn-from-claw-code-repo/",
    "/2026/gaojingqi-investment-system/",
    "/2026/ai-revolution-permanent-underclass-career-selection/",
    "/2026/live-longer-than-earn-fast-investment-infinite-game/",
]

FORBIDDEN = [
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
    "关注",
    "欢迎收看",
    "感谢大家",
    "三连",
    "BV1",
]


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    desc: str
    category: str
    series: str
    tags: list[str]
    minutes: int
    body: str
    accent: tuple[str, str, str]
    required: list[str]
    minimum: int

    @property
    def url_path(self) -> str:
        return f"/2026/{self.slug}/"

    @property
    def full_url(self) -> str:
        return SITE + self.url_path


BODY_MONEY = r'''
<p>赚到第一桶 100 万，不一定靠内幕消息，不一定靠天才创意，也不一定非得抓住一个轰轰烈烈的风口。把一个值 500 元的东西，卖给 2000 个人，就是 100 万。</p>
<p>这听起来像一句废话，偏偏很多人一辈子没有真正想明白。因为“100 万”这个数字太大，大到大脑不知道怎样处理它，只能把它放进“以后再说”的文件夹里，然后就没有然后了。</p>
<p>换一种问法，事情马上变得具体：谁会花 500 元买我的东西？他们在哪里？他们为什么要买？大脑开始转动，开始找人，开始寻找痛点，也开始把一个虚幻的财富目标变成今天能做的动作。</p>

<h2 id="one-million-is-a-customer-problem">一、100 万不是财富问题，而是找人问题</h2>
<p>100 万看起来像一个财富问题，实际上它先是一个找人问题。只要把数字拆开，就能看到目标背后的真实结构：价值、价格、客户数量、成交效率、复购和交付能力。</p>
<p>如果产品或服务定价 500 元，100 万对应 2000 单。每天成交 1 单，需要 2000 天，差不多五年半；每天成交 3 单，需要 667 天，不到两年；每天成交 10 单，需要 200 天，不到七个月。</p>
<p>这组数字没有魔法，但它让人清醒。所谓远大的目标，并不是每天对着自己喊口号，而是能不能找到今天的第一个客户、第二个客户、第三个客户。进度条必须是真实的，而不是感动自己的努力感。</p>
<p>从这个角度看，赚钱不是先问“我怎样一夜之间改变命运”，而是先问“我今天能不能多找到一个愿意付钱的人”。问题一旦具体，焦虑就会减少，行动就会出现。</p>

<h2 id="from-big-goal-to-today-action">二、拆解目标，是把虚幻数字变成今天动作</h2>
<p>拆解的意义，不只是把大目标变小，而是把虚幻的数字变成今天能做的动作。一个人总想着“我要赚 100 万”，很容易陷入空想；一个人每天想着“谁会花 500 元买我的服务”，就会开始接近市场。</p>
<p>目标越宏大，越容易让人麻木。动作越具体，越容易形成反馈。今天发出 20 个有效邀约，和 3 个潜在客户沟通，改一次介绍文案，完成一单交付，都是可以被验证的动作。</p>
<p>这种拆解会带来第一个变化：不再焦虑怎样赚 100 万，而是把注意力放到今天能不能多找到一个客户。每成交一单，目标就往前推进一点；每一次沟通失败，也是在收集市场反馈。</p>
<p>所以真正重要的不是豪言壮语，而是把目标压到足够低、足够近、足够可执行。先成交第一单，再成交第十单，再成交第一百单。100 万就在这些重复动作里逐步变得可见。</p>

<h2 id="five-hundred-yuan-value">三、核心问题不是模式多漂亮，而是 500 元值不值</h2>
<p>一旦目标被拆成“500 元 × 2000 人”，注意力就会从花里胡哨的商业模式，回到一个朴素问题：我的 500 元到底值不值？</p>
<p>两千个人愿意掏钱，前提不是口号漂亮，也不是包装精致，而是你的东西真的值 500 元。所有精力都应该聚焦到把价值做实：解决什么痛点，节省多少时间，带来什么确定结果，交付体验是否稳定。</p>
<p>很多人喜欢研究复杂模型，研究流量打法，研究所谓高级方法，却迟迟不肯面对最基础的问题：一个陌生人为什么要把钱交给我？如果这个答案说不清楚，价格再低也难成交；如果这个答案足够明确，500 元并不贵。</p>
<p>把价值做实，意味着不靠忽悠，不靠一次性成交，不靠消耗信任。真正能重复成交的东西，一定经得起客户比较，也经得起长期口碑检验。</p>

<h2 id="repetition-is-the-best-teacher">四、重复本身就是最好的老师</h2>
<p>第一位客户会告诉你他为什么买。第五十位客户会让你看清他们的共同痛点。第二百位客户会教会你怎样把成交率提高一倍。</p>
<p>很多商业认知不是坐在屋里想出来的，而是在重复接触客户、重复表达价值、重复交付服务时长出来的。客户的问题会逼你改文案，客户的犹豫会逼你改报价，客户的投诉会逼你改交付流程。</p>
<p>重复不是低级劳动。重复到一定数量之后，人的判断会变得敏感：谁是真客户，谁只是闲聊；什么话能打动人，什么话只是自嗨；什么需求值得服务，什么需求会拖垮自己。</p>
<p>这就是为什么简单动作反复做，最后会变成能力。找人的能力、说服的能力、迭代的能力，都是从一单一单的真实接触里练出来的。</p>

<h2 id="why-people-do-not-act">五、道理都懂，为什么还是赚不到钱</h2>
<p>很多人听完“500 元卖给 2000 个人”的逻辑，会点头说有道理，然后照旧没有多赚一分钱。问题不在于道理难懂，而在于人经常被三个障碍卡住。</p>
<p>第一个障碍，是看不起 500 元。总觉得卖 500 元的东西太小，要做就做大的，宁愿花三个月研究一个估值过亿的项目，也不愿意花三天想清楚谁会为自己的服务付 500 元。最后项目还停留在 PPT 里，一分钱也没有赚到。</p>
<p>这不是没有能力，而是眼高手低。把“小钱”看轻，往往会错过最真实的商业训练。能让陌生人付 500 元，本身就是一次严肃的市场验证。</p>
<p>第二个障碍，是熬不过蛰伏期。两千单不是一天卖完的。多数人第七天没看到结果就怀疑自己，第十四天开始换方向，第三十天宣布这条路不行。他们不是输给市场，而是输给自己的耐心。</p>
<p>第三个障碍，是恐惧简单动作，迷信复杂技巧。赚钱当然需要策略，但最初的策略一定要落到找人、沟通、成交、交付。一直研究、分析、规划，却不去找第一个愿意付钱的人，本质上是在用学习逃避行动。</p>

<h2 id="two-paths">六、两种人的结局：聪明地空转，笨拙地积累</h2>
<p>一种人很聪明，用一年时间研究七个方向，做了三个项目。每个项目都觉得差点意思，每个项目都在刚起步时放弃。永远等更好的机会，永远在准备，永远没有结果。</p>
<p>另一种人只做一件小事：帮本地中小企业主做基础账号运营，最开始收费 500 元一个月。第一个月找到 3 个客户，第三个月靠口碑稳定到 10 个客户。第一年累计服务 60 个客户，第二年涨价到 800 元，客户数量继续翻倍。到第四年，小团队服务 200 个客户，年收入超过 100 万。</p>
<p>这条路没有惊天动地的故事，也没有玄乎的概念。它只是死磕一个小而确定的闭环：提供真实价值，收取合理费用，重复这个动作。</p>
<p>很多人一边等待风口，一边错过眼前最小的生意。真正把小生意做扎实的人，最后往往已经不需要风口。因为能力本身会变成风口之外的资产。</p>

<h2 id="three-bottom-assets">七、死磕 2000 单，练出来的是三种底层资产</h2>
<p>只盯着 100 万这个结果，会低估 2000 单真正带来的回报。钱只是结果之一，更重要的是过程里练出的三种底层资产。</p>
<p>第一是找人的能力。你会知道目标客户在哪里，什么样的人最可能付费，什么渠道效率最高，什么圈层只是热闹但没有成交。</p>
<p>第二是说服的能力。说服不是油嘴滑舌，而是准确表达价值、处理顾虑、建立信任、让客户相信交付结果。</p>
<p>第三是迭代的能力。每一次成交和失败都会推动产品进化，价格进化，交付进化，客户筛选进化。能持续迭代的人，不会被一次失败定义。</p>
<p>这三种能力在任何行业、任何方向都能使用。平台倒了，人还在；风口转了，人还在；经济周期来了，人也还在。因为练出来的是自己，而不是依赖某个平台或某个机会的技巧。</p>

<h2 id="start-from-the-smallest-value">八、从最小价值开始，别再等准备好</h2>
<p>很多人会说，我不知道卖什么，我找不到 2000 个客户，我的东西不值 500 元。更真实的问题往往是：不是找不到，而是不敢找；不是不值 500 元，而是不敢开口要 500 元；不是不知道卖什么，而是不愿意从最小的那个价值开始。</p>
<p>现在只需要一个动作：想清楚自己当前能提供的最小价值。可以是一次咨询，一份整理，一项代办，一个模板，一段陪跑，一次修复，一个小结果。它不必完美，不必系统，也不必等准备好。</p>
<p>先找到第一个人，成交第一单。哪怕是 50 元，哪怕是 100 元，也要先动起来。在行动中迭代，在迭代中涨价，在涨价中扩量。</p>
<p>100 万不是藏在某个神秘方法里，而是在枯燥重复中一单一单等着被取走。差的不是方法，差的往往是第一单。</p>

<h2 id="what-can-be-sold-for-five-hundred">九、什么东西可以卖 500 元</h2>
<p>很多人卡在“我能卖什么”这个问题上，其实可以从三类价值里找答案。第一类是节省时间。别人不会做、不愿做、没时间做的事，你能稳定完成，就有收费空间。整理资料、搭建页面、剪辑短内容、陪同跑流程、配置工具、做基础运营，都属于这一类。</p>
<p>第二类是减少麻烦。很多人不是追求惊艳结果，而是希望少踩坑、少走弯路、少被琐事消耗。你如果能把一个混乱问题变成清单、步骤、模板和结果，就能把混乱转化成服务。</p>
<p>第三类是带来确定改善。比如帮小店把介绍文案改清楚，帮普通人做预算表，帮企业主整理客户线索，帮求职者优化简历和作品集。只要改善足够具体，客户就能理解这 500 元买到的是什么。</p>
<p>一开始不要追求产品宏大，也不要追求体系完整。越早期越应该做窄：只服务一种人，只解决一个问题，只承诺一个可交付结果。窄，才容易找到第一批客户；小，才容易快速迭代。</p>

<h2 id="first-order-action-list">十、第一单行动清单</h2>
<p>第一单不需要复杂计划，只需要一张行动清单。先写下自己能提供的三个最小服务，每个服务用一句话说明结果，而不是说明过程。比如“帮你把 30 条客户反馈整理成一页决策表”，就比“提供咨询服务”更容易被理解。</p>
<p>然后列出 30 个可能需要这个结果的人。先从熟人、同城小商家、过去合作对象、同领域社群和身边正在为这个问题头疼的人开始。不要一上来幻想 2000 个客户，先找到 30 个具体名字。</p>
<p>接着准备一段朴素表达：我能帮你解决什么问题，交付什么东西，需要多久，收费多少。越早期越不要把话术写得太油，真实、具体、敢报价，胜过漂亮包装。</p>
<p>最后做复盘。每沟通 10 个人，就记录三件事：谁有兴趣，谁拒绝，拒绝理由是什么。把拒绝理由改进到下一轮表达里。第一单之后，立刻问客户哪里有价值、哪里不值、能不能介绍一个有类似需求的人。这样才会从一单进入下一单。</p>

<h2 id="earn-before-you-scale">十一、先成交，再谈规模</h2>
<p>很多人还没成交第一单，就开始想品牌、组织、系统、自动化和融资。这些东西不是不重要，但顺序错了就会变成逃避。普通人最先需要的，不是搭建一个看起来很大的生意，而是证明有人愿意为自己提供的价值付钱。</p>
<p>成交之前，所有设想都只是猜测。成交之后，才有真实反馈。十单之后，才看得出客户画像。一百单之后，才谈得上优化流程。两千单之后，能力已经被市场锤炼过一轮。</p>
<p>所以先不要急着变大。先把一件小事做稳，把一个小结果做实，把一个小价格收上来。能收 100 元，就有机会收 500 元；能稳定收 500 元，就有机会卖给 2000 个人。财富不是从幻想里长出来的，而是从第一次敢开口、第一次敢交付、第一次敢复盘里长出来的。</p>
<p>真正的分水岭也在这里。有人每天都在寻找更高级的方法，有人每天都在接触更具体的人。前者越学越复杂，后者越做越清楚。把 500 元价值卖给 2000 个人，表面是在赚钱，本质是在用市场把自己训练成一个能发现需求、解决问题、承担交付的人。</p>
'''

BODY_LESS = r'''
<p>一定要少买不必要的东西。钱变成东西太容易，东西再变成钱却太难。真正的生活不是把房间堆满杂物，而是清空多余，让家里变得干净，让心也跟着安定下来。</p>
<p>少买点，买好点，用久点，才是最划算的生活方式。它不是消费降级，也不是刻意委屈自己，而是把钱、空间和精力从无意义的物品里解救出来。</p>

<h2 id="money-turns-into-things-too-easily">一、钱变成东西太容易，东西变回钱太难</h2>
<p>很多冲动消费都发生在最松懈的时候。半夜睡不着，捧着手机刷直播间，听着限时、低价、最后几件的刺激话术，脑子一热就下了单。快递到了，撕开包装时有一瞬间快感，随后东西就被塞进柜子深处。</p>
<p>打开衣柜，会看到许多连吊牌都没剪，或者只穿过一次就再也没有碰过的衣服。打开抽屉，会看到没用完就过期的护肤品，落满灰尘的小设备，一时兴起买回来却只用过一次的工具。</p>
<p>打折、凑单、满减，经常让人产生“占便宜”的错觉。买的时候觉得以后用得上，反正也不贵，买来玩玩。可这些看似便宜的决定，正在一点点掏空钱包。</p>
<p>钱变成东西的时候很顺滑，只需要一次付款；东西再变成钱的时候却很痛苦。把闲置挂出去，500 元买的裙子穿一次后 50 元都没人问，还可能被继续压价；几千元买的健身器材，最后像废铁一样处理，还要费心找人搬走。</p>
<p>那一刻才会明白，很多以为自己买下的“资产”，其实只是快速贬值的工业垃圾。辛苦赚来的钱，悄悄变成一堆占地方、惹人烦、难处理的东西。</p>

<h2 id="clutter-is-expensive-storage">二、杂物不是免费存在，它占用最贵的空间</h2>
<p>杂物最容易被忽视的成本，是空间成本。城市里的房价和房租都很贵，一平方米可能是一两万元，租房每个月也要大几千。花这么高的居住成本，却用来堆放几年都不会碰一次的东西，本质上是在给杂物租仓库。</p>
<p>一个柜子、一面墙、一个阳台、半间房，看似只是放东西，实际上都对应着居住成本。东西越多，人的活动空间越小；空间越挤，生活越没有舒展感。</p>
<p>更关键的是，杂物不只占空间，还占注意力。只要它在眼前，就会不断提醒人：这里还没整理，那个还没处理，这些钱又浪费了。家不再是恢复能量的地方，而变成一块被未完成事项塞满的压力场。</p>
<p>所以清空杂物不是洁癖，也不是形式主义。它是在把已经被物品占走的居住权，重新还给自己。</p>

<h2 id="visual-noise-drains-energy">三、视觉混乱会榨干精神能量</h2>
<p>东西越多，心越乱。周末好不容易休息一天，看着满屋杂物，扔了舍不得，不扔又乱到没法下脚。于是花大把时间整理、擦灰、收纳，整理完没过几天，又恢复原样。</p>
<p>长期的视觉杂乱，会直接带来焦虑、烦躁和压抑。很多人回到家觉得喘不过气，宁愿在楼下或车里多坐一会，也不想马上进门。不是人懒，而是空间已经被杂物堵住了。</p>
<p>一个杂乱无章的房间，很难让住在里面的人保持平静。所谓环境影响状态，并不是玄学。人每天看到什么、被什么包围、需要处理什么，都会反过来塑造情绪。</p>
<p>真正的整理，不只是把东西摆整齐，而是减少东西本身。收纳只能把问题藏起来，克制购买和主动清理，才是在源头上解决问题。</p>

<h2 id="consumerism-loop">四、消费主义最会利用“反正不贵”的心理</h2>
<p>消费主义最厉害的地方，不是让人买昂贵的大件，而是让人一次次为“反正不贵”付款。9.9 元、29 元、满减差一点、第二件半价，单次看起来都不疼，合在一起却会变成长期漏水的钱包。</p>
<p>“万一以后用得上”也是一个危险念头。很多东西所谓的未来使用场景，只是当下为冲动找的借口。真正需要的东西，不会靠营销话术反复说服你；真正高频使用的东西，买之前往往已经有明确位置和明确用途。</p>
<p>便宜不是问题，盲目才是问题。一个便宜但无用的东西，仍然是浪费；一个贵但长期高频使用的东西，反而可能更划算。</p>
<p>清醒消费的第一步，是承认每一次付款都在投票：你是在购买更好的生活，还是在购买更重的负担。</p>

<h2 id="three-questions-before-buying">五、下单前，先问三个极其现实的问题</h2>
<p>控制购买欲不需要复杂方法。每次想买东西时，先问自己三个问题。</p>
<p>第一，这个东西是真的需要，还是仅仅想要？如果只是想要，把它放进购物车，冷静 48 小时。很多冲动两天后会自然消退，甚至连再看一眼的欲望都没有。</p>
<p>第二，如果买了这个东西，家里有没有合适的地方放？如果没有，坚决不买。没有位置的物品，最终一定会变成新的混乱源。</p>
<p>第三，如果确实需要，能不能买一个质量更好、能用更久的版本？这就是少买点、买好点、用久点。不要再买穿几次就起球变形的廉价衣服，可以攒钱买一件剪裁得体、面料扎实、能穿好几年的经典款。不要再买用两次就坏的小家电，可以买功能基础但质量可靠的产品。</p>
<p>这三个问题会把冲动消费拉回现实：需要、位置、寿命。只要其中任何一项答不上来，这笔钱就应该先留在账户里。</p>

<h2 id="buy-less-buy-better-use-longer">六、少买点、买好点、用久点，生活品质反而上升</h2>
<p>当购买变少，生活品质并不会下降，反而会变得更高。因为身边留下来的每一件物品，都是自己真正喜欢、真正需要、能够长期陪伴的好东西。</p>
<p>衣服少一点，但每一件都合身耐看；家电少一点，但每一件都稳定好用；护肤品少一点，但每一瓶都能用完；工具少一点，但每一个都有明确用途。生活不再被大量低质量物品填满，而是被少量高质量选择支撑。</p>
<p>更重要的是，当不乱花钱，账户余额一点点变多，人的底气会明显不同。那种踏实感，是任何即时消费都给不了的。</p>
<p>钱只有留得住，才是抵御生活风险的底气。钱一旦变成没有意义的杂物，就会从安全感变成负资产。</p>

<h2 id="clear-the-home-clear-the-mind">七、清空家里的多余，也是在清空心里的负担</h2>
<p>找一个周末，拿一个大袋子，把家里一年以上没碰过的东西集中处理。该扔的扔，该捐的捐，该挂二手的挂二手。不要指望一次整理改变人生，但一次认真清理，足以让空间开始恢复呼吸。</p>
<p>当多余的杂物被清出去，家里变得宽敞明亮，阳光不再被遮挡，人会明显觉得呼吸顺畅。空间变轻，心也会跟着变轻。</p>
<p>大道至简，繁华落尽见真纯。真正的生活，从来不是靠堆积物品填补内心空虚，而是清空外在的多余，把精力留给真正重要的人和事。</p>
<p>从今天起，捂紧钱包，停止无意义的买买买。家里没杂物，心就定了；卡里有存款，人就硬气了。这才是普通人最清醒、也最顶级的生活方式。</p>

<h2 id="how-to-clear-without-regret">八、怎样清理，才不会一边扔一边后悔</h2>
<p>清理杂物最难的地方，不是体力，而是舍不得。很多东西明明不用，却总觉得“当初花了钱”“以后可能用得上”“扔了太浪费”。这种舍不得，其实是在用未来的空间和心情，为过去的错误付款。</p>
<p>可以先用三个标准判断。第一，过去一年有没有用过。没有用过，未来高频使用的概率通常很低。第二，如果今天重新选择，还会不会原价买它。如果不会，说明它已经不再代表真实需要。第三，它留下来是在改善生活，还是只是在提醒自己曾经乱花钱。</p>
<p>对仍有使用价值的东西，不必全部扔掉。能送人的送人，能捐出去的捐出去，能挂二手的挂二手。处理方式不重要，重要的是让它离开你的核心生活空间。家不是仓库，柜子也不是后悔的陈列馆。</p>
<p>如果真的拿不准，可以设一个“观察箱”。把犹豫的东西装进去，封箱写日期，放到不显眼的位置。三个月内一次也没想起来，说明它并不重要。到期直接处理，减少反复纠结。</p>

<h2 id="saving-money-is-life-resilience">九、存下来的钱，是普通人的抗风险底气</h2>
<p>少买东西带来的最大变化，不只是房间更整洁，而是账户开始变厚。余额一点点增加，会改变人面对生活的姿态。</p>
<p>没有存款时，任何小意外都会让人心慌。一次生病，一次失业，一次家电损坏，一次临时搬家，都可能把人推入被动。钱留在账户里，未必让人立刻兴奋，却会让人睡得更稳。</p>
<p>消费带来的快感很短，存款带来的底气很长。前者需要不断追加刺激，后者会在关键时刻保护自己。普通人不一定要过苦日子，但一定要分清楚：有些钱花出去是在提升生活，有些钱花出去只是在制造负担。</p>
<p>真正成熟的消费观，不是永远不买，而是每一次购买都能经得起时间检验。买得少，是为了留下钱；买得好，是为了少替换；用得久，是为了让每一笔钱都发挥最大价值。</p>

<h2 id="build-a-new-buying-rule">十、给自己建立一套新的购买规则</h2>
<p>想要长期改变，不能只靠一时热血。最有效的方法，是给自己建立规则。比如非刚需物品必须冷静 48 小时；买一件新衣服，至少处理一件旧衣服；超过某个金额的消费，必须写下购买理由和使用频率；同类物品没有用完之前，不买新的。</p>
<p>规则的目的不是束缚自己，而是保护自己不被情绪牵着走。一个人最容易在疲惫、焦虑、孤独、无聊时乱买东西。这个时候买下的往往不是需要，而是情绪出口。</p>
<p>如果真的想奖励自己，也可以换一种方式。与其买一堆很快失去新鲜感的小东西，不如把钱花在能恢复身体、提升能力、连接重要关系的地方。一次好好休息，一本真正会读完的书，一顿认真做的饭，一次必要的体检，可能比十个无用快递更值得。</p>
<p>当购买规则稳定下来，生活会变得轻。东西少了，整理少了，后悔少了，账户余额多了，内心空间也多了。少买不是失去，而是重新拿回选择权。</p>
<p>真正高级的生活，不是让别人看见自己买了多少，而是自己知道什么可以不要。少一点杂物，少一点冲动，少一点被营销牵走的焦虑，多一点现金，多一点空间，多一点安静。一个人的家越清爽，钱越留得住，心越容易定下来。</p>
<p>从今天开始，不需要立刻变成极简主义者，只要少下一个无意义的单，清掉一件长期不用的物品，留下第一笔原本会被花掉的钱，生活秩序就已经开始往回长。</p>
'''

BODY_HARDSHIP = r'''
<p>要成大事的人，往往先要经历一段干什么都不行、喝口凉水都塞牙的日子。做什么都不顺，走到哪里都像被卡住，很多计划刚开始就碰壁，很多努力还没结果就被否定。</p>
<p>这段日子很难熬，但它并不一定是坏事。正是那些事与愿违的时刻，真正打磨人的心性，锤炼人的意志，也增长人的才干。</p>

<h2 id="hard-days-shape-the-mind">一、干什么都不顺的日子，正在打磨心性</h2>
<p>一个人如果一路顺风顺水，没碰过壁，没摔过跤，没有困顿到极致的体验，未必是好事。太顺了，人容易飘，容易把运气当本事，把平台当实力。</p>
<p>真正的成长，从来不是顺境中轻松得来的。它往往发生在一次次被拒绝、被否定、被打回原形之后，仍然能站稳脚跟，继续往前走的时刻。</p>
<p>顺境会给人信心，逆境会给人骨头。前者让人敢想，后者让人扛事。一个只见过顺风的人，遇到第一场大风就可能慌乱；一个被现实反复锤过的人，反而更知道怎样稳住自己。</p>

<h2 id="do-not-fear-being-stuck">二、不要怕当下的一地鸡毛</h2>
<p>眼前的一地鸡毛，会让人怀疑自己，也会让人觉得所有路都走不通。但很多以后能扛事的底气，正是从这些当下看起来过不去的坎里长出来的。</p>
<p>被拒绝，会让人学会调整表达；被否定，会让人学会检查能力；被打回原形，会让人知道自己真正缺在哪里。痛苦本身没有价值，但痛苦之后还能继续修正，就会产生价值。</p>
<p>所以不必害怕暂时的混乱。那些让人痛苦的日子，可能正在为以后铺路。熬过去之后，它们会变成经验、判断力和韧性。</p>

<h2 id="turn-frustration-into-grounding">三、把卡点熬过去，就会变成扛事的底气</h2>
<p>很多坎在当下看起来像终点，过后回头看，只是训练。那些你以为过不去的卡，一旦熬过去，就会变成以后扛事的底气。</p>
<p>真正厉害的人，不是没有低谷，而是在低谷里没有彻底散掉。他们会难受，会怀疑，会停下来喘口气，但最终还是把自己重新拉回轨道。</p>
<p>这就是逆境的意义。它把虚浮的东西打掉，把幻想打掉，把对运气和环境的依赖打掉，逼人长出更扎实的能力和更稳定的心。</p>

<h2 id="keep-moving-forward">四、站稳脚跟，继续向前</h2>
<p>困顿时最重要的不是立刻翻盘，而是不要彻底停下。能做一点就做一点，能修一处就修一处，能多撑一天就多撑一天。</p>
<p>大事不是在情绪高涨时完成的，而是在反复受挫后仍然继续推进中完成的。每一次继续，都是在告诉自己：我还没有被这一关击垮。</p>
<p>当人能在不顺里稳住，在否定里修正，在失败后继续向前，心性就变硬了，意志就变深了，才干也会慢慢长出来。</p>
<p>那些痛苦的日子不会白过。它们不是人生的废稿，而是以后真正成事之前必须铺好的路。</p>

<h2 id="three-things-to-practice-in-low-point">五、低谷里真正要练的三件事</h2>
<p>第一件事，是练稳定。越不顺，越不能让情绪牵着自己乱跑。稳定不是没有情绪，而是情绪来了也能把基本动作做完。该吃饭就吃饭，该睡觉就睡觉，该复盘就复盘，该继续就继续。</p>
<p>第二件事，是练判断。顺的时候，人很难分清哪些是能力，哪些是运气。只有不顺的时候，才会被迫看清自己的短板。哪里准备不足，哪里表达不清，哪里能力不够，哪里选择太急，都会在挫折里暴露出来。</p>
<p>第三件事，是练耐力。很多路不是走不通，而是还没走到反馈出现的时候就放弃了。能熬过最难看的阶段，才能等到能力、经验和机会重新组合。</p>

<h2 id="do-not-mistake-luck-for-skill">六、不要把运气当本事，也不要把低谷当判决</h2>
<p>顺境里最危险的误判，是把运气当本事；逆境里最危险的误判，是把暂时失败当成最终判决。前者让人轻飘，后者让人自毁。</p>
<p>平台、环境、贵人、时机，都会给人助力。但这些外部因素一旦变化，真正留下来的只有心性、意志和才干。低谷之所以重要，是因为它会把外部光环拿走，让人重新面对自己。</p>
<p>只要还在修正，还在行动，还在把失败变成经验，低谷就不是判决书，而是训练场。被打回原形不可怕，可怕的是被打回原形后不再重建。</p>
<p>成大事的人，未必比别人少受挫，但一定更懂得把受挫变成材料。每一次没被击垮的经历，都会成为下一次站稳的地基。</p>
'''


POSTS = [
    Post(
        slug="first-million-500-yuan-2000-customers",
        title="赚到第一桶 100 万：把 500 元价值卖给 2000 个人",
        desc="把 100 万拆成 500 元乘以 2000 个客户，普通人的赚钱问题就会从空想变成找人、成交、交付和迭代。",
        category="商业思维",
        series="普通人赚钱方法",
        tags=["第一桶金", "副业", "创业", "客户成交", "商业模式", "现金流", "长期主义"],
        minutes=9,
        body=BODY_MONEY,
        accent=("#111827", "#0f766e", "#f59e0b"),
        required=["100 万", "500 元", "2000", "客户", "第一单", "成交", "迭代"],
        minimum=4200,
    ),
    Post(
        slug="buy-less-buy-better-clear-clutter-save-money",
        title="少买点，买好点，用久点：清空杂物后的金钱与生活秩序",
        desc="钱变成东西太容易，东西变回钱太难；少买、买好、用久，是普通人守住钱包和精神能量的生活策略。",
        category="个人财务",
        series="生活方式",
        tags=["断舍离", "消费主义", "存钱", "极简生活", "消费决策", "家庭整理", "生活秩序"],
        minutes=8,
        body=BODY_LESS,
        accent=("#0f172a", "#7c2d12", "#22c55e"),
        required=["少买点", "买好点", "用久点", "杂物", "存款", "48 小时", "消费主义"],
        minimum=3600,
    ),
    Post(
        slug="hardship-before-great-things-shapes-mind",
        title="成大事之前，先熬过干什么都不顺的日子",
        desc="低谷不是人生的废稿，碰壁、被否定和被打回原形，往往是在打磨心性、意志和真正能扛事的底气。",
        category="心理成长",
        series="成长笔记",
        tags=["逆境", "低谷", "成长", "心性", "意志力", "长期主义", "自我修炼"],
        minutes=4,
        body=BODY_HARDSHIP,
        accent=("#1f2937", "#7c3aed", "#06b6d4"),
        required=["成大事", "不顺", "心性", "意志", "低谷", "扛事"],
        minimum=1200,
    ),
]


@dataclass
class RemoteRef:
    commit_sha: str
    tree_sha: str


def run_gh(args: list[str], payload: dict | None = None) -> dict | list | str:
    proc = None
    for attempt in range(3):
        proc = subprocess.run(
            ["gh", "api", *args],
            input=json.dumps(payload, ensure_ascii=False) if payload is not None else None,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode == 0:
            break
        if attempt < 2 and any(token in (proc.stderr + proc.stdout).lower() for token in ["timeout", "timed out", "connection", "reset", "temporarily"]):
            time.sleep(2 + attempt * 3)
            continue
        break
    assert proc is not None
    if proc.returncode != 0:
        raise RuntimeError(f"gh api failed: {' '.join(args)}\n{proc.stderr or proc.stdout}")
    out = proc.stdout.strip()
    if not out:
        return ""
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return out


def endpoint(path: str) -> str:
    return f"repos/{OWNER}/{REPO}/{path}"


def get_ref() -> RemoteRef:
    ref = run_gh([endpoint(f"git/ref/heads/{BRANCH}")])
    commit_sha = ref["object"]["sha"]
    commit = run_gh([endpoint(f"git/commits/{commit_sha}")])
    return RemoteRef(commit_sha=commit_sha, tree_sha=commit["tree"]["sha"])


def get_file(path: str) -> str | None:
    api_path = quote(path, safe="/")
    proc = None
    for attempt in range(3):
        proc = subprocess.run(
            ["gh", "api", endpoint(f"contents/{api_path}?ref={BRANCH}")],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode == 0:
            break
        if "Not Found" in (proc.stderr + proc.stdout):
            return None
        if attempt < 2:
            time.sleep(2 + attempt * 3)
            continue
    assert proc is not None
    if proc.returncode != 0:
        raise RuntimeError(f"gh api get_file failed: {path}\n{proc.stderr or proc.stdout}")
    data = json.loads(proc.stdout)
    return base64.b64decode(data["content"]).decode("utf-8")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def plain_text(html_text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(html_text))


def meta_links(post: Post) -> str:
    cat = f'<a href="/categories/{quote(post.category)}/">{esc(post.category)}</a>'
    tags = "&nbsp;".join(f'<a href="/tags/{quote(tag)}/">{esc(tag)}</a>' for tag in post.tags)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min'


def build_toc(body: str) -> str:
    links = [
        f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>'
        for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    ]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + "".join(links) + "</nav></div></div>"


def cover_svg(post: Post) -> str:
    c1, c2, c3 = post.accent
    title = post.title.replace("：", "：\n", 1)
    lines = title.split("\n")[:2]
    title_svg = "".join(
        f'<text x="92" y="{145 + i * 70}" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="{50 if i == 0 else 42}" font-weight="800">{esc(line)}</text>'
        for i, line in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">{esc(post.title)}</title>
  <desc id="desc">{esc(post.desc)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="0.55" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.28"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.16" stroke="#ffffff" stroke-width="2">
    <path d="M120 655 H1480"/><path d="M120 535 H1480"/><path d="M120 415 H1480"/>
    <path d="M390 260 V750"/><path d="M760 260 V750"/><path d="M1130 260 V750"/>
  </g>
  <g filter="url(#shadow)">
    <path d="M170 650 C340 560 510 590 680 455 C860 312 1030 398 1210 270 C1325 188 1422 158 1500 120" fill="none" stroke="#f8fafc" stroke-width="13" stroke-linecap="round" opacity="0.86"/>
    <circle cx="680" cy="455" r="34" fill="#ffffff" opacity="0.92"/><circle cx="1210" cy="270" r="44" fill="#f8fafc" opacity="0.96"/>
    <rect x="94" y="585" width="520" height="132" rx="26" fill="#ffffff" opacity="0.92"/>
    <text x="132" y="660" fill="#0f172a" font-family="Noto Sans SC, PingFang SC, Arial" font-size="38" font-weight="800">{esc(post.category)} · {esc(post.series)}</text>
    <text x="132" y="700" fill="{c2}" font-family="Noto Sans SC, PingFang SC, Arial" font-size="25" font-weight="700">{esc(str(post.minutes))} min 深度梳理</text>
  </g>
  {title_svg}
  <text x="96" y="322" fill="#e5e7eb" font-family="Noto Sans SC, PingFang SC, Arial" font-size="30" font-weight="700">{esc(post.desc[:54])}</text>
</svg>'''


def article_nav(post: Post, index: int) -> str:
    if index == 0:
        newer = '<a class="newer-posts">下一篇<br>没有更新的文章</a>'
    else:
        newer_post = POSTS[index - 1]
        newer = f'<a class="newer-posts" href="{newer_post.url_path}">下一篇<br>{esc(newer_post.title)}</a>'
    if index + 1 < len(POSTS):
        older_post = POSTS[index + 1]
        older = f'<a class="older-posts" href="{older_post.url_path}">上一篇<br>{esc(older_post.title)}</a>'
    else:
        older = f'<a class="older-posts" href="{PREV_EXISTING_URL}">上一篇<br>{esc(PREV_EXISTING_TITLE)}</a>'
    return newer + older


def build_article_page(post: Post, body: str, template: str, index: int) -> str:
    start = template.find('<article class="post">')
    end = template.find("</article>", start) + len("</article>")
    if start == -1 or end == -1:
        raise RuntimeError("article template not found")
    head, tail = template[:start], template[end:]
    replacements = {
        r"<title>.*?</title>": f"<title>{esc(post.title)} - zcxGGmu's Blog</title>",
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(post.desc)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(post.full_url)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(post.title)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(post.desc)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(post.full_url)}">',
    }
    for pattern, replacement in replacements.items():
        head = re.sub(pattern, replacement, head, count=1, flags=re.S)
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('/images/posts/{post.slug}/cover.svg')"><div class="post-title">{esc(post.title)}<div class="post-subtitle">{esc(post.desc)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links(post)}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{body}</div></div><nav class="post-pagination">{article_nav(post, index)}</nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(body), tail, count=1, flags=re.S)
    return head + article + tail


def update_previous_article(text: str) -> str:
    last_post = POSTS[-1]
    return re.sub(
        r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>',
        f'<a class="newer-posts" href="{last_post.url_path}">下一篇<br>{esc(last_post.title)}</a>',
        text,
        count=1,
        flags=re.S,
    )


def home_card(post: Post) -> str:
    return f'''<a href="{post.url_path}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(post.title)}</div>
            <div class="post-item-summary">{esc(post.desc)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('/images/posts/{post.slug}/cover.svg')"></div></div>
        </div>
      </div>
    </a>'''


def strip_home_card(text: str, url_path: str) -> str:
    return re.sub(rf'<a href="{re.escape(url_path)}" class="a-block">.*?</a>\s*', "", text, flags=re.S)


def update_home(text: str) -> str:
    for post in POSTS:
        text = strip_home_card(text, post.url_path)
    pos = text.find(f'<a href="{PREV_EXISTING_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError("homepage insertion marker not found")
    block = "\n".join(home_card(post) for post in POSTS) + "\n"
    return text[:pos] + block + text[pos:]


def pub_date(index: int) -> datetime:
    return BASE_DT - timedelta(minutes=index)


def update_rss(text: str) -> str:
    text = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{format_datetime(BASE_DT)}</lastBuildDate>", text, count=1)
    for post in POSTS:
        text = re.sub(rf"<item>\s*<title>{re.escape(esc(post.title))}</title>.*?</item>\s*", "", text, flags=re.S)
    block = "".join(
        f'''<item>
<title>{esc(post.title)}</title>
<link>{post.full_url}</link>
<guid>{post.full_url}</guid>
<pubDate>{format_datetime(pub_date(i))}</pubDate>
<description>{esc(post.desc)}</description>
</item>
'''
        for i, post in enumerate(POSTS)
    )
    return text.replace("<item>", block + "<item>", 1)


def update_sitemap(text: str) -> str:
    for post in POSTS:
        text = re.sub(rf"\s*<url><loc>{re.escape(post.full_url)}</loc></url>", "", text)
    block = "".join(f"  <url><loc>{post.full_url}</loc></url>\n" for post in POSTS)
    return text.replace("</urlset>", block + "</urlset>")


def archive_item(post: Post) -> str:
    return f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{post.url_path}">{esc(post.title)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(post.category)}</span></span>
      </div> '''


def remove_archive_item(text: str, post: Post) -> str:
    return re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(post.url_path)}">.*?</div>\s*', "", text, flags=re.S)


def update_archive(text: str) -> str:
    original = text
    for post in POSTS:
        text = remove_archive_item(text, post)
    delta = sum(1 for post in POSTS if post.url_path not in original)
    if delta:
        text = re.sub(
            r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>',
            lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + delta} 篇</span>',
            text,
            count=1,
        )
    pos = text.find(f'<a href="{PREV_EXISTING_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    if start == -1:
        raise RuntimeError("archive insertion marker not found")
    block = "".join(archive_item(post) for post in POSTS)
    return text[:start] + block + text[start:]


def tax_item(post: Post) -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{post.url_path}" style="font-size:16px;text-decoration:none">{esc(post.title)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''


def remove_tax_item(text: str, post: Post) -> str:
    return re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(post.url_path)}".*?</div>\s*', "", text, flags=re.S)


def new_term_page(kind: str, term: str, posts: list[Post]) -> str:
    prefix = "分类" if kind == "categories" else "标签" if kind == "tags" else "系列"
    label = f"{prefix}: {term}"
    items = "".join(tax_item(post) for post in posts)
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(term)}</h1><p style="color:#999;margin-bottom:30px">共 {len(posts)} 篇文章</p>{items}</div></div></div><script src="/js/journal.js"></script></body></html>'''


def update_term_page(text: str | None, kind: str, term: str, posts: list[Post]) -> tuple[str, int]:
    if text is None:
        return new_term_page(kind, term, posts), len(posts)
    original = text
    for post in posts:
        text = remove_tax_item(text, post)
    delta = sum(1 for post in posts if post.url_path not in original)
    if delta:
        text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + delta} 篇文章", text, count=1)
    marker = '<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">'
    first = text.find(marker)
    if first == -1:
        first = text.find("</div></div></div>")
    if first == -1:
        raise RuntimeError(f"term page insertion point not found: {kind}/{term}")
    block = "".join(tax_item(post) for post in posts)
    return text[:first] + block + text[first:], delta


def update_term_index(text: str, kind: str, term: str, delta: int) -> str:
    if delta == 0:
        return text
    hrefs = [f"/{kind}/{quote(term)}/", f"/{kind}/{term}/"]
    for href in hrefs:
        pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span[^>]*>\()(\d+)(\)</span></a>)')
        text, count = pattern.subn(lambda m: f"{m.group(1)}{int(m.group(2)) + delta}{m.group(3)}", text, count=1)
        if count:
            return text
    href = f"/{kind}/{quote(term)}/"
    if kind == "tags":
        item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">({delta})</span></a>\n'
    else:
        item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">({delta})</span></a>\n'
    pos = text.find("</div></div></div><script")
    if pos == -1:
        pos = text.find("</div></div></div>")
    if pos == -1:
        raise RuntimeError(f"term index insertion point not found for {kind}/{term}")
    return text[:pos] + item + text[pos:]


def collect_term_posts() -> dict[tuple[str, str], list[Post]]:
    mapping: dict[tuple[str, str], list[Post]] = {}
    for post in POSTS:
        for kind, term in [("categories", post.category), ("series", post.series), *[("tags", tag) for tag in post.tags]]:
            mapping.setdefault((kind, term), []).append(post)
    return mapping


def body_file_name(post: Post) -> str:
    return f"{post.slug}-body.html"


def collect_outputs() -> dict[str, str]:
    outputs: dict[str, str] = {}
    template = get_file(PREV_EXISTING_URL.strip("/") + "/index.html")
    if template is None:
        raise RuntimeError("article template missing")

    for i, post in enumerate(POSTS):
        body = post.body.strip() + "\n"
        outputs[f"2026/{post.slug}/index.html"] = build_article_page(post, body, template, i)
        outputs[f"images/posts/{post.slug}/cover.svg"] = cover_svg(post)
        outputs[f"tasks/{body_file_name(post)}"] = body

    outputs[f"tasks/{SCRIPT_NAME}"] = Path(__file__).read_text(encoding="utf-8")

    current_home = get_file("index.html")
    current_rss = get_file("index.xml")
    current_archive = get_file("archive/index.html")
    current_sitemap = get_file("sitemap.xml") or '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n'
    previous = get_file(PREV_EXISTING_URL.strip("/") + "/index.html")
    if None in (current_home, current_rss, current_archive, previous):
        raise RuntimeError("required remote files missing")
    outputs["index.html"] = update_home(current_home)
    outputs["index.xml"] = update_rss(current_rss)
    outputs["archive/index.html"] = update_archive(current_archive)
    outputs["sitemap.xml"] = update_sitemap(current_sitemap)
    outputs[PREV_EXISTING_URL.strip("/") + "/index.html"] = update_previous_article(previous)

    index_cache: dict[str, str] = {}
    for (kind, term), posts in collect_term_posts().items():
        term_path = f"{kind}/{term}/index.html"
        term_source = outputs.get(term_path) or get_file(term_path)
        term_page, delta = update_term_page(term_source, kind, term, posts)
        outputs[term_path] = term_page
        index_path = f"{kind}/index.html"
        index_text = index_cache.get(index_path) or outputs.get(index_path) or get_file(index_path)
        if index_text is None:
            raise RuntimeError(f"{index_path} missing")
        index_cache[index_path] = update_term_index(index_text, kind, term, delta)
    outputs.update(index_cache)

    manifest_files = sorted(outputs.keys() | {f"tasks/{MANIFEST_NAME}"})
    outputs[f"tasks/{MANIFEST_NAME}"] = json.dumps(manifest_files, ensure_ascii=False, indent=2)
    return outputs


def validate(outputs: dict[str, str]) -> None:
    failures: list[str] = []
    for post in POSTS:
        article = outputs[f"2026/{post.slug}/index.html"]
        cover = outputs[f"images/posts/{post.slug}/cover.svg"]
        body_match = re.search(r'<div class="post-body" v-pre>(.*?)</div></div><nav', article, re.S)
        body_html = body_match.group(1) if body_match else ""
        plain = plain_text(body_html)
        if len(plain) < post.minimum:
            failures.append(f"{post.slug}: body too short: {len(plain)}")
        for word in FORBIDDEN:
            if word in article or word in cover:
                failures.append(f"{post.slug}: forbidden/source wording present: {word}")
        for term in post.required:
            if term not in article:
                failures.append(f"{post.slug}: missing required topic: {term}")
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != links or len(h2) < 4:
            failures.append(f"{post.slug}: toc mismatch or too few h2: h2={len(h2)} links={len(links)}")
        ET.fromstring(cover)

    ET.fromstring(outputs["index.xml"])
    home_cards: list[str] = []
    for match in re.finditer(r'<a href="([^"]+)" class="a-block">', outputs["index.html"]):
        href = match.group(1)
        if href not in home_cards:
            home_cards.append(href)
    expected_prefix = PINNED_PREFIX + [post.url_path for post in POSTS] + [PREV_EXISTING_URL]
    if home_cards[: len(expected_prefix)] != expected_prefix:
        failures.append(f"homepage order mismatch: {home_cards[:len(expected_prefix)]}")
    rss_links = re.findall(r"<link>(https://zcxggmu.github.io/2026/[^<]+/)</link>", outputs["index.xml"])
    if rss_links[: len(POSTS)] != [post.full_url for post in POSTS]:
        failures.append(f"rss order mismatch: {rss_links[:len(POSTS)]}")
    for post in POSTS:
        if post.url_path not in outputs["archive/index.html"]:
            failures.append(f"archive missing {post.slug}")
        if post.full_url not in outputs["sitemap.xml"]:
            failures.append(f"sitemap missing {post.slug}")
        for kind, term in [("categories", post.category), ("series", post.series), *[("tags", tag) for tag in post.tags]]:
            term_path = f"{kind}/{term}/index.html"
            if post.url_path not in outputs[term_path]:
                failures.append(f"{term_path} missing {post.slug}")
            if term not in outputs[f"{kind}/index.html"]:
                failures.append(f"{kind}/index.html missing {term}")
    previous = outputs[PREV_EXISTING_URL.strip("/") + "/index.html"]
    if POSTS[-1].url_path not in previous:
        failures.append("previous article newer link missing")
    for i, post in enumerate(POSTS):
        article = outputs[f"2026/{post.slug}/index.html"]
        if i and POSTS[i - 1].url_path not in article:
            failures.append(f"{post.slug}: newer link missing")
        if i + 1 < len(POSTS) and POSTS[i + 1].url_path not in article:
            failures.append(f"{post.slug}: older link missing")
        if i + 1 == len(POSTS) and PREV_EXISTING_URL not in article:
            failures.append(f"{post.slug}: previous older link missing")
    if failures:
        raise SystemExit("\n".join(failures))


def write_outputs(outputs: dict[str, str]) -> None:
    out_dir = Path("/tmp/three-life-business-articles-20260809-publish-output")
    if out_dir.exists():
        subprocess.run(["rm", "-rf", str(out_dir)], check=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in outputs.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(json.dumps({"local_output": str(out_dir), "files": len(outputs), "urls": [post.full_url for post in POSTS]}, ensure_ascii=False, indent=2))


def create_commit(outputs: dict[str, str], ref: RemoteRef) -> str:
    tree_entries = []
    for path, content in sorted(outputs.items()):
        blob = run_gh(["-X", "POST", endpoint("git/blobs"), "--input", "-"], {"content": content, "encoding": "utf-8"})
        tree_entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = run_gh(["-X", "POST", endpoint("git/trees"), "--input", "-"], {"base_tree": ref.tree_sha, "tree": tree_entries})
    commit = run_gh(
        ["-X", "POST", endpoint("git/commits"), "--input", "-"],
        {"message": "Publish three life and business articles", "tree": tree["sha"], "parents": [ref.commit_sha]},
    )
    run_gh(["-X", "PATCH", endpoint(f"git/refs/heads/{BRANCH}"), "--input", "-"], {"sha": commit["sha"], "force": False})
    return commit["sha"]


def main() -> None:
    ref = get_ref()
    outputs = collect_outputs()
    validate(outputs)
    write_outputs(outputs)
    commit_sha = create_commit(outputs, ref)
    print(json.dumps({"parent": ref.commit_sha, "pushed": commit_sha, "urls": [post.full_url for post in POSTS]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
