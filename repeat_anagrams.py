def filter_anagrams(word, words):
    anagrams = []
    for test_word in words:
        if all(map(lambda sym: word.count(sym) == test_word.count(sym), word)) and len(word) == len(test_word):
            anagrams.append(test_word)
    return anagrams


# def filter_anagrams(word, anagrams):
#     return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]


word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))




