def numbers_sum(elems):
    """
    Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    """
    return sum([elem if isinstance(elem, (int, float)) else 0 for elem in elems])

print(numbers_sum([1, '2', 3, 4, 'five']))
