# put your python code here

import sys

lines = sys.stdin.readlines()
news = [line.split(' / ') for line in sorted(lines[:-1])]
category = lines[-1]

for title in sorted(news, key=lambda n: float(n[2].strip())):
    if title[1] == category:
        print(title[0])

# news = [i.strip().split(' / ') for i in sys.stdin]
# filtered = filter(lambda x: x[1] == news[-1][0], news[:-1])
#
# print(*(i[0] for i in sorted(filtered, key=lambda x: (float(x[2]), x[0]))), sep='\n')