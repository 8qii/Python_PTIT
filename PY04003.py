import math


class PhanSo1:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def ChuanHoa(self):
        k = math.gcd(self.tu, self.mau)
        self.tu = int(self.tu / k)
        self.mau = int(self.mau / k)

    def output(self):
        print(str(self.tu) + "/" + str(self.mau))


if __name__ == '__main__':
    arr = [int (i) for i in input().split()]
    p = PhanSo1(arr[0] , arr[1])
    p.ChuanHoa()
    p.output()