#!/bin/pwsh

$ErrorActionPreference = "Stop"

# Cleanup directories
$venv_dir = "./.venv.dev"
$directories = @($venv_dir, "./build", "./dist")
foreach ($dir in $directories) {
    if (Test-Path $dir -PathType Container) {
        Remove-Item $dir -Recurse -Force
    }
}

# Generate the man page, then build `sdist` and `bdist`.
# Runs in a throwaway environment containing the package (non-editable), its
# optional extras and the locked `docs-offline` dependencies. `uv build` is called
# by the export script.
$env:UV_PROJECT_ENVIRONMENT = $venv_dir
try {
    uv run --locked --no-editable --group docs-offline --extra crypto-eth-addresses python package/export pkg
    if ($LASTEXITCODE -ne 0) { throw "package/export pkg failed" }
}
finally {
    Remove-Item Env:UV_PROJECT_ENVIRONMENT -ErrorAction SilentlyContinue
}
