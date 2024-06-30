def around(iterable):
    if iterable:
        iterable = iter(iterable)
        item = None
        next_item = next(iterable)
        next_next_item = next(iterable, None)
        yield item, next_item, next_next_item
        elem = None
        for elem in iterable:
            yield next_item, next_next_item, elem
            next_item = next_next_item
            next_next_item = elem
        yield next_item, next_next_item, None
    else:
        iterable


data = map(str.upper, 'yt')

print(*around(data))
