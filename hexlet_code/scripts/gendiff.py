import argparse
import json
from pathlib import Path

def parse_file(file_path):
    """Чтение и парсинг JSON-файла"""
    with open(file_path) as f:
        return json.load(f)

def generate_diff():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False
    )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument(
        '-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='show this help message and exit'
    )
    optional_args.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output'
    )
    
    return parser

def main():
    parser = generate_diff()
    args = parser.parse_args()
    
    # Получаем абсолютные пути к файлам
    file1 = Path(args.first_file).absolute()
    file2 = Path(args.second_file).absolute()
    
    # Парсим файлы
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    
    # Выводим информацию для проверки
    print(f"File 1 ({file1}):")
    print(data1)
    print(f"\nFile 2 ({file2}):")
    print(data2)
    print(f"\nOutput format: {args.format or 'plain'}")

if __name__ == '__main__':
    main()