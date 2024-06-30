ru_letters = 'АаВСсЕеНКМОоРрТХху'
ru_count = 0
for _ in range(3):
    letter = input()
    if letter in ru_letters:
        ru_count += 1
if ru_count == 3:
    print('ru')
elif ru_count == 0:
    print('en')
else:
    print('mix')


# langs = ['ru', 'mix', 'mix', 'en']
# eng = 'AaBCcEeHKMOoPpTXxy'
# ind = sum(input() in eng for _ in range(3))
# print(langs[ind])
