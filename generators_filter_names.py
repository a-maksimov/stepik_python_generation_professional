def filter_names(names, ignore_char, max_names):
    numbers = set('0123456789')
    filtered_names = filter(
        lambda name: not name.lower().startswith(ignore_char.lower()) and not set(name).intersection(numbers),
        names
    )
    for _ in range(max_names):
        try:
            yield next(filtered_names)
        except StopIteration:
            return

# TEST_10:
data = ['1Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', 'Ruslan']

print(*filter_names(data, 'A', 100))

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))