.PHONY: test lint

test:
	python -m pytest --cov=hexlet_code --cov-report=term-missing -v

lint:
	ruff check hexlet_code tests
	ruff format --check hexlet_code tests