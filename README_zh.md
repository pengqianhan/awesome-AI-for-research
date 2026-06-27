# Awesome AI for Research

[英文](README.md) | [中文](README_zh.md)

> 持续整理 AI for Research / AI4Research 相关项目、论文、基础设施与基准，用于观察生态、定位痛点和发现可做方向。

经常看到有的文章或者产品，是用 AI 来直接做 research，切入点各有不同。为了了解这个领域具体的生态，我准备整理我看到的资料，然后进行分析，从而找到 AI4Research 的痛点和可做的方向。

## 目录

- <a href="#ai-scientist">AI-scientist</a>
  - <a href="#基于-api">基于 API</a>
  - <a href="#遗传算法和搜索算法结合-llm">遗传算法和搜索算法结合 LLM</a>
  - <a href="#基于-claude-code-或-codex-的科研系统">基于 Claude Code 或 Codex 的科研系统</a>
  - <a href="#skills">Skills</a>
  - <a href="#heuristic-learning-using-claude-code-or-codex-as-optimizer">Heuristic Learning using Claude Code or Codex as optimizer</a>
  - <a href="#autoresearch-related">Autoresearch related</a>
  - <a href="#ai4llm">AI4LLM</a>
  - <a href="#harness-engineering">Harness Engineering</a>
  - <a href="#others--待分类">Others / 待分类</a>
- <a href="#infrastructure-for-agent-friendly-research">Infrastructure for agent friendly research</a>
- <a href="#benchmark-for-the-research-agent">Benchmark for the research agent</a>
- <a href="#papers-collection">Papers collection</a>
- <a href="#xcode-series">xCode series</a>
- <a href="#related-projects-and-resources">Related Projects and Resources</a>
- <a href="#维护说明">维护说明</a>

## AI-scientist

### 基于 API

1. [AI-scientist](https://github.com/SakanaAI/AI-Scientist) and [AI-scientist v2](https://github.com/SakanaAI/AI-Scientist-v2/tree/main) - 自动化科研发现系统，覆盖想法生成、实验执行和论文写作；v2 进一步引入 agentic tree search，面向更强的 workshop 级科学发现。
2. [AI-Researcher(HKUDS)](https://github.com/HKUDS/AI-Researcher) - 面向自主科学创新的系统，支持从研究构想到实验和论文生成的端到端流程。
3. [Paperorchestra](https://yiwen-song.github.io/paper_orchestra/) - 多智能体论文写作框架，可把稀疏想法摘要和原始实验日志转成接近投稿状态的 AI 研究论文。
4. [PaperBanana](https://dwzhu-pku.github.io/PaperBanana/) - 面向 AI 科学家的学术插图生成框架，用于自动生成论文级方法图和统计图。
5. [Scientist-One](https://scientist-one.github.io/) - ScientistOne 能够自主生成具备可验证证据链的研究论文——其每一项主张均可追溯至代码、数据或文献——同时在前沿算法发现任务上，达到甚至超越人类专家的水平。

### 遗传算法和搜索算法结合 LLM

1. [OpenEvolve(alphaevolve)](https://github.com/algorithmicsuperintelligence/openevolve) - AlphaEvolve 风格的开源实现，用进化搜索优化代码和算法。
2. [Claude-Evolve](https://github.com/samuelzxu/claude-evolve) - Claude Code 插件，用 ShinkaEvolve 风格的进化搜索和多模型/多思考强度组合来演化代码。
3. [MLEvolve](https://github.com/InternScience/MLEvolve) - 自主机器学习算法设计与优化系统，结合渐进式搜索和经验记忆。

### 基于 Claude Code 或 Codex 的科研系统

1. [Auto-claude-code-research-in-sleep(ARIS)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) - 轻量级 Markdown-only 科研技能栈，用于自主 ML 研究循环、想法发现、评审和实验自动化。
2. [Academic Research Skills for Claude Code (ARS)](https://github.com/Imbad0202/academic-research-skills/tree/main) - 面向 Claude Code 的学术研究技能流程，覆盖调研、写作、审阅、修订和定稿。
3. [AutoR](https://github.com/AutoX-AI-Labs/AutoR) - AI 负责执行、人类把握方向的研究系统，每次运行都会沉淀为可检查的磁盘 artifact。
4. [Feynman](https://github.com/companion-inc/feynman/tree/main) - 开源 AI 科研代理，支持文献综述、深度研究、模拟评审、审计、复现实验和实验流程。
5. [Deli_AutoResearch](https://victorchen96.github.io/auto_research/framework.html#fullmd) - 面向长期自主任务的协议框架。

### Skills

1. [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) - 大规模科学智能体技能库，包含面向生物、化学、医学和药物发现的技能与数据库集成。
2. [ToolUniverse](https://github.com/mims-harvard/ToolUniverse) - 面向 AI 科学家的工具生态，为智能体提供科学工具、数据库和执行能力。

### Heuristic Learning using Claude Code or Codex as optimizer

1. [Learning Beyond Gradients](https://trinkle23897.github.io/learning-beyond-gradients/) - 提出 Heuristic Learning 的长文，讨论编码智能体如何在不更新梯度的情况下持续改进软件策略和系统。
2. [HL-ImageNet](https://github.com/xisen-w/hl-imagenet) - 在 ImageNet 风格视觉识别任务上探索 Heuristic Learning 的实验项目。
3. [Trajevo(Evolving SOTA Trajectory Prediction Heuristics with LLMs)](https://github.com/ai4co/trajevo) - 使用 LLM 驱动的进化流程来设计轨迹预测启发式方法。
4. [PatchWorld: Learning Executable World Models without Gradients](https://bjx.fun/p/patchworld-learning-executable-world-models-without-gradients/) - 无梯度框架，通过反例驱动的代码修复，从离线轨迹中归纳可检查的 Python 世界模型。

### Autoresearch related

1. [autoresearch](https://github.com/karpathy/autoresearch) - 极简单卡 nanochat 研究循环，让智能体编辑训练代码、运行限时实验，并自动保留或回滚改动。
2. [Autoresearch Paradigm Fire](https://paragiri.com/blog/2026/autoresearch-paradigm-fire/) - 关于扩展 autoresearch 循环的文章，讨论如何超越基础的指标优化智能体。
3. [PrimeIntellect](https://www.primeintellect.ai/auto-nanogpt) - Prime Intellect 的自主 nanoGPT speedrun 实验，让 Codex 和 Claude Code 在大规模算力上搜索优化器方案。
4. [AutoScientists](https://github.com/mims-harvard/AutoScientists/tree/main) - 面向长期科学实验的自组织多智能体团队框架。
5. [DeLM](https://yuzhenmao.github.io/DeLM/) - 去中心化多智能体框架，让并行智能体通过共享的已验证上下文和任务队列协作。（注：第 4 和第 5 项都使用并行智能体开展研究）
6. [ENPIRE](https://research.nvidia.com/labs/gear/enpire/#article-title) - Agentic Robot Policy
Self-Improvement in the Real World (ENPIRE)，让机器人智能体在物理世界中通过自主实验和改进来提升性能。

### AI4LLM

1. [Autoresearch](https://github.com/karpathy/autoresearch) - 用于单卡 LLM 训练研究的紧凑型自主实验循环。
2. [ML-Intern](https://github.com/huggingface/ml-intern) - 开源 ML 工程师智能体，可阅读论文、训练模型并交付机器学习 artifact。

### Harness Engineering

1. [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness) - Meta-Harness 论文的参考代码，用于在昂贵评估条件下搜索 agent harness。

### Others / 待分类

1. [AutoScientists](https://github.com/mims-harvard/AutoScientists) - 基于自组织多智能体团队的长期科学实验框架。
2. [DeepScientist](https://github.com/ResearAI/DeepScientist) - 本地优先的自主科研工作室，管理 baseline、实验轮次、记忆和论文级输出。
3. [evoscientist](https://github.com/EvoScientist/EvoScientist) - 自进化 AI 科学家项目，关注迭代式、智能体驱动的研究流程。

## Infrastructure for agent friendly research

1. [Adding arXiv and 150M+ abstracts to Paperclip](https://gxl.ai/blog/adding-arxiv-and-abstracts) - 介绍 Paperclip 如何为智能体索引 arXiv 全文和 OpenAlex 规模的摘要语料，支持搜索、阅读和综合。
2. [DeepXiv SDK](https://github.com/DeepXiv/deepxiv_sdk) - 用于和 arXiv 论文对话的 Python 包与 AI agent 接口。
3. [AI 方法演化图谱](https://intern-atlas.opendatalab.org.cn/#api) - 面向智能体的结构化、可查询 AI 方法演化图谱，可作为科学记忆层。
4. [The Last Human-Written Paper Agent-Native Research Artifacts](https://www.orchestra-research.com/ara) - 提出用机器原生研究 artifact 替代扁平论文，保留逻辑、代码、探索轨迹和证据。
5. [General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent) - 自进化合成智能体环境，通过持续扩展任务语料来提升 agent 训练的多样性和难度。
6. [sepo: self-evolving repository(use GitHub to manage long-horizon tasks)](https://github.com/self-evolving/repo/tree/main) - GitHub-native agent 模板，用 issue、PR、Actions、分支和仓库记忆承载长期任务。
7. [AirXiv](https://airaxiv.com/) - 面向 AI 生成论文和人类论文的 AI 驱动开放预印本平台，并提供 AI 评审支持。
8. [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) - 一个开源的知识库格式，用于存储和检索科学知识。
9. [ModernTSF](https://github.com/Diaugeia/ModernTSF/tree/main) - 面向时间序列预测的 AI Infrastructure —— 而不只是又一个工具包。 一个统一、可复现的底座，让人和 Agent 都把时间花在创新 idea 上， 而不是它周围的各种胶水工作
## Benchmark for the research agent

1. [PaperBench](https://github.com/paperbench/paperbench) - 用于评估智能体从零复现 AI 研究论文能力的基准；当前列出的 GitHub URL 可能需要核对。
2. [ResearchClawBench](https://internscience.github.io/ResearchClawBench-Home/) - 用于评估 AI 智能体自动科研能力的基准，覆盖从 rediscovery 到 new discovery 的任务。
3. [EinsteinArena](https://einsteinarena.com/) - 开放竞技场，让 AI 智能体围绕未解决科学和优化问题协作、竞争并提交解法。
4. [ResearchClawBench](https://github.com/InternScience/ResearchClawBench) - ResearchClawBench 的 GitHub 仓库，包含相关基准实现和资源。
5. [MLS-Bench](https://mls-bench.com/) - Machine Learning Science 基准，用于测试智能体是否能提出原子化、可泛化的 ML 科研贡献。
6. [Autolab](https://github.com/autolabhq/autolab) - 面向前沿超长周期自主科研任务的评测基准。

## Papers collection

1. [AI Discovery in the Wild (CAIS 2026 Workshop)](https://ai-discovery-in-the-wild.github.io/papers.html) - CAIS 2026 研讨会论文合集，主题是面向真实科学发现的 AI 智能体。

## xCode series

1. [MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) - 小米 MiMo 的 coding-agent CLI，定位为下一代 agent 起点，并与 OpenCode 生态相关。
2. [OpenCode](https://github.com/anomalyco/opencode) - 开源 coding agent，用于终端中的软件工程工作流。
3. [Kimi-Code](https://github.com/MoonshotAI/kimi-code) - Moonshot AI 的 Kimi Code CLI，面向下一代 coding-agent 工作流。

## Related Projects and Resources

1. [Awesome-Autoresearch](https://github.com/alvinreal/awesome-autoresearch) - 自主改进循环、research agents 和 autoresearch 风格系统的精选列表。
2. [Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) - 自动化科研工具合集，覆盖文献搜索、论文阅读、实验管理和代码生成。
3. [Awesome-AI-for-Research](https://github.com/WecoAI/awesome-ai-for-research) - AI research 工具相关的 awesome-list 风格资源；当前列出的 GitHub URL 可能需要核对。
4. [Awesome-Autoresearch(A curated awesome list of public autoresearch use cases across industries.)](https://github.com/yibie/awesome-autoresearch) - 公开 autoresearch 用例、基准、研讨会和行业案例的精选列表。
5. [Awesome-Vibe-Research](https://github.com/modelscope/Awesome-Vibe-Research) - 面向 AI 辅助科研的开放共建仓库, 收集和沉淀科研全流程中的 agents、skills、workflows、tools 与最佳实践

## 维护说明

- 当前分类会持续调整，后续会为每个类别补充更多代表性工作。
- 如果有必要添加新的分类，会优先保证资源条目清晰、可检索、便于比较。
