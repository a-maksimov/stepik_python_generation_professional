from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

persons = sorted(persons, key=lambda p: p.height)

groupby_height = groupby(persons, key=lambda p: p.height)

for height, group in groupby_height:
    print(f'{height}:', ', '.join(sorted((p.name for p in group))))
