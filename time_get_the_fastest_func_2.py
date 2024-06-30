import time


def get_the_fastest_func(funcs, arg):
    times = {}
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        times[end_time - start_time] = func
    return times[min(times)]


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


fastest_function = get_the_fastest_func([list_comprehension, list_function, list_comprehension], range(100_000))
print(fastest_function)
