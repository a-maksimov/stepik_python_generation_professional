from collections import Counter

products = input().split(',')

def get_value(word):
    return sum([ord(c) for c in word if c.isalpha()])

products_counter = Counter(products)

for product, num in sorted(products_counter.items()):
    value = get_value(product)
    print(f'{product}{" " * (len(max(products, key=len)) - len(product))}: {value} UC x {num} = {value * num} UC')