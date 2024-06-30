def get_value(data, key):
    if key in data:
        return data[key]  # базовый случай

    for v in data.values():
        if type(v) == dict:
            value = get_value(v, key)  # рекурсивный случай
            if value is not None:
                return value
