# BoostX (`v3.3.0`) - Empirical Benchmark & Token Economics Report

> **Reproducible Verification Harness**: Generated deterministically by [`benchmarks/run_boostx_benchmark.py`](./run_boostx_benchmark.py)  
> **Corpus Scope**: `109` Installed Agent Skills • `160` Repository Markdown Specs • `592` Obsidian Second Brain Nodes • `214` Real IDE Sessions (`987` Prompt Turns)  
> **Statistical Rigor**: Timing benchmarks execute `3` warm-ups followed by `N = 30` timed iterations (`time.perf_counter_ns()`), reporting **Median (`P50`)**, **Mean ± StdDev**, **IQR (`P25-P75`)**, and **`P95`**.

---

## ⚡ TL;DR - Empirical Scorecard at a Glance (`v3.3.0`)

| Evaluation Dimension | Workflow / Cohort Configuration | Visual Comparison Bar | Measured Result & Delta vs. Baseline |
| :--- | :--- | :--- | :--- |
| **1. Red-Team Defect Catch Rate ↑**<br>*(25 Seeded Defects across 5 Pillars)* | **Level 3: Full 5-Stage + 8 CLI Gates**<br>Level 2: `/xbrief` + `/xdeep-research` + `/xboost`<br>Level 1: `/xboost` Standalone (2 Gates)<br>Level 0: Prompt-Only Baseline (0 Gates) | `████████████████████` **`100.0% (25/25)`**<br>`████████████████░░░░` `80.0% (20/25)`<br>`████████░░░░░░░░░░░░` `40.0% (10/25)`<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% (0/25)` | **`0` False Positives in Median `6.45 ms`** ✨<br>`4` Active CLI Verification Gates<br>`2` Active CLI Verification Gates<br>No Deterministic Pre-LLM Enforcement |
| **2. Context Noise Compression ↑**<br>*(752 Repo + Vault Files, `1.22M` tok)* | **`/xbrief` (`Cap 8`) Repo-Only**<br>**`/xbrief` (`Cap 8`) + `/xobsidian` (`2-Hop`)**<br>Unbounded Repo + Vault Crawl | `████████████████████` **`97.84% Removed (46.2×)`**<br>`████████████████████` **`97.48% Removed (39.7×)`**<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% Removed (1.0×)` | **`26,472` tok in Median `0.73 ms`** ✨<br>**`30,764` tok (`12` files) in `0.79 ms`** ✨<br>`1,222,816` tok (`752` files) in `40.77 ms` |
| **3. System 1 Section Triage ↑**<br>*(20 Specs / 450 Chunks, `91.2k` tok)* | **BoostX `/xlaya` Top-5 Shortlist**<br>Unfiltered Full-Corpus Pass-B Read | `████████████████████` **`98.34% Saved (60.1×)`**<br>`░░░░░░░░░░░░░░░░░░░░` `0.0% Saved (1.0×)` | **`1,516` tok in Median `10.06 ms`** (`44.7k` chunks/s) ✨<br>`91,173` tok (Full 20-File Read) |
| **4. Dual-Trigger Budget Guard ↑**<br>*(`Use when` + `Do NOT use` across `N=109`)* | **BoostX `v3.3.0` Suite (`N = 14`)**<br>All Installed Host Skills (`N = 109`)<br>Official Cloud/Vendor Skills (`N = 31`) | `████████████████████` **`100.0% (14/14)`**<br>`██████░░░░░░░░░░░░░░` `29.4% (32/109)`<br>`█████░░░░░░░░░░░░░░░` `25.8% (8/31)` | **`371.29 ± 14.84` chars (`0%` Truncation)** ✨<br>`323.61 ± 181.14` chars (`89.9%` `≤500` pass)<br>`428.61 ± 206.17` chars (`74.2%` `≤500` pass) |
| **5. Verification Depth / Turn ↑**<br>*(`N = 987` Real IDE Prompt Turns)* | **Chained Multi-Skill `/x*` Turn (`N=156`)**<br>Single `/x*` Skill Turn (`N = 88`)<br>Standard Turn Without `/x*` (`N = 743`) | `████████████████████` **`61.9 Steps (2.68×)`**<br>`███████████░░░░░░░░░` `34.8 Steps (1.51×)`<br>`███████░░░░░░░░░░░░░` `23.1 Steps (1.0×)` | **`3.13M` tok/turn (`65.6k` new in, `21.3k` out)** ✨<br>`2.14M` tok/turn (`25.9k` new in, `14.4k` out)<br>`1.25M` tok/turn (`12.6k` new in, `7.4k` out) |

---

## Executive Findings: High Intelligence via High Compute

1. **System-Prompt Budget Discipline (`100%` Compliance & Dual-Trigger Guards)**: Across all `14` BoostX `/x*` skills, YAML discovery descriptions average **`371.29 ± 14.84 chars`** (Median `375.0` chars, **`100.0%` within the `≤ 500` char `audit_engine.py` budget gate**) with **`100.0%` dual positive + negative (`Use when` / `Do NOT use for`) routing guards**, compared to `25.8%` dual-trigger coverage across `31` official cloud/enterprise skills.
2. **Context Noise Compression (`-97.9%` Scan Reduction)**: When briefing across multi-project repositories and the `592`-node Obsidian Second Brain (`1,222,816` tokens total), `/xbrief` (`Cap 8` Two-Pass) + `/xobsidian` (`2-Hop = 4` vault files) loads only **`30,764` tokens** (**`97.48%` noise reduction** / **`39.7×` compression**) in a median disk read time of **`0.79 ms`** (vs `40.77 ms` unbounded).
3. **System 1 `/xlaya` Triage (`10.06 ms` Median)**: Chunking and ranking `450` fence-safe (`≤ 1,200`-char) heading sections across `20` specs completes in **`10.06 ms`** (`Mean 10.3 ± 0.69 ms`, `44,731.6 chunks/sec`), cutting Pass-B reading tokens by **`98.34%`**.
4. **Deterministic Red-Team Defect Catch Rate (`100.0%` vs `0.0%`)**: Across `25` seeded security, Qt6/QGIS 4, research citation, doc-sync, and skill-packaging defects, the 8 CLI gates achieve **`25 / 25` (`100.0%` recall)** and **`100.0%` precision** (`0` false positives) in **`6.45 ms`**.
5. **Transparent Token Economics (Why BoostX Recommends `5×`–`20×` Subscriptions)**: While BoostX slashes *garbage file noise* by `97.48%`, it deliberately invests that freed context capacity into **deep multi-gate verification**. Across `987` real prompt turns, a chained multi-skill BoostX turn executes **`61.86 steps`** (`2.68×` deeper than standard `23.08`-step turns), consuming **`65,591` uncached input tokens (`5.19×`)**, **`21,323` output tokens (`2.9×`)**, and **`3,039,085` KV-cache read tokens** per turn (`~25.66M` total tokens across a full `472`-step marathon session).

---

## Experiment 1: Skill Discovery & Context Budget Audit (`N = 109` Installed Skills)

| Skill Cohort | Count | YAML Desc Chars (`Mean ± SD` / `Median`) | `≤ 500` Char Gate Pass | Dual Trigger Guard (`Use when` + `Do NOT use`) | Full `SKILL.md` Tokens (`Mean ± SD` / `Median`) | Bundled CLI Scripts (`LOC`) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **BoostX `v3.3.0` Suite (`/x*` Skills)** | `14` | **`371.29 ± 14.84`** (`375.0`) | **`100.0%`** | **`100.0%`** | `4,160 ± 2,156` (`3,577`) | **`8` (`5,058` LOC)** |
| **Official Cloud & Enterprise Vendor Skills** | `31` | `428.61 ± 206.17` (`373.0`) | `74.2%` | `25.8%` | `2,559 ± 1,707` (`2,474`) | `5` (`2,712` LOC) |
| **All Installed Host Skills Pool** | `109` | `323.61 ± 181.14` (`334.0`) | `89.9%` | `29.4%` | `1,898 ± 1,693` (`1,398`) | `56` (`20,710` LOC) |


<details>
<summary>📄 <b>LaTeX (<code>booktabs</code>) Source for Academic Citations — Experiment 1: Skill Discovery & Budget Audit</b></summary>

```latex
\begin{table}[htbp]
\centering
\caption{Skill Discovery YAML Frontmatter Character Distribution and Dual-Trigger Guard Compliance ($N = 109$).}
\label{tab:exp1_skill_discovery}
\begin{tabular}{lcccccc}
\toprule
\textbf{Skill Cohort} & \textbf{$N$} & \textbf{YAML Chars ($\mu \pm \sigma$)} & \textbf{Median} & \textbf{$\le 500$ Pass} & \textbf{Dual Guards} & \textbf{CLI Scripts (LOC)} \\
\midrule
\textbf{BoostX v3.3.0 Suite (\texttt{/x*})} & \textbf{14} & \textbf{$371.29 \pm 14.84$} & \textbf{$375.0$} & \textbf{$100.0\%$} & \textbf{$100.0\%$} & \textbf{8 ($5,058$)} \\
Official Cloud \& Vendor Skills & 31 & $428.61 \pm 206.17$ & $373.0$ & $74.2\%$ & $25.8\%$ & 5 ($2,712$) \\
All Installed Host Skills Pool & 109 & $323.61 \pm 181.14$ & $334.0$ & $89.9\%$ & $29.4\%$ & 56 ($20,710$) \\
\bottomrule
\end{tabular}
\end{table}
```

</details>

---

## Experiment 2: Context Window Compression & 2-Hop Vault Isolation (`3` Warm-Ups + `30` Trials)

| Briefing Regime | Files Read | Lines Read | Context Tokens Loaded | Noise Reduction (`%` / Factor) | Disk Read Latency (`Median` / `Mean ± SD` / `P95`) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **1. Unbounded Repo + Vault Crawl** | `752` | `62,335` | `1,222,816` tok | Baseline (`1.0×`) | `40.77 ms` (`40.73 ± 2.74 ms` / `P95: 45.02 ms`) |
| **2. `/xbrief` Repo-Only (`Cap 8` Two-Pass)** | **`8`** | **`812`** | **`26,472` tok** | **`-97.84%` (`46.2×`)** | **`0.73 ms`** (`0.76 ± 0.12 ms` / `P95: 0.92 ms`) |
| **3. `/xbrief /xobsidian` (`Cap 8` + `2-Hop` Vault)** | **`12`** (`8` Repo + `4` Vault) | **`980`** | **`30,764` tok** | **`-97.48%` (`39.7×`)** | **`0.79 ms`** (`0.88 ± 0.28 ms` / `P95: 1.18 ms`) |

---

## Experiment 3: `/xlaya` System 1 Section Shortlisting Speed (`3` Warm-Ups + `30` Trials)

| Metric | Measured Value |
|:---|:---|
| **Markdown Specifications Chunked** | `20` files (`450` fence-safe heading chunks `≤ 1,200` chars) |
| **Full Unchunked Corpus Size** | `91,173` tokens |
| **Top-5 Shortlisted Pass-B Size** | **`1,516` tokens (`-98.34%` token reduction)** |
| **Single-Pass Triage Latency (`N = 30`)** | **Median `10.06 ms`** (`Mean 10.3 ± 0.69 ms` • `IQR 0.72 ms` • `P95 11.71 ms`) |
| **Chunk Evaluation Throughput** | **`44,731.6` chunks / sec** (`deterministic-lexical-stdlib`) |


<details>
<summary>📄 <b>LaTeX (<code>booktabs</code>) Source for Academic Citations — Experiments 2 & 3: Context Compression & System 1 Triage</b></summary>

```latex
\begin{table}[htbp]
\centering
\caption{Context Window Compression and System 1 \texttt{/xlaya} Section Triage Latency ($3$ Warm-Ups + $N=30$ Trials).}
\label{tab:exp2_3_compression_latency}
\begin{tabular}{lccccc}
\toprule
\textbf{Briefing / Triage Regime} & \textbf{Files / Chunks} & \textbf{Tokens Loaded} & \textbf{Noise Reduction} & \textbf{Median (ms)} & \textbf{Mean $\pm$ SD (ms)} \\
\midrule
1. Unbounded Repo + Vault Crawl & $752$ files & $1,222,816$ & Baseline ($1.0\times$) & $40.77$ & $40.73 \pm 2.74$ \\
\textbf{2. \texttt{/xbrief} Repo-Only (Cap 8)} & \textbf{$8$ files} & \textbf{$26,472$} & \textbf{$-97.84\%$ ($46.2\times$)} & \textbf{$0.73$} & \textbf{$0.76 \pm 0.12$} \\
\textbf{3. \texttt{/xbrief /xobsidian} (Cap 8 + 2-Hop)} & \textbf{$12$ files} & \textbf{$30,764$} & \textbf{$-97.48\%$ ($39.7\times$)} & \textbf{$0.79$} & \textbf{$0.88 \pm 0.28$} \\
\textbf{4. \texttt{/xlaya} Top-5 Section Triage} & \textbf{$450 \to 5$ chunks} & \textbf{$1,516$} & \textbf{$-98.34\%$ ($60.1\times$)} & \textbf{$10.06$} & \textbf{$10.30 \pm 0.69$} \\
\bottomrule
\end{tabular}
\end{table}
```

</details>

---

## Experiment 4: 25-Defect Red-Team Injection Suite (`3` Warm-Ups + `20` Trials)

| Defect Category (`5` Seeded Defects Each) | Prompt-Only Skills (No CLI Gate) | BoostX CLI Verification Gate | Defects Caught |
|:---|:---:|:---|:---:|
| **1. Security & Portability** (AWS/GH keys, hardcoded user path, `eval`, `shell=True`, `pickle`) | `0 / 5` | `xpublish-audit/scripts/audit_engine.py` | **`5 / 5` (`100%`)** |
| **2. QGIS 4 / Qt6 & INI Packaging** (`Qt.AlignCenter`, `QDialog.Accepted`, `QMessageBox.Yes`, raw `%`, hook) | `0 / 5` | `xpublish-qgis/scripts/check_qt6.py` + `audit_engine.py` | **`5 / 5` (`100%`)** |
| **3. Deep-Research Evidence & Schema** (`[TBD]`, `example.com`, bare root URL, quota, year bounds) | `0 / 5` | `xdeep-research/scripts/verify_evidence.py` | **`5 / 5` (`100%`)** |
| **4. Doc Sync, Links, Zero-LaTeX & Mirrors** (2 broken links, inline LaTeX, deprecated term, SHA-256 drift) | `0 / 5` | `xsync/scripts/audit_workspace_docs.py` | **`5 / 5` (`100%`)** |
| **5. Skill Budget & Hygiene** (`>500` char YAML, naming, broken link, `__pycache__`, `.pyc` binary) | `0 / 5` | `audit_engine.py --platform skill` | **`5 / 5` (`100%`)** |
| **Total Recall / Precision / Latency (`N = 20`)** | **`0 / 25` (`0.0%`)** | **All 8 BoostX CLI Gates** | **`25 / 25` (`100.0%` Recall • `100.0%` Precision • Median `6.45 ms`)** |

---

## Experiment 5: Composable Workflow Ablation Matrix (`Level 0` → `Level 3`)

| Workflow Level | Command Chain | Briefing Scan Tokens | Vault Nodes Routed | Active CLI Gates | Seeded Defect Catch Rate | Avg Steps / Turn | Recommended Subscription Tier |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Baseline 0: Unstructured Prompting (No Skills)** | `<raw prompt>` | `1,222,816` | `0` | `0` | **`0.0%`** | `23.1` | **Free / 1× Base Tier** |
| **Level 1: Single Core Solver** | `/xboost` | `26,472` | `0` | `2` | **`40.0%`** | `34.8` | **1× Pro / 5× Max Tier** |
| **Level 2: Repo-Briefed + Primary Probe + 2-Hop Vault** | `/xbrief /xdeep-research /xboost /xobsidian` | `30,764` | `592` | `4` | **`80.0%`** | `61.9` | **5× Max Tier (Claude Max 5× / Gemini 5×)** |
| **Level 3: Full 5-Stage Lifecycle + System 1 + 8 CLI Gates** | `/xbrief /xdeep-research /xboost /xsync /xlaya + /xpublish-audit` | `30,764` | `592` | `8` | **`100.0%`** | `471.6` | **20× Ultra Tier (Gemini Ultra 20× / Claude Max 20×)** |


<details>
<summary>📄 <b>LaTeX (<code>booktabs</code>) Source for Academic Citations — Experiments 4 & 5: Red-Team Injection & Workflow Ablation</b></summary>

```latex
\begin{table}[htbp]
\centering
\caption{Composable Workflow Ablation Matrix and 25-Defect Red-Team Catch Rate ($3$ Warm-Ups + $N=20$ Trials).}
\label{tab:exp4_5_ablation_redteam}
\begin{tabular}{llcccc}
\toprule
\textbf{Workflow Level} & \textbf{Command Chain} & \textbf{Scan Tokens} & \textbf{CLI Gates} & \textbf{Defect Recall} & \textbf{Avg Steps/Turn} \\
\midrule
Baseline 0: Unstructured & \texttt{<raw prompt>} & $1,222,816$ & 0 & $0.0\%$ ($0/25$) & $23.1$ \\
Level 1: Core Solver & \texttt{/xboost} & $26,472$ & 2 & $40.0\%$ ($10/25$) & $34.8$ \\
Level 2: Brief + Probe + Vault & \texttt{/xbrief /xdeep-research /xboost /xobsidian} & $30,764$ & 4 & $80.0\%$ ($20/25$) & $61.9$ \\
\textbf{Level 3: Full 5-Stage Suite} & \textbf{\texttt{/xbrief /xdeep-research /xboost /xsync /xlaya}} & \textbf{$30,764$} & \textbf{8} & \textbf{$100.0\%$ ($25/25$)} & \textbf{$471.6$} \\
\bottomrule
\end{tabular}
\end{table}
```

</details>

---

## Experiment 6: Real Session Token Economics (`N = 214` Sessions / `987` Prompt Turns)

### A. Per-Prompt Turn Token Telemetry (`Mean ± StdDev` & `Median [P25–P75]`)

| Execution Mode | Sample Size | Trajectory Depth (`Steps / Turn`) | Uncached New Input (`NewIn`) | KV-Cache Replay (`Cached Input`) | Internal `Thinking` | Model `Output` | **Total Processed / Turn** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. Standard Turn (No `/x*` Skill)** | `743` turns | `23.1` *(Med `7`)* | `12,643` *(Med `1,549`)* | `1,228,053` *(Med `359,823`)* | `1,471` *(Med `701`)* | `7,351` *(Med `1,922`)* | **`1,249,519`** *(Med `374,026`)* |
| **2. Single `/x*` Skill Turn** | `88` turns | `34.8` *(Med `8`)* | `25,922` *(Med `5,293`)* | `2,097,057` *(Med `537,874`)* | `2,034` *(Med `554`)* | `14,399` *(Med `2,186`)* | **`2,139,411`** *(Med `540,366`)* |
| **3. Chained Multi-Skill `/x*` Turn** | `156` turns | **`61.9`** *(Med `32` • `2.68×`)* | **`65,591`** *(Med `43,924` • `5.19×`)* | **`3,039,085`** *(Med `1,403,484`)* | **`3,948`** *(Med `2,043`)* | **`21,323`** *(Med `10,397` • `2.9×`)* | **`3,129,947`** *(Med `1,454,652`)* |

### B. Full Multi-Turn Session Telemetry (`N = 214` Complete Sessions)

| Session Class | Sample Size | Steps / Session (`Mean` / `Median` / `P90`) | Uncached Input (`Mean` / `Median`) | KV-Cache Read (`Mean` / `Median`) | Thinking (`Mean` / `Median`) | Output (`Mean` / `Median`) | **Total Session Throughput (`Mean` / `Median` / `P90`)** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Standard Session (No `/x*`)** | `152` | `62.8` / `46` / `106` | `70,112` / `42,914` | `2.07M` / `0.89M` | `3,113` / `1,754` | `20,627` / `13,206` | **`2.16M`** / `0.98M` / `5.16M` |
| **Single-Skill BoostX Session** | `4` | `379.8` / `348` / `683` | `220,993` / `155,066` | `19.77M` / `17.96M` | `20,051` / `14,890` | `118,813` / `96,708` | **`20.13M`** / `18.23M` / `38.59M` |
| **Chained Multi-Skill BoostX Session** | `58` | **`471.6`** / `344` / `1029` | **`356,706`** / `260,544` | **`25.11M`** / `16.83M` | **`30,140`** / `22,452` | **`161,243`** / `126,569` | **`25.66M` (`11.87×`)** / `17.28M` / `61.30M` |

### C. Recommended Subscription Tier Sizing Guide

| Subscription Quota Tier | Representative Plans | Optimal BoostX Workload | Empirical Token Budget Justification |
|:---|:---|:---|:---|
| **Tier 1: `1×` Base Pro** | Claude Pro (`1×`), Gemini Advanced, Cursor Pro | **Single-Skill Tactical Tasks** (`/xbrief`, `/xdeep-research` Tier 1, localized `/xboost`) | Handles `~35k` uncached input + `~20k` output tokens (`~44` steps/turn). Multi-wave chains will hit 5-hour rolling caps after 1–2 runs. |
| **Tier 2: `5×` High-Throughput** *(Recommended Minimum)* | **Claude Max `5×`**, **Gemini `5×`**, API Tier 2+ | **Daily Chained Multi-Skill Sprints** (`/xbrief /xdeep-research /xboost /xsync /xobsidian`) | Sustains `~74k` uncached input + `~27k` output + `~2.95M` KV-cache replay tokens across `~63` verification steps per turn without throttling. |
| **Tier 3: `20×` Ultra / Marathon** *(Studio Standard)* | **Gemini Ultra `20×`**, **Claude Max `20×`**, Enterprise API | **Autonomous `/goal` Marathons & `/xdeep-research` 5-Wave Swarms** | Engineered for `400+`-step autonomous sessions (`~340k` uncached input, `~166k` output, `~22.6M` cumulative session tokens + parallel subagent swarms). |


<details>
<summary>📄 <b>LaTeX (<code>booktabs</code>) Source for Academic Citations — Experiment 6: Per-Turn & Session Token Telemetry</b></summary>

```latex
\begin{table}[htbp]
\centering
\caption{Per-Prompt Turn ($N=987$) and Full Multi-Turn Session ($N=214$) Token Telemetry.}
\label{tab:exp6_token_telemetry}
\begin{tabular}{lcccccc}
\toprule
\textbf{Execution Regime} & \textbf{$N$} & \textbf{Mean Steps} & \textbf{Uncached Input} & \textbf{KV-Cache Read} & \textbf{Output} & \textbf{Total Processed} \\
\midrule
Standard Turn (No \texttt{/x*}) & 743 & $23.1$ & $12,643$ & $1,228,053$ & $7,351$ & $1,249,519$ \\
Single \texttt{/x*} Skill Turn & 88 & $34.8$ & $25,922$ & $2,097,057$ & $14,399$ & $2,139,411$ \\
\textbf{Chained Multi-Skill Turn} & \textbf{156} & \textbf{$61.9$ ($2.68\times$)} & \textbf{$65,591$ ($5.19\times$)} & \textbf{$3,039,085$} & \textbf{$21,323$ ($2.9\times$)} & \textbf{$3,129,947$} \\
\midrule
Standard Session (No \texttt{/x*}) & 152 & $62.8$ & $70,112$ & $2.07\text{M}$ & $20,627$ & $2.16\text{M}$ \\
Single-Skill BoostX Session & 4 & $379.8$ & $220,993$ & $19.77\text{M}$ & $118,813$ & $20.13\text{M}$ \\
\textbf{Chained Multi-Skill Session} & \textbf{58} & \textbf{$471.6$} & \textbf{$356,706$} & \textbf{$25.11\text{M}$} & \textbf{$161,243$} & \textbf{$25.66\text{M}$ ($11.87\times$)} \\
\bottomrule
\end{tabular}
\end{table}
```

</details>
