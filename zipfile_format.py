from zipfile import ZipFile
from datetime import datetime

date_time_format = '%Y-%m-%d %H:%M:%S'

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    files = list(filter(lambda f: not f.is_dir(), info))

for file in sorted(files, key=lambda f: f.filename.split('/')[-1]):
    print(file.filename.split('/')[-1])
    print(f'  Дата модификации файла: {datetime(*file.date_time).strftime(date_time_format)}')
    print(f'  Объем исходного файла: {file.file_size} байт(а)')
    print(f'  Объем сжатого файла: {file.compress_size} байт(а)')
    print()