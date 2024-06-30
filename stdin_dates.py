# put your python code here

import sys
from datetime import datetime

dates_list = sorted([datetime.fromisoformat(line.strip()) for line in sys.stdin])
print((dates_list[-1] - dates_list[0]).days)