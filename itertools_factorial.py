from itertools import accumulate
from operator import mul


def factorials(n):
    yield from accumulate(range(1, n + 1), mul)


numbers = factorials(6)

print(*numbers)