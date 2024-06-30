import time
from datetime import date, timedelta
# from collections import Counter

t = time.perf_counter()

weekdays = set(range(7))
week_days_dict = {}

# week_days_dict = Counter((date.min + timedelta(days=i)).weekday() for i in range(12, (date.max - date.min).days)
#                          if (date.min + timedelta(days=i)).day == 13)
# TODO: skip a month
for date in (date.min + timedelta(days=i) for i in range(12, (date.max - date.min).days)
             if (date.min + timedelta(days=i)).day == 13):
    week_days_dict[date.weekday()] = week_days_dict.get(date.weekday(), 0) + 1

for day in sorted(week_days_dict.keys()):
    print(week_days_dict[day])

print(f"Время перебора:  {time.perf_counter() - t} с.")
