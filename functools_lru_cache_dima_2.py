from functools import lru_cache


@lru_cache
def ways(number):
    if number == 1:
        return 1
    if number < 1:
        return 0
    return ways(number - 1) + ways(number - 3) + ways(number - 4)

print(ways(10))

