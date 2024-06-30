import sys

game = [(pair[0], int(pair[1].strip())) for pair in enumerate(sys.stdin.readlines())]

if game[-1][0] % 2 == 0:
    if game[-1][1] % 2 == 0:
        print('Анри')
    else:
        print('Дима')
else:
    if game[-1][1] % 2 == 0:
        print('Дима')
    else:
        print('Анри')


# s = tuple(int(i.strip()) for i in sys.stdin.readlines())
# print(('Дима', 'Анри')[(len(s) - 1) % 2 == s[-1] % 2])