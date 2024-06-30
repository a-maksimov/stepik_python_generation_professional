class DictItemsIterator:
    def __init__(self, data):
        self.data = list(data.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

pairs = DictItemsIterator(data)

print(tuple(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')
