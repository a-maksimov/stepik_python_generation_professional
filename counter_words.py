from collections import Counter


def count_occurences(word, words):
    word_counter = Counter(words.lower().split())
    return word_counter[word.lower()]

word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))