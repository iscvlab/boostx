# Changelog

## v3.3.0

- **Unified `/xpublish` Consolidation (`14 → 13 Composable Skills`, `5,450` CLI LOC, `--platform pr` Diff-Scoped Auditor, `GITHUB_PUBLISHING_PROTOCOL.md` `v1.3` `§6.D` Review-Bot Convergence, and `/xboost` + `/xultra` + `/xdeep-research` Bounded `/browser` & Headless Test Routing)**:
  - **Skill Consolidation (`14 → 13 Composable /x* Skills`)**: Unified `/xpublish-audit` and `/xpublish-qgis` into **`/xpublish`** (backward-compatible aliases `/xpublish-audit`, `/xpublish-qgis`, `/publish`) with progressive disclosure (`SKILL.md` `113` lines + `references/github_readme_protocol.md` `v1.3` + `references/qgis_release_protocol.md` `163` lines) and bundled `scripts/{audit_engine.py,check_qt6.py,package_qgis.py}` (`1,997` combined LOC; `5,450` total LOC across all `8` Python CLI engines).
  - **`--platform pr` Diff-Scoped Upstream PR Auditor (`audit_pr_diff_invariants` in `audit_engine.py`, `1,049` LOC)**: Added `--platform pr` (`--base-ref`, `--issue-ref`) inspecting `git diff --name-status <base_ref>...HEAD` to block accidental repo-root modifications, unrequested binary/submodule additions, secret/path leaks in diff hunks, and closing-keyword mismatches (`Fixes #N` vs `Part of #N` / `Addresses #N`).
  - **`GITHUB_PUBLISHING_PROTOCOL.md` `v1.3` (`§6.D` Upstream PR Etiquette, Closing-Keyword Parity & Review-Bot Convergence)**: Codified single-concern branch hygiene, review-bot convergence loops (CodeRabbit, Copilot, Gemini Code Assist), and non-interactive test gates (`GIT_TERMINAL_PROMPT=0`, `MPLBACKEND=Agg`, `QT_QPA_PLATFORM=offscreen`).
  - **`/xsync` 3-Signal Bounded Up-Tree & Cross-Repo Mirror Federation (`--federated` in `audit_workspace_docs.py`, `454` LOC)**: Upgraded `/xsync` and `audit_workspace_docs.py` with `--federated` to auto-discover sibling git repositories, global `~/.gemini/config/skills/` mirrors, canonical protocol mirrors (`GITHUB_PUBLISHING_PROTOCOL.md`), org/personal profile READMEs, and sister repo READMEs under a safe parent stop-list.
  - **Bounded `/browser` Escalation & Headless Test Routing**: Wired `REST API / CLI → Raw HTTP Fetch → Bounded /browser (< 30s) → Graceful Skip` escalation and headless test environment guards into `/xboost`, `/xultra`, and `/xdeep-research`.
- **Context-Conditioned Single-Layer Universal First-Principles Laws (`UL-01..UL-08` in `skills/xboost/references/deep_audit_protocol.md`)**:
  - **`UL-01` (Bracketed Support, Scale Conditioning & Graph-Cut Isolation)**: Enforces exact bracketed domain support (`x_left ≤ x ≤ x_right`), explicit scale conditioning, and `0.0` future/cross-cut information leakage across partition boundaries.
  - **`UL-02` (Exact-Condition Refinement & Absorbing Failure Precedence)**: Enforces exact predicate refinement on candidate sets (`S_exact = {x ∈ S_cand : P(x)}`) and pessimistic absorbing failure tie-breaking (`Failure > Success`).
  - **`UL-03` (Step-Measure Scaling Convergence & Zero-Forcing Equilibrium Identity)**: Enforces theoretical step-measure convergence order (`O(Δμ^p)`) and exact zero-forcing equilibrium identity (`Δx = 0 ⇒ Δy = 0.0 / y == y_eq` with `0` `NaN`/`Inf`).
  - **`UL-04` (Extensive Partition, Remainder Conservation & Intended Peer-Branch Routing Completeness)**: Enforces extensive conservation (`∑ Child_k + Remainder ≈ Parent`) and peer-branch routing completeness (`K_peer ⊆ K_eval`, `0` blocking-`continue` drops).
  - **`UL-05` (Bidirectional Counter-Anchors, Strict Feasibility Dominance & Goal-Matched Objective/Constraint Polarity)**: Pairs simultaneous positive and negative counter-anchors (`A_pos ∧ A_neg`) with strict feasibility dominance (`J(x_infeas) ≺ J(x_feas)`), non-zero marginal sensitivity (`|∂J/∂M| > 0`) on unbounded objectives, goal-matched dispersion (`symmetric MSE/σ` for setpoint tracking vs `one-sided σ_fail` for directional goals), and role-matched `binary / continuous / budgeted` constraints.
  - **`UL-06` (Piece-Wise Codomain Reachability, Marginal Seam Scaling Order & Non-Degeneracy)**: Verifies live reachability of every declared codomain branch (`count(Branch_k) > 0`), interior marginal seam scaling (`|ΔY(α_2)/ΔY(α_1)| ≈ (α_2/α_1)^p_theory` without accidental `α²` double-application), and non-degeneracy.
  - **`UL-07` (Read-Only Feature-Stream Decoupling, Cache Idempotency & Post-Gate Non-Regression)**: Prevents in-place feature-stream mutation and cache compounding (`0` `T(T(x))` double-transforms) while locking post-gate non-regression.
  - **`UL-08` (Live-Entrypoint Parity, Active-Regime Sensitivity & Bounded Complexity)**: Requires testing the live production entrypoint directly (`∃ x ∈ Active_Regime(X) : ΔY ≠ 0`, `N_proc == N_exp`, `source != "fallback"`) under bounded asymptotic complexity.
- **`/xdeep-research` Wave 2.5 Rejected-Candidate Graveyard & Zero-Retrain Counterfactual Ablation Forensics**:
  - Mandates inspecting existing pruning logs, rejected candidate archives, and post-processing dampers via zero-retrain counterfactual ablation before proposing new external architectures or expensive retraining loops.
- **`/xultra` Two-Stage Evolutionary Ratchet (`Stage A → Stage B`)**:
  - **Stage A (Zero-Retrain Post-Processing Audit)**: Audits existing model/solver states (`0` retraining cost) for unintended post-processing throttles (`UL-04..UL-07`) to lock `Floor_StageA ≥ Floor_0`.
  - **Stage B (Warm-Start Evolutionary Generations `1..T`)**: Runs warm-start evolutionary generations seeded from the Stage A champion while strictly enforcing `Pass_Set(t+1) ⊇ Pass_Set(StageA)`.
- **`/xcreate-skill` Mode C (`Post-Session Skill Evolution, Universal Law Ratchet & Pre-Proposal Sieve`) & `5-Gate Universal Law Falsification Protocol`**:
  - Enforces **Agent-Process Law vs. Domain-Equation Inversion**, the **Global CLI Script Ban** (zero project-specific domain math inside global `skills/*/scripts/*.py`), a mandatory **Pruned Project-Specific Ideas** ledger, a **3-Domain Translation Proof Table** (`Archetypes A × B × C`), and a **7-Point Mathematical Boundary Table** before proposing or editing any global skill.
- **`/xpublish` (`audit_engine.py` `1,049` LOC across `8` CLI Engines / `5,450` Total LOC) & YAML Budget Compression (`370.54 ± 16.97` Chars)**:
  - Upgraded `audit_engine.py` with **`--platform pr` Diff-Scoped PR Invariant Auditor (`audit_pr_diff_invariants`)**, **Gate 3 Over-Specific Law Detector (`Check 4B`)**, **`≤ 500`-Line Sprawl Gate (`Check 4C`)**, **Raw LaTeX Macro Scanner (`Check 4D`)**, and the **Tri-OS Native Clipboard Protocol (`CF_UNICODETEXT` / `pbcopy` / `wl-copy`)**.
  - Tightened all `13` BoostX `/x*` skill YAML discovery descriptions to **`370.54 ± 16.97` chars** (`Median 374.0`, range `322–389` chars, `100.0%` within `≤ 400`-char target and `≤ 500`-char gate, `1,249` total discovery tokens).

### Install

See README. Tag: `v3.3.0`.
```bash
git clone --branch v3.3.0 https://github.com/iscvlab/boostx.git
```

## v3.2.0

- **Prefix `/x*` Namespace Migration & `/xocr` Hybrid PDF/Table Engine (`14 Composable Skills` & `8 Bundled CLI Engines`) — Instant `/x` Autocomplete Discovery**:
  - **Standardized `x...` Prefix Namespace**: Migrated every skill in the BoostX ecosystem to the `x-` prefix so typing `/x` in any IDE/CLI slash-command menu immediately surfaces all 14 BoostX skills in a single contiguous block without memorizing base names:
    - `/boostx` → **`/xboost`**
    - `/briefx` → **`/xbrief`**
    - `/contextx` → **`/xcontext`**
    - `/create-skillx` → **`/xcreate-skill`**
    - `/deep-researchx` + `/researchx` → **`/xdeep-research`**
    - `/kickoffx` → **`/xkickoff`**
    - `/layax` → **`/xlaya`**
    - `/obsidianx` → **`/xobsidian`**
    - `/unlimited-ocr` + `/ocrx` + `/ocr` → **`/xocr`** *(NEW in public suite)*
    - `/planx` → **`/xplan`**
    - `/publishx-audit` → **`/xpublish-audit`**
    - `/publishx-qgis` → **`/xpublish-qgis`**
    - `/syncx` → **`/xsync`**
    - `/ultrax` → **`/xultra`**
  - **`/xocr` High-Speed Hybrid PDF & Table Engine (`skills/xocr/scripts/ocr_runner.py`)**: Combines single-pass C++ `PyMuPDF` (`fitz`) coordinate-sorted text (`sort=True`), a Two-Stage Grid + LaTeX `booktabs` table extractor (`page.find_tables()` with horizontal-rule grouping, extracting `6/6` tables from `Unlimited-OCR.pdf` in `2.48 s`), Thai PUA (`U+F700..U+F71A`) & toned decomposed Sara-Am (`\u0e4d([\u0e48-\u0e4b]?)\u0e32` → `\1\u0e33`) glyph normalization, a per-page garble & image-coverage router, and a 4-tier OCR backend ladder (`SGLang :10000` → HuggingFace `baidu/Unlimited-OCR` CUDA VLM with `no_repeat_ngram_size=35` → process-cached `EasyOCR` → `pytesseract`), with automatic PDF/image routing wired into `/xdeep-research`, `/xbrief`, `/xboost`, `/xobsidian`, and `/xultra`.
  - **Backward-Compatible Trigger Aliases**: All 14 `SKILL.md` YAML frontmatter descriptions preserve legacy `-x` (`/*x`) and unprefixed triggers while maintaining **`100%` compliance** within the `≤ 400`-char `audit_engine.py --platform skill` context budget guard.
- **Elastic Cognitive Swarm (`N × K × C × T` Topology, 4-Law First-Principles Sizing & `UL-01..UL-08` Universal Laws)**:
  - **4-Law Swarm Sizing Calculus (`N × K × C × T`)**: Upgraded `/xultra` and integrated first-principles swarm sizing across all 14 skills—replacing arbitrary headcount quotas (`3+2`, `4–12 agents`, `≤ 3 items/agent`, `2–4 scouts`) with:
    1. **Law 1 (Code-Over-Swarm Split)**: Offloads deterministic sweeps (`laya_triage.py`, `audit_engine.py`, `verify_evidence.py`, regex/SQLite/AST probes) to zero-token CLI scripts before spawning System 2 subagents.
    2. **Law 2 (True Orthogonality Sizing — `K` Vectors)**: Spawns `K ≥ 2` competing builders on coupled problems (`N = 1`) strictly for genuinely orthogonal algorithms, module seams, or visual paradigms.
    3. **Law 3 (Cognitive-Density Partitioning — `N` Shards)**: Sizes parallel fleets by per-shard working-set weight (1 dedicated subagent per heavy module, case study, or interactive HTML deck; domain-clustered subagents for lightweight items) bound by a **Pre-Locked Shared Seam Header** (and a **Pre-Assigned Bridge Matrix** for `/xobsidian /xultra`).
    4. **Law 4 (Two-Stage Elastic Verification — `Wave 2A` Parallel Critic Shards `C ≥ 1` → `Wave 2B` Serialized Main Checker Gate + `T`-Generation Cumulative Monotonic Ratchet)**: Scales read-only critic shards (`C = 1..3`) elastically by coupled invariant clusters, serializes global integration & build locks through a single Wave 2B Main Checker Gate, and enforces `Pass_Set(t+1) ⊇ Pass_Set(t)` across iterative turns (`<artifactDir>/scratch/boostx_state.md`).
  - **Single-Layer Universal First-Principles Laws (`UL-01..UL-08` in `skills/xboost/references/deep_audit_protocol.md`)**: Codified 8 domain-neutral mathematical & runtime laws (`UL-01` Dimensional & Scale Invariance, `UL-02` Dual-Stream Operator Separation, `UL-03` Partition Seam & Boundary Continuity, `UL-04` Set-Partition Conservation & Non-Blocking Cascade, `UL-05` Bidirectional Counter-Anchor & Monotonicity, `UL-06` Numerical Stability & Degeneracy Guard, `UL-07` Topological & Graph Invariants, `UL-08` Live-Callable Parity & Zero-Input Identity) separated cleanly from Builder Self-Audit Gates (`G1..G5`) and Scout Structural Defect Classes (`Axis 1..4`).
  - **Pointer-Not-Payload Return Contract & 3-Bucket Numeric Litmus Test**: Replaced arbitrary word-count caps (`≤ 150 words`) with **Compact Pointer Receipts** (for write-capable subagents) and **Schema-Complete Telegraphic Evidence Tables** (for read-only scouts), and embedded the **3-Bucket Numeric Litmus Test** into `/xcreate-skill`, `/xdeep-research`, `/xultra`, and `audit_engine.py`.
- **Unified `/xdeep-research`, `/xsync` Level 1 Receipts & `/xobsidian` Converged-Only Ratchet**:
  - Merged `researchx`'s **3-Tier Adaptive Scope Routing** (`Tier 1: Fast Inline Probe ≤ 2 sources`, `Tier 2: Single Isolated Scout`, `Tier 3: 5-Wave Adversarial Swarm`), **4-Tier Primary-Source Authority Ladder** (local pinned manifests, SQLite/AST/CLI probes first), **Single-SSOT In-Place Upsert & Iterative Delta Routing** (banning duplicate `RESEARCH_*.md` file forking on `Turn t > 1`), and **Capability-Aware Subagent Write-Permission Contract** directly into **`/xdeep-research`** (and `/xboost` Track B).
  - Upgraded **`/xsync`** Level 1 to require verified non-fallback runtime receipts (`source != "fallback"`, `N_proc == N_exp`, `UL-04` Partition Conservation) and forked sibling doc consolidation, and upgraded **`/xobsidian`** with the **Converged-Only Ratchet & Session Dirty-Note Ledger (`DIRTY_IN_SESSION`)**.
- **Automated Legacy Directory Cleanup & Empirical Re-Benchmarking**:
  - Updated `scripts/install.ps1` and `scripts/install.sh` to automatically purge deprecated `*x` and pre-`v3.0` folders from `~/.gemini/config/skills`, `~/.claude/skills`, and `~/.grok/skills` during upgrades.
  - Re-ran the full multi-trial benchmark harness (`benchmarks/run_boostx_benchmark.py` and `benchmarks/generate_figures.py`) across `109` installed skills, `752` markdown files, `25` red-team defects (`100%` catch rate in `6.45 ms`), and `214` real IDE sessions (`987` prompt turns).

### Install

See README. Tag: `v3.2.0`.
```bash
git clone --branch v3.2.0 https://github.com/iscvlab/boostx.git
```

## v3.1.0

- **`/ultrax` (`13 → 14 Composable Skills`) — Dynamic Topology-Matched Multi-Agent Swarm & Blind Verification Multiplier**:
  - **Order-Independent Canonical Stage DAG**: Normalizes any slash-command combination regardless of typing order into `Stage 0: RETRIEVE (/briefx, /obsidianx, /layax) → Stage 1: RESEARCH (/researchx, /deep-researchx) → Stage 2: PLAN (/planx) → Stage 3: BUILD (/boostx) → Stage 4: AUDIT & SYNC (/syncx, /publishx-audit) → Stage 5: RATCHET (/obsidianx) → Stage 6: VERIFY (/goal)`.
  - **Dynamic `N × K` Topology Sizer (Zero Fixed-Count Bloat)**:
    - **Complexity Floor (`2-Agent Fast Pair`)**: Automatically bypasses swarm fan-out on localized 1-file tasks (`1 Maker + 1 Blind Verifier`).
    - **Archetype 1 (`3 + 2` Best-of-3 Tournament)**: Spawns 3 orthogonal Makers (`Vector A: Stdlib/Minimal`, `Vector B: Performance/Algorithmic`, `Vector C: Deep Module/UX`) + 2 Blind Verifiers (`Adversarial Spec Critic` + `Red-Team Edge-Case Breaker`). Supports Objective Auto-Promote vs. Aesthetic Visual QA Side-by-Side (`_vA`/`_vB`/`_vC`) modes.
    - **Archetype 2 (`N + 2` Partitioned Batch Swarm)**: Enforces a strict `≤ 3` items/files per subagent cap (`N = ceil(M / 3)`, max `6` concurrent per wave) and locks a **Pre-Locked Shared Seam Header** in the main thread before fan-out to prevent cross-partition interface drift.
    - **Archetype 3 (`Multi-Wave DAG`)**: Chains Scout Wave → Builder Wave → Blind Audit Wave for full-stack cross-layer features.
  - **Universal 5-Domain Adaptation, Multi-Host Dispatch & Build-Lock Serialization**:
    - Adapts seamlessly across Software/Web/Cloud, Data/ML/SQL, CAD/GIS/Physics, Presentation/UI/Docs, and General Research/Strategy across Antigravity (`invoke_subagent`), Claude Code (`Task`), and Sequential Personas.
    - Enforces **Wave 1 Isolation** (write-only to partitioned paths or `Workspace="share"`/`"branch"`, zero concurrent `dotnet build`/`pytest`/`cargo` lock contention) followed by **Wave 2 Serialized Build & Red-Team Verification** and **`≤ 150-Word` Caveman Receipt** returns.
- **`/contextx` Cross-Platform Token Telemetry Upgrade (`scripts/check_context.py`)**:
  - Added pure-stdlib Protobuf wire decoding for SQLite `conversations/<id>.db` step metadata alongside `transcript.jsonl` parsing, surfacing active-session token counts (`input_tokens`, `cache_read_tokens`, `output_tokens`, `thinking_tokens`, `cache_hit_pct`) and cross-platform aggregation flags (`--tokens`, `--days <N>`, `--all-time`) across Antigravity 2.0, Antigravity IDE, and Antigravity CLI.
- **Zero-Persona Neutrality & Bidirectional Ecosystem Wiring**:
  - Added opt-in `/ultrax` composable hooks across `/boostx`, `/planx`, `/briefx`, `/researchx`, `/deep-researchx`, `/syncx`, `/obsidianx`, and `/kickoffx`.
  - Sanitized personal hardware/persona references across `/boostx`, `/create-skillx`, and `/kickoffx`, and added automated persona-neutrality checks to `/create-skillx` and `publishx-audit/scripts/audit_engine.py`.

### Install

See README. Tag: `v3.1.0`.
```bash
git clone --branch v3.1.0 https://github.com/iscvlab/boostx.git
```

## v3.0.0

- **Unified BoostX (`-x`) Composable Ecosystem & 13-Skill Suite Expansion**:
  - **Standardized `-x` Command Namespace**: Unified all core workflow skills under the `-x` suffix while preserving backward-compatible legacy triggers in YAML descriptions:
    - `/brief` → **`/briefx`**
    - `/obsidian-vault` → **`/obsidianx`**
    - `/update-doc` → **`/syncx`**
    - `/plan` → **`/planx`**
    - `/context` → **`/contextx`**
    - `/kickoff` → **`/kickoffx`**
    - `/laya` → **`/layax`**
    - `/create-skill` → **`/create-skillx`**
    - `/publish-audit` → **`/publishx-audit`**
    - `/publish-qgis` → **`/publishx-qgis`**
    - Retained **`/boostx`**, **`/researchx`**, and **`/deep-researchx`**.
  - **5 Newly Added Skills in Public Distribution (`8 → 13 Skills`)**:
    - **`/obsidianx` (NEW)**: Portable 2-Hop Obsidian Second Brain & Cross-Domain Knowledge Graph Architect. Features zero-hardcode dynamic vault resolution via OS `obsidian.json` (`open: true`) or ancestor `.obsidian/` discovery, strict opt-in execution (zero vault I/O when `/obsidianx` is omitted from the prompt), 2-Hop navigation (`00 Index.md` → `Hub - <Domain>.md` → Atomic Note), Cross-Domain Concept Bridges, and a 4-check Post-Ratchet Graph Verifier.
    - **`/planx` (NEW — BoostX v2.0 Architecture Planner)**: Locks a 2D Plan Contract (`Scope × Risk`), runs blast-radius & invariant discovery, evaluates Ponytail × Deep Module Vectors A/B/C, embeds an Inline Grilling Decision Matrix (`DEC-01..N`) and Red → Green Verification Table inside `implementation_plan.md` with zero chat Q&A spam, and halts for user approval.
    - **`/layax` (NEW — System 1 Semantic Decision & Triage Sidecar)**: Non-autoregressive System 1 decision layer (`choice`, `score`, `noul`) powered by `convaiinnovations/laya` (~7–33 ms local forward pass) and bundled `scripts/laya_triage.py` (fence-safe `≤ 1,200`-char heading chunker with exact `#L<start>-L<end>` line ranges and `laya.is_english()` bilingual routing). Accelerates `/syncx /layax` contradiction hunting, `/briefx /layax` large-corpus section shortlisting, `/deep-researchx /layax` candidate triage, and `/publishx-audit /layax` public claim verification, with 100% graceful fallback to native tools when `laya` is not installed.
    - **`/contextx` (NEW)**: IDE conversation transcript compaction & active window pressure analyzer (`scripts/check_context.py`). Features automatic subagent transcript filtering (`is_user_conversation`), strict `CHECKPOINT` boundary detection, exact checkpoint step indices, active window fill `%`, and a 4-tier 2D memory drift rubric (`HEALTHY`, `NOMINAL`, `CAUTION`, `CRITICAL`).
    - **`/kickoffx` (NEW)**: End-of-session handover protocol enforcing pre-handover `/syncx` verification, task-smart command routing, strategic next-step options, and a self-contained copy-pasteable kickoff prompt for fresh conversations.
  - **6th & 7th Bundled CLI Engines (`syncx/scripts/audit_workspace_docs.py` & `layax/scripts/laya_triage.py`)**:
    - Added repo-agnostic workspace documentation auditor verifying relative links, Zero-LaTeX compliance, SHA-256 mirror parity, and `--deprecated` sweeps.
    - Added `layax/scripts/laya_triage.py` with fence-safe heading chunking (`≤ 1,200` chars / `~300` tokens), automatic English vs multilingual model selection (`laya.is_english`), 4 triage modes (`rubric`, `contradiction`, `shortlist`, `classify`), and deterministic pure-Python fallback.
  - **Composable Pipeline Wiring & Visual Architecture Diagrams**:
    - Wired left-to-right composable handoffs (`Context → Research → Plan/Execute → Sync + Modifiers/Sidecars`) across `/briefx`, `/researchx`, `/deep-researchx`, `/planx`, `/boostx`, `/syncx`, `/obsidianx`, and `/layax`.
    - Added vector architecture diagrams (`docs/assets/boostx-master-ecosystem.svg` and `docs/assets/boostx-composable-routing.svg`).

### Install

See README. Tag: `v3.0.0`.
```bash
git clone --branch v3.0.0 https://github.com/iscvlab/boostx.git
```

## v2.0.0

- **Core 8 Portable Skill Suite Expansion**:
  - **`/deep-researchx` (NEW)**: Universal, domain-agnostic 5-Wave Multi-Agent Deep Research & 100%-Proof Synthesis Engine:
    - **Wave 1 (`Intent × Domain` 2D Contract)**: Dynamically synthesizes evaluation axes, quotas, and disambiguation rules across Built Environment/Case Studies, Physical Sciences/Simulations, Software/Systems, Natural Sciences, and Policy/Strategy.
    - **Wave 2 (Parallel Harvester Swarm)**: Concurrent subagent fan-out with mandatory primary deep-link scraping (banning bare homepage URLs and snippet-only claims).
    - **Wave 3 & 3.5 (Blind Adversarial Auditor + `scripts/verify_evidence.py` + Prune & Replace Loop)**: Independent red-team falsification of completion vs policy years, attributions, units, and metrics, paired with a deterministic Python CLI verifier (`verify_evidence.py`) and zero-forgery replacement harvesting.
    - **Wave 4 & 5 (100%-Proof Synthesis & Composable Handoff)**: Strict `[VERIFIED FACT]` vs `[RECOMMENDED SYNTHESIS]` binding, dual Markdown + JSON/SQLite persistence, and direct spec-to-code handoff into `/boostx` and `/goal`.
  - **`/researchx` (NEW)**: Fast tactical primary-source research protocol:
    - **3-Tier Execution Routing**: Inline probe (`≤ 2` sources) vs single isolated scout vs parallel multi-angle swarm.
    - **4-Tier Primary-Source Authority Ladder**: Local pinned manifests (`package.json`, `pyproject.toml`, `*.csproj`, `metadata.txt`) and local SQLite/XML/AST probes first, version-matched official specs second, upstream source/tests third, standards/papers fourth.
    - **Capability-Aware Subagent Routing**: Prevents read-only subagent write deadlocks and enforces `≤ 150`-word compressed main-thread return digests.
  - **`/boostx` (v2.0 Upgrade)**:
    - **2D `Task × Project` Goal Contract Synthesis**: Crosses 6 Task Archetypes (`DEBUG/RCA`, `BUILD/FEATURE`, `SIMULATE/SOLVER`, `REFACTOR/SIMPLIFY`, `OPTIMIZE/SCALE`, `AUDIT/PLAN/SHIP`) with 5 Project Verification Harnesses (`CAD/Rhino/GH`, `GIS/QGIS`, `Web UI/Figma`, `Data/GCP/ML`, `Agent Skills/CLI`).
    - **Simulation Physics Triad**: Enforces explicit CAD-to-SI unit bridges, CFL/timestep caps, zero-load identity checks (zero `NaN`/`Inf`), and 1D analytical toy benchmarks.
    - **Composable Escalation**: Native hooks for `/goal` marathon state checkpointing, `/researchx` tactical lookups, and `/deep-researchx` 5-wave formulation.
  - **`/create-skill` & `/publish-audit` (`--platform skill` Globalization & Context Budget Guard)**:
    - Added `--platform skill` profile to `audit_engine.py` verifying frontmatter schema, `≤ 350`-char description budget (preventing system-prompt truncation of sibling skills), Universal Globalization placement, POSIX link integrity, and `sys.dont_write_bytecode` hygiene.
  - **`/brief` & `/update-doc` Upgrades**:
    - `/brief`: Added 4-tier authority hierarchy, Two-Pass reading (`Pass A` structural skeleton/cardinality before `Pass B` section deep dive), and deferred/frozen zone gates.
    - `/update-doc`: Added 4-level Conflict Arbitration Hierarchy (Code/Data Receipts > Canonical SSOT > Chat Lock > Drafts), ghost reference sweeps, quantitative cardinality sweeps, and Sync Ledger output.

### Install

See README. Tag: `v2.0.0`.
```bash
git clone --branch v2.0.0 https://github.com/iscvlab/boostx.git
```

## v1.3.0

- `/publish-audit`:
  - **5-Pillar High-Security & Privacy Architecture**: expanded secret detection across 16 high-entropy token patterns (AWS, GitHub classic & fine-grained, OpenAI, Anthropic, Google AI, Slack, HuggingFace, PyPI, GitLab, NPM, Stripe, SendGrid, Discord webhooks, SSH/RSA private keys, and database connection strings).
  - **Deep Python AST Vulnerability Scanner**: static AST analysis blocking dynamic execution (`eval()`, `exec()`, `compile()`, `__import__()`), shell injection (`os.system()`, `os.popen()`, `subprocess.*(shell=True)`), insecure deserialization (`pickle`, `_pickle`, `marshal`, `shelve`), race-condition temp files (`tempfile.mktemp()`), and memory injection primitives (`VirtualAlloc`, `WriteProcessMemory`, `CreateRemoteThread`).
  - **Undeclared Network Activity Auditing**: inspects and flags outbound socket connections and HTTP clients (`urllib`, `requests`, `httpx`, `aiohttp`, `socket`).
  - **Flake8 Quality Gate**: integrated code quality audit strictly enforcing the project's local `.flake8` configuration.
  - **QGIS Architecture Invariants**: validates mandatory `classFactory(iface)` hook in `__init__.py`, INI interpolation syntax (zero raw unescaped `%`), HTTPS-only public metadata links, and integrated Qt6 forward-compatibility checks.
- `/publish-qgis`:
  - **Qt6 / QGIS 4 Forward-Compatibility Scoped Enum Expansion**: added scoping for `QPageSize.Unit.Point`, `QPageLayout.Orientation.Portrait`, `QPageSize.PageSizeId`, and `QPageLayout.Mode`, guaranteeing the green **"QGIS 4 Ready"** badge on `plugins.qgis.org`.
  - **Pure Runtime Release Packaging**: automatically excludes developer setup scripts (`install_plugin.py`, `generate_icons.py`), test suites (`test_*.py`), scratch files, and linter configs (`.flake8`, `.bandit`, `.secrets.baseline`) from release archives.
  - **Deterministic Byte-Reproducible ZIP Creation**: fixed epoch timestamp `(2026, 1, 1, 0, 0, 0)` and normalized POSIX permissions (`0o644`) to eliminate developer timestamp and metadata leaks.

### Install

See README. Tag: `v1.3.0`.
```bash
git clone --branch v1.3.0 https://github.com/iscvlab/boostx.git
```

## v1.2.0

- `/update-doc`: major upgrade to the cross-document synchronization protocol:
  - **Interactive HTML & Web Artifact Parity**: explicitly governs slide decks, architecture viewers, and dashboard portals. Mandates DOM container parity (`<section class="slide">`), sequential heading counters (`SLIDE 01 / N`), embedded JavaScript state (`totalSlides = N`), and repository CSS design token compliance.
  - **Distribution Mirrors & Shadow References Invariant**: detects duplicated documents across distribution or export bundles (`dist/docs/`, `package/docs_reference/`) and enforces deterministic byte-for-byte synchronization.
  - **Historical Boundary Protocol**: separates active SSOT invariants (must hit zero stale references) from immutable historical changelogs / ADRs (preserving past event context).
  - **Cross-Platform Scripting Hygiene**: mandates Python standard library scratch execution with UTF-8 stdout reconfiguration for multi-line DOM / regex replacements, eliminating shell-specific CLI quote mangling.
- `/update-doc`: added dedicated MIT LICENSE file and clean scripts guidance for standalone packaging.

### Install

See README. Tag: `v1.2.0`.
```bash
git clone --branch v1.2.0 https://github.com/iscvlab/boostx.git
```

## v1.1.0

- `/brief`: load related workspace markdown (cap 8), then do `/brief <task>` in the same turn. HTML only when the task is a specific page. Portable: no baked-in filename list.
- `/create-skill`: machine-path ban uses `C:\Users\<user>` so `/publish-audit --platform github` does not treat ellipsis placeholders as a real home path.

### Install

See README. Tag: `v1.1.0`.
```bash
git clone --branch v1.1.0 https://github.com/iscvlab/boostx.git
```

## v1.0.0

First tagged public line of this skill suite.

**Who it is for:** anyone who wants the same `/boostx`, `/create-skill`, `/update-doc`, `/publish-audit`, and `/publish-qgis` behavior on Claude Code, Grok, Gemini/Antigravity, Cursor, or Codex, in an IDE or a CLI, on Windows, macOS, or Linux.

**Who it is not for:** a drop-in thesis-workspace auditor. That HTML checker is not in this package. Add `scripts/audit_docs.py` in **your** repo if you need extra checks.

### Skills in this release

| Command | Role in v1.0.0 |
|:---|:---|
| `/boostx` | Red / Ponytail / dual-OS / green. Task classes: code, docs, audit. Host tools are optional. |
| `/create-skill` | Discover skill roots, approve description, write a full SKILL.md. |
| `/update-doc` | Chat delta + workspace markdown/HTML scan + relation sync + zero-stale grep. |
| `/publish-audit` | Pre-flight engine for generic, qgis, food4rhino, github. |
| `/publish-qgis` | QGIS zip / SemVer / Qt6 packager (unchanged role; still the zip SSOT). |

### Changed (vs untagged `main` before this tag)

- `/update-doc` no longer assumes one author's filenames or a bundled thesis HTML auditor.
- `/create-skill` is not Gemini-only and does not stop at a stub README.
- `/boostx` does not require Antigravity `invoke_subagent` / `DeepCoder` / `manage_task`.
- `/publish-audit` scans `.env` and shell/toml; GitHub LICENSE and Food4Rhino `.gha` are blocking; README overclaim is advisory; no PyPI/NPM platform claim.

### Install

See README. Tag: `v1.0.0`.
```bash
git clone --branch v1.0.0 https://github.com/iscvlab/boostx.git
```
