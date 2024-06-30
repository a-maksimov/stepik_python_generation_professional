from collections import Counter
import csv
import json

files_list = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']

veg_count = Counter()
for filename in files_list:
    with open(filename, encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
        for row in rows:
            veg_count += Counter({row['продукт']: sum([int(value) for value in list(row.values())[1:]])})

with open('prices.json', encoding='utf-8') as file:
    prices = json.load(file)

total_earnings = sum(veg_count[product] * prices[product] for product in veg_count)
print(total_earnings)