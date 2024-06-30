from itertools import pairwise


def is_rising(iterable):
    return all(map(lambda pair: pair[1] - pair[0] > 0, pairwise(iterable)))


print(is_rising([1, 2, 3, 4, 5]))

iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

# def is_rising(iterable):
#     return all(a < b for a, b in pairwise(iterable))
#
# from itertools import pairwise, starmap
# def is_rising(iterable):
#     return all(starmap(lambda a, b: a < b, pairwise(iterable)))