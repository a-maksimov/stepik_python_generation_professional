def get_min_max(iterable):
    iterable = iter(iterable)
    try:
        min = next(iterable)
        max = min
        for item in iterable:
            if item <= min:
                min = item
            if item >= max:
                max = item
    except StopIteration:
        return None
    return min, max


iterable = iter(range(10))

print(get_min_max(iterable))
