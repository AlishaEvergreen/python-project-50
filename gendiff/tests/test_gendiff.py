import pytest
from gendiff import generate_diff
from pathlib import Path


def get_fixture_path(filename):
    return Path(__file__).parent / 'fixtures' / filename


def read_file(filepath):
    with open(filepath, encoding='utf8') as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, format, expected, ", [
    (get_fixture_path('file1.json'),
     get_fixture_path('file2.json'), 'stylish',
     read_file(get_fixture_path('flat_json_yml_result.txt'))),

    (get_fixture_path('file1.yml'),
     get_fixture_path('file2.yml'), 'stylish',
     read_file(get_fixture_path('flat_json_yml_result.txt'))),

    (get_fixture_path('nested_file1.json'),
     get_fixture_path('nested_file2.json'), 'stylish',
     read_file(get_fixture_path('stylish_result.txt'))),

    (get_fixture_path('nested_file1.yaml'),
     get_fixture_path('nested_file2.yaml'), 'stylish',
     read_file(get_fixture_path('stylish_result.txt'))),

    (get_fixture_path('nested_file1.json'),
     get_fixture_path('nested_file2.json'), 'plain',
     read_file(get_fixture_path('plain_result.txt'))),

    (get_fixture_path('nested_file1.yaml'),
     get_fixture_path('nested_file2.yaml'), 'plain',
     read_file(get_fixture_path('plain_result.txt'))),

    (get_fixture_path('nested_file1.json'),
     get_fixture_path('nested_file2.json'), 'json',
     read_file(get_fixture_path('json_result.txt'))),

    (get_fixture_path('nested_file1.yaml'),
     get_fixture_path('nested_file2.yaml'), 'json',
     read_file(get_fixture_path('json_result.txt'))),
])
def test_gendiff(file1, file2, format, expected):
    assert generate_diff(file1, file2, format) == expected
