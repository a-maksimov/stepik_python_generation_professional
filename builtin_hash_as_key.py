def hash_as_key(objects):
    hash_list = [(hash(o), o) for o in objects]
    hash_dict = {}
    for o in hash_list:
        hash_dict[o[0]] = hash_dict.get(o[0], []) + [o[1]]
    for k, v in hash_dict.items():
        if len(v) == 1:
            hash_dict[k] = v[0]

    return hash_dict


data = [1, 2, 3, 4, 5, 5]

print(hash_as_key(data))
