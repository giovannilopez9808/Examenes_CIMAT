import numpy as np
N = 6
matrix = np.ones((N, N))
value = 1
for i in range(N):
    value = 1+i
    i = N-i-1
    for j in range(i+1):
        value_j = value+j
        matrix[i, j] = value_j
        matrix[j, i] = value_j
print(matrix)
