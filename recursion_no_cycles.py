def no_cycles(number):
    print(number)
    if number <= 0:
        return None
    no_cycles(number - 5)
    print(number)


no_cycles(16)
