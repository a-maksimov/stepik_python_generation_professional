size_dict = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}  # словарь для преобразования размерностей

with open('files.txt', 'r', encoding='utf-8') as file:
    lines = [line.split() for line in file]

# Создаем сортированный список расширений из множества
filetypes = sorted({line[0].split('.')[1] for line in lines})

# Создаем список словарей. Каждый словарь -- файл
list_of_dicts = []
for line in lines:
    files_dict = {'filename': line[0].split('.')[0], 'filetype': line[0].split('.')[1], 'filesize': line[1],
                  'filesize_dimension': line[2]}
    list_of_dicts.append(files_dict)

# Группируем файлы по расширениям
groups = []
for filetype in filetypes:
    group = []
    for file in list_of_dicts:
        if file['filetype'] == filetype:
            group.append(file)
    groups.append(group)

for group in groups:
    summary = 0
    for file in sorted(group, key=lambda f: f['filename']):  # внутри группы сортируем файлы по имени
        print(file['filename'] + '.' + file['filetype'])
        summary += int(file['filesize']) * size_dict[file['filesize_dimension']]
    if 0 <= summary < size_dict['KB']:
        dimension = 'B'
    elif size_dict['KB'] <= summary < size_dict['MB']:
        summary = summary / size_dict['KB']
        dimension = 'KB'
    elif size_dict['MB'] <= summary < size_dict['GB']:
        summary = summary / size_dict['MB']
        dimension = 'MB'
    else:
        summary = summary / size_dict['GB']
        dimension = 'GB'
    print('----------')
    print(f'Summary: {round(summary)} {dimension}')
    print()
