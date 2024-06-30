def fill_up_missing_dates(dates):
    from datetime import datetime, timedelta
    date_format = '%d.%m.%Y'
    dates = sorted([datetime.strptime(d, date_format).date() for d in dates])
    filled_dates = []
    for i in range(len(dates) - 1):
        delta_days = (dates[i + 1] - dates[i]).days
        if delta_days > 1:
            insert_dates = []
            for j in range(delta_days):
                insert_dates.append(dates[i] + timedelta(days=j))
            filled_dates.extend(insert_dates)
        else:
            filled_dates.append(dates[i])
    filled_dates.append(dates[-1])
    return [date.strftime(date_format) for date in filled_dates]


# для решения достаточно минимальной и максимальной даты их входного списка
# def fill_up_missing_dates(dates):
#     pattern = '%d.%m.%Y'
#     dates = [datetime.strptime(d, pattern) for d in dates]
#     start, end = min(dates), max(dates)
#     days = (end - start).days
#     return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]

# def fill_up_missing_dates(l, pat='%d.%m.%Y'):
#     l = list(map(lambda x: datetime.strptime(x, pat), l))
#     return [datetime.strftime(min(l) + timedelta(days=i), pat) for i in range((max(l) - min(l)).days + 1)]

dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))
