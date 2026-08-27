[CmdletBinding()]
param(
    [ValidateSet("User", "Repo")]
    [string]$Scope = "User",

    [string]$RepoPath = (Get-Location).Path,

    [switch]$Force
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir
$Source = Join-Path $RootDir "skills\sota-first"

if (-not (Test-Path (Join-Path $Source "SKILL.md"))) {
    throw "Could not find the source skill at $Source"
}

if ($Scope -eq "User") {
    $Target = Join-Path $HOME ".agents\skills\sota-first"
} else {
    $ResolvedRepo = (Resolve-Path $RepoPath).Path
    $Target = Join-Path $ResolvedRepo ".agents\skills\sota-first"
}

if (Test-Path $Target) {
    if (-not $Force) {
        throw "Target already exists: $Target. Re-run with -Force to replace it."
    }
    Remove-Item -Recurse -Force $Target
}

$Parent = Split-Path -Parent $Target
New-Item -ItemType Directory -Force -Path $Parent | Out-Null
Copy-Item -Recurse -Force $Source $Target

Write-Host "Installed sota-first to $Target"
Write-Host "Restart Codex if the skill does not appear automatically."
