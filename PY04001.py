from math import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_string_format(self, other):
        return '{:.4f}'.format(sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2))

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def Decimal(x):
    return float(x)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance_string_format(p2))
        t -= 1