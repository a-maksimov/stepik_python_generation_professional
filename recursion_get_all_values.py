def get_all_values(nested_dicts, key):
    result = set()
    for k in nested_dicts:
        if isinstance(nested_dicts[k], dict):
            values = get_all_values(nested_dicts[k], key)
            result.update(values)
        if key in nested_dicts:
            result.add(nested_dicts[key])
    return result


my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))

