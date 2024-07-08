# Contributing to `validators`

Hi, to start, you need the following installed on your system.

1. [Git](https://git-scm.com)
2. [Python](https://www.python.org) v3.8 or later
3. [PDM](https://pdm-project.org) for easy dependency management
4. (Optional/Recommended) [`NodeJS`](https://nodejs.org/en) for type checking
5. (Optional/Recommended) [`mise`](https://github.com/jdx/mise) to manage multiple versions of Python, NodeJS and other such tools.

First [fork this repository](https://github.com/python-validators/validators/fork). (If you are or intend to be a collaborator, uncheck "fork only `master`", because for versioned docs you'll need `gh-pages` branch too.) Clone it to your system and install the development dependencies.

```sh
# clone repository
$ git clone "https://github.com/YOUR-USERNAME/validators.git"
# change directory 
$ cd validators
# install development dependencies
$ pdm install
```

Activate the virtual environment and run `tox` to verify test cases.

```sh
# activate virtual environment
$ . ./.venv/bin/activate # replace `/bin/` with `/Scripts/` if you're on Windows.
# run tox for linting, type checking, formatting etc.
$ tox
```

Create a git branch and make changes to the source code. If needed, test your changes by running `pytest`. Execute `tox` to format, lint and type-check your code before committing. Commit, push and create a pull request. If you're in doubt, feel free to start a discussion [here](https://github.com/python-validators/validators/discussions).

## Documentation

> Documentation is extracted from the source code. Please follow [Google's Python Doc Style](https://google.github.io/styleguide/pyguide.html).

If you're adding/removing a module, you must update the `nav` key in `mkdocs.yml`.
Then export documentation as follows:

```sh
$ . ./.venv/bin/activate
# generate documentation
$ python package/export TYPE # where TYPE is any of `doc`, `man` or `web`.

# doc - generates docs found here: https://yozachar.github.io/pyvalidators
# man - generates sphinx based manpages
# web - generates sphinx based web docs
```

You can preview the generated documentation:

```sh
$ . ./.venv/bin/activate
# To preview mkdocs
$ mkdocs serve
# To preview man pages
$ man docs/_build/man/validators.1
# To preview sphinx webpages
$ python -m http.server -d docs/_build/web
```

## Versioning, Packaging & Releasing (for collaborators)

> You must be familiar with [semantic versioning](https://semver.org) and [Python packaging](https://packaging.python.org).

### Tagging

1. Take a look at [`CHANGES.md`](CHANGES.md). They are generated with [GitHub's releaser](https://github.com/python-validators/validators/releases/new), and then modified to fit the shown style.
2. Update the [changelog](CHANGES.md). Version number must be updated in both [`SECURITY.md`](SECURITY.md) and [`src/validators/__init__.py`](src/validators/__init__.py).
3. The final merge commit on the upstream (i.e. this repo) is tagged.

    ```sh
    # syncing with upstream
    $ git pull upstream master
    $ git push
    # tagging that final merge commit before release
    $ GIT_COMMITTER_DATE=$(git log -n1 --pretty=%aD) git tag -a -m "vMAJOR.MINOR.PATCH" MAJOR.MINOR.PATCH
    # pushing tag to remote
    $ git push --tag
    $ git push upstream --tag
    ```

### Versioned documentation

1. To preview versioned docs, run `mike serve` (`mike` is a dev dependency).
2. Then (look at <https://yozachar.github.io/pyvalidators/stable/>)
    - to publish stable docs run `mike deploy -p -u VERSION stable` after checking out to a stable tag name like `0.28.3` (note: document `VERSION = 0.29 if tag_name == 0.29.1`).
    - to publish bleeding-edge docs run `mike deploy -p -u dev master` after checking out to the `master` branch.
3. This will deploy docs to the `gh-pages` branch (see: <https://github.com/python-validators/validators/tree/gh-pages/>)

### Packaging and releasing

1. Run `./package/roll.sh` (or `./package/roll.ps1`) to generate both `sdist` and `bdist`.
2. Install [`twine`](https://pypi.org/project/twine) using [`pipx`](https://pipx.pypa.io) to upload package to PyPI.

    ```sh
    # publishing
    $ twine check dist/*
    $ twine upload dist/*
    ```

3. Create a GitHub release with the contents from the [changelog](CHANGES.md). Upload the wheel from `dist/` along with the shasum file generated with:

    ```sh
    # generate sha256sum
    $ sha256sum dist/validators-VERSION-py3-none-any.whl > dist/validators-VERSION-py3-none-any.whl.sha256
    ```

---

Thank your for taking interest in this library!
