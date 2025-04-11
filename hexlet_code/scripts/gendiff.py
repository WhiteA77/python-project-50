import argparse
import json
from pathlib import Path

def parse_file(file_path):
    with open(file_path) as f:
        return json.load(f)

def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    
    for key in keys:
        if key not in data2:
            diff.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            diff.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            diff.append(f"    {key}: {data1[key]}")
        else:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")
    
    return "{\n" + "\n".join(diff) + "\n}"

def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    return build_diff(data1, data2)

def main():
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
    
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))

if __name__ == '__main__':
    main()