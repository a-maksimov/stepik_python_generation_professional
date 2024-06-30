from zipfile import ZipFile


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'


with ZipFile('data.zip', mode='r') as zip_file:
    info = zip_file.infolist()

for item in info:
    path = item.filename.strip('/').split('/')
    if not item.is_dir():
        print('  ' * (len(path) - 1) + f'{path[-1]} {convert_bytes(item.file_size)}')
    else:
        print('  ' * (len(path) - 1) + f'{path[-1]}')
