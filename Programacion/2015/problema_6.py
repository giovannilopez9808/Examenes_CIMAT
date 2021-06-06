def solve(a, b, c, d, e, f):
    div = b*d-a*e
    x = None
    y = None
    up_x = b*f-e*c
    up_y = c*d-a*f
    if div == 0:
        solution_type = 0
    else:
        x = up_x/div
        y = up_y/div
        solution_type = 1
    if up_x == 0:
        solution_type = 2
    solution = "El tipo de solución es {}\n".format(solution_type)
    solution += "La solucion de x es {}\n".format(x)
    solution += "La solucion de y es {}".format(y)
    print(solution)


a = 2
b = 1
c = 5
d = 1
e = 1
f = 3
solve(a, b, c, d, e, f)
