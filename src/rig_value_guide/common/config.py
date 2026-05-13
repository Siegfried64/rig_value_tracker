from pathlib import Path

import yaml

base_dir = Path(__file__).resolve().parents[3]

def load_config():
    config_path = base_dir / "config/settings.yaml"
    with config_path.open("r") as file:
        config = yaml.safe_load(file)

    if "paths" in config:
        for key, value in config["paths"].items():
            config["paths"][key] = base_dir / value

        return config

config = load_config()
