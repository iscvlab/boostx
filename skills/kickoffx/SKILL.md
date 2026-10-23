---
name: kickoffx
description: >
  Synthesize end-of-session progress, verify doc synchronization, present next-step options, and generate a pristine kickoff prompt for a fresh conversation (/kickoffx, /kickoff).
  Use when wrapping up a session, starting a fresh chat, transitioning after context compaction, or running /kickoffx.
  Do NOT use for diagnosing context health (/contextx), mid-session doc rewriting (/syncx), or skill authoring (/create-skillx).
---

# `/kickoffx` (Session Transition & Kickoff Prompt Synthesizer)

Prepare a seamless, zero-loss transition from a compacted or ending conversation into a **pristine fresh conversation**.

This skill performs a three-way bridge:
1. **Doc Sync Verification**: Ensures decisions made in this session are committed to documentation before exiting.
2. **Strategic Options Formulation**: Analyzes active roadmaps to offer 2–3 structured next-step paths.
3. **Pristine Kickoff Prompt Generation**: Assembles a self-contained prompt block containing locked invariants, active file paths, and task-matched `-x` slash commands (`/briefx`, `/planx`, `/researchx`, `/deep-researchx`, `/layax`, `/obsidianx`, `/boostx`, `/ultrax`, `/goal`) for the new chat.

Portable across Antigravity IDE, `agy` CLI, Claude Code, Cursor, and multi-agent platforms across Windows, macOS, and Linux.

Red failure modes to prevent:
1. Leaving uncommitted, unsynchronized facts behind when starting a fresh chat.
2. Giving a vague or underspecified prompt to the new agent, forcing it to guess the context or hallucinate previously resolved decisions.
3. Losing hard-won negative constraints or locked invariants (e.g. structural cardinalities, frozen sections, styling protocols) across the chat boundary.
4. **Accidental In-Chat Execution Trap**: Treating a user's option selection (`"Option A"`, `"Option B"`, `"1"`, etc.) after `/kickoffx` as a command to *execute* that task inside the current exhausted chat, instead of generating/updating the Kickoff Prompt for the new chat.

---

## Strict Terminal-Session Guardrail (Anti-Execution Invariant)

> [!CAUTION]
> **ONCE `/kickoffx` IS INVOKED, THIS CHAT IS IN TERMINAL HANDOFF MODE.**
> - When the user replies to a `/kickoffx` turn with an option choice (e.g., `"Option A"`, `"Option B"`, `"2"`) or a refinement (e.g., `"also mention X"`, `"don't lock Y yet"`), you **MUST NEVER** start executing that task in the current chat.
> - Your **ONLY** action upon receiving the user's selection or refinement is to **write (or rewrite) the Pristine Kickoff Prompt** tailored to that selection so the user can copy-paste it into a fresh conversation.

---

## When Not to Use

| Need | Use Instead |
| :--- | :--- |
| Check current context compaction round or memory health | [`/contextx`](../contextx/SKILL.md) |
| Deep multi-file document synchronization sweep | [`/syncx`](../syncx/SKILL.md) |
| Create an implementation plan inside an active session | [`/planx`](../planx/SKILL.md) |
| Run primary-source or 5-wave deep research | [`/researchx`](../researchx/SKILL.md), [`/deep-researchx`](../deep-researchx/SKILL.md) |
| Author or distill a skill | [`/create-skillx`](../create-skillx/SKILL.md) |
| Regular task briefing inside an active chat | [`/briefx`](../briefx/SKILL.md) |

---

## Standard Operating Procedure (Smart Hybrid 2A Routing)

### Step 1: Pre-Handoff Sync Gate (Zero Stale State)

Before formulating the next session's work, verify that the current conversation's outputs are safely recorded on disk:

1. Check `git status --short` (or recent file edits) to identify modified, untracked, or staged files.
2. Verify that active documentation accurately reflects the latest decisions made in this session.
3. If documents were edited or spatial/quantitative metrics were recalculated, confirm that [`/syncx`](../syncx/SKILL.md) verification has been completed (and if `/obsidianx` was used in the session, confirm reusable domain knowledge was ratcheted).
4. *Sync Guard*: If uncommitted or unsynced state exists, advise the user or sync it before finalizing handoff.

---

### Step 2: Smart Hybrid 2A Routing (Explicit Topic vs. Bare `/kickoffx`)

Determine which path applies based on how the user invoked `/kickoffx`:

#### Path A — Explicit Topic Provided (e.g. `/kickoffx <task>` or `"write /kickoffx so I can discuss X"`)
- **Zero Redundant Option Prompting**: Because the user has already stated what they want to do in the next chat, do **NOT** stop to ask them to pick an option, and do **NOT** clutter the response with competing options that distract from their chosen focus.
- Proceed **directly to Step 3** and output the **Pristine Kickoff Prompt** for their specified topic in the **same turn** (1-turn completion).
- If the user replies afterward with adjustments or scope tweaks, **rewrite the Kickoff Prompt** with those adjustments (never execute the task in the current chat).

#### Path B — Bare `/kickoffx` Invoked Without a Specific Topic (`Select Option First → Write Kickoff Later`)
1. **Turn 1 (Formulate & Ask Options ONLY — Do NOT Write the Kickoff Prompt Yet)**:
   - Analyze the active workspace roadmap, master plan, or presentation deck to formulate **2–3 clear, high-impact options** for the next conversation:
     * **Option A (Recommended — Direct Continuation)**: The immediate next logical subsection, slide, module, or task on the active roadmap.
     * **Option B (Technical Deep Dive / Parallel Scope)**: Evidence modeling, script execution, simulation, or multi-slide pairing.
     * **Option C (Bookmark Polish / Synthesis)**: Returning to bookmarked cards/maps, visualization polish, or executive review.
   - Present the options concisely (using the `ask_question` tool if available, or a clean numbered/lettered list in chat) and ask: *"Which focus would you like me to write the `/kickoffx` prompt for?"*
   - **STOP and end the turn without generating the long Kickoff Prompt block yet** (saves context tokens and avoids writing the wrong prompt).
2. **Turn 2 (User Selects Option → Write the Pristine Kickoff Prompt)**:
   - Once the user selects `Option A`, `Option B`, `Option C`, or states a custom focus, proceed immediately to **Step 3** and generate the **Pristine Kickoff Prompt** for that exact choice.
   - **Strictly obey the Terminal-Session Guardrail**: Do **NOT** execute the selected option in this chat; only output the Kickoff Prompt for the new chat!

---

### Step 3: Pristine Kickoff Prompt Synthesis & Smart Command Selector

#### A. Task-Smart Recommended Execution Command Selector
Select the exact `-x` slash command pipeline for the bottom of the Kickoff Prompt based on the next session's workload (avoiding unnecessary PyTorch cold-start when files are already pinned, while activating [`/layax`](../layax/SKILL.md) whenever semantic triage or contradiction hunting is needed):

| Next Session Task Archetype | Recommended Command Line to Generate |
| :--- | :--- |
| **Standard Build / Debug / CAD / UI** *(Target files already pinned)* | `/briefx "[Topic Name]" /boostx /goal` |
| **Architecture & Design Decision First** *(Needs inline grilling plan)* | `/briefx "[Topic Name]" /planx` |
| **Tactical API / Formula / DB Lookup → Implementation** | `/briefx "[Topic Name]" /researchx /boostx /goal` |
| **Multi-File Doc Sync / Semantic Conflict Audit** | `/briefx "[Topic Name]" /syncx /layax` |
| **Large Unpinned Corpus / Deep Research / Dataset Triage** | `/deep-researchx /layax "[Topic Name]" /boostx /goal` *(or `/briefx /layax`)* |
| **High-Complexity Swarm / Best-of-3 Tournament / Multi-Agent Batch** | Append `/ultrax` (e.g., `/briefx "[Topic Name]" /boostx /ultrax /goal` or `/deep-researchx /boostx /ultrax /goal`) |
| **Any Task Reading or Ratcheting Second Brain Knowledge** | Append `/obsidianx` (e.g., `/briefx "[Topic Name]" /boostx /obsidianx /goal`) |

#### B. 5-Part Kickoff Prompt Architecture
Generate a self-contained, copy-pasteable prompt block formatted inside a fenced markdown code block:

````markdown
```markdown
# Objective: [Concise Task Title]

## Role & Operating Protocol
Operate as a Principal [Domain / Systems] Architect & Lead Engineer.
- Language Mode: [Primary Language or Bilingual Mode] (Maintain throughout this entire chat, zero language drift).
- Chat Panel Cleanliness: Strictly NO Mermaid blocks or LaTeX math ($) inside the agent chat bubble (use clean GFM tables/bullets in chat). Mermaid diagrams are supported in .md files and artifacts only.
- Formatting Standards: Native Unicode symbols only (→, •, ✓, ², etc.), GFM tables with outer boundary pipes.

## Scope & Target Files
- `[Primary File]` (Active document or module to edit or review)
- `[Reference Spec]` (SSOT / Master Roadmap)

## Locked Invariants & Session Decisions (DO NOT RE-ARGUE OR DRIFT)
1. [Core Decision 1 established in previous session, e.g. exact framework cardinality: 6 Acts / 4 Tiers]
2. [Negative Invariant: e.g. Do not touch frozen sections / Do not lock open deliberation items prematurely]
3. [Architectural, Styling, or Performance Invariant: e.g. design tokens, unit bridges, O(N) runtime bounds]

## Immediate Next Task
[Detailed, actionable instructions for what the agent should accomplish first in this new session].

## Recommended Execution Command
[Selected Task-Smart Command from Table 3.A, e.g.: /briefx "[Topic Name]" /boostx /goal]
```
````

### Step 4: Exit Checklist & User Guidance

Deliver the final instructions to the user:
1. **Copy the Kickoff Prompt**: Highlight the code block above for quick copying.
2. **Start Fresh Chat**: Direct the user to open a new conversation window in the IDE.
3. **Paste & Run**: Paste the block into the new chat and press Enter.
4. **Optional Adjustments**: Remind the user: *"If you want any tweaks to this kickoff prompt, reply here and I will rewrite the prompt block for you."*

---

## Quality Rubric

- [ ] Current session state verified against `git status` and documentation.
- [ ] **Smart Hybrid 2A Routing enforced**:
  - If explicit topic given → wrote Kickoff Prompt immediately in 1 turn without redundant option questioning.
  - If bare `/kickoffx` given → presented Options A/B/C first (`ask_question` or concise list) and waited for selection before generating the Kickoff Prompt.
- [ ] **Strict Terminal-Session Guardrail enforced**: Never executed the chosen option inside the current chat; treated option selection strictly as a directive to write/rewrite the Kickoff Prompt.
- [ ] **Task-Smart Command Selector applied**: Included `/layax`, `/planx`, `/researchx`, `/deep-researchx`, or `/obsidianx` when matched to the next session's workload, while keeping pinned-file build kickoffs lean (`/briefx "[Topic]" /boostx /goal`).
