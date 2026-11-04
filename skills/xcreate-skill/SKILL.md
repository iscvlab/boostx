---
name: xcreate-skill
description: >
  Build, distill, evolve, and audit global agent skills with universal laws (/xcreate-skill, /create-skill).
  Use when running /xcreate-skill or /create-skill, or when creating, distilling, upgrading, evolving, or auditing
  global agent skills. Do NOT use for workspace doc sync (/xsync) or package release checks (/xpublish-audit).
---

# Antigravity Skill Creator & Universal Law Auditor (`/xcreate-skill`)

Authoring, distilling, evolving, and verifying production-grade global agent skills across **Antigravity IDE**, **Antigravity CLI (`agy`)**, **Claude Code**, and cross-platform multi-agent environments.

This skill synthesizes four core frameworks:
1. **The [`/xboost`](../xboost/SKILL.md) Protocol**: 4-phase engineering lifecycle (Red Invariant Gate → Ponytail × 5-Gate Universal Law Filter → Dual-OS Surgical Build → Ruthless 3-Tier Verification).
2. **`writing-great-skills` Discipline**: Information hierarchy, progressive disclosure, leading words, single-source-of-truth (`SSOT`) co-location, and context-load vs. cognitive-load optimization.
3. **The 5-Gate Universal Law Falsification Protocol**: Pre-proposal counter-domain stress testing (`Archetypes A × B × C`), Agent-Process vs. Domain-Equation separation, and mathematical boundary auditing so project-specific equations or scripts never leak into global skills.
4. **Universal Cross-Platform Globalization**: Physical directory allocation, dual-OS path normalization (Windows PowerShell + macOS/Linux bash), and zero-breakage cloud synchronization (OneDrive / Google Drive).

---

## 1. Scope & Universal Globalization Policy

Every agent skill authored or upgraded via `/xcreate-skill` **MUST reside in the Global Customizations Root** so that it is instantly accessible across **every workspace** and synchronized across **every device** (Windows, macOS, and Linux workstations):

| Target Path | Physical Cloud Storage | Behavior Across Workspaces & Devices |
| :--- | :--- | :--- |
| **`~/.gemini/config/skills/<skill-name>/`** | **OneDrive (`gemini-config/skills/<name>/`)**<br>• Windows: `C:\Users\<User>\OneDrive\gemini-config\skills\<name>\`<br>• macOS: `~/Library/CloudStorage/OneDrive-Personal/gemini-config/skills/<name>/` | **Universal Globalization**: Automatically loaded into every workspace on all machines. Real-time background sync via OneDrive. Zero git-push or symlink chore required. |

> [!IMPORTANT]
> **The Universal Globalization Invariant (Zero Project-Local Silos)**:
> Never create skills inside a workspace-local `.agents/skills/<name>/` folder. Local project skills become isolated silos that are invisible when opening other repositories, and they cause version drift between machines. Always write directly to `~/.gemini/config/skills/<name>/`.

> [!IMPORTANT]
> **The NTFS Junction & Real Directory Rule**:
> When authoring global skills on Windows where `~/.gemini/config` is an NTFS junction to `OneDrive\gemini-config`, **always create real directories** inside `skills/<name>/`. Never create nested secondary junctions, as IDE file watchers and Node.js globbers refuse to traverse recursive reparse points.

> [!TIP]
> **Global Git Ledger & Rollback Protection (Dual-OS)**:
> The global config root is version-controlled via Git. After creating or updating a skill, commit the change:
> - **macOS / Linux**:
>   ```bash
>   git -C ~/.gemini/config add -A && git -C ~/.gemini/config commit -m "feat(skills): update <skill-name>"
>   ```
> - **Windows (PowerShell)**:
>   ```powershell
>   git -C "$env:USERPROFILE\.gemini\config" add -A; git -C "$env:USERPROFILE\.gemini\config" commit -m "feat(skills): update <skill-name>"
>   ```

---

## 2. Ingestion Modes (`Mode A`, `Mode B`, `Mode C`)

Operate in one of three distinct modes based on user intent:

### Mode A: Session Workflow Distillation ("Make this a new skill")
* Triggered when the user says *"make this a skill"*, *"package what we just did"*, or *"turn this workflow into a reusable skill"*.
* Reads the active conversation history / transcript (`transcript.jsonl`), extracts the sequence of successful commands, tool calls, and output schemas, strips debugging detours, and synthesizes a repeatable workflow skill.

### Mode B: Greenfield Domain / Tool Architecture ("Create a skill for X")
* Triggered when building a brand-new skill from an API, library documentation, standard, or domain (e.g., QGIS analysis, Grasshopper solver, Docx processing).
* Conducts a focused, non-bloated 3-question interview (`Intent`, `Tools/Inputs/Outputs`, `Edge Cases`).

### Mode C: Post-Session Skill Evolution, Universal Law Ratchet & Ecosystem Audit ("Upgrade existing skills with what we learned")
* Triggered when the user asks to **inspect what can be learned from a session to upgrade existing skills** (e.g., [`/xboost`](../xboost/SKILL.md), [`/xdeep-research`](../xdeep-research/SKILL.md), [`/xultra`](../xultra/SKILL.md), [`/xplan`](../xplan/SKILL.md), [`/xsync`](../xsync/SKILL.md)) or asks to **re-audit existing skills** for universal applicability and conflicts.
* **Mandatory Pre-Proposal Abstraction Sieve (Run BEFORE Suggesting in Chat)**:
  To prevent **Session Hangover / Recency Bias** (proposing disguised project equations or project-specific scripts), every candidate lesson must pass four pre-proposal steps before you present it to the user:
  1. **Agent-Process Law vs. Domain-Equation Inversion**:
     * Core `/x*` skills govern **how the AI agent investigates, plans, verifies, and orchestrates subagents**—they are **NOT** domain physics/finance textbooks.
     * Never copy a project's domain equation into a global skill. Instead ask: *"What flaw in the AI agent's reasoning or verification process allowed this bug to happen, and what universal verification step prevents it across all domains?"*
  2. **The Global CLI Script Ban**:
     * **Never** propose adding a project-specific helper script (or domain-specific CLI check) into `~/.gemini/config/skills/<skill>/scripts/*.py`. Global skill scripts may only operate on universal primitives shared across all projects (`.md` links, `.json` schemas, `.pdf` OCR, `git` diffs, Python AST security, SQLite transcript telemetry). Keep domain scripts inside the project repository's own `scripts/` folder.
  3. **Mandatory "Pruned Project-Specific Ideas" Ledger in Chat**:
     * In your chat proposal to the user, explicitly list the session lessons/scripts you **rejected (`PRUNED — Project-Specific`)** and explain where they belong instead (project `docs/` or domain vault notes) before presenting surviving universal upgrades.
  4. **Mandatory 3-Domain Translation Proof Table in Chat**:
     * For every proposed universal upgrade, include a 3-column proof table in chat demonstrating how the exact rule applies naturally to **(A) Continuous / Stateful Solver & CAD/Physics**, **(B) Discrete / Web UI / API / CRUD**, and **(C) Non-Code Research / Docs / Knowledge Graph**. If any column feels forced or meaningless, **reject or context-condition (`When [Condition C] holds: ...`)** the rule before proposing it!

---

## 3. The 4-Phase XBoost Skill Creation & Evolution Lifecycle

```mermaid
flowchart TD
    P1["Phase 1: THE RED INVARIANT & PRE-PROPOSAL GATE\n(Failure Mode, Agent-Process Inversion, 2 Trigger Probes)"] --> P2["Phase 2: PONYTAIL LADDER & 5-GATE UNIVERSAL LAW FALSIFICATION\n(3-Bucket Numerics + 3-Domain Stress Test + 7-Point Math Audit + SSOT Owner)"]
    P2 --> P3["Phase 3: DUAL-OS SURGICAL EXECUTION\n(Front-loaded SKILL.md <= 500 lines, POSIX paths, UTF-8 header)"]
    P3 --> P4["Phase 4: RUTHLESS 3-TIER VERIFICATION\n(Static YAML Lint, Live CLI Counter-Anchor Probe, audit_engine.py)"]
```

---

### Phase 1: The Red Invariant Gate (Pre-Creation / Pre-Upgrade)

Answer these three questions before drafting or proposing edits:

1. **What is the Red Agent Failure Mode?**
   * What does the AI agent get wrong without this skill or rule? (e.g., trusts green linters without calling the live entrypoint, extrapolates outside bracketed bounds, spawns redundant subagents, fails on cross-platform paths).
2. **Invocation Decision (Context Load vs. Cognitive Load)**:
   * **Model-Invoked** (Default): Keeps a rich `description` (`≤ 400` chars target) with leading words, positive triggers, and an explicit `Do NOT use for...` exclusion clause. Contributes context load every turn; agent can trigger it autonomously.
   * **User-Invoked**: Set `disable-model-invocation: true`. Note that `description` is **still mandatory in YAML frontmatter** (write a concise 1-line human-facing summary; positive/negative trigger clauses become optional).
     > [!WARNING]
     > **`disable-model-invocation: true` suppresses prompt context**: In Antigravity IDE, setting this flag completely strips the skill from the agent prompt's `<skills>` catalog. Only set this for manual user-typed commands.
3. **Bidirectional Trigger & Behavioral Probes (`A_pos ∧ A_neg`)**:
   * **Positive Probe (`A_pos`)**: A prompt or input fixture that *must* trigger/pass the skill or rule.
   * **Negative Counter-Anchor (`A_neg`)**: A related out-of-scope prompt or counter-domain fixture that *must NOT* falsely trigger or break under the rule.

---

### Phase 2: Ponytail Ladder, 3-Bucket Numeric Rule & 5-Gate Universal Law Falsification

#### A. The Ponytail Senior Dev Filter (Rungs 1–4)
* **Rung 1 (YAGNI / Rule Check)**: Does this actually need a new skill or rule? If the model already obeys it by default (**No-Op** in `writing-great-skills`), delete it.
* **Rung 2 (Tool & SSOT Reuse)**: Do native tools, MCP servers, or an existing owner skill already cover this? If yes, point to the existing owner (`[label](../xboost/SKILL.md)`) rather than duplicating prose.
* **Rung 3 (Structure Selection)**: Choose **Workflow Archetype** (ordered steps + completion criteria), **Task Toolkit Archetype** (independent sub-actions), or **Reference Archetype** (flat peer rules).
* **Rung 4 (Code vs. No-Code)**: Default to **Pure Instruction (Zero Code)**. Only add `scripts/<name>.py` for deterministic, 100% domain-agnostic parsing/auditing using Python stdlib (`argparse`, `pathlib`, `json`, `re`, `ast`).

#### B. Core Invariant 1: The 3-Bucket Numeric Litmus Test & Zero-Persona Neutrality
Classify every numeric bound (`≤ N`, `N..M`, `< N`) into one of three buckets:
1. **Bucket 1 — Physical / Platform Constants (Keep & Cite Source)**: Hardware, model, or runtime limits (`512`-token `ModernBERT` window, `< 30s` synchronous tool timeout, `2-Hop` GraphRAG diameter, `≤ 400`-char target / `≤ 500`-char advisory YAML description budget, `≤ 500`-line `SKILL.md` progressive disclosure budget).
2. **Bucket 2 — Per-Window Cognitive Working-Set Bounds (Keep Per Window, Scale via `/xultra` Shards)**: Per-thread reading caps (such as `/xbrief`'s `8`-file Pass-B cap per single context window) paired with horizontal [`/xultra`](../xultra/SKILL.md) shard scaling when corpus size exceeds one window.
3. **Bucket 3 — Arbitrary Task / Subagent Quotas, Snapshot Counts & Persona Leaks (Strictly Forbidden)**: Never hardcode fixed subagent headcounts (`3+2`, `4–12`, `2–4 scouts`), arbitrary output word/line caps (`≤ 150 words`, `1–2 notes`, `< 30 lines`), transient dataset row counts (`14,203 rows`), or personal hardware/persona strings into global skill instructions.

#### C. Core Invariant 2: The 5-Gate Universal Law Falsification Protocol
Whenever Mode A or Mode C distills a rule, mathematical invariant, or verification probe into any global skill, it **MUST pass all 5 gates in order**:

| Gate | Falsification Check | Pass / Conditioning / Removal Criterion |
| :---: | :--- | :--- |
| **Gate 1** | **Domain-Jargon & Vocabulary Strip** | Strip 100% of source-project nouns, domain metrics, and filenames. Express strictly in universal systems primitives: `Input/Control (X)`, `Output/Objective (Y, J)`, `Active_Regime(X)`, `Step Measure (Δμ)`, `Candidate Superset vs. Exact Subset (S_cand ⊇ S_exact)`, `Parent vs. Child + Remainder (P = ∪ C_i ∪ P_rem)`. |
| **Gate 2** | **3-Domain Orthogonal Counterexample Stress Test (`Archetypes A × B × C`)** | Test against **(A) Continuous/Stateful Numerical or Physics Solver**, **(B) Discrete/Web UI/API/CRUD System**, and **(C) Non-Code Research/Docs/Knowledge Graph**. If falsified or meaningless on any archetype, either **generalize the formulation** or prefix an explicit **Context-Conditioned Branch Guard (`When [Condition C] holds: ...`)**. |
| **Gate 3** | **7-Point Mathematical & Regime Boundary Audit** *(See Table below & [`deep_audit_protocol.md`](../xboost/references/deep_audit_protocol.md))* | Verify that equations and runtime probes do not fail on affine offsets (`y_eq ≠ 0`), non-zero intercepts (`Y(0) ≠ 0`), intensive measures (means/rates/temps), intentional deadbands/free budget zones (`τ_free`), stateful warmup lookbacks (`W > 1`), IEEE-754 float reductions (`rtol/atol`), or `@decorator` wrappers. |
| **Gate 4** | **Ponytail YAGNI, No-Op & "Delete-Over-Debug" Filter** | Delete rules that (a) the model obeys by default (`No-Op`), (b) force project-specific ceremony (e.g., mandatory `.bat`+`.sh` launchers) onto repos that don't need them, or (c) clash with standard language idioms or global typography rules. |
| **Gate 5** | **Cross-Skill SSOT Co-Location & Pointer-Over-Paste** | Every universal law has **one canonical owner file** (e.g., `UL-01..UL-08` live in [`../xboost/references/deep_audit_protocol.md`](../xboost/references/deep_audit_protocol.md); `N × K × C × T` swarm sizing lives in [`../xultra/SKILL.md`](../xultra/SKILL.md)). Never copy-paste 20-line tables across multiple skills; use a 1–2 line summary + relative **Context Pointer**, and keep `SKILL.md ≤ 500` lines. |

##### Gate 3 Reference: The 7-Point Mathematical & Regime Boundary Table

| # | Boundary Axis | ❌ Forbidden Over-Specific Form | ✅ Mandatory Universal / Context-Conditioned Form |
| :---: | :--- | :--- | :--- |
| **3.1** | **Equilibrium / Intercept** | `x = 0 → y = 0` *(fails on affine offsets `y = mx + b` & Kelvin/ambient baselines)* | **Zero-Forcing Equilibrium (`UL-03`)**: `Δx = 0 ⇒ Δy = 0.0` (or `y == y_eq`) with `0` `NaN`/`Inf`. |
| **3.2** | **Seam Scaling Order** | `d log\|Y\|/d log α == p` or `\|Y(α)/Y(1)\| == α^p` *(fails when `Y(0) ≠ 0` or at clamp walls)* | **Interior Baseline-Subtracted Marginal Scaling (`UL-06`)**: With `ΔY(α) = Y(α) - Y(0)` at `α_1, α_2 ∈ Interior(Dom(α))`, `\|ΔY(α_2) / ΔY(α_1)\| ≈ (α_2 / α_1) ^ p_theory`. |
| **3.3** | **Partition Conservation** | Unqualified `sum(Child) == Parent` *(fails on intensive means/rates/temps & partial matches)* | **Extensive Partition & Remainder Conservation (`UL-04`)**: *For extensive conserved measures*, `abs((∑ μ(C_i) + μ(P_rem)) - μ(P)) <= max(rtol·max(1.0, abs(μ(P))), atol)`. |
| **3.4** | **Parameter Sensitivity** | Unqualified `∀ x, f(x + δ) ≠ f(x)` *(flags intentional deadbands & free budget zones)* | **Active-Regime Sensitivity (`UL-08`)**: `∃ x ∈ Active_Regime(X) : ΔY ≠ 0` (permitting `ΔY == 0` in deadbands and `Penalty = 0.0` inside budgeted free zones `c ≤ τ_free` per `UL-05`). |
| **3.5** | **Prefix Causality** | Memoryless `f(x)[k:] == f(x[k:])` *(fails on stateful filters/EMA/ODEs with warmup `W > 1`)* | **Prefix Causality & Warmup Lookback (`UL-01`)**: `f(x[:T_1])[:t] == f(x[:T_2])[:t]` (`t < T_1 < T_2`), and finite-lookback `W` sufficiency `f(x)[k:] == f(x[k - W + 1:])[W - 1:]`. |
| **3.6** | **Float Equivalence** | Exact `max(\|y_opt - y_base\|) == 0.0` on vectorized/parallel float reductions | **ULP / Relative Tolerance (`UL-08`)**: `max(\|y_opt - y_base\|) <= max(rtol·\|y_base\|, atol)` for numerical refactors; reserve exact `0.0` for cache-replay idempotency (`UL-07`). |
| **3.7** | **Callable Provenance** | `callable.__module__ == prod_module` *(breaks on `@wraps` decorators, re-exports, C-exts)* | **Wrapper-Safe Live Entrypoint Proof (`UL-08`)**: Import & invoke the live production entrypoint directly on live-resolved inputs; assert `N_processed == N_expected` & `source != "fallback"`. |

---

### Phase 3: Dual-OS Surgical Execution

When authoring or editing skill files, enforce strict cross-platform standards:

#### 1. Structure Blueprint & Progressive Disclosure (`≤ 500` Lines)
```text
skill-name/
├── SKILL.md              ← Required. Frontmatter + Core Steps & Invariants (≤ 500 lines)
├── references/           ← Optional. Deep taxonomies/matrices loaded on-demand via context pointers
└── scripts/              ← Optional. Universal, 100% domain-agnostic CLI helpers (stdlib-first)
```

#### 2. YAML Frontmatter Template (`≤ 400`-Char Target Budget)
```yaml
---
name: [lowercase-hyphenated-name-max-64-chars]
description: >
  [Leading-word summary in 1 sentence].
  Use when [primary triggers, exact slash commands, and distinct branches].
  Do NOT use for [explicit negative exclusions to prevent false triggers].
---
```

> [!NOTE]
> **Antigravity Schema Standardization**: Antigravity natively standardizes on `name` and `description`. Avoid non-standard fields like `argument-hint: "<task>"`, as non-standard keys can break slash autocomplete indexing in some IDE builds.

#### 3. Dual-OS, Shell Escaping & Portability Invariants
* **POSIX Forward Slashes**: Zero backslashes (`\`) inside markdown links `[label](#section)`.
* **No Hardcoded Machine User Paths**: Never hardcode `C:\Users\<User>\...` or `/Users/<username>/...`. Use relative paths (`../<skill>/SKILL.md`) or home-relative `~/` and `$env:USERPROFILE` / `%APPDATA%`.
* **PowerShell & Bash Backtick Safety in One-Liners**: Inside `python -c "..."` double-quoted commands, never write literal backticks `` ` `` (PowerShell treats `` ` `` as an escape character and Bash treats `` `...` `` as command substitution); always use hex escape `\x60` inside regexes.
* **UTF-8 & Bytecode Python Header Standard**: Every helper script in `scripts/*.py` must start with `sys.dont_write_bytecode = True`, `sys.stdout.reconfigure(encoding="utf-8")`, and pass `encoding="utf-8", errors="replace"` to all `subprocess.run(..., text=True)` calls.

---

### Phase 4: Ruthless 3-Tier Verification (The Green Gate)

A skill creation or evolution task is **NOT finished** until it passes all three verification tiers:

```mermaid
flowchart LR
    T1["Tier 1: Static YAML & Budget Linter"] --> T2["Tier 2: 5-Gate Universal Law & Live CLI Probe"] --> T3["Tier 3: Automated audit_engine.py --platform skill"]
```

#### Tier 1: Static Frontmatter & Progressive Disclosure Linter
* `name` matches `^[a-z0-9-]+$` (`≤ 64` chars) and matches folder name.
* `description` is present (`≤ 400` chars target, `≤ 500` chars advisory ceiling, `1024` hard max) and includes both positive triggers and `Do NOT use for...` (unless `disable-model-invocation: true`).
* `SKILL.md` is `≤ 500` lines (disclosing deep reference tables into `references/*.md` when needed) and contains zero raw LaTeX math macros (`\rightarrow`, `\times`, `\approx`).

#### Tier 2: 5-Gate Universal Law, Anti-Hardcode & Live CLI Counter-Anchor Scan
* **Universal Globalization Check**: Confirm the skill lives in `~/.gemini/config/skills/<name>/` (never in workspace `.agents/skills/`).
* **Zero-Hardcode & Secret Audit**: Scan all `.md`, `.py`, `.sh`, `.json` files using the exact case-sensitive boundary patterns enforced by [`audit_engine.py`](../xpublish-audit/scripts/audit_engine.py):
  * **Windows Path**: `(?i)\b([a-z]:[/\\]users[/\\](?!<)[a-zA-Z0-9_\-\.]+)`
  * **macOS Path** *(case-sensitive `/Users/` with trailing `/` so REST routes like `/users/profile` never false-positive)*: `(?:^|[\s"'`=:(])(/Users/(?!<|shared\b|runner\b)[a-zA-Z0-9_\-\.]+/)`
  * **Linux Path**: `(?:^|[\s"'`=:(])(/home/(?!<)[a-z0-9_\-\.]+)`
* **3-Bucket Numeric & 5-Gate Over-Specific Equation Sweep**: Verify zero Bucket 3 magic quotas, zero personal hardware/project strings, and zero unqualified Gate 3 anti-patterns (`x = 0 → y = 0`, `d log|Y|/d log α == p`, memoryless `f(x)[k:] == f(x[k:])`, intensive `sum(Child) == Parent`, or `callable.__module__ == prod_module`).
* **Live CLI Smoke & Bidirectional Counter-Anchor Probe (`scripts/*.py`)**:
  * Never rely on `py_compile` alone (`Anti-"Green-Linter" Gate`). For every modified or created script in `scripts/*.py`:
    1. Run `python -m flake8 --max-line-length=120 <script.py>` (`0` violations) and `python <script.py> --help` (`exit code 0`).
    2. Execute a live **Bidirectional Counter-Anchor Probe (`A_pos ∧ A_neg`)**: verify the script returns `0 Blocking` on valid edge-case inputs (`A_pos`, e.g., bold Markdown links `**[Label](https://...)**`, `$100 to $200` currency, paths with spaces) and accurately flags a synthetic defect (`A_neg`).

#### Tier 3: Automated Pre-Flight Engine Verification (`audit_engine.py --platform skill`)
Execute [`/xpublish-audit`](../xpublish-audit/SKILL.md) with `--platform skill` across all created or modified skills:

* **macOS / Linux**:
  ```bash
  python3 ~/.gemini/config/skills/xpublish-audit/scripts/audit_engine.py ~/.gemini/config/skills/<skill-name> --platform skill
  ```
* **Windows (PowerShell)**:
  ```powershell
  python "$env:USERPROFILE\.gemini\config\skills\xpublish-audit\scripts\audit_engine.py" "$env:USERPROFILE\.gemini\config\skills\<skill-name>" --platform skill
  ```
Must exit with **`VERDICT: PASS`** (`0` blocking issues, `0` unaddressed advisories) before committing to `~/.gemini/config`.

---

## 4. Composable BoostX Ecosystem Chaining (`/xcreate-skill` × `/x*`)

| Chained Command | Execution Upgrade |
| :--- | :--- |
| **`/xcreate-skill /xdeep-research`** | **Primary-Source Spec & Equation Lock**: Inspects local pinned manifests/SDKs or authoritative literature in Wave 1 before drafting Mode B tool skills or Mode C mathematical laws (`0` hallucinated CLI flags or unverified equations). |
| **`/xcreate-skill /xboost`** | **4-Phase Red→Green Skill & CLI Engineering**: Applies the 5-Gate Universal Law Falsification Protocol, authors stdlib-first CLI verifiers (`scripts/*.py`), and runs live `A_pos ∧ A_neg` counter-anchor probes in Phase 4. |
| **`/xcreate-skill /xultra`** | **3-Wave Adversarial Skill Audit Swarm (`Maker ≠ Checker`)**:<br>• **Wave 1**: Runs Law 1 deterministic `audit_engine.py --platform skill` + 3-Bucket & Gate 3 regex scans.<br>• **Wave 2A (`Blind Counter-Domain Critic Subagent`)**: Spawns an independent Read-Only Critic (`TypeName="research"`) instructed to attack candidate rules across **Archetypes A × B × C** and classify items into **`REMOVE (Ponytail YAGNI)`** vs. **`SURGICAL FIX`**.<br>• **Wave 2B**: Applies approved surgical edits, verifies cross-skill SSOT pointers, and re-runs `audit_engine.py --platform skill`. |
| **`/xcreate-skill /xsync`** | **Cross-Skill Relation-Set Sync**: Sweeps all sibling skills in `~/.gemini/config/skills/` sharing modified CLI flags, mode names, regexes, or `UL` law IDs so zero cross-skill contradictions remain. |
| **`/xcreate-skill /xobsidian`** *(Strict Opt-In)* | Without `/xobsidian`, never touch any Obsidian vault. When `/xobsidian` is included, ratchet converged `#tier/method` or `#tier/package` ecosystem notes into `VAULT_ROOT` after Tier 3 passes (`BROKEN=0`, `ORPHANS=0`, `DUP_NEIGHBOR_GROUPS=0`). |

---

## 5. Post-Creation / Evolution Summary Rubric

When reporting a newly created or upgraded skill to the user, provide:
1. **Pruned Project-Specific Items vs. Approved Universal Laws** *(for Mode C upgrades)*: What session-specific items were filtered out and why.
2. **3-Domain Translation Proof (`Archetypes A × B × C`)**: Concise proof that every added law holds across Continuous Solvers, Discrete Web/API Systems, and Non-Code Research/Docs.
3. **SSOT Location & Changed Files**: Clickable `file://` links to modified `SKILL.md`, `references/*.md`, and `scripts/*.py`.
4. **Verification Scorecard**: Confirmation that `audit_engine.py --platform skill`, `flake8`, live `A_pos ∧ A_neg` CLI probes, and `~/.gemini/config` Git commit passed `100% CLEAN`.
