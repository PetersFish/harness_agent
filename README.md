# harness_agent

Multi-framework agent learning workspace.

## Structure

- `smolagent/` — smolagents learning subproject (Ollama Cloud, ToolCallingAgent)
- `deepagents/` — (planned) DeepAgents learning subproject

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Run

```bash
# smolagents quick start
uv run --package smolagent python -m smolagent.quick_start

# tests
uv run pytest

# notebook
uv run jupyter lab
```

## Environment

Copy `smolagent/.env.example` to `smolagent/.env` and fill in your Ollama Cloud API key.