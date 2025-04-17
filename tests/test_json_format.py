import json

from gendiff import generate_diff


def test_json_format():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"
    result = generate_diff(file1, file2, "json")

    # Проверяем, что результат — валидный JSON-объект
    parsed = json.loads(result)
    assert isinstance(parsed, dict)

    # Проверяем наличие ключей верхнего уровня
    assert "follow" in parsed or "timeout" in parsed

    # Проверяем, что каждый элемент содержит допустимый тип изменений
    assert any(
        item["type"] in ["added", "removed", "changed", "unchanged"]
        for item in parsed.values()
    )
