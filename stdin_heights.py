# put your python code here

import sys

heights = [int(line.strip()) for line in sys.stdin.readlines()]

if heights:
    print(f'Рост самого низкого ученика: {min(heights)}')
    print(f'Рост самого высокого ученика: {max(heights)}')
    print(f'Средний рост: {sum(heights) / len(heights)}')
else:
    print('нет учеников')