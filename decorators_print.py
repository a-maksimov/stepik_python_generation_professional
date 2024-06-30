def upper_case_print(func):
    def wrapper(*args, **kwargs):
        args = [str(arg).upper() for arg in args]
        kwargs = {k: v.upper() for k, v in kwargs.items() if isinstance(v, str)}
        func(*args, **kwargs)
    return wrapper

print = upper_case_print(print)

print('hi', 'there', end='!')