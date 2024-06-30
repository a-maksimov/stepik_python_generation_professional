from collections import defaultdict


def flip_dict(dict_of_lists):
    flipped_dict = defaultdict(list)
    for key, value in dict_of_lists.items():
        for elem in value:
            flipped_dict[elem].append(key)
    return flipped_dict


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
