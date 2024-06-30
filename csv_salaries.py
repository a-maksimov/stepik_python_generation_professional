import csv

with open('salary_data.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    companies = {}
    for row in rows:
        companies.setdefault(row['company_name'], []).append(int(row['salary']))

for company in sorted(sorted(companies), key=lambda c: sum(companies.get(c)) / len(companies.get(c))):
    print(company)
    
