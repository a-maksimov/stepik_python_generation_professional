def get_nums(n=int(input())):
    if n != 0:
        get_nums(int(input()))
    print(n)


get_nums()
