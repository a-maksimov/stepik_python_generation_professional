def is_greater(lists, number):
    return any(map(lambda l: True if sum(l) > number else False, lists))