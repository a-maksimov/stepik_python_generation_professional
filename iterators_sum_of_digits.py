from itertools import chain


def sum_of_digits(iterable):
    gen = chain.from_iterable(str(item) for item in iterable)
    return sum(int(item) for item in gen)


print(sum_of_digits([13, 20, 41, 2, 2, 5]))
