import math


class PhanSo2:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def mul(self, other):
        x = self.tu * other.mau + other.tu * self.mau
        y = self.mau * other.mau
        return PhanSo2(x,y)

    def ChuanHoa(self):
        k = math.gcd(self.tu, self.mau)
        self.tu = int(self.tu / k)
        self.mau = int(self.mau / k)

    def output(self):
        print(str(self.tu) + "/" + str(self.mau))


if __name__ == '__main__':
    arr = [int (i) for i in input().split()]
    p = PhanSo2(arr[0] , arr[1])
    p2 = PhanSo2(arr[2] , arr[3])
    p3 = p.mul(p2)
    p3.ChuanHoa()
    p3.output()