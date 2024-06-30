from datetime import date, timedelta


def years_days(year):
    start_date = date(year, 1, 1)
    yield from (start_date + timedelta(days=i) for i in range(366) if (start_date + timedelta(days=i)).year == year)


dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
