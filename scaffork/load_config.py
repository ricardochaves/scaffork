import yaml

from scaffork.data import Config


def _build_config(data: dict) -> Config:
    return Config(data)


def load_config_yaml(file: str) -> Config:
    with open(file, "r") as stream:
        return _build_config(yaml.load(stream))
