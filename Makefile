.PHONY: test lint coverage

install:
	uv pip install -e .[test]

test:
	pytest --cov=hexlet_code tests/ -v

lint:
	ruff check hexlet_code tests
	ruff format --check hexlet_code tests

coverage:
	pytest --cov=hexlet_code --cov-report=term-missing tests/ -v