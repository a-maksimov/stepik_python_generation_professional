old_print = print


def print(*args, **kwargs):
    caps = tuple(arg.upper() if isinstance(arg, str) else arg for arg in args )

    if not kwargs:
        old_print(*caps)

    else:
        old_print(*caps, sep=kwargs['sep'].upper(), end=kwargs['end'].upper())


print('bee', 'geek', sep=' and ', end=' wow')
