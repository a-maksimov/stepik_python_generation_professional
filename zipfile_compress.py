from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    max_compress, max_compress_name = min(list(map(lambda f: ((f.compress_size/f.file_size), f.filename),
                                                   list(filter(lambda f: not f.is_dir(), info)))))

    print(max_compress_name.split('/')[-1])
