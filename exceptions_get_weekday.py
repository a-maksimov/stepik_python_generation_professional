import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru-RU')


def get_weekday(number):
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if number < 1 or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return calendar.day_name[number - 1].title()


print(get_weekday(0))