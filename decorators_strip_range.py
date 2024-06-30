from functools import wraps


def strip_range(start, end, char='.'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal end
            res = func(*args, **kwargs)
            if end <= len(res):
                begin = res[:start]
                ending = res[end:]
                return begin + char * (end - start) + ending

            elif start <= len(res):
                begin = res[:start]
                return begin + char * (len(res) - len(res[:start]))
            return res

        return wrapper

    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())
