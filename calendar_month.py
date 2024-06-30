import calendar
from datetime import datetime

date_format = '%Y %b'  # %b -- abbr of month name
input_date = datetime.strptime(input(), date_format)

print(calendar.month(input_date.year, input_date.month))
