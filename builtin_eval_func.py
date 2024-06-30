# put your python code here

func = input()
a, b = [int(num) for num in input().split()]

min_val = min([eval(func) for x in range(a, b + 1)])
max_val = max([eval(func) for x in range(a, b + 1)])

print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min_val}')
print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max_val}')
