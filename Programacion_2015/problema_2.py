def sum_diagonals(matrix):
    results = []
    size_x, size_y = len(matrix[0]), len(matrix)
    for x in range(size_x):
        pos_x = size_x-x-1
        pos_y = 0
        results.append(sum_diagonal(pos_x, pos_y, size_x, size_y))
    for y in range(size_y-1):
        pos_y = y+1
        pos_x = 0
        results.append(sum_diagonal(pos_x, pos_y, size_x, size_y))
    return results


def sum_diagonal(pos_x, pos_y, lim_x, lim_y):
    next = True
    sum_diag = 0
    while next:
        if (pos_x >= 0 and pos_x < lim_x) and (pos_y >= 0 and pos_y < lim_y):
            sum_diag += matrix[pos_y][pos_x]
        else:
            next = False
        pos_x += 1
        pos_y += 1
    return sum_diag


matrix = [[10, 26],
          [12, 20],
          [-5, 4]]

results = sum_diagonals(matrix)
print(results)
