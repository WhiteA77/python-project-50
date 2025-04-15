import os
import pytest
from hexlet_code import generate_diff


def get_fixture_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', filename)


@pytest.mark.parametrize("file1,file2", [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml'),
    ('file1.yaml', 'file2.yaml'),
])
def test_gendiff(file1, file2):
    with open(get_fixture_path('expected_result.txt')) as f:
        expected = f.read().strip()
    result = generate_diff(get_fixture_path(file1), get_fixture_path(file2))
    assert result == expected