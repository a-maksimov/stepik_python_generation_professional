from functools import wraps


def takes(*args):
    def decorator(func):
        @wraps(func)
        def wrapper(*fargs, **kwargs):
            if all(isinstance(farg, args) for farg in list(fargs) + list(kwargs.values())):
                res = func(*fargs, **kwargs)
                return res
            else:
                raise TypeError

        return wrapper

    return decorator


@takes(int, str)
def repeat_string(string, times):
    return string * times


print(repeat_string('bee', 3))
