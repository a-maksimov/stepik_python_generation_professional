import csv

n = int(input()) - 1

with open('deniro.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    sorting_key = lambda r: r[0].strip("'").split(',')[n] if not (r[0].strip("'").split(',')[n]).isdigit() else int(r[0].strip("'").split(',')[n])
    for row in sorted(rows, key=sorting_key):
        print(*row)

# i = int(input()) - 1
#
# with open('deniro.csv', 'r', encoding='utf-8') as file:
#     data = list(csv.reader(file))
#
# data.sort(key=lambda x: int(x[i]) if x[i].isdigit() else x[i])
# for lst in data:
#     print(*lst, sep=',')
