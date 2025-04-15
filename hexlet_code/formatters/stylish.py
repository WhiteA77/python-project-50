def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f"{' ' * (depth + 4)}{key}: {format_value(val, depth + 4)}")
        return '{\n' + '\n'.join(lines) + '\n' + ' ' * depth + '}'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)

def format_stylish(diff, depth=0):
    lines = []
    for key, node in diff.items():
        indent = ' ' * (depth + 2)
        if node['type'] == 'nested':
            lines.append(f"{indent}  {key}: {format_stylish(node['children'], depth + 4)}")
        elif node['type'] == 'added':
            lines.append(f"{indent}+ {key}: {format_value(node['value'], depth + 4)}")
        elif node['type'] == 'removed':
            lines.append(f"{indent}- {key}: {format_value(node['value'], depth + 4)}")
        elif node['type'] == 'changed':
            lines.append(f"{indent}- {key}: {format_value(node['old_value'], depth + 4)}")
            lines.append(f"{indent}+ {key}: {format_value(node['new_value'], depth + 4)}")
        else:
            lines.append(f"{indent}  {key}: {format_value(node['value'], depth + 4)}")
    
    result = ['{'] + lines + [' ' * depth + '}']
    return '\n'.join(result)