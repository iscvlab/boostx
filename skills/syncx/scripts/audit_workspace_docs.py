#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universal Workspace Documentation & Cross-File Consistency Auditor (/syncx).
Repository-agnostic deterministic verifier for Markdown (.md) and HTML (.html) suites:
  1. Relative Markdown Link Integrity (verifies local targets exist on disk)
  2. Zero-LaTeX Math Policy (flags inline $...$ or \\rightarrow / \\times outside code spans)
  3. Zero-Stale Deprecated Value Sweep (--deprecated "old_term_1,old_term_2")
  4. Exact SHA-256 Distribution Mirror Parity (--mirror "src:dst" + auto docs_reference/ detection)
  5. Optional Delegation to Repo-Local Auditor (scripts/audit_docs.py)
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
    ".pytest_cache",
}

LATEX_CMD_RE = re.compile(r"\\(?:rightarrow|leftarrow|leftrightarrow|times|approx|pm|leq|geq)\b")
INLINE_DOLLAR_RE = re.compile(r"(?<![\\`\w])\$(?!\s)([^$\n`]{1,80}?)(?<!\s|\\)\$(?![\w`])")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def sha256_bytes(path: Path) -> str:
    """Compute SHA-256 hex digest of file bytes (normalizing CRLF to LF for cross-OS parity)."""
    raw = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(raw).hexdigest()


def strip_code_regions(text: str, suffix: str) -> str:
    """Strip fenced code blocks, inline code spans, and HTML script/style blocks before prose scanning."""
    cleaned = text
    if suffix == ".md":
        cleaned = re.sub(r"```[\s\S]*?```", "", cleaned)
        cleaned = re.sub(r"`[^`\n]+`", "", cleaned)
    elif suffix == ".html":
        cleaned = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"<style\b[^>]*>[\s\S]*?</style>", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"<code\b[^>]*>[\s\S]*?</code>", "", cleaned, flags=re.IGNORECASE)
    return cleaned


def discover_doc_files(workspace_root: Path, include_obsidian: bool = False) -> list:
    """Discover active .md and .html files in workspace, respecting /syncx exclusion boundaries."""
    docs = []
    for root, dirs, files in os.walk(workspace_root):
        root_path = Path(root)
        # Skip Obsidian vaults unless --include-obsidian is explicitly enabled
        if not include_obsidian and (root_path / ".obsidian").is_dir():
            dirs[:] = []
            continue
        dirs[:] = [
            d for d in dirs
            if d not in EXCLUDED_DIRS and (include_obsidian or not (root_path / d / ".obsidian").is_dir())
        ]
        for fname in files:
            fpath = root_path / fname
            if fpath.suffix.lower() in {".md", ".html"}:
                docs.append(fpath)
    return sorted(docs)


def audit_workspace(args) -> int:
    ws_root = Path(args.workspace).resolve()
    if not ws_root.is_dir():
        print(f"ERROR: Workspace directory not found: {ws_root}", file=sys.stderr)
        return 1

    docs = discover_doc_files(ws_root, include_obsidian=args.include_obsidian)
    deprecated_terms = [t.strip() for t in args.deprecated.split(",") if t.strip()]

    errors = []
    warnings = []
    passes = []

    broken_links = 0
    latex_hits = 0
    deprecated_hits = 0

    for doc in docs:
        rel_doc = doc.relative_to(ws_root).as_posix()
        try:
            text = doc.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            warnings.append(f"[{rel_doc}] Unable to read file: {e}")
            continue

        suffix = doc.suffix.lower()
        prose = strip_code_regions(text, suffix)

        # 1. Relative Markdown Link Verification
        if suffix == ".md":
            for m in MD_LINK_RE.finditer(prose):
                label, target_url = m.group(1), m.group(2).strip()
                if target_url.startswith(("http://", "https://", "mailto:", "#", "file://", "conversation://")):
                    continue
                clean_rel = target_url.split("#")[0].split("?")[0].strip()
                if not clean_rel:
                    continue
                resolved = (doc.parent / clean_rel).resolve()
                if not resolved.exists():
                    broken_links += 1
                    errors.append(f"[{rel_doc}] Broken relative link: `[{label}]({target_url})`")

        # 2. Zero-LaTeX Math Policy Check
        if not args.allow_latex:
            for m in LATEX_CMD_RE.finditer(prose):
                latex_hits += 1
                errors.append(f"[{rel_doc}] LaTeX command `{m.group(0)}` detected (use native Unicode symbols).")
            if suffix == ".md":
                for m in INLINE_DOLLAR_RE.finditer(prose):
                    inner = m.group(1)
                    if any(op in inner for op in ("\\", "^", "_", "=", "\\times", "\\rightarrow")):
                        latex_hits += 1
                        errors.append(f"[{rel_doc}] Inline LaTeX math `${inner}$` detected (use native Unicode).")

        # 3. Deprecated Term Zero-Hit Sweep (skip immutable changelogs)
        is_historical = "changelog" in doc.name.lower() or "history" in doc.name.lower()
        if deprecated_terms and not is_historical:
            for term in deprecated_terms:
                if term in text:
                    deprecated_hits += 1
                    errors.append(f"[{rel_doc}] Deprecated value still present: `{term}`")

    if broken_links == 0:
        passes.append(f"Relative Markdown links verified across {len(docs)} files (0 broken links).")
    if not args.allow_latex and latex_hits == 0:
        passes.append("Zero-LaTeX Math Policy verified (0 inline LaTeX leaks).")
    if deprecated_terms and deprecated_hits == 0:
        passes.append(f"Deprecated value sweep clean (0 hits for {deprecated_terms}).")

    # 4. Exact Content / SHA-256 Distribution Mirror Parity
    mirror_pairs = []
    for pair_str in args.mirror:
        if ":" in pair_str:
            src_s, dst_s = pair_str.split(":", 1)
            mirror_pairs.append((ws_root / src_s.strip(), ws_root / dst_s.strip()))

    # Auto-detect docs/ -> */docs_reference/ mirrors if present in workspace
    docs_dir = ws_root / "docs"
    if docs_dir.is_dir():
        for ref_dir in ws_root.glob("*/docs_reference"):
            if ref_dir.is_dir():
                for mirrored_file in ref_dir.iterdir():
                    primary_file = docs_dir / mirrored_file.name
                    if mirrored_file.is_file() and primary_file.is_file():
                        mirror_pairs.append((primary_file, mirrored_file))

    for src_p, dst_p in mirror_pairs:
        if not src_p.is_file():
            errors.append(f"Mirror source missing: {src_p}")
            continue
        if not dst_p.is_file():
            errors.append(f"Mirror target missing: {dst_p}")
            continue
        src_hash = sha256_bytes(src_p)
        dst_hash = sha256_bytes(dst_p)
        rel_src = src_p.relative_to(ws_root).as_posix()
        rel_dst = dst_p.relative_to(ws_root).as_posix()
        if src_hash == dst_hash:
            passes.append(f"Mirror SHA-256 parity verified: `{rel_src}` == `{rel_dst}`")
        else:
            errors.append(
                f"Mirror content drift detected: `{rel_src}` ({src_hash[:8]}) != `{rel_dst}` ({dst_hash[:8]})"
            )

    # 5. Optional Delegation to Repo-Local scripts/audit_docs.py
    local_auditor = ws_root / "scripts" / "audit_docs.py"
    if local_auditor.is_file() and local_auditor.resolve() != Path(__file__).resolve():
        proc = subprocess.run(
            [sys.executable, str(local_auditor), str(ws_root)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if proc.returncode == 0:
            passes.append("Repo-local `scripts/audit_docs.py` passed (exit code 0).")
        else:
            errors.append(f"Repo-local `scripts/audit_docs.py` failed:\n{proc.stdout}\n{proc.stderr}")

    print("=" * 70)
    print("SYNCX WORKSPACE DOCUMENTATION AUDIT SCORECARD")
    print("=" * 70)
    print(f"Workspace: {ws_root}")
    print(f"Files:     {len(docs)} (.md / .html)")
    print(f"Blocking:  {len(errors)}")
    print(f"Advisory:  {len(warnings)}")
    print("-" * 70)

    for p in passes:
        print(f"  ✓ {p}")
    for w in warnings:
        print(f"  ! {w}")
    for err in errors:
        print(f"  ✗ {err}")

    if errors:
        print("\n❌ VERDICT: FAIL (Resolve synchronization errors above)")
        return 1

    print("\n✅ VERDICT: PASS (100% Workspace Sync Invariants Verified)")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Universal Workspace Documentation Auditor (/syncx)")
    parser.add_argument("workspace", nargs="?", default=".", help="Target workspace root directory (default: .)")
    parser.add_argument(
        "--deprecated",
        type=str,
        default="",
        help="Comma-separated list of deprecated values/counts that must have 0 hits",
    )
    parser.add_argument(
        "--mirror",
        action="append",
        default=[],
        help="Explicit mirror pair 'src_rel_path:dst_rel_path' for SHA-256 content parity check",
    )
    parser.add_argument("--allow-latex", action="store_true", help="Allow inline LaTeX math syntax in docs")
    parser.add_argument(
        "--include-obsidian",
        action="store_true",
        help="Include directories containing .obsidian/ (use only when /syncx /obsidianx is active)",
    )
    args = parser.parse_args()
    sys.exit(audit_workspace(args))


if __name__ == "__main__":
    main()
