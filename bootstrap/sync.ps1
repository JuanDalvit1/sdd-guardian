[CmdletBinding()]
param(
    [string]$CodexHome,
    [switch]$SkipPull,
    [switch]$SkipValidation
)

$ErrorActionPreference = 'Stop'
$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))

if (-not $SkipPull) {
    if (Test-Path -LiteralPath (Join-Path $repoRoot '.git')) {
        git -C $repoRoot pull --ff-only
    } else {
        Write-Warning "No .git directory found at $repoRoot. Skipping git pull."
    }
}

$installScript = Join-Path $repoRoot 'bootstrap\install.ps1'
$params = @{
    CodexHome = $CodexHome
    SkipValidation = $SkipValidation
}

& $installScript @params

