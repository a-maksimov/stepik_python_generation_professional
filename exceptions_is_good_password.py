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


# TEST_13:
try:
    print(is_good_password('123456789A'))
except Exception as err:
    print(type(err))
