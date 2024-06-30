import csv

with open('titanic.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    for survivor in sorted(rows, key=lambda d: d.get('sex'), reverse=True):
        if int(survivor['survived']) and float(survivor['age']) < 18:
            print(survivor['name'])