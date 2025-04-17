from gendiff import generate_diff


def test_plain_format():
    file1 = "tests/fixtures/nested_file1.json"
    file2 = "tests/fixtures/nested_file2.json"
    with open("tests/fixtures/plain_expected.txt") as f:
        expected = f.read().strip()
    assert generate_diff(file1, file2, "plain") == expected
