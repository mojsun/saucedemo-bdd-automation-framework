"""Read configuration from config.json. For a larger project, consider python-dotenv + YAML or Pydantic Settings."""
import json
import os

_config = None
_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config.json")


def get_config():
    global _config
    if _config is None:
        with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
            _config = json.load(f)
    return _config
