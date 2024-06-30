import json
from functools import reduce

with open('people.json', 'r', encoding='utf=8') as file:
    data = json.load(file)
    keys = reduce(lambda a, b: set(a).union(set(b)), data, set())
    for item in data:
        for key in keys.difference(set(item)):
            item[key] = None

with open('updated_people.json', 'w', encoding='utf=8') as file:
    json.dump(data, file)
