import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if string.lower() == string or string.upper() == string:
        raise LetterError
    if string.isalpha():
        raise DigitError
    return True


# lines = sys.stdin.readlines()
# Если будете итерироваться через sys.stdin, то при вызове функции не забывайте к  итерируемому элементу применять .strip()
lines = ['arr1', 'Arrrrrrrrrrr', 'arrrrrrrrrrrrrrr1', 'Arrrrrrr1']
for i in range(len(lines)):
    string = lines[i]
    try:
        is_good_password(string)
        print('Success!')
        break
    except LengthError:
        print('LengthError')
    except LetterError:
        print('LetterError')
    except DigitError:
        print('DigitError')

    # except Exception as err:
    #     print(err)