import json


def filter_by_parameter(sequence, parameter, value):
    return list(filter(lambda p: p[parameter] == value, sequence))


def select_max_by_parameter(sequence, parameter):
    sequence_max = max(sequence, key=lambda p: int(p[parameter]))
    return filter_by_parameter(sequence, parameter, sequence_max[parameter])


with open('food_services.json', 'r', encoding='utf-8') as file:
    restaurants = json.load(file)

set_of_types = {restaurant['TypeObject'] for restaurant in restaurants}

for type_of_restaurant in sorted(set_of_types):
    max_type_of_restaurant = select_max_by_parameter(filter_by_parameter(restaurants, "TypeObject", type_of_restaurant), "SeatsCount")[0]
    print(f'{type_of_restaurant}: {max_type_of_restaurant["Name"]}, {max_type_of_restaurant["SeatsCount"]}')

