string = 'Sorted12345'

string = sorted(string)

string = ''.join(sorted(string, key=lambda x: (not x.islower(), not x.isupper(), not (x.isdigit() and int(x) % 2 != 0))))
print(string)