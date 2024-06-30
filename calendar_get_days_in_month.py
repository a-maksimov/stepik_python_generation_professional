def get_days_in_month(year, month):
    from calendar import month_name, monthrange
    from datetime import date, timedelta
    month_num = list(month_name).index(month)
    input_date = date(year, month_num, 1)
    num_of_days = monthrange(year, month_num)[1]
    return [input_date + timedelta(days=i) for i in range(num_of_days)]


# def get_days_in_month(year, month):
#     month = list(calendar.month_name).index(month)
#     return [date(year, month, day) for day in range(1, calendar.monthrange(year, month)[1] + 1)]

print(get_days_in_month(2021, 'December'))
