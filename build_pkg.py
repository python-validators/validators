"""Remove Refs."""

# standard
from subprocess import run

# from shutil import rmtree
from pathlib import Path

# local
from docs.gen_docs import generate_documentation

if __name__ == "__main__":
    project_dir = Path(__file__).parent
    generate_documentation(project_dir, only_rst_man=True)
    print()
    process = run(("poetry", "build"), capture_output=True)
    print(process.stderr.decode() + process.stdout.decode())
