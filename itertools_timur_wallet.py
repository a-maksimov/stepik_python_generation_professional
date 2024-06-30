wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

from itertools import combinations

combs = (combinations(wallet, r=i) for i in range(len(wallet)))

comb_set = set()
for comb_len in combs:
    for comb in comb_len:
        if sum(comb) == 100:
            comb_set.add(comb)

print(len(comb_set))
