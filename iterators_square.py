class Square:
    def __init__(self, n):
        self.times = n
        self.index = -1
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.times:
            raise StopIteration
        self.square = self.number ** 2
        self.number += 1
        return self.square


squares = Square(2)

print(next(squares))
print(next(squares))
