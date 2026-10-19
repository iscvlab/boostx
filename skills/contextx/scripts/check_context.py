#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Context Compaction Diagnostic Helper
Analyzes the active Antigravity IDE transcript to determine the current
compaction round, step metrics, and memory degradation risk.

Part of the /contextx skill. Cross-platform (Windows, macOS, Linux).
Zero external dependencies (Python stdlib only).
"""

import os
import sys
import json
import argparse

# BoostX UTF-8 stream guard
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def get_brain_dirs():
    """Resolve the platform-appropriate brain directories for Antigravity IDE."""
    candidates = [
        os.path.expanduser("~/.gemini/antigravity/brain"),
        os.path.expanduser("~/.gemini/antigravity-ide/brain"),
        os.path.expanduser("~/Library/Application Support/antigravity-ide/brain"),
    ]
    return [c for c in candidates if os.path.isdir(c)]


def find_active_conversation_dir(conv_id=None):
    """Find conversation directory by ID or by latest modification time."""
    brain_dirs = get_brain_dirs()
    if not brain_dirs:
        return None

    if conv_id:
        for bdir in brain_dirs:
            target = os.path.join(bdir, conv_id)
            if os.path.isdir(target):
                return target

    # Find the most recently modified transcript.jsonl across all brain dirs
    entries = []
    for bdir in brain_dirs:
        for d in os.listdir(bdir):
            full_p = os.path.join(bdir, d)
            transcript_p = os.path.join(full_p, ".system_generated", "logs", "transcript.jsonl")
            if os.path.isdir(full_p) and not d.startswith(".") and os.path.isfile(transcript_p):
                entries.append((os.path.getmtime(transcript_p), full_p))

    if not entries:
        return None

    return max(entries, key=lambda x: x[0])[1]


def analyze_transcript(conv_dir):
    """Parse transcript.jsonl and extract compaction metrics."""
    transcript_path = os.path.join(conv_dir, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.isfile(transcript_path):
        return None

    total_steps = 0
    user_inputs = 0
    compaction_checkpoints = []

    with open(transcript_path, "r", encoding="utf-8", errors="replace") as f:
        for idx, line in enumerate(f):
            total_steps += 1
            try:
                data = json.loads(line)
            except Exception:
                continue

            msg_type = data.get("type", "")
            source = data.get("source", "")
            content = str(data.get("content", ""))

            if msg_type == "USER_INPUT" and source == "USER_EXPLICIT":
                user_inputs += 1

            if msg_type == "CHECKPOINT" or "resuming from a compaction" in content.lower():
                if "resuming from a compaction" in content.lower():
                    compaction_checkpoints.append(idx)

    compaction_round = len(compaction_checkpoints)
    last_compaction_step = compaction_checkpoints[-1] if compaction_checkpoints else 0
    steps_since_compaction = (total_steps - last_compaction_step) if compaction_checkpoints else total_steps

    # Health status evaluation
    if compaction_round == 0 and total_steps < 120:
        health = "HEALTHY"
        level_icon = "🟢"
        risk_desc = "Optimal context capacity. Zero compaction rounds."
        recommendation = "Safe to continue in the current conversation."
        action = "CONTINUE"
    elif compaction_round <= 1 and total_steps < 250:
        health = "NOMINAL"
        level_icon = "🟡"
        risk_desc = "Good context retention with mild history compaction."
        recommendation = "Safe for continued execution. Keep edits focused."
        action = "CONTINUE"
    elif compaction_round == 2 or total_steps < 350:
        health = "CAUTION"
        level_icon = "🟠"
        risk_desc = "Memory pruning active. Early constraints may begin to drift."
        recommendation = "Wrap up the active milestone soon. Plan to start a fresh chat for the next phase."
        action = "PREPARE_TRANSITION"
    else:
        health = "CRITICAL"
        level_icon = "🔴"
        risk_desc = f"Heavy compaction (Round {compaction_round}). High risk of hallucinated constraints and timeouts."
        recommendation = (
            "Strongly recommend starting a fresh conversation now. "
            "Run `/kickoffx` to verify doc sync and generate the prompt for the next session."
        )
        action = "START_NEW_CHAT"

    return {
        "conv_id": os.path.basename(conv_dir),
        "compaction_round": compaction_round,
        "total_steps": total_steps,
        "user_inputs": user_inputs,
        "steps_since_compaction": steps_since_compaction,
        "health": health,
        "level_icon": level_icon,
        "risk_desc": risk_desc,
        "recommendation": recommendation,
        "action": action,
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze Antigravity context compaction metrics")
    parser.add_argument("--conv-id", type=str, default=None, help="Target conversation ID")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of markdown")
    args = parser.parse_args()

    conv_dir = find_active_conversation_dir(args.conv_id)
    if not conv_dir:
        print("Error: Could not locate active conversation directory in brain logs.", file=sys.stderr)
        sys.exit(1)

    metrics = analyze_transcript(conv_dir)
    if not metrics:
        print(f"Error: Could not read transcript logs in {conv_dir}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(metrics, indent=2))
        return

    # Render clean GitHub-flavored markdown scorecard
    print("\n### Context & Compaction Scorecard\n")
    print("| Metric | Value | Status |")
    print("|:---|:---|:---:|")
    round_str = f"Round {metrics['compaction_round']}"
    status_str = f"{metrics['level_icon']} {metrics['health']}"
    print(f"| **Compaction Round** | {round_str} | {status_str} |")
    print(f"| **Total Session Steps** | {metrics['total_steps']} steps | — |")
    print(f"| **User Prompts Processed** | {metrics['user_inputs']} prompts | — |")
    print(f"| **Steps Since Last Compaction** | {metrics['steps_since_compaction']} steps | — |")
    print(f"| **Conversation ID** | `{metrics['conv_id'][:8]}...` | — |\n")
    print(f"**Diagnostic Assessment**: {metrics['risk_desc']}\n")
    print(f"**Recommendation**: {metrics['recommendation']}\n")

    if metrics["action"] in ("PREPARE_TRANSITION", "START_NEW_CHAT"):
        print(
            "👉 **Next Step**: Run `/kickoffx` to verify document synchronization, "
            "review next-phase options, and generate a pristine prompt for your fresh conversation.\n"
        )


if __name__ == "__main__":
    main()
