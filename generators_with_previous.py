def with_previous(iterable):
    iterable = iter(iterable)
    counter = 0
    for item in iterable:
        if counter == 0:
            yield item, None
            elem = item
            counter += 1
        else:
            yield item, elem
            elem = item
            counter += 1


numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))

def with_previous(iterable):
    prev = None
    return ((i, prev, prev := i)[:-1] for i in iterable)