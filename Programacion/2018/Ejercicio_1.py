import numpy as np
N = 4
M = 5
matrix = np.ones((N, M))
value = 1
for i in range(N):
    value = 1+i
    i = N-i-1
    for j in range(M):
        value_j = value+j
        matrix[i, j] = value_j
print(matrix)
