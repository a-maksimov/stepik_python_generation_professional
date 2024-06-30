def index_of_nearest(numbers, number):
    if numbers:
        diff_numbers = list(map(lambda num: abs(number - num), numbers))
        return diff_numbers.index(min(diff_numbers))
    return -1
