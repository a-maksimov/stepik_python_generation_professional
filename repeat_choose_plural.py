def choose_plural(amount, declensions):
    if amount % 100 not in range(11, 19):
        if amount == 1 or amount % 10 == 1:
            return f'{amount} {declensions[0]}'
        elif amount in [2, 3, 4] or amount % 10 in [2, 3, 4]:
            return f'{amount} {declensions[1]}'
        else:
            return f'{amount} {declensions[2]}'
    else:
        return f'{amount} {declensions[2]}'


print(choose_plural(2, ('пример', 'примера', 'примеров')))

print(choose_plural(512312, ('цент', 'цента', 'центов')))
