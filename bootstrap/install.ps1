[CmdletBinding()]
param(
    [string]$CodexHome,
    [switch]$SkipValidation
)

$ErrorActionPreference = 'Stop'

function Resolve-CodexHome {
    param([string]$RequestedCodexHome)

    if ($RequestedCodexHome) {
        return [System.IO.Path]::GetFullPath($RequestedCodexHome)
    }

    if ($env:CODEX_HOME) {
        return [System.IO.Path]::GetFullPath($env:CODEX_HOME)
    }

    return [System.IO.Path]::GetFullPath((Join-Path $HOME '.codex'))
}

function Set-ManagedAgentsBlock {
    param(
        [string]$AgentsPath,
        [string]$SnippetPath
    )

    $startMarker = '<!-- sdd-guardian:start -->'
    $endMarker = '<!-- sdd-guardian:end -->'
    $snippet = Get-Content -Raw -LiteralPath $SnippetPath
    $managedBlock = @"
$startMarker
$snippet
$endMarker
"@.Trim()

    if (Test-Path -LiteralPath $AgentsPath) {
        $current = Get-Content -Raw -LiteralPath $AgentsPath
    } else {
        $current = ''
    }

    if ($current -match [regex]::Escape($startMarker) -and $current -match [regex]::Escape($endMarker)) {
        $pattern = '(?s)' + [regex]::Escape($startMarker) + '.*?' + [regex]::Escape($endMarker)
        $updated = [regex]::Replace($current, $pattern, $managedBlock)
    } elseif ([string]::IsNullOrWhiteSpace($current)) {
        $updated = $managedBlock + [Environment]::NewLine
    } else {
        $updated = $current.TrimEnd() + [Environment]::NewLine + [Environment]::NewLine + $managedBlock + [Environment]::NewLine
    }

    Set-Content -LiteralPath $AgentsPath -Value $updated -Encoding utf8
}

$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$resolvedCodexHome = Resolve-CodexHome -RequestedCodexHome $CodexHome
$skillsDir = Join-Path $resolvedCodexHome 'skills'
$targetSkillDir = Join-Path $skillsDir 'sdd-guardian'
$sourceSkillDir = Join-Path $repoRoot 'skill\sdd-guardian'
$agentsPath = Join-Path $resolvedCodexHome 'AGENTS.md'
$snippetPath = Join-Path $repoRoot 'codex\AGENTS.snippet.md'
$validatorPath = Join-Path $resolvedCodexHome 'skills\.system\skill-creator\scripts\quick_validate.py'

if (-not (Test-Path -LiteralPath $sourceSkillDir)) {
    throw "Skill source not found at $sourceSkillDir"
}

New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null

if (Test-Path -LiteralPath $targetSkillDir) {
    $resolvedTarget = [System.IO.Path]::GetFullPath($targetSkillDir)
    if (-not $resolvedTarget.StartsWith($skillsDir, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to overwrite unexpected target: $resolvedTarget"
    }

    Remove-Item -LiteralPath $targetSkillDir -Recurse -Force
}

Copy-Item -LiteralPath $sourceSkillDir -Destination $targetSkillDir -Recurse -Force
Set-ManagedAgentsBlock -AgentsPath $agentsPath -SnippetPath $snippetPath

if (-not $SkipValidation) {
    if (Test-Path -LiteralPath $validatorPath) {
        python $validatorPath $targetSkillDir
    } else {
        Write-Warning "Validator not found at $validatorPath. Skipping quick_validate.py."
    }
}

Write-Host "Installed sdd-guardian into $targetSkillDir"
Write-Host "Updated managed block in $agentsPath"
