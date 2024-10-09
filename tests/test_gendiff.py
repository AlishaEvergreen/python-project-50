import pytest
from gendiff import generate_diff
from pathlib import Path


def get_fixture_path(filename):
    '''Returns the full path to files from the 'fixtures' directory.'''
    return Path(__file__).parent / 'fixtures' / filename


def read_file(filepath):
    '''Reads the content of a file and returns it as a string.'''
    with open(filepath, encoding='utf8') as f:
        return f.read()


@pytest.mark.parametrize("filename1, filename2, format, expected", [
    ('file1.json', 'file2.json', 'stylish', 'flat_json_yml_result.txt'),
    ('file1.yml', 'file2.yml', 'stylish', 'flat_json_yml_result.txt'),
    ('nested_file1.json', 'nested_file2.json', 'stylish', 'stylish_result.txt'),
    ('nested_file1.yaml', 'nested_file2.yaml', 'stylish', 'stylish_result.txt'),
    ('nested_file1.json', 'nested_file2.json', 'plain', 'plain_result.txt'),
    ('nested_file1.yaml', 'nested_file2.yaml', 'plain', 'plain_result.txt'),
    ('nested_file1.json', 'nested_file2.json', 'json', 'json_result.txt'),
    ('nested_file1.yaml', 'nested_file2.yaml', 'json', 'json_result.txt'),
])
def test_gendiff(filename1, filename2, format, expected):
    file1 = get_fixture_path(filename1)
    file2 = get_fixture_path(filename2)
    result = read_file(get_fixture_path(expected))
    assert generate_diff(file1, file2, format) == result
