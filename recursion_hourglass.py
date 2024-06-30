def hourglass(n, num=0):
    if n > 4:
        print(' ' * (num + num) + f'{num + 1}' * n)
        hourglass(n - 4, num + 1)
    print(' ' * (num + num) + f'{num + 1}' * n)

hourglass(16)

# def bee(n):
#     if n > 0:
#         print(n)
#         bee(n - 1)
#         print(n)
#
# bee(2)