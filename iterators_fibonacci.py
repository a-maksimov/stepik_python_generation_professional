class Fibonacci:
    def __init__(self):
        self.result = 1
        self.a = 1
        self.b = 1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < 2:
            return self.result
        result = self.a + self.b
        self.a = self.b
        self.b = result
        return result


fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
