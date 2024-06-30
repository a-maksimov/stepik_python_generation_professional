from zipfile import ZipFile
from datetime import datetime

date = datetime.fromisoformat('2021-11-30 14:22:00')
pass
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    filtered_files = list(filter(lambda f: not f.is_dir() and datetime(*f.date_time) > date, info))

for file in sorted(filtered_files, key=lambda f: f.filename.split('/')[-1]):
    print(file.filename.split('/')[-1])