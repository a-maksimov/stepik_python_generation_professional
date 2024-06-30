def get_min_max(data):
    if data:
        return min(enumerate(data), key=lambda item: item[1])[0], max(enumerate(data), key=lambda item: item[1])[0]


data = [2, 3, 8, 1, 7]

print(get_min_max(data))
