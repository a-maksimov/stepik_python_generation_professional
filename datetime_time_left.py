from datetime import datetime, date

datetime_format = '%d.%m.%Y %H:%M'


def choose_plural(amount, declensions):
    if amount % 100 not in range(11, 19):
        if amount == 1 or amount % 10 == 1:
            return f'{amount} {declensions[0]}'
        elif amount in [2, 3, 4] or amount % 10 in [2, 3, 4]:
            return f'{amount} {declensions[1]}'
        else:
            return f'{amount} {declensions[2]}'
    else:
        return f'{amount} {declensions[2]}'


release_date = datetime.strptime('08.11.2022 12:00', datetime_format)
input_date = datetime.strptime(input(), datetime_format)
if release_date <= input_date:
    print('Курс уже вышел!')
else:
    time_before_release = release_date - input_date
    hours = time_before_release.seconds // 3600
    if time_before_release.days > 0:
        if time_before_release.seconds > 0:
            print(f'До выхода курса осталось: {choose_plural(time_before_release.days, ["день", "дня", "дней"])} '
                  f'и {choose_plural(hours, ["час", "часа", "часов"])}')
        else:
            print(f'До выхода курса осталось: {choose_plural(time_before_release.days, ["день", "дня", "дней"])}')
    else:
        minutes = (time_before_release.seconds // 60) % 60
        if hours > 0 and minutes > 0:
            print(f'До выхода курса осталось: {choose_plural(hours, ["час", "часа", "часов"])} '
                  f'и {choose_plural(minutes, ["минута", "минуты", "минут"])}')
        elif hours > 0 and minutes == 0:
            print(f'До выхода курса осталось: {choose_plural(hours, ["час", "часа", "часов"])}')
        else:
            print(f'До выхода курса осталось: {choose_plural(minutes, ["минута", "минуты", "минут"])}')
