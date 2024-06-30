from datetime import datetime

date_format = '%d.%m.%Y'
n = int(input())
workers = {}
for firstname, lastname, date in [input().split() for _ in range(n)]:
    key = datetime.strptime(date, date_format).date()  # key -- birthday
    workers[key] = workers.get(key, []) + [' '.join([firstname, lastname])]  # value -- list of workers

if len(workers.get(min(workers))) == 1:
    print(min(workers).strftime(date_format), *workers.get(min(workers)))
else:
    print(min(workers).strftime(date_format), len(workers.get(min(workers))))
