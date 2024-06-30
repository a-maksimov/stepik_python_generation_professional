from calendar import monthrange

year, month = [int(item) for item in input().split()]  # возвращает кортеж (день недели первого дня, кол-во дней в
# месяце)

print(monthrange(year, month)[1])