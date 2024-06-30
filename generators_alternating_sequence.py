def alternating_sequence(count=None):
    if not count:
        count = 1
        while True:
            yield -count if count % 2 == 0 else count
            count += 1
    else:
        for i in range(1, count + 1):
            yield -i if i % 2 == 0 else i


generator = alternating_sequence()

print(next(generator))
print(next(generator))

generator = alternating_sequence(10)

print(*generator)
