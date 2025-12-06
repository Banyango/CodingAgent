# Makefile to run ruff and pyright (prefers uv if available)
RUN := export PYTHONPATH=src && uv run

# Default pytest args (can be overridden when calling make, e.g. `make pytest PYTEST_ARGS="-k test_name"`)
PYTEST_ARGS ?= tests/unit

.PHONY: lint typecheck check install-dev pytest test

format:
	$(RUN) ruff format

lint:
	$(RUN) ruff check . --fix
	$(RUN) pyright src tests

check: lint typecheck

install-dev:
ifeq ($(UV),)
	@echo "uv not found; please install ruff and pyright in your PATH or install uv."
else
	uv install --with dev
endif

create-migration:
	$(RUN) alembic revision --autogenerate -m "$(msg)"

apply-migrations:
	$(RUN) alembic upgrade head

down-migrations:
	$(RUN) alembic downgrade -1

# Run the test suite using pytest. You can pass extra args via PYTEST_ARGS, e.g.:
#   make pytest PYTEST_ARGS="-k test_name -q"
pytest:
	$(RUN) pytest $(PYTEST_ARGS)

# Alias
test: pytest
