import json
from pathlib import Path

import yaml


def parse_file(file_path):
    path = Path(file_path)
    if path.suffix in (".yaml", ".yml"):
        return parse_yaml(file_path)
    elif path.suffix == ".json":
        return parse_json(file_path)
    raise ValueError(f"Unsupported file format: {path.suffix}")


def parse_json(file_path):
    with open(file_path) as f:
        return json.load(f)


def parse_yaml(file_path):
    with open(file_path) as f:
        return yaml.safe_load(f)
