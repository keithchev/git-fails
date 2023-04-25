import os
import pathlib
import yaml

CONFIG_FILEPATH = pathlib.Path('~/.config/gitfails/config.yaml').expanduser()


def init_config(reset=False):
    os.makedirs(CONFIG_FILEPATH.parent, exist_ok=True)
    if reset or not os.path.isfile(CONFIG_FILEPATH):
        with open(CONFIG_FILEPATH, 'w') as file:
            yaml.dump(dict(), file)


def read_config():
    with open(CONFIG_FILEPATH, 'r') as file:
        return yaml.safe_load(file)


def write_config(config):
    with open(CONFIG_FILEPATH, 'w') as file:
        yaml.dump(config, file)
