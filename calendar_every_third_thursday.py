from calendar import weekday, monthrange
from datetime import date

date_format = '%d.%m.%Y'


def get_all_third_thursdays(year):
    return [[date(year, month, day) for day in range(1, monthrange(year, month)[1] + 1) if weekday(year, month, day) == 3][2]
            for month in range(1, 13)]


for thursday in get_all_third_thursdays(int(input())):
    print(thursday.strftime(date_format))

# третий четверг в любом случае будет между 15 и 21 числом...