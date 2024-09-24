import json
import yaml
from pathlib import Path


def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def load_yaml(filepath):
    with open(filepath, 'r') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def parse_by_extension(file):
    file_extension = Path(file).suffix
    if file_extension in ['.yml', '.yaml']:
        return load_yaml(file)
    elif file_extension == '.json':
        return load_json(file)
    else:
        return ValueError(f'Unsupported file extension - .{file_extension}')
