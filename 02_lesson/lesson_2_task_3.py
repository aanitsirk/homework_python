import math


def square(side):
    area = side * side

    if side == int(side):
        return area
    else:
        return math.ceil(area)


print('Площадь квадрата со стороной 4: ', square(4))
print('Площадь квадрата со стороной 2.5: ', square(2.5))
print('Площадь квадрата со стороной 4.2: ', square(4.2))
