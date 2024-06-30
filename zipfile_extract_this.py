from zipfile import ZipFile


def extract_this(filename, *args):
    with ZipFile(filename, mode='r') as zip_file:
        if not args:
            zip_file.extractall()
        else:
            [zip_file.extract(x) for x in args]
