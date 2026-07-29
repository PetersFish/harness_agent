from __future__ import annotations

from types import SimpleNamespace

import smolagent.code_agent_demo as demo


def test_build_agent_uses_code_agent_with_shared_fibonacci_tool(monkeypatch) -> None:
    captured: dict[str, object] = {}

    class FakeModel:
        def __init__(self, **kwargs: object) -> None:
            captured["model_kwargs"] = kwargs
            captured["model"] = self

    class FakeCodeAgent:
        def __init__(self, **kwargs: object) -> None:
            captured["agent_kwargs"] = kwargs

    monkeypatch.setattr(
        demo,
        "load_settings",
        lambda: SimpleNamespace(
            model_id="test-model",
            base_url="https://example.test/v1",
            api_key="test-key",
        ),
    )
    monkeypatch.setattr(demo, "OpenAIModel", FakeModel)
    monkeypatch.setattr(demo, "CodeAgent", FakeCodeAgent)

    agent = demo.build_agent()

    assert isinstance(agent, FakeCodeAgent)
    assert captured["model_kwargs"] == {
        "model_id": "test-model",
        "api_base": "https://example.test/v1",
        "api_key": "test-key",
    }
    assert captured["agent_kwargs"] == {
        "tools": [demo.fibonacci_number],
        "model": captured["model"],
    }
