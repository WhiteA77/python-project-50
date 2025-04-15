from argparse import ArgumentParser
from hexlet_code.parsers import parse_file


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    return build_diff(data1, data2)


def build_diff(data1, data2):
    keys = sorted({**data1, **data2}.keys())
    lines = []
    for key in keys:
        if key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {format_value(data1[key])}")
        else:
            lines.append(f"  - {key}: {format_value(data1[key])}")
            lines.append(f"  + {key}: {format_value(data2[key])}")
    return "{\n" + "\n".join(lines) + "\n}"


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def main():
    parser = ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()