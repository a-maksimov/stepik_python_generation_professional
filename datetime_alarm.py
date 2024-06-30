from datetime import datetime, timedelta

time_format = '%H:%M:%S'


def get_alarm_time(time, seconds):
    return time + timedelta(seconds=seconds)


print(get_alarm_time(datetime.strptime(input(), time_format), int(input())).strftime(time_format))

# mask = '%d.%m.%Y'
# date = datetime.strptime(input(), mask)
# [print((date+timedelta(days=i)).strftime(mask)) for i in range(-1,2,2)]
