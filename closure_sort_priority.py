def sort_priority(values, group):
    gr_in_values = set(filter(lambda n: n in values, group))
    rest_values = set(values) - gr_in_values
    values[:] = sorted(gr_in_values) + sorted(rest_values)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)

# def sort_priority(numbers, group):
#     numbers.sort(key=lambda x: (x not in group, x))