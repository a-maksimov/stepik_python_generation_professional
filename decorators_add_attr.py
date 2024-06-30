from functools import wraps


def add_attrs(**kwargs):
    def decorator(func):
        func.__dict__.update(kwargs)

        @wraps(func)
        def wrapper(*args, **fkwargs):
            res = func(*args, **fkwargs)
            return res

        return wrapper

    return decorator


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
