# ci-check.ps1 - project check entry (shared by local and CI; see .github/workflows/ci.yml)
# Purpose: idempotent, repeatable lint / build / test entry.
# The template ships only a basic whitespace check; replace/extend with real checks.
# Usage: powershell -File scripts/ci-check.ps1 (PowerShell 7: pwsh -File ...)
# Exit code: 0 pass; non-zero fail (CI and pre-release both rely on this).
# NOTE: this script is intentionally ASCII-only so it parses identically under
#       Windows PowerShell 5.1 (ANSI) and PowerShell 7 (UTF-8).

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host '==> ci-check: basic check (git whitespace errors)'
git diff --check
if ($LASTEXITCODE -ne 0) {
    Write-Error 'whitespace check failed (unstaged).'
    exit 1
}
git diff --cached --check
if ($LASTEXITCODE -ne 0) {
    Write-Error 'whitespace check failed (staged).'
    exit 1
}

Write-Host '==> ci-check: TODO - implement lint / build / test for this project'
Write-Host '    Node example: npm ci; npm run build; npm test'
Write-Host '    Python example: python -m pytest'
Write-Host '    Rust example: cargo check --all-targets; cargo test'
Write-Host '    After changing this file, update the check table in private/dev/TEST-REPORT.md.'

Write-Host '==> ci-check: passed (template placeholder)'
exit 0
