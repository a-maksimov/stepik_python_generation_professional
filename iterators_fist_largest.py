from itertools import dropwhile


def first_largest(iterable, number):

    return next(dropwhile(lambda pair: pair[1] < number, enumerate(iterable)), (-1, None))[0]


numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))