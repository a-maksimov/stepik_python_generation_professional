import csv
from collections import namedtuple
from datetime import datetime

date_format = '%d.%m.%Y'
time_format = '%H:%M'

with open('meetings.csv', 'r', encoding='utf-8') as file:
    fieldnames, *rows = csv.reader(file)
    Person = namedtuple('Person', fieldnames)
    people = []
    for row in rows:
        person = Person(*row)
        people.append(person)

for person in sorted(people,
                     key=lambda p: (datetime.strptime(p.meeting_date, date_format), datetime.strptime(p.meeting_time, time_format))):
    print(person.surname, person.name)
