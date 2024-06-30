class SkipIterator:
    def __init__(self, iterable, n):
        iterable = list(iterable)
        self.iterable = [iterable[i] for i in range(0, len(iterable), n + 1)]
        self.index = -1

    def __iter__(self):
        yield from self.iterable

    def __next__(self):
        self.index += 1
        if self.index >= len(self.iterable):
            raise StopIteration
        item = self.iterable[self.index]
        return item
    
# class SkipIterator:
#     def __init__(self, iterable, n):
#         self.iterable = iter(iterable)
#         self.n = n
#         self.first = True
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.first:
#             self.first = False
#             return next(self.iterable)
#         for _ in range(self.n):
#             next(self.iterable)
#         return next(self.iterable)


# skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)  # пропускаем по одному элементу
#
# print(*skipiterator)
#
# skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента
#
# print(*skipiterator)

# TEST_10:
skipiterator = SkipIterator(range(1000), 7)

for _ in range(25):
    next(skipiterator)

print(next(skipiterator))
print(next(skipiterator))
print(next(skipiterator))

# TEST_10:
# 200
# 208
# 216
