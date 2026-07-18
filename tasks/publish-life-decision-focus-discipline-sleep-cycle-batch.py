# -*- coding: utf-8 -*-
from __future__ import annotations
import html, json, re, xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote
ROOT=Path('/tmp/hermes-video-publish')
SITE='https://zcxggmu.github.io'
DATE='2026-07-19'
PINNED=['/2026/codeinsights-local-first-agent-workbench/','/2026/what-you-need-to-learn-from-claw-code-repo/','/2026/gaojingqi-investment-system/','/2026/ai-revolution-permanent-underclass-career-selection/','/2026/live-longer-than-earn-fast-investment-infinite-game/']
PREV_ORIGINAL_URL='/2026/aluminum-cycle-capacity-ceiling-yunlv-shenhuo-hongqiao/'
PREV_ORIGINAL_TITLE='电解铝周期正在变形：产能天花板、绿电成本与三家公司的盈利分化'
POSTS=[
  {
    "slug": "decide-big-things-four-step-framework",
    "title": "怎样决定人生大事：在不确定中下注，而不是在拖延中耗尽一生",
    "desc": "重大选择从来不是等到信息完美才行动，而是在迷雾中看清场景、把握时机、审视假设、持续修正。真正改变命运的，不是一次稳稳赢的选择，而是一套可执行、可复盘、可迭代的决策机制。",
    "category": "认知方法",
    "series": "人生决策",
    "tags": [
      "人生决策",
      "怎样决定大事",
      "不确定性",
      "四步法则",
      "拖延",
      "风险管理",
      "自我修正",
      "重大选择"
    ],
    "minutes": 12,
    "cover_sub": "看清场景 · 把握时机 · 审视假设 · 随时修正",
    "cover_note": "在七分把握时行动，剩下三分交给反馈",
    "article": "\n<h2 id=\"decision-not-result\">好的决策，不等于幸运的结果</h2>\n<p>人生里真正改变轨迹的选择，往往只占全部日常事件的 1%。是否换城市、换职业、买房、结婚、离婚、创业、接受某个机会，表面上只是一个节点，实际上会重写之后很多年的生活结构。问题在于，这些选择几乎从不发生在信息完美、风险可控、内心笃定的时候。</p>\n<p>很多人把决策理解成“想清楚再行动”。于是站在人生十字路口时，一边想走向未知的风暴，一边又舍不得熟悉的平庸；一边知道继续拖延会让路越走越窄，一边又告诉自己再等等、再准备准备。结果三年五年过去，所谓谨慎变成了逃避，所谓等待变成了人生机会的流失。</p>\n<p>必须先拆掉一个误区：好决策不等于好结果。股票涨了，不代表当初的判断一定高明；换工作后收入翻倍，不代表方法论就无懈可击；选择失败，也不意味着当时一定愚蠢。结果里有运气、环境、时代和随机性。真正能评估的，是做决定那一刻是否用了尽可能可靠的框架，把可控变量控制住，把干扰排除掉，把内心噪音降到最低。</p>\n<h2 id=\"four-step-model\">四步法则：把窒息的大事拆成可执行动作</h2>\n<p>重大决策之所以让人窒息，是因为它看起来像一个巨大的黑箱：选错了怎么办，别人怎么看，未来会不会后悔，最坏会不会发生。四步法则的价值，是把这个黑箱拆成四个可执行动作：看清场景、把握时机、审视假设、随时修正。</p>\n<p>看清场景，是先搞清楚现在到底发生了什么，而不是急着解释和脑补。把握时机，是承认完美时机不存在，在足够好的窗口期行动。审视假设，是把那些“我以为”“大家都说”“过去一直如此”的前提逐条拿出来检查。随时修正，是把决策看成动态循环，而不是一锤定音。</p>\n<p>这套方法不保证每次都赢，但能让人在混沌中建立秩序，在未知中锚定方向。它的重点不是让人变得绝对正确，而是让人不再被恐惧、拖延和自欺牵着走。</p>\n<h2 id=\"see-scene\">第一步：看清场景，把“我觉得”拉回“我看到”</h2>\n<p>很多重大选择之所以失控，是因为问题还没定义清楚，情绪已经先接管了大脑。比如一段关系走到临界点，脑子里全是“他是不是不爱我了”“孩子怎么办”“别人会怎么看”。这些当然重要，但它们不是事实本身，而是解释、恐惧和社会压力。</p>\n<p>事实是什么？是过去一个月争吵了几次，是财务账目是否清晰，是双方是否还有沟通意愿，是核心矛盾有没有被反复回避。职业选择也是一样。真正的事实不是“我怕失败”，而是行业增长是否还在、自己的技能是否匹配、现金流能撑多久、最坏情况下能否退回。</p>\n<p>看清场景需要一种情境意识：从“我觉得”退回“我看到”。把模糊焦虑写成具体风险，把脑内悲剧写成可核对清单。所谓“可怕叙事”不是为了吓自己，而是把最坏剧本摆到桌面上：如果失败，会失去什么？会痛苦多久？是否真的无法承受？很多恐惧一旦被具体化，威慑力反而下降。</p>\n<h2 id=\"timing-window\">第二步：把握时机，等待本身也是风险</h2>\n<p>人最容易迷恋完美时机。想转行的人说等考完证，想创业的人说等经济回暖，想表达心意的人说等对方心情更好。可现实是，证书永远考不完，经济永远有波动，别人的心情永远无法完全预测。</p>\n<p>真正的决策者不追求“最好时间点”，只寻找“足够好的窗口期”。当信息已经多到继续收集只会带来拖延，风险已经低到再低就是幻想，行动成本已经低于继续等待的代价，就必须动手。七分把握时就要进入行动，剩下三分交给反馈和修正。</p>\n<p>拖延最危险的地方，是它常常伪装成理性。反复权衡看似负责，其实可能只是内耗；无限等待看似谨慎，其实可能是对失败的恐惧。时机不是等出来的，而是在行动中被验证出来的。</p>\n<h2 id=\"test-assumptions\">第三步：审视假设，别让旧地图绑架新人生</h2>\n<p>绝大多数决策失败，不是因为信息太少，而是因为假设错了。换工作一定涨薪，结婚一定幸福，买房一定保值，出国一定轻松，稳定一定安全，这些前提像空气一样存在，却很少被认真质疑。</p>\n<p>审视假设的做法很简单：把所有前提写下来，然后逐条问自己，如果它错了怎么办？如果新工作没有预期收入，自己能承受多久？如果国外生活更卷，孩子不适应，语言过不了关，还要不要继续？如果所谓稳定行业正在衰退，继续留下到底是安全还是慢性风险？</p>\n<p>更深层的假设往往藏在身份认同里：我必须成功，我不能让父母失望，我是个稳重的人，我不能冒险。它们看起来像价值观，实际上可能是别人塞进脑子里的过时程序。只有把这些隐性前提挖出来，人才有可能做出属于自己的选择。</p>\n<h2 id=\"revise-loop\">第四步：随时修正，决策是起点，不是终点</h2>\n<p>传统观念常把坚持看得太重，好像一旦改变方向就是半途而废。可真实世界不是线性剧本。做出决定只是上路，后面还会遇到新信息、新风险、新机会。死守原计划，有时不是坚定，而是拒绝学习。</p>\n<p>更成熟的做法，是定期复盘：当初的假设还成立吗？场景是否变化？行动是否有效？如果出现偏差，马上调整。修正不是失败，而是系统升级。真正的高手不是从不犯错，而是犯错后能最快调整、最小损失、最大学习。</p>\n<p>这也是重大决策最容易被忽略的一点。签了合同，不代表不再观察市场；进入婚姻，不代表不再经营关系；入职一家公司，不代表不再学习新技能。环境会变，人也必须变。</p>\n<h2 id=\"emotion-data\">恐惧、拖延和逃避，都是数据源</h2>\n<p>面对大事时，恐惧不是弱点，而是风险提醒；拖延不一定只是懒，也可能说明准备不足；逃避有时说明某个选择违背了核心价值。关键不是压抑这些情绪，而是把它们纳入决策框架。</p>\n<p>当感到害怕时，不要只说“我不敢”，而要追问：我具体怕什么？发生概率有多大？我能做什么降低它？当总想拖延时，也要追问：是信息不够，能力不够，还是我只是不愿面对结果？情绪一旦被拆解，就从阻碍变成了数据。</p>\n<p>还可以给重大选择设置决策截止时间。不是无限期思考，而是规定某个时间点前必须基于现有分析推进。决策质量不取决于思考时长，而取决于思考密度。十分钟高强度聚焦，胜过十天漫无目的纠结。</p>\n<h2 id=\"advisory-circle\">重大决定，不要关起门独自煎熬</h2>\n<p>高风险领域没有真正的孤胆英雄。指挥官依赖团队，医生依赖检查和会诊，救援者依赖实时反馈。普通人做大决定时，却常常关起门苦思冥想，生怕暴露自己的犹豫。</p>\n<p>更好的方式，是为自己组建一个小型决策顾问团。它不需要正式，可以是几个信任的朋友、行业前辈、专业人士，甚至是与自己立场不同的人。把场景分析、时机判断、假设清单和修正计划摊开，让他们挑盲点、补信息、质疑脆弱前提。</p>\n<p>别人的意见不是圣旨，最终拍板仍然是自己。但外部视角能把人从自我循环里拉出来。很多时候，一个尖锐问题就足以刺破思维死角。</p>\n<h2 id=\"life-compass\">所谓大事，是会改变人生轨迹的选择</h2>\n<p>大事不一定外在规模巨大。选择伴侣、教育孩子、换职业、处理健康、管理资产、决定是否离开一段关系，甚至每天如何安排时间，都可能塑造未来的自己。衡量大事的标准，不是事件看起来多宏大，而是它对人生轨迹的影响力。</p>\n<p>掌握四步法则，不是为了把生活变成军事演习，而是为了让每一步更有底气、更少遗憾。面对不确定性，真正可依靠的不是一次完美预测，而是一套可迭代、可修正、可执行的决策机制。</p>\n<p>人不可能避免所有错误，也不可能提前知道未来。但可以做到：少一点慌乱，多一点清醒；少一点幻想，多一点行动；少一点拖延，多一点复盘。命运的很多转折，就藏在这种看似朴素的行动纪律里。</p>\n"
  },
  {
    "slug": "focus-on-your-life-mainline",
    "title": "永远只专注于自己：95% 的事与你的人生主线无关",
    "desc": "注意力是最重要的复利资本。真正改变命运的，不是更忙、更热闹、更会回应别人，而是把时间持续投向那 5% 能形成复利的主线任务。",
    "category": "认知方法",
    "series": "人生主线",
    "tags": [
      "人生主线",
      "注意力",
      "纳瓦尔",
      "复利",
      "专注",
      "深度工作",
      "信息过滤",
      "情绪管理"
    ],
    "minutes": 7,
    "cover_sub": "注意力 · 复利 · 人生主线",
    "cover_note": "你聚焦什么，最终就会成为什么",
    "article": "\n<h2 id=\"mainline\">人生真正重要的，通常只占 5%</h2>\n<p>生活里绝大多数事情，其实与人生主线无关。这句话听起来刺耳，却非常真实。每天醒来之后，消息、会议、聊天、热搜、短视频、争论、临时请求，会把人的注意力撕成碎片。忙了一整天，回头一看，真正推动自己前进的事情几乎没有做几件。</p>\n<p>很多人不是不努力，而是努力被分散到太多方向。看起来很忙，实际上是在为那 95% 的噪音消耗精力；真正能改变命运的 5%，比如核心能力、长期作品、健康、深度关系、关键资产，却长期得不到稳定投入。</p>\n<p>人生主线不是一句口号，而是一个残酷筛选：什么事情值得长期投入，什么事情只是热闹，什么事情会把你带向复利，什么事情只是在消耗生命。</p>\n<h2 id=\"attention-capital\">注意力是最重要的复利资本</h2>\n<p>很多人谈复利，只想到金钱投资。其实注意力也是复利资本。时间和精力持续投入真正重要的方向，会像滚雪球一样积累能力、作品、信誉和机会。反过来，如果注意力每天被无意义的信息切碎，损失的不只是当天几个小时，而是未来所有可能叠加的复利周期。</p>\n<p>人生像种树。今天浇水的是树苗，几年后收获的是果实。如果每天东挖一铲、西栽一棵，最后什么都长不出来。真正可怕的不是不够勤奋，而是勤奋从来没有压在同一条主线上。</p>\n<p>很多人的问题，就是把最宝贵的生产线租给了别人。别人发来消息，别人制造热点，别人拉你争论，别人让你情绪波动。你忙得团团转，却没有制造出任何属于自己的产品。</p>\n<h2 id=\"noise-life\">忙碌不等于成果，回应世界不等于经营人生</h2>\n<p>一个典型的陷阱是：谁的消息都秒回，谁的忙都不好意思拒绝，什么热点都跟，什么争论都参与。这样的人看起来负责、热情、忙碌，但一年过去，工资没有明显增长，技能没有显著提升，作品没有积累，核心竞争力几乎原地踏步。</p>\n<p>问题不在于他不努力，而在于他把人生主线让位给了噪音。别人安排给你的，通常不是最重要的，而是最喧闹的。如果不主动筛选，世界会替你安排日程；如果不主动拒绝，人生会被一堆不属于你的优先级填满。</p>\n<p>所以，主线人生的第一步不是更努力，而是夺回注意力所有权。</p>\n<h2 id=\"filters\">建立免疫系统：信息、社交、情绪三重过滤</h2>\n<p>如果注意力是资本，筛选能力就是守住资本的护城河。第一层过滤是信息过滤。那些只会让人焦虑、愤怒、分心、看热闹的账号和推送，表面上是在提供信息，实际上是在劫持节奏。高效的人往往不是知道最多的人，而是能拒绝最多无效信息的人。</p>\n<p>第二层过滤是社交过滤。一个人最容易被身边最常接触的人影响。无效社交不只是浪费时间，更是情感内耗。如果某段关系只带来索取、比较、控制、抱怨和消耗，就要重新评估它在生命中的位置。真正值得维护的关系，是彼此成就、彼此尊重，而不是单向消耗。</p>\n<p>第三层过滤是情绪过滤。很多人不是败给能力，而是败给愤怒、委屈、不甘和抱怨。每当陷入情绪旋涡时，最好立刻问自己：这件事能帮我完成主线吗？如果不能，它大概率不值得继续沉浸。愤怒像手里的热煤，想扔向别人，往往先烫伤自己。</p>\n<h2 id=\"specific-knowledge\">把 5% 的精力押在特定知识上</h2>\n<p>人生主线的核心，是找到并深耕自己的特定知识。特定知识不是标准化培训能直接教出来的，而是来自个人天赋、兴趣、长期积累和真实反馈。</p>\n<p>有些人擅长表达，有些人擅长解决复杂问题，有些人擅长整合资源，有些人对数字、结构、人心、审美或系统特别敏感。真正重要的是找到那个别人难以替代，而自己又愿意长期投入的方向。</p>\n<p>深耕不是机械重复，而是持续迭代。做、反馈、修正、再做。时间久了，普通执行者会变成某个领域里有壁垒的人。一旦拥有特定知识，就不再只是在红海里拼体力，而是在更广阔的空间里创造不可替代的价值。</p>\n<h2 id=\"not-to-do-list\">先定义不做什么，再定义要做什么</h2>\n<p>很多人喜欢写目标清单，却很少写“不做清单”。但对主线人生来说，不做什么往往更重要。无意义刷手机、随叫随到式社交、情绪化争论、低质量信息摄入、无目的比较，都应该被明确写进不做清单。</p>\n<p>反向思维的价值就在这里：先排除错误答案，往往比盲目寻找正确答案更有效。一个人不可能什么都要，也不可能什么都做。越早承认精力有限，越能把最好的时间留给真正重要的事。</p>\n<p>拒绝不是冷漠，而是对人生主线负责。</p>\n<h2 id=\"environment\">用环境设计替代意志力硬撑</h2>\n<p>意志力是有限的，环境设计却能替人节省大量意志力。每天固定两到三小时深度工作，手机飞行模式，关闭弹窗和通知，物理隔绝干扰，减少低质量社交，把容易让人分心的入口提前堵住。</p>\n<p>不要高估自己对诱惑的抵抗力。真正高效的人，不是每天都靠意志力打胜仗，而是把战场设计成更容易胜利的样子。环境越干净，注意力越集中；注意力越集中，复利越容易发生。</p>\n<h2 id=\"review\">长期复盘：每天校准，每季度纠偏</h2>\n<p>主线不是一次定义完就永远不变。每天睡前可以花五分钟问自己：今天的时间有没有花在主线上？有没有被无关事务切走？哪些习惯需要马上调整？每个季度再做一次系统校准：核心能力是否增强，人生方向是否偏离，投入是否正在形成复利。</p>\n<p>真正的满足感，不是来自外界掌声，而是来自自己确实走在那条 5% 的主线上。人一旦知道自己的注意力正在投向未来，就会少很多无意义的焦虑。</p>\n<h2 id=\"become\">你聚焦什么，最终就会成为什么</h2>\n<p>人不是被一天决定的，而是被长期注意力塑造的。你反复关注抱怨，就会成为抱怨的一部分；你反复关注能力，就会长出能力；你反复关注作品，就会留下作品；你反复关注主线，就会逐渐变成自己想成为的人。</p>\n<p>从今天开始，真正值得做的不是让生活更热闹，而是让注意力更干净。把最宝贵的资产投资给自己，投资给能产生复利的事情。远离无关干扰，守住核心任务，时间会把这种专注变成命运的差距。</p>\n"
  },
  {
    "slug": "road-less-traveled-discipline-love-maturity",
    "title": "少有人走的路：自律、爱与心智成熟，为什么人生苦难重重仍要向前",
    "desc": "人生不是本该轻松顺利，而是一连串必须面对的问题。真正的自律，是主动承受痛苦并解决问题；真正的爱，是促进自己和他人心智成熟的行动。",
    "category": "读书笔记",
    "series": "心智成熟",
    "tags": [
      "少有人走的路",
      "自律",
      "心智成熟",
      "推迟满足",
      "承担责任",
      "尊重事实",
      "爱",
      "心理成长"
    ],
    "minutes": 13,
    "cover_sub": "自律 · 爱 · 成熟",
    "cover_note": "拒绝成熟，就是拒绝解决问题",
    "article": "\n<h2 id=\"life-is-hard\">人生苦难重重：承认它，才可能超越它</h2>\n<p>“人生苦难重重”之所以重要，不是因为它悲观，而是因为它真实。大多数痛苦来自一个错误期待：人生本该舒适顺利，麻烦只是偶然，困难是不公平的命运安排。于是人一遇到问题，就怨天尤人，觉得自己不该承受这些。</p>\n<p>可人生本来就是一连串难题。面对问题时，真正的分水岭不在于痛苦是否出现，而在于人是束手无策地哀叹，还是积极主动地解决。解决人生问题的首要工具，叫自律。</p>\n<p>这里的自律，不是每天几点起床，也不是机械打卡。真正的自律，是主动要求自己以积极态度承受痛苦、解决问题。缺少自律，任何麻烦都会被拖延、逃避和扭曲放大；局部自律只能解决局部问题，完整自律才可能支撑完整人生。</p>\n<h2 id=\"delayed-gratification\">推迟满足：先吃苦，后享受更大的快乐</h2>\n<p>自律的第一个原则，是推迟满足感。它的本质，是重新安排快乐与痛苦的顺序。先面对麻烦，先处理困难，先做最棘手的事，然后再享受更大的轻松。</p>\n<p>拖延的人通常把顺序反过来：先做简单的事，先享受短暂快乐，把痛苦推到后面。问题不会因为被推迟而消失，只会越积越重，最终压垮自己。真正成熟的生活方式，是在一天开始时先处理最难的任务，把痛苦主动领走。</p>\n<p>推迟满足并不是天生能力，它常常来自童年时期稳定的爱。被认真陪伴、被理解需求、被教会“辛苦之后会有甜”的孩子，更容易相信未来值得等待。相反，从小被忽视和遗弃的人，可能觉得未来遥远而渺茫，于是更倾向于透支当下快乐。</p>\n<h2 id=\"responsibility\">承担责任：逃避责任，就是放弃自由</h2>\n<p>自律的第二个原则，是承担责任。很多人遇到问题时，第一反应是“这不是我的问题”。环境不好、别人不配合、条件不允许、命运不公平，都可以成为逃避的理由。</p>\n<p>但只要问题发生在自己的生活里，就必须先问：我能负责的部分是什么？一个人把责任全部推给别人，也就把改变的权利交给了别人。逃避责任的代价，是甘愿处于附属地位。</p>\n<p>心理问题常有两种相反方向：一种人把别人的责任也揽到自己身上，什么都怪自己；另一种人把自己的责任全部推给外界，什么都怪别人。前者让自己痛苦，后者让别人痛苦。成熟不是无限自责，也不是无限甩锅，而是准确识别哪一部分属于自己，然后承担它。</p>\n<h2 id=\"truth-map\">尊重事实：不断更新自己的人生地图</h2>\n<p>我们对现实的理解，像一张人生地图。地图准确，就知道自己在哪里、要去哪里、怎么走；地图漏洞百出，就会在现实中迷路。问题是，人出生时没有地图，地图要靠自己画；更麻烦的是，世界不断变化，地图也必须不断更新。</p>\n<p>很多人过了青春期，就停止更新地图。到了中年，更觉得自己那套观念已经完美无缺，对新信息不再感兴趣。于是旧经验、旧创伤、旧判断，被带到全新的生活场景里，造成持续误判。</p>\n<p>有些人在童年被反复欺骗，于是得出“任何人都不可信”的结论。这个结论小时候可能保护过他，让他不再对失信的父母抱有期待；但长大后如果把它套在所有人身上，关系、工作和婚姻都会被破坏。过时地图一旦被当成真理，就会把人困在过去。</p>\n<h2 id=\"balance\">保持平衡：自律也需要弹性</h2>\n<p>自律的第四个原则，是保持平衡。真正成熟的人不是永远压抑情绪，也不是放任情绪，而是既能表达，也能控制；该委婉时委婉，该直接时直接，该心平气和时心平气和，该发火时也能发火。</p>\n<p>保持平衡的最高原则，是放弃。放弃一时快感，才能换来转弯时的平衡；放弃必须赢的欲望，才能成为更好的父亲、伴侣、朋友和自己。有些放弃很小，比如放弃速度、放弃争辩、放弃一次发怒；有些放弃很大，比如放弃固有人格、根深蒂固的行为模式，甚至整个世界观。</p>\n<p>放弃不是失败，而是为了让新的自己出生。失去平衡，远比放弃更痛苦。</p>\n<h2 id=\"love-action\">爱不是感觉，而是促进心智成熟的行动</h2>\n<p>自律的原动力，是爱。真正的爱，是为了促进自己和他人心智成熟而产生的自我完善意愿。这个定义非常严格：爱是长期艰难的过程，是心智不断成熟，是爱自己也是爱他人，更重要的是，爱必须落实为行动。</p>\n<p>爱的愿望不等于爱的行动。口头说爱，却不付出时间、精力、关注和责任，本质上只是情绪表达。真正的爱，要让自己和对方都更成熟、更自由、更完整。</p>\n<p>因此，很多被误认为爱的东西，其实不是爱。</p>\n<h2 id=\"false-love\">坠入情网、依赖和感觉，都不等于爱</h2>\n<p>坠入情网常被误认为最强烈的爱，但它更像自我界限的暂时崩塌。激情让人觉得彼此合而为一，孤独消失，狂喜涌现。可蜜月会结束，激情会消退，现实会让两个人重新看见彼此的差异。</p>\n<p>情侣只有从情网中走出来，才可能真正相爱。真爱不是自我界限的短暂崩塌，而是自我界限的扩展。它不是吞并对方，而是在尊重独立的前提下，让自己能够关心、理解和成全另一个独立生命。</p>\n<p>依赖也不是爱。有些人并不在乎依赖对象是谁，只要有人可以填补内心空洞就满足。没有别人就无法生存，那不是爱，而是寄生。真正的爱是自由选择：两个人不一定非要生活在一起，只是选择生活在一起。</p>\n<p>爱的感觉同样不是爱。真正的爱需要行动，而行动最常见、最重要的形式之一是关注。认真倾听一个孩子单调、重复、没完没了的表达，需要耐心和注意力；但正是这种倾听，让孩子感受到尊重，进而学会自尊自爱。</p>\n<h2 id=\"independence\">爱与独立：不要把爱变成枷锁</h2>\n<p>不能接受所爱之人的独立性，就会伤害亲情和爱情。孩子不是父母的延伸，伴侣也不是自我的附属物。可以给予爱，却不能把自己的想法强加给对方；可以站在一起，却不能靠得太近，以至于彼此无法成长。</p>\n<p>真正的爱会面对冲突风险，也会在批评之前自我反省：我的观点有价值吗？我的动机真的是为对方着想吗？我是否真正了解这个人？成熟的爱不是控制，而是尊重独立之后仍愿意投入行动。</p>\n<h2 id=\"worldview\">成长，就是走出童年的小宇宙</h2>\n<p>每个人都有自己的“宗教”，这里指的不是是否信神，而是对人生和世界的基本理解。一个人的世界观往往来自童年家庭。父母充满爱，孩子容易相信世界有温暖；父母言而无信、控制欲强、睚眦必报，孩子就可能把世界理解成充满危险和惩罚。</p>\n<p>心智成熟，就是从童年小宇宙进入更大的现实宇宙。人必须摆脱父母、创伤和早年经验塞给自己的狭窄世界观，通过自己的经验和思考，建立与现实接轨的信念。</p>\n<p>有时治疗真正开始的时刻，是一个人终于敢承认被压抑的真实情绪：我恨、我怕、我失望、我不愿继续扮演好孩子。只有真实浮出水面，成熟才可能发生。</p>\n<h2 id=\"unconscious\">倾听潜意识：心智成熟是接近真实</h2>\n<p>人的潜意识知道的事情，常常比意识多。梦、口误、迟到、忘记签名、莫名其妙的抗拒，可能都在传递被意识压住的信息。很多心理症状，正是意识抗拒潜意识智慧的结果。</p>\n<p>成熟不是只靠理性压制一切，而是学会倾听心灵深处的信号，让意识更接近真实。那些不愿面对的愤怒、嫉妒、恐惧、渴望和怨恨，不会因为被压抑而消失，只会以更扭曲的方式回来。</p>\n<h2 id=\"road\">少有人走的路，疼，但通向自由</h2>\n<p>人可以拒绝很多东西，但不能拒绝成熟。拒绝成熟，就是拒绝问题；拒绝问题，就是逃避痛苦；而规避问题和逃避痛苦，正是许多心理疾病的根源。</p>\n<p>少有人走的路，不是因为没人知道，而是因为这条路太疼。它要求人先吃苦、承担责任、尊重事实、放弃旧自我；它要求人把爱从感觉变成行动，把依赖变成自由，把童年地图更新成现实地图。</p>\n<p>大多数人宁愿躲在熟悉的痛苦里，也不敢走向未知的自由。但真正的心智成熟，恰恰从承认痛苦、面对问题、主动行动开始。勇敢点，走上去。</p>\n"
  },
  {
    "slug": "sleep-biological-sovereignty-modern-civilization",
    "title": "睡眠是一种生物主权：现代文明如何异化了深度睡眠",
    "desc": "睡眠不是躺下休息，而是大脑清理、记忆固化、心血管修复和生物节律重建的核心机制。现代照明、恒温房间和数字刺激正在改写这套古老系统。",
    "category": "健康科学",
    "series": "生物主权",
    "tags": [
      "睡眠",
      "深度睡眠",
      "生物节律",
      "生物主权",
      "现代文明",
      "光照",
      "体温",
      "健康"
    ],
    "minutes": 10,
    "cover_sub": "深度睡眠 · 生物节律 · 生命主权",
    "cover_note": "修复大脑的关键，不是睡了多久，而是睡得多深",
    "article": "\n<h2 id=\"sleep-paradox\">睡眠悖论：最危险的行为，为什么被进化保留下来</h2>\n<p>在自然界里，睡眠看起来是一个巨大的生存漏洞。闭上眼睛、降低警觉、放弃行动能力，意味着捕食风险大幅上升。对许多动物来说，夜晚睡眠就是把生命交给环境。</p>\n<p>但所有高等生物都保留了睡眠。这个事实说明，睡眠的底层价值远远超过短期生存风险。它不是多余的休息，也不是懒惰的生理借口，而是大脑和身体必须支付的修复成本。</p>\n<p>真正的问题在于，现代文明用工业时间、人工照明、恒温空间和数字刺激，把这套古老系统重塑到接近异化。人类占有了夜晚，却付出了睡眠质量滑坡的代价。</p>\n<h2 id=\"evolution\">从古猿到农耕：人类睡眠一直在被环境改造</h2>\n<p>早期古猿的睡眠并不舒服。庇护有限，还有坠落风险，即使睡很久，大部分也可能是低效浅睡。现在偶尔入睡时出现坠落感、身体突然抖动，很可能仍保留着远古时期刻进身体的生存警觉。</p>\n<p>进入狩猎采集时代，篝火、部落和轮流守夜让安全系数大幅提高。人类睡眠出现了一次大胆革命：总睡眠时间被压缩，深度却提升。连续而高质量的慢波睡眠，成为人类大脑发展和认知优势的一部分。</p>\n<p>农耕时代，房屋构建了更安全的物理边界，睡眠开始私有化。但那时并不一定是一觉到天亮。历史文献显示，人类长期存在“双相睡眠”：先睡约四小时，午夜自然醒来两三个小时，再继续睡到天亮。中间清醒时间用于修补衣物、交谈、祈祷、亲密生活或静静独处。</p>\n<h2 id=\"industrial-time\">电灯亮起之后，机械时钟驯化了生物时钟</h2>\n<p>双相睡眠很可能更贴近某种自然节律，但工业文明不欢迎它。电灯、工厂、打卡、通勤和统一作息，把两段式睡眠强行缝合成单相睡眠。睡觉被压缩成一段可以被管理、被计算、被工作制度安排的时间块。</p>\n<p>不能适应单相早起的人，被贴上懒惰、不自律、效率低的标签。可这未必是个人品质问题，而是现代制度把生物差异简化成了道德评价。</p>\n<p>到了数字时代，刺激恒温、通宵照明、游戏、短视频和 24 小时信息流，进一步抹掉了自然气流、温差、黑暗和安静给身体的入睡信号。人类确实拥有了更明亮的夜晚，却也失去了很多古老的节律提示。</p>\n<h2 id=\"deep-sleep\">深度睡眠：大脑真正的大扫除</h2>\n<p>无论睡眠形式如何变化，深度睡眠都有强烈的内稳态需求。白天，大脑千亿神经元高速运转，产生大量代谢废物。要清理它们，必须等到脑波活动变慢、神经元间隙增大，脑脊液才能像高压水流一样冲刷毒性蛋白。</p>\n<p>这个过程主要发生在非快速眼动睡眠的 N3 期，也就是深度睡眠。它不是整晚连续发生，而是分布在多个睡眠周期里。这样的结构看起来复杂，却是进化在安全、修复和应急之间找到的折中方案。</p>\n<p>当深度睡眠不足时，躺够八九个小时也可能醒来脑雾重重。全球大量人群存在睡眠障碍，许多白领每天深度睡眠甚至凑不够 45 分钟。问题不是睡眠时长看起来不够，而是黄金修复时间被挤碎了。</p>\n<h2 id=\"temperature\">温度曲线：恒温房间并不等于好睡眠</h2>\n<p>自然界的夜晚，温度会不断变化。皮肤感受到昼夜温差后，微血管扩张，核心体温下降，这是进入深度睡眠的重要物理条件。早期人类以地为席、以天为被，身体温度和环境温度可以自然对流。</p>\n<p>现代人用空调、厚被和恒温房间给自己制造了热量绝缘体。问题在于，睡眠不同阶段对温度的需求并不相同。入睡需要降温，深睡需要低温窗口，快速眼动睡眠阶段低温又可能导致微觉醒，临近醒来还需要环境变暖来唤醒肌肉和神经。</p>\n<p>因此，固定温度只是粗暴地“一刀切”，并不符合睡眠修复的动态需求。真正有效的睡眠环境，不是永远保持某个舒适温度，而是尽量贴近身体在不同阶段需要的温度曲线。</p>\n<h2 id=\"light\">光照：蓝光和昼夜错位会推迟睡意</h2>\n<p>光照是搅乱睡眠的另一个重要推手。大脑会根据光线判断时间。如果夜晚持续暴露在高色温白光和电子屏幕蓝光下，身体会误以为白天还没结束，从而推迟褪黑素分泌和睡意到来。</p>\n<p>更合理的做法，是在睡前几个小时逐渐把环境光从高色温白光调成低色温、低照度、偏红或琥珀色的光，模拟自然日落。睡前减少手机和强光刺激，不是仪式感，而是在给身体一个明确的夜晚信号。</p>\n<h2 id=\"cognition\">深度睡眠决定记忆、学习和认知表现</h2>\n<p>深度睡眠不仅清理大脑，也参与记忆固化和技能整合。研究中，当人即将进入深度睡眠时被无声干扰、拉回浅睡眠，第二天记忆固化和运动技能表现会明显下降。</p>\n<p>如果把这种差距放到考试、工作、训练和关键决策上，它会悄悄改变人生轨迹。很多人以为自己只是没休息好，实际上可能是在用低质量睡眠削弱判断、学习和反应速度。</p>\n<p>长期看，深度睡眠不足还可能与神经退行性问题相关。某些毒性蛋白堆积会破坏产生深度睡眠脑波的区域，而深度睡眠越少，清理越差，形成恶性循环。记忆被逐渐抹掉，是人类能想象的最残酷告别之一。</p>\n<h2 id=\"heart\">睡眠也是心血管系统的夜间维护</h2>\n<p>深度睡眠中，负责激活身体的交感神经会把控制权交给负责修复的副交感神经。血压下降，心率降低，心脏和主动脉进入维护时间。</p>\n<p>当深度睡眠受限，交感神经会在深夜继续保持高激活，向血液中释放压力相关激素，造成心血管系统负担。少睡几小时之后，心跳偏快和紧绷感可能持续好几个小时。长期睡眠不足的人，心血管风险会显著抬升。</p>\n<p>所以睡眠不是躺下休息，而是身体每天必须执行的一整套维护程序。</p>\n<h2 id=\"technology\">科技不是妥协，而可能是重新夺回节律</h2>\n<p>既然现代人已经很难退回篝火、自然温差和无屏幕夜晚，就需要用新的方式重建节律。动态温控床垫、睡眠监测、光照管理和环境设计，本质上不是炫技，而是在工业文明里重新为身体编辑更接近自然的信号。</p>\n<p>关键不在设备本身，而在思路：睡眠需要被当作一项生物资产管理。温度、光照、噪音、床品、作息、屏幕、饮食和压力，都在共同决定深度睡眠能否出现。</p>\n<h2 id=\"sovereignty\">守住睡眠，就是守住生物主权</h2>\n<p>现代文明最隐蔽的剥夺，不只是占用人的工作时间，也包括侵入夜晚、切碎睡眠、重写节律。一个长期睡不好的人，很难真正拥有清醒、稳定、专注和自由的白天。</p>\n<p>睡眠是一种生物主权。它决定大脑能否清理，记忆能否固化，心血管能否修复，情绪能否稳定。守住睡眠，不是逃避努力，而是守住努力的底层系统。</p>\n<p>真正高级的生活，不是用咖啡因和意志力硬扛疲惫，而是尊重身体古老而精密的节律。把夜晚还给修复，把黑暗还给睡意，把深度睡眠还给大脑，这是一种清醒的生命管理。</p>\n"
  },
  {
    "slug": "economic-cycles-interest-debt-human-nature",
    "title": "逃不开的经济周期：利率、债务与人性，如何反复收割普通人",
    "desc": "经济周期不是随机意外，而是市场经济中反复出现的商业循环。繁荣会孕育萧条，债务会放大崩塌，人性的贪婪和恐惧会让顶点更高、谷底更深。",
    "category": "投资研究",
    "series": "周期与资产",
    "tags": [
      "经济周期",
      "逃不开的经济周期",
      "利率",
      "债务",
      "房地产周期",
      "资产配置",
      "金融危机",
      "人性"
    ],
    "minutes": 13,
    "cover_sub": "利率 · 债务 · 人性",
    "cover_note": "周期不死，只是形态在变",
    "article": "\n<h2 id=\"cycle-never-dies\">周期不死，只是剧本换了演员</h2>\n<p>2015 年，很多人记得那种空气里的狂热：辞职炒股、抵押房子加杠杆、逢人就谈财务自由。到了多年以后，当年看起来老老实实上班、攒钱、还房贷的人，反而可能是损失最少的。</p>\n<p>这样的剧本不会只演一次。再过十年，人物会换，台词会换，资产名字会换，但情绪结构很可能一样：繁荣时人人相信明天更好，萧条时人人相信天要塌了。周期不是意外，而是市场经济的潮汐。</p>\n<p>《逃不开的经济周期》最核心的提醒是：繁荣一定会来，繁荣之后萧条也一定会来，萧条之后复苏仍会来。真正的问题不在于周期是否存在，而在于你站在周期的什么位置。</p>\n<h2 id=\"business-cycle\">经济周期，本质是商业循环</h2>\n<p>“经济周期”听起来很学术，但它更准确地说是商业循环：企业、信贷、市场选择、库存、投资和资产价格共同驱动的起落。农业社会没有现代意义上的经济周期，因为增长慢，兴衰更多由天灾和战争决定。计划经济也没有典型商业循环，因为价格、信贷和企业行为高度行政化。</p>\n<p>只有在工商企业占主体、市场价格发挥作用、信贷能够扩张和收缩的地方，周期才会像潮水一样反复出现。1862 年，法国经济学家朱格拉通过欧洲和美国几十年的数据发现，经济危机并不是随机事件，而是大约每 9 到 10 年出现一次。</p>\n<p>朱格拉有一句极透彻的话：萧条的唯一原因就是繁荣。萧条不是繁荣的反面，而是繁荣的必然账单。就像大醉之后的头痛，不是意外，而是酒精早就写好的后果。</p>\n<h2 id=\"nested-cycles\">多个周期叠加，才是真实世界</h2>\n<p>周期不止一种。最短的是库存周期，大约三到五年。商品好卖，企业加库存；库存过高，企业去库存；就业、工资和消费随之波动。</p>\n<p>再往上是朱格拉周期，大约 9 到 10 年，对应企业设备投资。企业赚钱后贷款买设备、建厂房、扩产线；同行都这么做，产能过剩就会出现，利润被压缩，危机随之而来。</p>\n<p>更长的是库兹涅茨周期，大约 18 年，与房地产密切相关。房地产之所以被称为周期之母，是因为它牵连土地、金融、财政、居民资产负债表和上下游产业链，杠杆巨大，杀伤力也巨大。</p>\n<p>再往上还有康德拉季耶夫长波，大约 50 到 60 年，对应一轮技术革命从诞生、普及到平庸的过程：蒸汽机、铁路、电力、互联网，每一代技术都会经历类似的扩散和退潮。</p>\n<p>人以为自己活在当下，其实活在多条不同频率周期线交织的网格里。短期库存周期可能让工资上涨，长期房地产周期却可能让资产负债表受重创。长周期碾压短周期时，个人感受会非常割裂。</p>\n<h2 id=\"asset-sequence\">资产价格有传导顺序：利率是第一张牌</h2>\n<p>周期传导有一个经典顺序：央行加息，债券价格先跌，接着股票跌，然后大宗商品跌，最后房地产跌；反过来，央行降息，债券先涨，股票涨，商品涨，房地产再涨。</p>\n<p>这个顺序像多米诺骨牌。利率是最先被推动的那张牌。普通人不需要搞懂所有经济学理论，但必须明白：当央行连续降息，水已经开始往管道里灌；至于什么时候流到股市、商品、房地产和实体经济，是时间差问题。</p>\n<p>利率上行时，不要轻易加杠杆追资产；利率下行时，也不要在最恐慌的时候把优质资产扔在地板上。</p>\n<h2 id=\"central-bank\">央行调控是一门艺术，因为人性无法精确计算</h2>\n<p>央行最核心的权力，是印钱和调利率。松一松手，市场开始狂欢；紧一紧手，市场开始逃命。但这个操作不是机械公式，而是一门艺术。</p>\n<p>理论上，通胀高了加息，经济冷了降息。可现实中，加息少了，市场不当回事，资金继续冲向股市和房市；加息猛了，某家机构资金链断裂，恐慌可能迅速传染成系统性危机。风险敞口可以计算，恐慌的传播速度却很难计算。</p>\n<p>观察宏观水温，一个重要指标是全社会每年支付的利息总额占 GDP 的比重。如果利息负担太重，钱都用来还债，消费和投资会被压制，经济更容易滑向衰退；利息负担较轻时，储蓄更容易转化为投资，经济活动也更活跃。</p>\n<h2 id=\"debt-deflation\">债务紧缩：越努力还债，债务反而越重</h2>\n<p>欧文·费雪曾在大萧条前判断股市进入永久高原，随后被崩盘重创。但也正是这次打击，让他写出了关于萧条的重要分析：过度负债会引发连锁崩塌。</p>\n<p>当全社会债务过高，系统就极其脆弱。一个环节违约，会迫使其他人抛售资产还债；资产越卖越便宜，越便宜越不够还债，越不够还债越要继续卖。这就是债务紧缩螺旋。</p>\n<p>最残酷的是，债务人越努力还债，整体债务反而越重。因为大家同时清算债务，会推高货币购买力、压低资产价格，而债务名义金额却固定不变。房子卖便宜了，债还是那个数，人反而更还不起。</p>\n<p>建立在债务之上的繁荣，迟早要面对债务清算的痛苦。</p>\n<h2 id=\"human-nature\">周期一半是数学，一半是人性</h2>\n<p>人的贪婪和恐惧，会放大一切。经济好到不能再好时，人们觉得还能更好，于是追加投资、追加消费、追加贷款；经济坏到不能再坏时，人们觉得天要塌了，于是囤积现金、解雇员工、抛售资产。</p>\n<p>集体行为本身，会让顶点更高、谷底更深。所谓周期，一半是数学，一半是人性。数学部分可以建模，人性部分只能靠纪律和清醒去对抗。</p>\n<p>当理发师、出租车司机、同学聚会都在讨论某类资产时，该考虑的可能不是加仓，而是风险正在抬升；当所有人都喊现金为王时，优质资产可能已经被打到很低的位置。</p>\n<h2 id=\"policy-limit\">政府能救急，不能替代企业家复苏</h2>\n<p>经济衰退时，政府可以通过发债、基建、降息、补贴创造需求。这些政策像强心针，能救急，能避免系统坍塌，但未必能真正治病。</p>\n<p>真正的复苏，最终还是来自企业家精神：有人愿意在废墟中找机会，创造新产品、新模式、新市场。熊彼特称之为创造性毁灭。旧东西死掉，新东西长出来，经济才有新的增长基础。</p>\n<p>政府能铺路、降息、发补贴，但不能替企业发现市场缝隙，也不能替个人和企业建立新的生产力。</p>\n<h2 id=\"ordinary-person\">普通人如何与周期共处</h2>\n<p>理解周期，不是为了预测每一个拐点。顶级经济学家也预测不准所有细节，普通人更不必给自己加戏。真正有用的是知道自己在什么河流里游泳：这不是平静湖面，而是一条有暗流、有涨落、有季节的大河。</p>\n<p>第一，搞懂利率。利率上行时别加杠杆，别追资产，别把房价和股价想象成永远上涨。利率下行时也别过度恐慌，要观察资金重新进入资产的顺序。</p>\n<p>第二，搞清周期位置。不要用短期景气判断长期趋势。工资上涨可能只是库存周期回暖，买房却可能踩在房地产长周期顶部。</p>\n<p>第三，留足缓冲。过度负债的人，在周期转折点最容易被打穿。现金流、安全垫和低杠杆，是穿越周期最朴素也最有效的保护。</p>\n<p>第四，克制贪婪，也克服恐惧。繁荣时别把未来永远线性外推，萧条时也别相信世界从此不会好转。</p>\n<h2 id=\"coldness\">穿越周期的人，不是最聪明，而是最冷静</h2>\n<p>周期的本质，是利用人性赚钱：在别人贪婪时把筹码卖给他，在别人恐惧时从他手里把筹码接过来。听起来简单，执行起来反人性。</p>\n<p>真正穿越周期的投资者和企业，不一定是最聪明的，而是最冷静的。他们在向上时留有余地，在向下时保留底气；在繁荣中记得萧条会来，在萧条中记得复苏也会来。</p>\n<p>周期无法逃开，但可以理解、承受、应对和利用。历史的韵脚从未改变，改变的只是穿在韵脚外面的那套衣服。</p>\n"
  }
]
CHANGED=set()
def esc(v): return html.escape(v, quote=True)
def rec(p): CHANGED.add(p.relative_to(ROOT).as_posix())
def write(p,t): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(t, encoding='utf-8'); rec(p)
def term_url(kind, term): return f'/{kind}/{quote(term)}/'
def meta_links(post):
    cat=f'<a href="{term_url("categories", post["category"])}">{esc(post["category"])}</a>'
    tags='&nbsp;'.join(f'<a href="{term_url("tags", tag)}">{esc(tag)}</a>' for tag in post['tags'])
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post["minutes"]} min'
def toc(article):
    links=[f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>' for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', article)]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>'+''.join(links)+'</nav></div></div>'
def cover_svg(post, idx):
    palettes=[('#111827','#7c2d12','#dc2626','#fef3c7'),('#0f172a','#1e3a8a','#22c55e','#dcfce7'),('#111827','#581c87','#f59e0b','#fef3c7'),('#082f49','#164e63','#38bdf8','#e0f2fe'),('#1f2937','#312e81','#f97316','#ffedd5')]
    a,b,c,d=palettes[idx%len(palettes)]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900"><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="0.55" stop-color="{b}"/><stop offset="1" stop-color="{c}"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.34"/></filter></defs><rect width="1600" height="900" fill="url(#bg)"/><g opacity="0.14" stroke="#f8fafc" stroke-width="3"><path d="M130 690 H1470"/><path d="M130 560 H1470"/><path d="M130 430 H1470"/><path d="M130 300 H1470"/><path d="M340 235 V760"/><path d="M660 235 V760"/><path d="M980 235 V760"/><path d="M1300 235 V760"/></g><g filter="url(#shadow)"><path d="M210 620 C390 430 520 575 700 420 C860 282 995 358 1175 235 C1268 172 1360 148 1450 124" fill="none" stroke="{d}" stroke-width="18" stroke-linecap="round"/><rect x="112" y="610" width="980" height="118" rx="24" fill="#ffffff" opacity="0.94"/><text x="156" y="682" fill="{b}" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800">{esc(post['cover_sub'])}</text></g><text x="96" y="150" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="56" font-weight="800">{esc(post['title'])}</text><text x="100" y="236" fill="{d}" font-family="Noto Sans SC, PingFang SC, Arial" font-size="34" font-weight="700">{esc(post['cover_note'])}</text></svg>'''
def build_article(post, idx, prev_url, prev_title, next_url, next_title):
    template=(ROOT/PREV_ORIGINAL_URL.strip('/')/'index.html').read_text(encoding='utf-8')
    start=template.find('<article class="post">'); end=template.find('</article>', start)+len('</article>')
    head, tail=template[:start], template[end:]
    full=SITE+post['url']
    replacements={r'<title>.*?</title>':f'<title>{esc(post["title"])} - zcxGGmu\'s Blog</title>',r'<meta name="description" content="[^"]*">':f'<meta name="description" content="{esc(post["desc"])}">',r'<meta property="og:url" content="[^"]*">':f'<meta property="og:url" content="{esc(full)}">',r'<meta property="og:title" content="[^"]*">':f'<meta property="og:title" content="{esc(post["title"])}">',r'<meta property="og:description" content="[^"]*">':f'<meta property="og:description" content="{esc(post["desc"])}">',r'<link rel="canonical" href="[^"]*">':f'<link rel="canonical" href="{esc(full)}">'}
    for pat, repl in replacements.items(): head=re.sub(pat,repl,head,flags=re.S)
    newer=f'<a class="newer-posts" href="{next_url}">下一篇<br>{esc(next_title)}</a>' if next_url else '<a class="newer-posts">下一篇<br>没有更新的文章</a>'
    older=f'<a class="older-posts" href="{prev_url}">上一篇<br>{esc(prev_title)}</a>'
    article=f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{post['cover']}')"><div class="post-title">{esc(post['title'])}<div class="post-subtitle">{esc(post['desc'])}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links(post)}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{post['article']}</div></div><nav class="post-pagination">{newer}{older}</nav>\n    </article>'''
    tail=re.sub(r'<div class="toc-wrapper">.*?</div></div>', toc(post['article']), tail, flags=re.S)
    write(ROOT/post['url'].strip('/')/'index.html', head+article+tail)
def update_original_prev(new_url, new_title):
    path=ROOT/PREV_ORIGINAL_URL.strip('/')/'index.html'
    text=path.read_text(encoding='utf-8')
    text=re.sub(r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>', f'<a class="newer-posts" href="{new_url}">下一篇<br>{esc(new_title)}</a>', text, count=1, flags=re.S)
    write(path,text)
def home_card(post):
    return f'''<a href="{post['url']}" class="a-block">\n      <div class="post-item-wrapper ">\n        <div class="post-item post-item-no-divider">\n          <div class="post-item-info-wrapper">\n            <div class="post-item-title">{esc(post['title'])}</div>\n            <div class="post-item-summary">{esc(post['desc'])}</div>\n            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post['minutes']} min&nbsp;&nbsp;</div>\n          </div>\n          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{post['cover']}')"></div></div>\n        </div>\n      </div>\n    </a>'''
def update_home():
    path=ROOT/'index.html'; text=path.read_text(encoding='utf-8')
    for post in POSTS: text=re.sub(rf'<a href="{re.escape(post["url"])}" class="a-block">.*?</a>\s*','',text,flags=re.S)
    pos=text.find(f'<a href="{PREV_ORIGINAL_URL}" class="a-block">')
    if pos==-1: raise RuntimeError('homepage marker missing')
    cards='\n'.join(home_card(p) for p in reversed(POSTS))+'\n'
    write(path,text[:pos]+cards+text[pos:])
def update_rss():
    path=ROOT/'index.xml'; text=path.read_text(encoding='utf-8')
    pub_dt=datetime(2026,7,19,9,0,tzinfo=timezone(timedelta(hours=8)))+timedelta(minutes=len(POSTS))
    text=re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{format_datetime(pub_dt)}</lastBuildDate>', text)
    for post in POSTS: text=re.sub(rf'<item>\s*<title>{re.escape(esc(post["title"]))}</title>.*?</item>\s*','',text,flags=re.S)
    items=[]
    for i,post in enumerate(reversed(POSTS)):
        dt=datetime(2026,7,19,9,0,tzinfo=timezone(timedelta(hours=8)))+timedelta(minutes=len(POSTS)-i)
        full=SITE+post['url']
        items.append(f'<item>\n<title>{esc(post["title"])}</title>\n<link>{full}</link>\n<guid>{full}</guid>\n<pubDate>{format_datetime(dt)}</pubDate>\n<description>{esc(post["desc"])}</description>\n</item>\n')
    write(path,text.replace('<item>',''.join(items)+'<item>',1))
def update_archive():
    path=ROOT/'archive/index.html'; text=path.read_text(encoding='utf-8')
    missing=sum(1 for p in POSTS if p['url'] not in text)
    if missing:
        text=re.sub(r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>', lambda m:f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1))+missing} 篇</span>', text, count=1)
    for post in POSTS: text=re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(post["url"])}">.*?</div>\s*','',text,flags=re.S)
    items=[]
    for post in reversed(POSTS):
        items.append(f'''<div style="padding:8px 0;font-size:15px">\n        <span style="color:#999">{DATE}</span>&nbsp;\n        <a href="{post['url']}">{esc(post['title'])}</a>\n        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(post['category'])}</span></span>\n      </div> ''')
    pos=text.find(f'<a href="{PREV_ORIGINAL_URL}">'); start=text.rfind('<div style="padding:8px 0;font-size:15px">',0,pos)
    write(path,text[:start]+''.join(items)+text[start:])
def tax_item(post):
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">\n        <a href="{post['url']}" style="font-size:16px;text-decoration:none">{esc(post['title'])}</a>\n        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>\n      </div> '''
def update_term_index(kind, term, delta):
    if not delta: return
    path=ROOT/kind/'index.html'; text=path.read_text(encoding='utf-8'); href=f'/{kind}/{quote(term)}/'
    if href in text:
        pattern=re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span style="color:#999[^>]*>\()(\d+)(\)</span></a>)')
        text=pattern.sub(lambda m:f'{m.group(1)}{int(m.group(2))+delta}{m.group(3)}', text, count=1)
    else:
        item=f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">({delta})</span></a>\n' if kind=='tags' else f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">({delta})</span></a>\n'
        pos=text.find('</div></div></div>'); text=text[:pos]+item+text[pos:]
    write(path,text)
def update_term(kind, term, prefix, emoji, posts):
    path=ROOT/kind/term/'index.html'
    if path.exists():
        old=path.read_text(encoding='utf-8'); inserted=sum(1 for p in posts if p['url'] not in old); text=old
        for p in posts: text=re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(p["url"])}".*?</div>\s*','',text,flags=re.S)
        if inserted: text=re.sub(r'共 (\d+) 篇文章', lambda m:f'共 {int(m.group(1))+inserted} 篇文章', text, count=1)
        first=text.find('<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">')
        if first==-1: first=text.find('</div></div></div>')
        text=text[:first]+''.join(tax_item(p) for p in reversed(posts))+text[first:]
    else:
        inserted=len(posts); label=f'{prefix}: {term}' if prefix else term; h1=f'{emoji} {term}' if emoji else label
        text=f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu\'s Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu\'s Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 {len(posts)} 篇文章</p>{''.join(tax_item(p) for p in reversed(posts))}</div></div></div><script src="/js/journal.js"></script></body></html>'''
    write(path,text); update_term_index(kind, term, inserted)
def update_taxonomies():
    groups={}
    for p in POSTS:
        groups.setdefault(('categories',p['category'],'分类',''),[]).append(p)
        groups.setdefault(('series',p['series'],'','📚'),[]).append(p)
        for tag in p['tags']: groups.setdefault(('tags',tag,'标签','🏷️'),[]).append(p)
    for (kind,term,prefix,emoji),posts in groups.items(): update_term(kind,term,prefix,emoji,posts)
def validate():
    failures=[]; forbidden=['B站','bilibili','哔哩','视频里','视频中','原视频','音频里','音频中','UP主','up主','这期','本期','作者说','他提到','观看','点赞','订阅','欢迎来到','感谢你看到','下期再见','一键三连','投币']
    for p in POSTS:
        article=(ROOT/p['url'].strip('/')/'index.html').read_text(encoding='utf-8')
        for w in forbidden:
            if w in article: failures.append(f'{p["slug"]} forbidden {w}')
        for w in [p['title']]+p['must']:
            if w not in article: failures.append(f'{p["slug"]} missing {w}')
        h2=re.findall(r'<h2 id="([^"]+)">',article); links=re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"',article)
        if h2!=links: failures.append(f'{p["slug"]} toc mismatch')
    home=(ROOT/'index.html').read_text(encoding='utf-8')
    order=re.findall(r'<a href="(/2026/[^"]+/)" class="a-block">',home)[:11]
    expected=PINNED+[p['url'] for p in reversed(POSTS)]+[PREV_ORIGINAL_URL]
    if order!=expected: failures.append(f'home order mismatch {order}')
    ET.parse(ROOT/'index.xml')
    for p in POSTS:
        for rel in ['archive/index.html', f'categories/{p["category"]}/index.html', f'series/{p["series"]}/index.html', f'tags/{p["tags"][0]}/index.html']:
            path=ROOT/rel
            if not path.exists(): failures.append(f'missing {rel}')
            elif p['url'] not in path.read_text(encoding='utf-8'): failures.append(f'{rel} missing {p["url"]}')
        cover=ROOT/p['cover'].strip('/')
        if not cover.exists() or cover.stat().st_size<1000: failures.append(f'bad cover {p["slug"]}')
        else: ET.parse(cover)
    previous=(ROOT/PREV_ORIGINAL_URL.strip('/')/'index.html').read_text(encoding='utf-8')
    if POSTS[0]['url'] not in previous: failures.append('original previous newer link missing')
    for a,b in zip(POSTS, POSTS[1:]):
        txt=(ROOT/a['url'].strip('/')/'index.html').read_text(encoding='utf-8')
        if b['url'] not in txt: failures.append(f'{a["slug"]} newer chain missing')
    if failures: raise SystemExit('\n'.join(failures))
    print(json.dumps({'validation':'passed','articles':len(POSTS),'home_top':order[:11]}, ensure_ascii=False, indent=2))
def publish_changed_list():
    script_rel='tasks/publish-life-decision-focus-discipline-sleep-cycle-batch.py'; changed_rel='tasks/publish-life-decision-focus-discipline-sleep-cycle-changed-files.json'
    rec(ROOT/script_rel); all_changed=sorted(CHANGED|{script_rel,changed_rel}); write(ROOT/changed_rel,json.dumps(all_changed,ensure_ascii=False,indent=2)); print(json.dumps({'changed':len(all_changed),'urls':[SITE+p['url'] for p in POSTS]},ensure_ascii=False,indent=2))
def main():
    for i,p in enumerate(POSTS):
        p['url']=f'/2026/{p["slug"]}/'; p['cover']=f'/images/posts/{p["slug"]}/cover.svg'; p['must']=[p['title'].split('：')[0], p['tags'][0], p['tags'][1], p['tags'][2]]; write(ROOT/p['cover'].strip('/'), cover_svg(p,i))
    for i,p in enumerate(POSTS):
        prev_url=PREV_ORIGINAL_URL if i==0 else POSTS[i-1]['url']; prev_title=PREV_ORIGINAL_TITLE if i==0 else POSTS[i-1]['title']
        next_url=POSTS[i+1]['url'] if i<len(POSTS)-1 else None; next_title=POSTS[i+1]['title'] if i<len(POSTS)-1 else None
        build_article(p,i,prev_url,prev_title,next_url,next_title)
    update_original_prev(POSTS[0]['url'], POSTS[0]['title']); update_home(); update_rss(); update_archive(); update_taxonomies(); validate(); publish_changed_list()
if __name__=='__main__': main()