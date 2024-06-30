import json

with open('data1.json', 'r', encoding='utf=8') as file1, open('data2.json', 'r', encoding='utf=8') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)
    for key, value in data2.items():
        data1[key] = value

with open('data_merge.json', 'w', encoding='utf=8') as file:
    json.dump(data1, file)

    # Конкатенация словарей с помощью "|"
    #  json.dump(data1 | data2, file)
