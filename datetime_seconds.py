from datetime import timedelta

hours, minutes, seconds = (int(x) for x in input().split(':'))

print(round(timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()))
