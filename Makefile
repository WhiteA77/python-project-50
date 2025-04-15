.PHONY: test lint coverage

setup:
	export PYTHONPATH=. && uv pip install --system -e .[test,dev]

install:
	uv pip install --system -e .[test,dev]

test:
	pytest --cov=hexlet_code tests/ -v

check:
	ruff check hexlet_code tests
	ruff format --check hexlet_code tests

coverage:
	pytest --cov=hexlet_code --cov-report=term-missing tests/ -v

test-coverage:
	pytest --cov=hexlet_code --cov-report=xml

debug:
	ls -l gendiff.py && python3 -c "import gendiff; print('OK')"

