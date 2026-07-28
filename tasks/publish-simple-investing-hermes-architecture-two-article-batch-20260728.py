from __future__ import annotations

import html
import json
import re
import shutil
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote


ROOT = Path("/tmp/hermes-video-publish")
SITE = "https://zcxggmu.github.io"
DATE = "2026-07-19"
BASE_DT = datetime(2026, 7, 19, 23, 55, tzinfo=timezone(timedelta(hours=8)))
PREV_EXISTING_URL = "/2026/modern-single-men-happiest-generation-solitude-freedom/"
PREV_EXISTING_TITLE = "现代单身男性为什么可能是最快乐的一代：独处、自由与内在秩序"
SCRIPT_NAME = "publish-physical-ai-three-article-batch.py"
MANIFEST_NAME = "publish-physical-ai-three-article-batch-changed-files.json"
CHANGED: set[str] = set()


@dataclass(frozen=True)
class Post:
    source_id: str
    slug: str
    title: str
    desc: str
    category: str
    series: str
    tags: list[str]
    minutes: int
    body: str
    cover_kicker: str
    cover_line: str
    cover_theme: tuple[str, str, str]
    duration: float
    segments: int
    chars: int

    @property
    def url_path(self) -> str:
        return f"/2026/{self.slug}/"

    @property
    def full_url(self) -> str:
        return SITE + self.url_path

    @property
    def cover(self) -> str:
        return f"/images/posts/{self.slug}/cover.svg"


BODY_AI_THIRD_WAVE = """
<p><img src="/images/posts/ai-third-wave-physical-ai-vla-world-model-investment-map/cover.svg" alt="AI 第三浪：物理 AI 如何从屏幕走向真实世界"></p>
<p>AI 的前两轮浪潮，主要发生在屏幕之内。第一轮是感知式 AI，让机器能够识别图像、理解语音、完成基础的模式判断；第二轮是生成式 AI，让机器能够写文字、生成图片和视频、辅助代码与内容生产。但这两轮浪潮的核心，仍然是信息世界里的效率提升。</p>
<p>真正的第三浪，是物理 AI。它的目标不是让机器停留在对话框里，而是让智能进入真实环境，感知三维空间、理解任务目标、预测物理变化，并通过机器人、自动驾驶、工业设备和各类智能终端完成现实世界里的动作。</p>
<p>物理 AI 的关键变化在于：AI 不再只是“理解世界”，而是开始“改变世界”。它对应的不是单一产品，而是一整套跨越基础模型、世界模型、仿真训练、传感器、执行器、本体制造和场景交付的产业系统。</p>

<h2 id="three-waves">AI 的三次跃迁：从识别、生成到行动</h2>
<p>第一波 AI 的核心是感知。人脸识别、语音交互、智能音箱、图像识别等应用，本质上都是让机器在某个维度上“看见”或“听见”。这类能力非常重要，但它解决的是信息输入和模式识别问题。</p>
<p>第二波 AI 的核心是生成。大模型、聊天机器人、AI 绘画、AI 视频、代码助手、办公自动化工具，让机器具备了更强的知识组织和内容生产能力。它让 AI 从“识别工具”升级为“生产工具”，但多数能力仍然锁在数字世界中。</p>
<p>第三波 AI 的核心是行动。物理 AI 要把感知、语言、推理、规划和控制统一起来，让智能系统能够在复杂物理环境中执行任务。人形机器人、自动驾驶平台、工业自动化设备，是这一阶段最典型的载体。</p>
<p>这也是理解产业空间的关键：数字 AI 提升的是信息生产力，物理 AI 对应的是制造、物流、交通、医疗、农业、能源、家政、巡检和现场服务等真实劳动市场。后者的规模远大于纯软件世界，也更难被少数应用垄断。</p>

<h2 id="definition">什么是物理 AI</h2>
<p>物理 AI 是具备在真实物理环境中感知、理解、推理和执行能力的智能系统。它不仅要看懂图像、听懂指令，还要理解空间、重量、摩擦、碰撞、遮挡、材质、运动轨迹和安全边界。</p>
<p>一台传统工业机器人，只要环境固定、工位固定、动作固定，就能高效运行。但一旦任务改变、物体位置改变、场景发生扰动，它往往需要重新编程和调试。物理 AI 要解决的，就是让机器具备一定泛化能力，在真实环境里根据目标和反馈调整动作。</p>
<p>这类系统通常包含三类能力。第一是多模态感知，能够处理视觉、语言、触觉、力觉、位置和环境信息；第二是任务理解与规划，能够把自然语言目标拆成可执行步骤；第三是动作控制与反馈，能够把计划转化为机械臂、底盘、关节、电机和执行器的动作，并根据结果持续修正。</p>

<h2 id="vla">VLA：视觉、语言与动作的统一模型</h2>
<p>物理 AI 当前最重要的技术路线之一，是 VLA，也就是视觉、语言、动作模型。它在视觉语言模型的基础上，把动作也当成一种模态来处理，让模型不仅能看懂场景、理解语言，还能直接输出动作指令。</p>
<p>过去的大语言模型处理文本 token，视觉语言模型处理图像和文本，VLA 则进一步引入动作 token，把机械臂、电机、夹爪、移动底盘等执行指令编码进统一模型中。这样，机器人就有机会从“先识别、再规则控制”的传统架构，走向端到端的动作生成。</p>
<p>VLA 的进展很快，训练分布内的任务成功率不断提升。但它的瓶颈也非常清楚：一旦换到新任务、新场景、新物体，成功率可能明显下降。家庭场景训练好的模型，放到工业制造环境中未必可用；仿真环境表现好，迁移到真实世界仍然可能失败。</p>
<p>原因在于，VLA 很容易学习图像、语言和动作之间的表面对应，却不一定真正理解物理后果。它可能知道杯子在哪里，却不知道装满水的杯子不能倾斜；它可能知道箱子可以推动，却不理解摩擦、重心和碰撞会怎样影响结果。</p>

<h2 id="world-model">世界模型：给机器人注入“想象力”</h2>
<p>为了解决 VLA 缺乏前瞻推理的问题，世界模型成为物理 AI 的核心补充。世界模型的本质，是让机器学习环境如何变化：如果执行某个动作，下一秒会发生什么；如果碰到某个物体，物体会滑动、倾斜、变形，还是翻倒。</p>
<p>VLA 更像反应式系统，根据当前观测直接输出动作；世界模型则像内置物理引擎，提前模拟动作后果，验证计划是否可行。一个成熟的物理 AI 架构，未来很可能不是单独依靠 VLA，而是 VLA 与世界模型形成闭环。</p>
<p>世界模型在架构中承担四个角色。第一是规划器，预测未来状态，帮助系统选择更可靠的路径。第二是动作模型，把环境动态纳入动作生成，避免动作只符合图像而不符合物理。第三是合成器，生成大量可训练、可评测的观测和动作轨迹。第四是安全沙盒，让策略在虚拟环境中试错，降低真实设备损耗和安全风险。</p>
<p>这意味着，物理 AI 的核心突破，不只是机器人本体更像人，也不是机械臂更灵活，而是智能系统开始具备对物理后果的预测能力。</p>

<h2 id="training">训练场：仿真、合成数据与真实数据闭环</h2>
<p>物理 AI 最大的约束之一是数据。文本、图片、代码可以从互联网规模化获取，但高质量机器人操作数据极其昂贵。真实机器人每一次试错都需要设备、场地、人力和时间，还可能造成损耗。</p>
<p>因此，仿真平台和合成数据会成为物理 AI 的训练场。机器人可以在虚拟环境中练习抓取、搬运、避障、装配和巡检，自动驾驶系统可以在仿真道路中面对极端天气、突发行人和复杂交通场景，工业设备可以在数字孪生工厂中测试不同工况。</p>
<p>仿真的价值不只是便宜，更在于可控、可重复、可评测。真实世界中的长尾危险场景很难大量收集，但仿真可以生成并反复测试。未来真正有壁垒的平台，很可能不是只提供一个炫目的 3D 世界，而是能够把真实数据、合成数据、评测体系和模型训练连接成闭环。</p>

<h2 id="applications">三大落地场景：机器人、自动驾驶与工业自动化</h2>
<p>物理 AI 的应用生态非常庞大，但最清晰的方向主要有三类。</p>
<p>第一类是人形机器人和具身系统。它们需要多模态感知、运动控制、抓取操作、场景理解和任务规划。短期内，真正可落地的未必是全能家庭管家，而是工厂、仓库、园区、巡检、搬运、分拣、导览和特种作业等边界更清晰的场景。</p>
<p>第二类是自动驾驶和无人运载设备。自动驾驶本质上也是物理 AI：车辆要感知道路、预测轨迹、规划路径并控制车辆。它拥有真实数据回流、商业模式明确、政策逐步开放和场景相对标准化等优势，是物理 AI 中较早形成规模化验证的方向。</p>
<p>第三类是工业自动化与智能装备。制造、仓储、物流、质检、预测性维护、工业巡检、柔性装配等场景，付费意愿更强、ROI 更容易计算、环境更结构化，也更适合早期物理 AI 落地。</p>

<h2 id="market">产业空间：从数字世界走向实体经济</h2>
<p>物理 AI 的市场规模之所以被反复强调，是因为它面向的是现实世界中的劳动和资本开支。制造、物流、交通、医疗、农业、能源和基础设施运维，都不是单纯的软件市场，而是长期存在大量人力、设备、场地和安全成本的行业。</p>
<p>一旦 AI 能替代其中一部分现场操作、重复劳动和危险岗位，它带来的不是简单的效率优化，而是生产组织方式的变化。自动驾驶替代司机成本，工业机器人替代危险巡检，人形机器人参与搬运和分拣，医疗机器人辅助康复和手术，农业设备自动驾驶和自动喷灌，都会形成实际现金流。</p>
<p>北美目前在基础模型、芯片、仿真平台和头部企业上仍占主导；亚太地区则拥有制造能力、供应链、机器人量产和硬件降本优势。中国的机会不一定在单点模型全球第一，而在把模型、硬件、供应链、场景和工程交付结合起来。</p>

<h2 id="investment-map">投资图谱：不要只盯机器人外壳</h2>
<p>物理 AI 的投资不能只看机器人本体。真正的产业链至少包含五层：基础模型与世界模型、数据与仿真平台、端侧芯片与传感器、机器人本体与执行器、场景运营与服务闭环。</p>
<p>基础模型决定大脑能力，世界模型决定物理理解和规划能力，仿真平台决定训练效率，端侧芯片决定实时响应，本体制造决定成本和可靠性，场景服务决定商业化收入。任何单一环节都不足以解释整个产业。</p>
<p>更稳妥的思路，是寻找能够跨场景服务大量应用的基础设施公司，以及能够在具体场景中跑出 ROI 的本体和服务公司。前者可能成为物理 AI 时代的开发平台，后者则通过真实订单验证需求。</p>

<h2 id="risks">风险：路线未收敛，商业化仍要算账</h2>
<p>物理 AI 的长期空间很大，但早期风险同样明显。首先，技术路线仍未完全收敛。VLA、世界模型、端到端、分层控制、隐空间模型和仿真强化学习都在演进，过早押注单一路线，风险很高。</p>
<p>其次，仿真与现实存在差距。摩擦、材质、光照、遮挡、柔性物体、力反馈和设备误差，都可能让合成数据训练出的模型在真实场景中失效。物理 AI 也会有自己的“幻觉问题”，只是这种幻觉不再表现为说错话，而是表现为动作失败和安全事故。</p>
<p>最后，商业化节奏可能反复。机器人演示成功，不等于工厂可以连续运行；单次任务完成，不等于客户愿意付费；远期市场巨大，不等于短期估值合理。投资上必须同时看长期产业方向和短期交易节奏。</p>

<h2 id="conclusion">结论：第三浪的核心，是让智能进入物理世界</h2>
<p>物理 AI 是 AI 从信息生产力走向物理生产力的关键跃迁。它不是某一个机器人概念，也不是某一次大会上的技术口号，而是一套重新组织真实世界劳动、设备、数据和场景的产业体系。</p>
<p>未来真正重要的公司，可能不是单纯做最酷外形的机器人，而是能够定义模型、数据、仿真、评测、芯片、本体和场景闭环的企业。谁能让机器在现实世界里稳定工作，谁就有机会掌握第三浪的核心价值。</p>
"""


BODY_NEXT_CUDA = """
<p><img src="/images/posts/physical-ai-infrastructure-next-nvidia-cuda-world-model/cover.svg" alt="物理 AI 元年：谁会成为下一个英伟达与 CUDA"></p>
<p>AI 产业正在从数字世界进入物理世界。过去几年，生成式 AI、AI Coding、智能体和多模态模型改变了内容生产、软件开发和知识工作，但这些变化大多仍然发生在屏幕之内。接下来的核心问题是：当 AI 进入机器人、自动驾驶、无人设备、工业系统和智能终端，谁会成为物理 AI 时代的基础设施？</p>
<p>数字 AI 时代，英伟达通过 GPU 和 CUDA 生态成为算力基础设施的核心。物理 AI 时代，也会需要类似的底层平台：世界模型、仿真环境、合成数据、评测标准、动作模型、端侧芯片、开发框架和场景数据闭环。谁能定义这些基础设施，谁就可能拥有新的生态壁垒。</p>

<h2 id="digital-to-physical">从数字 AI 到物理 AI</h2>
<p>过去几年可以分成三个阶段。第一阶段是数字 AI 1.0，以对话框、文本生成、图片生成和知识问答为代表。它提升的是内容生产和信息处理效率。</p>
<p>第二阶段是数字 AI 2.0，以推理模型、AI Coding 和智能体为代表。AI 不再只是回答问题，而是开始拆解任务、调用工具、修改代码、运行测试、处理复杂流程。它开始接近软件世界中的自动执行者。</p>
<p>第三阶段是物理 AI。它要把 AI 的理解、推理和任务执行能力嵌入机器人、自动驾驶、无人车、无人机、工业设备、物流系统和各类智能终端。AI 从信息生产力走向物理生产力，这才是更大的市场。</p>
<p>数字 AI 替代或增强的是脑力劳动，尤其是白领、开发者、内容创作者和知识工作者；物理 AI 面向的是制造、物流、运输、建筑、能源、零售、农业、医疗护理、家庭服务和基础设施运维。这些行业承载了更大的 GDP、更重的人工成本和更明确的效率提升空间。</p>

<h2 id="application-pattern">数字 AI 集中，物理 AI 分散</h2>
<p>数字 AI 的应用层容易集中。一个聊天机器人、一个代码助手、一个办公工具，只要体验明显领先，就可以通过网页和 API 快速服务全球用户。用户在不同头部模型之间切换，最终份额往往集中在少数平台。</p>
<p>物理 AI 的应用层会更分散。汽车工厂、3C 产线、仓储物流、矿山巡检、医院护理、家庭厨房、农业采摘、低空无人机、自动驾驶卡车，它们对机器人形态、传感器、本体结构、动作能力、安全标准和交付方式的要求完全不同。</p>
<p>数字 AI 可以用一个网页服务全球，物理 AI 必须深入不同产业、不同国家、不同客户现场。工业机器人要懂工艺流程，仓储机器人要懂物流调度，医疗机器人要满足监管，自动驾驶要适应道路和法规。通用智能很重要，但现实世界首先是无数垂直场景。</p>
<p>因此，物理 AI 的基础设施层反而更重要。应用分散意味着上层难以被一两家公司完全垄断；但如果某家公司掌握了世界模型、仿真环境、合成数据、评测体系和开发框架，就可以服务大量分散应用。</p>

<h2 id="next-cuda">下一个 CUDA 可能不是软件工具，而是数据与仿真标准</h2>
<p>CUDA 的价值不只是一个编程接口，而是围绕 GPU 形成了开发者、模型公司、云厂商和应用生态。它让算力被高效调用，也让英伟达的硬件优势变成生态壁垒。</p>
<p>物理 AI 时代，同样需要一个底层生态：统一的数据生成体系、仿真环境、评测标准、动作模型、世界模型和部署框架。机器人公司、自动驾驶公司、无人设备公司和工厂智能化公司，都需要在这个体系上训练、测试和部署自己的模型。</p>
<p>如果某个平台能够持续提供高质量合成数据、真实场景还原、物理正确的仿真、动作对齐、模型评测和部署工具，它就不只是软件供应商，而可能成为物理 AI 的基础设施入口。</p>

<h2 id="model-economics">大模型价值公式：智能密度乘以 Token 吞吐量</h2>
<p>理解物理 AI 之前，必须理解大模型竞争正在从“榜单排名”走向“生产效率”。过去市场容易看参数规模、排行榜和融资估值，但这些指标越来越不够用。更关键的是模型输出真实价值的能力，以及这种能力能否规模化提供。</p>
<p>一个更接近商业本质的公式是：大模型企业价值等于智能密度乘以 Token 吞吐量。智能密度指的是每单位输出能否完成高价值任务，比如写出可运行代码、完成法律条款分析、生成商业视频、执行金融研究或替代真实劳动。Token 吞吐量则代表模型服务用户、企业任务和 API 调用的规模。</p>
<p>这会引出两条路线。第一条是智能路线，重点在复杂推理、代码能力、工具调用、企业任务、法律金融分析、办公室自动化和行业智能体。它更接近生产力工具，企业付费意愿更强。</p>
<p>第二条是想象路线，重点在视频、声音、音乐、图片、角色陪伴、游戏资产、广告创意和娱乐消费。它更接近内容生产和体验消费，C 端传播更快。头部模型公司未来大概率不会只做一条线，而会同时覆盖企业生产力、内容消费和开发者生态。</p>

<h2 id="ai-native-org">AI 原生组织：人才密度比团队规模更重要</h2>
<p>AI 公司之间的竞争，不只是模型和算力的竞争，也是组织结构的竞争。传统科技公司依赖大规模团队、分层管理和成熟流程，但 AI 行业的模型架构、推理架构、产品形态、用户需求和算力成本都在以月为单位变化。</p>
<p>真正高效的 AI 原生组织，通常更扁平、更年轻、更技术密集。核心研究员、工程负责人、产品负责人和 CEO 之间可以快速沟通，模型训练方向不对就立即调整，产品反馈不好就快速迭代，新技术路线出现就组织小团队验证。</p>
<p>大模型公司不是人越多越强。真正决定模型突破、架构创新和产品方向的，往往是少数顶尖人才。其他工程、数据、产品、评测和交付团队围绕关键任务形成高密度协作。人才密度、协作效率和目标一致性，往往比团队规模更重要。</p>

<h2 id="embodied-system">具身智能需要大脑、小脑和端侧芯片</h2>
<p>具身智能与传统机器人最大的不同，是它不是单纯执行预设程序，而是与环境持续交互，通过感知、理解、决策、操作和反馈不断学习。它既需要身体，也需要大脑；既需要传感器，也需要模型；既需要本体制造能力，也需要数据闭环和端侧推理能力。</p>
<p>首先是感知能力。机器人要识别物体位置、形状、材质、姿态和运动状态；无人车要理解道路、车辆、行人、交通灯和障碍物；无人机要感知高度、风向、地形和风险；工业机器人要理解零部件、夹具、产线节拍和缺陷特征。</p>
<p>其次是大脑和小脑。大脑负责理解任务、规划步骤、调用知识和做高层决策；小脑负责动作控制、运动协调、逆控反馈和实时调整。复杂推理可以在云端，避障、抓取、力反馈和安全判断必须在端侧完成。</p>
<p>最后是端侧芯片。物理世界要求毫秒级响应，机器人和无人设备不能把所有计算交给云端。感知芯片处理摄像头、雷达和触觉传感器，推理芯片运行视觉模型和动作模型，运控芯片控制电机、关节、底盘和执行器。</p>

<h2 id="china-advantage">中国的机会：供应链、场景和产业组织能力</h2>
<p>具身智能具有天然的国家战略属性。它不是一个孤立创业赛道，而是国家资本、产业资本、大厂生态、制造供应链和地方政府共同推动的战略产业。</p>
<p>中国的优势不一定是单点模型全球第一，而是完整制造供应链、大规模应用场景和强产业组织能力。电机、减速器、关节、传感器、摄像头、激光雷达、电池、电控、结构件、芯片模组、整机装配和测试能力，都可以从新能源汽车、消费电子、无人机、工业自动化和智能硬件体系中迁移。</p>
<p>物理 AI 需要大量真实场景验证，而中国拥有汽车、3C、光通信、物流、零售、农业、医疗和家庭服务等多样化场景。场景越多，数据越多，迭代越快。对物理 AI 来说，数据和场景往往比单纯算法更重要。</p>
<p>此外，地方政府、产业基金、国资平台、大厂生态和制造企业能够提供资金、试点场景和客户资源。这种产业组织能力，有助于新技术从概念验证进入规模化应用。</p>

<h2 id="world-model-2">从 VLA 到世界模型 2.0</h2>
<p>过去一到两年，VLA 是具身智能的重要路线。它把视觉、语言和动作结合起来，推动机器人从传统控制走向大模型驱动。但随着规模化落地临近，VLA 的瓶颈开始暴露。</p>
<p>第一，缺乏物理验证。视觉语言模型擅长识别和描述，却不一定理解因果和动力学。第二，动作学习效率不高。语言 token 是离散符号，动作是连续控制，细微偏差就可能导致抓取失败或安全事故。第三，数据需求巨大。高质量真机操作数据昂贵，难以像互联网文本那样规模化获取。</p>
<p>世界模型主导的具身智能 2.0，核心路径是物理世界预训练、动作对齐和强化学习。模型先通过视频、仿真、动作轨迹和物理交互数据学习物体如何移动、碰撞如何发生、重力如何作用；再把人类动作、机器人动作和任务目标对齐；最后通过试错、奖励和反馈学习长周期任务策略。</p>
<p>相比 VLA，世界模型最大的优势是数据效率和泛化能力。因为它先学到了大量物理规律，动作学习不再完全依赖昂贵真机数据。这可能是具身智能迎来真正拐点的关键。</p>

<h2 id="schools">世界模型的三条路线</h2>
<p>世界模型大致有三类方向。第一类是物理正确派，追求 3D 一致性、物理一致性和动作准确性，强调仿真环境与真实世界高度一致。这类路线适合自动驾驶、机器人操作、工业仿真和安全评测。</p>
<p>第二类是隐空间派，不一定追求可视化效果，而是强调机器内部表征和预测效率。模型在低维隐空间中学习世界状态、动作后果和环境变化，更适合具身基础模型和强化学习。</p>
<p>第三类是 3D 世界派，更强调生成可交互的三维空间，服务游戏、影视、虚拟现实、内容创作和沉浸式环境。它与物理 AI 有交集，但目标不完全相同。</p>
<p>未来的平台可能融合三者：既要物理正确性，也要高效隐空间表征，还要能够生成可交互 3D 世界。谁能把这三类能力合并进统一平台，谁就更接近物理 AI 的基础设施入口。</p>

<h2 id="data-pyramid">数据金字塔：物理 AI 的新 CUDA</h2>
<p>具身智能的数据需求远超自动驾驶。真实机器人不可能短期部署到足够规模，因此必须依赖数据金字塔。</p>
<p>最顶层是真实机器人数据，来自真实场景、真实动作和真实反馈，最宝贵但占比最小。中间层是仿真合成数据，通过仿真引擎、数字孪生、物理建模和生成式 AI 构建大量可交互场景。底层是互联网和人类视频数据，包含大量人类动作、工具使用、物体交互和生活场景。</p>
<p>这也是数据基础设施可能成为新 CUDA 的原因。CUDA 定义了 GPU 计算生态，而物理 AI 时代，谁能定义高质量数据生成、仿真训练、动作对齐、评测标准和物理世界建模工具，谁就有可能成为机器人训练、部署和评测的标准平台。</p>

<h2 id="landing">落地路径：先工业，再商业，最后家庭</h2>
<p>具身智能不可能一开始就进入最复杂的家庭场景，也不会马上替代所有一线工人。更现实的路径，是从好算账、任务边界清晰、容错空间较大的场景开始。</p>
<p>工业场景是最好的起点之一。工厂、仓库、园区、数据中心和产线相对结构化，任务重复，客户付费意愿强，ROI 容易计算，安全边界也更容易设计。机器人可以先承担巡检、搬运、分拣、质检、装配辅助等任务。</p>
<p>商业场景也会先从导购、咨询、巡逻、配送等轻操作任务开始。家庭场景长期空间很大，但短期难度最高。每个家庭环境不同，物品摆放不标准，老人儿童安全要求高，隐私和责任边界复杂，因此更可能先从清洁、厨房、食品加工、简单整理等局部任务切入。</p>

<h2 id="autonomous-driving">自动驾驶是物理 AI 最成熟的商业化样板</h2>
<p>自动驾驶已经是物理 AI 中最大规模落地的市场之一。车辆感知道路、预测轨迹、规划路径、控制方向盘和刹车，本质上就是感知、决策和行动的物理 AI 系统。</p>
<p>世界模型在自动驾驶中已经体现价值。它可以从真实摄像头数据中重建道路、车辆、行人、障碍物和运动轨迹，再生成更多合成场景训练系统。相比传统图形仿真，数据驱动的世界模型更接近真实道路，也更容易形成闭环。</p>
<p>低速无人配送车同样提供了清晰样板。它运行在园区、校园、社区、商圈和物流站点等相对受控场景，速度低、路线固定、ROI 清晰。无人车最大的优势不是车本身便宜，而是节省司机成本，只要月度成本能显著低于有人车，客户就不需要被过度教育。</p>

<h2 id="heavy-truck">新能源重卡：电动化、智能化与无人化交汇</h2>
<p>新能源重卡是容易被低估的方向。乘用车是消费品，用户关心品牌、外观、舒适性和残值；重卡是生产资料，客户最关心全生命周期成本。</p>
<p>重卡在交通碳排放和污染物排放中的占比远高于保有量占比。如果重卡不电动化，交通减排很难真正完成。新能源重卡绑定双碳战略、能源安全和物流降本，本质上是生产资料升级。</p>
<p>更大的想象空间是无人重卡。重卡司机工作强度高、安全风险高、人工成本高，且司机群体存在年龄结构问题。电动化先降低能源与维护成本，智能化和无人化再降低人工成本，最终有机会从卖车升级为低碳物流和无人运输平台。</p>

<h2 id="investment-framework">投资框架：模型、制造、服务与供应链</h2>
<p>物理 AI 产业链不能用传统机器人框架简单理解。它既有大模型属性，也有高端制造属性；既有硬件供应链，也有软件平台和运营服务；既需要技术突破，也需要场景落地。</p>
<p>第一层是链主层，包括大模型厂商、制造商和 AI 服务化公司。模型厂商提供具身大脑，制造商负责本体和供应链，服务公司把机器人、软件、数据、运维和持续收费结合起来。</p>
<p>第二层是应用层，未来会出现大量垂直领域公司。工业、商业、家庭、医疗、农业、物流、低空经济和自动驾驶的需求差异很大，因此应用层不会像数字 AI 那样赢家通吃。</p>
<p>第三层是供应链层，包括数据采集、仿真训练、端侧芯片、推理芯片、运控芯片、传感器、激光雷达、触觉传感器、关节模组、减速器、执行器、电机和控制器等。进入头部链主供应体系的高壁垒环节，可能获得长期订单。</p>

<h2 id="watchlist">真正该盯的五个方向</h2>
<p>第一是具身大脑，也就是能够理解视觉、语言、动作、三维空间、物理规律和任务目标的基础模型。它包括世界模型、动作模型、小脑控制模型和多模态任务规划系统。</p>
<p>第二是数据基础设施，包括仿真合成数据、人类视频数据、数字孪生数据和评测平台。这是最容易被低估、也最可能形成平台壁垒的方向。</p>
<p>第三是世界模型公司。它们既可以服务自动驾驶，也可以服务机器人、无人车、无人机和工业仿真。如果能够同时拥有真实客户现金流、数据闭环和跨场景扩展能力，就具备双轮驱动。</p>
<p>第四是具身本体。关键不在外形酷不酷，而在能否进入真实场景跑出 ROI。轮式双臂、四足、机械臂、商用服务机器人和人形机器人，对应不同场景和成本结构。</p>
<p>第五是智能运载设备与端侧芯片。无人配送、Robotaxi、新能源重卡、无人机、无人车、机器人都共享感知、决策、控制、端侧计算和数据闭环能力。</p>

<h2 id="risks">风险：长期向上不等于短期直线</h2>
<p>物理 AI 是未来 5 到 10 年的重要主线，但越是远期空间巨大的产业，早期越容易出现估值过热、路线摇摆和情绪波动。</p>
<p>技术路线尚未完全收敛，VLA、世界模型、混合架构、端到端、分层控制和隐空间模型都还在演化。数据获取也是核心风险，仿真和现实之间的差距，可能让模型在真实场景中失效。商业化同样不会一帆风顺，实验室成功不代表工厂连续运营，演示效果不等于客户复购。</p>
<p>此外，物理 AI 仍然离不开算力和高端芯片，地缘政治、出口管制、供应链合规和客户信任都会影响产业节奏。投资上应以长期产业逻辑选择方向，以短期交易纪律控制节奏。</p>

<h2 id="conclusion">结论：物理 AI 的核心资产是基础设施</h2>
<p>物理 AI 不是单一机器人行情，而是从数字任务走向物理任务的产业迁移。应用会高度分散，但基础设施可能高度集中。</p>
<p>谁能定义世界模型、仿真数据、评测标准、端侧芯片、动作模型和开发框架，谁就可能成为物理 AI 时代的“新 CUDA”。谁能在真实场景中形成数据飞轮和商业闭环，谁就有机会成为下一代智能产业的核心公司。</p>
"""


BODY_INVESTMENT_MAP = """
<p><img src="/images/posts/physical-ai-investment-map-autonomous-driving-robotics-industrial-software/cover.svg" alt="物理 AI 投资图谱：智能驾驶、人形机器人与工业软件"></p>
<p>当大语言模型把信息处理能力推到新高度之后，AI 的下一个主战场正在转向物理世界。物理 AI，也就是具身智能，要让机器在真实环境中感知、判断、行动和反馈。它不是一个单点赛道，而是一张覆盖基础模型、智能驾驶、人形机器人、工业软件、仿真平台、传感器、芯片和核心零部件的产业图谱。</p>
<p>投资上最容易犯的错误，是只盯着机器人外壳。真正的物理 AI 机会分布在三层：最上层是大脑与模型，中间层是身体与应用场景，底层是环境、工具和基础设施。只有把三层拆开，才能分清高壁垒、高确定性和高弹性的方向。</p>

<h2 id="three-layer">物理 AI 产业链的三层结构</h2>
<p>第一层是大脑，也就是基础模型层。世界模型负责预测环境变化，VLA 负责把视觉、语言和动作连接起来，VLM 负责理解视觉和语言指令。这一层决定了机器能否理解三维空间、任务目标和物理后果。</p>
<p>第二层是身体和应用场景，主要包括智能驾驶和人形机器人。智能驾驶是最先落地的物理 AI 场景，人形机器人则代表更长期的泛化空间。前者商业模式更清晰，后者想象力更大。</p>
<p>第三层是环境、工具和基础设施，包括仿真平台、工业软件、数字孪生、CAE、CAD、EDA、数据生成、评测系统和部署工具。物理 AI 要训练和落地，必须有虚拟训练场和工业级工具链，否则无法低成本获得足够数据，也无法在真实场景中稳定交付。</p>

<h2 id="autonomous-driving">智能驾驶：物理 AI 最先落地的第一曲线</h2>
<p>智能驾驶之所以最先落地，有三个原因：数据积累多、商业模式清晰、政策支持强。车辆天然能够持续采集道路数据，车企有明确的智能化竞争压力，用户也能感知智能驾驶带来的安全、效率和体验提升。</p>
<p>智能驾驶产业链可以拆成感知、决策和执行三层。感知层依靠摄像头、毫米波雷达、激光雷达等传感器；决策层依靠芯片、算法和模型；执行层依靠域控制器、底盘控制和整车电子电气架构。</p>
<p>投资上，感知层可以关注激光雷达和 3D 视觉，决策层关注智能驾驶芯片和算法平台，执行层关注域控制器和整车电子。智能驾驶不是孤立赛道，它与世界模型、仿真数据、端侧芯片和机器人控制高度同源。</p>

<h2 id="humanoid">人形机器人：第二曲线的长期价值</h2>
<p>人形机器人代表物理 AI 的第二曲线。它的目标是让机器具有人类环境中的感知和运动能力，能够理解空间、处理未知情况，并与人自然交互。特斯拉、小米、宇树等公司持续投入，说明这一方向已经从概念走向工程验证。</p>
<p>人形机器人投资可以分为两类。第一类是核心零部件，包括 3D 视觉传感器、减速器、关节模块、电机、丝杠、执行器和控制器。这类环节有明确技术参数和量产标准，下游客户一旦定点，替换成本较高，确定性相对更强。</p>
<p>第二类是软件和服务，包括具身智能操作系统、仿真工具链、模型平台和部署服务。它的弹性更大，但标准尚未统一，压单一软件公司的风险也更高。因此，机器人投资要分清确定性和弹性，不能把零部件逻辑与软件平台逻辑混在一起。</p>

<h2 id="simulation">仿真平台：物理 AI 的虚拟训练场</h2>
<p>物理 AI 训练需要海量数据，但真实数据太贵。让机器人在真实工厂里不断撞坏设备、摔坏零件再学习，成本无法承受。仿真平台因此成为刚需。</p>
<p>仿真平台用数学模型模拟物理世界，让机器人可以在虚拟环境中练习上万次。自动驾驶可以在仿真道路中遇到极端天气、突然横穿的行人和复杂交通；机器人可以在虚拟工厂里练习开抽屉、抓取零件、避障和装配。</p>
<p>没有仿真数据，物理 AI 很难训练出来。过去 CAE 可能是工程研发中的锦上添花，如今在物理 AI 中，它正在变成训练、验证和评测的基础设施。</p>

<h2 id="industrial-software">工业软件：被低估的控制台</h2>
<p>工业软件是物理世界的数字化表达。机器人设计、工厂布局、工艺规划、力学仿真、流体仿真、电磁仿真、芯片设计、产线控制，都离不开工业软件。</p>
<p>物理 AI 训练需要仿真数据，仿真需要物理引擎，物理引擎来自工业软件。每一台物理 AI 设备背后，可能对应成千上万小时的 CAE 仿真、CAD 设计、EDA 芯片设计和工控系统验证。</p>
<p>英伟达与 Cadence、达索、西门子、PTC、Synopsys 等工业软件巨头合作，本质上是在把 GPU 和仿真能力注入工业软件生态。谁掌握仿真和工业软件入口，谁就更接近物理 AI 时代的“军火商”位置。</p>

<h2 id="cae">CAE 与数字孪生：索辰科技和 51WORLD 的逻辑</h2>
<p>CAE 仿真软件的价值，是在电脑里模拟物理世界。流体、电磁、多物理场耦合、结构力学和热管理，都可以通过仿真提前验证。物理 AI 到来后，CAE 不再只是研发工具，而是机器人和自动驾驶的训练数据来源。</p>
<p>索辰科技的核心在工业 CAE 仿真软件。它的看点在于物理 AI 带来新的仿真需求，过去较窄的应用场景可能拓展为训练刚需。生成式物理 AI 仿真平台仍处早期，收入体量不大，但方向值得跟踪。</p>
<p>51WORLD 则偏向数字孪生和仿真，既有自动驾驶仿真，也有场景重建和数字孪生。高阶智驾需要海量里程测试，仿真可以低成本、高效率完成。它更像看不见但关键的基础设施，短期看订单，中期看 VLA 和世界模型渗透率，长期看数字孪生能否扩展到更多场景。</p>

<h2 id="industrial-control">工业控制与 CAD：中控技术和中望软件</h2>
<p>中控技术的主业是工业控制系统，工厂生产线的大脑离不开 DCS、控制软件和工业自动化系统。它与物理 AI 的关系在于：机器人进入工厂，需要与工控系统对接；预测性维护、智能优化、边缘控制，本质上就是物理 AI 在工业场景中的落地。</p>
<p>中控技术的优势是工业客户基础、现金流和工艺理解。风险在于工控市场整体增速有限，工业 AI 商业化还需要持续观察。</p>
<p>中望软件是国产 CAD 龙头。CAD 是机器人设计、工厂布局、工艺规划和机械结构设计的画笔。2D CAD 已具备较强竞争力，3D CAD 仍在追赶。国产替代空间大，但 3D CAD 技术壁垒极高，研发投入也会压制短期利润。</p>

<h2 id="eda">EDA：华大九天的关键位置</h2>
<p>EDA 是芯片设计工具，没有 EDA，现代芯片设计无法完成。物理 AI 拉动机器人、自动驾驶和端侧智能设备，也会拉动算力芯片、传感器芯片、控制芯片和边缘推理芯片需求。</p>
<p>华大九天是国产 EDA 的代表企业，国内少数具备全流程 EDA 工具体系的公司。它的逻辑既来自半导体自主可控，也来自物理 AI 对芯片设计工具的长期需求。</p>
<p>风险也很明确：全球 EDA 长期被国际巨头垄断，高端制程覆盖、工具完整度和生态适配都需要时间。它是高壁垒方向，但不能用短期收入弹性去简单定价。</p>

<h2 id="sensors">机器的眼睛：奥比中光和禾赛科技</h2>
<p>物理 AI 必须先看见世界。3D 视觉传感器让机器理解三维空间，结构光、TOF、双目立体等技术可以用于机器人、智驾、智能门锁、AR/VR 和工业检测。</p>
<p>奥比中光的逻辑在于 3D 视觉龙头位置。人形机器人要与物理世界交互，首先需要理解空间结构、距离、形状和运动状态。但消费电子需求疲软、竞争加剧，也会影响节奏。</p>
<p>禾赛科技是车载激光雷达龙头之一。激光雷达通过发射激光并接收反射信号，构建周围环境三维点云图。国内主流车企普遍采用激光雷达作为冗余感知，随着量产扩大，成本下降和毛利率修复值得跟踪。风险在于价格战和技术路线不确定性。</p>

<h2 id="controllers-os">域控制器与操作系统：德赛西威和中科创达</h2>
<p>德赛西威的核心产品是智能驾驶域控制器，可以理解为智驾系统的大脑。传感器收集数据，域控制器进行决策，再控制车辆行为。智驾渗透率提升，会推动域控制器成为汽车智能化的重要增量。</p>
<p>德赛西威的优势在于与英伟达等平台的合作、域控制器量产能力和智能座舱现金流。风险是价格战压缩毛利率，以及新进入者竞争。</p>
<p>中科创达从操作系统起家，延伸到智能汽车、物联网和机器人。具身智能需要统一管理传感器、执行器和计算平台的软件层，操作系统和中间件的价值会逐步体现。它的优势是智能汽车 OS 经验和全球客户基础，风险在于手机业务压力与机器人商业化进展。</p>

<h2 id="parts">核心零部件：绿的谐波与机器人确定性</h2>
<p>机器人要真正工作，离不开关节、电机、减速器、丝杠和执行器。电机转得快但力量小，减速器负责降低速度、放大扭矩，让机器人能够稳定完成动作。</p>
<p>绿的谐波的逻辑在于谐波减速器国产替代。全球市场长期由日本企业主导，国产厂商若能进入人形机器人供应链，并在产能、精度、寿命和成本上持续提升，就具备较高确定性。</p>
<p>但它的风险同样来自量产节奏和价格竞争。人形机器人如果量产低于预期，核心零部件订单也会低于预期；海外龙头降价，也可能压缩国产替代的盈利空间。</p>

<h2 id="tracking">跟踪体系：大会、数据和融资</h2>
<p>物理 AI 不是只看财报的赛道，很多领先信号会提前出现。第一类信号是产业大会，例如 GTC、CES、Google I/O 等，通常会揭示模型、芯片、机器人、仿真和开发平台的新方向。</p>
<p>第二类信号是先行数据。机器人看出货量和客户定点，智驾看高阶渗透率和车型搭载，仿真看平台使用量和客户扩展，工业软件看订单和国产替代进度。这些指标往往比财报早半年到一年。</p>
<p>第三类信号是一级市场融资。物理 AI 的早期方向往往先在一级市场反映。世界模型、具身仿真、机器人本体、数据平台、端侧芯片、工业软件等方向的大额融资，值得持续跟踪。</p>

<h2 id="portfolio">组合思路：确定性与弹性分开看</h2>
<p>物理 AI 投资应该分层。确定性较高的方向，通常来自核心零部件、传感器、域控制器、工控系统、工业软件和已形成客户订单的基础设施。它们不一定最性感，但更容易用订单、份额和毛利率验证。</p>
<p>弹性较高的方向，通常来自世界模型、仿真平台、具身操作系统、人形机器人本体和数据基础设施。这些方向一旦跑通，空间很大，但路线、估值和商业化节奏也更不确定。</p>
<p>更合理的方式，是用确定性环节作为底仓，用高弹性方向作为观察和进攻仓位，并持续用先行指标验证产业节奏。</p>

<h2 id="risks">风险：概念很大，兑现很慢</h2>
<p>物理 AI 不是短期就能全面兑现的概念。智能驾驶、人形机器人、工业软件、仿真平台、传感器和芯片都在同一张图谱里，但它们的商业化节奏完全不同。</p>
<p>智能驾驶最先落地，但价格战和技术路线仍有不确定性；人形机器人空间最大，但量产节奏和成本下降仍需验证；工业软件壁垒高，但国产替代周期长；仿真平台想象力大，但收入兑现仍在早期。</p>
<p>因此，物理 AI 投资不能只看故事，要看订单、客户、产品迭代、数据闭环、场景复用和现金流。概念越大，越需要用具体指标拆开验证。</p>

<h2 id="conclusion">结论：物理 AI 的主线，是智能进入实体经济</h2>
<p>物理 AI 的本质，是让 AI 从信息处理工具升级为实体经济中的生产工具。智能驾驶、人形机器人、工业软件、仿真平台和核心零部件，都是这条主线的不同环节。</p>
<p>真正有价值的投资图谱，不是把所有概念都装进一个篮子，而是分清谁是大脑、谁是身体、谁是训练场、谁是工具链、谁是现金流入口。物理 AI 终局很大，但路径一定分阶段展开。</p>
"""


INPUT_ORDER = [
    Post(
        source_id="BV1do7864E6w",
        slug="ai-third-wave-physical-ai-vla-world-model-investment-map",
        title="AI 第三浪：物理 AI 如何从屏幕走向真实世界",
        desc="物理 AI 是从感知式 AI、生成式 AI 之后的第三次跃迁。VLA 与世界模型构成技术闭环，机器人、自动驾驶和工业自动化则是最重要的落地场景。",
        category="投资研究",
        series="物理AI",
        tags=["物理AI", "VLA", "世界模型", "具身智能", "人形机器人", "自动驾驶", "工业自动化", "仿真平台", "机器人", "AI产业链"],
        minutes=12,
        body=BODY_AI_THIRD_WAVE,
        cover_kicker="AI 第三浪",
        cover_line="VLA · 世界模型 · 真实世界行动",
        cover_theme=("#0f172a", "#1d4ed8", "#38bdf8"),
        duration=814.2309375,
        segments=42,
        chars=4313,
    ),
    Post(
        source_id="BV1YU5W6ZEPJ",
        slug="physical-ai-infrastructure-next-nvidia-cuda-world-model",
        title="物理 AI 元年：谁会成为下一个英伟达与 CUDA",
        desc="数字 AI 应用层高度集中，物理 AI 应用层更分散，真正有机会整合生态的是世界模型、仿真数据、评测标准、端侧芯片和开发框架等基础设施。",
        category="投资研究",
        series="物理AI",
        tags=["物理AI", "世界模型", "具身智能", "CUDA", "英伟达", "大模型", "Token经济", "仿真数据", "端侧芯片", "自动驾驶", "机器人"],
        minutes=32,
        body=BODY_NEXT_CUDA,
        cover_kicker="新 CUDA",
        cover_line="世界模型 · 数据飞轮 · 物理基础设施",
        cover_theme=("#111827", "#7c2d12", "#f97316"),
        duration=6267.762375,
        segments=3015,
        chars=25757,
    ),
    Post(
        source_id="BV1ShEm6wEBn",
        slug="physical-ai-investment-map-autonomous-driving-robotics-industrial-software",
        title="物理 AI 投资图谱：智能驾驶、人形机器人与工业软件",
        desc="物理 AI 产业链可以拆成基础模型、场景应用和工具基础设施三层。智能驾驶先落地，人形机器人看长期，仿真和工业软件是容易被低估的底层入口。",
        category="投资研究",
        series="物理AI",
        tags=["物理AI", "智能驾驶", "人形机器人", "工业软件", "CAE", "EDA", "激光雷达", "减速器", "仿真平台", "A股", "机器人"],
        minutes=10,
        body=BODY_INVESTMENT_MAP,
        cover_kicker="投资图谱",
        cover_line="智驾 · 机器人 · 工业软件",
        cover_theme=("#052e16", "#166534", "#86efac"),
        duration=632.7205625,
        segments=425,
        chars=3639,
    ),
]

PUBLISH_ORDER = list(reversed(INPUT_ORDER))


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def rec(path: Path) -> None:
    CHANGED.add(path.relative_to(ROOT).as_posix())


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    rec(path)


def term_url(kind: str, term: str) -> str:
    return f"/{kind}/{quote(term)}/"


def meta_links(post: Post) -> str:
    cat = f'<a href="{term_url("categories", post.category)}">{esc(post.category)}</a>'
    tags = "&nbsp;".join(f'<a href="{term_url("tags", tag)}">{esc(tag)}</a>' for tag in post.tags)
    return f'<span class="meta-icon" aria-hidden="true">▣</span> {cat}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◇</span> {tags}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min'


def build_toc(body: str) -> str:
    links = [
        f'<a class="toc-link toc-level-2" href="#{m.group(1)}">{m.group(2)}</a>'
        for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    ]
    return '<div class="toc-wrapper"><div class="toc"><div class="toc-title">目录</div><nav>' + "".join(links) + "</nav></div></div>"


def cover_svg(post: Post) -> str:
    c1, c2, c3 = post.cover_theme
    title_lines = post.title.replace("：", "：\n", 1).split("\n")
    title_svg = "".join(
        f'<text x="96" y="{155 + i * 72}" fill="#f8fafc" font-family="Noto Sans SC, PingFang SC, Arial" font-size="{58 if i == 0 else 50}" font-weight="800">{esc(line)}</text>'
        for i, line in enumerate(title_lines[:2])
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">{esc(post.title)}</title>
  <desc id="desc">{esc(post.desc)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="0.58" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></linearGradient>
    <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000" flood-opacity="0.32"/></filter>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <g opacity="0.15" stroke="#fff" stroke-width="3">
    <path d="M120 690 H1480"/><path d="M120 570 H1480"/><path d="M120 450 H1480"/><path d="M120 330 H1480"/>
    <path d="M300 240 V760"/><path d="M600 240 V760"/><path d="M900 240 V760"/><path d="M1200 240 V760"/>
  </g>
  <g filter="url(#shadow)">
    <path d="M160 680 C320 570 470 620 650 485 C825 350 960 455 1160 305 C1290 190 1410 205 1500 130" fill="none" stroke="#f8fafc" stroke-width="15" stroke-linecap="round" opacity="0.88"/>
    <circle cx="650" cy="485" r="42" fill="{c3}"/><circle cx="1160" cy="305" r="50" fill="#f8fafc" opacity="0.92"/>
    <rect x="112" y="590" width="500" height="118" rx="24" fill="#f8fafc" opacity="0.94"/>
    <text x="152" y="665" fill="{c2}" font-family="Noto Sans SC, PingFang SC, Arial" font-size="42" font-weight="800">{esc(post.cover_kicker)}</text>
  </g>
  {title_svg}
  <text x="100" y="315" fill="#f8fafc" opacity="0.92" font-family="Noto Sans SC, PingFang SC, Arial" font-size="36" font-weight="700">{esc(post.cover_line)}</text>
  <text x="102" y="382" fill="#e5e7eb" font-family="Noto Sans SC, PingFang SC, Arial" font-size="28" font-weight="600">{esc(post.desc[:46])}</text>
</svg>'''


def pagination_for(post: Post) -> tuple[str, str, str, str]:
    idx = PUBLISH_ORDER.index(post)
    newer_url = ""
    newer_title = ""
    if idx > 0:
        newer_url = PUBLISH_ORDER[idx - 1].url_path
        newer_title = PUBLISH_ORDER[idx - 1].title
    older_url = PREV_EXISTING_URL
    older_title = PREV_EXISTING_TITLE
    if idx < len(PUBLISH_ORDER) - 1:
        older_url = PUBLISH_ORDER[idx + 1].url_path
        older_title = PUBLISH_ORDER[idx + 1].title
    return newer_url, newer_title, older_url, older_title


def build_article_page(post: Post) -> None:
    template = (ROOT / PREV_EXISTING_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    start = template.find('<article class="post">')
    end = template.find("</article>", start) + len("</article>")
    head, tail = template[:start], template[end:]
    replacements = {
        r"<title>.*?</title>": f"<title>{esc(post.title)} - zcxGGmu's Blog</title>",
        r'<meta name="description" content="[^"]*">': f'<meta name="description" content="{esc(post.desc)}">',
        r'<meta property="og:url" content="[^"]*">': f'<meta property="og:url" content="{esc(post.full_url)}">',
        r'<meta property="og:title" content="[^"]*">': f'<meta property="og:title" content="{esc(post.title)}">',
        r'<meta property="og:description" content="[^"]*">': f'<meta property="og:description" content="{esc(post.desc)}">',
        r'<link rel="canonical" href="[^"]*">': f'<link rel="canonical" href="{esc(post.full_url)}">',
    }
    for pattern, repl in replacements.items():
        head = re.sub(pattern, repl, head, count=1, flags=re.S)
    newer_url, newer_title, older_url, older_title = pagination_for(post)
    newer = '<a class="newer-posts">下一篇<br>没有更新的文章</a>'
    if newer_url:
        newer = f'<a class="newer-posts" href="{newer_url}">下一篇<br>{esc(newer_title)}</a>'
    older = f'<a class="older-posts" href="{older_url}">上一篇<br>{esc(older_title)}</a>'
    article = f'''<article class="post"><div class="post-head-wrapper" style="background-image:url('{post.cover}')"><div class="post-title">{esc(post.title)}<div class="post-subtitle">{esc(post.desc)}</div><div class="post-meta"><time itemprop="datePublished">{DATE}</time>&nbsp;&nbsp;{meta_links(post)}</div></div></div><div class="post-body-wrapper"><div class="post-body" v-pre>{post.body}</div></div><nav class="post-pagination">{newer}{older}</nav>
    </article>'''
    tail = re.sub(r'<div class="toc-wrapper">.*?</div></div>', build_toc(post.body), tail, count=1, flags=re.S)
    write(ROOT / "2026" / post.slug / "index.html", head + article + tail)


def update_existing_previous() -> None:
    path = ROOT / PREV_EXISTING_URL.strip("/") / "index.html"
    text = path.read_text(encoding="utf-8")
    target = PUBLISH_ORDER[-1]
    text = re.sub(
        r'<a class="newer-posts">下一篇<br>没有更新的文章</a>|<a class="newer-posts" href="[^"]+">下一篇<br>.*?</a>',
        f'<a class="newer-posts" href="{target.url_path}">下一篇<br>{esc(target.title)}</a>',
        text,
        count=1,
        flags=re.S,
    )
    write(path, text)


def home_card(post: Post) -> str:
    return f'''<a href="{post.url_path}" class="a-block">
      <div class="post-item-wrapper ">
        <div class="post-item post-item-no-divider">
          <div class="post-item-info-wrapper">
            <div class="post-item-title">{esc(post.title)}</div>
            <div class="post-item-summary">{esc(post.desc)}</div>
            <div class="post-item-meta">{DATE}&nbsp;&nbsp;<span class="meta-icon" aria-hidden="true">◷</span> {post.minutes} min&nbsp;&nbsp;</div>
          </div>
          <div class="post-item-image-wrapper"><div class="post-item-image" style="background-image:url('{post.cover}')"></div></div>
        </div>
      </div>
    </a>'''


def update_home() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    for post in INPUT_ORDER:
        text = re.sub(rf'<a href="{re.escape(post.url_path)}" class="a-block">.*?</a>\s*', "", text, flags=re.S)
    pos = text.find(f'<a href="{PREV_EXISTING_URL}" class="a-block">')
    if pos == -1:
        raise RuntimeError("homepage insertion marker not found")
    block = "\n".join(home_card(post) for post in PUBLISH_ORDER) + "\n"
    write(path, text[:pos] + block + text[pos:])


def update_rss() -> None:
    path = ROOT / "index.xml"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{format_datetime(BASE_DT)}</lastBuildDate>", text, count=1)
    for post in INPUT_ORDER:
        text = re.sub(rf"<item>\s*<title>{re.escape(esc(post.title))}</title>.*?</item>\s*", "", text, flags=re.S)
    items = []
    for offset, post in enumerate(PUBLISH_ORDER):
        pub_dt = BASE_DT - timedelta(minutes=offset)
        items.append(f'''<item>
<title>{esc(post.title)}</title>
<link>{post.full_url}</link>
<guid>{post.full_url}</guid>
<pubDate>{format_datetime(pub_dt)}</pubDate>
<description>{esc(post.desc)}</description>
</item>
''')
    write(path, text.replace("<item>", "".join(items) + "<item>", 1))


def update_archive() -> None:
    path = ROOT / "archive/index.html"
    text = path.read_text(encoding="utf-8")
    new_count = sum(1 for post in INPUT_ORDER if post.url_path not in text)
    if new_count:
        text = re.sub(
            r'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">(\d+) 篇</span>',
            lambda m: f'2026<span style="font-size:18px;color:#999;margin-left:10px;font-weight:400">{int(m.group(1)) + new_count} 篇</span>',
            text,
            count=1,
        )
    for post in INPUT_ORDER:
        text = re.sub(rf'<div style="padding:8px 0;font-size:15px">\s*<span style="color:#999">{DATE}</span>&nbsp;\s*<a href="{re.escape(post.url_path)}">.*?</div>\s*', "", text, flags=re.S)
    items = "".join(
        f'''<div style="padding:8px 0;font-size:15px">
        <span style="color:#999">{DATE}</span>&nbsp;
        <a href="{post.url_path}">{esc(post.title)}</a>
        <span style="margin-left:10px"><span style="color:#999;font-size:12px">{esc(post.category)}</span></span>
      </div> '''
        for post in PUBLISH_ORDER
    )
    pos = text.find(f'<a href="{PREV_EXISTING_URL}">')
    start = text.rfind('<div style="padding:8px 0;font-size:15px">', 0, pos)
    write(path, text[:start] + items + text[start:])


def tax_item(post: Post) -> str:
    return f'''<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">
        <a href="{post.url_path}" style="font-size:16px;text-decoration:none">{esc(post.title)}</a>
        <span style="color:#999;font-size:13px;margin-left:10px">{DATE}</span>
      </div> '''


def update_term_index(kind: str, term: str, delta: int) -> None:
    if not delta:
        return
    path = ROOT / kind / "index.html"
    text = path.read_text(encoding="utf-8")
    hrefs = [f"/{kind}/{quote(term)}/", f"/{kind}/{term}/"]
    replaced = False
    for href in hrefs:
        if href in text:
            pattern = re.compile(rf'(<a href="{re.escape(href)}"[^>]*>{re.escape(esc(term))}<span[^>]*>\()(\d+)(\)</span></a>)')
            text, count = pattern.subn(lambda m: f"{m.group(1)}{int(m.group(2)) + delta}{m.group(3)}", text, count=1)
            replaced = bool(count)
            if replaced:
                break
    if not replaced:
        href = f"/{kind}/{quote(term)}/"
        if kind == "tags":
            item = f'<a href="{href}" style="display:inline-block;margin:5px 8px;padding:4px 12px;background:rgba(25,118,210,0.06);border-radius:4px;font-size:15px">{esc(term)}<span style="color:#999;font-size:12px;margin-left:4px">({delta})</span></a>\n'
        else:
            item = f'<a href="{href}" class="a-block" style="padding:8px 0;font-size:18px">{esc(term)}<span style="color:#999;margin-left:8px">({delta})</span></a>\n'
        pos = text.find("</div></div></div>")
        text = text[:pos] + item + text[pos:]
    write(path, text)


def update_term(kind: str, term: str, posts: list[Post], prefix: str, emoji: str) -> None:
    path = ROOT / kind / term / "index.html"
    if path.exists():
        original = path.read_text(encoding="utf-8")
        text = original
        for post in posts:
            text = re.sub(rf'<div style="padding:12px 0;border-bottom:1px solid rgba\(128,128,128,0\.08\)">\s*<a href="{re.escape(post.url_path)}".*?</div>\s*', "", text, flags=re.S)
        inserted = sum(1 for post in posts if post.url_path not in original)
        if inserted:
            text = re.sub(r"共 (\d+) 篇文章", lambda m: f"共 {int(m.group(1)) + inserted} 篇文章", text, count=1)
        marker = '<div style="padding:12px 0;border-bottom:1px solid rgba(128,128,128,0.08)">'
        first = text.find(marker)
        if first == -1:
            first = text.find("</div></div></div>")
        text = text[:first] + "".join(tax_item(post) for post in posts) + text[first:]
    else:
        inserted = len(posts)
        label = f"{prefix}: {term}" if prefix else term
        h1 = f"{emoji} {term}" if emoji else label
        text = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#f8fafc"><meta name="description" content="{esc(label)}"><meta property="og:title" content="{esc(label)} - zcxGGmu's Blog"><link rel="canonical" href="{SITE}/{kind}/{quote(term)}/"><link rel="stylesheet" href="/scss/journal.min.css"><link rel="stylesheet" href="/scss/modern.min.css?v=20260607-sidebar-collapse"><title>{esc(label)} - zcxGGmu's Blog</title></head><body><div class="stream-container"><div class="post-list-container" style="min-height:100vh"><div style="padding:40px 35px"><h1 style="font-size:30px;font-weight:500;margin-bottom:10px">{esc(h1)}</h1><p style="color:#999;margin-bottom:30px">共 {len(posts)} 篇文章</p>{"".join(tax_item(post) for post in posts)}</div></div></div><script src="/js/journal.js"></script></body></html>'''
    write(path, text)
    update_term_index(kind, term, inserted)


def update_taxonomies() -> None:
    by_category: dict[str, list[Post]] = {}
    by_series: dict[str, list[Post]] = {}
    by_tag: dict[str, list[Post]] = {}
    for post in PUBLISH_ORDER:
        by_category.setdefault(post.category, []).append(post)
        by_series.setdefault(post.series, []).append(post)
        for tag in post.tags:
            by_tag.setdefault(tag, []).append(post)
    for term, posts in by_category.items():
        update_term("categories", term, posts, "分类", "")
    for term, posts in by_series.items():
        update_term("series", term, posts, "", "📚")
    for term, posts in by_tag.items():
        update_term("tags", term, posts, "标签", "🏷️")


def copy_script_and_manifest() -> None:
    tasks_dir = ROOT / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(__file__), tasks_dir / SCRIPT_NAME)
    rec(tasks_dir / SCRIPT_NAME)
    manifest_path = tasks_dir / MANIFEST_NAME
    all_changed = sorted(CHANGED | {f"tasks/{SCRIPT_NAME}", f"tasks/{MANIFEST_NAME}"})
    manifest_path.write_text(json.dumps(all_changed, ensure_ascii=False, indent=2), encoding="utf-8")
    rec(manifest_path)


def validate() -> None:
    failures: list[str] = []
    forbidden = ["B站", "bilibili", "哔哩", "视频里", "视频中", "原视频", "音频里", "音频中", "UP主", "up主", "这期", "本期", "作者说", "他提到", "观看", "点赞", "订阅"]
    expected_home = [
        "/2026/codeinsights-local-first-agent-workbench/",
        "/2026/what-you-need-to-learn-from-claw-code-repo/",
        "/2026/gaojingqi-investment-system/",
        "/2026/ai-revolution-permanent-underclass-career-selection/",
        "/2026/live-longer-than-earn-fast-investment-infinite-game/",
    ] + [post.url_path for post in PUBLISH_ORDER] + [PREV_EXISTING_URL]
    for post in INPUT_ORDER:
        article_path = ROOT / post.url_path.strip("/") / "index.html"
        article = article_path.read_text(encoding="utf-8")
        for word in forbidden:
            if word in article:
                failures.append(f"{post.slug}: forbidden {word}")
        for must in [post.title, post.desc, post.tags[0], post.category]:
            if must not in article:
                failures.append(f"{post.slug}: missing {must}")
        h2 = re.findall(r'<h2 id="([^"]+)">', article)
        links = re.findall(r'class="toc-link toc-level-2" href="#([^"]+)"', article)
        if h2 != links:
            failures.append(f"{post.slug}: toc mismatch")
        ET.fromstring((ROOT / "images/posts" / post.slug / "cover.svg").read_text(encoding="utf-8"))
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    order: list[str] = []
    for m in re.finditer(r'<a href="(/2026/[^"]+/)" class="a-block">', home):
        href = m.group(1)
        if href not in order:
            order.append(href)
    if order[: len(expected_home)] != expected_home:
        failures.append(f"home order mismatch: {order[: len(expected_home)]}")
    ET.parse(ROOT / "index.xml")
    previous = (ROOT / PREV_EXISTING_URL.strip("/") / "index.html").read_text(encoding="utf-8")
    if PUBLISH_ORDER[-1].url_path not in previous:
        failures.append("previous existing article newer link missing")
    for post in INPUT_ORDER:
        for path in [
            ROOT / "archive/index.html",
            ROOT / "categories" / post.category / "index.html",
            ROOT / "series" / post.series / "index.html",
            ROOT / "tags" / post.tags[0] / "index.html",
        ]:
            if post.url_path not in path.read_text(encoding="utf-8"):
                failures.append(f"{path}: missing {post.url_path}")
    pycache = [str(p) for p in ROOT.rglob("__pycache__")]
    if pycache:
        failures.append(f"__pycache__ present: {pycache[:3]}")
    if failures:
        raise SystemExit("\n".join(failures))


def main() -> None:
    for post in INPUT_ORDER:
        write(ROOT / "images/posts" / post.slug / "cover.svg", cover_svg(post))
        build_article_page(post)
    update_existing_previous()
    update_home()
    update_rss()
    update_archive()
    update_taxonomies()
    validate()
    copy_script_and_manifest()
    manifest = json.loads((ROOT / "tasks" / MANIFEST_NAME).read_text(encoding="utf-8"))
    print(json.dumps({"urls_input_order": [post.full_url for post in INPUT_ORDER], "changed": len(manifest)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
