# pre-release-check.ps1 - pre-release checks (markdown-driven, script-assisted)
# Usage: powershell -File scripts/pre-release-check.ps1 [-Version X.Y.Z] [-Description "desc"] [-SkipSubGit]
#        (PowerShell 7: pwsh -File ...)
# Behavior:
#   1) private sub-git: if it has changes -> auto add + commit
#      ("docs: private vX.Y.Z - desc") and confirm it is clean
#      (required before every release; see root AGENTS.md release flow);
#   2) main repo status: list uncommitted changes (agent commits them, not this script);
#   3) version consistency: VERSION vs top of CHANGELOG;
#   4) print audit & release reminders.
# Exit code: 0 all ready; 1 issues must be fixed first.
# NOTE: this script is intentionally ASCII-only so it parses identically under
#       Windows PowerShell 5.1 (ANSI) and PowerShell 7 (UTF-8).

param(
    [string]$Version = '',
    [string]$Description = '',
    [switch]$SkipSubGit
)

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$fail = $false

Write-Host '========== pre-release check =========='

# --- 0. environment ---
if (-not (Test-Path '.git')) {
    Write-Error 'Not inside a git repo root (no .git). Run from the repo root.'
    exit 1
}

# --- 1. VERSION ---
if (-not (Test-Path 'VERSION')) {
    Write-Error 'VERSION file missing.'
    exit 1
}
$version = (Get-Content 'VERSION' -Raw -Encoding UTF8).Trim()
if ($Version -ne '' -and $Version -ne $version) {
    Write-Warning "Argument Version($Version) differs from VERSION file ($version); using file value."
}
Write-Host "[1/4] current version: v$version"

# --- 2. private sub-git sync (required before release) ---
if (-not $SkipSubGit) {
    if (Test-Path 'private/.git') {
        $status = git -C private status --short 2>$null
        if ($LASTEXITCODE -ne 0) {
            Write-Warning 'Could not read private sub-git status; skipping auto commit.'
        }
        elseif ($status) {
            Write-Host '==> private sub-git has changes; auto committing:'
            $status | ForEach-Object { Write-Host "    $_" }
            $msg = "docs: private v$version - $Description"
            if ($Description -eq '') { $msg = "docs: private v$version - pre-release sync" }
            git -C private add -A -- .
            git -C private commit -m $msg
            if ($LASTEXITCODE -ne 0) {
                Write-Error 'private sub-git commit failed; fix manually.'
                exit 1
            }
            Write-Host "==> committed: $msg"
        }
        else {
            Write-Host '==> private sub-git clean.'
        }
        $status2 = git -C private status --short
        if ($status2) {
            Write-Error 'private sub-git still dirty; fix manually.'
            $fail = $true
        }
    }
    else {
        Write-Warning 'private/ is not a git repo (sub-git not initialized).'
    }
}
else {
    Write-Host '[2/4] private sub-git sync skipped (-SkipSubGit).'
}

# --- 3. main repo status ---
Write-Host '[3/4] main repo status:'
$mainStatus = git status --short
if ($mainStatus) {
    Write-Host '    uncommitted changes (commit before release):'
    $mainStatus | ForEach-Object { Write-Host "    $_" }
    Write-Warning 'Main repo has uncommitted changes. Confirm no private/ or secret files, then commit.'
}
else {
    Write-Host '    clean.'
}
# Safety scan: untracked/staged content must not contain private/ or common secret names
$scan = git status --short | Where-Object { $_ -match '^\?\?.*private/' -or $_ -match '(\.env|\.key|\.pem|secret)' }
if ($scan) {
    Write-Error 'Suspicious content in main repo status (private/ or secret files):'
    $scan | ForEach-Object { Write-Host "    $_" }
    $fail = $true
}

# --- 4. version consistency (VERSION vs CHANGELOG top) ---
$changelog = 'private/dev/CHANGELOG.md'
if (Test-Path $changelog) {
    $top = Get-Content $changelog -Encoding UTF8 | Select-String -Pattern '^## v' | Select-Object -First 1
    if ($top -and $top.Line -notmatch [regex]::Escape("v$version")) {
        Write-Warning "CHANGELOG top ($($top.Line)) does not match VERSION (v$version)."
        $fail = $true
    }
    else {
        Write-Host "[4/4] CHANGELOG top matches VERSION: v$version"
    }
}
else {
    Write-Warning "Missing $changelog (must be updated before release)."
    $fail = $true
}

# --- audit & release reminders ---
Write-Host '========== reminders =========='
Write-Host '1. auto-audit: check docs/audit-checklist.md; prefer an independent sub-agent to review git diff.'
Write-Host '2. docs ready: CHANGELOG / DESIGN / TEST-REPORT / README / root AGENTS.md / private/AGENTS.md.'
Write-Host '3. checks & tests passed and recorded in private/dev/TEST-REPORT.md (no pass, no release).'
Write-Host '4. commit format: feat:/fix:/docs:/chore: v<version> - description'
Write-Host '5. release: git tag v<version> + git push origin v<version> + gh release create (or CI auto).'

if ($fail) {
    Write-Error 'Issues must be fixed before release.'
    exit 1
}
Write-Host '========== check passed, ready to release =========='
exit 0
