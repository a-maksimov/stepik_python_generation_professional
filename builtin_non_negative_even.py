def non_negative_even(numbers):
    return all(map(lambda num: True if num >= 0 and num % 2 == 0 else False, numbers))

print(non_negative_even([0, 2, 4, 8, 16]))
