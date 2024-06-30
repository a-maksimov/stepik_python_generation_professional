def count_iterable(iterable):
    counter = 0
    return sum(counter + 1 for _ in iterable)


numbers = iter([1, 2, 3, 4, 5, 6, 7])

print(count_iterable(numbers))
