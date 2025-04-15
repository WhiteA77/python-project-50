def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = " " * (depth + 4)
        closing_indent = " " * (depth + 2)

        for key, val in value.items():
            formatted = format_value(val, depth + 4)
            lines.append(f"{indent}{key}: {formatted}")

        return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"

    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def format_stylish(diff, depth=0):
    lines = []
    indent = " " * (depth + 2)

    for key, node in diff.items():
        value_depth = depth + 4

        if node["type"] == "nested":
            children = format_stylish(node["children"], value_depth)
            lines.append(f"{indent}  {key}: {children}")
        elif node["type"] == "added":
            value = format_value(node["value"], value_depth)
            lines.append(f"{indent}+ {key}: {value}")
        elif node["type"] == "removed":
            value = format_value(node["value"], value_depth)
            lines.append(f"{indent}- {key}: {value}")
        elif node["type"] == "changed":
            old_val = format_value(node["old_value"], value_depth)
            new_val = format_value(node["new_value"], value_depth)
            lines.append(f"{indent}- {key}: {old_val}")
            lines.append(f"{indent}+ {key}: {new_val}")
        else:
            value = format_value(node["value"], value_depth)
            lines.append(f"{indent}  {key}: {value}")

    result = ["{"] + lines + [" " * depth + "}"]
    return "\n".join(result)
