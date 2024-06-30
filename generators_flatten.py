def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, int):
            yield item
        else:
            yield from flatten(item)


generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)
