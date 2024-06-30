import json
from datetime import datetime


def select_by_parameter(sequence, parameter):
    sequence_max = max(sequence, key=lambda p: int(p['DimensionsSummer'][parameter]))
    return list(
        filter(lambda p: int(p['DimensionsSummer'][parameter]) == int(sequence_max['DimensionsSummer'][parameter]),
               sequence))


time_format = '%H:%M'
select_start, select_close = map(lambda t: datetime.strptime(t, time_format), ['10:00', '12:00'])

with open('pools.json', 'r', encoding='utf-8') as file:
    pools = json.load(file)

selected_pools = []
for pool in pools:
    start, close = (datetime.strptime(time, time_format) for time in pool['WorkingHoursSummer']['Понедельник'].split('-'))
    if start <= select_start and close >= close:
        selected_pools.append(pool)

dimensions = ['Length', 'Width']
for dimension in dimensions:
    selected_pools = select_by_parameter(selected_pools, dimension)

for pool in selected_pools:
    print(f'{pool["DimensionsSummer"]["Length"]}x{pool["DimensionsSummer"]["Width"]}')
    print(f'{pool["Address"]}')