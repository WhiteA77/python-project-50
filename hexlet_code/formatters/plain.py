def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "'null'"
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, path=""):
    lines = []

    for key, node in diff.items():
        current_path = f"{path}.{key}" if path else key

        if node["type"] == "nested":
            nested_result = format_plain(node["children"], current_path)
            lines.append(nested_result)
        elif node["type"] == "added":
            value = format_value(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif node["type"] == "removed":
            lines.append(f"Property '{current_path}' was removed")
        elif node["type"] == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return "\n".join(filter(None, lines))
