from itertools import product


def password_gen():
    numbers = range(10)
    yield from (str(a) + str(b) + str(c) for a, b, c in product(numbers, numbers, numbers))


passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))