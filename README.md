# Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v2.0.0-blue.svg)](https://github.com/napattan/agent-skills/releases/tag/v2.0.0)
[![Platforms](https://img.shields.io/badge/Platforms-Claude_•_Grok_•_Gemini_•_Cursor_•_Codex-8A2BE2)](#-universal-installation)
[![Dual-OS](https://img.shields.io/badge/Dual--OS-Windows_•_macOS_•_Linux-success)](#-portable-by-design)
[![Verification](https://img.shields.io/badge/Protocol-BoostX_Verified-emerald)](#-portable-by-design)

> **Portable developer protocols for AI coding assistants.**  
> Same SKILL.md files on Claude Code, Grok, Gemini/Antigravity, Cursor, Codex, and similar loaders. IDE or CLI. Windows, macOS, and Linux. Not locked to one machine or one repo.

Sister repo: **[mcp-bridges](https://github.com/napattan/mcp-bridges)** (QGIS, Rhino, Grasshopper, Illustrator, Figma).

---

## Universal installation

Clone this repository, then put the `skills/` folder into **your host's skill root**. The files do not change per host.

| Host | Typical skill root |
|:---|:---|
| Claude Code | `~/.claude/skills` or `<repo>/.claude/skills` |
| Grok | `$GROK_HOME/skills` or `~/.grok/skills` or `<repo>/.grok/skills` |
| Gemini / Antigravity | `~/.gemini/config/skills` |
| Cursor / Codex / other IDEs | often `<repo>/.agents/skills` |

```bash
git clone https://github.com/napattan/agent-skills.git ~/.claude/skills
git clone https://github.com/napattan/agent-skills.git ~/.grok/skills
git clone https://github.com/napattan/agent-skills.git ~/.gemini/config/skills
git clone https://github.com/napattan/agent-skills.git .agents/skills
```

Windows PowerShell: `$env:USERPROFILE\.claude\skills`, `$env:USERPROFILE\.grok\skills`, `$env:USERPROFILE\.gemini\config\skills`.

Or run `scripts/install.ps1` (Windows) / `scripts/install.sh` (macOS, Linux). The installer copies into roots that already exist on this machine (`--claude`, `--grok`, `--antigravity`, or a workspace path).

Pin a known line with the tag: `git clone --branch v2.0.0 https://github.com/napattan/agent-skills.git`

---

## The suite

```
agent-skills/skills/
├── /boostx           2D Task × Project goal synthesis, Physics Triad & red-green problem solving
├── /brief            4-tier authority hierarchy, two-pass structural reading & invariant loading
├── /create-skill     author, distill & globalize portable SKILL.md files with context budget guard
├── /deep-researchx   5-wave multi-agent deep research, blind adversarial audit & 100%-proof engine
├── /publish-audit    6-pillar security, AST, Flake8, platform & skill globalization audit gate
├── /publish-qgis     QGIS 4 scoped enums, pure runtime & deterministic zip packaging
├── /researchx        tactical primary-source research, local SDK/DB/binary probe & architecture study
└── /update-doc       5-tier cross-document sync, conflict arbitration & zero-stale verification
```

| Skill | Command | What it does | What it stops |
|:---|:---|:---|:---|
| **BoostX** | `/boostx` | 2D `Task × Project` Goal Contract synthesis, Tri-Track Red gate (bugs, greenfield, simulation Physics Triad), Ponytail × Deep Module ladder, Universal Parity (Dual-OS + OneDrive + IDE/CLI), and composable `/goal`, `/researchx`, and `/deep-researchx` escalation. | Speculative edits, shallow wrapper bloat, physics unit/CFL blowups, hardcoded user paths |
| **Brief** | `/brief` | Discover related markdown in the **current workspace** via a 4-tier authority hierarchy (capped at 8 files), apply Two-Pass reading (`Pass A` structural skeleton/cardinality before `Pass B` deep dive), check deferred/frozen boundaries, and execute `/brief <task>` in the same turn. | Answering from memory, keyword tunneling without section cardinality, editing frozen zones |
| **Create Skill** | `/create-skill` | Universal Skill Globalization (`~/.gemini/config/skills`), Context Budget Guard (`≤ 350 chars` YAML description to prevent prompt truncation), 4-step cognitive distillation, and `--platform skill` pre-flight verification. | Workspace-siloed skills, bloated descriptions that drop sibling skills, hardcoded paths |
| **Deep-ResearchX** | `/deep-researchx` | Universal 5-Wave multi-agent deep research: (1) 2D `Intent × Domain` contract synthesis, (2) parallel Harvester scouts, (3) Blind Adversarial Auditor + deterministic `verify_evidence.py` with Wave 3.5 Prune & Replace loop, (4) 100%-Proof `[VERIFIED FACT]` vs `[RECOMMENDED SYNTHESIS]` binding, and (5) composable `/boostx` & `/goal` handoff. | Search-snippet hallucinations, conflated completion vs policy dates, root-domain lazy links, data forgery |
| **Publish Audit** | `/publish-audit` | 6-Pillar security & quality architecture (`generic`, `qgis`, `food4rhino`, `github`, `skill`): 16 high-entropy secret patterns, AST vulnerability scanner, Flake8 quality gate, Agent Skill Globalization & Context Budget auditor, and QGIS/GitHub/Food4Rhino invariants. | Leaked credentials, shell injection risks, broken skill frontmatter, unformatted code |
| **Publish QGIS** | `/publish-qgis` | 5-Gate release packaging: Qt6 / QGIS 4 scoped enum enforcement (`QPageSize.Unit`, `QPageLayout.Orientation`), pure runtime asset filtering (strips dev/test scripts), SemVer bumps, and deterministic byte-reproducible zip archives. Run after `/publish-audit` is green. | Plugin portal rejections, Qt6 deprecation warnings, folder-name mismatches, machine timestamp leaks |
| **ResearchX** | `/researchx` | Tactical primary-source counterpart to `/boostx`: 3-tier scope routing (inline probe vs isolated scout vs parallel swarm), 4-tier authority ladder (local pinned manifests/DBs/ASTs first, version-matched specs second), capability-aware subagent write routing, and `/brief`-ready Markdown notes. | Secondary-blog guesswork, researching wrong library versions, context-bloating raw dumps |
| **Update Doc** | `/update-doc` | 4-level Conflict Arbitration Hierarchy (Code/Data Receipts > Canonical SSOT > Chat Lock > Drafts), ghost reference & quantitative cardinality sweeps, 5-tier inner-to-outer sync with interactive HTML DOM/JS parity, distribution mirror byte parity, and final Sync Ledger. | Stale claims, unarbitrated doc contradictions, ghost links to deleted files, mirror drift |

Public status words (owned by `/update-doc`): **LIVE**, **REGISTERED** (or pending), **PREPARED**, **IN PIPELINE**, **DRAFT**. Do not claim public availability without a verifiable receipt.

---

## Portable by design

- **Any host:** feature-detect tools. Works inline or with subagents across Antigravity, Claude Code, Grok, Cursor, and Codex.
- **Any OS:** POSIX `/` in files; PowerShell and POSIX examples, or Python stdlib. No `C:\Users\<you>` in committed text.
- **Any repo:** `/update-doc` and `/deep-researchx` dynamically discover workspace rules without baked-in project filenames.
- **Typography for user-facing/release copy:** no em/en dashes (ASCII hyphen `-` is fine). Direct Unicode symbols (`→`, `×`, `≈`, `±`, `≤`, `≥`, `✓`), zero LaTeX math delimiters.

BoostX ladder (used by all skills here): YAGNI, reuse, stdlib, Deep Module seam, shortest diff. YAML `description` stays compact (`≤ 350 chars`) with a `Do NOT use for` clause.

---

## Repository layout

```
agent-skills/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── skills/
│   ├── boostx/SKILL.md
│   ├── brief/SKILL.md
│   ├── create-skill/SKILL.md
│   ├── deep-researchx/
│   │   ├── SKILL.md
│   │   └── scripts/verify_evidence.py
│   ├── publish-audit/
│   │   ├── SKILL.md
│   │   └── scripts/audit_engine.py
│   ├── publish-qgis/
│   │   ├── SKILL.md
│   │   └── scripts/check_qt6.py, package_qgis.py
│   ├── researchx/SKILL.md
│   └── update-doc/
│       ├── SKILL.md
│       ├── LICENSE
│       └── scripts/README.md
└── scripts/
    ├── install.sh
    └── install.ps1
```

---

## Related toolkits

- **[mcp-bridges](https://github.com/napattan/mcp-bridges):** MCP bridges for **QGIS, Rhino 3D, Grasshopper, Adobe Illustrator, and Figma**.

---

## Author

**Napat Phasundhiae**  
*Computational Design Technologist | Spatial Analytics • Urban & Environmental Simulation • Workflow Automation*

- GitHub: [@napattan](https://github.com/napattan)
- LinkedIn: [linkedin.com/in/napatphas](https://www.linkedin.com/in/napatphas/)

## License

[MIT License](LICENSE)
