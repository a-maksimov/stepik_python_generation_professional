import json

filename = input()

try:
    with open(filename, encoding='utf-8') as file:
        content = json.load(file)
except ValueError:
    print('Ошибка при десериализации')
except:
    print('Файл не найден')