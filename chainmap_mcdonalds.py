from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

chain = ChainMap(bread, meat, sauce, vegetables, toppings)

recipe = Counter(input().split(','))
max_len = len(max(recipe, key=len))
total = 0
string_len = 0
strings = []
for item, num in sorted(recipe.items()):
    string = f'{item}' + ' ' * (max_len - len(item)) + f' x {num}'
    strings.append(string)
    total += chain[item] * num
for string in strings:
    print(string)
total_string = f'ИТОГ: {total}р'
print('-' * max([len(max(strings, key=len)), len(total_string)]))
print(total_string)