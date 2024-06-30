import csv


def find_min(row: dict) -> tuple:
    return min(list(row.items())[1:], key=lambda pair: pair[1])


with open('prices.csv', 'r', encoding='utf-8') as file:
    rows_dict = list(csv.DictReader(file, delimiter=';'))
    for row in rows_dict:
        for field in row:
            if row[field].isdigit():
                row[field] = int(row[field])
    min_shop, min_product = min([(row['Магазин'], find_min(row)) for row in rows_dict], key=lambda pair: pair[1][1])
    products = {min_product[0]: [min_shop]}
    for row in rows_dict:
        shop, product = row['Магазин'], find_min(row)
        if product[1] == min_product[1]:
            if shop != min_shop:
                products[product[0]] = products.setdefault(product[0], []) + [shop]

print(f'{sorted(products)[0]}: {sorted(products.get(sorted(products)[0]))[0]}')
#
# for shop in sorted
