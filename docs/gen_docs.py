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

__all__ = ("generate_documentation",)


def _write_ref_content(source: Path, module_name: str, func_name: str):
    """Write content."""
    with open(source, "at") as ref:
        ref.write(
            (
                (f"# {module_name}\n\n" if getsize(source) == 0 else "")
                + f"::: validators.{module_name}.{func_name}\n"
            )
            if f"{source}".endswith(".md")
            else (
                (f"{module_name}\n{len(module_name) * '-'}\n\n" if getsize(source) == 0 else "")
                + f".. module:: validators.{module_name}\n"
                + f".. autofunction:: {func_name}\n"
            )
        )


def _parse_package(source: Path):
    """Parse validators package."""
    v_ast = parse(source.read_text(), source)
    for namespace in (node for node in v_ast.body if isinstance(node, ImportFrom)):
        if not namespace.module:
            continue
        yield (namespace.module, namespace.names)


def _generate_reference(source: Path, destination: Path, ext: str):
    """Generate reference."""
    nav_items: Dict[str, List[str]] = {"Code Reference": []}
    # generate reference content
    for module_name, aliases in _parse_package(source):
        for alias in aliases:
            _write_ref_content(destination / f"{module_name}.{ext}", module_name, alias.name)
        if ext == "md":
            nav_items["Code Reference"].append(f"reference/{module_name}.md")
    return nav_items


def _update_mkdocs_config(source: Path, destination: Path, nav_items: Dict[str, List[str]]):
    """Temporary update to mkdocs config."""
    copy(source, destination)
    with open(source, "rt") as mkf:
        mkdocs_conf = safe_load(mkf)
    mkdocs_conf["nav"] += [nav_items]
    with open(source, "wt") as mkf:
        safe_dump(mkdocs_conf, mkf, sort_keys=False)


def _gen_md_docs(source: Path, refs_path: Path):
    """Generate Markdown docs."""
    nav_items = _generate_reference(source / "validators/__init__.py", refs_path, "md")
    # backup mkdocs config
    _update_mkdocs_config(source / "mkdocs.yaml", source / "mkdocs.bak.yaml", nav_items)
    # build mkdocs as subprocess
    print(run(("mkdocs", "build"), capture_output=True).stderr.decode())
    # restore mkdocs config
    move(str(source / "mkdocs.bak.yaml"), source / "mkdocs.yaml")


def _gen_rst_docs(source: Path, refs_path: Path):
    """Generate reStructuredText docs."""
    # external
    from pypandoc import convert_file  # type: ignore

    # generate index.rst
    with open(source / "docs/index.rst", "wt") as idx_f:
        idx_f.write(
            convert_file(source_file=source / "docs/index.md", format="md", to="rst")
            + "\n\n.. toctree::"
            + "\n   :hidden:"
            + "\n   :maxdepth: 2"
            + "\n   :caption: Reference:"
            + "\n   :glob:\n"
            + "\n   reference/*\n"
        )
    # generate RST reference documentation
    _generate_reference(source / "validators/__init__.py", refs_path, "rst")
    # build sphinx web pages as subprocess
    web_build = run(("sphinx-build", "docs", "docs/_build/web"), capture_output=True)
    print(web_build.stderr.decode(), "\n", web_build.stdout.decode(), sep="")
    # build sphinx man pages as subprocess
    man_build = run(("sphinx-build", "-b", "man", "docs", "docs/_build/man"), capture_output=True)
    print(man_build.stderr.decode(), "\n", man_build.stdout.decode(), sep="")


def generate_documentation(
    source: Path, only_md: bool = False, only_rst: bool = False, discard_refs: bool = True
):
    """Generate documentation."""
    if only_md and only_rst:
        return
    # copy readme as docs index file
    copy(source / "README.md", source / "docs/index.md")
    # clean destination
    refs_path = source / "docs/reference"
    if refs_path.exists() and refs_path.is_dir():
        rmtree(refs_path)
    refs_path.mkdir(exist_ok=True)
    # documentation for each kind
    if not only_rst:
        _gen_md_docs(source, refs_path)
    if not only_md:
        _gen_rst_docs(source, refs_path)
    # optionally discard reference folder
    if discard_refs:
        rmtree(source / "docs/reference")


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent
    generate_documentation(
        project_root,
        only_md=True,
        only_rst=False,
        discard_refs=len(argv) <= 1 or argv[1] != "--keep",
    )
