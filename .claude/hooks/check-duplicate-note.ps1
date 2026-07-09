$ErrorActionPreference = "Stop"

try {
    $payloadText = [Console]::In.ReadToEnd()
    if ([string]::IsNullOrWhiteSpace($payloadText)) {
        exit 0
    }
    $payload = $payloadText | ConvertFrom-Json
} catch {
    exit 0
}

if ($payload.tool_name -ne "Write") {
    exit 0
}

$filePath = $payload.tool_input.file_path
if ([string]::IsNullOrWhiteSpace($filePath)) {
    exit 0
}

$projectDir = $env:CLAUDE_PROJECT_DIR
if ([string]::IsNullOrWhiteSpace($projectDir)) {
    $projectDir = (Get-Location).Path
}

if ([System.IO.Path]::IsPathRooted($filePath)) {
    $absPath = [System.IO.Path]::GetFullPath($filePath)
} else {
    $absPath = [System.IO.Path]::GetFullPath((Join-Path $projectDir $filePath))
}

$projectFull = [System.IO.Path]::GetFullPath($projectDir).TrimEnd('\', '/')
if (-not $absPath.StartsWith($projectFull, [System.StringComparison]::OrdinalIgnoreCase)) {
    exit 0
}
$relPath = $absPath.Substring($projectFull.Length).TrimStart('\', '/').Replace('\', '/')
$watchedDirs = @("01-Grammar", "02-Dictionary/Words")

$isWatched = $false
foreach ($dir in $watchedDirs) {
    if ($relPath.StartsWith($dir, [System.StringComparison]::OrdinalIgnoreCase)) {
        $isWatched = $true
        break
    }
}

if (-not $isWatched) {
    exit 0
}

if (Test-Path -LiteralPath $absPath) {
    exit 0
}

function Normalize-NoteName([string]$name) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($name).ToLowerInvariant()
    return ($base -replace '\d+$', '').Trim()
}

$targetDir = [System.IO.Path]::GetDirectoryName($absPath)
if (-not (Test-Path -LiteralPath $targetDir -PathType Container)) {
    exit 0
}

$targetName = [System.IO.Path]::GetFileName($relPath)
$targetNorm = Normalize-NoteName $targetName
if ([string]::IsNullOrWhiteSpace($targetNorm)) {
    exit 0
}

foreach ($existing in Get-ChildItem -LiteralPath $targetDir -Filter "*.md" -File) {
    if ((Normalize-NoteName $existing.Name) -eq $targetNorm) {
        $response = @{
            hookSpecificOutput = @{
                hookEventName = "PreToolUse"
                permissionDecision = "deny"
                additionalContext = "Blocked: '$targetName' looks like a near-duplicate of existing note '$($existing.Name)' in the same folder. Edit '$($existing.Name)' instead, or choose a clearer non-colliding name if this is a different concept."
            }
        }
        $response | ConvertTo-Json -Depth 5 -Compress
        exit 2
    }
}

exit 0
