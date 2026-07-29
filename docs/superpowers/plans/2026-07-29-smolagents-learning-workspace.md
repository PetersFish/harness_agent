# Smolagents Learning Workspace Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Set up a `uv` workspace rooted at `harness_agent/` with an independent `smolagent/` learning subproject that runs a `ToolCallingAgent` against the Ollama Cloud API using a safe local tool.

**Architecture:** `harness_agent/` is a `uv` workspace root declaring member subprojects. `smolagent/` is the first member: a standalone `uv` project with its own `pyproject.toml`, `.env`, `src/`, and `tests/`. The Agent uses `smolagents[openai]`'s `OpenAIModel` to reach the OpenAI-compatible Ollama Cloud endpoint at `https://ollama.com/v1` with model `ollama-cloud/glm-5.2`. A `ToolCallingAgent` registers one deterministic, side-effect-free local tool (Fibonacci number) for learning tool selection and invocation. DeepAgents will later live as a sibling member at `harness_agent/deepagents/`.

**Tech Stack:** Python 3.11, uv workspace, smolagents[openai], python-dotenv, pytest, ipykernel, jupyterlab.

---

## File Structure

```
harness_agent/
  pyproject.toml                    # workspace root; members only, no runtime deps
  uv.lock                           # single shared lockfile (generated)
  .gitignore                        # excludes .env, .venv/, __pycache__, Jupyter caches
  README.md                         # learning roadmap and per-framework entry points
  docs/superpowers/plans/           # this plan

  smolagent/
    pyproject.toml                  # member project; smolagents[openai], python-dotenv
    .env.example                    # OLLAMA_API_KEY, OLLAMA_MODEL, OLLAMA_BASE_URL
    .env                            # gitignored; user fills in real key
    src/smolagent/
      __init__.py
      settings.py                   # loads + validates env vars; no secrets in code
      tools.py                       # @tool fibonacci_number; pure local computation
      quick_start.py                 # builds OpenAIModel + ToolCallingAgent, runs a task
    tests/
      __init__.py
      test_tools.py                 # deterministic tests for fibonacci_number
      test_settings.py              # validation logic tests (no real API calls)
    quick_start.ipynb               # learning notebook: env check, tool demo, agent demo
```

---

### Task 1: Initialize uv workspace root

**Files:**
- Create: `harness_agent/pyproject.toml`
- Create: `harness_agent/.gitignore`
- Create: `harness_agent/README.md`

- [ ] **Step 1: Create workspace root pyproject.toml**

Create `harness_agent/pyproject.toml`:

```toml
[project]
name = "harness-agent"
version = "0.1.0"
description = "Multi-framework agent learning workspace (smolagents, deepagents, ...)"
requires-python = ">=3.11"
dependencies = []

[tool.uv.workspace]
members = ["smolagent", "deepagents"]

[tool.uv]
dev-dependencies = []
```

Note: `deepagents` member does not exist yet; uv will warn but not fail when running commands scoped to `smolagent`. Once `deepagents/` is added later, it will be picked up automatically. If `uv sync` at the root complains about the missing member, create a placeholder `deepagents/pyproject.toml` later in this plan's sibling work.

- [ ] **Step 2: Create root .gitignore**

Create `harness_agent/.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
.eggs/
build/
dist/

# Virtual environments
.venv/

# Environment files
.env

# Jupyter
.ipynb_checkpoints/

# uv
# uv.lock is committed for reproducibility

# OS
.DS_Store
```

- [ ] **Step 3: Create root README.md**

Create `harness_agent/README.md`:

```markdown
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
```

- [ ] **Step 4: Commit workspace root**

```bash
cd /Users/yuping/Documents/workspace/harness_agent
git init
git add pyproject.toml .gitignore README.md docs/
git commit -m "chore: initialize uv workspace root"
```

---

### Task 2: Initialize smolagent member project

**Files:**
- Create: `harness_agent/smolagent/pyproject.toml`
- Create: `harness_agent/smolagent/.env.example`
- Create: `harness_agent/smolagent/src/smolagent/__init__.py`
- Create: `harness_agent/smolagent/tests/__init__.py`

- [ ] **Step 1: Create member pyproject.toml**

Create `harness_agent/smolagent/pyproject.toml`:

```toml
[project]
name = "smolagent"
version = "0.1.0"
description = "smolagents learning subproject"
requires-python = ">=3.11"
dependencies = [
    "smolagents[openai]",
    "python-dotenv",
]

[dependency-groups]
dev = [
    "pytest",
    "ipykernel",
    "jupyterlab",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/smolagent"]
```

- [ ] **Step 2: Create .env.example**

Create `harness_agent/smolagent/.env.example`:

```dotenv
# Ollama Cloud (OpenAI-compatible)
OLLAMA_API_KEY=your-ollama-cloud-api-key
OLLAMA_MODEL=ollama-cloud/glm-5.2
OLLAMA_BASE_URL=https://ollama.com/v1
```

- [ ] **Step 3: Create package init**

Create `harness_agent/smolagent/src/smolagent/__init__.py`:

```python
"""smolagents learning subproject."""
```

- [ ] **Step 4: Create tests init**

Create `harness_agent/smolagent/tests/__init__.py`:

```python
```

- [ ] **Step 5: Create placeholder deepagents member to keep workspace valid**

Because the root workspace declares `deepagents` as a member, create a minimal placeholder so `uv sync` at the root does not fail. This will be replaced when the DeepAgents learning subproject is actually built.

Create `harness_agent/deepagents/pyproject.toml`:

```toml
[project]
name = "deepagents-demo"
version = "0.0.0"
description = "DeepAgents learning subproject (placeholder)"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/deepagents_demo"]
```

Create `harness_agent/deepagents/src/deepagents_demo/__init__.py`:

```python
"""DeepAgents learning subproject (placeholder)."""
```

- [ ] **Step 6: Sync and verify workspace**

Run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
uv sync
```

Expected: resolves and installs both members; `.venv/` created at root.

- [ ] **Step 7: Commit member project**

```bash
git add smolagent/ deepagents/ uv.lock
git commit -m "chore: add smolagent member project and deepagents placeholder"
```

---

### Task 3: Settings module (TDD)

**Files:**
- Create: `harness_agent/smolagent/tests/test_settings.py`
- Create: `harness_agent/smolagent/src/smolagent/settings.py`

- [ ] **Step 1: Write failing tests for settings validation**

Create `harness_agent/smolagent/tests/test_settings.py`:

```python
import os
from unittest.mock import patch

import pytest


def test_load_settings_returns_configured_values():
    env = {
        "OLLAMA_API_KEY": "test-key",
        "OLLAMA_MODEL": "ollama-cloud/glm-5.2",
        "OLLAMA_BASE_URL": "https://ollama.com/v1",
    }
    with patch.dict(os.environ, env, clear=False):
        from smolagent.settings import load_settings

        settings = load_settings()
        assert settings.api_key == "test-key"
        assert settings.model_id == "ollama-cloud/glm-5.2"
        assert settings.base_url == "https://ollama.com/v1"


def test_load_settings_uses_default_base_url_when_absent():
    env = {
        "OLLAMA_API_KEY": "test-key",
        "OLLAMA_MODEL": "ollama-cloud/glm-5.2",
    }
    with patch.dict(os.environ, env, clear=False):
        # ensure OLLAMA_BASE_URL not set
        with patch.dict(os.environ, {"OLLAMA_BASE_URL": ""}, clear=False):
            os.environ.pop("OLLAMA_BASE_URL", None)
            from smolagent.settings import load_settings

            settings = load_settings()
            assert settings.base_url == "https://ollama.com/v1"


def test_load_settings_raises_when_api_key_missing():
    env = {
        "OLLAMA_MODEL": "ollama-cloud/glm-5.2",
    }
    with patch.dict(os.environ, env, clear=False):
        os.environ.pop("OLLAMA_API_KEY", None)
        with pytest.raises(ValueError, match="OLLAMA_API_KEY"):
            from smolagent.settings import load_settings

            load_settings()


def test_load_settings_raises_when_model_missing():
    env = {
        "OLLAMA_API_KEY": "test-key",
    }
    with patch.dict(os.environ, env, clear=False):
        os.environ.pop("OLLAMA_MODEL", None)
        with pytest.raises(ValueError, match="OLLAMA_MODEL"):
            from smolagent.settings import load_settings

            load_settings()
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
uv run pytest smolagent/tests/test_settings.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'smolagent.settings'`.

- [ ] **Step 3: Write settings implementation**

Create `harness_agent/smolagent/src/smolagent/settings.py`:

```python
"""Load and validate Ollama Cloud configuration from environment.

No secrets are hardcoded. The module loads from a local .env file (via
python-dotenv) and/or process environment variables. It raises clear
errors when required values are missing so failures surface at startup.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

DEFAULT_BASE_URL = "https://ollama.com/v1"


@dataclass(frozen=True)
class Settings:
    api_key: str
    model_id: str
    base_url: str


def load_settings() -> Settings:
    """Load Ollama Cloud settings, loading .env first.

    Raises:
        ValueError: if OLLAMA_API_KEY or OLLAMA_MODEL is missing.
    """
    load_dotenv()

    api_key = os.environ.get("OLLAMA_API_KEY", "").strip()
    model_id = os.environ.get("OLLAMA_MODEL", "").strip()
    base_url = os.environ.get("OLLAMA_BASE_URL", "").strip() or DEFAULT_BASE_URL

    if not api_key:
        raise ValueError(
            "OLLAMA_API_KEY is required. Copy smolagent/.env.example to "
            "smolagent/.env and fill in your Ollama Cloud API key."
        )
    if not model_id:
        raise ValueError(
            "OLLAMA_MODEL is required. Set it in smolagent/.env, e.g. "
            "OLLAMA_MODEL=ollama-cloud/glm-5.2"
        )

    return Settings(api_key=api_key, model_id=model_id, base_url=base_url)
```

- [ ] **Step 4: Run tests to verify they pass**

Run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
uv run pytest smolagent/tests/test_settings.py -v
```

Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add smolagent/src/smolagent/settings.py smolagent/tests/test_settings.py
git commit -m "feat(smolagent): add settings module with env validation"
```

---

### Task 4: Local tool (TDD)

**Files:**
- Create: `harness_agent/smolagent/tests/test_tools.py`
- Create: `harness_agent/smolagent/src/smolagent/tools.py`

- [ ] **Step 1: Write failing tests for fibonacci_number tool**

Create `harness_agent/smolagent/tests/test_tools.py`:

```python
import pytest

from smolagent.tools import fibonacci_number


def test_fibonacci_base_cases():
    assert fibonacci_number(0) == 0
    assert fibonacci_number(1) == 1


def test_fibonacci_small_indices():
    assert fibonacci_number(10) == 55
    assert fibonacci_number(20) == 6765


def test_fibonacci_negative_index_raises():
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci_number(-1)


def test_fibonacci_non_integer_raises():
    with pytest.raises(TypeError):
        fibonacci_number(1.5)
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
uv run pytest smolagent/tests/test_tools.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'smolagent.tools'`.

- [ ] **Step 3: Write tools implementation**

Create `harness_agent/smolagent/src/smolagent/tools.py`:

```python
"""Side-effect-free learning tools for smolagents.

These tools do not access the network, filesystem, or shell. They exist
to practice tool selection and parameter passing with a ToolCallingAgent.
"""

from __future__ import annotations

from smolagents import tool


@tool
def fibonacci_number(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed).

    Args:
        n: A non-negative integer index into the Fibonacci sequence.
            fibonacci_number(0) == 0, fibonacci_number(1) == 1.

    Returns:
        The n-th Fibonacci number.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

- [ ] **Step 4: Run tests to verify they pass**

Run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
uv run pytest smolagent/tests/test_tools.py -v
```

Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add smolagent/src/smolagent/tools.py smolagent/tests/test_tools.py
git commit -m "feat(smolagent): add fibonacci_number local tool"
```

---

### Task 5: Agent entry point

**Files:**
- Create: `harness_agent/smolagent/src/smolagent/quick_start.py`

- [ ] **Step 1: Write quick_start.py**

Create `harness_agent/smolagent/src/smolagent/quick_start.py`:

```python
"""Minimal smolagents quick start against Ollama Cloud.

Builds an OpenAIModel pointing at the OpenAI-compatible Ollama Cloud
endpoint, registers one local tool, and runs a ToolCallingAgent on a
task that should trigger a tool call.

Run manually (consumes API quota):
    uv run --package smolagent python -m smolagent.quick_start
"""

from __future__ import annotations

from smolagents import OpenAIModel, ToolCallingAgent

from smolagent.settings import load_settings
from smolagent.tools import fibonacci_number


def build_agent() -> ToolCallingAgent:
    settings = load_settings()
    model = OpenAIModel(
        model_id=settings.model_id,
        api_base=settings.base_url,
        api_key=settings.api_key,
    )
    return ToolCallingAgent(
        tools=[fibonacci_number],
        model=model,
    )


def main() -> None:
    agent = build_agent()
    task = "What is the 20th Fibonacci number? Use the fibonacci_number tool."
    result = agent.run(task)
    print(f"Task: {task}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verify it imports without error**

Run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
uv run python -c "from smolagent.quick_start import build_agent; print('import ok')"
```

Expected: prints `import ok` (does not call the API; build_agent is not invoked).

Note: Do not run `main()` in CI/tests — it consumes Ollama Cloud quota. It is a manual verification step for the learner.

- [ ] **Step 3: Commit**

```bash
git add smolagent/src/smolagent/quick_start.py
git commit -m "feat(smolagent): add quick_start agent entry point"
```

---

### Task 6: Learning notebook

**Files:**
- Modify: `harness_agent/smolagent/quick_start.ipynb` (currently empty)

- [ ] **Step 1: Replace notebook with learning cells**

Overwrite `harness_agent/smolagent/quick_start.ipynb` with a minimal notebook containing these cells:

Cell 1 (markdown):
```markdown
# smolagents Quick Start (Ollama Cloud)

Learning notebook for smolagents with a ToolCallingAgent against the
OpenAI-compatible Ollama Cloud endpoint.
```

Cell 2 (code):
```python
import smolagents

print(f"smolagents {smolagents.__version__}")
```

Cell 3 (markdown):
```markdown
## 1. Load configuration

Configuration is loaded from `smolagent/.env` via python-dotenv. The API
key is never printed.
```

Cell 4 (code):
```python
from smolagent.settings import load_settings

settings = load_settings()
print(f"model: {settings.model_id}")
print(f"base_url: {settings.base_url}")
print(f"api_key: {'***' if settings.api_key else 'MISSING'}")
```

Cell 5 (markdown):
```markdown
## 2. Try the local tool in isolation

The tool does not call any API. It is a pure function wrapped with
`@tool` so the agent can discover it.
```

Cell 6 (code):
```python
from smolagent.tools import fibonacci_number

print(fibonacci_number(10))
print(fibonacci_number(20))
```

Cell 7 (markdown):
```markdown
## 3. Run the ToolCallingAgent

This cell calls the Ollama Cloud API. It should ask the model to select
the `fibonacci_number` tool and call it.
```

Cell 8 (code):
```python
from smolagent.quick_start import build_agent

agent = build_agent()
result = agent.run("What is the 20th Fibonacci number? Use the fibonacci_number tool.")
print(result)
```

- [ ] **Step 2: Commit notebook**

```bash
git add smolagent/quick_start.ipynb
git commit -m "docs(smolagent): fill quick_start learning notebook"
```

---

### Task 7: Final verification

- [ ] **Step 1: Run full test suite**

Run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
uv run pytest -v
```

Expected: all tests pass (8 tests: 4 settings + 4 tools). No API calls made.

- [ ] **Step 2: Manual API smoke test**

Ensure `smolagent/.env` exists with a real `OLLAMA_API_KEY`. Then run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
uv run --package smolagent python -m smolagent.quick_start
```

Expected: the agent selects `fibonacci_number`, calls it with `n=20`, and prints `6765` (or a result containing it).

- [ ] **Step 3: Verify git status is clean**

Run:

```bash
cd /Users/yuping/Documents/workspace/harness_agent
git status
```

Expected: clean working tree; `uv.lock` committed; `.env` and `.venv/` ignored.