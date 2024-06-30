# put your python code here

import sys

nums_list = [int(line.strip()) for line in sys.stdin]
# nums_list = [1, 9, 1, 1, 4, 5]

a = nums_list[1] - nums_list[0]
g = nums_list[1] // nums_list[0]

range_1 = range(len(nums_list))
range_2 = range(1, len(nums_list))
ranges = list(zip(range_1, range_2))

# TODO: зачем проверять все данные, если можно остановиться на 3 вводе?
ariph_boolean = all(list(map(lambda pair: nums_list[pair[1]] - nums_list[pair[0]] == a, ranges)))
geom_boolean = all(list(map(lambda pair: nums_list[pair[1]] // nums_list[pair[0]] == g, ranges)))

if ariph_boolean:
     print('Арифметическая прогрессия')
elif geom_boolean:
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')