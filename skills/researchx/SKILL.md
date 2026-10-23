---
name: researchx
description: >
  Primary-source research, local SDK/DB/binary inspection, and cited architecture study protocol (/researchx).
  Use when running /researchx, verifying APIs or physics constants, inspecting local packages/files, or benchmarking architectures.
  Do NOT use for workspace briefing (/briefx), bug repro (/diagnosing-bugs), or doc sync (/syncx).
---

# Antigravity ResearchX Protocol (`/researchx`)

When `/researchx` is invoked or high-rigor primary-source investigation is required, enter the **Antigravity ResearchX Protocol**. ResearchX is the fast tactical investigative counterpart to [`/boostx`](../boostx/SKILL.md): it replaces secondary-blog guesswork and context-bloating raw dumps with **version-pinned primary sources, direct local binary/DB/AST inspection, capability-aware subagent routing, and `/briefx`-ready Markdown architecture studies**.

> **Escalation to [`/deep-researchx`](../deep-researchx/SKILL.md)**: For exhaustive multi-agent precedent/dataset harvesting, blind adversarial fact-auditing, or 5-wave multi-system synthesis with `verify_evidence.py`, escalate to [`/deep-researchx`](../deep-researchx/SKILL.md).

---

## 1. Execution Routing & Subagent Capability Gate

Match execution topology to research scope and host subagent capabilities in Step 0:

### A. 3-Tier Scope & Parallelism Routing

| Tier | Scope & Trigger Condition | Execution Strategy |
| :--- | :--- | :--- |
| **Tier 1 — Fast Inline Probe** | ≤ 2 known sources, single API signature check, or quick local manifest/SQLite/XML schema probe. | Execute directly in the main thread (`read_file` / `view_file`, `read_url_content`, `search_web`, or 1-liner Python stdlib inspection). **Zero subagent cold-start latency.** |
| **Tier 2 — Single Isolated Scout** | Deep single-topic investigation requiring 3+ docs, upstream code tracing, or heavy web reading. | Spawn **1 background subagent** so raw search/file dumps stay out of the main context window. |
| **Tier 3 — Parallel Multi-Angle Swarm** | Comparing ≥ 2 libraries/architectures, or investigating **Local Pinned Code + External Specs + Empirical Benchmarks** simultaneously. | Spawn **2–3 concurrent subagents** via parallel `invoke_subagent` calls in the same turn (one per angle/library), then synthesize into a single comparative Markdown report. |

### B. Host Subagent Write-Permission & Return Contract
In multi-agent runtimes (Antigravity IDE, `agy` CLI, Claude Code), prevent **Read-Only Subagent Deadlocks** and **Main-Context Bloat**:
1. **Capability-Aware Subagent Selection**:
   * **Direct-Write Subagent (`TypeName="self"` in Antigravity / `general-purpose` in Claude Code)**: Use when the subagent should both investigate *and* write the Markdown report directly to disk.
   * **Read-Only Subagent (`TypeName="research"` in Antigravity / `Explore` / `cavecrew-investigator`)**: Has **read-only tools** (`enable_write_tools=false`). Never instruct a read-only subagent to save files; instead, instruct it to return a structured citation payload so the main thread writes the Markdown file.
2. **Compressed Return Contract (`/cavecrew` Discipline)**:
   * When a subagent writes the research Markdown file to disk, its reply message back to the main thread **MUST NOT paste the full Markdown report**.
   * Return **≤ 150 words** containing only:
     1. `Saved Path`: Clickable `[filename.md](file:///...)`
     2. `TL;DR Verdict`: 3–5 bullet conclusions with exact version/source citations
     3. `Open Gaps`: Any unverified claim or recommended `/prototype` spike
3. **Causality & Anti-Timeout Turn Rule**:
   * **Parallel Safe**: Keep working in the main thread *only* if you have strictly independent tasks that do not depend on the research answer.
   * **Dependency Blocked**: If the next code edit or architectural decision depends on the research result (e.g., `/boostx` Section 4.B escalation), **never write speculative code while waiting**. Launch the subagent and **end your turn immediately** to wait for reactive wakeup.

---

## 2. Synthesize the 2D Research Contract (`Step 0`)

Select the active **Research Archetype** and cross it with the **Domain Source Harness**:

| Research Archetype | Target Primary Evidence & Completion Proof |
| :--- | :--- |
| **`API / SDK / VERSION`** *(Signatures / Breaking Changes)* | Lock exact pinned version in local manifests first → verify exact method signatures, parameter types, return schemas, and deprecation boundaries against source/types + official version-matched docs. |
| **`REVERSE-ENGINEER / ASSET / DB`** *(Local Packages / SQLite / XML / CAD)* | Inspect installed binaries, SQLite databases, XML/JSON definitions, `.3dm`/`.gh` assets, or `.dll`/`.whl` symbols directly via non-destructive Python stdlib / CLI probes (`sqlite3`, `xml.etree.ElementTree`, `zipfile`, `inspect`, `rhino3dm`). Measure exact counts, schemas, and geometric invariants. |
| **`SIMULATION / PHYSICS / SOLVER`** *(Formulas / Units / Constants)* | Lock governing mathematical equations, dimensional unit bridges (`mm`/`cm`/`m` ↔ SI `m`/`kg`/`s`/`N`/`W/m²`, `deg` ↔ `rad`), empirical coefficients, and stability bounds (CFL `dt`, convergence `ε`) from standards (ISO/EN/ASHRAE) or peer-reviewed literature. |
| **`ARCHITECTURE / BENCHMARK`** *(Compare 2–4 Systems / Tools)* | Build an end-to-end `mermaid` architectural comparison diagram + a quantitative feature/performance trade-off matrix isolating bottlenecks in reference systems vs. our design advantage. |
| **`UPSTREAM BUG / SPEC TRACE`** *(Undocumented Behavior / Edge Cases)* | Trace behavior past prose docs directly into upstream repository source code, test suites, RFCs, PRs, and maintainer issue comments. |

State the compact contract before probing:
> **🔬 ResearchX Contract** — `[Research Archetype]` × `[Target Stack & Version]` (`Tier 1|2|3`)
> • **Core Question**: <Exact technical question or decision to resolve>
> • **Primary Sources**: <Pinned local manifests/binaries/DBs + Tier 1–3 external specs>
> • **Output Artifact**: `<Resolved save path>`

---

## 3. The 4-Tier Primary-Source Authority Ladder

Follow every technical claim back to the source that owns it. Rank evidence strictly by this hierarchy:

1. **Tier 1 — Local Pinned Ground Truth (Highest Authority)**:
   * **Manifests & Lockfiles**: Always inspect `package.json`, `pnpm-lock.yaml`, `pyproject.toml`, `requirements.txt`, `*.csproj`, or `metadata.txt` **first** so you never research v5 docs for a repo pinned to v3.
   * **Installed Code, Types & Local Databases**: Inspect `.d.ts` type definitions, `.venv`/`node_modules` source, C# assemblies, or local `.sqlite`/`.xml`/`.3dm` files on disk. Local runtime truth beats outdated documentation.
2. **Tier 2 — Version-Matched First-Party Specs & Official Documentation**:
   * Official API references, language specifications, W3C/IETF RFCs, and vendor docs matching the target version (`read_url_content`, `search_web`, or Python `urllib`).
3. **Tier 3 — Upstream Source Code, Test Suites & Issue Trackers**:
   * Canonical upstream repository source files (`file:line`), unit tests (which prove actual expected inputs/outputs), release notes, and maintainer issue threads.
4. **Tier 4 — Engineering Standards & Peer-Reviewed Literature**:
   * Published standards (e.g., EN 12261, ASHRAE, Eurocode, Hydrology manuals) and primary papers for physical constants and numerical algorithms.

> [!IMPORTANT]
> **Zero Secondary-Slop Rule**:
> Secondary blog tutorials, SEO summaries, and unverified forum guesses are **leads, never citations**. If a secondary post points to a flag or API, verify it in Tier 1–3 before recording it as fact. If a claim cannot be verified against a primary source, label it **`[UNVERIFIED]`**.

---

## 4. Deterministic Save Location & Note Architecture

### A. 3-Step Save Destination Fallback
Never drop loose `.md` files into a repository root (preserving clean `git status` and BoostX scratch hygiene):
1. **Explicit or Existing Repo Convention**: Use the user-specified path, the path declared in `CONTEXT.md` / `AGENTS.md`, or an existing `docs/research/`, `docs/notes/`, or `research/` folder.
2. **Default Repository Path**: If inside a project workspace with no existing folder, save to `docs/research/YYYY-MM-DD-<topic-slug>.md` (or `RESEARCH_<TOPIC_SLUG>.md` when matching an existing uppercase root/docs convention).
3. **Workspace-less / Ephemeral Session Fallback**: When no active repository is open (or the user wants a standalone study without touching repo files), write to `<artifactDir>/RESEARCH_<TOPIC_SLUG>.md` and surface a clickable `file://` link.

### B. `/briefx`-Ready Research Note Schema
Structure every saved Markdown file so both humans and downstream [`/briefx`](../briefx/SKILL.md) (Pass A structural skeleton reads), `/planx`, and [`/boostx`](../boostx/SKILL.md) runs can consume it in seconds:

```markdown
# Primary-Source Research: <Title>

> **ResearchX Metadata**:
> - **Question**: <1-sentence question>
> - **Target Stack / Version**: <e.g., PyQGIS 3.34 / Qt6 | RhinoCommon 8.x | BigQuery SQL>
> - **Status**: `VERIFIED` | `PARTIALLY VERIFIED` | `CONFLICTING SOURCES`
> - **Primary Sources Inspected**:
>   1. `[Local/Upstream Source 1](file:///... or https://...)` (<exact version / scope>)
>   2. `[Official Spec / DB 2](file:///... or https://...)`

---

## 1. Executive TL;DR & Decision Verdict
* **Direct Answer**: <1–2 sentence bottom-line conclusion>
* **Key Architectural Invariants**: <3–5 bullet takeaways with inline source citations>

## 2. Architecture / Mechanism Breakdown
*(Include a `mermaid` flowchart/sequence diagram when mapping multi-component data flows or comparing reference vs. target architectures.)*

| Claim / Parameter / API | Primary Source Citation (`file:line` / URL) | Verified Behavior & Constraints | Engineering Implication |
| :--- | :--- | :--- | :--- |
| `<Symbol / Constant>` | `[source](...)` | `<Exact types, units, or edge cases>` | `<How our implementation must use it>` |

## 3. Contradictions, Unknowns & Next Action
* **Doc vs. Code Discrepancies**: <Where official docs disagreed with actual source/runtime behavior, if any>
* **Unresolved Gaps (`[UNVERIFIED]`)**: <Questions primary sources did not answer>
* **Recommended Next Step**: <Ready for `/boostx` implementation | Needs `/prototype` throwaway test | Needs `/planx` architectural decision>
```

### C. Composable `/layax`, `/planx`, `/boostx` & Opt-In `/obsidianx` Pipelines
* **Default Isolation Rule (Without `/obsidianx`)**:
  * When `/obsidianx` is **not** in the user's command (e.g., `/researchx` or `/researchx /boostx /goal`), **never** read from or write to any Obsidian vault.
* **Paired with [`/layax`](../layax/SKILL.md) (`/researchx /layax`)**:
  * Use `/layax` (`score` / `shortlist_choice`) to locally shortlist candidate docs or API sections before reading full specifications.
* **Paired with [`/ultrax`](../ultrax/SKILL.md) (`/researchx /ultrax`)**:
  * Force **Tier 3 Parallel Multi-Angle Swarm** (`2–4` concurrent primary-source scouts) plus a dedicated **Blind Adversarial Verifier** subagent (`Maker ≠ Checker`) that independently audits every cited signature, version, and formula before synthesis.
* **Paired with [`/planx`](../planx/SKILL.md) (`/researchx /planx`)**:
  * Pass verified primary-source API signatures and constraints directly into `/planx` Phase 1 to construct `implementation_plan.md`.
* **Paired with [`/boostx`](../boostx/SKILL.md) (`/researchx /boostx` or `/researchx /boostx /goal`)**:
  * **Spec-to-Code Bridge**: Once `/researchx` locks the verified primary-source API signature, governing equation, SI unit bridge, or closed-form analytical benchmark, pass that exact contract directly into **BoostX Phase 1** as the falsifiable Red → Green verification signal.
* **Paired with [`/obsidianx`](../obsidianx/SKILL.md) (`/researchx /obsidianx` or `/researchx /boostx /obsidianx`)**:
  1. **Step 0 Tier-1 Second Brain Cache**: Dynamically resolve `VAULT_ROOT` via [`/obsidianx`](../obsidianx/SKILL.md) (`obsidian.json` / `.obsidian/` marker) and inspect `00 *Index*.md` → `Hub - *.md` first so already-verified formulas, precedents, or component specs are reused without redundant external web searches.
  2. **Automatic Knowledge Ratchet**: After saving the repository research report, automatically mint or update the corresponding reusable atomic note(s) and `Hub - *.md` table inside `VAULT_ROOT` (enforcing unique `[[wikilink]]` neighbor signatures) and run the 1-line Vault Graph Integrity check (`BROKEN=0`, `ORPHANS=0`, `DUP_NEIGHBOR_GROUPS=0`).

---

## 5. Verification & Completion Rubric

Before declaring `/researchx` complete, verify every checkpoint:

- [ ] **Version & Local Truth Checked First**: Pinned workspace versions (`package.json`, `pyproject.toml`, `*.csproj`, `metadata.txt`) or local binaries/DBs were checked before external web search.
- [ ] **100% Primary-Source Citations**: Every technical claim links to a Tier 1–4 primary source (`file:///...#L10-L20` or canonical `https://...` URL); zero secondary blog posts cited as proof.
- [ ] **Quantitative & Structural Clarity**: Complex comparisons include a `mermaid` diagram and a structured Markdown evidence table using clean Unicode symbols (`→`, `×`, `≈`, `±`, `≤`, `≥`, `✓`).
- [ ] **Clean Destination Hygiene**: Saved to existing repo convention, `docs/research/`, or `<artifactDir>`—never polluting the repository root with untracked scratch debris.
- [ ] **Opt-In Composable Ratchet Verified**: If `/obsidianx` was included in the command, reusable domain findings were ratcheted into the resolved vault with `0` broken links and `0` duplicate neighbor sets (and untouched if `/obsidianx` was omitted).
- [ ] **Context-Compressed Main Thread**: If delegated to a subagent, the main thread received a concise digest (`≤ 150 words` + clickable file link) rather than a duplicate multi-thousand-word raw dump.

