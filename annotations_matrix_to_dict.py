def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {i + 1: matrix[i] for i in range(len(matrix))}

matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))