from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

time_format = '%H:%M'

total_seconds = list(map(lambda pair:
                         (datetime.strptime(pair[1], time_format) - datetime.strptime(pair[0],
                                                                                      time_format)).total_seconds(),
                         data))

print(int(sum(total_seconds) / 60))
