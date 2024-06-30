from datetime import datetime, timedelta

time_format = '%H:%M'
start = datetime.strptime(input(), time_format)
end = datetime.strptime(input(), time_format)
worktime = end - start
class_time = 45  # minutes
break_time = 10  # minutes
count = worktime // timedelta(minutes=class_time)
schedule = [(start + timedelta(minutes=i), start + timedelta(minutes=i + class_time))
            for i in range(0, class_time * count + 1, class_time + break_time)
            if start + timedelta(minutes=i + class_time) <= end]
for class_start, class_end in schedule:
    print(f'{class_start.strftime(time_format)} - {class_end.strftime(time_format)}')
