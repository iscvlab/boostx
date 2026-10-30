# BoostX Composable Agent Skills Installer (Windows PowerShell)
# Copies the 13-skill BoostX (/x*) suite into host skill roots that exist on this machine.

param(
    [switch]$Antigravity,
    [switch]$Claude,
    [switch]$Grok,
    [switch]$Agents,
    [switch]$All,
    [string]$Workspace = ""
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $PSScriptRoot
$SkillsSrc = Join-Path $ScriptDir "skills"

$LegacyDirs = @(
    "boostx", "briefx", "contextx", "create-skillx", "deep-researchx",
    "kickoffx", "layax", "obsidianx", "planx", "publishx-audit",
    "publishx-qgis", "researchx", "syncx", "ultrax",
    "brief", "create-skill", "deep-research", "publish-audit", "publish-qgis", "update-doc"
)

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  ⚡ BoostX Agent Skills (v3.2.0) - Windows Installer" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Source: $SkillsSrc"

function Install-Skills([string]$TargetDir, [string]$PlatformName) {
    if (-not (Test-Path $TargetDir)) {
        New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
    }
    Write-Host "`nInstalling into $PlatformName ($TargetDir)..." -ForegroundColor Yellow

    foreach ($oldName in $LegacyDirs) {
        $oldPath = Join-Path $TargetDir $oldName
        if (Test-Path $oldPath) {
            Remove-Item $oldPath -Recurse -Force
            Write-Host "  - Removed legacy /$oldName" -ForegroundColor DarkGray
        }
    }

    Get-ChildItem -Directory $SkillsSrc | ForEach-Object {
        $skillName = $_.Name
        $dest = Join-Path $TargetDir $skillName

        if (Test-Path $dest) {
            Remove-Item $dest -Recurse -Force
        }

        # Copy as real directory to prevent nested junction recursion limits
        Copy-Item $_.FullName $dest -Recurse -Force
        Write-Host "  ✓ Installed /$skillName" -ForegroundColor Green
    }
}

$noHostFlag = -not $Antigravity.IsPresent -and -not $Claude.IsPresent -and -not $Grok.IsPresent -and -not $Agents.IsPresent -and [string]::IsNullOrEmpty($Workspace)

$geminiDir = Join-Path $env:USERPROFILE ".gemini\config\skills"
if ($Antigravity.IsPresent -or $All.IsPresent -or ($noHostFlag -and (Test-Path (Join-Path $env:USERPROFILE ".gemini")))) {
    Install-Skills $geminiDir "Gemini / Antigravity"
}

$claudeDir = Join-Path $env:USERPROFILE ".claude\skills"
if ($Claude.IsPresent -or $All.IsPresent -or ($noHostFlag -and (Test-Path (Join-Path $env:USERPROFILE ".claude")))) {
    Install-Skills $claudeDir "Claude Code"
}

$grokHome = if ($env:GROK_HOME) { $env:GROK_HOME } else { Join-Path $env:USERPROFILE ".grok" }
$grokDir = Join-Path $grokHome "skills"
if ($Grok.IsPresent -or $All.IsPresent -or ($noHostFlag -and (Test-Path $grokHome))) {
    Install-Skills $grokDir "Grok"
}

$agentsDir = Join-Path $env:USERPROFILE ".agents\skills"
if ($Agents.IsPresent -or $All.IsPresent -or ($noHostFlag -and (Test-Path (Join-Path $env:USERPROFILE ".agents")))) {
    Install-Skills $agentsDir "Cursor / Codex / Windsurf (.agents)"
}

if (-not [string]::IsNullOrEmpty($Workspace) -and (Test-Path $Workspace)) {
    Install-Skills (Join-Path $Workspace ".agents\skills") "Workspace .agents ($Workspace)"
    $wsGrok = Join-Path $Workspace ".grok\skills"
    if (Test-Path (Join-Path $Workspace ".grok") -or $Grok.IsPresent) {
        Install-Skills $wsGrok "Workspace .grok ($Workspace)"
    }
}

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "  ✓ BoostX v3.2.0 Installation Complete! All 13 /x* skills ready." -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
