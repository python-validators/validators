"""Generate docs."""
# -*- coding: utf-8 -*-

# standard
from shutil import rmtree, move, copy
from ast import parse, ImportFrom
from typing import List, Dict
from os.path import getsize
from subprocess import run
from pathlib import Path

# external
from yaml import safe_load, safe_dump

__all__ = ("generate_documentation",)


def _write_ref_content(source: Path, module_name: str, func_name: str):
    """Write content."""
    with open(source, "at") as ref:
        ref.write(
            (f"# {module_name}\n\n" if getsize(source) == 0 else "")
            + f"::: validators.{module_name}.{func_name}\n"
        )


def _generate_reference(source: Path, destination: Path):
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


def _update_mkdocs_config(source: Path, destination: Path, nav_items: Dict[str, List[str]]):
    """Temporary update to mkdocs config."""
    copy(source, destination)
    with open(source, "rt") as mkf:
        mkdocs_conf = safe_load(mkf)
    mkdocs_conf["nav"] += [nav_items]
    with open(source, "wt") as mkf:
        safe_dump(mkdocs_conf, mkf, sort_keys=False)


def generate_documentation(source: Path, discard_refs: bool = True):
    """Generate documentation."""
    # copy readme as docs index file
    copy(source / "README.md", source / "docs/index.md")
    # generate reference documentation
    nav_items = _generate_reference(source / "validators/__init__.py", source / "docs/reference")
    # backup mkdocs config
    _update_mkdocs_config(source / "mkdocs.yml", source / "mkdocs.bak.yml", nav_items)
    # build docs as subprocess
    print(run(("mkdocs", "build"), capture_output=True).stderr.decode())
    # restore mkdocs config
    move(str(source / "mkdocs.bak.yml"), source / "mkdocs.yml")
    # optionally discard reference folder
    if discard_refs:
        rmtree(source / "docs/reference")


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent
    generate_documentation(project_root)
    # NOTE: use following lines only for testing/debugging
    # generate_documentation(project_root, discard_refs=False)
    # from sys import argv
    # generate_documentation(project_root, len(argv) > 1 and argv[1] == "--keep")
