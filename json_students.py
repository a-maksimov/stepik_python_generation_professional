import json
import csv

with open('students.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

selected_students = []
for student in students:
    if student['age'] >= 18 and student['progress'] >= 75:
        selected_students.append({'name': student['name'], 'phone': student['phone']})

selected_students.sort(key=lambda x: x['name'])

with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'phone'])
    writer.writeheader()
    writer.writerows(selected_students)