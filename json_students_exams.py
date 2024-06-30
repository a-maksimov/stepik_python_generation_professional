import csv
import json
from datetime import datetime


def filter_by_parameter(sequence, parameter, value):
    return list(filter(lambda p: p[parameter] == value, sequence))


def select_max_by_parameter(sequence, parameter):
    try:
        sequence_max = max(sequence, key=lambda p: datetime.fromisoformat(p[parameter]))
    except:
        sequence_max = max(sequence, key=lambda p: int(p[parameter]))
    return filter_by_parameter(sequence, parameter, sequence_max[parameter])


with open('exam_results.csv', 'r', encoding='utf-8') as file:
    exam = list(csv.DictReader(file))

set_of_student_emails = {item['email'] for item in exam}
best_scores = []
for email in sorted(set_of_student_emails):
    student_by_email = filter_by_parameter(exam, 'email', email)
    student_best_score = select_max_by_parameter(student_by_email, 'score')
    student_best_date = select_max_by_parameter(student_best_score, 'date_and_time')
    best_scores.append(student_best_date[0])

for best_score in best_scores:
    best_score['best_score'] = int(best_score.pop('score'))

with open('best_scores.json', 'w', encoding='utf=8') as file:
    json.dump(best_scores, file, indent=3)
