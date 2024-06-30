# n = int(input())
names = [input().strip('@beegeek.bzz') for _ in range(n)]

names_dict = {}
for name in names:
    name_alpha = ''.join([sym for sym in name if not sym.isdigit()])
    name_number = ''.join([sym for sym in name if sym.isdigit()])
    names_dict[name_alpha] = names_dict.get(name_alpha, [])
    # Если номер есть, то добавляем номер в список. Если номера нет, то добавляем в список 0
    if name_number.isdigit():
        names_dict[name_alpha].append(int(name_number))
    else:
        names_dict[name_alpha].append(0)


m = int(input())
new_names = [input() for _ in range(m)]

for new_name in new_names:
    if not names_dict.get(new_name, []):  # Если имени не существует в словаре
        index = ''  # Номера нет
        names_dict[new_name] = [0]  # При следующем попадании в списке будет 0, и можно будет выдать номер 1
    else:
        # Выдаем свободные номера от 0 до максимального занятого номера включительно + 1
        for i in range(0, max(names_dict[new_name]) + 2):
            if i not in names_dict[new_name]:  # Если число не занято
                names_dict[new_name].append(i)  # Добавляем его в список номеров
                index = '' if i == 0 else i
                break
    print(new_name + str(index) + '@beegeek.bzz')

# digits, names = '0123456789', []
#
# for _ in range(int(input())):
#     name, _ = input().split('@')
#     names.append(name)
#
# for _ in range(int(input())):
#     name = input()
#     counter = 1
#     while name in names:
#         name = name.rstrip(digits) + str(counter)
#         counter += 1
#     names.append(name)
#     print(f'{name}@beegeek.bzz')