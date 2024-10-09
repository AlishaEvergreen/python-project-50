import json
import yaml
from pathlib import Path


def get_file_extension(filepath):
    '''Returns the file extension for the given file.'''
    return Path(filepath).suffix


def read_file(filepath, encoding='utf-8'):
    '''Reads the file content based on the file extension.'''
    extension = get_file_extension(filepath)

    with open(filepath, 'r', encoding=encoding) as file:
        data = file.read()

    return parse_data(data, extension)


def parse_data(data, file_extension):
    '''Parses the file data depending on its extension.'''
    parsers = {
        '.json': lambda data: json.loads(data),
        '.yml': lambda data: yaml.load(data, Loader=yaml.FullLoader),
        '.yaml': lambda data: yaml.load(data, Loader=yaml.FullLoader),
    }

    if file_extension in parsers:
        return parsers[file_extension](data)

    raise ValueError(f'Unsupported file extension - {file_extension}')
