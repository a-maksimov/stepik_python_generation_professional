from itertools import compress


def take(iterable, n):
    selector = [True] * n
    return compress(iterable, selector)


iterator = iter('beegeek')

print(*take(iterator, 22))

# from itertools import islice as take