from datetime import datetime, date

date_format = '%d.%m.%Y'
input_date = datetime.strptime(input(), date_format).date()
n = int(input())
dates = {}
for firstname, lastname, birthday in [input().split() for _ in range(n)]:
    key = datetime.strptime(birthday, date_format).date()  # key -- birthday
    # учитываем новый год
    if 0 < (date(1, key.month, key.day) - date(1, input_date.month, input_date.day)).days <= 7 \
            or (date(1, key.month, key.day) - date(1, input_date.month, input_date.day)).days + 365 <= 7:
        dates[key] = ' '.join([firstname, lastname])  # value -- worker

print(dates.get(max(dates)) if dates else 'Дни рождения не планируются')

# 29.12.2021
# 4
# Иван Петров 30.12.1995
# Петр Сергеев 04.01.1997
# Сергей Романов 03.01.1994
# Маша Иванова 31.12.1996

# 14.11.2021
# 3
# Иван Петров 16.11.1995
# Петр Сергеев 14.11.1997
# Сергей Романов 17.11.1994