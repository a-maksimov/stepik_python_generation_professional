def simple_sequence():
    index = 1
    while True:
        for _ in range(1, index + 1):
            yield index
        index += 1

generator = simple_sequence()

print(next(generator))
print(next(generator))