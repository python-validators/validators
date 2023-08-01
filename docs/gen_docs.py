"""Generate docs."""
# -*- coding: utf-8 -*-

# standard
from ast import ImportFrom, parse
from os.path import getsize
from pathlib import Path
from shutil import copy, move, rmtree
from subprocess import run  # nosec
from typing import Dict, List

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
    # external
    from yaml import safe_dump, safe_load

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
    mkdocs_build = run(("mkdocs", "build"), capture_output=True)  # nosec
    print(mkdocs_build.stderr.decode() + mkdocs_build.stdout.decode())
    # restore mkdocs config
    move(str(source / "mkdocs.bak.yaml"), source / "mkdocs.yaml")
    return mkdocs_build.returncode


def _gen_rst_docs(source: Path, refs_path: Path, only_web: bool = False, only_man: bool = False):
    """Generate reStructuredText docs."""
    # external
    from pypandoc import convert_file  # type: ignore

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
    rc = 0
    if not only_man:
        # build sphinx web pages as subprocess
        web_build = run(("sphinx-build", "docs", "docs/_build/web"), capture_output=True)  # nosec
        print(web_build.stderr.decode() + web_build.stdout.decode())
        rc = web_build.returncode
    if not only_web:
        # build sphinx man pages as subprocess
        man_build = run(  # nosec
            ("sphinx-build", "-b", "man", "docs", "docs/_build/man"), capture_output=True
        )
        print(man_build.stderr.decode() + man_build.stdout.decode())
        copy(source / "docs/_build/man/validators.1", source / "docs/validators.1")
        print(f"Man page copied to: {source / 'docs/validators.1'}")
        rc = man_build.returncode if rc == 0 else rc
    return rc


def generate_documentation(
    source: Path,
    only_md: bool = False,
    only_rst_web: bool = False,
    only_rst_man: bool = False,
    discard_refs: bool = True,
):
    """Generate documentation."""
    if only_md and only_rst_web and only_rst_man:
        return
    # copy readme as docs index file
    copy(source / "README.md", source / "docs/index.md")
    # clean destination
    refs_path = source / "docs/reference"
    if refs_path.exists() and refs_path.is_dir():
        rmtree(refs_path)
    refs_path.mkdir(exist_ok=True)
    rc = 0 if (only_rst_web or only_rst_man) else _gen_md_docs(source, refs_path)
    if not only_md:
        rc = _gen_rst_docs(source, refs_path, only_rst_web, only_rst_man) if rc == 0 else rc
    # optionally discard reference folder
    if discard_refs:
        rmtree(source / "docs/reference")
    return rc


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent

    # # standard
    # from sys import argv

    rc = generate_documentation(
        project_root,
        only_md=True,
        only_rst_web=False,
        only_rst_man=False,
        # # NOTE: use
        # discard_refs=len(argv) <= 1 or argv[1] != "--keep",
        # # instead of
        discard_refs=True,
        # # for debugging
    )
    quit(rc)

# TODO: Address all '# nosec'
