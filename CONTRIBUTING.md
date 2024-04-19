# How to contribute to `validators`

Hi, to start, you need the following installed on your system.

1. [Git](https://git-scm.com/)
2. [Python](https://www.python.org/) v3.8 or later and
3. [PDM](https://pdm-project.org/en/stable/) for easy dependency management.
4. (Optional/Recommended) NodeJS for type checking.
5. (Optional/Recommended) [mise](https://github.com/jdx/mise) to manage multiple versions of Python, NodeJS etc.


First [fork](https://github.com/python-validators/validators/fork) this repository. Then clone it to your system. Then install development dependencies.


```sh
# cloning repository
$ git clone "https://github.com/YOUR_USERNAME/validators.git"
# changing directory 
$ cd validators
# installing development dependencies
$ pdm install
```

Activate the virtual environment and run `tox` to verify test cases.

```sh
# activate virtual environment
$ . ./.venv/bin/activate # replace `/bin/` with `/Scripts/` if you're on Windows.
# run tox for linting, type checking, formatting etc.
$ tox
```

Create a git branch. You can now make changes to the source code. If needed, test your change by running `pytest`. Commit, push and create a pull request.

If you're in doubt feel free to start a discussion [here](https://github.com/python-validators/validators/discussions). Thanks for taking interest in this library.
