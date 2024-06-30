def polynom(x):
    res = x ** 2 + 1
    if 'values' not in polynom.__dict__:
        polynom.values = set()
    polynom.values.add(res)
    return res


for _ in range(10):
    polynom(10)

print(polynom.values)