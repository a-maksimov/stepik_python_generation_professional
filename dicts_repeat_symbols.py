# put your python code here

import string

eng_alpha = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

symbols = input()

mydict = {}
for symbol, letter in zip(symbols, eng_alpha):
    mydict[letter] = symbol

for c in input().lower():
    print(mydict[c] if c in mydict else c, end='')

# translator = str.maketrans(ascii_letters, input() * 2)
#
# print(input().translate(translator))

