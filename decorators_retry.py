from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    res = func(*args, **kwargs)
                    return res
                except:
                    pass
            raise MaxRetriesException

        return wrapper

    return decorator


@retry(3)
def no_way():
    raise ValueError


try:
    no_way()
except Exception as e:
    print(type(e))

