# Universal 4-Axis Deep Forensic Audit Protocol (`XBoost Reference`)

Read this reference on-demand when executing **`AUDIT / FORENSIC / SHIP`** tasks, hardening **`SIMULATE / SOLVER`** or **`OPTIMIZE / SCALE`** engines, or running **Phase 4 / Wave 2–2.5 Blind Adversarial Verification** under [`/xboost`](../SKILL.md) and [`/xultra`](../../xultra/SKILL.md).

This protocol is **100% language-, topic-, and workspace-agnostic**. It operates from universal mathematical, physical, and systems-engineering first principles rather than brittle language-specific regexes.

---

## 1. The 3-Wave Deep Forensic Audit Lifecycle (`Wave 1 → Wave 2 → Wave 2.5`)

Whenever auditing a codebase, simulation solver, data/ML pipeline, UI dashboard, or strategy matrix (standalone via `/xboost` or scaled across parallel subagents via `/xboost /xultra`), advance through three progressive waves:

```mermaid
flowchart LR
    W1["Wave 1: 4-Axis Orthogonal Forensic Shards\n(Truth • Criteria • Wiring • Hot-Path)"] --> W2A["Wave 2A: Elastic Critic Shards (C >= 1)\n(Isolated Ephemeral UL Probes)"]
    W2A --> W2B["Wave 2B: Main Checker Gate\n(Serialized Build/Tests & Cross-Axis Arbitration)"]
    W2B -->|"Verified Defects Found"| W25["Wave 2.5: Surgical Coordinate-Wise Remediation\n(1-Seam Fix + Cumulative Ratchet Lock)"]
    W25 --> W2A
    W2B -->|"0 Verified Defects"| Done["Phase 4 Green Gate / Stage 4 Sync"]
```

1. **Wave 1 — 4-Axis Orthogonal Forensic Shards (`Cognitive-Density Inspection`)**:
   - Inspect the target system across four orthogonal forensic dimensions (in `/xboost /xultra`, spawn 1 dedicated Read-Only Forensic Scout per axis or subsystem shard):
     - **Axis 1 (`TRUTH & ZERO-CHEAT`)**: Causality, bracketed interpolation, exact-predicate refinement, and holdout isolation (`UL-01`, `UL-02`).
     - **Axis 2 (`CRITERIA, OBJECTIVES & SCALE PARITY`)**: Step-measure invariance, bidirectional counter-anchors, piece-wise codomain reachability, and scale preservation (`UL-03`, `UL-05`, `UL-06`).
     - **Axis 3 (`WIRING PROVENANCE, PARTITION CONSERVATION & ROLLBACK`)**: Hierarchical partition & remainder conservation, read-only feature decoupling, exception transparency, DAG init order, and atomic state rollback (`UL-04`, `UL-07`, `UL-08`).
     - **Axis 4 (`HOT-PATH PERFORMANCE & COMPLEXITY`)**: Loop-invariant hoisting, monotonic commutation, vectorization/indexing, and bounded cache eviction (`UL-08`).
2. **Wave 2 — Elastic Blind Falsification Shards (`Wave 2A`) & Main Checker Gate (`Wave 2B`, `Maker ≠ Checker`)**:
   - Never accept speculative prose findings or static linter passes at face value, and never hardcode a fixed number of Critic subagents ([`/xultra`](../../xultra/SKILL.md) Law 3):
     - **Wave 2A (`Elastic Critic Shards`, `C ≥ 1`)**: For localized 1-seam edits, auto-downshift to `C = 1` Blind Critic. For heavy multi-module or full-system audits, spawn dedicated parallel Critic Shards per active `UL` cluster or subsystem. Each shard executes **isolated, non-mutating Ephemeral Runtime Probes** (`python -c`, `node -e`, `sqlite3`, or single-function callables with `0` global build-lock contention) to classify findings strictly as **`[VERIFIED DEFECT]`** (with exact `file:line` and observed delta) or **`[FALSE POSITIVE — PRUNED]`**.
     - **Wave 2B (`Main Checker / Lead Verifier Gate`)**: Ingests the Wave 2A shard receipts, executes any lock-sensitive global build or full regression suite **once** (serialized barrier), arbitrates cross-shard conflicts (`Truth/Conservation UL-01..UL-07` strictly overrides `Performance UL-08`), verifies cross-stage contract fidelity (`Spec/Research Formula == Plan Matrix == Live Code`), and sequences defects into a deduplicated Wave 2.5 queue.
3. **Wave 2.5 — Surgical Coordinate-Wise Remediation & Cumulative Monotonic Ratchet (`Pass_Set(t+1) ⊇ Pass_Set(t)`)**:
   - When fixing verified defects, apply **Coordinate-Wise Marginal Attribution**: patch and benchmark one logical seam at a time so beneficial fixes are never bundled with or cancelled out by regressions.
   - **Ephemeral-to-Permanent Ratchet Promotion**: Distinguish disposable scratch exploration scripts from **Verified Invariant & Counterexample Assertions (`UL-05`, `UL-08`)**, which MUST be promoted into the permanent regression suite (or `<artifactDir>/scratch/ratchet_invariants.py` + logged in `<artifactDir>/scratch/boostx_state.md`) so round `t+1` can never regress round `1..t` fixes.

---

## 2. The 5 Universal First-Principles Guardrails (`Builder Gates`)

| Guardrail | First-Principles Rule | Mandatory Runtime Proof / Probe |
| :--- | :--- | :--- |
| **G1. Anti-"Green-Linter" Illusion Gate** | Compiler, typechecker, or static AST/linter `0 warnings` proves **syntax only—never semantic, physical, or mathematical truth**. | Pair every static check with an executed **Live-Callable Runtime Provenance & Behavioral Probe (`UL-08`)** before signing off. |
| **G2. End-to-End Perturbation & Coverage Law (`ΔX → ΔY ≠ 0`)** | Every upstream parameter, input control, config key, or feature `X` must actively drive terminal output `Y` across `100%` of expected records without silent truncation, unreachable clamping, or fallback masking. | **1. Perturbation & Reachability (`UL-06`, `UL-08`)**: Perturb `X → X'`, verify `ΔY ≠ 0`, and confirm every piece-wise branch/tier is reachable (`> 0` hits).<br>**2. Coverage & Provenance**: Verify `N_processed == N_expected` and `source != "fallback"`. |
| **G3. Universal Conservation, Causality & Invariance Triad** | Generalizes conservation and boundary laws across all systems:<br>• **Partition & Remainder Conservation (`∑ Child_k + Remainder == Parent`, `UL-04`)**<br>• **Prefix Causality, Bracketed Support & Exact Refinement (`UL-01`, `UL-02`)**<br>• **Step-Measure Invariance (`Δμ`, `UL-03`) & Stream Decoupling (`UL-07`)** | **1. Conservation**: `abs((sum(Child_k) + Remainder) - Parent) <= 1e-9`.<br>**2. Prefix / Support Probe**: Mutating `t+1..T` yields `0.0` diff at `0..t`; out-of-interval `x ∉ [x_left, x_right]` is rejected/clamped.<br>**3. Step-Scaling & Idempotency**: Halving step measure `Δμ → Δμ/2` preserves integrals; repeated run yields `0.0` cache drift. |
| **G4. Bidirectional Counter-Anchors, Smoothness & Scale Parity Gate** | Scoring curves, filters, and ratchets must resist Goodhart's Law, lock **both positive and negative counter-anchors (`A_pos ∧ A_neg`, `UL-05`)**, preserve upstream weight scales across module seams (`UL-06`), and provide smooth search gradients. | Verify simultaneous `100%` pass on `A_pos ∧ A_neg` plus domain extremes `(x_min, x_max)`, concave/log-compounded aggregation (`log1p` over linear `cumsum`), smooth ramps over binary step cliffs, and feasible initial seeds. |
| **G5. Hot-Path Complexity & Resource Discipline** | Inner loops must run in `O(1)` or vectorized/indexed memory with zero redundant invariant recomputation, zero cache-clear thrashing, and zero eager pre-gate formatting (`UL-08`). | Measure `Before → After` wall-clock latency (`ms`) and verify `0.0` numerical drift between baseline and optimized outputs. |

---

## 3. Complete 4-Axis Forensic Audit Taxonomy (`Wave 1 Scout Catalog`)

### Axis 1 — `TRUTH & ZERO-CHEAT` (Anti-Illusion, Anti-Leakage & Boundary Integrity)
1. **Unbounded Extrapolation vs. Bracketed Interpolation & Graph-Cut Shortcuts (`UL-01`)**:
   - *Flaw*: Extrapolating values unboundedly from a single boundary into unconstrained space instead of requiring opposing verified anchors (`x_left ≤ x ≤ x_right`); or approximating graph shortest-path distance `d_G(u, v)` with unconstrained norm `||u - v||` across absent/disconnected graph edges `(u, v) ∉ E`.
   - *Fix*: Restrict interpolation strictly to bracketed interior intervals, decay or flag `OUT_OF_BOUNDS` outside anchor support, and route strictly along valid subgraph edges `E`.
2. **Coarse Candidate Pre-Filter (`S_cand`) vs. Exact Condition (`P(x)`) Contamination (`UL-02`)**:
   - *Flaw*: Computing feature averages, aggregates, or membership decisions directly over a coarse index, window, or bounding box lookup (`S_cand ⊇ S_exact`), allowing background/boundary items (`S_cand ∖ S_exact`) to dilute statistics.
   - *Fix*: Treat coarse lookups strictly as Stage 1 candidate generators and evaluate all statistics and predicates exclusively on the exact subset `S_exact = {x ∈ S_cand : P(x)}`.
3. **Post-Event Clamping, Absorbing-Failure Bypass & Optimistic Tie-Breaking (`UL-02`)**:
   - *Flaw*: Using end-of-step `min/max` clamping (`max(end_state, -limit)`) when a trajectory breaches a fatal limit mid-step (`τ ∈ [t, t + Δt]`), or checking `if success` before `if failure` on coarse discrete steps without deducting state-transition overhead.
   - *Fix*: Enforce immediate absorbing-state termination upon intra-step failure breach and **Pessimistic Priority (`Failure > Success`)** on ambiguous discrete steps.
4. **Temporal Prefix Leakage, Warm-Seed Contamination & Holdout Reuse (`UL-01`, `UL-07`)**:
   - *Flaw*: Joining coarse-to-fine sequences by period *open* timestamp instead of *completion* timestamp (`t_end_A <= t_end_B`); loading warm fallback checkpoints during cold-start benchmarks; or querying the blind Holdout split across iterative tuning generations.
   - *Fix*: Enforce closed-interval point-in-time joins, window-length-independent warmups (`f(x)[k:] == f(x[k:])`), cold-start cache isolation, and a masked **3-Way Split (`Train / Validation / Blind Holdout`)**.

### Axis 2 — `CRITERIA, OBJECTIVES & SCALE PARITY` (Anti-Goodhart & Mathematical Soundness)
1. **One-Sided See-Saw Tuning, Single-Metric Bias & Compensatory Averaging (`UL-05`)**:
   - *Flaw*: Tuning thresholds or weights solely against false positives (or solely against false negatives), causing iterative see-saw oscillation; or averaging high secondary scores to mask a violation of a hard feasibility constraint (`c_k(x) == 0`).
   - *Fix*: Lock simultaneous **Bidirectional Counter-Anchors (`A_pos ∧ A_neg`)** plus domain extremes `(x_min, x_max)` in Phase 1, and enforce multiplicative hard-constraint sieves (`J(x) = (∏ c_k(x)) · ∑ w_i u_i(x)`) prior to weighted scoring.
2. **Piece-Wise Clamp Tautologies, Dead UI/Status Tiers & Premature Scale Erasure (`UL-06`)**:
   - *Flaw*: Clamping an upstream component to `[a_i, b_i]` where `a_i ≥ τ_gate` (turning downstream gate `S ≥ τ_gate` into a `100%` tautology and starving tiers `< a_i` to `0` hits); or clamping `[-1.0, 1.0]` before normalizing by upstream weight multipliers `α ∈ [α_min, α_max]`.
   - *Fix*: Verify `inf S_i < τ_gate ≤ sup S_i` and non-empty pre-image measure across every declared branch/tier (`Range(S) ∩ [τ_k, τ_{k+1}) ≠ ∅`), and normalize by `α_max` prior to unit-interval clipping.
3. **Hardcoded Index-Count Operators, Upsampling Illusions & Linear-on-Multiplicative Math (`UL-03`)**:
   - *Flaw*: Parameterizing windows, derivatives, or thresholds by raw index counts (`k` steps) instead of the discretization step measure `Δμ` (`Δt`, `Δx`, weight); treating interpolated/upsampled grids as higher-resolution ground truth; using linear `1 + cumsum(r)` on multiplicative processes; or scaling 2D visual radii linearly (`R ∝ Value` instead of `R ∝ √Value`).
   - *Fix*: Scale all operators explicitly by step measure `Δμ`, use exact log-compounding (`exp(cumsum(log1p(r)))`), replace binary step cliffs with smooth monotonic ramps, and enforce area-proportional radius scaling (`R ∝ √Value`).
4. **Infeasible Initial Seeds, Asymmetric Branch Thresholds & Bundled Rejection (`UL-05`)**:
   - *Flaw*: Selecting an unconstrained initial incumbent seed `x_0` that violates hard constraints enforced in subsequent iterations (trapping optimization in an infeasible state); drifting threshold constants across symmetric `if/else` branches; or rejecting a multi-component update when only one component regressed.
   - *Fix*: Enforce identical feasibility guards on initial seeds (`∏ c_k(x_0) == 1`), unify branch constants, and execute **Coordinate-Wise Marginal Attribution**.

### Axis 3 — `WIRING PROVENANCE, PARTITION CONSERVATION & ROLLBACK` (Connectivity & State Hygiene)
1. **Parent-to-Child Constraint Bypass, Blocking-`continue` Remainder Drop & Stage Massacre (`UL-04`)**:
   - *Flaw*: Checking size/validity limits on split child fragments (`C_i ⊂ P`) instead of the parent entity (`P`), allowing fragments of invalid macro-entities to leak downstream; executing a blocking `continue` after Stage A consumes `5%` of `P` (`P_A ⊂ P`) instead of forwarding the remainder `P_rem = P ∖ P_A` to Stage B/C; or silently dropping `> 50%` of upstream outputs in an unlogged post-filter.
   - *Fix*: Propagate parent macro-constraints to all child fragments (`C_i.parent_id == P.id`), forward unconsumed remainders `P_rem = P ∖ P_A`, log stage survival ratios (`|Out_k| ÷ |In_k|`), and assert closed-system conservation (`∑ μ(C_i) + μ(P_rem) == μ(P)`).
2. **Read-Only Feature Transform (`φ(x)`) Overwriting or Double-Compounding Ground Truth (`x`) (`UL-07`)**:
   - *Flaw*: Applying a non-linear contrast/sensitivity transform `φ(x)` to aid detection/ranking and then evaluating hard physical/accounting constraints on `φ(x)` instead of raw `x`, multiplying redundant colinear weights (`W(x) · g(φ(x))`), or writing post-transform outputs `T(x)` back into a base cache slot (`T(T(x))`).
   - *Fix*: Isolate `φ(x)` in a read-only representation stream, evaluate hard constraints and conservation strictly on raw `x`, and keep base caches pre-transform (`run(run(x)) == run(x)`).
3. **Test-vs-Live Callable Drift, Circuit-Breaker Truncation & Silent `try/except` Fallbacks (`UL-08`)**:
   - *Flaw*: Writing duplicate toy formulas or loading stale cached inputs inside test scripts while production resolves different live inputs; letting live safety defaults (`timeout`, `limit`, circuit breakers) truncate offline batch runs after `1%` of records with `exit code 0`; or masking broken schemas via `except Exception: return default_val`.
   - *Fix*: Import the exact production callable and live input resolver in verification probes, pass explicit offline limits (`assert N_processed == N_expected`), surface schema exceptions (`source != "fallback"`), and verify every parameter/control via `ΔX → ΔY ≠ 0`.
4. **DAG Initialization-Order Inversion, Stale View State & Non-Atomic State Rollback (`UL-07`)**:
   - *Flaw*: Computing an auxiliary table *after* a consumer has already checked `if exists(): join()`; mutating UI/render view modes without deterministic teardown of prior view elements; or rolling back a rejected candidate's pointer while leaving visited sets (`V_visited`) or elite archives (`A_elite`) corrupted.
   - *Fix*: Enforce strict DAG dependency order (`t_write < t_read`), deterministic view teardown on state transitions, and atomic tuple rollback preserving `A_elite ← top_k(A_elite ∪ {s'})`.

### Axis 4 — `HOT-PATH PERFORMANCE & ALGORITHMIC COMPLEXITY` (Speed & Memory Discipline)
1. **Monotonic Transform Commutation & Sub-Key Loop Hoisting (`UL-08`)**:
   - *Flaw*: Calling expensive transcendental/root functions (`exp`, `log`, `sqrt`) across `N × K` matrices before finding `argmax`/`min`, or recomputing quantities that depend only on `(A, B)` inside an inner `(C)` loop.
   - *Fix*: Find `argmax`/`min` in log-space or squared-norm space first and apply `exp`/`sqrt` only to the winner; hoist sub-key invariants into outer caches.
2. **Zero-Order-Hold Prefix Scans, Sparse Events & Tree/Index Lookups (`UL-08`)**:
   - *Flaw*: Writing sequential interpreter `for` loops for state latching ("freeze value at entry until exit"), recurrence scans, or `O(N²)` all-pairs lookups.
   - *Fix*: Vectorize zero-order-hold latches via `np.maximum.accumulate(np.where(is_entry, np.arange(n), 0))`, iterate only over sparse transition indices (`np.flatnonzero(can_change)`), pre-allocate contiguous arrays (`double[]`), and enforce `O(log N)` tree/B-tree/composite indexes (`< 5 ms`).
3. **Sibling-Consumer Deduplication & Lazy Post-Gate Serialization (`UL-08`)**:
   - *Flaw*: Multiple sibling consumers running identical transforms/simulations on the same inputs, or building heavy UI/telemetry snapshots for every candidate *before* the selection gate filters out losers.
   - *Fix*: Share cached simulation artifacts across sibling consumers and defer snapshot formatting strictly to the winning candidate.
4. **Cache-Clear Thrashing & Read-Only Slice Copy Bloat (`UL-08`)**:
   - *Flaw*: Evicting caches via `if len(cache) > M: cache.clear()` when `M < working_set_size` (causing cyclic 100% cache misses), or calling `.copy()` on read-only array/DataFrame slices inside sweeps.
   - *Fix*: Use zero-copy slice views and single-entry FIFO/LRU eviction (`cache.pop(next(iter(cache)))`).

---

## 4. The 8 Universal First-Principles Laws & Ephemeral Probe Matrix (`UL-01` to `UL-08`)

Every Wave 2 Blind Critic shard must execute the corresponding **Ephemeral Runtime Probe** in the project's native runtime (`0` domain jargon; `100%` applicable across all languages, algorithms, data pipelines, solvers, and UIs):

| Law ID | Universal Law Name | Formal Mathematical & Systems Formulation | Mandatory Wave 2 Ephemeral Runtime Probe (`assert ...`) | Interlock (`Gate × Axis`) |
| :---: | :--- | :--- | :--- | :---: |
| **`UL-01`** | **Bounded Interpolation vs. Unbounded Extrapolation & Graph-Cut Isolation** | **1. Bracketed Support**: Interpolate missing states only when bracketed on opposing sides by verified anchors (`x_left ≤ x ≤ x_right`); never extrapolate unboundedly from a single boundary.<br>**2. Graph-Cut & Prefix Isolation**: On graph `G = (V, E, w)`, never approximate `d_G(u, v)` with unconstrained norm `\|\|u - v\|\|` across absent edges `(u, v) ∉ E`; for causal operator `F`, `F(x)[0..t] == F(x[0..t])` with `0` blind holdout (`D_test`) queries. | Probe `x_ext ∉ [x_left, x_right]` → assert `status == OUT_OF_BOUNDS` or bounded prior clamp; mutate `x[t+1..T] ← 10 × x[t+1..T]` → assert `max(\|F(x_mut)[0..t] - F(x)[0..t]\|) == 0.0`; sever edge `e` → assert routing strictly within `E ∖ {e}`. | `G3` × `Axis 1.1, 1.4` |
| **`UL-02`** | **Two-Stage Candidate Pre-Filter (`S_cand`) vs. Exact Condition (`P(x)`) & Absorbing Failure** | **1. Exact Refinement**: Any index, window, bucket, or bounding lookup returns a candidate superset (`S_cand ⊇ S_exact`); compute all statistics and membership decisions strictly on `S_exact = {x ∈ S_cand : P(x)}`.<br>**2. Absorbing Failure Priority**: If intra-step state `s(τ)` (`τ ∈ [t, t + Δt]`) breaches `F_fail`, terminate immediately (`Failure > Success` on ties) without end-of-step `min/max` recovery. | Construct boundary noise item `x_noise ∈ S_cand ∖ S_exact` → assert `x_noise ∉ Output` and aggregate statistics match `S_exact` exactly; inject mid-step breach `g(s(t + Δt/2)) < 0` → assert terminal state `∈ F_fail`. | `G3` × `Axis 1.2, 1.3` |
| **`UL-03`** | **Discretization & Step-Measure Scaling Invariance (`Δμ`)** | Parameterize window spans, derivatives, decay rates, and thresholds explicitly by the discretization step measure `Δμ` (`Δt`, `Δx`, sample weight, batch span) rather than raw index counts (`k` steps). Rescaling resolution (`Δμ → Δμ/2`) must preserve the integrated quantity (`∑ f(x_i) Δμ_i == Const`), and interpolated/upsampled grids must never be treated as native high-resolution truth. | Resample input sequence at `2×` and `0.5×` step size (`Δμ/2`, `2·Δμ`); assert invariant integral/rate drift `abs(I(Δμ) - I(Δμ/2)) < ε` and dimensional homogeneity (`x = 0 → y = 0.0` with `0` `NaN`/`Inf`). | `G3, G4` × `Axis 2.3` |
| **`UL-04`** | **Hierarchical Partition, Parent Provenance & Remainder Conservation** | When decomposing or routing parent entity `P` across pipeline stages (`Stage 1 → 2 → 3`):<br>**1. Parent Provenance**: Child fragments `C_i ⊂ P` inherit macro-constraints of `P` (`C_i.parent_id == P.id`).<br>**2. Remainder Forwarding**: Partial stage matches (`P_A ⊂ P`) must forward unconsumed remainder `P_rem = P ∖ P_A` downstream (never drop `P` via blocking `continue`).<br>**3. Closed Accounting**: `∑ μ(C_i) + μ(P_rem) == μ(P)` and `C_i ∩ C_j == ∅`. | Assert `abs((sum(Child_k) + Remainder) - Parent) <= 1e-9`, pairwise disjointness `len(C_i & C_j) == 0`, `0` child fragments bypassing rejected parent `P`, and logged stage survival ratios `\|Out_k\| ÷ \|In_k\|`. | `G3` × `Axis 3.1` |
| **`UL-05`** | **Bidirectional Counter-Anchor & Non-See-Saw Law (`A_pos ∧ A_neg`)** | Never tune parameters, thresholds, or scoring functions on one-sided failure cases. Lock **both** positive target anchors (`A_pos`) and negative counter-veto anchors (`A_neg`), plus domain extremes `(x_min, x_max)`, simultaneously in a single test harness. Enforce non-compensatory hard constraints multiplicatively: `J(x) = (∏_k c_k(x)) · ∑_i w_i u_i(x)`. | Execute single-command assertion over `(A_pos, A_neg, x_min, x_max)`: assert `100%` pass on both `A_pos` and `A_neg`, `sign(f(x + δ) - f(x)) == expected_sign`, and `c_k(x) == 0 ⇒ J(x) == 0.0`. | `G4` × `Axis 2.1, 2.4` |
| **`UL-06`** | **Piece-Wise Codomain Reachability & Non-Tautological Clamp Law** | Every piece-wise branch `S_i(x) ∈ [a_i, b_i]`, downstream threshold `τ_gate`, and display/status bucket `[τ_k, τ_{k+1})` must satisfy `a_i < b_i`, `inf S_i < τ_gate ≤ sup S_i`, and `Range(S) ∩ [τ_k, τ_{k+1}) ≠ ∅`. If `a_i ≥ τ_gate`, the gate is a `100%` tautology; if `τ_{k+1} ≤ inf S_i`, the bucket is an unreachable dead state (`0` hits). Normalize upstream weight scales `α ∈ [α_min, α_max]` before unit clipping. | Sweep inputs across `[x_min, x_max]`: assert `0 < pass_rate(τ_gate) < 1` (non-tautological), `count(Bucket_k) > 0` for every declared tier `k`, and `g(f(x, 1.5α)) != g(f(x, α))`. | `G2, G4` × `Axis 2.2` |
| **`UL-07`** | **Read-Only Feature Transform (`φ(x)`) vs. Ground-Truth (`x`) Decoupling & Cache Idempotency** | Non-linear feature transforms `φ(x)` used to boost detection/ranking sensitivity must reside in a read-only representation stream and **never** overwrite raw ground-truth `x` used for hard constraints/accounting, multiply colinear downstream weights (`W(x) · g(φ(x))`), or write post-transform state `T(x)` back into base caches (`T(T(x))`). Candidate rejection must atomically rollback `(state, visited_set, elite_archive)`. | Run cached pipeline twice (`y1 = run(x); y2 = run(x)`) → assert `max(\|y1 - y2\|) == 0.0`; verify single-factor perturbation elasticity `d(log Y)/d(log x)` is not double-compounded; verify atomic state snapshot equality after rollback. | `G3` × `Axis 3.2, 3.4` |
| **`UL-08`** | **Live-Callable Parity, Finite-Difference Sensitivity (`ΔX → ΔY ≠ 0`) & Counterexample Ratchet** | **1. Production-Callable Parity**: Test harnesses must import and invoke the exact production callable and live input resolver (`callable.__module__ == prod_module`)—never re-type duplicate toy formulas or run against stale cached inputs.<br>**2. Sensitivity & Coverage**: Perturb each active input `x_i → x_i + δ` and assert `ΔY ≠ 0`, `N_processed == N_expected`, and `provenance != "fallback"`.<br>**3. Cumulative Ratchet**: Pin every user-flagged failure `(x_bad → expected)` into the persistent regression suite (`Pass_Set(t+1) ⊇ Pass_Set(t)`). | Assert `prod_fn.__module__ == target_module`, `prod_fn(x + δ) != prod_fn(x)`, `N_processed == N_expected`, `provenance != "fallback"`, `t_opt < t_base` with `0.0` numerical drift, and `100%` pass on `Ratchet_Suite(1..t)`. | `G1, G2, G5` × `Axis 3.3, 4.1–4.4` |
