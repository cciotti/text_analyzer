SHELL := /usr/bin/env bash
TESTS := tests/
DOCKER_TAG := "text_analyzer"

PYTHON_PATH ?= $(PWD)

clean: ## Clean the cruft
	@find . -name .pytest_cache | xargs rm -fr
	@find . -name __pycache__ | xargs rm -fr
	@find . -name .coverage | xargs rm -fr

wicked-clean: ## Remove all packages
	@pip freeze | xargs pip uninstall -y > /dev/null 2>&1 || true

deps: clean ## Install all dependencies
	@pip install -r requirements-dev.txt -r requirements.txt

black: ## Run the formatter
	@black -l 120 .

test: clean ## Run the tests
	@python -m pytest $(TESTS)

coverage: ## Get a coverage report
	@python -m pytest --cov . --cov-config .coveragerc --cov-report term-missing $(TESTS)

sample: ## See a demo
	@cat tests/test_data.txt | python main.py samples/*.txt

docker: ## Build the Docker image
	@docker build -t $(DOCKER_TAG) .

