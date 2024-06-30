import json


def filter_by_parameter(sequence, parameter, value):
    return list(filter(lambda p: p[parameter] == value, sequence))


with open('food_services.json', 'r', encoding='utf-8') as file:
    restaurants = json.load(file)

set_of_types = {restaurant['District'] for restaurant in restaurants}
set_of_nets = {restaurant['OperatingCompany'] for restaurant in restaurants if restaurant['OperatingCompany']}

max_district = max(set_of_districts, key=lambda d: len(filter_by_parameter(restaurants, 'District', d)))
max_net = max(set_of_nets, key=lambda n: len(filter_by_parameter(restaurants, 'OperatingCompany', n)))

print(f'{max_district}: {len(filter_by_parameter(restaurants, "District", max_district))}')
print(f'{max_net}: {len(filter_by_parameter(restaurants, "OperatingCompany", max_net))}')
