def print_operation_table(operation, rows, cols):
    for r in range(1, rows + 1):
        row = []
        for c in range(1, cols + 1):
            row.append(operation(r, c))
        print(*[str(num).ljust(2) for num in row])


print_operation_table(lambda a, b: a * b, 5, 5)
