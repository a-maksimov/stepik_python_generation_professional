from itertools import groupby

word_list = sorted(input().split())

group_len = groupby(sorted(word_list, key=lambda w: len(w)), key=lambda w: len(w))

for length, group in group_len:
    print(f'{length} -> {", ".join(group)}')