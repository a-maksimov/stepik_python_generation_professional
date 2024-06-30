from collections import defaultdict

defaultdict(int, name='Timur', surname='Guev', hobby='math')
defaultdict(name='Timur', surname='Guev', hobby='math')
defaultdict(int, {'name': 'Timur', 'surname': 'Guev', 'hobby': 'math'})
defaultdict()
defaultdict(list)
defaultdict(int, [('name', 'Timur'), ('surname', 'Guev'), ('hobby', 'math')])
# defaultdict({'name': 'Timur', 'surname': 'Guev', 'hobby': 'math'})
defaultdict(None)
defaultdict.fromkeys(['name', 'surname', 'hobby'], None)