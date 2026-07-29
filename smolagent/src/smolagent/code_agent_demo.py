"""Minimal CodeAgent demo against Ollama Cloud.

Builds an OpenAIModel pointing at the OpenAI-compatible Ollama Cloud
endpoint, registers one local tool, and runs a CodeAgent on a task that
should generate Python code to call that tool.

Run manually (consumes API quota):
    uv run --package smolagent python -m smolagent.code_agent_demo
"""

from __future__ import annotations

from smolagents import CodeAgent, OpenAIModel

from smolagent.settings import load_settings
from smolagent.tools import fibonacci_number


def build_agent() -> CodeAgent:
    settings = load_settings()
    model = OpenAIModel(
        model_id=settings.model_id,
        api_base=settings.base_url,
        api_key=settings.api_key,
    )
    return CodeAgent(
        tools=[fibonacci_number],
        model=model,
    )


def main() -> None:
    agent = build_agent()
    task = (
        "What is the 20th Fibonacci number? "
        "Write and execute Python code that calls the fibonacci_number tool."
    )
    result = agent.run(task)
    print(f"Task: {task}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
