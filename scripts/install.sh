#!/usr/bin/env bash
# BoostX Composable Agent Skills (v3.2.0) - Universal Installer (macOS & Linux)
# Links the 14-skill BoostX (/x*) suite into Claude Code (~/.claude/skills), Grok (~/.grok/skills),
# Gemini/Antigravity (~/.gemini/config/skills), and Cursor/Codex (~/.agents/skills).

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$SCRIPT_DIR/skills"

LEGACY_DIRS=(
    "boostx" "briefx" "contextx" "create-skillx" "deep-researchx"
    "kickoffx" "layax" "obsidianx" "ocrx" "planx" "publishx-audit"
    "publishx-qgis" "researchx" "syncx" "ultrax" "unlimited-ocr"
    "brief" "create-skill" "deep-research" "ocr" "publish-audit" "publish-qgis" "update-doc"
)

echo "============================================================"
echo "  ⚡ BoostX Agent Skills (v3.2.0) - Universal Installer"
echo "============================================================"
echo "Source: $SKILLS_SRC"

install_to() {
    local target_dir="$1"
    local name="$2"

    mkdir -p "$target_dir"
    echo ""
    echo "Installing into $name ($target_dir)..."

    for old_name in "${LEGACY_DIRS[@]}"; do
        local old_dest="$target_dir/$old_name"
        if [ -L "$old_dest" ] || [ -d "$old_dest" ]; then
            rm -rf "$old_dest"
            echo "  - Removed legacy /$old_name"
        fi
    done

    for skill in "$SKILLS_SRC"/*; do
        if [ -d "$skill" ]; then
            local skill_name
            skill_name="$(basename "$skill")"
            local dest="$target_dir/$skill_name"

            if [ -L "$dest" ] || [ -d "$dest" ]; then
                rm -rf "$dest"
            fi
            ln -s "$skill" "$dest"
            echo "  ✓ Linked /$skill_name"
        fi
    done
}

NO_FLAG=false
if [ -z "$1" ]; then
    NO_FLAG=true
fi

# 1. Claude Code
if [ "$1" == "--claude" ] || [ "$1" == "--all" ] || { [ "$NO_FLAG" == true ] && [ -d "$HOME/.claude" ]; }; then
    install_to "$HOME/.claude/skills" "Claude Code"
fi

# 2. Gemini / Antigravity
if [ "$1" == "--antigravity" ] || [ "$1" == "--all" ] || { [ "$NO_FLAG" == true ] && [ -d "$HOME/.gemini" ]; }; then
    install_to "$HOME/.gemini/config/skills" "Gemini / Antigravity"
fi

# 3. Grok
GROK_ROOT="${GROK_HOME:-$HOME/.grok}"
if [ "$1" == "--grok" ] || [ "$1" == "--all" ] || { [ "$NO_FLAG" == true ] && [ -d "$GROK_ROOT" ]; }; then
    install_to "$GROK_ROOT/skills" "Grok"
fi

# 4. Cursor / Codex / Windsurf (~/.agents/skills)
if [ "$1" == "--agents" ] || [ "$1" == "--all" ] || { [ "$NO_FLAG" == true ] && [ -d "$HOME/.agents" ]; }; then
    install_to "$HOME/.agents/skills" "Cursor / Codex / Windsurf (.agents)"
fi

# 5. Target workspace if provided as $2
if [ -n "$2" ] && [ -d "$2" ]; then
    install_to "$2/.agents/skills" "Workspace .agents ($2)"
    if [ -d "$2/.grok" ] || [ "$1" == "--grok" ]; then
        install_to "$2/.grok/skills" "Workspace .grok ($2)"
    fi
fi

echo ""
echo "============================================================"
echo "  ✓ BoostX v3.2.0 Installation Complete! All 14 /x* skills ready."
echo "============================================================"
