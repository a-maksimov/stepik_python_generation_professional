from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'TRACE: вызов {wrapper.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {wrapper.__name__}(): {repr(res)}')
        return res

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')


@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)


@trace
def beegeek():
    """beegeek docs"""
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)
