# put your python code here

from collections import Counter

string = input().lower().split()
word_lens = Counter(list(map(len, string)))

for length, num in sorted(word_lens.items(), key=lambda l: l[1]):
    print(f'Слов длины {length}: {num}')