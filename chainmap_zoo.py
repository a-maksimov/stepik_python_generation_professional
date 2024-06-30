import json
from collections import ChainMap

with open('zoo.json', encoding='utf-8') as file:
    content = json.load(file)
    chain = ChainMap(*content)
    total = sum(chain.values())

print(total)