from calendar import monthrange
from datetime import datetime

date_format = '%Y %B'  # %B -- full month name
input_date = datetime.strptime(input(), date_format)

print(monthrange(input_date.year, input_date.month)[1])