#!/usr/bin/python3
# This is a matrix multiplication module
matrix_1 = [[1, 2], [4, 5]]
matrix_2 = [[1, 2], [3, 4]]
result_matrix = [[0, 0], [0, 0]]

for i, row in enumerate(matrix_1):
    for j, element in enumerate(row):
        result_matrix[i][j] = element * (matrix_2[i][j])
print(matrix_1)
print(matrix_2)
print(result_matrix)
