# BoostX (`v3.4.0`) — Empirical Benchmark & Token Economics Report

> **Reproducible Verification Harness**: Generated deterministically by [`benchmarks/run_boostx_benchmark.py`](./run_boostx_benchmark.py)  
> **Corpus Scope**: `108` Installed Agent Skills • `207` Repository Markdown Specs • `600` Obsidian Second Brain Nodes • `469` Real IDE Sessions (`1135` Prompt Turns) • `18` Upstream Open-Source Contributions  
> **Statistical Rigor**: Timing benchmarks execute `3` warm-up passes followed by `N = 30` timed iterations (`time.perf_counter_ns()`), reporting **Median (`P50`)**, **Mean ± StdDev**, **IQR (`P25–P75`)**, and **`P95`**.

---

## ⚡ TL;DR - Empirical Scorecard at a Glance (`v3.4.0`)

| Evaluation Dimension | Workflow / Cohort Configuration | Visual Comparison Bar | Measured Result & Delta vs. Baseline |
| :--- | :--- | :--- | :--- |
| **1. Red-Team Defect Catch Rate ↑**<br>*(25 Seeded Defects across 5 Pillars)* | **Level 3: Full 5-Stage + 8 CLI Gates**<br>Level 2: `/xbrief` + `/xdeep-research` + `/xboost`<br>Level 1: `/xboost` Standalone (2 Gates)<br>Level 0: Prompt-Only Baseline (0 Gates) | `████████████████████` **`100.0% (25/25)`**<br>`████████████████░░░░` `80.0% (20/25)`<br>`████████░░░░░░░░░░░░` `40.0% (10/25)`<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% (0/25)` | **`0` False Positives in Median `6.99 ms`** ✨<br>`4` Active CLI Verification Gates<br>`2` Active CLI Verification Gates<br>No Deterministic Pre-LLM Enforcement |
| **2. Context Noise Compression ↑**<br>*(807 Repo + Vault Files, `1.47M` tok)* | **`/xbrief` (`Cap 8`) Repo-Only**<br>**`/xbrief` (`Cap 8`) + `/xobsidian` (`2-Hop`)**<br>Unbounded Repo + Vault Crawl | `████████████████████` **`97.81% Removed (45.6×)`**<br>`████████████████████` **`97.5% Removed (40.0×)`**<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% Removed (1.0×)` | **`32,336` tok in Median `0.93 ms`** ✨<br>**`36,876` tok (`12` files) in `0.9 ms`** ✨<br>`1,473,613` tok (`807` files) in `48.59 ms` |
| **3. System 1 Section Triage ↑**<br>*(23 Specs / 606 Chunks, `133.8k` tok)* | **BoostX `/xlaya` Top-5 Shortlist**<br>Unfiltered Full-Corpus Pass-B Read | `████████████████████` **`98.89% Saved (90.3×)`**<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% Saved (1.0×)` | **`1,482` tok in Median `13.73 ms`** (`44.1k` chunks/s) ✨<br>`133,773` tok (Full 23-File Read) |
| **4. Dual-Trigger Budget Guard ↑**<br>*(`Use when` + `Do NOT use` across `N=108`)* | **BoostX `v3.4.0` Suite (`N = 13`)**<br>All Installed Host Skills (`N = 108`)<br>Official Cloud/Vendor Skills (`N = 31`) | `████████████████████` **`100.0% (13/13)`**<br>`███████████████████░` `93.5%`<br>`█████████████████░░░` `87.1%` | **`370.54 ± 16.97` chars (`0%` Truncation)** ✨<br>`324.42 ± 49.78` chars (`99.1%` `≤500` pass)<br>`331.1 ± 63.41` chars (`96.8%` `≤500` pass) |
| **5. Verification Depth / Turn ↑**<br>*(`N = 1135` Real IDE Prompt Turns)* | **Chained Multi-Skill `/x*` Turn (`N=260`)**<br>Single `/x*` Skill Turn (`N = 116`)<br>Standard Turn Without `/x*` (`N = 759`) | `████████████████████` **`73.7 Steps (3.39×)`**<br>`██████░░░░░░░░░░░░░░` `19.2 Steps`<br>`██████░░░░░░░░░░░░░░` `21.8 Steps (1.0×)` | **`3.92M` tok/turn (`70.3k` new in, `21.5k` out)** ✨<br>`1.02M` tok/turn (`15.5k` new in, `5.2k` out)<br>`1.21M` tok/turn (`11.9k` new in, `6.2k` out) |
| **6. Compound Learning OSS Speedups ↑**<br>*(`18` Upstream Contributions, `Batch 0 + A + B`)* | **`PAT-*` + `GOV-*` + `FALS-*` Playbook**<br>Unvectorized Upstream Baseline (`HEAD`) | `████████████████████` **`4.0× – 1,735.6× Faster`**<br>`░░░░░░░░░░░░░░░░░░░░` `1.0× Baseline` | **`100%` `assert_allclose` Parity (`4 MERGED`, `10 OPEN PRs`)** ✨<br>Python `np.vectorize`, `O(N²)` scans & OGR disk-seek loops |

---

## Executive Findings: High Intelligence via High Compute

1. **System-Prompt Budget Discipline (`100%` Compliance & Dual-Trigger Guards)**: Across all `13` BoostX `/x*` skills, YAML discovery descriptions average **`370.54 ± 16.97 chars`** (Median `374.0` chars, **`100.0%` within the `≤ 500` char `audit_engine.py` budget gate**) with **`100.0%` dual positive + negative (`Use when` / `Do NOT use for`) routing guards**, compared to `87.1%` dual-trigger coverage across `31` official cloud/enterprise skills.
2. **Context Noise Compression (`-97.9%` Scan Reduction)**: When briefing across multi-project repositories and the `600`-node Obsidian Second Brain (`1,473,613` tokens total), `/xbrief` (`Cap 8` Two-Pass) + `/xobsidian` (`2-Hop = 4` vault files) loads only **`36,876` tokens** (**`97.5%` noise reduction** / **`40.0×` compression**) in a median disk read time of **`0.9 ms`** (vs `48.59 ms` unbounded).
3. **System 1 `/xlaya` Triage (`13.73 ms` Median)**: Chunking and ranking `606` fence-safe (`≤ 1,200`-char) heading sections across `23` specs completes in **`13.73 ms`** (`Mean 14.07 ± 1.1 ms`, `44,136.9 chunks/sec`), cutting Pass-B reading tokens by **`98.89%`**.
4. **Deterministic Red-Team Defect Catch Rate (`100.0%` vs `0.0%`)**: Across `25` seeded security, Qt6/QGIS 4, research citation, doc-sync, and skill-packaging defects, the 8 CLI gates (`5,458` LOC) achieve **`25 / 25` (`100.0%` recall)** and **`100.0%` precision** (`0` false positives) in **`6.99 ms`**.
5. **Transparent Token Economics (Why BoostX Recommends `5×`–`20×` Subscriptions)**: While BoostX slashes *garbage file noise* by `97.5%`, it deliberately invests that freed context capacity into **deep multi-gate verification**. Across `1135` real prompt turns, a chained multi-skill BoostX turn executes **`73.7 steps`** (`3.39×` deeper than standard `21.75`-step turns), consuming **`70,321` uncached input tokens (`5.93×`)**, **`21,483` output tokens (`3.46×`)**, and **`3,826,567` KV-cache read tokens** per turn (`~29.00M` total tokens across a full `530`-step marathon session).
6. **Cross-Workspace Compound Learning (`4.0×` – `1,735.6×` Real-World Upstream Speedups)**: By distilling verified bug and bottleneck signatures into [`docs/COMPOUND_LEARNING_PLAYBOOK.md`](../docs/COMPOUND_LEARNING_PLAYBOOK.md) (`PAT-*`, `GOV-*`, `FALS-*`), BoostX achieved **`4.0×` to `1,735.6×` measured wall-clock speedups** with **`100%` numerical equivalence** across **18 upstream open-source contributions** (`Batch 0` + `Group A` + `Group B`).

---

## Experiment 1: Skill Discovery & Context Budget Audit (`N = 108` Installed Skills)

| Skill Cohort | Count | YAML Desc Chars (`Mean ± SD` / `Median`) | `≤ 500` Char Gate Pass | Dual Trigger Guard (`Use when` + `Do NOT use`) | Full `SKILL.md` Tokens (`Mean ± SD` / `Median`) | Bundled CLI Scripts (`LOC`) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **BoostX `v3.4.0` Suite (`/x*` Skills)** | `13` | **`370.54 ± 16.97`** (`374.0`) | **`100.0%`** | **`100.0%`** | `4,388 ± 2,283` (`3,563`) | **`8` (`5,458` LOC)** |
| **Official Cloud & Enterprise Vendor Skills** | `31` | `331.1 ± 63.41` (`324.0`) | `96.8%` | `87.1%` | `2,520 ± 1,694` (`2,468`) | `5` (`2,880` LOC) |
| **All Installed Host Skills Pool** | `108` | `324.42 ± 49.78` (`318.5`) | `99.1%` | `93.5%` | `2,055 ± 1,912` (`1,430`) | `57` (`23,265` LOC) |

---

## Experiment 2: Context Window Compression & 2-Hop Vault Isolation (`3` Warm-Ups + `30` Trials)

| Briefing Regime | Files Read | Lines Read | Context Tokens Loaded | Noise Reduction (`%` / Factor) | Disk Read Latency (`Median` / `Mean ± SD` / `P95`) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **1. Unbounded Repo + Vault Crawl** | `807` | `68,324` | `1,473,613` tok | Baseline (`1.0×`) | `48.59 ms` (`48.22 ± 2.82 ms` / `P95: 53.34 ms`) |
| **2. `/xbrief` Repo-Only (`Cap 8` Two-Pass)** | **`8`** | **`826`** | **`32,336` tok** | **`-97.81%` (`45.6×`)** | **`0.93 ms`** (`1.01 ± 0.2 ms` / `P95: 1.47 ms`) |
| **3. `/xbrief /xobsidian` (`Cap 8` + `2-Hop` Vault)** | **`12`** (`8` Repo + `4` Vault) | **`995`** | **`36,876` tok** | **`-97.5%` (`40.0×`)** | **`0.9 ms`** (`0.95 ± 0.12 ms` / `P95: 1.16 ms`) |

---

## Experiment 3: `/xlaya` System 1 Section Shortlisting Speed (`3` Warm-Ups + `30` Trials)

| Metric | Measured Value |
|:---|:---|
| **Markdown Specifications Chunked** | `23` files (`606` fence-safe heading chunks `≤ 1,200` chars) |
| **Full Unchunked Corpus Size** | `133,773` tokens |
| **Top-5 Shortlisted Pass-B Size** | **`1,482` tokens (`-98.89%` token reduction)** |
| **Single-Pass Triage Latency (`N = 30`)** | **Median `13.73 ms`** (`Mean 14.07 ± 1.1 ms` • `IQR 1.59 ms` • `P95 15.63 ms`) |
| **Chunk Evaluation Throughput** | **`44,136.9` chunks / sec** (`deterministic-lexical-stdlib`) |

---

## Experiment 4: 25-Defect Red-Team Injection Suite (`3` Warm-Ups + `20` Trials)

| Defect Category (`5` Seeded Defects Each) | Prompt-Only Skills (No CLI Gate) | BoostX CLI Verification Gate | Defects Caught |
|:---|:---:|:---|:---:|
| **1. Security & Portability** (AWS/GH keys, hardcoded user path, `eval`, `shell=True`, `pickle`) | `0 / 5` | `xpublish/scripts/audit_engine.py` | **`5 / 5` (`100%`)** |
| **2. QGIS 4 / Qt6 & INI Packaging** (`Qt.AlignCenter`, `QDialog.Accepted`, `QMessageBox.Yes`, raw `%`, hook) | `0 / 5` | `xpublish/scripts/check_qt6.py` + `audit_engine.py` | **`5 / 5` (`100%`)** |
| **3. Deep-Research Evidence & Schema** (`[TBD]`, `example.com`, bare root URL, quota, year bounds) | `0 / 5` | `xdeep-research/scripts/verify_evidence.py` | **`5 / 5` (`100%`)** |
| **4. Doc Sync, Links, Zero-LaTeX & Mirrors** (2 broken links, inline LaTeX, deprecated term, SHA-256 drift) | `0 / 5` | `xsync/scripts/audit_workspace_docs.py` | **`5 / 5` (`100%`)** |
| **5. Skill Budget & Hygiene** (`>500` char YAML, naming, broken link, `__pycache__`, `.pyc` binary) | `0 / 5` | `audit_engine.py --platform skill` | **`5 / 5` (`100%`)** |
| **Total Recall / Precision / Latency (`N = 20`)** | **`0 / 25` (`0.0%`)** | **All 8 BoostX CLI Gates (`5,458` LOC)** | **`25 / 25` (`100.0%` Recall • `100.0%` Precision • Median `6.99 ms`)** |

---

## Experiment 5: Composable Workflow Ablation Matrix (`Level 0` → `Level 3`)

| Workflow Level | Command Chain | Briefing Scan Tokens | Vault Nodes Routed | Active CLI Gates | Seeded Defect Catch Rate | Avg Steps / Turn | Recommended Subscription Tier |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Baseline 0: Unstructured Prompting (No Skills)** | `<raw prompt>` | `1,473,613` | `0` | `0` | **`0.0%`** | `21.8` | **Free / 1× Base Tier** |
| **Level 1: Single Core Solver** | `/xboost` | `32,336` | `0` | `2` | **`40.0%`** | `19.2` | **1× Pro / 5× Max Tier** |
| **Level 2: Repo-Briefed + Primary Probe + 2-Hop Vault** | `/xbrief /xdeep-research /xboost /xobsidian` | `36,876` | `600` | `4` | **`80.0%`** | `73.7` | **5× Max Tier (Claude Max 5× / Gemini 5×)** |
| **Level 3: Full 5-Stage Lifecycle + System 1 + 8 CLI Gates** | `/xbrief /xdeep-research /xboost /xsync /xlaya + /xpublish` | `36,876` | `600` | `8` | **`100.0%`** | `530.4` | **20× Ultra Tier (Gemini Ultra 20× / Claude Max 20×)** |

---

## Experiment 6: Real Session Token Economics (`N = 469` Sessions / `1135` Prompt Turns)

### A. Per-Prompt Turn Token Telemetry (`Mean ± StdDev` & `Median [P25–P75]`)

| Execution Mode | Sample Size | Trajectory Depth (`Steps / Turn`) | Uncached New Input (`NewIn`) | KV-Cache Replay (`Cached Input`) | Internal `Thinking` | Model `Output` | **Total Processed / Turn** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. Standard Turn (No `/x*` Skill)** | `759` turns | `21.8` *(Med `6`)* | `11,854` *(Med `1,151`)* | `1,195,166` *(Med `289,021`)* | `1,349` *(Med `585`)* | `6,202` *(Med `1,494`)* | **`1,214,571`** *(Med `298,845`)* |
| **2. Single `/x*` Skill Turn** | `116` turns | `19.2` *(Med `6`)* | `15,534` *(Med `3,699`)* | `1,002,132` *(Med `487,628`)* | `1,082` *(Med `356`)* | `5,208` *(Med `1,846`)* | **`1,023,956`** *(Med `494,966`)* |
| **3. Chained Multi-Skill `/x*` Turn** | `260` turns | **`73.7`** *(Med `46` • `3.39×`)* | **`70,321`** *(Med `50,445` • `5.93×`)* | **`3,826,567`** *(Med `2,101,384`)* | **`4,362`** *(Med `2,620`)* | **`21,483`** *(Med `12,662` • `3.46×`)* | **`3,922,734`** *(Med `2,154,486`)* |

### B. Full Multi-Turn Session Telemetry (`N = 469` Complete Sessions)

| Session Class | Sample Size | Steps / Session (`Mean` / `Median` / `P90`) | Uncached Input (`Mean` / `Median`) | KV-Cache Read (`Mean` / `Median`) | Thinking (`Mean` / `Median`) | Output (`Mean` / `Median`) | **Total Session Throughput (`Mean` / `Median` / `P90`)** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Standard Session (No `/x*`)** | `397` | `47.4` / `35` / `92` | `66,711` / `49,519` | `1.43M` / `0.73M` | `2,444` / `1,373` | `14,361` / `7,594` | **`1.51M`** / `0.80M` / `3.18M` |
| **Single-Skill BoostX Session** | `2` | `13.0` / `13` / `20` | `26,146` / `26,146` | `0.25M` / `0.25M` | `768` / `768` | `1,644` / `1,644` | **`0.28M`** / `0.28M` / `0.45M` |
| **Chained Multi-Skill BoostX Session** | `70` | **`530.4`** / `379` / `1230` | **`406,934`** / `318,341` | **`28.41M`** / `18.40M` | **`31,842`** / `25,156` | **`153,412`** / `135,124` | **`29.00M` (`19.17×`)** / `18.84M` / `68.10M` |

### C. Recommended Subscription Tier Sizing Guide

| Subscription Quota Tier | Representative Plans | Optimal BoostX Workload | Empirical Token Budget Justification |
|:---|:---|:---|:---|
| **Tier 1: `1×` Base Pro** | Claude Pro (`1×`), Gemini Advanced, Cursor Pro | **Single-Skill Tactical Tasks** (`/xbrief`, `/xdeep-research` Tier 1, localized `/xboost`) | Handles `~35k` uncached input + `~20k` output tokens (`~44` steps/turn). Multi-wave chains will hit 5-hour rolling caps after 1–2 runs. |
| **Tier 2: `5×` High-Throughput** *(Recommended Minimum)* | **Claude Max `5×`**, **Gemini `5×`**, API Tier 2+ | **Daily Chained Multi-Skill Sprints** (`/xbrief /xdeep-research /xboost /xsync /xobsidian`) | Sustains `~74k` uncached input + `~27k` output + `~2.95M` KV-cache replay tokens across `~63` verification steps per turn without throttling. |
| **Tier 3: `20×` Ultra / Marathon** *(Studio Standard)* | **Gemini Ultra `20×`**, **Claude Max `20×`**, Enterprise API | **Autonomous `/goal` Marathons & `/xdeep-research` 5-Wave Swarms** | Engineered for `400+`-step autonomous sessions (`~340k` uncached input, `~166k` output, `~22.6M` cumulative session tokens + parallel subagent swarms). |

---

## Experiment 7: Compound Learning Framework & Real-World Upstream Open-Source Speedup Receipts (`18` Contributions)

To evaluate how [`docs/COMPOUND_LEARNING_PLAYBOOK.md`](../docs/COMPOUND_LEARNING_PLAYBOOK.md) (`PAT-*` Defect & Bottleneck Catalog, `GOV-*` Governance Fingerprints, and `FALS-*` Mirage Guardrails) compounds engineering effectiveness across external codebases, we executed BoostX (`Stage 1 /xbrief + /xdeep-research → Stage 3 /xboost + /xultra → Stage 4 /xpublish --platform pr + /xsync --federated`) across **18 upstream open-source contributions** spanning `Batch 0` (Agent & Document AI Infrastructure), `Group A` (GeoAI, Remote Sensing & Urban Ecology), and `Group B` (Global ESG, Physical Climate Risk & Urban Physics):

| Cohort & Upstream Target | Playbook Patterns & Governance | Baseline Bottleneck / Defect (`HEAD`) | BoostX Patch & Numerical Verification | Measured Wall-Clock Speedup / Receipt |
|:---|:---|:---|:---|:---|
| **`Group B` — [`ladybug-tools/uwg #292`](https://github.com/ladybug-tools/uwg/pull/292)** *(MIT)* | `PAT-VEC-03`, `PAT-STATE-01..02`, `PAT-GIT-01`, `GOV-02` | `sum(soil_temp)` inside `105,120`-step loop (`8.85 s`); hardcoded `[0]` climate zone (`#291`); `windProf` step-buffer leak | Hoisted precomputed `forcIP.deepTemp` (`5.10 ms`); indexed `[zone_idx]`; reset `windProf`; preserved upstream `CRLF` (`38`-line diff) | **`1,735.6×` speedup** (`68/68` `pytest` PASS) |
| **`Group B` — [`os-climate/physrisk #651`](https://github.com/os-climate/physrisk/pull/651)** *(FINOS / Linux Foundation)* | `PAT-VEC-01..02`, `PAT-STATE-01`, `PAT-NUM-01`, `GOV-01` | `O(N²)` list scan in `geocode_in_place` (`541.3 ms`); `np.vectorize` in `get_impact_distrib` (`7.15 s`); caller array mutation & `left = -1` wrap | Direct key iteration (`0.32 ms`); broadcasted `scipy.stats.norm.cdf` (`0.22 s`); non-mutating `np.minimum`; clamped `np.maximum(0, right - 1)` | **`1,669.6×` & `32.5×` speedups** (`11/11` `pytest` PASS, `DCO -s`) |
| **`Group B` — [`CLIMADA-project/climada_python #1349`](https://github.com/CLIMADA-project/climada_python/pull/1349) & [`#1350`](https://github.com/CLIMADA-project/climada_python/pull/1350)** *(ETH Zürich)* | `PAT-VEC-01`, `PAT-SPARSE-01`, `PAT-NUM-01`, `GOV-04` | Scalar `box()` loop in `points_to_raster` (`1.49 s`); CSR column-slice loop in `impact_at_reg`; `.nonzero()` explicit-zero drop; ISO/NaN bugs (`#1331`) | C-vectorized `shapely.box` (`21.5 ms`); `imp_mat @ reg_ind` CSR matmul; direct `.indices`/`.indptr` read; ISO & `isnan` guards | **`69.3×` & `14.0×` speedups** (`17/17` tests PASS, `base: develop`) |
| **`Group B` — [`Deltares/hydromt #1566`](https://github.com/Deltares/hydromt/pull/1566)** *(Deltares Netherlands)* | `PAT-VEC-01`, `PAT-GIS-01`, `PAT-STATE-02`, `GOV-03` | Scalar `box()` loop in `create_mesh2d_from_geom` (`897 ms`); dropped `crs` on projected `bbox` (`#1563`); `nodata_ref = None` before warning log | C-vectorized `shapely.box` (`32.6 ms`); passed `crs=self.metadata.crs` & reprojected `geom`; logged `nodata_ref` before reset | **`27.5×` speedup** (`114/114` `pytest` PASS, `docs/changelog.rst`) |
| **`Group B` — [`natcap/invest #2813`](https://github.com/natcap/invest/issues/2813#issuecomment-6675810100) & [`#2829`](https://github.com/natcap/invest/issues/2829)** *(Stanford NatCap)* | `PAT-VEC-03`, `PAT-GIS-01`, `PAT-GIT-01`, `GOV-05` | Repeated OGR `GetFeature(fid)` + `wkb.loads` inside AOI R-tree loops (`420.2 ms` UCM, `421.6 ms` UFRM); `&` vs `\|` nodata mask; dead test paths | Pass-1 FID geometry/attribute cache (`18.0 ms` UCM, `22.0 ms` UFRM); De Morgan `\|` nodata mask; cleaned `test_ucm.py` | **`23.4×` UCM & `19.2×` UFRM speedups** (`100%` parity) |
| **`Group A` — [`martibosch/pylandstats #77`](https://github.com/martibosch/pylandstats/pull/77)** | `PAT-VEC-02` | Per-label `scipy.ndimage.center_of_mass` scan (`79.85 ms` on `66,496` patches); `dtype=object` crash in `compute_entropy` (`#50`) | Single-pass vectorized `np.bincount(labels.ravel(), weights=...)` (`19.76 ms`) + `centroids=False` extension (`#69`) | **`4.0×` speedup** (`9/9` `pytest` PASS) |
| **`Group A` — [`opengeos/geoai #960`](https://github.com/opengeos/geoai/pull/960) & [`segment-geospatial #569`](https://github.com/opengeos/segment-geospatial/pull/569)** | `PAT-ENV-01`, `PAT-STATE-01`, `PAT-3D-01`, `GOV-06` | Host `PYTHONEXECUTABLE` venv bleed (`#951`); missing `SamGeo` vector attributes (`#543`) & stale `_metadata` across `set_image()` | Sanitized `PYTHON*` env vars across 3 managers; added `source_name`/`scores`/`attributes` & state reset in `SamGeo 1/2/3` | `40/40` & `55/55` `pytest` PASS • **Both `@coderabbitai` `APPROVED`** |
| **`Group A` — [`Weecology/DeepForest #1440`](https://github.com/weecology/DeepForest/issues/1440#issuecomment-6657781223) & [`gboeing/osmnx #1405`](https://github.com/gboeing/osmnx/issues/1405#issuecomment-6657781737)** | `PAT-ENV-01`, `PAT-STATE-01`, `GOV-07` | `PathLike` rejection in `preprocess.py` (`#1440`); parallel `pytest-xdist` state collision in `test_simplify_graph` & `test_elevation` (`#1405`) | Accepted `(str, os.PathLike)` via `os.fspath()`; registered `xdist_group` marker & wrapped `elevation_url_template` in `try/finally` | `19/19` & `5/5` `pytest` PASS • Type C claims & branches ready |
| **`Batch 0` — [`xerj-org/xerj #2922–#2927`](https://github.com/xerj-org/xerj/pulls?q=is%3Apr+author%3Anapattan) & [`scb-10x/typhoon-ocr #15`](https://github.com/scb-10x/typhoon-ocr/pull/15)** | `PAT-OCR-01`, `PAT-ENV-01` | Sub-max image upscale (`5.11×` token bloat); legacy Thai PDF PUA junking (`exit 3`); Windows MSVC `#[cfg(unix)]` & spool lock test failures | Downscale-only `resize_if_needed`; Rust/Python Thai PUA + Sara-Am normalizer; `.gemini/config/skills` discovery; Windows test fixes | **`-35.9%` vision tokens** • **`1,912/1,954` MSVC tests** • **`4 MERGED`** |
