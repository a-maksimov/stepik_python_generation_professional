from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as file:
    content = file.read().lower()
    counter = Counter(content)

for character, number in sorted(counter.items()):
    if character.isalpha():
        print(f'{character}: {number}')