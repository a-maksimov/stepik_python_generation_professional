# put your python code here

import sys

results = []
for line in sys.stdin:
    results.append(eval(line))
print(max(results))