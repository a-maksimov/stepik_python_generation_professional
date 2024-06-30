# put your python code here

string = input()

o = eval(string)

if isinstance(o, list):
    print(o[-1])
elif isinstance(o, tuple):
    print(o[0])
elif isinstance(o, set):
    print(len(o))