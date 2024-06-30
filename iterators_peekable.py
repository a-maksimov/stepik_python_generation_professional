from itertools import tee


class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)

    def peek(self, *args, **kwargs):
        iterable, copy = tee(self.iterable)
        self.iterable = iterable
        if args:
            return next(copy, next(iter(args)))
        if 'default' in kwargs:
            return next(copy, kwargs.get('default'))
        return next(copy)


# SENTINEL = object()
#
#
# class Peekable:
#     def __init__(self, iterable):
#         self.iterator = iter(iterable)
#         self.cache = []
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.peek()
#         return self.cache.pop()
#
#     def peek(self, default=SENTINEL):
#         if not self.cache:
#             try:
#                 self.cache.append(next(self.iterator))
#             except StopIteration:
#                 if default is not SENTINEL:
#                     return default
#                 raise
#         return self.cache[0]

# iterator = Peekable('Python')
#
# print(next(iterator))
# print(iterator.peek())
# print(iterator.peek())
# print(next(iterator))
# print(iterator.peek())
# print(iterator.peek())


# TEST_4:
iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')

# TEST_4:
# Пустой итератор
# Пустой итератор
