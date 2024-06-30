from datetime import datetime, timedelta

date_format = '%d.%m.%Y'
input_date = datetime.strptime(input(), date_format).date()


def get_dates(date):
    dates = [date]
    for i in range(2, 11):
        date += timedelta(days=i)
        dates.append(date)
    return dates


print(*[d.strftime(date_format) for d in get_dates(input_date)], sep='\n')
