def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res

    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))


add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
