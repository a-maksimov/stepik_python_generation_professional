from functools import wraps


def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator


@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')


say_beegeek()