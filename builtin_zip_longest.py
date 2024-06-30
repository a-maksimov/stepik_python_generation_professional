def zip_longest(*args, fill=None):
    max_len = len(max(args, key=len))

    for arg in args:
        arg.extend([fill] * (max_len - len(arg)))

    return list(zip(*args))


data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))


