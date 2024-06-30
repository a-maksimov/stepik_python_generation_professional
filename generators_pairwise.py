def pairwise(iterable):
    if iterable:
        iterable = iter(iterable)
        item = next(iterable)
        elem = next(iterable, None)
        yield item, elem
        for item in iterable:
            yield elem, item
            elem = item
        yield item, None
    else:
        iterable


numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

iterator = pairwise('A')

print(next(iterator))