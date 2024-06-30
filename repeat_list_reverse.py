ls = [int(num) for num in input().split()]
n = ls[0]
x, y = ls[1:3]
a, b = ls[3:5]

numbers = list(range(1, n + 1))
numlist1 = numbers[x - 1:y]
numlist1.reverse()
numbers = numbers[:x - 1] + numlist1 + numbers[y:]
numlist2 = numbers[a - 1:b]
numlist2.reverse()
numbers = numbers[:a - 1] + numlist2 + numbers[b:]
print(*numbers)

# n, x, y, a, b = [int(i) for i in input().split()]
# nums = list(range(1, n + 1))
#
# nums[x - 1:y] = reversed(nums[x - 1:y])
# nums[a - 1:b] = reversed(nums[a - 1:b])
#
# print(*nums)