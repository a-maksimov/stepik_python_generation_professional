from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if key in chainmap:
        if not from_left:
            chainmap.maps.reverse()
        return chainmap[key]

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))
print(get_value(chainmap, 'name', False))

# def get_value(chainmap, key, from_left=True):
#     if not from_left:
#         chainmap.maps.reverse()
#     return chainmap.get(key)