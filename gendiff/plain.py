def format_value(value):
    '''Convert the value to its string representation in the required format.'''
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def make_plain(diffs, path=''):
    '''Generate a plain representation of a list of differences.'''
    lines = []

    for diff in diffs:
        key = diff.get('key')
        value1 = format_value(diff.get('value1'))
        value2 = format_value(diff.get('value2'))
        current_path = f"{path}.{key}" if path else key

        match diff['type']:
            case 'unchanged': continue
            case 'added':
                lines.append(
                    f"Property '{current_path}' was added with value: {value1}"
                )
            case 'removed':
                lines.append(
                    f"Property '{current_path}' was removed"
                )
            case 'updated':
                lines.append(
                    f"Property '{current_path}' was updated. "
                    f"From {value1} to {value2}"
                )
            case 'nested':
                lines.append(
                    make_plain(diff['children'], current_path)
                )
            case _:
                pass
    return '\n'.join(lines)
