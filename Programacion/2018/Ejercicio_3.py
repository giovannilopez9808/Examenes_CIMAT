import numpy as np


def count_neighbours(matrix, i, j):
    sum_value = 0
    for k in [-1, 1]:
        pos_i = i+k
        pos_j = j+k
        if pos_i >= 0 and pos_i <= 2:
            sum_value += matrix[pos_i, j]
        if pos_j >= 0 and pos_j <= 2:
            sum_value += matrix[i, pos_j]

    return sum_value % 2


# matrix = np.array([[1, 1, 1],
#                    [1, 0, 0],
#                    [0, 0, 1]])
matrix = np.array([[1, 0, 1],
                   [0, 0, 0],
                   [1, 0, 1]])
matrix_copy = np.copy(matrix)
run = True
count = 0
while run:
    for i in range(3):
        for j in range(3):
            matrix_copy[i, j] = count_neighbours(matrix,
                                                 i,
                                                 j)
    if np.sum(matrix_copy) == 0:
        run = False
    else:
        matrix = np.copy(matrix_copy)
        count += 1
print("-"*20)
print("Para la matriz\n{}\nSe obtuvo k(f(g))={}".format(matrix,
                                                        count))
print("-"*20)
