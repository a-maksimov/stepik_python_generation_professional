from itertools import zip_longest


def grouper(iterable, n):
    iterable = iter(iterable)
    iterators = (iterable for _ in range(n))
    return zip_longest(*iterators)

numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))

iterator = iter([1, 2, 3, 4, 5, 6, 7])

print(*grouper(iterator, 3))

