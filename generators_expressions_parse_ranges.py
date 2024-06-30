def parse_ranges(ranges):
    for r in ranges.split(','):
        yield from range(int(r.split('-')[0]), int(r.split('-')[1]) + 1)


print(*parse_ranges('1-2,4-4,8-10'))