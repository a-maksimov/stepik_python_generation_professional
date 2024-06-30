def takes_positive(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + [value for value in kwargs.values()]:
            if int(arg) != arg:
                raise TypeError()
            if abs(arg) != arg or arg == 0:
                raise ValueError()
        return func(*args, **kwargs)

    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(*range(100, -1, -1)))
except Exception as err:
    print(type(err))
