from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     if system == CoordinateSystem.POLAR:
    #         self.x = a * sin(b)
    #         self.y = b * cos(b)

    # If you want to add a new coordinate system you would have to change both classes, breaks the open-closed principle
    # We can use the Factory Method pattern

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # Factory Methods to create Point objects in different Coordinate System
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p = Point(2,3)
    p2 = Point.new_polar_point(1,2)
    p3 = Point.new_cartesian_point(2,3)

    print(p)
    print(p2)
    print(p3)
