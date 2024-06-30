#!/bin/pwsh

$ErrorActionPreference = "Stop"

# Check if CI environment variable is set to "false"
if ($null -eq $env:CI || "false" -eq $env:CI) {
    # tooling
    pdm export --group tooling,crypto-eth-addresses -f requirements -o package/requirements.tooling.txt
    # testing
    pdm export --group testing,crypto-eth-addresses -f requirements -o package/requirements.testing.txt
    # mkdocs
    pdm export --group docs-online -f requirements -o package/requirements.mkdocs.txt
    # sphinx
    pdm export --group docs-offline -f requirements -o package/requirements.sphinx.txt
    
    # create environment variable
    $env:CI = "true";
}

# Cleanup directories
$venv_dir = "./.venv.dev"
$directories = @($venv_dir, "./build", "./dist")
foreach ($dir in $directories) {
    if (Test-Path $dir -PathType Container) {
        Remove-Item $dir -Recurse -Force
    }
}

# Create venv
python -m venv $venv_dir


$bin_path = "Scripts"
if ($IsLinux || $IsMacOS) {
    $bin_path = "bin"
}

# Upgrade pip
& $venv_dir\$bin_path\python -m pip install --upgrade pip

# Install the current package
& $venv_dir\$bin_path\pip install .

# Install sphinx requirements
& $venv_dir\$bin_path\pip install -r package/requirements.sphinx.txt

# Install build tool
& $venv_dir\$bin_path\pip install build

# Activate virtual environment
. $venv_dir\$bin_path\Activate.ps1

# Run export script
python package/export pkg

# Deactivate virtual environment
deactivate

# delete environment variable
$env:CI = "";
