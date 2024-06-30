def primes(left, right):
    for i in range(left, right + 1):
        for j in range(2, i + 1):
            if i % j == 0 and j != i:
                prime = False
                break
        else:
            prime = True
        if prime and i != 1:
            yield i


generator = primes(1, 15)

print(*generator)
print(next(generator))
