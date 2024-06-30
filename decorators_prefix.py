from functools import wraps


def prefix(string, to_the_end=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if to_the_end:
                return res + string
            else:
                return string + res
        return wrapper
    return decorator


@prefix('€')
def get_bonus():
    return '2000'


print(get_bonus())