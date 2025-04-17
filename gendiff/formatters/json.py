import json


def format_json(diff):
    def convert_node(node):
        if node["type"] == "nested":
            return {**node, "children": format_json(node["children"])}
        return node

    if isinstance(diff, dict):
        return {key: convert_node(value) for key, value in diff.items()}
    return diff


def format_json_output(diff):
    processed_diff = format_json(diff)
    return json.dumps(processed_diff, indent=2)
