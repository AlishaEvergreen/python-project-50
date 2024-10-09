from gendiff.data_parsers import read_file
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


FORMATTERS = {
    'stylish': make_stylish,
    'plain': make_plain,
    'json': make_json,
}


def generate_diff(file1, file2, format='stylish'):
    """Generates the difference between two files."""
    first_dict = read_file(file1)
    second_dict = read_file(file2)
    diff = build_diff(first_dict, second_dict)

    return FORMATTERS[format](diff)


def build_diff(data1, data2):
    """ Builds a list of differences between two dictionaries."""
    combined_keys = sorted(data1.keys() | data2.keys())
    return [get_node(key, data1, data2) for key in combined_keys]


def get_node(key, data1, data2):
    """Determines the type of difference for a specific key."""
    value1 = data1.get(key)
    value2 = data2.get(key)

    match (key in data1, key in data2, value1, value2):
        case (True, False, _, _):
            return create_diff_dict('removed', key, value1)
        case (False, True, _, _):
            return create_diff_dict('added', key, value2)
        case (True, False, value1, _) if is_dict(value1):
            return create_diff_dict('nested', key, build_diff(value1))
        case (False, True, _, value2) if is_dict(value2):
            return create_diff_dict('nested', key, build_diff(value2))
        case (True, True, value1, value2):
            if value1 == value2:
                return create_diff_dict('unchanged', key, value1)
            elif is_dict(value1) and is_dict(value2):
                return create_diff_dict(
                    'nested', key, build_diff(value1, value2)
                )
            return create_diff_dict('updated', key, value1, value2)


def is_dict(data):
    """Checks if the given object is a dictionary."""
    return isinstance(data, dict)


def create_diff_dict(diff_type, key, value1, value2=None):
    """Builds a dictionary with information about the type of change."""
    diff_dict = {
        'type': diff_type,
        'key': key,
    }
    if diff_type == 'nested':
        diff_dict['children'] = value1
    else:
        diff_dict['value1'] = value1

    if diff_type == 'updated':
        diff_dict['value2'] = value2

    return diff_dict
