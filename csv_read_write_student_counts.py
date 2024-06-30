import csv

with open('student_counts.csv', 'r', encoding='utf-8') as file_read, \
        open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_write:
    rows_dict = csv.DictReader(file_read)
    fieldnames = [rows_dict.fieldnames[0]] + sorted(sorted(rows_dict.fieldnames[1:], key=lambda c: c.split('-')[1]),
                                                    key=lambda c: int(c.split('-')[0]))
    writer = csv.DictWriter(file_write, fieldnames=fieldnames)
    writer.writeheader()
    for data in rows_dict:
        writer.writerow(data)


# def key_func(grade):
#     number, letter = grade.split('-')
#     return int(number), letter