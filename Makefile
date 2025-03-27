COMMIT_SHA := $(shell git rev-parse HEAD)
BRANCH_NAME := $(shell git rev-parse --abbrev-ref HEAD)
TAGS := -t $(DOCKER_REGISTRY):$(COMMIT_SHA) -t $(DOCKER_REGISTRY):$(BRANCH_NAME)
MANAGE_PY := uv run python manage.py

.DEFAULT_GOAL := runserver

clean: clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/ .coverage coverage.xml htmlcov/ .pytest_cache

test: ## run tests quickly with the default Python
	uv run pytest flashcard_workshop

coverage: ## check code coverage quickly with the default Python
	uv run pytest --cov=flashcard_workshop flashcard_workshop
	uv run coverage report -m
	uv run coverage html
	xdg-open htmlcov/index.html

quality-check: autoformatters ## check quality of code
	uv run ruff check flashcard_workshop
	uv run dmypy run flashcard_workshop

autoformatters: ## runs auto formatters
	uv run ruff format flashcard_workshop

install_requirements:  ## install python requirements
	uv sync

install_pre_commit:  ## install pre-commit hooks
	uv run pre-commit install --install-hooks
	uv run pre-commit install -t commit-msg

psql_cmd := $(if $(POSTGRES_HOST),\
 psql -d "user=$(POSTGRES_USER) port=$(POSTGRES_PORT) password=$(POSTGRES_PASSWORD) host=$(POSTGRES_HOST)" ,\
 sudo -u postgres psql -U postgres) # if POSTGRES_HOST is set, use envvars, otherwise use default postgres user. Required for testing on CI
bootstrap: install_requirements install_pre_commit  ## bootstrap project
	cp .env.example .env
	sed -i 's/^POSTGRES_PORT=.*/POSTGRES_PORT=5432/' .env
	echo  "DO \$$\$$ BEGIN IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'flashcard_workshop') THEN\
 		   CREATE USER flashcard_workshop WITH CREATEDB PASSWORD 'flashcard_workshop'; END IF; END \$$\$$;\
 		   SELECT 'CREATE DATABASE \"flashcard_workshop\" OWNER \"flashcard_workshop\"'\
 		   WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'flashcard_workshop')\\gexec" | $(psql_cmd)
	$(MANAGE_PY) migrate
	[ -d fixtures ] && $(MANAGE_PY) loaddata $(wildcard fixtures/*.yaml) || exit 0

rebuild-db:  ## recreates database with fixtures
	echo yes | $(MANAGE_PY) reset_db
	$(MANAGE_PY) migrate
	$(MANAGE_PY) loaddata fixtures/*

bootstrap-docker: install_requirements install_pre_commit  ## bootstrap project in docker
	cp .env.example .env
	docker compose up -d --wait
	$(MANAGE_PY) migrate
	$(MANAGE_PY) loaddata fixtures/*.yaml

build-docker-ci: ## build docker image for CI
	docker build --push --ssh default --target ci -t docker.deployed.pl/dpld/flashcard-workshop-backend:ci .

migrate: ## run migrations
	$(MANAGE_PY) migrate

load-fixtures: ## load fixtures
	$(MANAGE_PY) loaddata fixtures/*.yaml

runserver: ## run server
	$(MANAGE_PY) runserver
