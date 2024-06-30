from itertools import chain


class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *args):
        juniors = map(lambda d: (d, 'junior'), args)
        self.juniors.extend(juniors)

    def add_senior(self, *args):
        seniors = map(lambda d: (d, 'senior'), args)
        self.seniors.extend(seniors)

    def __iter__(self):
        yield from chain(self.juniors, self.seniors)


# TEST_5:
smart_monkey = DevelopmentTeam()

smart_monkey.add_senior('Gvido', 'Alan')
smart_monkey.add_junior('Denis')

print(list(smart_monkey))

# [('Denis', 'junior'), ('Gvido', 'senior'), ('Alan', 'senior')]
