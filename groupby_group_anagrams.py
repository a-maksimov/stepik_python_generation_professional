from itertools import groupby


def group_anagrams(words):
    words = sorted(words, key=lambda w: sorted(w))
    grouped_words = groupby(words, key=lambda w: sorted(w))
    return [tuple(group) for key, group in grouped_words]



groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

print(*groups)
