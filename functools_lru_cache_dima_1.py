from functools import lru_cache
import sys


@lru_cache
def dima_1(string):
    return ''.join(sorted(string))


for line in sys.stdin:
    res = dima_1(line.strip())
    print(res)
