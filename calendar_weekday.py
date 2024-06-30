import calendar
from datetime import datetime

input_date = datetime.fromisoformat(input())

weekdays = list(calendar.day_name)

print(weekdays[input_date.weekday()])