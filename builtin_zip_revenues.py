names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

revenues = [(data[0], data[2] - data[1]) for data in zip(names, budgets, box_offices)]
for revenue in sorted(revenues):
    print(f'{revenue[0]}: {revenue[1]}$')