import csv
from collections import Counter

with open('data.csv', 'r', encoding='utf-8') as file_read, \
        open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_write:
    rows = list(csv.reader(file_read))
    del rows[0]
    domains = Counter([row[2].split('@')[-1] for row in rows])
    columns = ['domain', 'count']
    data_write = [{columns[0]: domain_name, columns[1]: domain_count} for domain_name, domain_count in sorted(domains.items())]
    writer = csv.DictWriter(file_write, fieldnames=columns)
    writer.writeheader()
    for row in sorted(data_write, key=lambda d: d.get('count')):
        writer.writerow(row)
