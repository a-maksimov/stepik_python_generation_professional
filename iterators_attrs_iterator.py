class AttrsIterator:
    def __init__(self, obj):
        self.attrs = obj.__dict__
        self.index = -1

    def __iter__(self):
        yield from self.attrs.items()

    def __next__(self):
        self.index += 1
        if self.index >= len(self.attrs):
            raise StopIteration
        return list(self.attrs.items())[self.index]


# TEST_3:
class Kemal:
    def __init__(self):
        self.family = 'cats'
        self.breed = 'british'
        self.master = 'Kemal'


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))

# ('family', 'cats')
# ('breed', 'british')
# ('master', 'Kemal')


# class AttrsIterator:
#     def __init__(self, obj):
#         self._obj = list(obj.__dict__.items())
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index >= len(self._obj):
#             raise StopIteration
#         return self._obj[self.index]

