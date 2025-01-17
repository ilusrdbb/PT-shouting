import yaml
from lxml import html

config_data = {}


def init_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        global config_data
        config_data = yaml.safe_load(f)


def read(key):
    return config_data.get(key)
