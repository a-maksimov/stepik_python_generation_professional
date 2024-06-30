def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    elif not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    else:
        names.append(name)
        return len(names)


names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'


try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

