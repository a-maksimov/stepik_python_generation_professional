from datetime import datetime

date_format = '%d.%m.%Y'
input_dates = [datetime.strptime(d, date_format).date() for d in input().split()]


def get_list_of_deltas(list_of_dates):
    days = []
    for i in range(len(list_of_dates) - 1):
        days.append((list_of_dates[i + 1] - list_of_dates[i]).days)
    return [abs(day) for day in days]


print(get_list_of_deltas(input_dates))


# from datetime import datetime
#
# date_list = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), input().split()))
# print(list(map(lambda x, y: abs(x - y).days, date_list[1:], date_list[:-1])))