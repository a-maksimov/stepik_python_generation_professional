from datetime import date


def get_date_range(start, end):
    if start <= end:
        return [date.fromordinal(day) for day in range(start.toordinal(), end.toordinal() + 1)]
    return []


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    count = 0
    for date in get_date_range(start, end):
        if date.weekday() == 5:
            count += 1
    return count


# def saturdays_between_two_dates(start, end):
#     if start > end:
#         start, end = end, start
#
#     return sum(date.fromordinal(i).weekday() == 5 for i in range(start.toordinal(), end.toordinal() + 1))
