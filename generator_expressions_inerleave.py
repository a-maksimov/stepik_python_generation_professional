def interleave(*args):
    return (item for pair in zip(*args) for item in pair)


print(*interleave('bee', '123'))
