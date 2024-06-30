from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.max_values = lambda: list(filter(lambda d: d[1] == data.most_common()[0][1], data.most_common()))

data.min_values = lambda: list(filter(lambda d: d[1] == data.most_common()[-1][1], data.most_common()))

print(data.max_values())
print(data.min_values())


# data.min_values = lambda reverse=False: sorted(data.values(), reverse=reverse)