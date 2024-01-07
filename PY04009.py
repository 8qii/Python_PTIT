
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def mul(self, other):
        return Complex((self.b * other.b) * -1 + self.a * other.a, self.b * other.a + self.a * other.b)


if __name__ == '__main__':
    for t in range(int(input())):
        arr = [int(i) for i in input().split()]
        c1 = Complex(arr[0], arr[1])
        c2 = Complex(arr[2], arr[3])
        c3 = c1.add(c2)
        c4 = c3.mul(c3)
        c3 = c3.mul(c1)
        s = ""
        s += str(c3.a)
        if c3.b >= 0: s += ' + ' + str(c3.b) + 'i, '
        else: s += ' - ' + str(c3.b * -1) + 'i, '
        s += str(c4.a)
        if c4.b >= 0: s += ' + ' + str(c4.b) + 'i'
        else: s += ' - ' + str(c4.b * -1) + 'i'
        print(s)
