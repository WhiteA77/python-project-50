
install:
	uv sync

run:
	uv run gendiff -h

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

lint:
	uv run ruff check gendiff tests --fix
	uv run ruff format --check gendiff tests

check: test lint

build:
	uv build

package-install:
	uv tool install dist/*.whl

.PHONY: install run test test-coverage lint check build package-install