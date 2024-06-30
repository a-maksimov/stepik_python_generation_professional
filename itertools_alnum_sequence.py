from itertools import cycle
import string


letters = string.ascii_uppercase


def alnum_sequence():
    sequence = zip(range(1, 28), letters)
    yield from cycle(elem for pair in sequence for elem in pair)


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))