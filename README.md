# Hexlet tests and linter status

[![Actions Status](https://github.com/WhiteA77/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/WhiteA77/python-project-50/actions) [![CI Pipeline](https://github.com/WhiteA77/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/WhiteA77/python-project-50/actions/workflows/ci.yml) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=WhiteA77_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=WhiteA77_python-project-50)

## Gendiff - Configuration File Difference Generator

A command-line utility to find differences between configuration files.

## Features

- Supports JSON and YAML file formats
- Multiple output formats (stylish, plain text, and JSON)
- Easy to use command-line interface
- Handles nested structures

### Arguments

- `first_file`: Path to the first configuration file
- `second_file`: Path to the second configuration file
- `-f, --format`: Output format (default: stylish)
  - `stylish`: Structured output with indentation
  - `plain`: Plain text output
  - `json`: JSON format output

### Сравнение плоских файлов (JSON)

[![asciicast](https://asciinema.org/a/HqBr8HYZmDjOOvvQRuF3EdM4y.svg)](https://asciinema.org/a/HqBr8HYZmDjOOvvQRuF3EdM4y)

### Сравнение плоских файлов (YAML)

[![asciicast](https://asciinema.org/a/VriXfEs6SSjoWRj3ZqrpM0urS.svg)](https://asciinema.org/a/VriXfEs6SSjoWRj3ZqrpM0urS)

### Рекурсивное сравнение

[![asciicast](https://asciinema.org/a/G8HfthNbKRX7jJlj2UwFRCNyw.svg)](https://asciinema.org/a/G8HfthNbKRX7jJlj2UwFRCNyw)

### Плоский формат

[![asciicast](https://asciinema.org/a/AwiTjwTCtHsMzEZPwldMV8zrm.svg)](https://asciinema.org/a/AwiTjwTCtHsMzEZPwldMV8zrm)

### Вывод в JSON

[![asciicast](https://asciinema.org/a/HBXcVKaz0ullH7eLNcp6ruF9W.svg)](https://asciinema.org/a/HBXcVKaz0ullH7eLNcp6ruF9W)