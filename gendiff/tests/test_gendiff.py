import pytest
from gendiff import generate_diff
from pathlib import Path


def get_fixture_path(filename):
    return Path(__file__).parent / 'fixtures' / filename


def read_file(filepath):
    with open(filepath, encoding='utf8') as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, expected", [
    (get_fixture_path('file1.json'),
     get_fixture_path('file2.json'),
     read_file(get_fixture_path('flat_json_result.txt')))
])
def test_gendiff(file1, file2, expected):
    assert generate_diff(file1, file2) == expected
