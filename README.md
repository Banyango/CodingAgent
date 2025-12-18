# Coding Agent

A small assistant service that uses a local Ollama model/ Gemini API for chat and function-calling tools.

This README explains how to install dependencies, use the included `Makefile`, and set up Ollama with the model used by this project (`gpt-oss:20b`).

## Requirements

- Python 3.12+
- pip (or a Python package manager that can read `pyproject.toml`)
- Ollama (local model runtime) — see the instructions below
- uv >= 0.7.20

## Install dependencies

This project uses `pyproject.toml`. You can install dependencies with `uv`.

```bash
uv install
```

## Makefile

This repo includes a `Makefile` to simplify common tasks. Typical targets you may find useful:

- `make format` — format code with `black`
- `make test` — run the test suite
- `make lint` — run linters/type checkers

(If your environment is WSL, run `make` from the WSL shell.)

## Setting up Ollama

Ollama is used as a local LLM runtime. This project expects an Ollama daemon listening on `http://localhost:11434` and uses the `gpt-oss:20b` model by default.

### Install Ollama with docker

``bash
docker run --rm -it -p 11434:11434 ollama/ollama

### Pull the model
docker exec -it <container_id> ollama pull gpt-oss:20b

### Start the Ollama daemon
docker exec -it <container_id> ollama serve

### Verify Ollama is running
curl http://localhost:11434/v1/models
``

The project is configured to use `gpt-oss:20b`. If you prefer a different model, update the Ollama model setting in `src/libs/chat/ollama/client.py` or provide a configuration for `OllamaAISettings`.

## Using Gemini API

This project also includes a Google Gemini integration (`src/libs/chat/gemini`). Use the Gemini API when you prefer a cloud-hosted LLM instead of a local Ollama model.

What this adds:
- A `GeminiAISettings` configuration (env prefix `GEMINI_`) used by the Gemini adapter.
- An async Gemini client that expects an API key and a model name.

Quick steps to enable Gemini:


1. Set the required environment variables (the `GeminiAISettings` class reads env vars with the `GEMINI_` prefix):

```bash
export GEMINI_API_KEY="your_gemini_api_key"
export GEMINI_MODEL="gemini-2.5-flash"  # or your preferred Gemini model
```

Notes on configuration and customization:
- The `GeminiAISettings` pydantic settings are defined in `src/libs/chat/gemini/config.py` and include defaults. The class uses `model_config = {"env_prefix": "GEMINI_"}` so environment variables like `GEMINI_API_KEY` and `GEMINI_MODEL` will be picked up automatically.
- The DI container used by this project (wireup) will provide the Gemini client/adapter when requested by services. If you want to programmatically override settings, update or provide a different `GeminiAISettings` instance to the container.

## Using the env template

This repository includes a small `env-template` file at the project root to help you set up required environment variables (for example `GEMINI_API_KEY`). Copy it to a local `.env` file and edit the values for your environment.

Quick steps:

```bash
# from project root
cp env-template .env
# open and edit
${EDITOR:-nano} .env
```

## Running the app

Assuming dependencies are installed and Ollama is running with `gpt-oss:20b`:

```bash
# from the project root
uv run src/main.py
```

## Tests

Run tests with:

```bash
make test
```

## Pre-commit

Please ensure to run before commiting code:

1. `make format` to format code before committing.
2. `make lint` to check for linting issues.
3. `make test` to ensure all tests pass.