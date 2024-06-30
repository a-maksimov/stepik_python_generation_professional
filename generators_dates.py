from datetime import date, timedelta


def dates(start, count=None):
    index = -1
    result = start + timedelta(days=index + 1)
    if count is None:
        while result <= date(9999, 12, 31):
            yield result
            if result != date(9999, 12, 31):
                index += 1
                result = start + timedelta(days=index + 1)
            else:
                break
    else:
        while index < count - 1 and result <= date(9999, 12, 31):
            yield result
            if result != date(9999, 12, 31):
                index += 1
                result = start + timedelta(days=index + 1)
            else:
                break


generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))

print()

generator = dates(date(2022, 3, 8), 5)

print(*generator)

print()

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')
