wallet = [100, 50, 20, 10, 5]

from itertools import chain, combinations_with_replacement

# wallet = list(chain.from_iterable(map(lambda item: [item] * (100 // item), wallet)))

combs = (combinations_with_replacement(wallet, r=i) for i in range(21))

comb_set = set()
for comb_len in combs:
    for comb in comb_len:
        if sum(comb) == 100:
            comb_set.add(comb)

print(len(comb_set))