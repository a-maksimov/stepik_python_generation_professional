# import csv
#
# with open('wifi.csv', 'r', encoding='utf-8') as file:
#     rows = list(csv.reader(file, delimiter=';'))
#     del rows[0]
#     districts = []
#     for row in rows:
#         if [row[1], 0] not in districts:
#             districts.append([row[1], 0])
#     for row in rows:
#         for district in districts:
#             if row[1] == district[0]:
#                 district[1] += int(row[-1])
#
# for district in sorted(sorted(districts), key=lambda d: d[1], reverse=True):
#     print(f'{district[0]}: {district[1]}')

import csv

with open('wifi.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    districts = {}
    for row in rows:
        districts[row['district']] = districts.get(row['district'], 0) + int(row['number_of_access_points'])
for district in sorted(sorted(districts), key=lambda d: districts.get(d), reverse=True):
    print(f'{district}: {districts.get(district)}')

