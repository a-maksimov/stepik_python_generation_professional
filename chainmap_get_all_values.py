from collections import ChainMap


def get_all_values(chainmap, key):
    values_set = set()
    for dictionary in chainmap.maps:
        if key in dictionary:
            values_set.add(dictionary[key])
    return values_set


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

result = get_all_values(chainmap, 'name')

print(*sorted(result))
