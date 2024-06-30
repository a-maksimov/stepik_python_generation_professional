import json

with open('data.json', 'r', encoding='utf=8') as file:
    data = json.load(file)
    new_data = []
    for i, item in enumerate(data):
        if isinstance(item, str):
            new_data.append(item + '!')
        elif isinstance(item, bool):
            new_data.append(not item)
        elif isinstance(item, int) or isinstance(item, float):
            new_data.append(item + 1)
        elif isinstance(item, list):
            new_data.append(item * 2)
        elif isinstance(item, dict):
            item['newkey'] = None
            new_data.append(item)

with open('updated_data.json', 'w', encoding='utf=8') as file:
    json.dump(new_data, file)

