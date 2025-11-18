def transpose_matrix(matrix):
    # Using zip(*) to transpose
    transposed = [list(row) for row in zip(*matrix)]
    return transposed

# Example
matrix = [[1, 2], [3, 4], [5, 6]]
result = transpose_matrix(matrix)
print(result)
