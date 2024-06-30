from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

new_data = OrderedDict()

rule = False
for _ in range(len(data)):
    key, value = data.popitem(last=rule)
    new_data[key] = value
    rule = not rule

print(new_data)

# data = OrderedDict([data.popitem(last=i & 1) for i in range(len(data))])
