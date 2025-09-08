import os
from typing import Any

import yaml


def load_default_config() -> dict[str, Any]:
    config_path = os.path.join(os.path.dirname(__file__), "_default_lemonade_config.yaml")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config
