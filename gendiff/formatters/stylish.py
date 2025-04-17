INDENT = 4


def format_value(value, depth):
    if isinstance(value, dict):
        current_indent = " " * (depth + 1) * INDENT
        lines = []
        for key, val in value.items():
            formatted_value = format_value(val, depth + 1)
            lines.append(f"{current_indent}{key}: {formatted_value}")
        closing_indent = " " * depth * INDENT
        return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"

    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def format_stylish(diff, depth=0):
    lines = []
    current_indent = " " * depth * INDENT
    nested_indent = " " * (depth + 1) * INDENT

    for key, node in sorted(diff.items()):
        if node["type"] == "nested":
            children = format_stylish(node["children"], depth + 1)
            lines.append(f"{nested_indent}{key}: {children}")
        elif node["type"] == "added":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{current_indent}  + {key}: {value}")
        elif node["type"] == "removed":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{current_indent}  - {key}: {value}")
        elif node["type"] == "changed":
            old_value = format_value(node["old_value"], depth + 1)
            new_value = format_value(node["new_value"], depth + 1)
            lines.append(f"{current_indent}  - {key}: {old_value}")
            lines.append(f"{current_indent}  + {key}: {new_value}")
        else:  # unchanged
            value = format_value(node["value"], depth + 1)
            lines.append(f"{nested_indent}{key}: {value}")

    result = "{\n" + "\n".join(lines) + "\n" + current_indent + "}"
    return result
