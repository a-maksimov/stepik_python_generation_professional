from collections import namedtuple
from itertools import combinations, chain


Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

capacity = int(input())

if capacity < min(map(lambda i: i.mass, items)):
    print('Рюкзак собрать не удастся')
else:
    bag_set = set()
    combs = (combinations(items, r=i) for i in range(len(items) + 1))
    for comb_len in combs:
        comb_len_filtered = filter(lambda items: sum(map(lambda i: i.mass, items)) <= capacity, comb_len)
        for comb in comb_len_filtered:
            bag_set.add(comb)

    bag = max(bag_set, key=lambda b: sum(map(lambda i: i.price, b)))
    print(sum(map(lambda i: i.mass, bag)))
    for item in sorted(bag, key=lambda i: i.name):
        print(item.name)

# TEST_15:
# Гитара
# Золотая монета
# Лимитированные кроссовки
# Мобильный телефон
# Наушники
# Ноутбук
# Обручальное кольцо
# Ручка Паркер
# Статуэтка Оскар
# Фотоаппарат