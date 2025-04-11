import argparse

def generate_diff():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False
    )
    
    # Позиционные аргументы
    parser.add_argument(
        'first_file',
        help=''
    )
    parser.add_argument(
        'second_file',
        help=''
    )
    
    # Опциональные аргументы
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
    
    # Здесь будет основная логика сравнения файлов
    print(f"Comparing {args.first_file} and {args.second_file}")
    print(f"Output format: {args.format or 'plain'}")

if __name__ == '__main__':
    main()