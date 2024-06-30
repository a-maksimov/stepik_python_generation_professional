vowels = 'ауоыиэяюёе'


def letters_to_zeroes_and_ones(word):
    for sym in word:
        if sym in vowels:
            word = word.replace(sym, '1')
        else:
            word = word.replace(sym, '0')
    word = word.rstrip('0')
    return word


word = input()
word_mapped = letters_to_zeroes_and_ones(word)
n = int(input())

for _ in range(n):
    test_word = input()
    test_word_mapped = letters_to_zeroes_and_ones(test_word)
    if test_word_mapped == word_mapped:
        print(test_word)
