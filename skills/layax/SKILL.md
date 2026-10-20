---
name: layax
description: >
  System 1 fast semantic decision, section shortlisting, and conflict triage sidecar (/layax, /laya).
  Use when running /layax or /laya standalone or chained (/syncx /layax, /briefx /layax, /deep-researchx /layax, /publishx-audit /layax)
  for local classification (choice), scoring (score), or truth validation (noul).
  Do NOT use for prose generation or code authoring.
---

# `/layax` (System 1 Decision & Semantic Triage Sidecar)

A lightweight, non-autoregressive **System 1 decision layer** for agent workflows (`/layax`, legacy alias `/laya`), powered by the local `laya` Python library (`convaiinnovations/laya` and `convaiinnovations/laya-multilingual`).

Runs as a standalone decision helper or as a pluggable zero-token accelerator chained with other `-x` skills (`/syncx /layax`, `/briefx /layax`, `/deep-researchx /layax`, `/researchx /layax`, `/publishx-audit /layax`).

Operates on **Dual-Process Cognitive Architecture**:
- **System 1 (`laya` Python Engine)**: Ultra-fast (~7–33 ms per pass), zero-LLM-token local semantic triage, section shortlisting (`shortlist_choice`), ordinal scoring (`score`), and calibrated contradiction testing (`noul`).
- **System 2 (Antigravity Agent)**: Deep deliberative reasoning, surgical code/doc editing (`edit_file`), tool execution, and strategic synthesis.

---

## 1. When to Use & When NOT to Use

| Need | Action |
|:---|:---|
| **Fast semantic contradiction hunting across docs** | Chain `/syncx /layax` (`noul` hypothesis check against SSOT) |
| **Shortlisting relevant sections in a large unpinned doc corpus** | Chain `/briefx /layax` or `/planx /layax` (`shortlist_choice` / `score`) |
| **Filtering 20+ scraped precedents or dataset rows before deep audit** | Chain `/deep-researchx /layax` or `/researchx /layax` (`score` + `noul`) |
| **Pre-flight public claim verification (`LIVE` vs `PREPARED`)** | Chain `/publishx-audit /layax` (`LayaGuardrail` / `noul`) |
| **Large-scale bilingual (Thai + English) text classification / scoring** | Run `/layax` standalone with `choice` or `score` |
| **Text generation, rewriting prose, or authoring code** | Do NOT use `/layax` (Delegate to Antigravity System 2 / [`/boostx`](../boostx/SKILL.md)) |
| **Exact keyword, symbol, or regex lookup** | Do NOT use `/layax` (Use native grep / `rg` / `Select-String`) |

---

## 2. Core Primitives Specification

The `laya` library evaluates state against typed question schemas in a single forward pass without generating text:

```python
# Laya Typed Question Schema (Python package: `import laya`)
questions = {
    # 1. choice: Calibrated categorical distribution across caller-defined labels
    "category": {
        "type": "choice",
        "criteria": {
            "odor": "กลิ่นเหม็น ขยะ สารเคมี กลิ่นไหม้",
            "leachate": "น้ำเสีย น้ำชะขยะ คลองเน่าเสีย",
            "noise": "มลพิษทางเสียง เครื่องจักร รถขยะ",
        },
    },
    # 2. score: Ordinal rubric (returns expected score on defined scale)
    "severity": {
        "type": "score",
        "scale": [0, 4],
    },
    # 3. noul: Calibrated boolean truth/contradiction hypothesis P(true)
    "is_contradicting_ssot": {
        "type": "noul",
        "hypothesis": "This statement contradicts the canonical project facts.",
    },
}
```

Built-in high-level integrations in `laya`:
* `LayaRouter` & `shortlist_choice`: Fast semantic routing and top-K section/label shortlisting.
* `LayaTriage` & `LayaEvaluator`: Batch ordinal scoring and prioritization.
* `LayaGuardrail`: Calibrated `noul` policy and claim verification.
* `detect_language` / `detect_script`: Pure-Python script detection (zero PyTorch import overhead until model inference is called).

---

## 3. SOP: Execution & Graceful Degradation Protocol

Every execution of `/layax` MUST adhere to the following sequence:

### Step 1: Pre-Flight Environment Probe
Before attempting neural inference, probe the local Python environment for the `laya` package:

```bash
python -c "import laya; print('LAYA_AVAILABLE', laya.__version__)"
```

### Step 2: Fork on Availability

#### Path A: `laya` IS Available (`LAYA_AVAILABLE` returned)
1. Initialize the appropriate model (`convaiinnovations/laya-multilingual` for Thai/mixed text or `convaiinnovations/laya` for English-only text).
2. Execute the fast System 1 sweep across the target document paragraphs, candidate records, or dataset chunks.
3. Filter results by calibrated confidence threshold:
   - **Clean / Low-Risk (`P < 0.30` for contradictions, or low relevance score)**: Skip without loading into the LLM context window.
   - **Anomalies / High-Signal Matches (`P ≥ 0.70` or `score ≥ 2.5`)**: Flag exact file paths and line ranges.
4. Pass only the filtered high-signal set to the primary skill for surgical resolution (`read_file` / `edit_file`).

#### Path B: `laya` is NOT Available (Package missing, no PyTorch, or lightweight machine)
1. Output a compact diagnostic notice:
   ```text
   [Layax Sidecar: `laya` package not detected in current Python environment → Falling back to native pattern & agent scanner]
   ```
2. **DO NOT CRASH OR HALT THE SESSION**.
3. Gracefully route the workflow back to native Antigravity tools:
   - For document audits ([`/syncx`](../syncx/SKILL.md)): use `audit_workspace_docs.py` and regex/grep sweeps.
   - For briefing/research ([`/briefx`](../briefx/SKILL.md), [`/deep-researchx`](../deep-researchx/SKILL.md)): use the 2-Pass Skeleton Read and parallel subagents.

---

## 4. Chained Skill Combinations

### 4.1 [`/syncx`](../syncx/SKILL.md) + `/layax` (`/syncx /layax` — Semantic Contradiction Hunter)
* **Role Division**:
  - `/layax` scans `.md` and `.html` paragraphs in milliseconds using `noul` to spot semantic contradictions against the canonical SSOT that keyword grep misses (e.g. one file stating a module is *deferred* while another implies it is *completed*).
  - `/syncx` manages the 5-Tier Document Matrix and applies surgical fixes via `edit_file` (`replace_file_content`).

### 4.2 [`/briefx`](../briefx/SKILL.md) + `/layax` (`/briefx /layax` — Large-Corpus Section Shortlisting)
* **Role Division**:
  - When exploring an unfamiliar or large unpinned documentation tree (`> 8` files or `> 500`-line specs), `/layax` runs `shortlist_choice` / `score` across heading chunks to rank the top sections matching the user's task.
  - `/briefx` then executes Pass B (`read_file`) strictly on the shortlisted line ranges, saving massive context tokens.

### 4.3 [`/deep-researchx`](../deep-researchx/SKILL.md) / [`/researchx`](../researchx/SKILL.md) + `/layax` (`/deep-researchx /layax` — Candidate Triage)
* **Role Division**:
  - Between Wave 2 (Harvester Swarm) and Wave 3 (Blind Adversarial Auditor), `/layax` scores harvested candidates using `score` (relevance/completeness) and `noul` (scope compliance) to prune obvious out-of-bounds candidates before spawning expensive Auditor subagent turns.

### 4.4 [`/publishx-audit`](../publishx-audit/SKILL.md) + `/layax` (`/publishx-audit /layax` — Public Claim Verifier)
* **Role Division**:
  - `/publishx-audit` runs deterministic AST, secret, path, and packaging checks via `audit_engine.py`.
  - `/layax` evaluates README and release prose using `noul` (`LayaGuardrail`) to verify that public status claims (`LIVE`, `REGISTERED`, `PREPARED`, `IN PIPELINE`) match verifiable receipts.

---

## 5. Formatting & Typography Rules

- **Zero-LaTeX Math Policy**: In all generated outputs and terminal logs, NEVER use LaTeX syntax (`$...$`). ALWAYS use direct Unicode: `→`, `←`, `•`, `✓`, `✨`, `²`, `³`, `°`, `×`, `÷`, `±`, `≈`, `≤`, `≥`.
- **ASCII Dash Convention**: Use standard ASCII hyphens `-` for bullet points and separators.
- **Table Formatting**: Use GitHub Flavored Markdown (GFM) tables with outer pipes (`| Col 1 | Col 2 |`).
