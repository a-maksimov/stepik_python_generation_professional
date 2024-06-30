from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

groups = groupby(persons, key=lambda p: p.height)
groups = {k: v for group in groups for k, v in group}
groups.update({k: [person.name for person in v] for k, v in groups})
print(groups)
# print(*(f'{k}: ' ','.join(person.name for person in v) for k, v in groupby(persons, key=lambda p: p.height)), sep='\n')