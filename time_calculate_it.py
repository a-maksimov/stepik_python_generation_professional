import time


def calculate_it(function, *args):
    start_time = time.perf_counter()
    result = function(*args)
    end_time = time.perf_counter()
    return result, end_time - start_time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


print(calculate_it(add, 1, 2, 3))
