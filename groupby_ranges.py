from itertools import groupby, tee


def ranges(numbers):
    grouped_numbers = groupby(numbers, key=lambda n: numbers.index(n) - n)
    groups = (tee(group) for key, group in grouped_numbers)
    return [(next(a), list(b)[-1]) for a, b in groups]


numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))