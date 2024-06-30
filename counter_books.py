from collections import Counter

library = Counter(input().split())

n = int(input())
price_counter = Counter()

for _ in range(n):
    cl, price = input().split()
    library.subtract({cl: 1})
    if library[cl] >= 0:
        price_counter.update({cl: int(price)})

print(price_counter.total())

# from collections import Counter
# 
# books = Counter(map(int, input().split()))
# total = 0
#
# for _ in range(int(input())):
#     book, price = map(int, input().split())
#     total += bool(books[book]) * price
#     books -= Counter({book: 1})
#
# print(total)