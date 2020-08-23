lint:
	isort --diff validators tests
	isort --check-only validators tests

	flake8 validators tests

install:
	pip install -e ".[test]"

test:
	py.test --doctest-glob="*.rst" --doctest-modules --ignore=setup.py
