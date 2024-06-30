from datetime import date


def print_good_dates(dates):
    sorted_dates = sorted(dates)  # сначала сортировка объектов, потом форматирование
    print(*(date.strftime('%B %d, %Y') for date in sorted_dates if date.year == 1992 and date.day + date.month == 29),
          sep='\n')
