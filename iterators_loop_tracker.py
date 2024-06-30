from itertools import tee


class LoopTracker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.iterable, copy = tee(self.iterable)

        try:
            self._first = next(copy)
        except StopIteration:
            self._first = None

        self._accesses = 0
        self._empty_accesses = 0
        self._last = None

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._first is None:
            raise AttributeError('Исходный итерируемый объект пуст')
        return self._first

    @property
    def last(self):
        if not self._last:
            raise AttributeError('Последнего элемента нет')
        return self._last

    def is_empty(self):
        self.iterable, copy = tee(self.iterable)
        try:
            next(copy)
        except StopIteration:
            return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._last = next(self.iterable)
            self._accesses += 1
            return self._last
        except StopIteration:
            self._empty_accesses += 1
            raise StopIteration


# loop_tracker = LoopTracker([1, 2, 3])
# print(loop_tracker.first)
#
# print(next(loop_tracker))
# print(loop_tracker.first)
#
# print(next(loop_tracker))
# print(loop_tracker.first)
#
# print(next(loop_tracker))
# print(loop_tracker.first)

# TEST_11:
loop_tracker = LoopTracker(range(1_000))

for _ in range(100_000):
    next(loop_tracker, None)

print(loop_tracker.accesses)
print(loop_tracker.empty_accesses)

# TEST_11:
# 1000
# 99000