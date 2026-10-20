# Universal Workspace Documentation Auditor (`audit_workspace_docs.py`)

`audit_workspace_docs.py` is a 100% repository-agnostic CLI verifier for `/syncx`. It checks relative Markdown link integrity, enforces the Zero-LaTeX policy, sweeps for deprecated values (`--deprecated`), verifies SHA-256 mirror parity (`--mirror`), and automatically delegates to a project-local `scripts/audit_docs.py` if present in the target repository.
