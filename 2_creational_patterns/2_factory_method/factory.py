## Once you have too many factory methods in a class it might make sense to move them outside the class
## To get in line with the simple responsability principle and separation of concerns

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


class PointFactory:
    # Factory Methods to create Point objects in different Coordinate System
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p = Point(2,3)
    p2 = PointFactory.new_polar_point(1,2)
    p3 = PointFactory.new_cartesian_point(2,3)

    print(p)
    print(p2)
    print(p3)
