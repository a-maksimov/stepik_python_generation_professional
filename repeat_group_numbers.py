n = int(input())

def digit_sum(number: int):
    """
    Returns sum of digits of a number
    """
    return sum([int(sym) for sym in str(number)])


numbers = [number for number in range(1, n + 1)]

number_sums = set(map(lambda num: digit_sum(num), numbers))

groups = {}

for number_sum in number_sums:
    groups[number_sum] = []
    for number in numbers:
        if digit_sum(number) == number_sum:
            groups[number_sum].append(number)

print(max([len(numlist) for numlist in groups.values()]))

# data = {}
# for i in range(1, int(input()) + 1):
#     sum_of_digits = sum(map(lambda d: int(d), str(i)))
#     data[sum_of_digits] = data.get(sum_of_digits, 0) + 1
#
# print(max(data.values()))