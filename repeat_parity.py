def same_parity(numbers):
    if numbers:
        if numbers[0] % 2 == 0:
            return list(filter(lambda number: number % 2 == 0, numbers))
        else:
            return list(filter(lambda number: number % 2 != 0, numbers))
    else:
        return []

# def same_parity(nums):
#     return [i for i in nums if i % 2 == nums[0] % 2]