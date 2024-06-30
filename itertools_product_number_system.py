from itertools import product

n = int(input())
m = int(input())

values = '0123456789ABCDEF'

numbers = values[:n]

print(*(''.join(tup) for tup in product(numbers, repeat=m)))