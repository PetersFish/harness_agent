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