# def get_all_mondays(year):
#     from datetime import date, timedelta
#     return [date(year, 1, 1) + timedelta(days=i) for i in range(365)
#             if (date(year, 1, 1) + timedelta(days=i)).weekday() == 0]

def get_all_mondays(year):
    from calendar import weekday, monthrange
    from datetime import date
    return [date(year, month, day) for month in range(1, 13) for day in range(1, monthrange(year, month)[1] + 1)
            if weekday(year, month, day) == 0]


print(get_all_mondays(2021))
