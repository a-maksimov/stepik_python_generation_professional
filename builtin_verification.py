import string


def verification(login, password, success, failure):
    set_latin_letters = set(string.ascii_lowercase + string.ascii_uppercase)
    if set(password).isdisjoint(set_latin_letters):
        failure(login, 'в пароле нет ни одной буквы')
    elif set(password).isdisjoint(set(string.ascii_uppercase)):
        failure(login, 'в пароле нет ни одной заглавной буквы')
    elif set(password).isdisjoint(set(string.ascii_lowercase)):
        failure(login, 'в пароле нет ни одной строчной буквы')
    elif set(password).isdisjoint(set('123456789')):
        failure(login, 'в пароле нет ни одной цифры')
    else:
        success(login)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'HELLO_WORLD', success, failure)
