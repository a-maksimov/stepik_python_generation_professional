import json
import csv

with open('playgrounds.csv', 'r', encoding='utf=8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    addresses = {}
    for item in data:
        addresses[item['AdmArea']] = addresses.setdefault(item['AdmArea'], {})
        addresses[item['AdmArea']].update({item['District']: addresses[item['AdmArea']].get(item['District'], []) + [item.get('Address')]})
with open('addresses.json', 'w', encoding='utf=8') as file:
    json.dump(addresses, file, indent=3, separators=(', ', ': '), ensure_ascii=False)

# # ChatGPT:
#
# import csv
# import json
# 
# # читаем файл playgrounds.csv и создаем словарь
# playgrounds = {}
# with open('playgrounds.csv', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile, delimiter=';')
#     next(reader)  # пропускаем заголовок
#     for row in reader:
#         _, adm_area, district, address = row
#         if adm_area not in playgrounds:
#             playgrounds[adm_area] = {}
#         if district not in playgrounds[adm_area]:
#             playgrounds[adm_area][district] = []
#         playgrounds[adm_area][district].append(address)
#
# # записываем словарь в JSON файл
# with open('addresses.json', 'w', encoding='utf-8') as jsonfile:
#     json.dump(playgrounds, jsonfile, ensure_ascii=False, indent=4)