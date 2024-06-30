from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]


print(len(*(combination for combination in combinations(wallet, r=len(wallet)) if sum(combination) == 100)))