def triangle_area(a, b, c):
    s = (a + b + c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5

    return area

triangle_area(8,6,3)

