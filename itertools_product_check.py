from string import ascii_lowercase
from itertools import product

letters = ascii_lowercase[:8]
digits = [1, 2, 3, 4, 5, 6, 7, 8]

print(*(k + str(v) for k, v in product(letters, digits)), sep=' ')