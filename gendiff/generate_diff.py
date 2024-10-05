from gendiff.data_parsers import parse_by_extension
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain


FORMATTERS = {
    'stylish': make_stylish,
    'plain': make_plain,
}


def generate_diff(file1, file2, format='stylish'):
    """Generates the difference between two files."""
    first_dict = parse_by_extension(file1)
    second_dict = parse_by_extension(file2)
    diff = build_diff(first_dict, second_dict)

    return FORMATTERS[format](diff)


def build_diff(data1, data2):
    """ Builds a list of differences between two dictionaries."""
    diffs = []
    combined_keys = sorted(data1.keys() | data2.keys())

    for key in combined_keys:
        diff = set_type_for_difference(key, data1, data2)
        diffs.append(diff)

    return diffs


def set_type_for_difference(key, data1, data2):
    """Determines the type of difference for a specific key."""
    value1 = data1.get(key)
    value2 = data2.get(key)

    match (key in data1, key in data2, value1, value2):
        case (True, False, _, _):
            return set_type('removed', key, value1)
        case (False, True, _, _):
            return set_type('added', key, value2)
        case (True, False, value1, _) if is_dict(value1):
            return set_type('nested', key, build_diff(value1, {}))
        case (False, True, _, value2) if is_dict(value2):
            return set_type('nested', key, build_diff({}, value2))
        case (True, True, value1, value2):
            if value1 == value2:
                return set_type('unchanged', key, value1)
            elif is_dict(value1) and is_dict(value2):
                return set_type('nested', key, build_diff(value1, value2))
            else:
                return set_type('updated', key, value1, value2)


def is_dict(data):
    """Checks if the given object is a dictionary."""
    return isinstance(data, dict)


def set_type(diff_type, key, value1, value2="UNINITIALIZED"):
    """Builds a dictionary with information about the type of change."""
    result = {
        'type': diff_type,
        'key': key,
    }
    if diff_type == 'nested':
        result['children'] = value1
    else:
        result['value1'] = value1
    if value2 != "UNINITIALIZED":
        result['value2'] = value2

    return result
