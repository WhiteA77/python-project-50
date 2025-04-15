import json
import pytest
from hexlet_code import generate_diff

def test_json_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    result = generate_diff(file1, file2, 'json')
    
    # Проверяем что вывод валидный JSON
    parsed = json.loads(result)
    assert isinstance(parsed, dict)
    
    # Проверяем наличие ожидаемых ключей
    assert 'follow' in parsed or 'timeout' in parsed  # Пример проверки ключей
    assert any(item['type'] in ['added', 'removed', 'changed', 'unchanged'] 
               for item in parsed.values())