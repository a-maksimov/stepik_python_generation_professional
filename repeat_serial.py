n = int(input())

persons = [input().split(', ') for _ in range(n)]

language_set = set()

for person in persons:
    for language in person:
        language_set.add(language)

languages = []

for language in language_set:
    if all(map(lambda language_list: language in language_list, persons)):
        languages.append(language)

if languages:
    print(', '.join(sorted(languages)))
else:
    print('Сериал снять не удастся')

# n = int(input())
# langs = set(input().split(', '))
#
# for _ in range(n - 1): langs &= set(input().split(', ')) находим пересечение с новым каждым новым множеством и
# обновляем исходное множество
#
# if langs:
#     print(*sorted(langs), sep=', ')
# else:
#     print('Фильм снять не удастся')