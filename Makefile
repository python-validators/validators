.PHONY: clean
## Remove unneeded files
clean:
	find src -type d -name "__pycache__" -exec rm -rf {} + > /dev/null 2>&1
	find src -type f -name "*.pyc" -exec rm -rf {} + > /dev/null 2>&1

	find tests -type d -name "__pycache__" -exec rm -rf {} + > /dev/null 2>&1
	find tests -type f -name "*.pyc" -exec rm -rf {} + > /dev/null 2>&1

.PHONY: install
## Install this repo in develop mode
install:
	pip install -r requirements/ci.txt
	pip install -e .
	pre-commit install

.PHONY: test
## Run pytest
test:
	python -m pytest tests/