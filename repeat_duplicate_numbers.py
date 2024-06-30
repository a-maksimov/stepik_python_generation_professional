numbers = [int(number) for number in input().split()]
numbers_set = set(numbers)

result = []

for number in numbers_set:
    count = numbers.count(number)
    if count > 1:
        result.append(number)

print(*sorted(result))

# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))

# nums = list(map(int, input().split()))
# print(*set(i for i in nums if nums.count(i) > 1))