def palindromes():
    start = 1
    yield start
    while True:
        start += 1
        if str(start) == str(start)[::-1]:
            yield start


generator = palindromes()

print(next(generator))
print(next(generator))
print(next(generator))

print()

generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)
