from datetime import date, timedelta


def num_of_sundays(year):
    input_date = date(year, 1, 1)
    sunday = input_date + timedelta(days=6 - input_date.weekday())
    count = 0
    while sunday.year == input_date.year:
        count += 1
        sunday += timedelta(days=7)
    return count


# Количество воскресений в году равно номеру недели, начинающейся с воскресенья, для 31 декабря (%U)
# def num_of_sundays(year):
#     dt = datetime(year, 12, 31)
#     return int(dt.strftime('%U'))

print(num_of_sundays(2021))
