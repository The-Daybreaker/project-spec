# sync-template.ps1 - mirror project-template/ into init-project/assets/project-template/
# Keep the two copies identical: project-template/ is the master (human-readable),
# init-project/assets/project-template/ is what the init-project skill ships.
# Run this after ANY change under project-template/ (or before packaging the skill).
# Usage: powershell -File sync-template.ps1

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$src = Join-Path $root 'project-template'
$dst = Join-Path $root 'init-project\assets\project-template'

if (-not (Test-Path $src)) {
    Write-Error "template source not found: $src"
    exit 1
}
if (-not (Test-Path (Join-Path $root 'init-project\SKILL.md'))) {
    Write-Error "skill folder not found under $root"
    exit 1
}
if (Test-Path $dst) {
    Remove-Item -Recurse -Force $dst
}
Copy-Item -Recurse $src $dst

$count = (Get-ChildItem -Recurse -File $dst).Count
Write-Host "synced $count files: $src -> $dst"
exit 0
