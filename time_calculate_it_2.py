import time


def calculate_it(functions, *args):
    times_dict = {}
    for function in functions:
        start_time = time.perf_counter()
        result = function(*args)
        end_time = time.perf_counter()
        times_dict[function] = result, end_time - start_time
    return times_dict


def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


print(list(map(lambda item: (item[0], item[1][1]), calculate_it([for_and_append, list_comprehension]).items())))
