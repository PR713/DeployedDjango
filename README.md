# FlashCard Workshop
[![GitLab](https://img.shields.io/badge/GitLab-Project-blue)](https://gitlab.deployed.pl/dpld/flashcard-workshop-backend)



## Prerequisites

- [uv](https://docs.astral.sh/uv/) for dependency management
- [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) (optional)

## Bootstrap
You can either use database in `docker compose` or locally installed one.
For the specific approach refer to the corresponding section.

### With the local database

If you want to go with the local database you can make use of the `make bootstrap`
command to install all dependencies and setup the database. For the exact steps
refer to the [Makefile](./Makefile).

### Docker way

If you prefer to use docker then just run:
```bash
make bootstrap-docker
```

Then, you can manage containers with `docker compose`.

### Pre-commit hooks

They are installed as a part of the `make bootstrap*` commands, but if you want to install them again
for some reason, then run:

```bash
uv pre-commit install --install-hooks
```

## Usage

The project ships with a default user `admin:admin321!` in [fixtures](./fixtures/accounts.customuser.yaml)

### Installing dependencies

For managing dependencies, we use [uv](https://docs.astral.sh/uv/).

To install all dependencies, run:
```bash
uv sync
```

To add a new dependency:
```bash
uv add [--group <group>] <package>
```

### Applying migrations

To apply migrations, run:
```bash
uv run python manage.py migrate
```
or
```bash
make migrate
```

### Loading fixtures
```shell
uv run python manage.py loaddata fixtures/*.yaml
```
or
```bash
make load-fixtures
```

### Running the server
```bash
uv run python manage.py runserver
```
or just
```bash
make
```
