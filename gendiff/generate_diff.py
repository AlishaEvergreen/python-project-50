import json


def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def serialize_bool(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


def make_stylish(data, format):
    status_symbols = {
        'unchanged': '   ',
        'removed': ' - ',
        'changed': ' + ',
        'added': ' + '
    }
    lines = []
    indent = ' '

    for line in data:
        filtered_items = filter(lambda item: item[0] != 'type', line.items())
        key, value = list(filtered_items)[0]
        status_symbol = status_symbols.get(line['type'])
        line = f'{indent}{status_symbol}{key}: {serialize_bool(value)}'
        lines.append(line)

        result = ["{", *lines, "}"]

    return '\n'.join(result)


def generate_diff(first_file, second_file, format):
    file1, file2 = load_json(first_file), load_json(second_file)

    combined_keys = sorted(file1.keys() | file2.keys())
    diffs = []

    for key in (combined_keys):
        value1, value2 = file1.get(key), file2.get(key)

        if value1 == value2:
            diffs.append({'type': 'unchanged', key: value1})
        elif key in file1 and key in file2:
            diffs.append({'type': 'removed', key: value1})
            diffs.append({'type': 'changed', key: value2})
        elif key in file1:
            diffs.append({'type': 'removed', key: value1})
        elif key in file2:
            diffs.append({'type': 'added', key: value2})
    return make_stylish(diffs, format)
