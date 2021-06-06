def dis_Hausdorff(x, y):
    dis_xy = dis_h(x, y)
    dis_yx = dis_h(y, x)
    dis_max = dis_xy
    if dis_yx > dis_max:
        dis_max = dis_yx
    return dis_max


def dis_h(x, y):
    point_x = x[-1]
    point_y = y[0]
    return calculate_dist(point_x,
                          point_y)


def calculate_dist(x, y):
    dis_x = x[0]-y[0]
    dis_y = x[1]-y[1]
    return (dis_x**2+dis_y**2)**(1/2)


x = [[1, 1],
     [0, 0]]
y = [[1, -1],
     [0, 0]]
print("La distancia de Hausdorff para los conjuntos X, Y dados es {}".format(
    dis_Hausdorff(x, y)))
