def all_together(*args):
    return (item for iterable in args for item in iterable)


objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))
