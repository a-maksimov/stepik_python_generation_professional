from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    file_size_sum = sum(list(map(lambda f: f.file_size, list(filter(lambda f: not f.is_dir(), info)))))
    compressed_file_size_sum = sum(list(map(lambda f: f.compress_size, list(filter(lambda f: not f.is_dir(), info)))))

    print(f'Объем исходных файлов: {file_size_sum} байт(а)')
    print(f'Объем сжатых файлов: {compressed_file_size_sum} байт(а)')
