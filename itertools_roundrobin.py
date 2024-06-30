def zip_longest(*args, fill=None):
    max_len = len(max(args, key=len))

    for arg in args:
        arg.extend([fill] * (max_len - len(arg)))

    return zip(*args)


def roundrobin(*args):
    if args:
        sequences = zip_longest(*(list(arg) for arg in args), fill='_')
        yield from (elem for tup in sequences for elem in tup if elem != '_')
    else:
        return []


print(*roundrobin('abc', 'd', 'ef'))