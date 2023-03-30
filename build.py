"""Remove Refs."""

# standard
from subprocess import run
from shutil import rmtree
from pathlib import Path

# local
from docs.gen_docs import generate_documentation

if __name__ == "__main__":
    project_dir = Path(__file__).parent
    generate_documentation(project_dir, only_md=True, discard_refs=False)
    process = run(("poetry", "build"), capture_output=True)
    print(process.stderr.decode() + process.stdout.decode())
    rmtree(project_dir / "docs/reference", ignore_errors=True)
