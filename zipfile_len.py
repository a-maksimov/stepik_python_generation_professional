from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    print(len(list(filter(lambda f: not f.is_dir(), info))))