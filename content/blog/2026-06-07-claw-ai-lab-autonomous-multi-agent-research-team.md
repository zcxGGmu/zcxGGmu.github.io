---
title: "Claw AI Lab：一个自主多智能体研究团队"
date: "2026-06-07T21:35:00+08:00"
updated: "2026-06-07T21:35:00+08:00"
slug: "claw-ai-lab-autonomous-multi-agent-research-team"
description: "Claw AI Lab 将自动化科研从黑箱式 prompt-to-paper 流水线推进为可交互、可检查、可靠性感知的 AI 实验室：用户可以从一个提示创建完整研究团队，并在统一仪表盘中监控、回滚、复现和接管研究过程。"
categories:
  - "AI"
tags:
  - "Claw AI Lab"
  - "AI Agent"
  - "自动化科研"
  - "多智能体"
  - "Claw-Code"
series:
  - "AI Agent"
featured_image: "/images/posts/claw-ai-lab-paper/clawailab-main.png"
pinned: false
---

本文为论文 [Claw AI Lab: An Autonomous Multi-Agent Research Team](https://arxiv.org/abs/2605.22662) 的中文译文。论文 PDF 地址：[https://arxiv.org/pdf/2605.22662](https://arxiv.org/pdf/2605.22662)。文中图片保留自论文源码资源。

## 标题与作者

**Claw AI Lab：一个自主多智能体研究团队**

作者：Fan Wu、Cheng Chen、Zhenshan Tan、Taiyu Zhang、Xinzhen Xu、Yanyu Qian、Dingcheng Gao、Lanyun Zhu、Qi Zhu、Yi Tan、Deyi Ji、Guosheng Lin、Tianrun Chen、Deheng Ye、Fayao Liu。

机构：NTU、A*STAR、Moxin Technology Co., LTD、NUIST、THU、USTC。

项目地址：[https://github.com/Claw-AI-Lab/Claw-AI-Lab](https://github.com/Claw-AI-Lab/Claw-AI-Lab)

## 摘要

本文提出 Claw AI Lab，一个面向实验室原生场景的自主研究平台。它将自动化科研从隐藏的 prompt-to-paper 流水线推进为可交互的 AI 实验室。系统并不围绕单一智能体或固定串行工作流构建，而是允许用户从一个提示实例化完整研究团队，并通过统一仪表盘配置角色、组织协作流程、实时监控事件、检查中间产物，以及执行回滚和恢复控制。

平台还支持探索、多智能体讨论和复现等不同研究模式，使自主研究在实践中变得更可操控，也更接近真实实验室工作。Claw AI Lab 的一项关键实践贡献在于 Claw-Code Harness：它把本地代码库、数据集和检查点连接到可运行实验，并将执行产物反馈回研究循环。因此，harness 不仅改善执行集成，也提升实验完成度和结果完整性：实验更容易被检查、迭代，并忠实迁移到最终论文中，从而减少部分运行、错误表格和结果报告畸形等常见失败模式。

在五个 AI 研究案例的内部评估中，以 AutoResearchClaw 为基线，AI 专家评审在想法新颖性、实验完整性和论文呈现质量上持续偏好 Claw AI Lab。Claw AI Lab 可被视为一种新范式的早期步骤：自主研究作为可用、可交互、可靠性感知的科学基础设施。

## 1. 引言

大语言模型的快速进展使自主研究越来越可行。AutoResearchClaw、autoresearch 以及其他端到端研究智能体已经证明，自动化研究工作流具备可行性：一个主题可以在有限人类干预下，从想法发展推进到实验、分析和论文写作。同时，近期工作也不再局限于一次性论文生成，而是开始探索多智能体科学协作、假设生成，以及更具交互性的科学自动化形式。

Claw AI Lab 在这个方向上迈出不同一步：它不再把自主研究主要视为自动论文生产，而是将其重新定义为一个可运行的交互式 AI 实验室。

这种定位是 Claw AI Lab 设计的核心。系统被设计为实验室原生的多智能体研究平台，允许用户用一个提示创建完整 AI 研究实验室，并支持可定制角色、协作工作流和人类干预。它的界面围绕统一仪表盘展开，提供实时事件流、多项目监控、产物检查和一键回滚。Claw AI Lab 还支持三种不同研究模式：Explore、Discussion 和 Reproduce。由此，系统从隐藏的串行流水线转向更可见、更协作、更可控的研究环境。与纯离线论文生成流水线相比，它更接近交互式和持续性科学系统。

![Overview of Claw AI Lab](/images/posts/claw-ai-lab-paper/clawailab-main.png)

*图 1：Claw AI Lab 总览。系统将自动研究组织为五个相互连接的层：想法层、规划层、编码层、实验层和写作层。每一层都使用专门智能体和验证循环；反馈可以跨层流动，并在必要时修订早期决策。*

实验室视角非常重要，因为真实研究不是一次性生成任务。研究是交互式、迭代式、角色专门化并且产物密集的过程。因此，Claw AI Lab 旨在让自主研究在实践中更可用：用户可以启动项目、监控智能体、检查中间产物，并在研究过程中持续干预，而不是只在开始或结束时介入。从这个意义上说，系统的贡献不只是更强自动化，而是面向自主研究的更强系统抽象：研究被视为一个持久、可检查的过程，而不是黑箱流水线。

Claw AI Lab 的一个关键实践优势在于实验执行和结果整合。已有系统表明，编码智能体已经可以围绕真实训练代码和评估指标运行有效研究循环。Claw AI Lab 将 Claw-Code Harness 作为核心组件，引入读取本地代码库、数据集和检查点、编写可运行代码，并产出完整研究交付物的能力，这些交付物包括论文、代码、图表和实验日志。这个设计使 harness 不只是简单执行包装器，而是连接本地研究资产与可运行实验、并把实验输出接回更大研究工作流的接口。因此，harness 强化了实现、执行和报告之间的连续性。

这一点对实验完成度尤其重要。在自主研究中，常见失败模式包括：实验只部分运行，中间输出难以检查，或者最终报告里的结果表格不能忠实反映实际执行输出。近期基准也表明，多步研究执行、复现实验和证据追踪远比表层生成更困难。Claw AI Lab 明确针对这一缺口而设计。通过把 harness 嵌入仪表盘原生、以产物为中心的工作流，Claw AI Lab 让实验输出更可见、更容易追踪，也更容易进入最终报告。换言之，harness 改善的不只是实验能否运行，还包括实验是否能被推进为完整、可检查、并正确反映的研究产物。相比只从流水线角度理解自主研究，这正是 Claw 提升研究完成质量的关键实践原因。

综合来看，Claw AI Lab 指向该领域更广阔的方向。自主研究的未来可能不在于越来越长的隐藏流水线，而在于可交互、可检查、可靠性感知的 AI 实验室系统。从这个角度看，Claw 的贡献不只是更强平台，也是一种更强的自主研究框架：自主研究不应只是论文写作自动化，而应是可用科学基础设施的构建。

## 2. 方法

本文提出 Claw AI Lab，一个层级化多智能体框架。它通过把端到端研究过程分解为五个结构化层，实现研究自动化：Idea、Planning、Coding、Experiment 和 Writing。系统模拟真实研究实践，把角色专门化、迭代优化和跨阶段反馈统一到闭环流水线中。

### 总览

不同于以线性方式运行的流水线式研究智能体，Claw AI Lab 采用金字塔式架构：高层概念会逐步转化为可执行产物。每一层由职责不同的专门智能体处理，中间输出则通过验证循环持续优化。这个设计符合角色专门化研究智能体和交互式科学自动化的发展趋势。它既支持全局协调，也支持局部优化，从而确保早期决策与后续执行保持一致。

### 想法层

研究过程从多智能体讨论阶段开始。多个智能体共同探索问题空间。系统并不依赖单一视角，而是通过并行想法提案鼓励多样观点，随后进行结构化辩论和优化。共识机制会选择并整合最有前景的方向。

这种由讨论驱动的设计增强了稳健性和多样性，也更接近真实研究想法的形成方式：研究想法通常来自协作，而不是孤立生成。

### 规划层

在选定想法后，系统把它拆解为结构化计划，包括任务、依赖关系和里程碑。规划智能体通过验证循环持续细化计划；当计划尚不完整或存在模糊部分时，会在执行前进行修订。

关键在于，规划不是一次性过程。它支持自适应优化，可以根据下游阶段反馈进行更新，例如编码失败或实验结果反馈。这能确保计划始终可行，并与实际约束保持一致。

### 编码层

编码层把获批实验计划转化为可运行研究代码。该层以 Claw-Code Harness 为中心，使用 agentic coding loop：模型可以检查本地代码库、数据集和检查点，然后通过受控工具编写、运行、调试和改进实验文件。这些工具包括 bash、读取文件、写入文件、编辑文件、glob 搜索和 grep 搜索。

Harness 还通过在沙箱工作区执行每项任务来提高实验可靠性，并注入只读 Python 控制器，用于时间预算执行、指标报告、结果收尾以及 NaN/Inf 检测。它还会执行冒烟测试和反伪造检查，以检测虚假指标、占位代码或 mock 实现。

### 实验层

实现完成后，系统会在计算资源上部署实验，并收集指标和日志。实验层作为迭代优化循环运行：结果会被分析，并指导后续调整。

重要的是，反馈不仅在实验阶段内部传播，也会跨层传播。例如，意外结果可能触发规划阶段更新；反复失败可能导致重新审视最初想法。跨层反馈使系统能够持续改进，并防止错误积累。

### 写作层

最后阶段把实验结果转化为结构化研究输出。系统生成大纲、制作可视化、起草论文，并执行迭代审查与改进。

通过把写作整合到同一条流水线中，Claw AI Lab 可以保证实验结果与报告发现之间的一致性，减少执行与文档之间的断裂。

## 3. 实验

### 3.1 实验设置

Claw AI Lab 在完全自主项目模式下运行。它使用 GPT-5.4 作为主模型和编码模型，使用 Gemini-3-Pro-Image-Preview 作为论文插图生成模型，并使用 Qwen3.5-Plus / Qwen-Plus 作为备用模型。

AutoResearchClaw 使用 GPT-5.4 作为主模型，Gemini-2.5-Pro-Flash-Image 作为图像模型，并使用 GPT-4o / GPT-4o-mini 作为备用模型。

系统在四个不同主题上与 AutoResearchClaw 进行比较。主题 1 到主题 3 是研究主题，主题 4 是复现主题。四个主题分别是：

- Quantifying Hallucination in Generated Video Models
- LIAR Dataset-Based Fake News Classification Solution
- A Q-Learning Approach for Student Performance Improvement Using Public Educational Data
- Reproducing and Analyzing PhyCustom on Flux

每篇生成论文由两个 LLM 评估器评审：ChatGPT 5.4 Thinking 和 Gemini 3.1 Pro。评估维度共有六个，包括技术深度与可复现性、结构与章节流、创新性与贡献、清晰度与术语、逻辑论证、引用与证据支持。每次评审都在新的会话窗口中进行，以减少上下文延续影响。研究论文使用相同学术评审提示，复现论文使用单独的复现导向提示。

### 3.2 实验结果

表 1 汇总主题 1 到主题 3 的研究论文结果。Claw AI Lab 在两个评估器下均持续优于 AutoResearchClaw，平均提升在 +15.5 到 +16.5 分之间。

| 论文 | ChatGPT：AutoResearchClaw | ChatGPT：Claw AI Lab | Gemini：AutoResearchClaw | Gemini：Claw AI Lab | 平均提升 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Paper 1 | 62/100 | 77/100 | 68/100 | 86/100 | +16.5 |
| Paper 2 | 49/100 | 71/100 | 64/100 | 73/100 | +15.5 |
| Paper 3 | 62/100 | 73/100 | 73/100 | 95/100 | +16.5 |

*表 1：主题 1 到主题 3 的三篇研究论文定量结果。不同评估器从六个维度进行评分。*

表 2 展示主题 4 的复现报告结果。平均分从 73.0/100 提升到 78.0/100，对应 5.0 分提升。

| 评估器 | AutoResearchClaw | Claw AI Lab | 提升 |
| --- | ---: | ---: | ---: |
| ChatGPT | 66/100 | 73/100 | +7.0 |
| Gemini | 80/100 | 83/100 | +3.0 |
| Average | 73.0/100 | 78.0/100 | +5.0 |

*表 2：主题 4 复现报告的定量结果。*

总体来看，ChatGPT 和 Gemini 评估器在所有主题上都给 Claw AI Lab 更高评分，说明提升在不同评估协议下保持稳定。图 2 进一步给出六个维度上的细粒度比较。整体上，Claw AI Lab 在多数案例中表现更具竞争力，也更均衡。这些结果表明，Claw AI Lab 受益于更可靠、更高效的 Claw-Code harness；该 harness 能提供更可信的实验执行，并为生成论文提供更强实验证据支持，最终带来更稳定的整体论文质量提升。

![Paper 1 scored by Gemini](/images/posts/claw-ai-lab-paper/radar-paper-1-gemini.png)

*图 2a：Paper 1，由 Gemini 评分。*

![Paper 1 scored by ChatGPT](/images/posts/claw-ai-lab-paper/radar-paper-1-gpt.png)

*图 2b：Paper 1，由 ChatGPT 评分。*

![Paper 2 scored by Gemini](/images/posts/claw-ai-lab-paper/radar-paper-2-gemini.png)

*图 2c：Paper 2，由 Gemini 评分。*

![Paper 2 scored by ChatGPT](/images/posts/claw-ai-lab-paper/radar-paper-2-gpt.png)

*图 2d：Paper 2，由 ChatGPT 评分。*

![Paper 3 scored by Gemini](/images/posts/claw-ai-lab-paper/radar-paper-3-gemini.png)

*图 2e：Paper 3，由 Gemini 评分。*

![Paper 3 scored by ChatGPT](/images/posts/claw-ai-lab-paper/radar-paper-3-gpt.png)

*图 2f：Paper 3，由 ChatGPT 评分。*

![Paper 4 scored by Gemini](/images/posts/claw-ai-lab-paper/radar-paper-4-gemini.png)

*图 2g：Paper 4，由 Gemini 评分。*

![Paper 4 scored by ChatGPT](/images/posts/claw-ai-lab-paper/radar-paper-4-gpt.png)

*图 2h：Paper 4，由 ChatGPT 评分。每个面板都在六个维度上比较 Claw AI Lab 与 AutoResearchClaw。*

## 4. 结论

Claw AI Lab 将自主研究从隐藏式流水线推进为可交互、可检查、可靠性感知的 AI 实验室。它把完整研究过程拆分为想法、规划、编码、实验和写作五个层级，并通过多智能体协作、验证循环和跨层反馈连接起来。相比一次性生成论文，Claw AI Lab 更强调研究过程中的可观察性、可接管性和产物连续性。

系统的关键实践价值集中在 Claw-Code Harness。它将本地代码、数据集、检查点和实验执行连接起来，使实验不只是“能跑”，还要能被检查、迭代、追踪，并被忠实写入最终论文。这种设计减少了自主研究中常见的部分运行、虚假结果、结果表格与实际输出不一致等问题。

实验结果显示，在三个研究主题和一个复现主题上，Claw AI Lab 均优于 AutoResearchClaw。研究论文的平均提升达到约 15.5 到 16.5 分，复现报告平均提升 5 分。结果说明，将执行、产物、监控和写作放进统一实验室式工作流，可以稳定提升自主研究输出质量。

更大的意义在于研究范式的变化：自主研究不应只追求更长、更自动的黑箱流水线，而应走向可用、可交互、可靠性感知的科学基础设施。Claw AI Lab 展示的方向是，未来 AI 研究系统应当像实验室一样运行，而不只是像论文生成器一样输出。

## 参考文献

以下参考文献保留论文英文原始格式。

1. Xuan Dong, Huanyang Zheng, Tianhao Niu, Zhe Han, Pengzhan Li, Bofei Liu, Zhengyang Liu, Guancheng Li, Qingfu Zhu, and Wanxiang Che. *Epibench: Benchmarking multi-turn research workflows for multimodal agents*. arXiv preprint arXiv:2604.05557, 2026.
2. Ali Essam Ghareeb, Benjamin Chang, Ludovico Mitchener, Angela Yiu, Caralyn J. Szostkiewicz, Jon M. Laurent, Muhammed T. Razzak, Andrew D. White, Michaela M. Hinks, and Samuel G. Rodriques. *Robin: A multi-agent system for automating scientific discovery*. arXiv preprint arXiv:2505.13400, 2025.
3. Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, et al. *Towards an ai co-scientist*. arXiv preprint arXiv:2502.18864, 2025.
4. Andrej Karpathy. *autoresearch*, 2026. URL: [https://github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch).
5. Black Forest Labs. *Flux*, 2024. URL: [https://github.com/black-forest-labs/flux](https://github.com/black-forest-labs/flux).
6. Ed Li, Junyu Ren, Xintian Pan, Cat Yan, Chuanhao Li, Dirk Bergemann, and Zhuoran Yang. *Build your personalized research group: A multiagent framework for continual and interactive science automation*. arXiv preprint arXiv:2510.15624, 2025.
7. Jiaqi Liu, Peng Xia, Siwei Han, Shi Qiu, Letian Zhang, Guiming Chen, Haoqin Tu, Xinyu Yang, Jiawei Zhou, Hongtu Zhu, Yun Li, Jiaheng Zhang, Yuyin Zhou, Zeyu Zheng, Cihang Xie, Mingyu Ding, and Huaxiu Yao. *AutoResearchClaw: Fully autonomous research from idea to paper*, 2026. URL: [https://github.com/aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw).
8. Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob N. Foerster, Jeff Clune, and David Ha. *The AI Scientist: Towards fully automated open-ended scientific discovery*. arXiv preprint arXiv:2408.06292, 2024.
9. Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, and Emad Barsoum. *Agent Laboratory: Using LLM agents as research assistants*. Findings of the Association for Computational Linguistics: EMNLP 2025, pp. 5977-6043, 2025.
10. Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, and Tejal Patwardhan. *PaperBench: Evaluating AI's ability to replicate AI research*. Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, pp. 56843-56873, 2025.
11. UltraWorkers. *Claw Code*, 2026. URL: [https://github.com/ultraworkers/claw-code](https://github.com/ultraworkers/claw-code). Public Rust implementation of the `claw` CLI agent harness. Accessed: 2026-05-18.
12. Fan Wu, Cheng Chen, Zhoujie Fu, Jiacheng Wei, Yi Xu, Deheng Ye, and Guosheng Lin. *PhyCustom: Towards realistic physical customization in text-to-image generation*. arXiv preprint arXiv:2512.02794, 2025.
13. Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, and David Ha. *The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search*. arXiv preprint arXiv:2504.08066, 2025.
14. Yuxiang Zheng, Dayuan Fu, Xiangkun Hu, Xiaojie Cai, Lyumanshan Ye, Pengrui Lu, and Pengfei Liu. *DeepResearcher: Scaling deep research via reinforcement learning in real-world environments*. Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 414-431, 2025.

## 资料与图片来源

- arXiv 页面：[https://arxiv.org/abs/2605.22662](https://arxiv.org/abs/2605.22662)
- PDF：[https://arxiv.org/pdf/2605.22662](https://arxiv.org/pdf/2605.22662)
- 论文源码图片：来自 arXiv e-print 源码包
- 项目地址：[https://github.com/Claw-AI-Lab/Claw-AI-Lab](https://github.com/Claw-AI-Lab/Claw-AI-Lab)
