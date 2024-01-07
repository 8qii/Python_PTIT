
class Rectangle:

    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color[0].upper() + color[1::].lower()

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

    def colorr(self):
        return self.color


arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print(r.perimeter(), r.area(), r.colorr(), sep = ' ')
else:
    print("INVALID")