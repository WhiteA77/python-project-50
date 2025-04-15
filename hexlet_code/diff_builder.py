def build_diff(data1, data2):
    diff = {}
    keys = sorted({**data1, **data2}.keys())

    for key in keys:
        if key not in data2:
            diff[key] = {"type": "removed", "value": data1[key]}
        elif key not in data1:
            diff[key] = {"type": "added", "value": data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                "type": "nested",
                "children": build_diff(data1[key], data2[key]),
            }
        elif data1[key] == data2[key]:
            diff[key] = {"type": "unchanged", "value": data1[key]}
        else:
            diff[key] = {
                "type": "changed",
                "old_value": data1[key],
                "new_value": data2[key],
            }
    return diff
