# put your python code here

from datetime import date


def is_correct(day: int, month: int, year: int):
    try:
        date(year, month, day)
    except ValueError:
        return False
    return True


counter = 0
input_date = input()
while input_date != 'end':
    if is_correct(*map(int, input_date.split('.'))):
        print('Корректная')
        counter += 1
    else:
        print('Некорректная')
    input_date = input()
print(counter)
