from itertools import count


def tabulate(func):
    counter = count()
    yield from (func(i + 1) for i in counter)


func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))