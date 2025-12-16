# bottymcbotbot

A small assistant service that uses a local Ollama model/ Gemini API for chat and function-calling tools.

This README explains how to install dependencies, use the included `Makefile`, and set up Ollama with the model used by this project (`gpt-oss:20b`).

## Requirements

- Python 3.12+
- pip (or a Python package manager that can read `pyproject.toml`)
- Ollama (local model runtime) — see the instructions below

## Install dependencies

This project uses `pyproject.toml`. You can install dependencies with pip, pipx, or a virtual environment.

Example using a virtual environment and pip:

```bash
python -m venv .venv
source .venv/bin/activate  # on WSL / Linux
python -m pip install --upgrade pip
pip install -e .
# Install test/dev dependencies
pip install -r <(python - <<'PY'
import tomllib, sys
p = tomllib.loads(open('pyproject.toml','rb').read())
reqs = []
for g in ('dev','test'):
    if f"dependency-groups" in p and g in p['dependency-groups']:
        reqs.extend(p['dependency-groups'][g])
print('\n'.join(reqs))
PY
)
```

Alternatively, install directly from `pyproject.toml` using `pip` (PEP 621+ support may vary):

```bash
pip install -r requirements.txt  # if you generate one, or
pip install .
```

Recommended minimal dependencies from `pyproject.toml`:

- fastapi
- uvicorn
- wireup
- ollama
- openai

## Makefile

This repo includes a `Makefile` to simplify common tasks. Typical targets you may find useful:

- `make run` — start the application (usually runs uvicorn)
- `make test` — run the test suite
- `make lint` — run linters/type checkers

To see available targets, run:

```bash
make help
```

(If your environment is WSL, run `make` from the WSL shell.)

## Setting up Ollama

Ollama is used as a local LLM runtime. This project expects an Ollama daemon listening on `http://localhost:11434` and uses the `gpt-oss:20b` model by default.

1. Install Ollama — follow instructions at https://ollama.com/. On Linux/WSL you can install via the provided package or using their installation script.

2. Start the Ollama daemon:

```bash
ollama daemon
```

3. Pull/download the model used by this project (example name):

```bash
ollama pull gpt-oss:20b
```

Confirm the model is available:

```bash
ollama list
```

The project is configured to use `gpt-oss:20b`. If you prefer a different model, update the Ollama model setting in `src/libs/chat/ollama/client.py` or provide a configuration for `OllamaAISettings`.

## Using Gemini API

This project also includes a Google Gemini integration (`src/libs/chat/gemini`). Use the Gemini API when you prefer a cloud-hosted LLM instead of a local Ollama model.

What this adds:
- A `GeminiAISettings` configuration (env prefix `GEMINI_`) used by the Gemini adapter.
- An async Gemini client that expects an API key and a model name.

Quick steps to enable Gemini:

1. Install the Google GenAI client library (the project expects imports from `google.genai`):

```bash
pip install google-genai
```

2. Set the required environment variables (the `GeminiAISettings` class reads env vars with the `GEMINI_` prefix):

```bash
export GEMINI_API_KEY="your_gemini_api_key"
export GEMINI_MODEL="gemini-2.5-flash"  # or your preferred Gemini model
```

You can set these in your shell, in a `.env` file (with a tool like direnv or python-dotenv), or via your process manager.

3. Run the app pointing to the Gemini config (environment variables are sufficient):

```bash
# from project root; environment variables must be set in the same session
GEMINI_API_KEY="$GEMINI_API_KEY" GEMINI_MODEL="$GEMINI_MODEL" uvicorn src.main:app --reload
```

Notes on configuration and customization:
- The `GeminiAISettings` pydantic settings are defined in `src/libs/chat/gemini/config.py` and include defaults. The class uses `model_config = {"env_prefix": "GEMINI_"}` so environment variables like `GEMINI_API_KEY` and `GEMINI_MODEL` will be picked up automatically.
- The DI container used by this project (wireup) will provide the Gemini client/adapter when requested by services. If you want to programmatically override settings, update or provide a different `GeminiAISettings` instance to the container.

Troubleshooting
- "Invalid API key" — ensure your `GEMINI_API_KEY` is correct and not expired. Keep the value secret.
- Network or permission errors — confirm your environment has network access to the Gemini API endpoints and any required Google Cloud permissions.
- Model errors — verify the model name in `GEMINI_MODEL` matches a model available to your account.
- Missing package/import errors — run `pip install google-genai` in the same interpreter/environment used to run the app.

Tests
- The repository includes tests for the Gemini adapter (see `tests/component/libs/chat/test_gemini_adapter.py` and `tests/unit/libs/chat/gemini/test_adapter.py`). Running `pytest -q` will exercise those integrations (some tests may mock the client).

Security
- Do not commit your API keys. Use environment variables or secrets managers.

## Using the env template

This repository includes a small `env-template` file at the project root to help you set up required environment variables (for example `GEMINI_API_KEY`). Copy it to a local `.env` file and edit the values for your environment.

Quick steps:

```bash
# from project root
cp env-template .env
# open and edit
${EDITOR:-nano} .env
```

Notes and best practices:
- The `.env` file often contains secrets (API keys). Do not commit it to source control. Ensure your `.gitignore` includes `.env` (add it if missing).
- You can load `.env` in your shell session with tools like `direnv` or by using `python-dotenv` in your application startup if needed.
- If you prefer, export the variables directly in your shell instead of using a `.env` file.

## Configuration

- Default Ollama base URL: `http://localhost:11434/`
- Default model: `gpt-oss:20b` (configured in `src/libs/chat/ollama/client.py` via `OllamaAISettings`)

You can override these values via the dependency injection container or by editing `src/libs/chat/ollama/client.py`.

## Running the app

Assuming dependencies are installed and Ollama is running with `gpt-oss:20b`:

```bash
# from the project root
uvicorn src.main:app --reload
```

or use the Makefile target (if provided):

```bash
make run
```

## Tests

Run tests with:

```bash
pytest -q
```

## Notes

- This project relies on local Ollama models. Ensure you have disk space and network access to pull models.
- The codebase uses `wireup` for dependency injection; configuration is done via service classes in `src/libs/chat/ollama/client.py`.
- If you encounter issues contacting the Ollama daemon, ensure it's running and that the `base_url` matches the daemon address.

If you'd like, I can:
- Add a `requirements.txt` or `dev-requirements.txt` generated from `pyproject.toml`.
- Add a small script `scripts/setup_ollama.sh` to automate pulling the model and starting the daemon.
- Add Makefile targets for `pull-model` and `start-ollama`.

Which would you like next?
