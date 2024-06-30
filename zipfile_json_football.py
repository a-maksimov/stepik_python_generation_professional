import json
from zipfile import ZipFile


def is_correct_json(file):
    try:
        data = json.load(file)
    except:
        return {}
    return data


with ZipFile('data.zip', mode='r') as zip_file:
    info = zip_file.infolist()
    jsons = list(map(lambda f: f.filename, list(filter(lambda f: f.filename.split('.')[-1] == 'json', info))))
    [zip_file.extract(filename) for filename in jsons]

players = set()
for filename in jsons:
    with open(filename, 'r', encoding='utf-8') as file:
        data = is_correct_json(file)
        if data:
            if data['team'] == 'Arsenal':
                players.add(data['first_name'] + ' ' + data['last_name'])

for player in sorted(players):
    print(player)



