from argparse import ArgumentParser

from gendiff.diff_builder import build_diff
from gendiff.formatters.json import format_json_output
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import parse_file

FORMATTERS = {
    "stylish": format_stylish,
    "plain": format_plain,
    "json": format_json_output,
}


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)

    formatter = FORMATTERS.get(format_name)
    if not formatter:
        raise ValueError(
            f"Unknown format: '{format_name}'. "
            f"Available formats: {', '.join(FORMATTERS)}"
        )

    return formatter(diff)


def main():
    parser = ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        help="set format of output (default: stylish)",
    )
    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)
