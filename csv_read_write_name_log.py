import csv
from datetime import datetime

datetime_format = '%d/%m/%Y %H:%M'

with open('name_log.csv', 'r', encoding='utf-8') as file_read, \
        open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file_write:
    rows_dict = csv.DictReader(file_read)
    rows = list(rows_dict)
    emails = set(row['email'] for row in rows)
    writer = csv.DictWriter(file_write, fieldnames=rows_dict.fieldnames)
    writer.writeheader()
    for email in sorted(emails):
        latest_log = max(list(filter(lambda row: row['email'] == email, rows)),
                         key=lambda row: datetime.strptime(row['dtime'], datetime_format))
        writer.writerow(latest_log)

# header, *rows = csv.reader(f)
