from datetime import datetime, timedelta

date_format = '%d.%m.%Y'
input_date = datetime.strptime(input(), date_format).date()


def get_previous_and_next_date(date):
    one_day = timedelta(days=1)
    prev_date = date - one_day
    next_date = date + one_day
    return [prev_date, next_date]


print(*[d.strftime(date_format) for d in get_previous_and_next_date(input_date)], sep='\n')


# mask = '%d.%m.%Y'
# date = datetime.strptime(input(), mask)
# [print((date+timedelta(days=i)).strftime(mask)) for i in range(-1,2,2)]