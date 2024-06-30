from functools import wraps


def square(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res ** 2

    return wrapper


@square
def add(a, b):
    return a + b


print(add(3, 7))
