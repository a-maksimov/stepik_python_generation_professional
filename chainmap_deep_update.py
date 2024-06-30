from collections import ChainMap


def deep_update(chainmap, key, value):
    if all(map(lambda d: key not in d, chainmap.maps)):
        chainmap[key] = value
    else:
        for dictionary in chainmap.maps:
            if key in dictionary:
                dictionary.update({key: value})

chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)

# from collections import ChainMap
# def deep_update(chainmap, key, value):
#     for i in chainmap.maps:
#         if key in i:
#             i[key] = value
#     chainmap.setdefault(key, value)