from random import randint


def random_numbers(left, right):

    return iter(lambda: randint(left, right), '')


iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))
