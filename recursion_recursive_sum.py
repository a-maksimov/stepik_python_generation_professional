def recursive_sum(a, b):
    if b == 0:
        return a
    else:
        return recursive_sum(a + 1, b - 1)


a = 10
b = 22
print(recursive_sum(a, b))
