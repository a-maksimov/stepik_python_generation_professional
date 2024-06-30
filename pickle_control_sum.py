import pickle

filename = input()
control_sum = int(input())

with open(filename, mode='rb') as file:
    obj = pickle.load(file)
    if isinstance(obj, list):
        ints = list(filter(lambda i: isinstance(i, int), obj))
        test_sum = min(ints, default=0) * max(ints, default=0)
    elif isinstance(obj, dict):
        ints = list(filter(lambda i: isinstance(i, int), obj.keys()))
        test_sum = sum(ints, start=0)
print('Контрольные суммы совпадают' if control_sum == test_sum else 'Контрольные суммы не совпадают')
# max(iterable, key=, default= )