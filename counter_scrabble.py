from collections import Counter


def scrabble(symbols, word):
    if Counter(symbols.lower()) >= Counter(word.lower()):
        return True
    else:
        return False


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
