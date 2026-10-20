#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Context Compaction Diagnostic Helper (check_context.py)
Analyzes the active Antigravity IDE transcript to determine the current
compaction round, active window pressure, step metrics, and memory drift risk.

Part of the /contextx skill. Cross-platform (Windows, macOS, Linux).
Zero external dependencies (Python stdlib only).
"""

import argparse
import json
import os
import sys

sys.dont_write_bytecode = True

# BoostX UTF-8 stream guards
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ESTIMATED_STEPS_PER_COMPACTION = 170


def get_brain_dirs():
    """Resolve the platform-appropriate brain directories for Antigravity IDE."""
    candidates = [
        os.path.expanduser("~/.gemini/antigravity/brain"),
        os.path.expanduser("~/.gemini/antigravity-ide/brain"),
        os.path.expanduser("~/Library/Application Support/antigravity-ide/brain"),
    ]
    return [c for c in candidates if os.path.isdir(c)]


def is_user_conversation(transcript_path):
    """Return True if transcript belongs to a main user chat rather than an isolated subagent."""
    try:
        with open(transcript_path, "r", encoding="utf-8", errors="replace") as f:
            first_line = f.readline()
            if not first_line:
                return False
            first_obj = json.loads(first_line)
            return (
                first_obj.get("source") == "USER_EXPLICIT"
                or first_obj.get("type") == "USER_INPUT"
            )
    except Exception:
        return False


def find_active_conversation_dir(conv_id=None):
    """Find conversation directory by ID or by latest main user conversation modification time."""
    brain_dirs = get_brain_dirs()
    if not brain_dirs:
        return None

    if conv_id:
        for bdir in brain_dirs:
            target = os.path.join(bdir, conv_id)
            if os.path.isdir(target):
                return target
            # Support prefix matching (e.g. first 8 chars of UUID)
            for d in os.listdir(bdir):
                if d.startswith(conv_id):
                    candidate = os.path.join(bdir, d)
                    if os.path.isdir(candidate):
                        return candidate

    user_entries = []
    all_entries = []
    for bdir in brain_dirs:
        for d in os.listdir(bdir):
            full_p = os.path.join(bdir, d)
            transcript_p = os.path.join(full_p, ".system_generated", "logs", "transcript.jsonl")
            if os.path.isdir(full_p) and not d.startswith(".") and os.path.isfile(transcript_p):
                mtime = os.path.getmtime(transcript_p)
                all_entries.append((mtime, full_p))
                if is_user_conversation(transcript_p):
                    user_entries.append((mtime, full_p))

    if user_entries:
        return max(user_entries, key=lambda x: x[0])[1]
    if all_entries:
        return max(all_entries, key=lambda x: x[0])[1]
    return None


def analyze_transcript(conv_dir):
    """Parse transcript.jsonl and extract compaction and window pressure metrics."""
    transcript_path = os.path.join(conv_dir, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.isfile(transcript_path):
        return None

    total_steps = 0
    user_inputs = 0
    subagents_spawned = 0
    compaction_checkpoints = []

    with open(transcript_path, "r", encoding="utf-8", errors="replace") as f:
        for step_num, line in enumerate(f, 1):
            total_steps = step_num
            try:
                data = json.loads(line)
            except Exception:
                continue

            msg_type = data.get("type", "")
            source = data.get("source", "")
            content = str(data.get("content", ""))

            if msg_type == "USER_INPUT" and source == "USER_EXPLICIT":
                user_inputs += 1

            # Strict checkpoint detection: never trigger on GENERIC tool outputs or subagent quotes
            is_checkpoint = msg_type == "CHECKPOINT" or (
                source == "SYSTEM"
                and msg_type != "SYSTEM_MESSAGE"
                and content.lstrip().startswith("# Resuming from a compaction")
            )
            if is_checkpoint:
                compaction_checkpoints.append(step_num)

            if msg_type == "PLANNER_RESPONSE":
                for tc in data.get("tool_calls", []) or []:
                    if isinstance(tc, dict) and tc.get("name") == "invoke_subagent":
                        subagents_spawned += 1

    compaction_round = len(compaction_checkpoints)
    last_compaction_step = compaction_checkpoints[-1] if compaction_checkpoints else 0
    steps_since_compaction = (
        (total_steps - last_compaction_step) if compaction_checkpoints else total_steps
    )
    window_fill_pct = min(
        100, int(round((steps_since_compaction / float(ESTIMATED_STEPS_PER_COMPACTION)) * 100))
    )

    # 4-Tier Health Rubric (combining Cumulative Compaction Round + Active Window Pressure)
    if (
        compaction_round >= 3
        or (compaction_round == 2 and steps_since_compaction >= 120)
        or total_steps >= 450
    ):
        health = "CRITICAL"
        level_icon = "🔴"
        risk_desc = (
            f"Heavy cumulative compaction (Round {compaction_round}, {total_steps} total steps). "
            "High risk of early constraint drift and session timeouts."
        )
        recommendation = (
            "Strongly recommend starting a fresh conversation now. "
            "Run `/kickoffx` to verify doc sync and generate the prompt for the next session."
        )
        action = "START_NEW_CHAT"
    elif (
        compaction_round == 2
        or (compaction_round == 1 and steps_since_compaction >= 130)
        or total_steps >= 250
    ):
        health = "CAUTION"
        level_icon = "🟠"
        risk_desc = (
            f"Moderate memory pruning active (Round {compaction_round}, "
            f"{steps_since_compaction} steps since last compaction / ~{window_fill_pct}% active window load)."
        )
        recommendation = (
            "Safe to finish the current task, then wrap up the milestone and run `/kickoffx` "
            "before starting a new major phase."
        )
        action = "PREPARE_TRANSITION"
    elif compaction_round == 1 or steps_since_compaction >= 100 or total_steps >= 120:
        health = "NOMINAL"
        level_icon = "🟡"
        risk_desc = (
            f"Good context retention (Round {compaction_round}, "
            f"{steps_since_compaction} steps in active window / ~{window_fill_pct}% load)."
        )
        recommendation = "Safe for continued execution. Keep edits focused."
        action = "CONTINUE"
    else:
        health = "HEALTHY"
        level_icon = "🟢"
        risk_desc = (
            f"Optimal context capacity (Round 0, {steps_since_compaction} steps / "
            f"~{window_fill_pct}% active window load)."
        )
        recommendation = "Safe to continue in the current conversation."
        action = "CONTINUE"

    return {
        "conv_id": os.path.basename(conv_dir),
        "compaction_round": compaction_round,
        "checkpoint_steps": compaction_checkpoints,
        "total_steps": total_steps,
        "user_inputs": user_inputs,
        "subagents_spawned": subagents_spawned,
        "steps_since_compaction": steps_since_compaction,
        "window_fill_pct": window_fill_pct,
        "health": health,
        "level_icon": level_icon,
        "risk_desc": risk_desc,
        "recommendation": recommendation,
        "action": action,
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze Antigravity context compaction metrics")
    parser.add_argument(
        "--conv-id", type=str, default=None, help="Target conversation ID (full UUID or prefix)"
    )
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

    ckpt_list = (
        ", ".join(f"step {s}" for s in metrics["checkpoint_steps"])
        if metrics["checkpoint_steps"]
        else "none"
    )
    round_str = f"Round {metrics['compaction_round']} ({ckpt_list})"
    status_str = f"{metrics['level_icon']} {metrics['health']}"
    window_str = (
        f"{metrics['steps_since_compaction']} steps "
        f"(~{metrics['window_fill_pct']}% of ~{ESTIMATED_STEPS_PER_COMPACTION}-step window)"
    )

    print("\n### Context & Compaction Scorecard\n")
    print("| Metric | Value | Status |")
    print("|:---|:---|:---:|")
    print(f"| **Compaction Round** | {round_str} | {status_str} |")
    print(f"| **Steps Since Last Compaction** | {window_str} | — |")
    print(f"| **Total Session Steps** | {metrics['total_steps']} steps | — |")
    sub_str = f"{metrics['user_inputs']} prompts • {metrics['subagents_spawned']} subagents"
    print(f"| **User Prompts / Subagents** | {sub_str} | — |")
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
