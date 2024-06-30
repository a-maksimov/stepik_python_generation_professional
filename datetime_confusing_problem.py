from datetime import datetime, timedelta

date_format = '%d.%m.%Y'

start, end = (datetime.strptime(input(), date_format).date() for _ in range(2))

while (start.day + start.month) % 2 == 0:
    start += timedelta(days=1)

dates_list = [start + timedelta(days=i) for i in range(0, (end - start).days + 1, 3)
              if (start + timedelta(days=i)).weekday() not in (0, 3)
              and (start + timedelta(days=i)).day + (start + timedelta(days=i)).month % 2 != 0]

for d in dates_list:
    print(d.strftime(date_format))
