from functools import wraps


def returns(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, datatype):
                return res
            else:
                raise TypeError

        return wrapper

    return decorator


@returns(int)
def add(a, b):
    return a + b


print(add(10, 5))
