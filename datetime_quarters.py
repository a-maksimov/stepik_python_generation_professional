from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

for date in dates:
    if date.month <= 3:
        q = '1'
    elif 3 < date.month <= 6:
        q = '2'
    elif 6 < date.month <= 9:
        q = '3'
    else:
        q = '4'
    print(f'{date.year}-Q{q}')

# for d in dates:
#     print(f'{d.year}-Q{(d.month - 1) // 3 + 1}')

# for date in dates:
# #     print(f'{date.year}-Q{"111222333444"[date.month-1]}')

# [print(f'{x.year}-Q{(x.month+2)//3}') for x in dates]