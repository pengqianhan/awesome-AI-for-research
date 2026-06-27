# Awesome AI for Research

[English](README.md) | [Chinese](README_zh.md)

> A continuously updated collection of AI for Research / AI4Research projects, papers, infrastructure, and benchmarks for tracking the ecosystem, identifying pain points, and finding promising directions.

I often see articles and products that use AI directly for research, each with a different entry point. To understand the ecosystem more concretely, I am collecting the resources I come across and analyzing them to identify AI4Research pain points and directions worth pursuing.

## Table of Contents

- <a href="#ai-scientist">AI Scientist</a>
  - <a href="#api-based">API-based</a>
  - <a href="#llms-combined-with-genetic-and-search-algorithms">LLMs combined with genetic and search algorithms</a>
  - <a href="#research-systems-based-on-claude-code-or-codex">Research systems based on Claude Code or Codex</a>
  - <a href="#skills">Skills</a>
  - <a href="#heuristic-learning-using-claude-code-or-codex-as-optimizer">Heuristic Learning using Claude Code or Codex as optimizer</a>
  - <a href="#autoresearch-related">Autoresearch related</a>
  - <a href="#ai4llm">AI4LLM</a>
  - <a href="#harness-engineering">Harness Engineering</a>
  - <a href="#others--to-be-categorized">Others / To be categorized</a>
- <a href="#infrastructure-for-agent-friendly-research">Infrastructure for agent-friendly research</a>
- <a href="#benchmarks-for-research-agents">Benchmarks for research agents</a>
- <a href="#papers-collection">Papers collection</a>
- <a href="#xcode-series">xCode series</a>
- <a href="#related-projects-and-resources">Related Projects and Resources</a>
- <a href="#maintenance-notes">Maintenance notes</a>

## AI Scientist

### API-based

1. [AI Scientist](https://github.com/SakanaAI/AI-Scientist) and [AI Scientist v2](https://github.com/SakanaAI/AI-Scientist-v2/tree/main) - Automated scientific discovery systems that generate ideas, run experiments, and write papers; v2 adds agentic tree search for stronger workshop-level discovery.
2. [AI Researcher (HKUDS)](https://github.com/HKUDS/AI-Researcher) - An autonomous scientific innovation system that supports end-to-end research ideation, experimentation, and paper generation.
3. [Paperorchestra](https://yiwen-song.github.io/paper_orchestra/) - A multi-agent framework that turns sparse idea summaries and raw experiment logs into submission-ready AI research manuscripts.
4. [PaperBanana](https://dwzhu-pku.github.io/PaperBanana/) - An agentic framework for generating publication-ready academic diagrams and statistical plots.
5. [Scientist-One](https://scientist-one.github.io/) - ScientistOne autonomously generates research papers with verifiable evidence chains—every claim traces to code, data, or literature—while matching or exceeding human expert performance on frontier algorithm discovery tasks.

### LLMs combined with genetic and search algorithms

1. [OpenEvolve (AlphaEvolve)](https://github.com/algorithmicsuperintelligence/openevolve) - An open-source AlphaEvolve-style system for evolutionary code and algorithm optimization.
2. [Claude-Evolve](https://github.com/samuelzxu/claude-evolve) - A Claude Code plugin that applies ShinkaEvolve-style evolutionary search to code using model and thinking-effort ensembles.
3. [MLEvolve](https://github.com/InternScience/MLEvolve) - An autonomous machine learning algorithm design and optimization system powered by progressive search and experience memory.

### Research systems based on Claude Code or Codex

1. [Auto-Claude-Code-Research-in-Sleep (ARIS)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) - A lightweight Markdown-only skill stack for autonomous ML research loops, idea discovery, review, and experiment automation.
2. [Academic Research Skills for Claude Code (ARS)](https://github.com/Imbad0202/academic-research-skills/tree/main) - A Claude Code skill workflow for academic research, writing, review, revision, and finalization.
3. [AutoR](https://github.com/AutoX-AI-Labs/AutoR) - A research workflow where AI handles execution, humans steer direction, and each run becomes an inspectable artifact on disk.
4. [Feynman](https://github.com/companion-inc/feynman/tree/main) - An open-source AI research agent for literature review, deep research, peer review, auditing, replication, and experiment workflows.
5. [Deli_AutoResearch](https://victorchen96.github.io/auto_research/framework.html#fullmd) - A protocol framework for long-horizon autonomous tasks.

### Skills

1. [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) - A large library of reusable scientific agent skills and database integrations for biology, chemistry, medicine, and drug discovery.
2. [ToolUniverse](https://github.com/mims-harvard/ToolUniverse) - A tool ecosystem designed to give AI scientists access to scientific tools, databases, and execution capabilities.

### Heuristic Learning using Claude Code or Codex as optimizer

1. [Learning Beyond Gradients](https://trinkle23897.github.io/learning-beyond-gradients/) - An essay proposing Heuristic Learning, where coding agents iteratively improve software policies and systems without gradient updates.
2. [HL-ImageNet](https://github.com/xisen-w/hl-imagenet) - Experiments exploring Heuristic Learning on ImageNet-style visual recognition tasks.
3. [Trajevo: Evolving SOTA Trajectory Prediction Heuristics with LLMs](https://github.com/ai4co/trajevo) - An LLM-driven evolutionary framework for designing trajectory prediction heuristics.
4. [PatchWorld: Learning Executable World Models without Gradients](https://bjx.fun/p/patchworld-learning-executable-world-models-without-gradients/) - A gradient-free framework that induces inspectable Python world models from offline trajectories through counterexample-guided code repair.

### Autoresearch related

1. [autoresearch](https://github.com/karpathy/autoresearch) - A minimal single-GPU nanochat research loop where an agent edits training code, runs bounded experiments, and keeps or reverts changes automatically.
2. [Autoresearch Paradigm Fire](https://paragiri.com/blog/2026/autoresearch-paradigm-fire/) - A blog post about extending the autoresearch loop beyond a basic metric-optimization agent.
3. [PrimeIntellect](https://www.primeintellect.ai/auto-nanogpt) - An autonomous nanoGPT speedrun study where Codex and Claude Code ran large-scale optimizer search on Prime Intellect compute.
4. [AutoScientists](https://github.com/mims-harvard/AutoScientists/tree/main) - A framework for self-organizing agent teams that run long-horizon scientific experimentation.
5. [DeLM](https://yuzhenmao.github.io/DeLM/) - A decentralized multi-agent framework where parallel agents coordinate through shared verified context and a task queue. (note: items 4 and 5 both use parallel agents to conduct research)
6. [ENPIRE](https://research.nvidia.com/labs/gear/enpire/#article-title) - Agentic Robot Policy
Self-Improvement in the Real World (ENPIRE),where robotic agents autonomously experiment and improve themselves in the physical world to enhance performance.

### AI4LLM

1. [Autoresearch](https://github.com/karpathy/autoresearch) - A compact benchmark-style loop for autonomous LLM training research on a single GPU.
2. [ML-Intern](https://github.com/huggingface/ml-intern) - An open-source ML engineer agent that reads papers, trains models, and ships machine learning artifacts.

### Harness Engineering

1. [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness) - Reference code for Meta-Harness, a method for searching agent harnesses under expensive evaluation.

### Others / To be categorized

1. [AutoScientists](https://github.com/mims-harvard/AutoScientists) - A long-running scientific experimentation framework built around self-organizing multi-agent teams.
2. [DeepScientist](https://github.com/ResearAI/DeepScientist) - A local-first autonomous research studio that manages baselines, experiment rounds, memory, and paper-ready outputs.
3. [evoscientist](https://github.com/EvoScientist/EvoScientist) - A self-evolving AI scientist project focused on iterative, agent-driven research workflows.

## Infrastructure for agent-friendly research

1. [Adding arXiv and 150M+ abstracts to Paperclip](https://gxl.ai/blog/adding-arxiv-and-abstracts) - Describes Paperclip's agent-native indexing of arXiv full text and OpenAlex-scale abstracts for searchable research corpora.
2. [DeepXiv SDK](https://github.com/DeepXiv/deepxiv_sdk) - A Python package and AI agent interface for asking questions about arXiv papers.
3. [AI Method Evolution Map](https://intern-atlas.opendatalab.org.cn/#api) - A structured, queryable map of AI method evolution designed as scientific memory for agents.
4. [The Last Human-Written Paper: Agent-Native Research Artifacts](https://www.orchestra-research.com/ara) - A proposal to replace flat papers with machine-native research artifacts that preserve logic, code, traces, and evidence.
5. [General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent) - A synthetic agent environment that evolves its own task corpus to make agent training more diverse and difficult over time.
6. [sepo: self-evolving repository that uses GitHub to manage long-horizon tasks](https://github.com/self-evolving/repo/tree/main) - A GitHub-native agent template that uses issues, PRs, actions, branches, and repository memory to sustain long-horizon work.
7. [AirXiv](https://airaxiv.com/) - An AI-driven open-access preprint platform for AI-generated and human-authored papers, with AI review support.
8. [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) - A open knowledge format for storing and retrieving scientific knowledge.

## Benchmarks for research agents

1. [PaperBench](https://github.com/paperbench/paperbench) - A benchmark for evaluating agents on replicating AI research papers from scratch; the listed GitHub URL may need verification.
2. [ResearchClawBench](https://internscience.github.io/ResearchClawBench-Home/) - A benchmark for evaluating AI agents on automated research, from rediscovery to new discovery.
3. [EinsteinArena](https://einsteinarena.com/) - An open arena where AI agents collaborate and compete on unsolved science and optimization problems.
4. [ResearchClawBench](https://github.com/InternScience/ResearchClawBench) - The GitHub repository for ResearchClawBench and related benchmark implementation resources.
5. [MLS-Bench](https://mls-bench.com/) - A Machine Learning Science benchmark for testing whether agents can make atomic, generalizable ML research contributions.
6. [Autolab](https://github.com/autolabhq/autolab) - A benchmark for frontier ultra long-horizon autonomous research tasks.

## Papers collection

1. [AI Discovery in the Wild (CAIS 2026 Workshop)](https://ai-discovery-in-the-wild.github.io/papers.html) - A CAIS 2026 workshop paper collection on AI agents for real-world scientific discovery.

## xCode series

1. [MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) - Xiaomi MiMo's coding-agent CLI, positioned as a next-generation agent starting point and related to OpenCode.
2. [OpenCode](https://github.com/anomalyco/opencode) - An open-source coding agent for terminal-based software engineering workflows.
3. [Kimi-Code](https://github.com/MoonshotAI/kimi-code) - Moonshot AI's Kimi Code CLI for next-generation coding-agent workflows.

## Related Projects and Resources

1. [Awesome-Autoresearch](https://github.com/alvinreal/awesome-autoresearch) - A curated list of autonomous improvement loops, research agents, and autoresearch-style systems.
2. [Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) - A curated collection of automated research tools for literature search, paper reading, experiment management, and code generation.
3. [Awesome-AI-for-Research](https://github.com/WecoAI/awesome-ai-for-research) - A related awesome-list style resource for AI research tooling; the listed GitHub URL may need verification.
4. [Awesome-Autoresearch: A curated awesome list of public autoresearch use cases across industries](https://github.com/yibie/awesome-autoresearch) - A public list of autoresearch use cases, benchmarks, workshops, and industry examples.
5. [Awesome-Vibe-Research](https://github.com/modelscope/Awesome-Vibe-Research) - An open collaborative repository for AI-assisted research, collecting and distilling agents, skills, workflows, tools, and best practices across the research lifecycle.

## Maintenance notes

- The current categories will continue to evolve, and more representative work will be added to each category over time.
- When new categories are needed, the priority is to keep entries clear, searchable, and easy to compare.
