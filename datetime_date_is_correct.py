from datetime import date


def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))
    except ValueError:
        return False
    return True
