"""Generate docs."""
# -*- coding: utf-8 -*-

# standard
from shutil import rmtree, move, copy
from ast import parse, ImportFrom
from typing import List, Dict
from os.path import getsize
from subprocess import run
from pathlib import Path
from sys import argv

# external
from yaml import safe_load, safe_dump


def _write_ref_content(source: Path, module_name: str, func_name: str):
    """Write content."""
    with open(source, "at") as ref:
        ref.write(
            (f"# {module_name}\n\n" if getsize(source) == 0 else "")
            + f"::: validators.{module_name}.{func_name}\n"
        )


def generate_reference(source: Path, destination: Path):
    """Generate reference."""
    nav_items: Dict[str, List[str]] = {"Code Reference": []}
    # clean destination
    if destination.exists() and destination.is_dir():
        rmtree(destination)
    destination.mkdir(exist_ok=True)
    # parse source
    v_ast = parse(source.read_text(), source)
    # generate reference content
    for namespace in (node for node in v_ast.body if isinstance(node, ImportFrom)):
        if not namespace.module:
            continue
        for alias in namespace.names:
            ref_module = destination / f"{namespace.module}.md"
            _write_ref_content(ref_module, namespace.module, alias.name)
        nav_items["Code Reference"].append(f"reference/{namespace.module}.md")
    return nav_items


def update_mkdocs_config(source: Path, destination: Path, nav_items: Dict[str, List[str]]):
    """Temporary update to mkdocs config."""
    copy(source, destination)
    with open(source, "rt") as mkf:
        mkdocs_conf = safe_load(mkf)
    mkdocs_conf["nav"] += [nav_items]
    with open(source, "wt") as mkf:
        safe_dump(mkdocs_conf, mkf, sort_keys=False)


def generate_documentation(source: Path):
    """Generate documentation."""
    # copy readme as docs index file
    copy(source / "README.md", source / "docs/index.md")
    # generate reference documentation
    nav_items = generate_reference(source / "validators/__init__.py", source / "docs/reference")
    # backup mkdocs config
    update_mkdocs_config(source / "mkdocs.yml", source / "mkdocs.bak.yml", nav_items)
    # build docs as subprocess
    print(run(("mkdocs", "build"), capture_output=True).stderr.decode())
    # restore mkdocs config
    move(str(source / "mkdocs.bak.yml"), source / "mkdocs.yml")


if __name__ == "__main__":
    project_dir = Path(__file__).parent.parent
    generate_documentation(project_dir)
    # use this option before building package
    # with `poetry build` to include refs
    if len(argv) > 1 and argv[1] == "--keep":
        quit()
    rmtree(project_dir / "docs/reference")
