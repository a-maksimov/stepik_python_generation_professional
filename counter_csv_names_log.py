import csv
from collections import Counter

with open('name_log_1.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')
    email_counter = Counter([row['email'] for row in rows])

for email, num in sorted(email_counter.items()):
    print(f'{email}: {num}')