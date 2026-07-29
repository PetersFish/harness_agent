# harness_agent

Multi-framework agent learning workspace.

## Structure

- `smolagent/` — smolagents learning subproject (Ollama Cloud, ToolCallingAgent, CodeAgent)
- `deepagents/` — (planned) DeepAgents learning subproject

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Run

```bash
# ToolCallingAgent demo
uv run --package smolagent python -m smolagent.tool_calling_agent_demo

# CodeAgent demo
uv run --package smolagent python -m smolagent.code_agent_demo

# tests
uv run pytest

# notebook
uv run jupyter lab
```

## Environment

Copy `smolagent/.env.example` to `smolagent/.env` and fill in your Ollama Cloud API key.
