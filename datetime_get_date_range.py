from datetime import date


def get_date_range(start, end):
    if start <= end:
        return [date.fromordinal(day) for day in range(start.toordinal(), end.toordinal() + 1)]
    return []


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')
