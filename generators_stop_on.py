def stop_on(iterable, obj):
    iterable = iter(iterable)
    for item in iterable:
        if item == obj:
            return
        else:
            yield item


# numbers = [1, 2, 3, 4, 5]
#
# print(*stop_on(numbers, 4))
#
iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))