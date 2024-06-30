def my_pow(number):
    return sum([int(pair[1]) ** (pair[0] + 1) for pair in enumerate(list(str(number)))])

print(my_pow(139))
