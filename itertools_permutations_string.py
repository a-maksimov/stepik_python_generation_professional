# put your python code here
from itertools import permutations

string = input()

print(*(''.join(item) for item in sorted(set(permutations(string)))), sep='\n')
