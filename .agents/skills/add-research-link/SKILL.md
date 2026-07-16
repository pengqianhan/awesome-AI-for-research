---
name: add-research-link
description: Add a new AI-for-research project or resource URL to this repository's README.md and README_zh.md, including a clickable auto-updated Star count for GitHub repositories. Use when the user provides a URL or asks to add a link, resource, or project to the awesome-AI-for-research list and expects source-grounded bilingual descriptions, correct categorization, synchronized README entries, and GitHub Star metadata.
---

# Add Research Link

## Workflow

1. Confirm you are in the `awesome-AI-for-research` repository root and that both `README.md` and `README_zh.md` exist.
2. Treat a bare URL from the user as a request to add that link.
3. Fetch the linked source before writing:
   - For GitHub repositories, use the GitHub API or page metadata and prefer the repository description plus README summary.
   - For project pages, papers, blogs, benchmarks, or workshops, use the page title, abstract/intro, and meta description.
   - If a project page links to one clearly official GitHub repository, use that canonical repository URL for the README entry. Ignore dependencies, examples, website-template sources, and unrelated outbound repositories. Keep the project-page URL when ownership is ambiguous or no official repository is linked.
   - If the URL is unreachable, search the exact title or repo path before falling back to a cautious description.
4. Derive:
   - `name_en`: concise official English display name.
   - `name_zh`: normally the same official product/project name; translate only generic descriptive titles.
   - `desc_en`: one short English sentence, no hype, ideally under 28 words.
   - `desc_zh`: faithful Chinese version of `desc_en`.
   - `section_en` and `section_zh`: matching existing sections from the map below.
5. Insert the entry with `scripts/insert_readme_entry.py`. For a GitHub repository URL, the script must add the clickable `<!--stars:OWNER/REPO-->` marker automatically.
6. Refresh the new Star count with `python scripts/update_stars.py`. If network access is unavailable, keep `⭐ updating`; the scheduled GitHub Action will resolve it after merge.
7. Run validation:
   - `git diff --check`
   - Confirm each README gained exactly one numbered entry and that the new English and Chinese entries describe the same resource.
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
| `RSI (recursive self improvement) / Harness Engineering` | `RSI (recursive self improvement) / Harness Engineering` | Agent harness design, evaluation harnesses, runtime substrates, recursive self-improvement, and workflow scaffolds. |
| `Infrastructure for agent-friendly research` | `智能体友好型科研基础设施` | Corpora, APIs, preprint platforms, artifacts, structured scientific memory, and agent-native research infrastructure. |
| `Benchmarks for research agents` | `科研智能体评测基准` | Benchmarks, arenas, leaderboards, evaluation suites, and task collections for research agents. |
| `Paper collections` | `论文合集` | Workshops, accepted-paper lists, paper collections, and reading lists. |
| `xCode series` | `xCode 系列` | Coding-agent products or CLI agents such as OpenCode, Kimi Code, MiMo Code. |
| `Related projects and resources` | `相关项目与资源` | Awesome lists, curated resource collections, and adjacent indexes. |

If classification is genuinely uncertain, choose the closest existing section, keep the description factual, and mention the ambiguity in the handoff. Do not invent a missing catch-all section.

## Insert Command

Run from the repository root:

```powershell
python .agents\skills\add-research-link\scripts\insert_readme_entry.py `
  --section-en "Benchmarks for research agents" `
  --section-zh "科研智能体评测基准" `
  --name-en "ExampleBench" `
  --name-zh "ExampleBench" `
  --url "https://example.com/examplebench" `
  --desc-en "A benchmark for evaluating research agents on example scientific tasks." `
  --desc-zh "用于评估科研智能体处理示例科学任务能力的基准。"
```

Use `--dry-run` first when the section choice or generated text is uncertain.

## GitHub Star Counts

- Add a Star marker only when the resource URL identifies a GitHub repository.
- Use this exact linked form after the project link:

  ```markdown
  [<!--stars:OWNER/REPO-->⭐&nbsp;updating<!--/stars-->](https://github.com/OWNER/REPO)
  ```

- Keep the marker in both READMEs with the same case-sensitive `OWNER/REPO` value.
- Never add Star metadata to project pages, papers, blogs, or non-GitHub resources.
- Never hand-edit a resolved count. `scripts/update_stars.py` and `.github/workflows/update-stars.yml` own the displayed number.
- Treat `⭐ updating` as a temporary fallback, not a fabricated count.

## Rules

- Modify only `README.md` and `README_zh.md` for ordinary link additions; the shared Star updater and workflow are repository infrastructure, not per-entry files.
- Do not create a new category unless the user explicitly asks for taxonomy changes.
- Preserve existing order and append to the end of the chosen section.
- Do not duplicate an existing URL. If the URL is already present, report the existing location instead of adding another entry.
- Keep English and Chinese entries aligned: same category, same project, matching meaning.
- Keep descriptions brief and source-grounded. Avoid unsupported claims such as "best", "first", or "SOTA" unless the linked source explicitly says so.
