# put your python code here

import sys
from datetime import datetime

date_format = '%d.%m.%Y'

# dates_list = [datetime.strptime(line.strip(), date_format) for line in sys.stdin]

dates_list = [datetime.strptime(input(), date_format) for _ in range(3)]

if len(set(dates_list)) != len(dates_list):
    print('MIX')
elif dates_list == sorted(dates_list):
    print('ASC')
elif dates_list == sorted(dates_list, reverse=True):
    print('DESC')
else:
    print('MIX')
