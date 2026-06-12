---
name: add-research-link
description: Add a new AI-for-research project/resource URL to this repository's README.md and README_zh.md. Use when the user provides a URL, or asks to add a link/resource/project to the awesome-AI-for-research list, and expects the skill to fetch the linked source, choose the right existing category, create brief English and Chinese descriptions, and update both README files in this repo only.
---

# Add Research Link

## Workflow

1. Confirm you are in the `awesome-AI-for-research` repository root and that both `README.md` and `README_zh.md` exist.
2. Treat a bare URL from the user as a request to add that link.
3. Fetch the linked source before writing:
   - For GitHub repositories, use the GitHub API or page metadata and prefer the repository description plus README summary.
   - For project pages, papers, blogs, benchmarks, or workshops, use the page title, abstract/intro, and meta description.
   - If the URL is unreachable, search the exact title or repo path before falling back to a cautious description.
4. Derive:
   - `name_en`: concise official English display name.
   - `name_zh`: normally the same official product/project name; translate only generic descriptive titles.
   - `desc_en`: one short English sentence, no hype, ideally under 28 words.
   - `desc_zh`: faithful Chinese version of `desc_en`.
   - `section_en` and `section_zh`: matching existing sections from the map below.
5. Insert the entry with `scripts/insert_readme_entry.py`.
6. Run validation:
   - `git diff --check`
   - Count numbered entries in both READMEs and ensure they match.
   - Ensure `README.md` has no Chinese description text unless it is part of an official name.

## Category Map

Use one of these exact section pairs:

| English section | Chinese section | Use for |
| --- | --- | --- |
| `API-based` | `基于 API` | General AI scientist systems that primarily run through hosted/API model workflows. |
| `LLMs combined with genetic and search algorithms` | `遗传算法和搜索算法结合 LLM` | AlphaEvolve, evolutionary search, population search, program evolution, optimizer/search systems. |
| `Research systems based on Claude Code or Codex` | `基于 Claude Code 或 Codex 的科研系统` | Research systems built directly around Claude Code, Codex, coding-agent CLIs, or repo-local agent workflows. |
| `Skills` | `Skills` | Skill libraries, tool libraries, scientific databases, agent tools, and reusable capability packs. |
| `Heuristic Learning using Claude Code or Codex as optimizer` | `Heuristic Learning using Claude Code or Codex as optimizer` | Heuristic learning, gradient-free code optimization, executable policies/world models, and coding-agent optimizer examples. |
| `Autoresearch related` | `Autoresearch related` | Autonomous research loops, overnight experiment runners, self-organizing research agents, and multi-agent research execution. |
| `AI4LLM` | `AI4LLM` | Systems specifically improving LLM training, model development, or ML engineering with research agents. |
| `Harness Engineering` | `Harness Engineering` | Agent harness design, evaluation harnesses, runtime substrates, and workflow scaffolds. |
| `Others / To be categorized` | `Others / 待分类` | Ambiguous AI-for-research projects that do not clearly fit another category. |
| `Infrastructure for agent-friendly research` | `Infrastructure for agent friendly research` | Corpora, APIs, preprint platforms, artifacts, structured scientific memory, and agent-native research infrastructure. |
| `Benchmarks for research agents` | `Benchmark for the research agent` | Benchmarks, arenas, leaderboards, evaluation suites, and task collections for research agents. |
| `Papers collection` | `Papers collection` | Workshops, accepted-paper lists, paper collections, and reading lists. |
| `xCode series` | `xCode series` | Coding-agent products or CLI agents such as OpenCode, Kimi Code, MiMo Code. |
| `Related Projects and Resources` | `Related Projects and Resources` | Awesome lists, curated resource collections, and adjacent indexes. |

If classification is genuinely uncertain, choose `Others / To be categorized` and keep the description factual.

## Insert Command

Run from the repository root:

```powershell
python .agents\skills\add-research-link\scripts\insert_readme_entry.py `
  --section-en "Benchmarks for research agents" `
  --section-zh "Benchmark for the research agent" `
  --name-en "ExampleBench" `
  --name-zh "ExampleBench" `
  --url "https://example.com/examplebench" `
  --desc-en "A benchmark for evaluating research agents on example scientific tasks." `
  --desc-zh "用于评估科研智能体处理示例科学任务能力的基准。"
```

Use `--dry-run` first when the section choice or generated text is uncertain.

## Rules

- Modify only `README.md` and `README_zh.md` for ordinary link additions.
- Do not create a new category unless the user explicitly asks for taxonomy changes.
- Preserve existing order and append to the end of the chosen section.
- Do not duplicate an existing URL. If the URL is already present, report the existing location instead of adding another entry.
- Keep English and Chinese entries aligned: same category, same project, matching meaning.
- Keep descriptions brief and source-grounded. Avoid unsupported claims such as "best", "first", or "SOTA" unless the linked source explicitly says so.
