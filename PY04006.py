# from PY04001 import Point
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def output(self):
        a = self.p1.distance(self.p2)
        b = self.p3.distance(self.p2)
        c = self.p1.distance(self.p3)
        if max(a, b, c) * 2 >= (a + b + c):
            print('INVALID')
        else:
            print('{:.2f}'.format(sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4))


a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    tt = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    tt.output()
    i += 6