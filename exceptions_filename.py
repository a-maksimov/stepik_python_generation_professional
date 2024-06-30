filename = input()
try:
    with open(filename, encoding='utf-8') as file:
        print(file.read())
except:
    print('Файл не найден')