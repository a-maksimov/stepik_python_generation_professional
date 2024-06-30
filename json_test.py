import json

lines = {
         True: 97,
         2: "I've been running for a reason",
         "3": ("I", "could", "never", "retain"),
         4: ["Sweet", "lips", "like", "pink", "lemonade"],
         5.0: "When he's feeling generous he's gonna give me a taste",
         "six": "10"
        }

lines_json = json.dumps(lines)

lines = json.loads(lines_json)


colors = ['black', 'white']

colors_json = json.dumps(colors, indent='-> ')

print(colors_json)

weekdays = {i: day for i, day in enumerate(['Sunday', 'Monday', 'Tuesday'])}

weekdays_json = json.dumps(weekdays, separators=('; ', '-'))

print(weekdays_json)

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

countries_json = json.dumps(countries, indent='   ', separators=(',', ' - '))
print(countries_json)
pass