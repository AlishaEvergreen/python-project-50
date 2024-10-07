import json
import yaml
from pathlib import Path


def load_json(filepath):
    '''Load and parse a JSON file.'''
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_yaml(filepath):
    '''Load and parse a YAML file.'''
    with open(filepath, 'r', encoding='utf-8') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def parse_by_extension(file):
    '''Parses the file depending on its extension.'''
    file_extension = Path(file).suffix
    if file_extension in ['.yml', '.yaml']:
        return load_yaml(file)
    elif file_extension == '.json':
        return load_json(file)
    return ValueError(f'Unsupported file extension - .{file_extension}')
