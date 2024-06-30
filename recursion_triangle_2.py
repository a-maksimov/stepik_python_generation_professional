def triangle(h):
    if h > 0:
        h -= 1
        triangle(h)
        print('*' * (h + 1))

triangle(5)