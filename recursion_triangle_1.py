def triangle(h):
    if h > 0:
        print('*' * h)
        h -= 1
        triangle(h)