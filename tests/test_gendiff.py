import os

import pytest

from gendiff import generate_diff


def get_fixture_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "fixtures", filename)


@pytest.mark.parametrize(
    "file1,file2",
    [
        ("file1.json", "file2.json"),
        ("file1.yml", "file2.yml"),
        ("file1.yaml", "file2.yaml"),
    ],
)
def test_gendiff(file1, file2):
    with open(get_fixture_path("expected_result.txt")) as f:
        expected = f.read().strip()
    result = generate_diff(get_fixture_path(file1), get_fixture_path(file2))
    assert result == expected

    def test_nested_structure():
        file1 = get_fixture_path("nested_file1.json")
        file2 = get_fixture_path("nested_file2.json")
        with open(get_fixture_path("nested_expected.txt")) as f:
            expected = f.read()
        assert generate_diff(file1, file2) == expected
