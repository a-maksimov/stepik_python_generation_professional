class Xrange:
    def __init__(self, start, stop, step: [int, float] = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.result = self.start

    def __iter__(self):
        return self

    def __next__(self):
        self.start = self.result
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
        else:
            if self.start <= self.stop:
                raise StopIteration
        self.result += self.step
        return self.start


xrange = Xrange(10, 1, -1)

print(*xrange)