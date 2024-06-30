# put your python code here

from collections import Counter

string = input().lower()
words = Counter(string.split()).most_common()
max_value = words[0][1]

words_filtered = list(filter(lambda w: w[1] == max_value, words))
word = max(words_filtered)

print(word[0])