import csv


def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as file_read, \
            open('condensed.csv', 'w', encoding='utf-8', newline='') as file_write:
        rows = list(csv.reader(file_read))
        objects = {row[0] for row in rows}
        fields = []
        i = 0
        field = rows[i][1]
        while field not in fields:
            fields.append(field)
            i += 1
            field = rows[i][1]
        writer = csv.DictWriter(file_write, fieldnames=[id_name] + list(fields))
        writer.writeheader()
        for obj in sorted(objects):
            values = [row[2] for row in rows if row[0] == obj]
            data_write = dict(zip(fields, values))
            data_write[id_name] = obj
            writer.writerow(data_write)


condense_csv('data_to_condense.csv', 'ID')
