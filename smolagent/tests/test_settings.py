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