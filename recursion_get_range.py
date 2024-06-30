# put your python code here
def get_range(start, stop):
    if start <= stop:
        print(start)
        start += 1
        get_range(start, stop)


get_range(1, 100)