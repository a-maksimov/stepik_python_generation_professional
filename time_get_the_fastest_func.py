import time
from math import factorial  # функция из модуля math


def get_the_fastest_func(funcs, arg):
    times = {}
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        times[end_time - start_time] = func
    return times[min(times)]


def factorial_recurrent(n):  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):  # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


fastest_function = get_the_fastest_func([factorial, factorial_recurrent, factorial_classic], 900)
print(fastest_function)

