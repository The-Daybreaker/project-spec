# bump-version.ps1 - bump project version (VERSION file is the single source of truth)
# Usage: powershell -File scripts/bump-version.ps1 [-Part patch|minor|major] [-VersionFile VERSION]
#        (PowerShell 7: pwsh -File scripts/bump-version.ps1 ...)
# Behavior: read VERSION (X.Y.Z), bump by Part, write back (UTF-8 no BOM);
#           best-effort sync of version fields in package.json / Cargo.toml if present
#           (sync failure only warns, never aborts).
# Exit code: 0 success; 1 failure.
# NOTE: this script is intentionally ASCII-only so it parses identically under
#       Windows PowerShell 5.1 (ANSI) and PowerShell 7 (UTF-8).

param(
    [ValidateSet('patch', 'minor', 'major')]
    [string]$Part = 'patch',
    [string]$VersionFile = 'VERSION'
)

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

function Set-Utf8NoBom {
    param([string]$Path, [string]$Content)
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

if (-not (Test-Path $VersionFile)) {
    Write-Error "Version file not found: $VersionFile (run from repo root)"
    exit 1
}

$old = (Get-Content $VersionFile -Raw).Trim()
if ($old -notmatch '^(\d+)\.(\d+)\.(\d+)$') {
    Write-Error "Invalid VERSION format: '$old' (expected X.Y.Z)"
    exit 1
}

$maj = [int]$Matches[1]; $min = [int]$Matches[2]; $pat = [int]$Matches[3]
switch ($Part) {
    'major' { $maj++; $min = 0; $pat = 0 }
    'minor' { $min++; $pat = 0 }
    default { $pat++ }
}
$new = "$maj.$min.$pat"
Set-Utf8NoBom -Path $VersionFile -Content $new
Write-Host "==> VERSION: $old -> $new"

# Best-effort sync of common version files (failure only warns)
$syncTargets = @(
    @{ Path = 'package.json'; Pattern = '"version"\s*:\s*"[^"]+"'; Replace = '"version": "' + $new + '"' },
    @{ Path = 'Cargo.toml'; Pattern = '(?m)^version\s*=\s*"[^"]+"'; Replace = 'version = "' + $new + '"' },
    @{ Path = 'src-tauri/Cargo.toml'; Pattern = '(?m)^version\s*=\s*"[^"]+"'; Replace = 'version = "' + $new + '"' },
    @{ Path = 'src-tauri/tauri.conf.json'; Pattern = '"version"\s*:\s*"[^"]+"'; Replace = '"version": "' + $new + '"' }
)
foreach ($t in $syncTargets) {
    if (Test-Path $t.Path) {
        try {
            $content = Get-Content $t.Path -Raw
            if ($content -match $t.Pattern) {
                $updated = [regex]::Replace($content, $t.Pattern, $t.Replace)
                Set-Utf8NoBom -Path $t.Path -Content $updated
                Write-Host "==> synced $($t.Path) -> $new"
            }
        }
        catch {
            Write-Warning "sync $($t.Path) failed (VERSION unchanged): $($_.Exception.Message)"
        }
    }
}

Write-Host "==> done. Update the top entry of private/dev/CHANGELOG.md."
exit 0
