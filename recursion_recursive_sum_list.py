def recursive_sum(data):
    result = 0
    for item in data:
        if isinstance(item, int):
            result += item
        else:
            result += recursive_sum(item)
    return result


my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))
