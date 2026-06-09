---
title: "深度拆解 @aleabitoreddit：2026 年 5 月以来的供应链研究、CPO 主线与风险校准"
date: "2026-06-09T11:35:00+08:00"
updated: "2026-06-09T11:35:00+08:00"
slug: "serenity-aleabitoreddit-may-2026-analysis"
description: "本文基于公开归档和镜像数据，系统分析 Serenity（@aleabitoreddit）在 2026 年 5 月以来的全部可抓取公开发文和同期 X Article：核心主线是 CPO/硅光/SIVE，方法论是从下游 AI 资本开支追到上游瓶颈，同时必须严格区分事实、推断、自报收益和社群噪音。"
categories:
  - "投资"
tags:
  - "Serenity"
  - "aleabitoreddit"
  - "CPO"
  - "硅光"
  - "半导体"
  - "供应链"
  - "投资分析"
series:
  - "投资体系"
featured_image: "/images/posts/serenity-aleabitoreddit-analysis/serenity-cover.svg"
pinned: false
---

![Serenity 5 月以来发文深度拆解](/images/posts/serenity-aleabitoreddit-analysis/serenity-cover.svg)

这篇文章分析的是 X 账号 [Serenity（@aleabitoreddit）](https://x.com/aleabitoreddit) 在 2026 年 5 月以来的公开内容。这个账号的中文圈认知度最近快速上升，原因不是普通宏观评论，而是它持续把 AI 半导体、CPO、硅光、上游材料、功率半导体、机器人供应链和小市值股票放在同一张供应链地图里研究。

我的结论先放在前面：2026 年 5 月以来，这个频道的主线非常明确，不是泛泛看多 AI，而是围绕 CPO / silicon photonics / optical interconnect 展开的上游瓶颈交易。`$SIVE` 是绝对中心，`$AAOI`、`$LITE`、`$SOI`、`$AXTI`、`$JBL`、`$MRVL` 是围绕这条主线不断被引用的关键节点。第二层主线是融资质量和资本结构，尤其是用 `$NBIS` 对比 `$IREN`、`$CRWV`。第三层主线是 AI 基建继续向存储、电力、800V DC、机器人实体供应链和先进封装外溢。

但这不是一个可以无脑跟单的频道。它的价值在于提供研究线索和供应链推理框架，而不是提供可审计交易记录。频道里有大量高质量的链条拆解，也有不少高置信度推断、社群众包、短期价格归因和自报收益。读者如果只复制结论，风险极高；如果学习它如何从需求端回溯供应链瓶颈，价值很大。

本文不是投资建议。所有个股提及只用于分析该频道内容结构，不构成买卖建议。

## 一、研究边界：什么叫“5 月以来的所有文章”

先把边界说清楚，否则这类分析很容易不严谨。

X 的公开时间线在未登录环境下访问不稳定，原始 X 页面不能稳定提供全量历史。本文使用三个层级的公开来源：

第一，公开归档 [yan-labs/serenity-aleabitoreddit](https://github.com/yan-labs/serenity-aleabitoreddit)。该归档说明其包含 5,857 条公开推文，覆盖 2025-07-02 到 2026-06-08，并提供文章摘要、方法论、track record 和 ticker 统计。

第二，本地可验证的归档子集。2026-05-01 以来共有 832 条非转推公开记录，时间范围是 2026-05-01T02:31:08Z 到 2026-06-08T08:43:24Z。其中 2026 年 5 月 621 条，2026 年 6 月前 8 天 211 条。

第三，公开镜像 [serenitysaid.com](https://serenitysaid.com/)。该页面在 2026-06-09 GMT+8 10:50 显示最新 35 条内容，最新可见记录为 2026-06-09T02:29:21Z，其中 18 条晚于本地归档最后一条。这个镜像用于确认 6 月 8 日 08:43 UTC 之后确有新增公开内容，但它不是完整历史库。

另外，X Article 长文和普通 X 发文要分开看。公开归档的 [X Articles Supplement](https://github.com/yan-labs/serenity-aleabitoreddit/blob/main/serenity-aleabitoreddit/references/articles.md) 索引了 4 篇长文；2026 年 5 月以来只有 1 篇，即 2026-05-19 的 [SIVE - The CPO Laser Chokepoint for Hyperscalers](https://x.com/i/article/2056688641448321024)，分享帖为 [2056691097594925522](https://x.com/aleabitoreddit/status/2056691097594925522)。归档明确不保存长文全文，只保存摘要、元数据和可迁移的 thesis 变化。

所以，本文的“所有文章”定义为：2026-05-01 以来本次会话可公开检索到的全部普通发文、线程、回复、众包清单，以及同期唯一一篇 X Article 长文的公开元数据和摘要。本文不能证明覆盖删除内容、私密内容、订阅者专属内容或登录后才可见内容。

![语料边界](/images/posts/serenity-aleabitoreddit-analysis/serenity-corpus-boundary.svg)

## 二、频道画像：它不是财经新闻号，而是供应链 OSINT 研究流

Serenity 的自我定位是 AI / semiconductor supply chain analyst。公开资料里，他把自己的方法描述为把金融科技、风投分析、AI 研究和半导体经验结合起来，寻找市场尚未充分理解的上游瓶颈。频道的语言风格很强，常用“10x”“bottleneck”“hyperscaler”“chat”“retail can find this before institutions”这样的表达，这会让内容看起来像高波动交易号。但如果剥离表达风格，它的核心其实是供应链 OSINT。

所谓 OSINT，在这里不是神秘信息，而是公开资料拼接：公司公告、财报措辞、conference slides、客户和伙伴页面变化、LinkedIn 招聘、指数纳入、持仓披露、供应链路线图、产品 qualification 进度、融资结构、ATM 或可转债条款。这些信息单独看都不一定重要，但组合起来可能形成一条上游供应链路径。

这个频道最重要的特点有三个。

第一，研究对象经常不是下游最显眼的大公司，而是大公司资本开支上游的“小而关键”的供应商。比如 AI 需求落到 CPO，不是只看 `$NVDA`，而是继续问：谁提供 CW / DFB laser？谁提供 InP substrate？谁做 silicon photonics substrate？谁做光模块、封装、检测、玻璃基板、功率半导体、变压器？

第二，它喜欢在 volume ramp 之前研究。传统筛选器看 trailing revenue、PE 和当季利润，但 Serenity 更关心 qualification、design-in、客户验证、产线准备、供应短缺和 2026-2027 年以后是否会进入大规模收入确认。这个思路有价值，但也天然高风险，因为大量 thesis 会停留在“验证中”而不是“已兑现”。

第三，它把资本结构当作核心变量。频道反复强调，不是所有增长都对普通股东有利。融资质量、客户信用、ATM 规模、可转债、债务利息、SBC 和流通股动态，都会决定一个高增长故事最终是股东增值还是股东被稀释。

## 三、数据看板：5 月以来真正的主线是什么

从 832 条本地归档记录看，5 月以来频道并不是平均覆盖所有 AI 方向，而是高度集中。

可见互动数据合计约 9441 万浏览、40.8 万点赞、12.1 万收藏、5.0 万回复。这个互动量说明它已经不只是小圈子研究帖，而是有明显社群分发能力的公开影响力账号。

主题上，CPO / 光通信 / 硅光命中 383 条，是最强主题；相关帖子累计浏览约 4713 万，占本地样本总浏览的一半左右。第二类是组合收益、社群影响和自我 track record；第三类是 AI 算力、Neocloud 和数据中心融资质量；之后才是政策资本市场、存储、800V 电力、机器人和航天防务。

![主题强度](/images/posts/serenity-aleabitoreddit-analysis/serenity-theme-distribution.svg)

ticker 统计更直观。清洗标点后，`$SIVE` 在 5 月以来出现 214 次，远高于第二名 `$NVDA` 的 80 次。`$AAOI` 72 次、`$LITE` 69 次、`$SOI` 57 次、`$AXTI` 50 次。也就是说，`$NVDA` 在这个频道里更像需求源和叙事锚点，真正反复被拆解的是 CPO / optical / substrate 供应链上的上游股票。

![热门 ticker](/images/posts/serenity-aleabitoreddit-analysis/serenity-ticker-mentions.svg)

发文节奏也值得注意。2026-06-01 单日 53 条，2026-05-30 单日 39 条。这个账号是高频研究流，不是每周一篇的低频专栏。读这种账号，逐条复述没有意义，必须按主题聚类，否则会被短期情绪和社群互动带偏。

![日更节奏](/images/posts/serenity-aleabitoreddit-analysis/serenity-daily-cadence.svg)

## 四、方法论：从下游 AI 资本开支追到上游瓶颈

Serenity 反复使用的核心方法可以概括成一句话：不要停在显眼赢家，继续沿 BOM 和供应链向上游追，直到找到没有足够替代、验证周期长、产能扩张慢、下游又必须买的瓶颈。

这套框架有六个步骤。

第一，确认下游需求是真实扩张。比如 AI 集群、CPO、光互连、存储、机器人、800V DC、玻璃基板、数据中心电力。

第二，拆供应链。不是“AI 需要芯片”这么粗，而是拆到 ASIC、光模块、外部光源、CW/DFB laser、InP substrate、SOI substrate、epi wafer、foundry、封装、检测、材料、设备和电力基础设施。

第三，找瓶颈。什么环节不能快速扩产？什么环节 qualification 周期长？什么环节如果断供，会影响下游更大的资本开支？什么环节的成本占比低但重要性高，因而下游愿意付更高价格？

第四，拼证据。证据包括公开公告、客户页面变化、conference transcript、公司年报、指数纳入、持仓变化和供应商生态位置。它经常不是单一硬证据，而是多条公开线索的组合。

第五，过滤资本结构。即使供应链 thesis 对，融资结构错也可能伤害股东。`$NBIS` 被看作融资质量较好的 neocloud，`$IREN` 则被用作大规模 ATM 和股权稀释的反面案例。

第六，做风险校准。把公司已经披露的事实、合理推断、社群众包和自报收益分层。这个步骤最容易被读者忽略，但其实最重要。

![方法论地图](/images/posts/serenity-aleabitoreddit-analysis/serenity-methodology-map.svg)

这套方法的优点是能发现常规筛选器看不到的早期供应链机会。缺点是很容易过度推断，尤其是在客户关系 NDA、量产时间、产能利用率、客户切换、良率和收入确认还没兑现时。

## 五、第一章：CPO / 硅光是 5 月以来压倒性主线

5 月以来最重要的章节就是 CPO 和 silicon photonics。

Serenity 的基本判断是：AI scale-out 继续扩张，传统铜互连和现有光模块架构会越来越难满足带宽、功耗和距离要求，CPO / optical interconnect 的市场会快速扩大。沿着这条链路，他反复讨论 `$LITE`、`$COHR`、`$AAOI`、`$MRVL`、`$JBL`、`$SOI`、`$AXTI`、`$IQE`、`$POET`，但中心是 `$SIVE`。

为什么是 `$SIVE`？因为在他的框架里，Sivers Photonics 被看作 CPO 和 1.6T 光模块上游的 merchant laser supplier，尤其是 CW / DFB laser 方向。它不是下游整机，也不是通用半导体设计公司，而是卡在外部光源和硅光系统里的一个小但关键的节点。

围绕 `$SIVE`，5 月以来出现了几类证据和推断：

一是 Jabil 1.6T pluggable optical-transceiver / LRO 方向。Serenity 把 Jabil 路径视为近期生产桥梁，认为这使 SIVE 不只押 CPO，也能受益于 1.6T pluggable transceiver。

二是 Ayar Labs、GFS、AMD、MRVL / Celestial 等生态路径。他把这些路径用于说明 SIVE 可能处在多个硅光或 CPO 路线的上游激光源位置。

三是 `$LITE` 和 `$COHR` 的行业确认。他多次引用光通信龙头对 CPO 时间线、激光瓶颈和供需紧张的说法，作为整个 CPO 链条的需求侧确认。

四是 `$SOI` 和 `$AXTI` 这样的材料 / substrate 侧延伸。`$SOI` 对应 silicon-on-insulator substrate，`$AXTI` 对应 InP substrate 和更上游材料链。它们说明他的 CPO 研究并不止于光模块，而是继续追到材料和基板。

五是台湾和亚洲供应链外溢，包括 Shunsin、FOCI、Xintec、Win Semi、MSSCorps、TSEM 等。这个方向把 CPO 从欧美上市标的扩展到台湾代工、封装、检测和设备。

这条主线的强度很高，但证据质量并不完全相同。`$LITE` 的公开 transcript、Jabil 公开进展、GFS 参考设计和公司公告属于较硬证据；客户映射、Apple / Aeva / Lightmatter / defense 路径更偏高置信推断；短期涨跌、社群争论和“机构抢筹”则需要独立核验持仓文件和流通股变化。

## 六、第二章：5 月唯一 X Article，SIVE/CPO 激光瓶颈长文

2026 年 5 月以来唯一一篇 X Article 是 [SIVE - The CPO Laser Chokepoint for Hyperscalers](https://x.com/i/article/2056688641448321024)。公开归档的摘要把它定义为 5 月以来组合影响最大的一篇长文，因为它把 `$SIVE` thesis 从推文信号升级成更系统的供应链地图。

这篇长文的核心不是简单说“SIVE 会涨”，而是把 SIVE 放在多个潜在客户和技术路线之间：

公开可映射路径包括 Jabil 1.6T 光模块、POET 外部光源合作、Ayar Labs 伙伴路径、O-Net / Enablence 外部光源、Lightium 薄膜铌酸锂集成，以及 Win Semi / GFS 作为规模化和 foundry 降风险路径。

高置信但仍未完全公开确认的路径包括 Apple silicon photonics / Apple Watch、Aeva FMCW LiDAR、Marvell / Celestial 路线等。

可选路径包括 Lightmatter / Lightelligence、AMD via GlobalFoundries、Nokia / telecom，以及 tied to defense / space 的 YSS、York Space、ALLSPACE 等。

![SIVE 供应链地图](/images/posts/serenity-aleabitoreddit-analysis/serenity-sive-supply-chain.svg)

技术壁垒上，这篇长文隐含了几个重点。

第一，激光源不是普通 commodity。CPO 或硅光系统需要稳定、低噪声、高可靠性的 CW / DFB laser，而且要和硅光平台、封装、热管理、功耗预算和客户系统验证配合。激光器一旦通过客户 qualification，替换成本不低。

第二，CPO 的难点不是单一芯片，而是系统集成。外部光源、硅光芯片、封装、驱动、交换 ASIC、热设计、良率和测试都要协同。供应链中任何一个小节点不能量产，都可能影响整条链的节奏。

第三，SIVE 的多路径 optionality 是 thesis 的吸引力，也是风险来源。路径越多，想象空间越大；但在公开订单、量产收入和毛利兑现之前，很多路径仍然是推断，不是已经完成的收入。

第四，CPO 从“未来架构”变成“近期量产”需要跨越几个关口：客户 design-in、样品验证、模块整合、foundry 产能、良率爬坡、供应协议、收入确认和毛利释放。投资分析必须盯这些节点，而不能只看概念热度。

因此，SIVE 长文最有价值的地方在于供应链地图，而不是任何单一目标价。读者真正应该学习的是：他如何把一个小公司放进多个大型下游技术路线里，然后把公开证据和推断路径分层。

## 七、第三章：Neocloud，不是“谁有 GPU”，而是谁的融资结构更干净

5 月以来第二个很重要的主题是 AI 云和 neocloud，但 Serenity 的切入点不是简单看数据中心扩张，而是看融资质量。

最典型的对比是 `$NBIS` 和 `$IREN`。他把 `$NBIS` 看作相对优质的 AI infrastructure / GPU cloud 标的，理由包括大客户、融资结构、可转债和战略投资质量。他把 `$IREN` 当作反面案例，核心批评集中在大规模 ATM、股权稀释和每次反弹都可能面临结构性抛压。

这个框架对读者很有启发。AI 基建公司有时会签大合同、买 GPU、扩数据中心，看上去成长很快，但普通股东最终能不能受益，取决于资本开支如何融资。如果依靠持续增发、昂贵债务或对散户不友好的 ATM，收入增长可能被股权稀释吞掉。

Serenity 对 neocloud 的排序大致围绕三点：

第一，客户是谁。微软、Meta、Google、Amazon 这种 hyperscaler 背书和现金流质量，和现金流不稳定的 AI lab 或投机性客户不是一个层级。

第二，融资来自哪里。战略投资、可转债、客户背书和较低成本资金优于高息债务和大规模 open-market ATM。

第三，披露质量如何。它反复强调 GAAP gross margin、SBC、债务利息、ATM 和 float dynamics，而不是只看公司宣传的 non-GAAP 指标。

这部分的风险在于，融资结构本身也会变化，合同执行和电力、水、芯片交付、租赁条款都需要持续核验。频道里的观点很适合做风险 checklist，但不能替代公司 filings。

## 八、第四章：存储、HBM、NAND 和韩国资产

存储是 5 月以来从 CPO 主线外溢出来的另一条重要线索。Serenity 的基本观点是：市场仍然容易把 memory 当作周期品，但 AI 基础设施可能改变 DRAM、HBM、NAND 的周期强度和持续性。

这个主题里，`$MU`、`$EWY`、Samsung、SK Hynix、`$SNDK` 被反复提及。`$EWY` 不是单一公司，而是韩国市场和存储巨头的 ETF 暴露，Serenity 曾用它表达对韩国存储链的方向性和波动率看法。`$SNDK` 则与 NAND 价格、盈利弹性和市场对 forward earnings 的低估有关。

6 月 7 日之后，公开镜像显示他继续围绕 Nvidia CEO 对 memory shortage 和 silicon photonics supply volume 的评论，强化 `$MU`、`$EWY`、`$SIVE`、`$SOI` 之间的链条。这里的逻辑是：AI 基建越扩大，GPU 之外的内存、光互连和硅光基板也越可能成为长期供给约束。

但这个主题要特别谨慎。存储价格确实可能因 AI 需求上行，但存储行业仍有供给周期、资本开支周期和价格波动。把“AI 打破周期”作为长期判断可以研究，但不应忽略 DRAM / NAND 行业历史上的剧烈均值回归。

## 九、第五章：800V DC、电力基础设施和功率半导体

5 月下旬，频道明显增加了对 800V DC、power semi、SiC、GaN、变压器和电网的讨论。这条线的起点是 AI 数据中心的功率密度提升。如果 GPU 机柜、电源架构和数据中心配电向更高电压、更高效率演进，那么功率器件、SiC / GaN、模块、电源管理、变压器、开关设备和电网基础设施都会被重新定价。

这条主线中，`$FLNC`、`$NVTS`、`$WOLF`、`$XFAB`、`$POWI`、`$HPS.A`、`$AMSC` 等名字或方向被提及。6 月 8 日，镜像和归档都显示他在整理粉丝推荐的 800V DC 相关标的清单，并强调这些并非他的正式推荐。

这点非常重要。众包清单的作用是扩大研究面，不是形成买入结论。一个名字进入清单，只说明它可能与 800V DC 或电力架构相邻；真正进入高置信度组合，还需要确认产品暴露、客户、订单、产能、毛利、估值和融资结构。

从方法论上看，800V DC 是 Serenity 框架的自然延伸：下游是 AI 数据中心，往上追就是电力转换、配电、功率器件、热管理和电网设备。这个方向值得研究，但 5 月以来多数内容仍在“发现和筛选阶段”，不如 CPO/SIVE 主线成熟。

## 十、第六章：机器人、实体 AI 与中国供应链

机器人方向在 5 月中旬开始升温。典型帖子包括 5 月 12 日向 followers 众包 humanoid exposure，以及后来发布 humanoid exposure 清单。这里他寻找的是类似早期 `$RKLB` 的高弹性机器人纯度标的。

这条线后来延伸到中国供应链，尤其是 LeaderDrive / 绿的谐波（688017）。公开镜像 6 月 9 日显示，他继续讨论 688017，强调自己没有持有该股、主要因为外国人难以购买，并表示仍会继续研究新机会。6 月 8 日和 6 月 9 日的镜像内容也显示，他把 LeaderDrive 放在 humanoid reducer、actuator、joint 和核心机器人零部件的供应链位置中讨论。

这条线的底层逻辑是：机器人不是只有 AI 模型，实体量产需要减速器、电机、执行器、稀土磁材、结构件、传感器、LiDAR、电池和制造能力。如果美国软件和模型领先，但关键 hardware / actuator / materials 依赖中国，那么机器人供应链的投资机会可能在中国、日本、欧洲和台湾，而不只在美国本体公司。

但机器人主题目前的风险也更高。许多 humanoid 订单、量产节奏、单位价值量、供应商份额和客户验证仍不透明。中国 A 股和港股的情绪波动也很强。对这条线，最合适的使用方式是拿它当供应链研究地图，而不是看到媒体报道或涨停就追。

## 十一、第七章：玻璃基板、先进封装、台湾和日本供应链

除 CPO、存储、电力和机器人之外，5 月以来还有一个横向主题：先进封装和亚洲供应链。

玻璃基板方向围绕 `$LPK`、SKC Absolics、Samsung Electro-Mechanics、Sumitomo Chem、GCS / glass core substrate 等展开。Serenity 的核心判断是：随着 AI GPU、ASIC、CPO 和 HBM 对高端封装提出更高要求，玻璃基板可能成为下一个高增长环节；设备、材料和工艺 know-how 可能比传统 ABF 叙事更有弹性。

台湾方向围绕 Shunsin、FOCI、Xintec、Win Semi、MSSCorps 等展开。它把台湾看作 CPO 代工、封装、检测和供应链落地的重要区域。日本方向则更多对应 chemicals、substrates、red phosphorus、glass 和各种细分材料。欧洲方向集中在 lasers、machines、SOI、XFAB、SIVE、LPK 等高技术小公司。

这个章节有一个很有价值的观察：Serenity 的全球供应链地图不是“美国科技公司赢了，所以只买美国科技股”。他的框架更接近：美国是最终 AI 资本开支和应用出口，但真正的 upstream bottleneck 可能分布在台湾、韩国、日本、欧洲和中国。

这也是读者最应该吸收的部分。AI 投资如果只停在 Mag7，很容易错过上游链条；但如果上游链条研究不扎实，也很容易买到低流动性、高估值、高波动的故事股。

## 十二、可靠性校准：哪些能信，哪些必须降权

分析这个频道，最关键的不是判断它“神”或“不神”，而是分层。

更硬的证据包括公司公告、年报、财报电话会、客户或伙伴页面、指数纳入、持仓披露、订单和收入确认。这些可以作为研究起点，但仍要回原始披露核验。

合理推断包括客户链路、供应商映射、产品路线、量产时间窗口和多跳 BOM 推理。这是 Serenity 的核心优势，但它仍然是推断。推断可以用于形成假设，不能直接当成事实。

市场结构包括 ATM、可转债、被动资金、短仓、流通股、融资质量和客户信用。这个维度经常被普通投资者忽略，但对高增长小盘股非常关键。

社群噪音包括粉丝数、订阅数、媒体报道、众包清单、短期涨跌归因和与其他账号的争论。这些信息有分发价值，但不能当作买入依据。

未验证项包括自报收益、私信线索、NDA 客户路径、删除内容、订阅内容和未公开持仓。公开归档的 track-record 文件也明确提示，自报收益未验证，公开 feed 存在赢家选择偏差。

![风险校准](/images/posts/serenity-aleabitoreddit-analysis/serenity-risk-calibration.svg)

我的建议是，把这个频道当成供应链雷达，而不是交易系统。它能告诉你“哪里可能有未被市场充分理解的上游节点”，但不能替你完成财报、估值、流动性、仓位和风险控制。

## 十三、代表性帖子和章节索引

下面这张表不是逐条复述，而是把 5 月以来最能代表频道结构的公开帖子按主题标出来。普通帖子只做摘要，避免复制长文原文。

| 日期 UTC | 链接 | 章节意义 |
|---|---|---|
| 2026-05-01 | [2050237030828052862](https://x.com/aleabitoreddit/status/2050237030828052862) | 光子链行情反馈，`$AXTI`、`$AAOI` 等前期 thesis 的延续。 |
| 2026-05-05 | [2051593478245851178](https://x.com/aleabitoreddit/status/2051593478245851178) | CPO TAM 扩张叙事，是 5 月 CPO 主线升温的代表。 |
| 2026-05-07 | [2052494142765441301](https://x.com/aleabitoreddit/status/2052494142765441301) | Bearish `$IREN`，用融资结构和 ATM 风险反推 neocloud 质量。 |
| 2026-05-10 | [2053377238532329611](https://x.com/aleabitoreddit/status/2053377238532329611) | 玻璃基板价值链研究，涉及设备、材料和先进封装。 |
| 2026-05-12 | [2054183097470775339](https://x.com/aleabitoreddit/status/2054183097470775339) | 众包 humanoid exposure，机器人供应链章节的起点。 |
| 2026-05-12 | [2054335940026573222](https://x.com/aleabitoreddit/status/2054335940026573222) | 发布 humanoid exposure 清单，覆盖传感、执行器和减速器等方向。 |
| 2026-05-13 | [2054524864866980010](https://x.com/aleabitoreddit/status/2054524864866980010) | `$NBIS` earnings 和 AI cloud 融资质量框架。 |
| 2026-05-14 | [2054868760629272850](https://x.com/aleabitoreddit/status/2054868760629272850) | `$SIVE` 年报分析，强调 CPO、pluggable transceiver 和 pipeline。 |
| 2026-05-15 | [2055401446397690311](https://x.com/aleabitoreddit/status/2055401446397690311) | 自报收益和影响力代表帖，适合放在校准章节而非当作投资证据。 |
| 2026-05-17 | [2056036968220528767](https://x.com/aleabitoreddit/status/2056036968220528767) | `$KRUS` / Kura Sushi 高传播帖子，说明频道也会覆盖事件型消费股叙事。 |
| 2026-05-19 | [2056691097594925522](https://x.com/aleabitoreddit/status/2056691097594925522) / [Article](https://x.com/i/article/2056688641448321024) | 5 月以来唯一 X Article，系统化 `$SIVE` / CPO laser chokepoint thesis。 |
| 2026-05-20 | [2056891308934148253](https://x.com/aleabitoreddit/status/2056891308934148253) | 把 humanoid mass production 的关键约束指向中国供应链和材料。 |
| 2026-05-24 | [2058577885754163382](https://x.com/aleabitoreddit/status/2058577885754163382) | 众包 NVDA 800V DC / power semi 候选，是电力主线筛选阶段代表。 |
| 2026-06-03 | [2062079425475473595](https://x.com/aleabitoreddit/status/2062079425475473595) | Ayar / Nvidia NVLink Fusion 后，把 `$SIVE` 映射到 Nvidia CPO 生态链。 |
| 2026-06-07 | [2063583856025108986](https://x.com/aleabitoreddit/status/2063583856025108986) | Nvidia CEO memory shortage 相关读法，强化 `$MU`、`$EWY` 和硅光链。 |
| 2026-06-09 | [2064172972102070714](https://x.com/aleabitoreddit/status/2064172972102070714) | 镜像确认的归档后新增内容，强调免费分享、不要盲从和自担研究责任。 |

## 十四、如果要长期跟踪，应该看什么

第一，看 `$SIVE` thesis 是否从 pipeline 和客户路径进入实际订单、volume ramp、收入确认和毛利改善。所有 CPO 叙事最终都要回到财务报表。

第二，看 `$AAOI`、`$LITE`、`$COHR`、`$MRVL`、Jabil、Ayar、GFS 等公开信息是否继续印证 CPO 量产时间线。下游节奏如果推迟，上游小盘弹性会被放大反向波动。

第三，看 `$SOI`、`$AXTI`、`$IQE` 等上游材料和基板是否真正获得定价权，而不是只获得叙事关注。

第四，看 neocloud 公司融资结构是否变化。大规模 ATM、债务利息、SBC 和客户信用恶化，可能比收入增速更重要。

第五，看 800V DC、电力和机器人供应链是否从众包清单进入公司披露、订单、资本开支和产业标准。现在很多内容还在 early discovery 阶段。

第六，看频道自身的错误修正。一个研究账号真正的质量，不只在于说中过多少，更在于 thesis 错时是否能快速降权、承认误差、更新路径。

## 结论

2026 年 5 月以来，@aleabitoreddit 最值得总结成三句话。

第一，它的主线是上游瓶颈，不是泛 AI。CPO、硅光、激光、InP、SOI、封装、检测、功率半导体、存储和机器人硬件，都是从 AI 资本开支向上游拆链得到的结果。

第二，它的核心资产是方法论，不是任何单一 ticker。`$SIVE` 是样本期最重要的研究对象，但真正可迁移的是“从 downstream capex 追到 upstream chokepoint，再用资本结构和证据质量过滤”的框架。

第三，它的最大风险是高置信推断被社群传播放大。读者必须把事实、推断、众包和自报收益分层。最好的使用方式是把它当研究雷达，拿到线索后自己回到原始公告、财报、订单、产能和估值模型里验证。

如果用一句话评价：这是一个少见的高密度 AI 半导体供应链研究流，但只适合做研究起点，不适合做交易终点。

## 参考资料

- [Serenity X 账号：@aleabitoreddit](https://x.com/aleabitoreddit)
- [yan-labs/serenity-aleabitoreddit 公开归档](https://github.com/yan-labs/serenity-aleabitoreddit)
- [X Articles Supplement](https://github.com/yan-labs/serenity-aleabitoreddit/blob/main/serenity-aleabitoreddit/references/articles.md)
- [Methodology — the reusable lens](https://github.com/yan-labs/serenity-aleabitoreddit/blob/main/serenity-aleabitoreddit/references/methodology.md)
- [Track Record — dated calls & calibration](https://github.com/yan-labs/serenity-aleabitoreddit/blob/main/serenity-aleabitoreddit/references/track-record.md)
- [serenitysaid.com 公开镜像](https://serenitysaid.com/)
- [2026-05-19 X Article：SIVE - The CPO Laser Chokepoint for Hyperscalers](https://x.com/i/article/2056688641448321024)
