from itertools import dropwhile


def first_true(iterable, predicate):
    try:
        if predicate:
            return next(dropwhile(lambda item: not predicate(item), iterable))
        else:
            return next(dropwhile(lambda item: not bool(item), iterable))
    except StopIteration:
        return None


numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))
