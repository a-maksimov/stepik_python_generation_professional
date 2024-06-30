from functools import wraps


def ignore_exception(*exceptions):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as e:
                if e.__class__ in exceptions:
                    print(f'Исключение {e.__class__.__name__} обработано')
                else:
                    raise e

        return wrapper

    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)


@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    return 'beegeek'


print(beegeek())
