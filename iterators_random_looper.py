from itertools import chain
from random import shuffle


class RandomLooper:
    def __init__(self, *args):
        self.iterable = list(chain(*args))
        shuffle(self.iterable)
        self.iterable = iter(self.iterable)

    def __iter__(self):
        yield from self.iterable

    def __next__(self):
        return next(self.iterable)
