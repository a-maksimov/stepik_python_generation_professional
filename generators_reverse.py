def reverse(sequence):
    for item in sequence[::-1]:
        yield item


print(*reverse([1, 2, 3, 4, 5]))
