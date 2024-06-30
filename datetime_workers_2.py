from datetime import datetime

date_format = '%d.%m.%Y'
n = int(input())
dates = {}
for firstname, lastname, date in [input().split() for _ in range(n)]:
    key = datetime.strptime(date, date_format).date()  # key -- birthday
    dates[key] = dates.get(key, []) + [' '.join([firstname, lastname])]  # value -- list of workers

max_date = max(dates, key=lambda date: len(dates.get(date)))
for date in sorted(dates):
    if len(dates.get(date)) == len(dates.get(max_date)):
        print(date.strftime(date_format))

