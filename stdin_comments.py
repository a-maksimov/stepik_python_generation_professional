# put your python code here

import sys

print(len([line.strip() for line in sys.stdin.readlines() if not line.strip().split('#')[0]]))

# print(sum(1 for row in stdin if row.lstrip().startswith('#')))