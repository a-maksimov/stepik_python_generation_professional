def dict_travel(nested_dicts):
    string = ''
    counter = 0

    def find_value(nested_dicts, string, counter):
        for key in sorted(nested_dicts.keys()):
            string += key
            if not isinstance(nested_dicts[key], dict):
                string += f': {nested_dicts[key]}'
                print(string.strip('.'))
                string = string.replace(f'{key}: {nested_dicts[key]}', '')
            else:
                counter += 1
                find_value(nested_dicts[key], string + '.', counter)
                string_list = string.split('.')[:-(counter - 1)]
                string = ('.'.join(string_list) + '.')

    return find_value(nested_dicts, string, counter)


data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
dict_travel(data)
print()
data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
dict_travel(data)
print()
data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}
dict_travel(data)

