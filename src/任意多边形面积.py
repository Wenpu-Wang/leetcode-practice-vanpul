# 求任意多边形面积公式：https://zhuanlan.zhihu.com/p/110025234

def get_polygon_area(points):
    area = 0
    # x_n = x_0, y_n = y_0
    # + x_n-1 * y_n - x_n * y_n-1 = + x_n-1 * y_0 - x_0 * y_n-1
    area += points[-1][0] * points[0][1]
    area -= points[0][0] * points[-1][1]
    # 0 ~ n-1
    for i in range(len(points)-1):
        area += points[i][0] * points[i+1][1]
        area -= points[i+1][0] * points[i][1]
    area = 0.5 * abs(area)
    return area


# 面积30
li = [[3, 4], [5, 11], [12, 8], [9, 5], [5, 6]]
res = get_polygon_area(li)
print("area:", res)
