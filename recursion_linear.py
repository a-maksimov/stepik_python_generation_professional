def linear(nested_lists):
    ls = []
    for item in nested_lists:
        if isinstance(item, int):
            ls.append(item)
        else:
            ls = ls + linear(item)
    return ls


my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))
