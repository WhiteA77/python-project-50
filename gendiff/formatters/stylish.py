INDENT = 4  # Константа для размера отступа


def format_value(value, depth):
    if isinstance(value, dict):
        current_indent = ' ' * (depth + 1) * INDENT
        closing_indent = ' ' * depth * INDENT
        lines = []
        for key, val in value.items():
            lines.append(
                f"{current_indent}{key}: {format_value(val, depth + 1)}"
            )
        return '{\n' + '\n'.join(lines) + '\n' + closing_indent + '}'
    
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff, depth=0):
    lines = []
    base_indent = ' ' * depth * INDENT
    value_indent = ' ' * (depth + 1) * INDENT
    
    for key, node in sorted(diff.items()):
        node_type = node['type']
        
        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(
                f"{value_indent}{key}: {{\n{children}\n{value_indent}}}"
            )
        elif node_type == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{base_indent}{' ' * (INDENT - 2)}+ {key}: {value}")
        elif node_type == 'removed':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{base_indent}{' ' * (INDENT - 2)}- {key}: {value}")
        elif node_type == 'changed':
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            lines.append(
                f"{base_indent}{' ' * (INDENT - 2)}- {key}: {old_value}"
            )
            lines.append(
                f"{base_indent}{' ' * (INDENT - 2)}+ {key}: {new_value}"
            )
        else:  # unchanged
            value = format_value(node['value'], depth + 1)
            lines.append(f"{value_indent}{key}: {value}")
    
    result = '{\n' + '\n'.join(lines) + '\n' + ' ' * depth * INDENT + '}'
    return result