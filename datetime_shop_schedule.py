from datetime import datetime, timedelta

schedule = {
    0: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    1: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    2: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    3: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    4: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    5: {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    6: {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }

datetime_format = '%d.%m.%Y %H:%M'
input_datetime = datetime.strptime(input(), datetime_format)
input_day = input_datetime.weekday()
input_hours, input_minutes = input_datetime.hour, input_datetime.minute
input_timedelta = timedelta(hours=input_hours, minutes=input_minutes)
open_seconds = (schedule[input_day]['end'] - schedule[input_day]['start']).total_seconds()
closing_seconds = (schedule[input_day]['end'] - input_timedelta).total_seconds()
print(round(closing_seconds / 60) if 0 < closing_seconds <= open_seconds else 'Магазин не работает')

# from datetime import datetime
# date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
#
# start, end = (date.replace(hour=i, minute=0) for i in ((9, 21), (10, 18))[date.weekday() > 4])
#
# if start <= date < end:
#     print((end - date).seconds // 60)
# else:
#     print('Магазин не работает')


