from argparse import ArgumentParser
from hexlet_code.parsers import parse_file
from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters.stylish import format_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    
    if format_name == 'stylish':
        return format_stylish(diff)
    raise ValueError(f"Unknown format: {format_name}")


def main():
    parser = ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                       help='set format of output (default: stylish)')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))