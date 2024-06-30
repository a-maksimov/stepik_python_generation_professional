import csv


def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        columns = {}
        for row in rows:
            for column in row:
                columns.setdefault(column, []).append(row[column])
    return columns

csv_columns('exam.csv')
