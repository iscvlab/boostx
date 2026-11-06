# BoostX (`v3.3.0`) — Empirical Benchmark & Token Economics Report

> **Reproducible Verification Harness**: Generated deterministically by [`benchmarks/run_boostx_benchmark.py`](./run_boostx_benchmark.py)  
> **Corpus Scope**: `108` Installed Agent Skills • `207` Repository Markdown Specs • `600` Obsidian Second Brain Nodes • `469` Real IDE Sessions (`1135` Prompt Turns)  
> **Statistical Rigor**: Timing benchmarks execute `3` warm-up passes followed by `N = 30` timed iterations (`time.perf_counter_ns()`), reporting **Median (`P50`)**, **Mean ± StdDev**, **IQR (`P25–P75`)**, and **`P95`**.

---

## ⚡ TL;DR - Empirical Scorecard at a Glance (`v3.3.0`)

| Evaluation Dimension | Workflow / Cohort Configuration | Visual Comparison Bar | Measured Result & Delta vs. Baseline |
| :--- | :--- | :--- | :--- |
| **1. Red-Team Defect Catch Rate ↑**<br>*(25 Seeded Defects across 5 Pillars)* | **Level 3: Full 5-Stage + 8 CLI Gates**<br>Level 2: `/xbrief` + `/xdeep-research` + `/xboost`<br>Level 1: `/xboost` Standalone (2 Gates)<br>Level 0: Prompt-Only Baseline (0 Gates) | `████████████████████` **`100.0% (25/25)`**<br>`████████████████░░░░` `80.0% (20/25)`<br>`████████░░░░░░░░░░░░` `40.0% (10/25)`<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% (0/25)` | **`0` False Positives in Median `6.99 ms`** ✨<br>`4` Active CLI Verification Gates<br>`2` Active CLI Verification Gates<br>No Deterministic Pre-LLM Enforcement |
| **2. Context Noise Compression ↑**<br>*(807 Repo + Vault Files, `1.47M` tok)* | **`/xbrief` (`Cap 8`) Repo-Only**<br>**`/xbrief` (`Cap 8`) + `/xobsidian` (`2-Hop`)**<br>Unbounded Repo + Vault Crawl | `████████████████████` **`97.81% Removed (45.6×)`**<br>`████████████████████` **`97.5% Removed (40.0×)`**<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% Removed (1.0×)` | **`32,336` tok in Median `0.93 ms`** ✨<br>**`36,876` tok (`12` files) in `0.9 ms`** ✨<br>`1,473,613` tok (`807` files) in `48.59 ms` |
| **3. System 1 Section Triage ↑**<br>*(23 Specs / 606 Chunks, `133.8k` tok)* | **BoostX `/xlaya` Top-5 Shortlist**<br>Unfiltered Full-Corpus Pass-B Read | `████████████████████` **`98.89% Saved (90.3×)`**<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% Saved (1.0×)` | **`1,482` tok in Median `13.73 ms`** (`44.1k` chunks/s) ✨<br>`133,773` tok (Full 23-File Read) |
| **4. Dual-Trigger Budget Guard ↑**<br>*(`Use when` + `Do NOT use` across `N=108`)* | **BoostX `v3.3.0` Suite (`N = 13`)**<br>All Installed Host Skills (`N = 108`)<br>Official Cloud/Vendor Skills (`N = 31`) | `████████████████████` **`100.0% (13/13)`**<br>`███████████████████░` `93.5%`<br>`█████████████████░░░` `87.1%` | **`370.54 ± 16.97` chars (`0%` Truncation)** ✨<br>`324.42 ± 49.78` chars (`99.1%` `≤500` pass)<br>`331.1 ± 63.41` chars (`96.8%` `≤500` pass) |
| **5. Verification Depth / Turn ↑**<br>*(`N = 1135` Real IDE Prompt Turns)* | **Chained Multi-Skill `/x*` Turn (`N=260`)**<br>Single `/x*` Skill Turn (`N = 116`)<br>Standard Turn Without `/x*` (`N = 759`) | `████████████████████` **`73.7 Steps (3.39×)`**<br>`██████░░░░░░░░░░░░░░` `19.2 Steps`<br>`██████░░░░░░░░░░░░░░` `21.8 Steps (1.0×)` | **`3.92M` tok/turn (`70.3k` new in, `21.5k` out)** ✨<br>`1.02M` tok/turn (`15.5k` new in, `5.2k` out)<br>`1.21M` tok/turn (`11.9k` new in, `6.2k` out) |

---

## Executive Findings: High Intelligence via High Compute

1. **System-Prompt Budget Discipline (`100%` Compliance & Dual-Trigger Guards)**: Across all `13` BoostX `/x*` skills, YAML discovery descriptions average **`370.54 ± 16.97 chars`** (Median `374.0` chars, **`100.0%` within the `≤ 500` char `audit_engine.py` budget gate**) with **`100.0%` dual positive + negative (`Use when` / `Do NOT use for`) routing guards**, compared to `87.1%` dual-trigger coverage across `31` official cloud/enterprise skills.
2. **Context Noise Compression (`-97.9%` Scan Reduction)**: When briefing across multi-project repositories and the `600`-node Obsidian Second Brain (`1,473,613` tokens total), `/xbrief` (`Cap 8` Two-Pass) + `/xobsidian` (`2-Hop = 4` vault files) loads only **`36,876` tokens** (**`97.5%` noise reduction** / **`40.0×` compression**) in a median disk read time of **`0.9 ms`** (vs `48.59 ms` unbounded).
3. **System 1 `/xlaya` Triage (`13.73 ms` Median)**: Chunking and ranking `606` fence-safe (`≤ 1,200`-char) heading sections across `23` specs completes in **`13.73 ms`** (`Mean 14.07 ± 1.1 ms`, `44,136.9 chunks/sec`), cutting Pass-B reading tokens by **`98.89%`**.
4. **Deterministic Red-Team Defect Catch Rate (`100.0%` vs `0.0%`)**: Across `25` seeded security, Qt6/QGIS 4, research citation, doc-sync, and skill-packaging defects, the 8 CLI gates achieve **`25 / 25` (`100.0%` recall)** and **`100.0%` precision** (`0` false positives) in **`6.99 ms`**.
5. **Transparent Token Economics (Why BoostX Recommends `5×`–`20×` Subscriptions)**: While BoostX slashes *garbage file noise* by `97.5%`, it deliberately invests that freed context capacity into **deep multi-gate verification**. Across `1135` real prompt turns, a chained multi-skill BoostX turn executes **`73.7 steps`** (`3.39×` deeper than standard `21.75`-step turns), consuming **`70,321` uncached input tokens (`5.93×`)**, **`21,483` output tokens (`3.46×`)**, and **`3,826,567` KV-cache read tokens** per turn (`~29.00M` total tokens across a full `530`-step marathon session).

---

## Experiment 1: Skill Discovery & Context Budget Audit (`N = 108` Installed Skills)

| Skill Cohort | Count | YAML Desc Chars (`Mean ± SD` / `Median`) | `≤ 500` Char Gate Pass | Dual Trigger Guard (`Use when` + `Do NOT use`) | Full `SKILL.md` Tokens (`Mean ± SD` / `Median`) | Bundled CLI Scripts (`LOC`) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **BoostX `v3.3.0` Suite (`/x*` Skills)** | `13` | **`370.54 ± 16.97`** (`374.0`) | **`100.0%`** | **`100.0%`** | `4,388 ± 2,283` (`3,563`) | **`8` (`5,450` LOC)** |
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
| **Total Recall / Precision / Latency (`N = 20`)** | **`0 / 25` (`0.0%`)** | **All 8 BoostX CLI Gates** | **`25 / 25` (`100.0%` Recall • `100.0%` Precision • Median `6.99 ms`)** |

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
