.PHONY: venv start-health lint test

venv:
	python -m venv .venv
	. .venv/bin/activate && pip install -r backend/requirements-dev.txt

start-health:
	python backend/app/health.py

lint:
	pre-commit run --all-files

test:
	pytest -q
