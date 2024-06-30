from datetime import date, datetime


def is_available_date(booked_dates, date_for_booking):
    date_format = '%d.%m.%Y'
    booked_dates_set = set()

    def get_date_range(start, end):
        return [date.fromordinal(start.toordinal() + day) for day in range(end.toordinal() - start.toordinal() + 1)]

    for d in booked_dates:
        if '-' not in d:
            booked_dates_set.add(datetime.strptime(d, date_format).date())
        else:
            s, e = (datetime.strptime(day, date_format) for day in d.split('-'))
            booked_dates_set.update(get_date_range(s, e))

    dates_for_booking_set = set()
    if '-' not in date_for_booking:
        dates_for_booking_set.add(datetime.strptime(date_for_booking, date_format).date())
    else:
        s, e = (datetime.strptime(day, date_format) for day in date_for_booking.split('-'))
        dates_for_booking_set.update(get_date_range(s, e))

    if not dates_for_booking_set.intersection(booked_dates_set):
        return True
    return False


# def is_available_date(booked_dates, date_for_booking):
#     date_for_booking = list(map(lambda dt: datetime.strptime(dt, '%d.%m.%Y'), date_for_booking.split('-')))
#     booked_dates = [list(map(lambda dt: datetime.strptime(dt, '%d.%m.%Y'), date.split('-'))) for date in booked_dates]
#
#     for date in booked_dates:
#         if not (date_for_booking[-1] < date[0] or date_for_booking[0] > date[-1]):
#             return False
#     return True

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))