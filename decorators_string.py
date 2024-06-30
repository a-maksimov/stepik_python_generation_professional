from functools import wraps


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return res
        else:
            raise TypeError()
    return wrapper


@returns_string
def beegeek():
    return 'beegeek'


print(beegeek())