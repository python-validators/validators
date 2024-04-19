# How to contribute to `validators`

Hi, to start, you need the following installed on your system.

1. [Git](https://git-scm.com)
2. [Python](https://www.python.org) v3.8 or later
3. [PDM](https://pdm-project.org) for easy dependency management
4. (Optional/Recommended) NodeJS for type checking
5. (Optional/Recommended) [mise](https://github.com/jdx/mise) to manage multiple versions of Python & NodeJS.

First [fork this repository](https://github.com/python-validators/validators/fork). Clone it to your system. Install development dependencies.

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

1. Take a look at the [`CHANGES.md`](CHANGES.md). They are generated with [GitHub's releaser](https://github.com/python-validators/validators/releases/new), and then modified.
2. Update the changelog. Version number must be updated in both [`SECURITY.md`](SECURITY.md) and [`src/validators/__init__.py`](src/validators/__init__.py).
3. The final merge commit on the upstream (i.e. this repo) is tagged.

    ```sh
    # syncing with upstream
    $ git pull upstream master
    $ git push
    # tagging that final merge commit before release
    $ GIT_COMMITTER_DATE=$(git log -n1 --pretty=%aD) git tag -a -m "vMAJOR.MINOR.PATCH" vMAJOR.MINOR.PATCH
    # pushing tag to remote
    $ git push --tag
    $ git push upstream --tag
    ```

4. To update versioned docs, you must track the `gh-pages` onto a local branch. `git checkout --track upstream/gh-pages`, once.
5. Checkout to the tag you want to include in the versioned documentation `git checkout TAG_NAME`.
6. Then using [`mike`](https://github.com/jimporter/mike) (which is already a dev dependency) run `mike deploy -p -u VERSION stable`.
7. Or use `mike deploy -p -u dev master`, which will deploy docs in the CURRENT commit as the `latest` documentation.
8. Run `./package/roll.sh` (or `./package/roll.ps1`) to generate both sdist and bdist.
9. Install [`twine`](https://pypi.org/project/twine) using [`pipx`](https://pipx.pypa.io) to upload package to PyPI.

    ```sh
    # publishing
    $ twine check dist/*
    $ twine upload dist/*
    ```

10. Create a GitHub release with the contents from the [changelog](CHANGES.md). Upload the wheel from `dist/` along with the shasum file generated with:

    ```sh
    # generate sha256sum
    $ sha256sum dist/validators-VERSION-py3-none-any.whl > dist/validators-VERSION-py3-none-any.whl.sha256
    ```

Thanks for taking interest in this library!
