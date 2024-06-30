def spell(*args):
    if args:
        words = [arg.lower() for arg in args]
        letters = set(map(lambda word: word.lower()[0], words))
        letter_dict = {}
        for letter in letters:
            words_startswith = list(filter(lambda word: word.startswith(letter), words))
            letter_dict[letter] = len(max(words_startswith, key=len))
        return letter_dict
    return {}

# def spell(*args):
#     return {str.lower(item[0]): len(item) for item in sorted(args, key=len)}

words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
