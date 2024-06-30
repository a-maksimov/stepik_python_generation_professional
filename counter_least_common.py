# put your python code here

from collections import Counter


string = input().lower()
words = Counter(string.split()).most_common()
min_value = words[-1][1]

words_filtered = list(filter(lambda w: w[1] == min_value, words))

print(', '.join(word[0] for word in sorted(words_filtered)))
