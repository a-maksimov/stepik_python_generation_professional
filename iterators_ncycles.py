from itertools import chain, tee


def ncycles(iterable, times):
    iterators = tee(iterable, times)
    return chain.from_iterable(iterators)


print(*ncycles([1, 2, 3, 4], 3))