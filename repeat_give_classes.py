def print_given(*args, **kwargs):
    if any([args, kwargs]):
        types_args = list(map(lambda name: (name, type(name)), args))
        types_kwargs = sorted(list(map(lambda name: (name[0], name[1], type(name[1])), kwargs.items())))
        for arg in types_args + types_kwargs:
            print(*arg)


# def print_given(*args, **kwargs):
#     print(*(f'{i} {type(i)}' for i in args), sep='\n')
#     print(*(f'{k} {v} {type(v)}' for k, v in sorted(kwargs.items())), sep='\n')

print_given(1, [1, 2, 3], 'three', two=2)

print_given(b=2, d=4, c=3, a=1)
