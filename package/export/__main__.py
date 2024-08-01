"""Generate docs."""

# standard
from ast import ImportFrom, parse
from os import getenv
from os.path import getsize
from pathlib import Path
from shutil import copy
from subprocess import Popen  # nosec


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
                (
                    f"{module_name}\n{len(module_name) * '-'}\n\n"
                    + f".. module:: validators.{module_name}\n"
                    if getsize(source) == 0
                    else ""
                )
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


def _gen_md_docs(source: Path, refs_path: Path):
    """Generate Markdown docs."""
    # remove existing markdown files
    for md_files in (source / "docs/api").glob("*.md"):
        md_files.unlink()
    # generate md reference documentation
    for module_name, aliases in _parse_package(source / "src/validators/__init__.py"):
        for alias in aliases:
            _write_ref_content(refs_path / f"{module_name}.md", module_name, alias.name)
    # build mkdocs as subprocess
    mkdocs_build = Popen(("mkdocs", "build"))  # nosec
    mkdocs_build.communicate()
    return mkdocs_build.returncode


def _gen_rst_docs(source: Path, refs_path: Path, only_web: bool = False, only_man: bool = False):
    """Generate reStructuredText docs."""
    # external
    from pypandoc import convert_file  # type: ignore

    # remove existing rST files
    for rst_files in (source / "docs/api").glob("*.rst"):
        rst_files.unlink()

    with open(source / "docs/index.rst", "wt") as idx_f:
        idx_f.write(
            convert_file(source_file=source / "docs/index.md", format="md", to="rst").replace(
                "\r\n", "\n"  # remove carriage return in windows
            )
            + "\n\n.. toctree::"
            + "\n   :hidden:"
            + "\n   :maxdepth: 2"
            + "\n   :caption: Quick Start:"
            + "\n   :glob:\n"
            + "\n   install_config_use"
            + "\n\n.. toctree::"
            + "\n   :hidden:"
            + "\n   :maxdepth: 2"
            + "\n   :caption: API Reference:"
            + "\n   :glob:\n"
            + "\n   api/*\n"
        )

    with open(source / "docs/install_config_use.rst", "wt") as iau_f:
        iau_f.write(
            convert_file(source_file=source / "docs/install_config_use.md", format="md", to="rst")
            .replace("\r\n", "\n")  # remove carriage return in windows
            .replace("’", "'")
        )

    # generate rST reference documentation
    for module_name, aliases in _parse_package(source / "src/validators/__init__.py"):
        for alias in aliases:
            _write_ref_content(refs_path / f"{module_name}.rst", module_name, alias.name)
    exit_code = 0
    if not only_man:
        # build sphinx web pages as subprocess
        web_build = Popen(("sphinx-build", "docs", "docs/_build/web"), shell=False)  # nosec
        web_build.communicate()
        exit_code = web_build.returncode
        print("Run `python -m http.server -d docs/_build/web` to preview.")
    if not only_web:
        # build sphinx man pages as subprocess
        man_build = Popen(  # nosec
            ("sphinx-build", "-b", "man", "docs", "docs/_build/man"), shell=False
        )
        man_build.communicate()
        copy(source / "docs/_build/man/validators.1", source / "docs/validators.1")
        print(f"Man page copied to: {source / 'docs/validators.1'}")
        exit_code = man_build.returncode if exit_code == 0 else exit_code
    return exit_code


def _generate_documentation(
    source: Path,
    only_md: bool = False,
    only_rst_web: bool = False,
    only_rst_man: bool = False,
):
    """Generate documentation."""
    if only_md is only_rst_web is only_rst_man is True:
        return
    if only_md is only_rst_web is only_rst_man is False:
        return
    # copy readme as docs index file
    copy(source / "README.md", source / "docs/index.md")
    # clean destination
    refs_path = source / "docs/api"
    # if refs_path.is_dir():
    #     rmtree(refs_path)
    refs_path.mkdir(exist_ok=True)
    exit_code = 0 if (only_rst_web or only_rst_man) else _gen_md_docs(source, refs_path)
    if not only_md:
        exit_code = (
            _gen_rst_docs(source, refs_path, only_rst_web, only_rst_man)
            if exit_code == 0
            else exit_code
        )
    return exit_code


def package(source: Path):
    """Package the source code."""
    _generate_documentation(source, only_rst_man=True)
    if getenv("CI", "false") == "true":
        process = Popen(("./.venv/bin/python", "-m", "build"), shell=False)  # nosec
    else:
        process = Popen(("pdm", "build"), shell=False)  # nosec
    process.communicate()
    return process.returncode


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent.parent
    exit_code = 0

    # standard
    from sys import argv

    if len(argv) != 2:
        print("Expected one of these augments: `pkg` `doc` `man` or `web`")
        quit(1)

    if argv[1] == "pkg":
        exit_code = package(project_root)
    elif argv[1] == "doc":
        exit_code = _generate_documentation(project_root, only_md=True)
    elif argv[1] == "man":
        exit_code = _generate_documentation(project_root, only_rst_man=True)
    elif argv[1] == "web":
        exit_code = _generate_documentation(project_root, only_rst_web=True)
    quit(exit_code)

# TODO: Address all '# nosec'
