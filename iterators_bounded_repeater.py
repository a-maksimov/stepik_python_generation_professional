class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.times:
            raise StopIteration
        return self.obj
