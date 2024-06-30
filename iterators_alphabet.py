class Alphabet:
    def __init__(self, language):
        self.language = language
        self.alphabet = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.alphabet[self.language][self.index % len(self.alphabet[self.language])]


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
