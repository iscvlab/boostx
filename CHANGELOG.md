# Changelog

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
git clone --branch v2.0.0 https://github.com/napattan/agent-skills.git
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
git clone --branch v1.3.0 https://github.com/napattan/agent-skills.git
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
git clone --branch v1.2.0 https://github.com/napattan/agent-skills.git
```

## v1.1.0

- `/brief`: load related workspace markdown (cap 8), then do `/brief <task>` in the same turn. HTML only when the task is a specific page. Portable: no baked-in filename list.
- `/create-skill`: machine-path ban uses `C:\Users\<user>` so `/publish-audit --platform github` does not treat ellipsis placeholders as a real home path.

### Install

See README. Tag: `v1.1.0`.
```bash
git clone --branch v1.1.0 https://github.com/napattan/agent-skills.git
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
git clone --branch v1.0.0 https://github.com/napattan/agent-skills.git
```
