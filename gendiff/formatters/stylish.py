def format_value(value, depth):
    if isinstance(value, dict):
        indent = ' ' * (depth + 4)
        lines = []
        for key, val in value.items():
            lines.append(f"{indent}{key}: {format_value(val, depth + 4)}")
        closing_indent = ' ' * (depth + 2)
        return '{\n' + '\n'.join(lines) + '\n' + closing_indent + '}'
    
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff, depth=0):
    lines = []
    base_indent = ' ' * (depth + 2)
    
    for key, node in sorted(diff.items()):
        node_type = node['type']
        value_indent = depth + 4
        
        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 4)
            lines.append(f"{base_indent}  {key}: {children}")
        elif node_type == 'added':
            value = format_value(node['value'], value_indent)
            lines.append(f"{base_indent}+ {key}: {value}")
        elif node_type == 'removed':
            value = format_value(node['value'], value_indent)
            lines.append(f"{base_indent}- {key}: {value}")
        elif node_type == 'changed':
            old_value = format_value(node['old_value'], value_indent)
            new_value = format_value(node['new_value'], value_indent)
            lines.append(f"{base_indent}- {key}: {old_value}")
            lines.append(f"{base_indent}+ {key}: {new_value}")
        else:  # unchanged
            value = format_value(node['value'], value_indent)
            lines.append(f"{base_indent}  {key}: {value}")
    
    result = ['{'] + lines + [' ' * depth + '}']
    return '\n'.join(result)