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