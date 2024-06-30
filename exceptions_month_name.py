import calendar

months_dict = dict(zip(range(1, 13), list(calendar.month_name)[1:]))

try:
    n = int(input())
    print(months_dict[n])
except KeyError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
