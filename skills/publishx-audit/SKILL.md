---
name: publishx-audit
description: >
  Pre-flight security, secret, privacy, quality, and agent skill globalization audit (/publishx-audit, /publish-audit).
  Use when the user asks to audit before publish, scan for secrets or tokens, check API keys,
  or run /publishx-audit, /publish-audit, preflight audit, or audit a global agent skill.
  Do NOT use for documentation sync (/syncx) or QGIS zip packaging (/publishx-qgis).
---

# `/publishx-audit` (portable & 100% risk-proof)

Pre-flight security, privacy, and code quality engine for a **target directory**. Works on any OS. No workspace-specific paths.

---

## Platforms & Security Gates

Engine flag `--platform`: `generic` | `qgis` | `food4rhino` | `github` | `skill`.

| Profile | Blocking (must fix before release) | Advisory |
|:---|:---|:---|
| **skill** | Missing or malformed `SKILL.md` frontmatter; invalid `name` regex (`^[a-z0-9-]+$`) or >64 chars; `description` >1024 chars; machine user paths (`C:\Users\<user>`); secrets/tokens; backslashes in markdown links; recursive self-nesting (`skill/skill`); Python syntax errors in `scripts/*.py` | Non-globalized skill placement (isolated in workspace `.agents/skills/` instead of `~/.gemini/config/skills/`); description >500 chars (risking Antigravity system prompt context budget exhaustion); missing negative exclusion (`Do NOT use for...`); `disable-model-invocation: true` (hidden from agent prompt in Antigravity); non-standard `argument-hint`; hardcoded ephemeral counts (`all \d+ layers`) or personal hardware/persona strings; packaging debris (`__pycache__`, `.pyc`, `.DS_Store`); missing UTF-8 guard in helper scripts |
| **qgis** | Credentials / tokens (HF, PyPI, AWS, OpenAI, GitHub, Slack); machine user paths (`C:\Users\<user>`); unescaped `%` in `metadata.txt`; missing required metadata fields; `__init__.py` lacking `classFactory(iface)`; Qt6/QGIS 4 AST violations; Flake8 lint/syntax errors; unsafe `eval`/`exec`/`shell=True`/`pickle` | Packaging debris; missing icon; broad `except: pass` |
| **food4rhino** | Secrets; machine paths; **no `.gha`/`.dll`**; unsafe code | Missing sample `.gh` |
| **github** | Secrets; machine paths; **no LICENSE**; Flake8 violations | Missing README; debris; README words Published / LIVE / 1-click install without receipt |
| **generic** | Secrets; machine paths; syntax errors; Flake8 violations | Debris; README/LICENSE |

Public-claim **vocabulary** (LIVE, REGISTERED, PREPARED, IN PIPELINE) is owned by `/syncx`. This skill only **advises** on Published / LIVE / 1-click in README files.

---

## 6-Pillar Security & Quality Architecture

1. **Secrets & Privacy Gate (Zero Leaks)**:
   - Scans against high-entropy patterns: AWS, GitHub Classic & Fine-Grained, OpenAI, Anthropic, Google AI, HuggingFace, PyPI, GitLab, NPM, RSA/SSH keys, DB connection strings.
   - Dual-OS Invariant: strictly blocks machine user paths (`C:\Users\<user>`, `/Users/<user>`, `/home/<user>`).
2. **AST Vulnerability Inspector**:
   - Blocks dynamic execution: `eval()`, `exec()`, `compile()`.
   - Blocks shell injection: `os.system()`, `subprocess.*(..., shell=True)`.
   - Blocks unsafe deserialization: `pickle.load()`, `pickle.loads()`.
   - Blocks unsafe temp files: `tempfile.mktemp()`.
3. **Flake8 Code Quality Gate**:
   - Automatically executes Flake8 audit against the project's local `.flake8` configuration (bypassed for `--platform skill`).
   - Blocks releases on syntax errors, undefined variables, and style violations.
4. **Agent Skill Invariant Enforcer (`--platform skill`)**:
   - **Universal Globalization Verification**: Audits physical path to ensure the skill is stored in the Global Customizations Root (`~/.gemini/config/skills/`), warning if isolated in a project `.agents/skills` silo.
   - **Context Budget Protection**: Warns on descriptions > 500 characters to prevent triggering Antigravity's system prompt context budget limit and causing other skills to be silently excluded.
   - Validates `SKILL.md` frontmatter schema (`name`, `description`).
   - Audits model-invocation disclosure (flags `disable-model-invocation: true` to prevent accidental exclusion from Antigravity IDE prompt context).
   - Enforces POSIX forward slashes in markdown links (`[text](path/to/file)`) and verifies relative link target existence.
   - Detects hardcoded ephemeral snapshot counts (e.g. `all \d+ layers`) and personal hardware/persona leaks, enforcing universal behavioral formulation.
5. **Platform Invariant Enforcer (QGIS / Food4Rhino / GitHub)**:
   - QGIS: Validates `metadata.txt` (zero unescaped `%`), verifies `def classFactory(iface)` in `__init__.py`, and checks Qt6/QGIS 4 readiness via `check_qt6.py`.
   - Food4Rhino: Verifies compiled `.gha`/`.dll` assembly.
   - GitHub: Verifies OSI-compliant `LICENSE`.
6. **Packaging Hygiene**:
   - Detects build debris (`.pyc`, `__pycache__`, `Thumbs.db`, `.DS_Store`, `.swp`, `.env`).

---

## Protocol

### 1. Run the engine

Execute via cross-platform paths:

**macOS / Linux**:
```bash
python ~/.gemini/config/skills/publishx-audit/scripts/audit_engine.py <target_directory> --platform <generic|qgis|food4rhino|github|skill>
```

**Windows (PowerShell / Command Prompt)**:
```powershell
python "$env:USERPROFILE\.gemini\config\skills\publishx-audit\scripts\audit_engine.py" <target_directory> --platform <generic|qgis|food4rhino|github|skill>
```

*(Optional sidecar: chain [`/layax`](../layax/SKILL.md) via `/publishx-audit /layax` to semantically verify `LIVE` / `REGISTERED` / `PREPARED` public claims against receipts).*

### 2. Flags

- `--skip-flake8`: Bypass Flake8 code quality checks (if flake8 is temporarily unavailable).
- `--skip-qt6`: Bypass Qt6 AST forward-compatibility check for QGIS platform.

### 3. Output Format

```text
======================================================================
PRE-FLIGHT AUDIT SCORECARD
======================================================================
Target:    <target_dir>
Platform:  <platform>
Files:     <count>
Blocking:  0
Advisory:  <count>
----------------------------------------------------------------------
✅ VERDICT: PASS (100% Risk-Proof & Safe to Publish)
```

If a secret is found, the engine automatically masks it (`abcd...wxyz`).
For generating the deterministic QGIS release zip after audit passes, run `/publishx-qgis`.
