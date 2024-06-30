def is_power(number):
    if number < 1:
        return False
    elif number == 1:
        return True
    else:
        return is_power(number / 2)