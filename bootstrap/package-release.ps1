[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Version
)

$ErrorActionPreference = 'Stop'

$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$distDir = Join-Path $repoRoot 'dist'
$stageRoot = Join-Path $distDir '_stage'
$repoStage = Join-Path $stageRoot "sdd-guardian-$Version"
$skillStage = Join-Path $stageRoot "sdd-guardian-skill-$Version"

$fullZip = Join-Path $distDir "sdd-guardian-$Version.zip"
$skillZip = Join-Path $distDir "sdd-guardian-skill-$Version.zip"

function Reset-Dir {
    param([string]$PathToReset)

    if (Test-Path -LiteralPath $PathToReset) {
        Remove-Item -LiteralPath $PathToReset -Recurse -Force
    }

    New-Item -ItemType Directory -Force -Path $PathToReset | Out-Null
}

function Safe-RemoveFile {
    param([string]$PathToRemove)

    if (Test-Path -LiteralPath $PathToRemove) {
        Remove-Item -LiteralPath $PathToRemove -Force
    }
}

Reset-Dir $stageRoot
New-Item -ItemType Directory -Force -Path $distDir | Out-Null
Reset-Dir $repoStage
Reset-Dir $skillStage

$itemsToCopy = @(
    '.github',
    'assets',
    'bootstrap',
    'codex',
    'docs',
    'skill',
    '.gitignore',
    'CODE_OF_CONDUCT.md',
    'CONTRIBUTING.md',
    'LICENSE',
    'PROJECT.md',
    'README.md',
    'SECURITY.md',
    'STATE.md'
)

foreach ($item in $itemsToCopy) {
    $source = Join-Path $repoRoot $item
    if (Test-Path -LiteralPath $source) {
        Copy-Item -LiteralPath $source -Destination $repoStage -Recurse -Force
    }
}

Copy-Item -LiteralPath (Join-Path $repoRoot 'skill\sdd-guardian') -Destination $skillStage -Recurse -Force

Safe-RemoveFile $fullZip
Safe-RemoveFile $skillZip

Compress-Archive -Path (Join-Path $repoStage '*') -DestinationPath $fullZip -CompressionLevel Optimal
Compress-Archive -Path (Join-Path $skillStage '*') -DestinationPath $skillZip -CompressionLevel Optimal

if (Test-Path -LiteralPath $stageRoot) {
    Remove-Item -LiteralPath $stageRoot -Recurse -Force
}

Get-ChildItem -LiteralPath $distDir -Filter '*.zip' | Select-Object Name,Length
